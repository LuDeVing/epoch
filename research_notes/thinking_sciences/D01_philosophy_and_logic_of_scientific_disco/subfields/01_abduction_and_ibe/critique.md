# D01.01 Abduction and IBE: cross-check critique

Checker run 2026-10-26. Sources re-opened this session (PDF text via pdftotext, or PMC HTML): Dalal et al. 2402.10767, Wang et al. 2309.05660, Del and Fishel 2212.10114, Salimi et al. 2604.08016, He et al. (GEAR) 2509.24096, Qiu et al. 2310.08559, Abe et al. 2603.06428, Sun and Saparov 2509.03345 (cached text), Lombrozo 2007 (cached text), Douven and Schupbach 2015 (PMC4410515), Trpin and Pellert 2019 (cached text), Liu et al. 2404.03028 (cached text). PDFs deleted from D:/research_scratch/D01.01.

## Numbers confirmed (10 checked)

1. Lombrozo 2007: 96% one-cause with no base rates, 92% more probable disease with base rates (Exp 1, N=48); 41% simple at 1:10 and 63% overall (Exp 3, N=108); 17% / 46% / 61% in Exp 4 with chi2(1)=8.85. Confirmed.
2. Douven and Schupbach 2015: R2 0.90 (MOAB) vs 0.83 (MO), AIC -398.77 for MO, chi2(2)=124.87, p<0.0001. Confirmed. N=26 is from the evidence file and the paper's reanalysis of Schupbach 2011.
3. Dalal et al. IBE-Eval: up to 77%, +17.5 average over GPT-3.5 judge, parsimony 14% better than consistency, Spearman 0.64 vs 0.31. Confirmed.
4. Wang et al. Hypothesis Search: ARC 17% direct, 23% programs only, 30% LLM-summarised, 33% human-selected. Confirmed. Added detail: of 49 tasks with a human-judged correct hypothesis, 33 (67%) became correct programs, so about a third of correct hypotheses are lost at implementation.
5. Del and Fishel True Detective: random 0.24, human average 0.47, vanilla 0.28/0.26/0.27, CoT 0.26/0.29/0.38, golden CoT 0.46/0.63/0.83. Confirmed.
6. Salimi et al. survey: medians 79.96 / 42.50 / 28.8; ART 87.2, e-CARE 88.0, True Detective 42.9, MuSR best 68.0 (GPT-4o; GPT-5.4 only 60.8); ProofWriter 21.5. Confirmed.
7. GEAR: 50,340 hypotheses, 17,835 consistent (35%), 28,159 contradicted an observation, 4,346 format failures; "70B-class about 20%"; "around 80% of equally plausible hypotheses labelled incorrect". Confirmed. 20% and 35% are consistent: 20% is the 70B class, 35% is all nine models.
8. Qiu et al. Table 1 (GPT-4): ACRE raw IO 64.0, SC 65.0, SR 70.0, refinement T=3,N=5 82.5; task 28/29/32/59; MiniSCAN task 0.0 to 46.0 (T=3,N=1) and 70.0 (T=3,N=5). Confirmed. See correction A.
9. Abe et al.: zero-shot abduction GPT-4 41.67, GPT-3.5 31.02, Llama3-8B 37.50, Llama3-70B 37.04; deduction GPT-4 72.22; GPT-4 "Neither" 0.00. Confirmed (216 items per task).
10. Trpin and Pellert: IBE** high-probability-on-truth in about 49-52% of runs vs 16% / 11% for JC; false-confident 30% / 22% vs 24% / 17%. Confirmed. See correction B.

Also confirmed: Sun and Saparov (above 80% to below 50% at height 2; true hypotheses 3.0 to 3.5), Liu et al. (30% to 96% for GPT-4-turbo with the true instruction).

## Corrections and additions

A. Qiu et al.: the evidence file (a29) lists MiniARC but the framing in the c-file reads as if refinement helps broadly. It does not. On MiniARC raw accuracy refinement is worse than plain prompting (T=3,N=5: 18.7 vs IO 33.1; T=1,N=1: 5.9; self-refine 15.1). Table 4 rows for other models were garbled in extraction; only the GPT-4 Table 1 numbers were relied on. Claim K02 states this boundary.

