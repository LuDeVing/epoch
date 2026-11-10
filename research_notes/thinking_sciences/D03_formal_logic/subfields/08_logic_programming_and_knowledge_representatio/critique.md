# D03.08 Logic programming and knowledge representation: cross-check critique

Checker re-opened the full text (arXiv PDFs, pdftotext) of Logic-LM, LINC, ProverQA, Ishay et al., SatLM, RuleTaker, Sprague et al. and Faithful CoT. PDFs were deleted after extraction.

## Numbers re-checked (10 groups)
1. Logic-LM Table 2 (all three models) confirmed cell by cell. GPT-4: 77.40/98.79/83.20 (PrOntoQA), 52.67/68.11/79.66, 69.11/70.58/78.92, 71.33/75.25/87.63, 33.33/35.06/43.04.
2. Logic-LM depth gains +7.1, +5.0, +12.7, +20.0, +39.4 at depth 0,1,2,4,5 confirmed (text says 0,1,2,4,5; the c04 note about "<=3" is the figure caption only).
3. Logic-LM Table 3 executable rates confirmed (GPT-4: 100, 99.0, 79.9 FOLIO, 100, 32.6 AR-LSAT; refinement FOLIO 79.9 to 85.8, AR-LSAT 32.6 to 39.8; Exe_Acc FOLIO 80.4 to 79.9).
4. LINC Figure 3 confirmed: FOLIO StarCoder+ 56.0 vs 41.8, GPT-3.5 62.6 vs 54.9, GPT-4 CoT 75.3 vs LINC 72.5, p=0.58; ProofWriter 96.4 and 98.3. 57% Uncertain, 93% precision, 38% syntax errors confirmed in text.
5. SatLM confirmed: GSM-SYS 69.4 greedy and 80.9 SC, GSM 84.8 SC, LSAT 37.4, BoardgameQA 80.7, selective 77% vs 45%. Exemplar-set robustness (Table 7) also seen: SATLM wins on GSM-SYS in all three sets.
6. SatLM ablation: SatNoSolver is 26.6/23.7/40.7 (GSM-SYS/GSM/CLUTRR) vs STANDARD 21.0/22.2/41.2 (text layout garbled, rows re-paired by triple order). SatCoTSolver 54.5/63.2/48.9. The "about standard" claim holds, but SatNoSolver is 5.6 points above standard on GSM-SYS.
7. RuleTaker confirmed: 81% flip = 16654/(16654+3895); D2 model 71.1% at depth 3, D3 model 97.6% at depth 5 (same paper, same sentence).
8. ProverQA confirmed: GPT-4o CoT 94.20/79.40/50.00; Claude-3.5-Sonnet 95.20/83.60/56.40; standard prompting GPT-4o 87.20/68.60/46.20.
9. Ishay et al.: zero-shot GPT-4 12%/21% (train/test), few-shot 6%/7%, GPT-3 ASP 86/81, GPT-4 ASP 92/92 confirmed.
10. Sprague appendix: FOLIO GPT-4o 79.8 vs 62.6, Gemini 1.5 Pro 73.9 vs 74.4 confirmed as numbers; which column is CoT was not confirmed from a header (assumed CoT first).

## Corrections
- c01/b01 said Logic-LM beat standard and CoT on all five datasets with GPT-3.5. Wrong against CoT: ChatGPT PrOntoQA is Logic-LM 61.00 < CoT 67.80. (Beats standard on all five.) text-davinci-003 is also fine (85.0 vs 83.0).
- a18 said Faithful CoT "best on 8 of 10". The abstract says better than CoT on 9 of 10 (b10, c12 correct).
- b27 paired figure numbers 66.7/79.4/79.9/85.3 as rounds of one model. They are two models: GPT-3.5 66.7 to 79.4 and GPT-4 79.9 to 85.3 executable rate (before and after refinement). Table 3 gives 85.8 for GPT-4; the 85.3 vs 85.8 gap is inside the paper and unexplained.
- b22 said the 71.1 and 97.6 depth figures came from different training mixes. They are the D2 and D3 models of one experiment.
- b15 said strong models fall "near chance" on ProverQA hard. 50.0 to 56.4 is not near chance if labels are three-way (chance 33%); chance level of the hard split was not verified. Treat as "about 50-56%".
- c06 vs a20: Logic-LM++ GPT-3.5 FOLIO Logic-LM is 62.80 in one table and 62.74 in Logic-LM's own. Rounding level only.
- Logic-LM++ 18.5/12.3/5% averages were not recomputed.

