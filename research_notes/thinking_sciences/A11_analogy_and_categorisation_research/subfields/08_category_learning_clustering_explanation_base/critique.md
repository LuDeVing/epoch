# A11.08 Cross-check: category learning (clustering, explanation-based, Bayesian)

Checked 2026-11-10 by re-opening the PDF text of: Sanborn et al. 2010, Love et al. 2004, Jagadish et al. 2024 (ERMI), Qiu et al. 2024, Wang et al. 2024, Parab et al. 2025, Zhu et al. 2023 (HtT), Piriyakulkij et al. 2024, MacLellan et al. 2026, Bazigaran and Sohn 2025, Moskvichev et al. 2023 (partial).

## Confirmed exactly
- Sanborn 2010: local MAP r=.87 / PF M=100 .78 / M=1 .77 (1 block); .95/.93/.90 (10 blocks); 25 of 40 (62.5%) order effect; PF 63%, M=100 52%; PF better in 58% of Shepard settings, SSD 0.24 vs 0.31; 0.9997 ratio.
- Love 2004: 6.5 (7.5), 12.3 (11.2), 27.4 (28.6), 10.4 (10.6) blocks; first/last name 7.1 vs 9.7.
- Jagadish 2024: BIC 38722.13 vs 39816.90 and 41207.20 vs 42401.42; posterior frequency .43 vs .41; OpenML 70.95/70.51; Claude "completely exemplar-based after the second block"; Shepard MSE 0.0287 ERMI vs 0.2627 MI.
- Wang 2024: 17/23/30/33/45%; 49 tasks with a correct hypothesis; 33 (67%); Icecuber 43%; SyGuS 94.3%.
- Bazigaran 2025: JSD .36/.56, best fit .30/.49, MAP/BinL/MaxL values, rule bias .9 vs 1.0.
- Parab 2025: 46.4 / 34.5 / 61.2 / 62.0 / 4.3 / 257 / 12.1.
- HtT: +11.1 to +16.4 CLUTRR, +27.2 GPT-3.5 with GPT-4 rules, 34.4 List Functions task, +13.7, +21.0.
- Piriyakulkij: R2 .57 / .10 / .05 / .25; log-lik -1478.82 vs -1539 vs -5209.93.

## Corrections
1. b09 mislabels Zendo rows. The paper's table has six non-human rows; 6.55/8 belongs to Online Hard (the authors' strongest model, per their text), 5.35 to Online Fuzzy (text: "fuzzy variant 5.35"), 6.01 and 6.18 to the batch hard variants, 4.57 to Batch Fuzzy. b09's "batch hard 6.55 (best)" and "batch fuzzy 5.35" are wrong. ActiveACRE 0.35 is Online Hard; 0.15 and 0.10 are batch hard / batch with refinement (confirmed). Row alignment is from a garbled table extraction, so it is probable, not certain.
2. "LM as interpreter collapses accuracy" (a18, b13, c09) is true for MiniSCAN (above 80 to near 0) but milder elsewhere: ACRE task 59.0 to 47.0, List Functions 61.2 to 50.0, MiniARC 14.6 to 5.4. The mapping of these numbers to the LM-interpreter condition is inferred from table labels (the table row is labelled "Standard"); treat as likely. a18's MiniARC "14.6 symbolic vs 5.4" matches.
3. b12 compares MiniARC raw 33.1 to 5.9-12.8 only; the best setting (T=3, N=5) is 18.7 raw. Task accuracy: IO 13.8, best refinement 14.6, so no real gain.
4. Authorship: a16, c05-c07 credit "Ellis (2023)"; arXiv 2306.02797 is Wong, Grand, Lew, Goodman, Mansinghka, Andreas, Tenenbaum. Ellis is a co-author of Piriyakulkij et al. (b09), not first author of this paper. Those lines are one source, counted once.
5. Jagadish MSE values are three different analyses and are mixed in b02/c18: Shepard curves ERMI .03 vs MI .26 (RMC .10, PFN .17 in Table 5/learning curves); Badham error rates Claude .18 vs ERMI .05. Not contradictions, but never compare across them.
6. MacLellan: Cobweb .95 vs RMC .91 is a rank correlation on a handful of transfer items with no significance test; footnote 5 says the RMC predictions "look different but are ordered similarly"; the context model itself scores .96 on Exp 2. "Better than RMC" is a weak claim.
7. b01/c18 "better than seven models": ERMI .43 vs RMC .41 with SE .05 is a tie on Badham; on Devraj it leads (.32 vs GCM .24).

## Contradictions between sources
- Wong et al. (GPT-4 ratings unlike humans, number game) vs Bazigaran (o1-mini more rule-biased, max-likelihood). Not in conflict, but models differ (GPT-4 vs o1-mini).
- Qiu: refinement helps ACRE and MiniSCAN, hurts MiniARC raw. Wang: refinement helps ARC. Parab: refinement fixes 4.3% of wrong hypotheses. Net: refinement helps only where the hypothesis space contains the answer.
- Hard rules score higher than fuzzy rules, but fuzzy rules fit humans (Piriyakulkij). A human-like fit is not an accuracy-maximising design.
- Prototype-to-exemplar shift: needs alpha near 2 in Cobweb; alpha<0.6 removes it. Mechanism contested (Nosofsky and Zaki 2002 attention account, not opened).

