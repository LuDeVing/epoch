# Critique: D07.06 Computational reconstruction of discoveries

Cross-check done by re-opening arXiv PDF text for 8 sources (LLM-SRBench, NewtonBench, SR-Scientist, LaSR, AI Feynman, FIRE-Bench, DiscoveryWorld, DiscoveryBench). SRBench and LLM-SR could not be downloaded as PDF this session (only the SRBench abstract was read, via the arXiv API). 26 claims are in claims.jsonl (K01-K26).

## Numbers re-checked

Confirmed as written:
- LLM-SRBench: 239 problems; LLM-SR GPT-4o-mini 31.53 symbolic / 39.64 Acc0.1 on LSR-Transform; direct prompting GPT-4o-mini 7.21; Llama 3.61; GPT-3.5 2.10; PySR 8.11 / 56.76; LLM-SR Llama-8B 30.63 / 38.55; material science LLM-SR GPT-4o-mini 20.24 / 88.28; GPT-4o judge agreement 94.6 percent.
- NewtonBench: 324 tasks; GPT-5 75.9, Gemini-2.5-pro 65.4; hardest setting 40.3 and 16.7; noise 0.0001 gives 12 to 16 percent loss; GPT-4.1 5.8 to 18.9 with code.
- SR-Scientist: 63.57 / 49.35 (GPT-OSS-120B); ablation Table 3 exactly as in a18, a19, c17; footnote "nearly 50%" of LSR-Transform near-solved after first iteration; "6% to 35%" margin.
- LaSR: 59 (PySR) and 72 (LaSR GPT-3.5 p=1%); 67/69/71 with Llama3-8B; other baselines 20, 24, 26, 23, 40, 38.
- AI Feynman: 100 vs Eureqa 68 percent on Feynman; 90 vs 15 on bonus; 66.7 vs 48.9 on non-physical functions.
- FIRE-Bench: Claude Code F1 46.7 +- 23.4; median CV 0.37; contradictory plus unrelated 76.4 to 95.0 percent.
- DiscoveryWorld: ReAct completion 0.38 / 0.18 / 0.18 and knowledge 0.25 / 0.14 / 0.10; Hypothesizer completion 0.28 / 0.23 / 0.08; humans 0.66 completion, 0.55 knowledge. DiscoveryBench: 264 tasks, 903 synthetic, best 25 percent.

## Corrections made (applied in claims, not to the evidence files)

1. LLM-SRBench "28.1 percent on LSR-Synth" (a14, b01, c07) is a single cell: LaSR on material science (28.12). Best per domain: chemistry 11.11, biology 25.30, physics 9.91, material science 28.12. Unweighted mean of those four is about 18.6. The paper text does say "28.1% on LSR-Synth", so the evidence matches the paper, but the paper's headline overstates the typical domain. K07 uses the range.
2. NewtonBench noise result (b17, c20) was run on GPT-5-mini only, not on all models. Also whether "12-16 percent" is absolute or relative points is not stated in the text; I kept "percent loss".
3. SR-Scientist "w/o top-k" means random sampling from the buffer instead of top-k sampling, not removal of the buffer (a18, a19, b19, c17 say "no top-k"). K08 states this.
4. LaSR headline is inconsistent inside the paper: intro says 66 of 100, Table 1 says 72. The appendix equal-time test gives PySR 59 + 3 = 62 with 10 hours per equation against LaSR 72 with 40 iterations, so the fair gain is about +10, not +13. The paper also has a synthetic anti-leakage test and a same-equation memorisation check (not read in detail).
5. AI Feynman prior-best baseline is 71 in the abstract and one text passage and 68 in "Key findings" (a09, b08 already flag it). The paper contradicts itself; both appear.
6. NewtonBench extra figures read: GPT-5 with code 73.3 (down from 75.9, so the strongest model also dips slightly); GPT-5 tokens about 19.15k per task (b16 "about 19k" fine).
7. FIRE-Bench "sd 23.4" (c25) is the spread across tasks in the table, not clearly across runs.
8. DiscoveryWorld: the human table shows 10 scientists, not "up to 11" (b15). Small.

## Contradictions between sources