## Contradictions between sources
- FOLIO, GPT-4: Logic-LM 78.9 vs CoT 70.6 (solver wins) against LINC 72.5 vs CoT 75.3 (CoT wins, not significant). Different setup (CoT fallback on 20.1% failures, 10-vote majority, subsets). Not controlled; K24.
- Formal wording: DeBERTa HardSymbolic 58.5% vs OWL proofs under 8% drop (K15). Different tasks and models (fine-tuned vs prompted reasoning models).
- ASP: agent loop saturates (ASP-Bench) vs one-shot semantic failure (BLAST, 17 of 21 flawed). Different conditions, plus ASP-Bench is saturated and prompt-tuned (K19).
- Sprague: CoT hurts or does nothing for some models on FOLIO yet Logic-LM treats CoT as a competitive baseline; model dependence.

## Weak spots
- Almost all LLM evidence is 2023 models (code-davinci-002, GPT-3.5, GPT-4 early). Only 2025-26 items: ProverQA (prompting only), OntoURL (open models), OWL proofs, ASP-Bench, BLAST (graph problems, approximate heatmap numbers).
- Benchmarks are mostly synthetic (PrOntoQA, ProofWriter, CLUTRR); FOLIO has annotation noise (LINC and ASP papers both note it).
- Solver gains reported with fallback to CoT (Logic-LM) mix two methods.
- Several effects are single-paper: the proof-planning finding (Saparov), faithfulness (Lyu), modules (Yang et al.), complementarity (LINC).
- No paper compares solver routes at equal token cost. Cost in tokens and calls is almost never reported; this matters for our equal-token rule.
- Primary founding papers (van Emden-Kowalski 1976, Clark 1978, Gelfond-Lifschitz 1988, Brachman-Levesque 1984, DL Handbook) were not opened. K02 and K03 rest on memory and citing texts.
- No human study; no replication of the Kowalski logic/control claim beyond the author's own papers.

## Seen only in snippets or figures
a04, a05, a06, a24, a25 not opened. PrOntoQA ontology effect (b21) values only in a figure. DL-Lite F1 cells (b16, b25) not extracted. BLAST numbers read from a heatmap. ProofWriter table cells (a09, c19) are abstract-level only. ChatLogic (c16) table pairing inferred from layout.

## GAPS (most decision-relevant first)
1. At equal tokens, does a solver route (rules to Prolog/Z3/ASP) beat CoT with current frontier models (2025-26) on FOLIO, ProverQA hard and AR-LSAT? Almost all evidence is from 2023 models.
2. What is the real token and call cost of translate-and-solve, including retries, refinement rounds and CoT fallback, compared with CoT?
3. How to catch semantic mistranslation without a human: does round-trip back-translation, test cases or a second independent translator raise accuracy beyond the +5% of Logic-LM++? Does it work without an LLM judging its own edit (G5)?
4. Does an ensemble or disagreement trigger (solver arm vs CoT arm) beat either alone? LINC suggests low error overlap (0.14-0.22) but nobody tested it.
5. When should the agent route to a solver at all? Can depth, interdependence or constraint count be estimated from the problem text well enough to gate it (CoT wins on shallow synthetic items)?
6. Is the benefit retained on open-ended, non-benchmark tasks where rules are implicit and facts missing (LINC lost implicit facts like Person(Harry))? Any evidence on defeasible or default rules, not just classical FOL?
7. Does a reusable verified rule-module library (Yang et al.) transfer to new domains, and what does building one cost relative to Cyc-style hand work?
8. Which rule fragment (Datalog, Horn, ASP, decidable DL) should S2 use? No paper compares fragments for LLM translation accuracy and solver time-outs head to head.
9. How do formal wording and symbol names affect LLM accuracy (DeBERTa 58.5% vs OWL under 8%)? Is the prompted-model result robust across models?
10. Was the "CoT vs direct" direction on FOLIO in Sprague et al. correctly read, and does it hold for current reasoning models with long internal chains?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01 to d20, all opened). New claims K26 to K33; K05, K07, K15, K18, K19, K23, K25 got extra evidence. The search budget ran out after four WebSearch calls (the shared limit), and the arXiv, Semantic Scholar and OpenAlex APIs rate-limited, so some gaps got no new sources.