## Weak spots
- Source count is inflated. 85 lines come from about 25 papers. Qiu (a18, a19, b12-b14, c08-c11), Jagadish (b01-b05, c18-c20), Wong (a16, b06-b08, c05-c07), MacLellan (a05, a06, b17, b18), Lee (a14, b21), Wang (a17, b15, c12) are one source each.
- Founding works not opened: Anderson 1991, Tenenbaum 1999, Pazzani 1991 (all opened:false; facts via Sanborn 2010 and recall). Medin and Schaffer 1978, Smith and Minda 1998, Hayes-Roth 1977, Shepard 1961 are second-hand. Tenenbaum and Griffiths 2001 abstract only. Several b2x/c2x lines are "recalled, not read" and were not used as evidence in claims except as context.
- No human-data replication of EBL in people; Pazzani's prior-knowledge effects have no numbers.
- Qiu noise results are in figures; no exact numbers.
- LLM numbers are mostly GPT-4 / Claude-2 / o1-mini; nothing on 2025-26 reasoning models for ARC-style induction except Bazigaran; results may not transfer.
- Studies are task-specific (list functions, ARC, number game); none tests rule fit across a run (S7) in a long-horizon agent.
- Same-lab clustering: ConceptARC pair (Mitchell group), Wong/Piriyakulkij (Ellis, Tenenbaum links).

## Snippets only
a13 (abstract only), a26, a27 (second-hand), a25 (second-hand via MacLellan), b23 (no new data), b24-b29, c26-c29 (not read).

## GAPS
1. Does an LLM agent that keeps several weighted candidate rules (Dirichlet-process style, open a new rule only on a surprise) beat one-rule-at-a-time at equal tokens on ARC-style and list-function tasks with current models?
2. Which stage of propose-test-refine fails first with 2025-26 reasoning models: hypothesis generation, pruning, or application? Parab and Wang used GPT-4/4o.
3. Can in-model rule application be made reliable cheaply (explicit per-example check, code tool), and what token cost does it add versus the 59.0 to 47.0 ACRE drop?
4. How should the agent treat noisy or exceptional examples (Qiu brittleness; humans fix exceptions from segment 4 of 10)? Does an explicit exception list restore accuracy?
5. Does hypothesis-order or example-order sensitivity (Sanborn order effect 62.5%) appear in LLM rule induction, and does shuffling plus voting fix it?
6. Does the size principle (prefer smaller consistent hypotheses) prompt move LLM number-game generalisation toward humans (JSD .56 toward .36)?
7. Does explanation-based generalisation (explain one example with a stated theory, keep only used features) beat inductive rules when the theory is partly wrong? Pazzani 1991 and Minton 1990 were not opened; read them.
8. What is the utility cost of a growing rule library in memory (EBL utility problem) for an LLM agent, and does random-rule contamination (HtT) have a safe filter?
9. Anderson 1991 and Tenenbaum 1999 original numbers (Medin-Schaffer fits, Number Game, size principle) are not verified first-hand; obtain the open copies.
10. Do human-like priors (ERMI-style, LLM-generated tasks) improve a scaffolded agent, or only a trained network? Is the .43 vs .41 tie versus RMC robust on other human datasets?

## Gap search results (2026-11-10, evidence_d.jsonl d01-d18, claims K23-K29 added)

Search note: about 4 WebSearch calls plus direct arXiv PDFs; Semantic Scholar and arXiv query APIs were rate-limited. Pazzani 1991, Minton 1990 and the Tenenbaum thesis PDF could not be downloaded.

1. Weighted candidate pool vs one rule at equal tokens: PARTLY CLOSED. Pool breadth helps (K23: diversity method +4.5/+5.0 points; K24: ARC Prize 43% sampling vs 14-18% single pass). No study weights rules Dirichlet-style at equal tokens with 2025-26 models. Still open as a controlled test.
2. Which stage fails first with 2025-26 models: PARTLY CLOSED. FalsifyBench (12 models incl. GPT-5.2) shows the test step (confirmation bias) and drift to surface-feature rules, not generation, as the first failure (K25). Pruning and application with reasoning models were not isolated. Jin 2026 and Jhaveri 2026 not read.
3. Reliable cheap rule application: PARTLY CLOSED. Executable rules (PAL, SRR) work; no token-cost comparison against the 59.0 to 47.0 ACRE drop was found (K26).
4. Noise and exceptions: PARTLY CLOSED. Second lab confirms brittleness (K11 now established); subset sampling plus execution feedback reduces the drop. An explicit exception list was not tested directly.
5. Order sensitivity in LLM rule induction: STAYS OPEN. Only 2021-22 classification evidence and voting gains on other tasks (K27, contested).
6. Size-principle prompt: STAYS OPEN. Arithmetic verified (K29); no LLM test found.
7. EBL vs induction with a partly wrong theory: STAYS OPEN. Pazzani and Minton not opened (d14, d15 opened:false).
8. Rule-library utility cost and filter: PARTLY CLOSED. Xiong 2025 shows a strict utility filter helps and a noisy one hurts (K28); no rule-library or Minton numbers.
9. Anderson 1991 and Tenenbaum 1999 first-hand: STAYS OPEN. Number-game likelihood arithmetic is confirmed via a lecture summary (d12); thesis human data still unverified.
10. Human-like priors improve a scaffolded agent: STAYS OPEN. Nothing new found; the .43 vs .41 tie versus RMC was not retested.

Caveats: table extractions for Li 2025, Lee 2025 and Xiong 2025 were garbled, so figures above are limited to those that were unambiguous; d11 memory numbers are approximate.
