# A11.04 Schema induction: cross-check and critique

Cross-checker pass. Inputs: evidence_a.jsonl (31 lines), evidence_b.jsonl (29), evidence_c.jsonl (26). Output: claims.jsonl (23 claims, A11.04-K01 to K23).

Claim status count: established 7 (K01, K02, K05, K08, K11, K13, K22), contested 2 (K03, K17), single-source 14. Refuted: none.

## 1. Numbers re-opened this session

Re-read from the source text (PDF or arXiv HTML), not from the evidence lines:

| # | Number | Source re-opened | Result |
|---|---|---|---|
| 1 | Gick and Holyoak Exp 4: 45% vs 21% pre-hint, 80% vs 53% total, G2 6.35 and 8.36 | gwern PDF text | Confirmed |
| 2 | GH83 Exp 4 good schema 91% pre-hint; mix 21% good, 59% poor | same | Confirmed (91% in text; the 10/11 cell not rechecked) |
| 3 | GH83 Exp 5: principle with two analogs 62% vs 40% pre-hint, 82% vs 67% total | same | Confirmed. Added: in Exp 5, good schemas reached the solution 94% vs 53% for poor (with-principle group, G2(4)=13.0, p<.02); without a principle the link was not significant (p=.14). Not in the evidence file. |
| 4 | GH83 Exp 6: diagrams 57% vs 37% pre-hint, 92% vs 79% total | same | Confirmed |
| 5 | GH83 Exp 2 G2(2)=2.05, p=.36 | same | Confirmed |
| 6 | Step-back MMLU table: PaLM-2L 73.2/81.8, GPT-4 CoT 82.9/85.3, step-back 84.5/85.6; error fix 20.5% vs new 11.9%; over 90% of errors in Reasoning | arXiv 2310.06117 PDF | Confirmed. GPT-4 SDs (0.5 to 1.4) show the +1.6 and +0.3 gaps over CoT are near or inside noise. |
| 7 | Buffer of Thoughts GPT-4 table (82.4, 86.4, 93.6, 89.2, 52.4, 100.0; Meta-prompting 67.0/57.2/78.2) and "12% of the cost" | arXiv HTML 2406.04271 | Confirmed. Column order is GPT4, GPT4+CoT, Expert, PAL, ToT, GoT, Meta-prompting, BoT. Note GoT is 51.4 on Checkmate and 73.2 on Game of 24, so ToT is not always the strongest baseline. |
| 8 | Alfieri et al. 2013: d=.50, CI [.44,.56], 57 experiments, 336 tests; four reliable moderators | OpenAlex abstract of the journal paper | Confirmed. The d=.60 in a23 and b18 is the earlier conference report. Use .50. |
| 9 | Gentner, Loewenstein, Thompson 2003: Exp 1 47% (15/32), Exp 2 48% vs 19% chi2=11.85, Exp 3 90/70/55/37% | gwern-style PDF from Northwestern | Confirmed. Added: in Exp 3, "ideal contract" answers were 73% and 68% for guided and compare groups vs 48% and 47% for separate and baseline, and full schema articulation was 35% vs 8%. |
| 10 | Yasunaga analogical prompting: GSM8K 75.0 to 77.8, MATH 33.0 to 37.3; K table 76.1/34.8 at K=1 up to 77.8/37.1 | arXiv 2310.01714 PDF | Confirmed with a caveat: the K table is garbled in text extraction, so which row is which K is inferred. The text itself says K=1 underperforms and K=3 to 5 is best. Gain is real but small (+2.8 GSM8K). |
| 11 | Puranam et al. human numbers: factory 6.3% to 8.7%, HR 20.3% to 37% (4/46, 17/46) | arXiv 2505.00603 PDF text | Confirmed. GPT-4 15/15 and 1/15 counts not rechecked. |
| 12 | Self-Discover: 87.5% structures correct (175 of 200), 74.7% of failures computation, 10 to 40x fewer calls, BBH +7 and +6 over CoT and PS | arXiv HTML 2402.03620 | Confirmed, with one correction below. |

## 2. Corrections made

