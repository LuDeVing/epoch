# Critique: Geneplore model (A09.01), cross-check

Cross-checker pass, 2026-10-26. Claims are in claims.jsonl (K01 to K25).

## Numbers re-opened (full text this session)

1. Finke and Slayton 1988 (a01, a02): 119/312 = 38.1%, 19 creative; Exp 2 124/280 = 44.3% (19 creative, 15.3%), 110/280 = 39.3% (15 creative). Confirmed. Detail: the 18.5% is the share of recognizable patterns subjects predicted; 10.0% when all three guesses were made.
2. Si et al. 2024 (a19, b10, c01) novelty 4.84 / 5.64 / 5.81, N=49 per condition, 119/109/109 reviews. Confirmed. Added: the result also holds averaged per idea (Test 2: 4.86 vs 5.62 vs 5.78) and per reviewer (Test 3). Overall score with rerank 5.34 is p=0.04 in Test 1 only.
3. Si dedup: about 200 of 4000 seed ideas non-duplicate at cosine 0.8. Confirmed.
4. Si judge accuracy: 56.1 (experts), 53.3, 50.0, 45.0. Confirmed.
5. Si et al. 2025 ideation-execution gap (b13, c04, was abstract-only for c04): CORRECTION. The significant result is that LLM ideas dropped more than human ideas (p<.05). The post-execution human vs AI difference was not significant on any metric ("we do not have sufficient statistical power"). Evidence lines saying rankings "flipped" or "reversed" must be read as point estimates. Claim K11 states this.
6. Meincke et al. 2024 (b17, b18, c13, c14): 0.243, 0.377, 0.368, 0.387; pools 3,700 vs 4,700; repeats 13.8% vs 11.7%; advantage gone about 750 to 800. Confirmed.
7. Gupta and Pruthi 2025 (b14): 14.0% (7/50) plus 10.0% (5/50) = 24%. Confirmed. Note the 50 documents are not all new pipeline output (36 generated plus 14 exemplars, per the evidence line); I did not re-verify that split.
8. MacGyver (c05 to c07): 1,683 problems, GPT-4 62.4%, humans 65.1%, wrong tool use 42.4%, self-reflection 9.7% vs 4.3%, div-conv 6.5% vs 2.2%. Confirmed. Small mismatch: c05 says zero-shot GPT-4 37.5% infeasible, the table row implies 37.6. Immaterial. The GPT-4 vs human gap (62.4 vs 65.1) is small and no test was given; "humans stronger on feasibility" is weak wording.
9. Hubert et al. 2024 (b19): F=622.10, 0.51, DAT 84.56 vs 76.95, fluency 6.94 vs 7.01. Confirmed. The 0.51 is eta squared, not Cohen d; the evidence line calls it "effect size", which is fine but should not be compared with d.
10. Marsh et al. 1996 (a11, b04, b05) and Smith et al. 1993 (a09, b01, b03): conformity .087 to .280, 4.4% to 12.1% critical features, F(4,75)=5.91 omnibus, F(3,76)=8.69, t(76)=2.89, 1.56. Confirmed. Note the .087 to .280 values are a mean of three features; antennae alone was not significant (F=1.46, p=.224), so the dose-response is carried by tail and four legs.

Not re-opened: McKnight et al. 2006 numbers (download failed twice). The b28 student replication is a search-snippet only.

## Duplicate coverage (not independent)

- a19, b10, c01 are the same Si 2024 paper; a20, b11, b12, c02, c03 likewise. Counted as one source.
- a09, a10, b01 to b03 are Smith 1993; a11 to a13, b04 to b07 are Marsh 1996.
- a23, b25, c15, c16 are Gu et al., one paper.
- a15, b08, b09 are Christensen and Schunn 2007.
- b14 and b15 are one paper. b17, b18, c13, c14 are one paper.

## Contradictions and tensions

- Prompt2Craft: fresh resample beat feedback repair (85.0 vs 75.7), while EscapeBench and MacGyver found reflection helps. Task and feedback quality differ (K18).
- Showing earlier outputs raises conformity (Smith, Marsh) yet NoveltyBench found in-context regeneration (earlier answers shown) works best for diversity. Probably different measures: avoiding exact repeats vs inheriting features of the shown set. Unresolved (K03, K15).
- Si 2024 (LLM ideas more novel) vs Si 2025 (advantage gone after execution) vs Gupta 2025 (a quarter plagiarised). Novelty at ideation stage is not value (K13).
- McKnight 2006: original theory predicted more creative products with a preinventive phase; got more original but less practical, nil net (K06).
- Self-reflection helped GPT-4 but not Claude2 or Llama2-13b: model dependence.

## Weak spots

- The Geneplore human core rests on one lab (Finke, Ward, Smith) and on judges with no published reliability (McKnight critique). Replications mostly test the example-fixation branch, not the preinventive-structure claim.
- Preinventive-structure evidence in humans is old (1988 to 2006). No test of the claim that unconstrained generate-then-interpret beats goal-first at equal effort has been done with an LLM.
- Most LLM evidence is from non-checkable domains (stories, research ideas, consumer products). Our scaffold targets checkable tasks; transfer is untested.
- Ward 1994 (a14) was not opened. Structured-imagination numbers are from secondary reports.
- c04 and c23 abstract-only; b06 Marsh Exp 2 and 3 from abstract only; b27 (fMRI) has no creativity outcome; b28, b29 are snippet or abstract.
- The Preis thesis and course-project replications are low-grade.
- The 2026 papers (c17, c22, a24) are preprints or very recent and unreplicated.

## Seen only in snippets or abstracts

b28 (student replication), b29 (Kwon et al. abstract), c04 (execution gap, now confirmed via full HTML for the key claim), c23 (Bellemare-Pepin model scores), a14 (Ward 1994).

