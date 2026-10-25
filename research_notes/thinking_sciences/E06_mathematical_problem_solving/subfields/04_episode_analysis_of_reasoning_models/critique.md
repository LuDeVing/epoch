# Critique: episode analysis of reasoning models (E06.04)

Cross-check of evidence_a, evidence_b, evidence_c. Claims are in claims.jsonl (E06.04-K01 to K23).

## Numbers re-opened this session (10 checks)

Sources re-read: arXiv 2509.14662 (PDF text), arXiv 2512.19995 v1 (HTML), 2501.18585 (HTML), 2509.19284 v1 (HTML), 2510.08308 v1 (HTML), 2506.04210 (HTML), 2412.21187 (HTML).

1. 0.805 accuracy and kappa 0.764 for GPT-4.1 with examples and guidebook (Table 4, 2509.14662): confirmed. 38 responses, 915 paragraphs, 3,087 sentences: confirmed. The 30% test subset is about 11 responses, so about 900 sentences, with no interval reported.
2. Same paper, Table 2: the same GPT-4.1 example+guidebook setting scores 0.681 on sentences (0.757 paragraphs). So the headline 0.805 and the 0.681 are two different numbers for nominally the same labeller. The paper does not explain the 12-point gap (test split vs all data is the likely cause). Treat 0.805 as an upper figure on a small split.
3. Confusion matrix diagonal for GPT-4.1 sums to 80.5 percent: confirmed. Analyze-to-Verify 4.8 and Implement-to-Verify 3.2: confirmed.
4. ThinkARM gold set size: **correction.** b01 says "7,067 sentences from 99 problems". The paper says the gold set comes from 9 problems chosen from the 100 sampled (a10 and c05 had it right). b01 is wrong.
5. ThinkARM Table 5 efficiency numbers: **correction.** b04 reports ThinkPrune Verify 7.31 and Arora-Zanette Verify 4.63. The table columns are Read, Analyze, Plan, Implement, Explore, Verify, Monitor, Answer. Those two values are the Monitor column. Correct Verify values: baseline 11.43, L1 6.99, ThinkPrune 8.37, A&Z 9.94. a15 and c08 were right. New observation from the same table: Monitor share rises from 1.84 (baseline) to 8.52 (L1), 7.31 (ThinkPrune), 4.63 (A&Z). Shortened models say "let me think" style filler more, not less.
6. Lasso coefficients (Table 4, Explore-to-Monitor +0.41, Explore ratio -0.54): confirmed in the HTML text. New facts: features were z-scored, C=0.5, liblinear, 500 traces, about 75 features, and no held-out accuracy, AUC, cross-validation or confidence interval is reported. The "predicts correctness" wording in the evidence files is stronger than the paper supports; it is an association table. The Imp-to-Read value is -0.32 in Table 4 and -0.33 in Table 7 per b03; I did not re-check the second digit.
7. Wang et al. (2501.18585): 225 percent more tokens and 418 percent more thought switches in incorrect than correct responses: confirmed, stated for two open o1-like models (QwQ-32B-Preview and R1-Preview) in the intro; the third model (R1-671B) is added in the later tables. Over 70 percent of wrong responses hold a correct thought and over 50 percent have more than 10 percent correct thoughts: confirmed. The 225 percent figure is a raw difference and does not control for question difficulty; Feng et al. is the controlled test.
8. Chen et al. (2412.21187): 1,953 percent more tokens, 13 solutions, first round correct in over 92 percent of cases and under 60 percent of tokens: confirmed. 901 tokens and 35.8 percent process efficiency: confirmed (39+109+39+29+29+19+59 over 901).
9. Feng et al. (2509.19284): R1 first failed branch removed 20.89 (+-1.36) to 29.42 (+-1.66): confirmed. New: depth of the first failed step has little to no correlation with correctness, so it is the amount of failed work, not its timing.
10. Kang et al. (2510.08308): over 90 percent of reflections confirmatory, corrective mostly under 2 percent: confirmed. Ma/Ghosal (2506.04210): 82.2 to 87.3 percent from 385 to 1,100 tokens, then 70.3 percent at 15,980: confirmed.

Not re-opened: Thought Anchors, Gandhi, Kargupta, Thoughtology, Lu et al., DEER, probing paper, TRACE, AgentThink, Chen and Wang 2026, s1. These numbers are as the earlier agents reported them.

## Contradictions and tensions