1. **c10 (Self-Discover) said gains concentrate in algorithmic tasks.** The paper says the opposite: "performs best on tasks requiring world knowledge" and the gain on algorithmic tasks is "moderate". Claim K23 states the correct direction. The evidence line c10 still carries the old wording and should be treated as wrong on this point.
2. **Meta-analysis effect size.** Use d=.50 (journal, 2013), not .60 (2011 conference abstract). K09 says so.
3. **a15 and a13 give two different compare vs advice rates** (54% vs 13% from earlier work; 64% vs 23% in the 2000 paper). These are different studies, not an error, but they should not be pooled.
4. **a24 vs c24 (SAGE).** a24 mixes up the two experiments (it lists prototype 62% with a 77% ALIGN peak, plus the text "prototypes and examples both 55%"). c24 sorts this out: sketch task examples 55%, prototypes 55%, ALIGN 62%; geospatial ALIGN peak 77%, prototypes 62%, examples 53%. Use c24. K21 follows c24.
5. **a27 vs c02 on TimeQA baseline.** a27 lists 38.1 next to CoT, c02 lists 41.5 as the base. Both are right for different arms (CoT 38.1, base 41.5). Use 41.5 for the base.
6. **c16 compares with "Gick and Holyoak Exp 2: 29% no hint, 50% with hint".** Our own read of GH83 Exp 2 gives 29% pre-hint but 79% total with hint, not 50%. The 50% figure may come from a different hint definition in Puranam et al. Not resolved; do not quote the 50%.
7. **Agent_relevance in a few lines** (c21 "cheap rule-based version gets nearly all the gain") is stronger than the data: it is one site-set on WebArena with GPT-4.

## 3. Contradictions between sources

- **Is separate-case study useless?** Loewenstein 2003 (a19): separate 22% vs baseline 23%. Gentner 2003 Exp 3 (a18): separate 55% vs baseline 37%. Different tasks (teams vs face-to-face pairs) and baselines (23% vs 37%). Marked contested (K03).
- **Does a stated principle help?** GH83: no with one analog, yes with two. Gentner group (cited, not opened): naming the principle added nothing. Alfieri: principles after comparison help more than before. These can all be true, but only the GH83 data are opened. Student replication (b20) seen only as a snippet.
- **Do LLMs do analogy?** Webb 2023 (c12): GPT-3 above human mean. Hodel and West, Lewis and Mitchell, Stevenson (c13, c14, c15): collapse under counterfactual or unfamiliar alphabets. Contested (K17); Webb's authors dispute the contamination reading.
- **Does abstraction matter for strong models?** Step-back: large on PaLM-2L, near zero over CoT on GPT-4. Buffer of Thoughts: huge on GPT-4 for Game of 24 and Checkmate. The difference is template content, not abstraction alone: BoT supplies a worked procedure, step-back supplies only a principle.
- **Does comparison help in delayed/changed contexts?** Catrambone and Holyoak 1989: floor effect at one week unless heavily scaffolded; Gentner 2009 shows comparison can raise recall of an earlier case (27% vs 6%) but the absolute rate is low.

## 4. Weak spots

- **Almost all human evidence is small and old.** GH83 cells are 15 to 50; Catrambone 1989 cells about 19; student/undergraduate samples; one problem (radiation) carries most of the induction literature.
- **Same-lab clustering.** Gentner, Loewenstein, Thompson, Kurtz, Forbus are one network; the "3 independent sources" for K22 are partly the same group. Only Alfieri (meta-analysis) and Hattikudur are outside it.
- **Meta-analysis read from the abstract only.** No per-moderator effect sizes. The "principle after" and "find similarities" findings are therefore directional only.
- **No LLM study compares at equal tokens.** Step-back, BoT, Self-Discover, AoT, analogical prompting all add tokens (AoT about 80% more). Our guardrail G7 cannot be checked from any of them.
- **BoT, Self-Discover, AWM and ReasoningBank use the authors' own benchmarks and in-family templates.** Leakage between template and test items is not excluded.
- **No LLM study tests the human recipe**: showing two cases, forcing alignment, deriving a rule, then transferring to a new surface form. The nearest are Hypothesis Search (rule from many examples) and analogical prompting (self-made cases).
- **Evidence from no paper about varied-case choice.** GH83's similar vs dissimilar contrast is a non-significant trend.
- **Failed replications are thin.** Only the Catrambone delay result and Hattikudur boundary were opened. The two recent replications (b20, b21) are snippet-only and unverified.

## 5. Seen only in snippets or not opened

- b20 (student replication of Gick and Holyoak, 2023): search summary only, no numbers. Authors and title not verified.
- b21 (replication of Kurtz and Loewenstein 2007): search summary only.
- a15 (Loewenstein, Thompson, Gentner 1999): cited secondhand.
- a21 to a23, b18, b19: abstracts only.
- Thompson, Gentner, Loewenstein 2000 PDF could not be fetched this pass; the 14/22 vs 5/22 numbers rest on the earlier agents' read.
- Catrambone and Holyoak 1989 not re-opened (no free PDF found quickly); numbers rest on the earlier read.
- GPT-4 counts in Puranam (1/15, 15/15), Lewis and Mitchell exact numbers, and all figure-only ablations (BoT figures 7 to 9, AoT).