- LaSR: strong on Feynman (72 of 100, beats PySR) but weak on memorisation-controlled sets (5.4 to 12.6 percent symbolic on LSR-Transform in LLM-SRBench; far below SR-Scientist and LLM-SR in SR-Scientist's table). Either LaSR gains are partly recall, or the benchmark runs used weaker settings. Not resolved (K13 contested).
- Tools: SR-Scientist says the data-analysis tool is the biggest lever for GPT-OSS-120B, NewtonBench says code access slightly hurts strong models. Different tasks (static data fitting versus interactive experiments), different models. Not truly contradictory but the rule "give a tool" is not safe (K08, K09).
- Contamination: LLM-SR, LLM-SRBench and SR-Scientist see memorisation on Feynman; FIRE-Bench finds no clear cutoff effect on ML-paper rediscovery; one anecdote says GPT-5 did not recall Kepler's law once variables were renamed, while Sharlin and Josephson say Kepler data are recognised even without context. Mixed (K26 contested).
- AI Feynman: 100 percent by authors, 53 percent exact in SRBench (not re-opened by me), and SRBench says it wins only noise-free.

## Weak spots

- Heavy reliance on one family of papers: LLM-SRBench and its own authors' LLM-SR, plus SR-Scientist which uses the same benchmark. Independent source counts are lower than the number of evidence lines suggests.
- LLM-judged symbolic accuracy in LLM-SRBench, NewtonBench (98.3 percent agreement with humans), MOOSE-Chem and DiscoveryBench. Judge bias is possible; G5 asks for code equivalence.
- Backbones in LLM-SR / LLM-SRBench are GPT-3.5, Llama-8B, GPT-4o-mini: far weaker than 2026 reasoning models. Rankings may not hold.
- The founding historical work (BACON, STAHL, DALTON, GLAUBER) has almost no counted data: no run-to-run variance, tasks chosen by authors, data cleaned. The book (a25) and the Klahr and Dunbar / Klahr and Simon papers (a26, a27) were never opened.
- Human data: Qin and Simon (4 of 14) seen only in a search summary; no human protocol numbers from Klahr and Dunbar.

## Only seen in snippets or unopened

a25 (book), a26, a27, a28 (Eureqa), b29 (Qin and Simon), b30 (Heeffer), b27 (BoxingGym, abstract only), b28 (abstract only). SRBench 53 percent / 27 percent (b10) and LLM-SR ablation values (a13, b06, c04) not re-opened by the cross-checker (LLM-SR PDF failed to download), though three agents agree on the same values. Many table cells in LLM-SR and LLM-SRBench text were scrambled.

## GAPS

1. Does a generate-fit-score-revise scaffold beat the plain reasoning model at equal tokens on changed-law or invented-law tasks (NewtonBench, DiscoveryWorld style)? Every positive scaffold result so far used weak backbones or the authors' own benchmark.
2. Which of the two loop parts (data inspection by code, best-attempts buffer) pays for which backbone, and does the answer hold for current reasoning models rather than GPT-OSS, Qwen, GLM?
3. Why does code access hurt strong models (NewtonBench, early satisficing from two traces), and does a minimum-hypotheses rule or held-out check fix it at equal tokens?
4. What does an independent replication of AI Feynman, LaSR and LLM-SR show on one shared, contamination-controlled set with repeated seeds and code-based symbolic equivalence (not an LLM judge)?
5. Can a code-run structure probe (units, symmetry, separability) run before generation lift LLM agents the way it lifted AI Feynman, and where does it fail (non-physical, noisy data)?
6. What are the human numbers: Klahr and Dunbar (1988), Qin and Simon (1990), Klahr and Simon (1999) sample sizes, success rates and which search space (hypothesis or experiment) stalls? Needed as a bar and to test the dual-space reading on LLM traces.
7. Does STAHL-style historical-order feeding (with reproduction of wrong turns) work as a test for an LLM scaffold on a case series, and are there any LLM studies that did it (not found so far)?
8. Does a scope-tagged revision (split by condition, ABACUS style) beat overwrite on revision tasks with conditional laws, and do LLM systems ever learn conditional laws?
9. How much of the gap between LLM agents and humans in DiscoveryWorld and FIRE-Bench is control design and conclusion drawing (FIRE-Bench failure analysis), and does a code claim-versus-output check close it?
10. Do recall controls generalise: renamed variables, altered laws and post-cutoff splits disagree across studies; which one best predicts out-of-distribution performance?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d18). New claims K27 to K33; K09, K11, K16, K18, K19, K24, K26 got extra evidence and a note. WebSearch ran out of quota, and the arXiv, OpenAlex and Semantic Scholar APIs rate-limited, so coverage is thinner than planned.