- Verify direction. ThinkARM's Lasso gives Verify ratio +0.21 (more Verify goes with correct), Read-to-Verify +0.27, Answer-to-Verify +0.22. Feng et al. find review ratio negatively tied to accuracy within a question for most models (Claude 3.7 on math is the exception). Kang et al. find most post-answer reflection confirmatory with tiny gain. These agree only if the useful Verify is at the start and end and short, and the harmful one is repeated mid-trace. Nobody tested that. Treated as contested (K12).
- Wait/budget forcing: s1 gains on AIME24, Ma et al. loses accuracy at long extensions. Different base models and budgets; unresolved (K11).
- ThinkARM says efficient methods cut Verify; Hassid and Kang say much of that Verify was wasted. Not a contradiction but ThinkARM does not report accuracy per method in the pieces seen, so "what was cut" and "what was lost" are not linked.
- Non-reasoning vs reasoning easy-problem Verify: Qwen3-32B reasoning 55.89 percent Verify on GSM8K vs DeepSeek-R1 8.19 percent on the same set. Large model-to-model spread; one number per model, no variance.

## Weak spots

- Everything on Schoenfeld labels comes from one research group (Li, Fan, Cheng, Feizi, Zhou and co-authors). 2509.14662 and 2512.19995 are not independent. No external replication of the labels was found.
- Labels are produced by an LLM (GPT-5) and checked on 7,067 sentences from 9 problems. Reasoning-model sentences are harder than non-reasoning ones; Verify confusion is the known weak class.
- The correctness case study is 500 traces, 5 models, no held-out test. Models, problems and difficulty are mixed in one regression, so episode ratios may stand in for difficulty.
- Most "wandering" evidence is on math (MATH500, AIME, GSM8K), and o1-like open models of 2025. Little on code, agents or tool use (one project page).
- No source measures a detector. Claims K21 and K22 are about absence.
- Human side is second-hand: the 1985 book, 1992 chapter, and Harskamp and Suhre (2007) were not opened. Artzt and Armour-Thomas (27 students) was only seen in an abstract.
- Several evidence lines come from abstract pages with no numbers (Pipis, Su et al., Gandhi, Capable yet Parsimonious).

## Snippet-only items (opened false, or marked true on abstract only)

a01, a02, a03, a04, b22, c26 (Pi Loop Police search snippet), c28 (survey summary, "41 to 52 percent of reasoning tokens after answer commitment" is second-hand), c25 (abstract only), b16 (Chen and Wang 2026, no per-category counts), b21, b20, c12.

Environment note: the disk holding the temp folder ran out of space during this check. I deleted only my own downloaded files (PDFs and HTML in my scratch folder). Other agents' PDFs in the shared scratch folder were not touched. The user may want to free space.

## GAPS (open questions, most decision-relevant first)

1. Does any Schoenfeld-label feature predict failure on a held-out set better than length alone? ThinkARM reports coefficients but no AUC. This decides whether an episode-coded detector is worth building.
2. What is the precision and recall of a cheap impasse or wild-goose-chase detector (switch rate, revisit count, repeated n-grams, failed-branch share) against human-labelled stuck points, and what action should it trigger? No measured detector exists.
3. Which Verify is useful? Early and final checks (Read-to-Verify, Answer-to-Verify) correlate with success while mid-trace review loops correlate with failure. A controlled test that separates them is missing.
4. Do Schoenfeld episode statistics transfer from math to code, planning or agentic tasks? Only one project page covers agents.
5. Is the difference in Table 2 (0.681) vs Table 4 (0.805) in 2509.14662 a split effect or a prompt effect, and is a small fine-tuned BERT (0.732) enough as a cheap labeller for online use?
6. Does a scaffold-level thought-switch rule (finish or declare abandoned before switching) reproduce the gain of decoding-time TIP at equal tokens?
7. What is the human baseline? Original Schoenfeld episode statistics (share of attempts with no monitoring, timeline-graph numbers) were not verified; the book and chapters need to be read directly.
8. When does extra thinking help? The s1 vs Ma/Ghosal conflict needs a study varying difficulty, model and budget together, and ideally a probe-based stop (DEER-style) in a black-box scaffold.
9. Why does Monitor share rise in length-penalised models (1.84 to 8.52 percent in L1)? Is it filler that can be dropped or a compensating control act?
10. Are failed-branch pruning effects (+8.5 points on edited traces) preserved when the pruning is done by a summary note in context rather than deleting text?