| Gap | State | What we now know |
|---|---|---|
| 1. Solver vs CoT at equal tokens, frontier models | Partly closed | Constraint-heavy tasks: yes, even for o4-mini, R1 and Gemini 2.5 (51.3 to 78.0 mean, Ishay and Lee 2026, d07). Shallow deduction and FOLIO: CoT wins for GPT-4o and open models (d01, d03). Still missing: any reasoning-model run on FOLIO, ProverQA hard or AR-LSAT with a solver arm. Equal-token matching is not done in any paper. VERUS-LM beats Logic-LM on AR-LSAT (68.4 vs 23.4) but with GPT-4 (d05). |
| 2. Real token and call cost | Partly closed | Mean 2.18 revisions, 7.7 tool calls on hard ASP items, 6 to 26 calls per round-trip repair, up to about 622k input tokens on one hard item (d02, d08, d12, d19). No paper gives tokens per correct answer for solver vs CoT on FOLIO-type items. |
| 3. Catching mistranslation without a human | Partly closed | Round-trip equivalence with an SMT solver is a gold-free detector: 44.7% to 85.3% equivalent after repair; 93% vs 73% faithful by human check on 25 rules (d12, d13). LLM self-approval has 5 to 37% false accepts (d09), which supports G5. A prover-based partial fix cut errors 45 to 72% on a synthetic set (d14). No test of test cases or a second independent translator, and no comparison with the +5% of Logic-LM++. Stays open for those two. |
| 4. Ensemble or disagreement trigger | Open | No paper tests solver-vs-CoT agreement. Closest is NSCoT (CoT then FOL), which still trailed CoT (d03). K23 stays single-source. |
| 5. Gating by depth, interdependence, constraint count | Mostly open | Only signals: He and Wang's pattern (d01) and a BERT classifier for inference type, 92.6% (d06). No router tested against always-solver or always-CoT. |
| 6. Open-ended tasks, implicit rules, defaults | Partly closed | Implicit rules get lost in translation (d20, plus LINC's lost Person(Harry)). ASP handles default and exception tasks far better than SMT (92.9 vs 35.8 skeptical, d10). But frontier models already do explicit defeasible rules with stated priority (BoardgameQA 84.7 baseline vs 82.4 ASP, d11). No test on truly open-ended text with missing facts. |
| 7. Reusable verified rule modules | Open, one hint | Ishay and Lee say self-correction replaces hand-made modules (compact guide 73.1 vs none 61.4; per-task modules are not needed on their sets, d10). No transfer study of Yang et al.'s modules and no build-cost figure versus Cyc. |
| 8. Which rule fragment | Partly closed | Prompted accuracy: FOL 63.92, NLTK 61.44, ASP 56.40, Pyke 44.55 on shallow sets (d15). SMT beats ASP on plain puzzles, ASP beats SMT on defaults (d10). Datalog, plain Horn and decidable DL fragments still untested for LLM translation and time-outs. |
| 9. Formal wording and symbol names | Partly closed | Prompted models drop 13 points when predicate names are enumerated (58.42 to 45.49, d15). The DeBERTa 58.5% vs OWL under-8% conflict (K15) is still not settled across prompted models; K15 stays contested. |
| 10. Sprague FOLIO column order; CoT for reasoning models | First part closed | Table 7 header lists zero-shot CoT accuracy first, then direct answer (d18), so GPT-4o 79.8 vs 62.6 is CoT vs direct. Whether CoT still helps FOLIO for reasoning models is unmeasured. |

Corrections and cautions for earlier claims:
- ProverQA "near chance" for hard stays unverified: the paper text read does not give the label mix (d17).
- The ProverQA hard-split CoT gain is only +3.86 points on average, which fits the idea that a different route is needed there.
- The Ishay and Lee baselines are the model alone, not a token-matched CoT. Treat the 51.3 to 78.0 gain as an upper bound on the solver advantage.
- Table text for He and Wang, VERUS-LM and Bansal was garbled by PDF extraction; only rows that could be read by position were used, and the evidence lines say so.

Top remaining questions for the build: (a) run a reasoning-model CoT arm against a solver arm on FOLIO, ProverQA hard, AR-LSAT with logged tokens; (b) test agreement of the two arms as a trigger; (c) compare round trip, test cases and a second translator for false-accept rate.