## GAPS

1. Does the human recipe (two worked cases, forced alignment, derived rule, new instance) improve a language model at equal tokens against one case, against plain reasoning, and against self-generated examples? No paper tests this. This decides whether S2 should contain an induction step at all.
2. At equal tokens, do step-back, abstract-plan-first (AoT prompting) and Self-Discover beat a short plain answer on a strong current model? All the reported gains are on weaker or older models with unequal token use; GPT-4 gains over CoT were within noise on MMLU.
3. How many cases are enough for a model, and does the choice of pair (similar, dissimilar, near-miss contrast) matter? Humans: two beat one, 3 helped after a delay, similar vs dissimilar not significant. Models: K=1 worst, K=3 to 5 stable (+1 to +3 points). No work on contrast pairs for LLMs beyond SAGE-style near-misses on tiny symbolic data.
4. Does the written schema quality predict transfer in models the way it does in people (91% vs 30%)? Needs a check on whether a model's own rule statement, scored on held-out instances, predicts later success, and whether that holds under the hypothesis-search finding that summarising loses 26% of correct rules.
5. Is a stored abstraction safe across surface forms? Lewis and Mitchell, Hodel and West, Stevenson show collapse on altered symbols. Do current reasoning models keep a rule when only the surface changes, and does a rewording step (the target-wording rescue in Catrambone 1989) restore retrieval?
6. How much of the memory gain (BoT, AWM, ReasoningBank) is abstraction versus reuse of validated routines? AWM's rule-based induction matched the LM version (35.6 vs 35.5). Needs an ablation: raw solved cases vs code-built routines vs model-summarised templates, with a held-out task class.
7. What are the per-moderator effect sizes in Alfieri 2013 (principle after vs before, find similarities vs differences, lag)? Full paper and its tables must be read; the abstract gives direction only.
8. Do the two recent human replications (Gick and Holyoak student replication 2023; Kurtz and Loewenstein replication) hold, and with what numbers? Both are snippet-only here.
9. When should the agent skip induction? Step-back gave zero on StrategyQA and GSM8K, Hattikudur found benefit only for some learners, and abstraction rarely fails. A gate rule based on plain pass rate and principle recall need, for S0, is untested.
10. Can a model be shown two cases and told to compare them without using the principle on the cases themselves? Puranam found GPT-4 used the correct source 1/15 unprompted and about 50% precision when hinted. Is that fixed by forcing a causal-structure check (G3)?

## Gap search results (evidence_d.jsonl d01 to d19; claims K24 to K33 added)

Search note: WebSearch hit its session budget on the first calls. Semantic Scholar, OpenAlex and the arXiv API were then rate-limited or out of budget after a few queries. Work continued by direct PDF download of papers known by id and by fetching a few pages. Coverage of new 2025 to 2026 literature is therefore thin, and the absence of a paper below means "not found with the tools that worked", not "does not exist".

Status by gap