## Gap search results (evidence_d.jsonl, d01-d16; claims K24-K29 added, K02, K08, K12, K13, K19, K21, K22 updated)

Search note: the web search quota ran out early, and arXiv, Semantic Scholar and OpenAlex rate-limited the API routes. Papers were opened through arxiv.org/html and /pdf directly. Forward-citation search from ThinkARM was therefore not done.

### Correction to the earlier critique (important)
The "Monitor" values in ThinkARM Table 5 were misread twice. The column order is Read, Analyze, Plan, Implement, Explore, Verify, Answer, Monitor. 8.52 (L1), 7.31 (ThinkPrune) and 4.63 (Arora-Zanette) are the Answer column. Monitor is 1.84 (baseline), 1.64, 1.80, 1.64. Verify values 6.99, 8.37, 9.94 are right. The earlier correction in b04 (that 7.31 and 4.63 were Monitor) was itself wrong. Fixed in K13 (d14).

### Closed or mostly closed
- Gap 9 (Monitor rises under length penalty): CLOSED by correction. There is no Monitor rise. Answer share rises because answer-writing is a fixed cost (208 vs 376 tokens) over a trace four times shorter.
- Gap 5 (0.681 vs 0.805; BERT as labeller): MOSTLY CLOSED. The paper says Table 2 is all data and Table 4 is the 30% test subset (about 11 responses), so it is a different evaluation set. ThinkARM's larger gold set gives GPT-4.1 86.10% accuracy, kappa 82.74, so 0.805 is not out of line, and the 0.681 looks like a small-data, prompt-design number. Whether the subset was easier is still not shown. BERT 0.732 / kappa 0.671 is below our 0.75 bar, so it is a logger, not a gate.
- Gap 10 (failed-branch pruning by a note): PARTLY CLOSED. Feng's summary arm keeps 85% / 92% of the delete gain for R1 and 17% / 81% for GPT-oss-120B. The summary is not a one-line dead-end note, so a one-line note is still untested.

### Partly answered
- Gap 1 (episode features vs length on held-out data): No Schoenfeld-label test found. Closest: Bloom features AUC 0.676 vs 0.613 length-only (nested CV, 9,132 samples); ReasonOps within-problem AUC 0.701 vs 0.551 for length. The gain is real but modest, and wait and backtrack counts already beat length. Decision: a coded detector is worth building only if it uses cheap counts and oscillation (Evaluate/Analyze back-and-forth), and is judged within problem. Do not expect AUC above 0.7.
- Gap 2 (detector precision and recall): Only white-box probes have measured accuracy (word-salad probe 78-93%, ROM AUROC 0.928) and labels are machine-made. No text-only detector against human stuck points. SmartSwitch shows intervening at every switch hurts (20.0 to 18.9), so the action must be gated by a second check.
- Gap 6 (prompt rule vs TIP): On one small model, a bare prompt rule gave 29.0 vs 28.9 vanilla, TIP 31.3. So a bare rule does not reproduce TIP there. Not tested on a frontier model, not at equal tokens, and not with a scaffold that checks the dropped thought.
- Gap 8 (when thinking helps): Difficulty matters. ReasonOps: the forward-stepping signal exists on easy problems (AUC 0.76) and vanishes on hard (0.48). No study varies difficulty, model and budget together; DEER-style black-box stop is untested.
- Gap 3 (which Verify helps): Tension is smaller than thought. Feng's Review is broader than Verify (it includes rewinds and restating) and its labeller agrees 90% with humans. ThinkARM Answer-to-Verify is a final check. Still no controlled test of check placement.

### Still open
- Gap 4 (transfer to code, planning, agents): Only descriptive Bloom profiles on non-math tasks (back-loaded verification holds) and AgentThink's 20-trace judge validation. ReasonOps predictive signal holds on LiveCodeBench (0.795) but not on BBH or HumanEval.
- Gap 7 (human baseline): Berkeley PDF paths 404, Harskamp and Suhre 403. No figures verified. Keep the Schoenfeld percentage out of the schema.

### Updated priorities
1. Build the within-problem logging test (K24): wait count, backtrack count, switch count, Evaluate/Analyze oscillations vs length, problem-grouped folds.
2. Run the three-arm Verify test (K26) at equal tokens.
3. Test a one-line dead-end note against a summary and against deletion (K08).
4. Treat any detector as an advisory flag with a second check before action (K19, K21).