## GAPS

1. Does a "build first, name the purpose after" generation step (preinventive phase) beat "purpose first" on an LLM at equal tokens, scored by code-checked use? No LLM test of the Finke parts-to-object task exists. Build and run a small one.
2. How do we reconcile example conformity (showing earlier outputs raises feature overlap) with NoveltyBench's finding that in-context regeneration raises distinct answers? Measure both overlap and distinct count in one experiment.
3. At what marginal new-candidate rate should S3 stop sampling and an operator fire? Si and Meincke show saturation near 750 ideas or 5% unique; what is the rate on checkable puzzle classes?
4. Does the explore step work better as revise-from-failing-output or as a fresh resample, by task class (Prompt2Craft vs EscapeBench disagree)?
5. Does the ideation-stage novelty edge matter for checkable tasks, or is it only an artifact of unverified idea evaluation? Is there a run-based novelty measure that predicts later success (execution gap)?
6. Are the Smith and Marsh conformity effects replicated by later work (2005 to 2025), including LLM analogues (does a model that sees its own earlier attempt copy features of it)?
7. What do Ward 1994 and later structured-imagination studies show numerically, and does the "path of least resistance" effect appear in LLM generation of novel categories (non-Earth creatures)?
8. Which constraints lift originality without collapsing correctness? Denial prompting dropped pass@1 from 16.1% to 2.1%; is there a constraint form (drop a constraint O4, add a banned approach only after impasse) with a better trade?
9. Is the McKnight finding (more original, less practical after a preinventive phase) robust? Only one within-experiment replication plus an unverified student replication.
10. Do model-based novelty checks ever beat random selection if grounded in retrieved prior art (the Gupta plagiarism result suggests searching changes the verdict)?

## Gap search results (2026-10-26, evidence_d.jsonl d01 to d18, claims K26 to K31)

Tool limits: WebSearch quota ran out after four queries; OpenAlex, Semantic Scholar and the arXiv API then hit rate limits; escholarship.org returned 403. All sources below were opened as PDF text through direct links.

Closed or mostly closed
- Gap 7 (Ward): partly closed. Ward 2002 (d01 to d03) gives numbers: 63% to 68% of people name a known base exemplar (animals N=71, tools N=135, fruit N=203); 99% / 97% / 91% of alien creatures keep sense organs, appendages, bilateral symmetry; reliance lowers originality by about 1 point (3.18 vs 4.34; 3.03 vs 4.18; 2.50 vs 3.40); a no-appendage constraint did not reduce reliance (people patched the tool). Ward 1994 itself still unopened (d04, opened:false). No LLM study of non-Earth creatures was found, so the LLM half of gap 7 is open.
- Gap 3 (stop rule): answered for checkable classes. Coverage keeps rising log-linearly (d12: MATH 82.9% to 98.44% from 100 to 10,000 samples; SWE-bench Lite 15.9% to 56% at 250), so use marginal coverage per doubling, not the duplicate rate. No per-class rate for puzzle sets was found; it has to be measured (K28).
- Gap 6 (conformity replication and LLM analogue): partly closed. George and Wiley 2020 (d05) is a later study with a boundary (verbal examples alone no gain, visual examples fixate, avoid instruction needed). Verma 2026 (d07, d08) shows a model copies its own earlier attempt (33-68% near-identical vs 2-14%), and that other-task examples do not hurt. Caveats: single-author preprint, small models, code. No direct replication of Smith 1993 or Marsh 1996 by a different lab was found.
- Gap 4 (revise vs resample): answer is by task class and feedback quality (d07, d09, d10, d11). Test-checked code with weak feedback and small models: resample. Strong feedback or no-test voting: refine helps. A bandit mix (REx) used 1.5x to 5x fewer calls. Claim K18 stays contested but is now sharper.

Partly closed
- Gap 2 (overlap vs distinct count): a reconciliation is proposed (K30): instruction wording decides. Examples shown with no instruction raise overlap (Smith, Marsh); earlier answers shown with an avoid or recombine instruction raise distinct count (NoveltyBench, George and Wiley, Grammenos and Lubart). Not measured in one experiment. No LLM run was possible here.
- Gap 5 (novelty and later success): Heuresis (d13, d14) found novel ideas rarely reach top quality (1 idea in the top-10 and NS<=2 intersection) and ideator surprise correlates r=-0.11 with quality. So no run-based novelty measure that predicts success has been found. Proposed test: pass-rate lift after one refinement.
- Gap 10 (novelty check vs random): a retrieval-grounded grader exists (Heuresis, after Gupta and Pruthi) and retrieval at generation raises unique novel ideas (Nova, d16), but no study compares a grounded novelty filter with random selection. Open.
- Gap 8 (constraints): only indirect evidence. Humans patch the default rather than leave it under a hard constraint (d02); targeted release beat a generic creativity instruction (d03); verbal avoid list helped (d05). No test of O4 (drop a constraint) or ban-after-impasse found. Open.

Still open
- Gap 1 (parts-to-object on an LLM at equal tokens, code-checked): not run. This agent had no model access to run it, and none of the searches found a prior run. Protocol stays as in K25 agent_test.
- Gap 9 (McKnight 2006 robustness): not re-opened. Escholarship returned 403 and search quota ended. K06 stays single-source.

Corrections or cautions added by this pass
- Verma 2026 and Bilal 2026 are preprints from 2026 with no replication. Treat K27 as single-source.
- Heuresis uses an LLM with web search as the novelty grader; its zero-Original result is only as good as that grader.
- George and Wiley 2020 is on the alternate uses task, not parts-to-object.
- Ward 2002 is the same lab as Ward 1994; K26 is single-source despite four experiments.