1. Human recipe versus plain, one case, self-made cases at equal tokens. OPEN. Nothing tests it. Nearest are LEAP (d15) and contrastive CoT (d16), which compare wrong with right, and Kurtz and Loewenstein (d12), which suggests comparing two problems under one shared-solution instruction. DeepSeek reports that few-shot examples degrade R1 (d02, no numbers), so the first S2 test must include a zero-shot arm. See K26, K27.
2. Step-back, abstract-plan-first and Self-Discover at equal tokens on a strong model. OPEN, with better priors. No token-matched test exists. Plain CoT adds about +3 points or less to o3-mini and o4-mini and -3.3 to Gemini Flash 2.5 (d01). Chain of Draft gives the right control: about 40 tokens keep 91 of 95 points on GSM8K (d03). Self-Discover re-opened: on GPT-4 the gain over CoT is +6 BBH but only +2 MATH (d05). See K24, K25, K23.
3. How many cases, which pair. PARTLY CLOSED. K=1 worst and K=3 to 5 stable for self-made cases (d17); for retrieved agent memory 1 is best and 4 is worse (d07). Not closed: similar versus different versus near-miss pairs for models. Correction to the gap text: contrast work for LLMs does exist (LEAP, contrastive CoT), but it is wrong-versus-right, not near-miss structure pairs. See K28.
4. Does a model's own rule quality predict transfer. OPEN, reframed. No paper scores a model's written rule and relates it to held-out success. What exists points to execution as the check. In ARC a train-passing program almost always passed the test (d10); in list functions 45.4 percent did not (Parab, c19 and c20). The two disagree, so claim K20 is now "contested". The "26 percent of correct rules lost by summarising" figure belongs to the list-function study only; in ARC the loss was 30 versus 33 tasks. See K29.
5. Is a stored abstraction safe when only surface form changes. PARTLY ANSWERED, still open for current models. GPT-4 digit matrices: 0.813 original, 0.790 symbols, 0.480 moved blank (d13). o1-preview lost 17.5 points from one irrelevant clause (d14). No paper tests altered alphabets on a current reasoning model. No paper tests a rewording rescue with a model. Catrambone and Holyoak 1989 still not re-opened. See K30.
6. Abstraction versus reuse of validated routines. MOSTLY CLOSED as a picture, not as a clean ablation. Ladder in ReasoningBank: raw 42.1, workflows 44.1, distilled 48.8 (d07). Dynamic Cheatsheet: raw retrieval 6, curated code memory 93 to 99 on Game of 24 (d08). AWM: rule-built matches model-built on WebArena, trails on Mind2Web (d06). PlugMem: structuring adds 10 to 12 points (d09). All use authors' own benchmarks, and each change also alters something else (failures, instructions, indexing). The clean three-arm test on a held-out class is not published. K14 changed to "contested"; K31 added.
7. Alfieri et al. 2013 per-moderator effect sizes. OPEN. Full text is paywalled and no free copy was reachable (journal 403, no repository copy found). Claim K09 stays single-source and abstract-only. No email was sent to any service.
8. The two human replications. PARTLY CLOSED. b20 is Boyce, Mathur and Frank (2023), a student-replication project; the FORRT atlas marks the Gick and Holyoak replication successful and says the verbal statement helped transfer from a pair of analogs (d18). No N or effect size found. b21 (a 2017 replication of Kurtz and Loewenstein) could not be found at all and should be treated as unverified or wrong. The original Kurtz and Loewenstein text was opened (d12). See K32.
9. When to skip induction. OPEN as a rule, with indirect support. Reasoning models gain little from extra prompting (d01); structure pays only for large models on hard tasks (d04); LEAP is near zero on strong-model math (d15). The gate is written down as an untested design inference (K33).
10. Can a forced causal-structure check fix source choice. OPEN. Re-reading Puranam et al. with tables (d11): GPT-4 chose the right source 0 of 15 unprompted, and with a hint claimed both sources almost every time (precision 0.50 to 0.52). The authors did not test a causal check. This also resolves the c16 puzzle: the 29 and 50 percent figures in that paper are Gick and Holyoak 1983 Exp 2 (8/28 and 14/28), cited by the authors, so c16's "50% with hint" belongs to the 1983 study. K18 rewritten.

Corrections made to earlier notes
- K23 and c10: confirmed again that Self-Discover gains are largest on world-knowledge tasks and moderate on algorithmic ones. MATH gain over CoT is +8.5 on PaLM 2-L and only +2 on GPT-4.
- K14: the AWM rule-versus-LM tie holds on WebArena only; on Mind2Web the model-written version was better (task success 4.8 versus 2.0).
- K20: split into the two studies; status changed to contested.
- K04: student replication now identified, no numbers.
- K18: human and model numbers corrected; c16 discrepancy explained.

New idea worth testing
- Kurtz and Loewenstein (d12): comparing two unsolved problems under a shared-solution instruction matched or beat comparing two solved stories (51 and 40 percent against 38 and 35). An operator that writes a sibling problem and solves both under one strategy is cheap and has no LLM test yet (K26).

Still open after this pass: gaps 1, 2 (token-matched), 4, 7, 9, 10; gap 5 for current reasoning models; gap 3 for pair choice. Suggested next step is to run the equal-token arms in our own harness rather than search further, because the literature does not contain them.

New caveats on the new evidence
- Several 2026 papers (StyleBench, ReasoningBank, PlugMem) are preprints or very recent and use the authors' own benchmarks. Text layers of several tables were garbled; only readable rows are quoted.
- Chain of Draft, Self-Discover, LEAP and contrastive CoT use 2023 to 2024 models and unequal prompt lengths.
- d19 (Zenodo preprint) is abstract-only; d18 was read through a summarising fetch tool.