B. Trpin and Pellert (a18): the file reports IBE** winning on truth-detection and being "also more often confident in a false hypothesis" (30%/22% vs 24%/17%). Their Table 7 adds a much sharper early effect: at the first update step IBE** puts above 0.95 on a false hypothesis in 47% of simulations (above 0.99 in 37%) vs 3% and 1% for JC. The paper says IBE** is "often initially lead astray" and then converges (Brier scores toward 0), while JC stays inaccurate. Early overconfidence is the decision-relevant fact for a scaffold and was missing. Folded into K17.

C. Salimi et al. median (c17): the medians pool single experiments of different models, methods and datasets. They are an ordering, not a controlled comparison. The abduction-vs-deduction pair scatter shares model and method, which is better, but the headline 42.5 vs 79.96 should not be quoted as a like-for-like gap. The like-for-like figure is Abe et al. (41.67 vs 72.22, same content).

D. MuSR: b16 and c15 both say the best is 68.0 by GPT-4o, while the same table gives GPT-5.4 60.8. The claim text keeps both. The newest model is worse than an older one on this item.

E. Sun and Saparov year: a22 says 2025, b11 says 2026. Same paper (arXiv 2509.03345, v3 in 2026). Models in the later version include GPT-5.4 and o3. Numbers cited are from the same tables.

## Independence problem (important)

The three evidence files overlap heavily. These are the same source recorded two or three times, not independent confirmation:

- Lombrozo 2007: a08-a11 = b01-b04.
- Dalal et al.: b09, b10, c01-c03.
- Sun and Saparov: a22, a23, b11, b12, c04-c06.
- GEAR: a24, a25, b19, b20, c12, c13.
- Qiu et al.: a29, c07-c09.
- Wang et al.: a28 = b18.
- Del and Fishel: a27 = b17.
- Salimi et al.: b16 = c15-c17.
- Abe et al.: b13 = c18.
- Douven and Schupbach: a14 = b06.
- Steiglechner et al.: b14, b15.

Claims count independent sources per paper (and per lab for Lombrozo), not per evidence line. As a result, many claims that look well supported are single-source. Of 22 claims: 7 established, 13 single-source, 2 contested.

## Contradictions between sources

- Speed of IBE vs Bayes: Douven (2013) and Douven and Wenmackers (2017) find explanationist updating faster to the truth; Pettigrew finds a trivial rule matches it on speed and Bayes wins on expected accuracy; Trpin and Pellert find speed gains but early overconfidence in the false hypothesis. This is a trade-off, not a win (K17, contested).
- Few-shot: helps Llama-3-70B on syllogism abduction (75.5%) but hurts GPT-4 (28.7%) (K09).
- Self-consistency: no help on ACRE (64 to 65) in Qiu, but beat the multi-role Theorem-of-Thought on some cases in Abdaljalil. Different tasks and model sizes.
- Does the LLM do abduction: Floridi et al. (no) vs Imran et al. (weak yes in one of three cases) (K21). Not decisive for engineering.
- Simplicity: Lombrozo shows a human simplicity bias that is not simply irrational; Liquin and Lombrozo 2018 show it reverses in some causal structures; for LLMs, Sun and Saparov show models fail to be simplest even when told to explain. No source tests whether adding a simplicity score improves LLM selection except Dalal (parsimony features).

## Weak spots

- Everything on human explanation preference comes from one lab (Lombrozo). The only outside tests are Douven and Schupbach (reanalysis of one study, N=26) and SEP summaries.
- The IBE-versus-Bayes literature is simulation only, with coin or urn tasks and hand-set bonus parameter c. No test on language-model hypothesis pools.
- IBE-Eval used GPT-3.5 and Llama 2 on COPA and E-CARE, two easy short commonsense sets. Whether parsimony and hedging features survive on harder tasks and on modern models is unknown.
- Several benchmarks (InAbHyD, GEAR, Steiglechner) are synthetic. Real-world abduction (diagnosis, debugging) has only Graph of States, one paper.
- Peirce and Hanson material is secondhand via SEP.
- Hypothesis Search and Qiu et al. use GPT-4 and 2023-era setups. Current reasoning models were not tested with these loops except in the survey and Sun and Saparov.