Status of the ten gaps:

1. Scaffold vs plain reasoning model at equal tokens on changed-law or invented-law tasks: **still open**. No study has that arm. Closest: SciLaws-Bench (14 current models, one harness, no scaffold arm; GPT-6 beats GPT-5.5 by 14 points on invented variants, so backbone swamps scaffold effects), LLM-PySR (equal budget, GPT-5.1, but the plain arm is LLM-SR, not a reasoning model with code), IGSR (300k-token budget, GPT-4o-mini). Every positive scaffold result is still on a weak backbone or the authors' own benchmark.
2. Which loop part pays for which backbone: **still open**. Nothing new on current reasoning models. IGSR suggests per-term held-out feedback helps a weak model; SR-Scientist ablations unchanged.
3. Why code hurts strong models; does a rule or held-out check fix it: **still open**, but sharper. NewtonBench's evidence is phrase counts in two traces (d14). SciLaws-Bench shows the problem may sit in selection (best candidate beats submitted law by 0.14 for a weak model, 0.03 to 0.04 for the best; self-selection recovers under 2 of 4.5 to 5.3 oracle points), so a held-out check is the right first test (K30). Not run by anyone.
4. Independent replication of AI Feynman, LaSR, LLM-SR: **partly closed, with a worse picture for the LLM systems**. The paired library-reachability study (4 seeds, one fitter and budget, 129 tasks) found a no-LLM bank at 77.7 percent Acc0.01 beating SR-Scientist 63.6, LLM-SR 41.1, PySR 29.5, LaSR 16.0 as reported (K29). Still no single contamination-controlled set with all three methods and code-based equivalence; its symbolic accuracy still uses an LLM judge with a 10-of-10 vote.
5. Structure probe before generation: **partly closed**. KeplerAgent (symmetry tool, GPT-4o-mini) lifted ODE symbolic accuracy from 30/10 (PySR) and 40/15 (LLM-SR) to 75/45 clean/noisy (d12). It failed to beat PySR in one run on LSR-Transform (35.1 vs 37.8; d13). Units and separability probes with an LLM agent remain untested; weak backbone only.
6. Human numbers: **half closed**. Klahr and Dunbar (1988) read in full (d01 to d03): Study 1 N=20, 19 solved, 19.8 min; 13 Experimenters stalled in hypothesis space and were rescued by an experiment; Study 2 N=10. Qin and Simon (1990) and Klahr and Simon (1999) still unread (paywalls); K26 stays unverified (d18).
7. STAHL-style historical-order feeding with an LLM: **still open**; no LLM study found (K33, weak negative).
8. Scope-tagged revision and LLM conditional laws: **still open**. Only the multi-group tasks in SciLaws-Bench (shared form, group-specific parameters) come near; no revision comparison.
9. Control design and conclusions in agent-vs-human gap: **half closed**. FIRE-Bench confirms planning and conclusion errors dominate and false positives are 76 to 95 percent contradictory or unrelated (d16); the code claim-versus-output check was not tested by anyone. SciLaws-Bench adds that fit and validity agree on only 53.6 percent of pairs (d07).
10. Which recall control best predicts out-of-distribution performance: **still open, but the controls are now better described**. Renaming gives a graded drop (Acc0.01 49.8 to 41.1, d09); cold-recall tiers predict published-form recovery (92 vs 61 percent) but not new-structure recovery (flat 12 to 13 percent, d05); FIRE-Bench cutoff cells have 1 to 8 tasks (d16). No study compared the controls against OOD scores directly; the cheapest design is all three on one task set.

Corrections and cautions:
- The "LLM-SR 41" and "SR-Scientist 63.6" numbers are on the 129 LSR-Synth tasks; the "no-LLM bank" arm is a ceiling for that task set only.
- LLM-PySR's advantage over plain PySR is +3.6 points ACC0.1 with a large spread (SD 0.165); the big gains are against LLM-SR and DrSR on tokens.
- KeplerAgent's DiffEq table was read from a garbled extraction; the text confirms only "45 percent noisy, 3 times the best baseline".
- SciLaws-Bench, library reachability, LLM-PySR and IGSR are 2026 preprints; none seen peer-reviewed.