## Seen only in snippets or abstracts (opened:false or partial)

b22 (Schupbach simulation summary), b23 (Climenhaga), b24 (Cabrera), b25 (Bonawitz and Lombrozo 2012), b26 (Douven 2013; fetch blocked). b05 (Liquin and Lombrozo 2018): abstract page only, effect sizes not read. b08 (Trpin and Pellert catalogue page; numbers verified here from the full text). b20 (GEAR training deltas not read). b21 (Kim 2022). c27 (Farmer 2026 abstract). Claim K17 relies partly on these and is marked contested.

## GAPS

1. Do code-computed virtues (parsimony, scope, hedging, consistency) beat vote and a blind model judge at picking the right hypothesis from a pool of N candidates, with modern models and harder tasks than COPA and E-CARE? Only Dalal et al. (GPT-3.5, Llama 2) measured this.
2. How often does the correct hypothesis appear in the pool but fail to be selected or implemented (Wang: correct hypothesis in 49 of 100 ARC tasks, 33 turned into correct programs), and does a held-out-example gate (G3) recover the lost third at equal tokens?
3. Can a code-checked good-enough gate detect the bad lot, that is, flag a candidate pool that contains no true explanation? No benchmark with distractor-only pools exists in our evidence; Abe shows models almost never answer Neither.
4. Does hypothesis-then-test help or hurt by problem class? Qiu shows MiniARC gets worse; what predicts the sign (plain pass rate, rule complexity, model size)? This decides S0 mode choice.
5. Does the explanationist bonus (Douven's EXPL) have any use in S7 when ranking candidate rules by support from successive observations, and what bonus size avoids the early-overconfidence failure seen in Trpin and Pellert (47% early false-high)?
6. How does abduction accuracy fall with the number of interacting causes for current reasoning models, and does a code-built "what changed" table (S2) or an impasse operator (S6) flatten the curve (Steiglechner: 0.32 for one change, 0.03 for interacting changes)?
7. Is the Lombrozo simplicity preference a good prior for LLM selection? Needs an independent lab replication and a test on LLM pools: does adding a simplicity weight help when ground truth is simple vs when it has an exception?
8. Does set-level scoring (GEAR: consistency, generalisation, diversity) improve final accuracy when used as the selection rule in S7 at inference time, not only as a training signal?
9. Does self-explanation in S2 (Lombrozo 2016) bias an LLM toward one unifying rule, and does it hurt when the truth is a rule with exceptions?
10. What do external replications of the explanation-preference human results (outside Lombrozo and Douven) show, and is there any failed replication? None found in these files.


## Gap search results

Evidence file: `evidence_d.jsonl` (d01 to d31, 31 lines; 25 opened, 6 abstract-only). Claims file now has K01 to K33. WebSearch quota was exhausted, so papers were found through the Hugging Face papers search, Europe PMC and Crossref, and PDFs were read from arXiv or open archives. Scratch text sits in D:/research_scratch/D01.01 (PDFs deleted).

Status changes: K08 single-source to established (4 independent sources). New claims K23 to K33. Existing claims K02, K06, K11, K13, K15, K16, K17, K22 got extra evidence ids and short notes.

### Closed or mostly closed

- **Gap 2 (pool has it, never used): mostly closed.** K23 and K24. Across five independent sources the right item is often in the pool but not picked (MATH coverage 98.44% vs 41.41% picked; AIMO 42/50 vs pass@20 45.5; 2% to 46% of trajectories that sample the answer lose the vote). For Wang et al. the larger loss is implementation: 49 correct hypotheses, 33 programs with a human picking, 30 with an LLM summary step. So a held-out gate at equal tokens would recover about 3 tasks in 100 on selection, not the whole 16. Where a strict code check exists it recovers most of the loss (74.2% to 92.2%, no new errors). Not tested directly: an equal-token run of G3 on the Wang setup.
- **Gap 4 (what predicts the sign): partly closed.** K28. Symbolic, short, composable rules gain (ACRE, List Functions, ARC induction); perceptual or visual-pattern items and wide-window rules do not (MiniARC 33.1 to 18.7, ConceptARC, InductionBench). No paper tested a predictor head-on. A usable S0 check: does any short program fit the examples.
- **Gap 5 (bonus size): partly closed.** K26. Trpin and Pellert full text confirms 47% vs 3% early false confidence at a fixed bonus of 0.1 and never varies the bonus (footnote 11). Douven 2020 is the only test of size: best near 0.01, with heavy early die-off of explanationist agents. Simulations only; nothing on LLMs.
- **Gap 9 (self-explanation and exceptions): closed for chain of thought.** K27. Liu et al. 2025: GPT-4o needs 12.5 rounds vs 2.9, Sonnet 6.4 vs 2.3, Opus 5.5 vs 2.4; GPT-4o with CoT stays at 80%. Not tested: an S2 self-explanation step in our scaffold, and reasoning models released after 2024.

### Still open

- **Gap 1 (code virtues vs voting and judge, modern models, hard tasks): open.** No new test. Nearest: USC judge ties voting and sits 6 to 20 points under the oracle (K23); CodeT agreement score gives +18.8 on HumanEval (K11 note). IBE-Eval remains the only virtue test, with GPT-3.5 and Llama 2.
- **Gap 3 (bad-lot gate): open.** K29. No distractor-only benchmark found. Models rarely abstain and reasoning makes it worse (AbstentionBench, DNR Bench). DeFAb shows a code check on the observed case alone is passed by trivial local fixes (K32); a held-out transfer group is needed.
- **Gap 6 (interacting causes, code-built diff or impasse step): open.** K30. Reasoning effort adds little on Elenchos (attribution 0.37 to 0.41 to 0.47 for GPT-5.4 at none, low, medium). o1 stayed flat on a different, composed-causal-arithmetic task. The proposed fixes were not tested by anyone.
- **Gap 7 (simplicity prior for LLM selection): open.** K33. No test on LLM pools with simple truths vs truths with exceptions. Human evidence is mixed across labs.
- **Gap 8 (set-level scoring at inference time): open.** K31. GEAR text has no inference-time use. CodeT is the nearest analogue.
- **Gap 10 (outside replications of the human results): open, with partial information.** K33. No direct replication or failed replication of Lombrozo 2007 or of Douven and Schupbach was found. Outside labs report moderators (Lim and Oppenheimer, read in full; Johnson, Valenti and Keil; Zemla et al., abstracts only). Treat K13 as one lab's result and K33 as contested.

### New weak spots from this pass

- Six of 31 lines are abstract-only (d22 to d27); their effect sizes are unknown.
- Several 2026 preprints (DeFAb, AIMO 3, Li and Li, Reason Less) are single-author or small-team and not peer reviewed; DeFAb says its own test is flawed.
- Many tables in the PDFs extract badly (Trpin and Pellert Table 1, Li et al. Table 2, CodeARC Table 4). Mappings used are noted in the lines.
- The Trpin and Pellert 47% is the first-assignment share across 500,000 runs in Table 7; the older evidence line a18 had the 49% to 52% and 30%/22% figures with garbled columns, now mapped in d19.

### Next tests worth running (cheap, our own harness)

1. Distractor-only pools with a held-out transfer set (gap 3).
2. Three selectors at equal tokens (vote, blind judge, code consistency plus held-out fit) on ARC-style items (gaps 1 and 8).
3. Bonus size sweep 0, 0.01, 0.03, 0.1 on a small rule-ranking task (gap 5).
4. Rule-with-exceptions set with and without a self-explanation step (gaps 7 and 9).
