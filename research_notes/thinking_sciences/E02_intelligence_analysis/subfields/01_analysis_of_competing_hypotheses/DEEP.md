# Analysis of competing hypotheses (ACH): deep document

*Subfield E02.01. Sources: evidence_a-d.jsonl (ids a01-a30, b01-b29, c01-c25, d01-d15), claims.jsonl (K01-K21), critique.md in this folder. Status marks: [E] established, [S] single-source, [C] contested. Evidence date: 2026-11-03.*

## 1. What it is

ACH is an eight-step method for judging between several explanations. Richards Heuer described it in chapter 8 of "Psychology of Intelligence Analysis" (CIA, 1999). The core object is a matrix. Hypotheses go across the top. Evidence goes down the side. Each cell is marked consistent (C), inconsistent (I) or not applicable (N/A), sometimes with double marks for strong links (a01).

The eight steps (a01):
1. List all reasonable hypotheses. Heuer advises 3 to 7. Group more than 7.
2. List the evidence and the assumptions.
3. Build the matrix. Judge how diagnostic each item is.
4. Refine. Delete evidence that does not discriminate.
5. Draw tentative conclusions by trying to refute, not confirm.
6. Test how sensitive the result is to a few key items.
7. Report all hypotheses, not only the winner.
8. Set milestones that would show the picture is changing.

The ranking rule is the unusual part. Work down the columns. The hypothesis with the fewest inconsistent cells is the most likely. Consistent cells count for little, because evidence that fits any reasonable hypothesis is easy to find (a02). That rule throws away confirming evidence and base rates. It is not Bayesian.

Heuer's stated reasons (a03, a04):
- Holding 3 to 7 hypotheses and checking each against each item is beyond human working memory, so the matrix is an external memory.
- People generate few hypotheses. List first, evaluate second.
- Try to refute. Keep a hypothesis alive until it is disproved.
- He claims it "increases the odds of getting the right answer". He also says only the process and the audit trail are guaranteed, and that experts may drop the full eight steps.

Why it matters to us: ACH is the best-known structured analytic technique (SAT) for "keep several explanations alive and weigh evidence". Our schema has hypothesis-keeping and disconfirmation ideas (S2/S3, G1, G3). The question is whether a matrix procedure adds anything at equal tokens. From this study: no evidence that it does, some evidence that it hurts, and a few cheap parts that may help.

## 2. History and theories in depth

**Origin.** Heuer developed the method inside the CIA and published it in 1999. The chapter reports no experiment. It calls ACH "a surprisingly effective, proven process" (b23) but gives argument and one case (India's 1998 nuclear tests, where a deception hypothesis was kept alive). Heuer's own words, as reported by Mandel and Tetlock (a05): in a 15 Aug 2010 reply he said he would "ignore it and stick with my common sense judgment" if tests did not match how ACH is used in the community. Mandel and Tetlock call this the "goodness heuristic": a method that looks good on inspection gets adopted without test.

**Psychological roots claimed.** Cognitive psychology (limited working memory, confirmation bias), decision analysis (diagnosticity, likelihood ratios), and the scientific method (falsification) (a01). Heuer cites Gettys et al. 1980 on hypothesis generation (a03). Other background names (Tolcott on confirmation bias, Doherty on pseudo-diagnosticity) come from memory, were not opened, and carry no numbers here.

**Early evaluations (2004-2008).** MITRE ran the first controlled tests: Cheikes et al. 2004 and Lehner et al. 2008 (a16, a24, b17). 24 R&D employees judged three hypotheses about the USS Iowa gun explosion over four rounds of evidence. ACH cut confirmation bias only for people with no analytic experience; experienced analysts showed no effect. Cells were tiny (5 experienced in ACH, 7 in control). We saw this only through the Wilcox and Mandel review table; the MITRE PDF returned 403. Pirolli and Good (2004) tested a software ACH workspace; not opened (c25).

**The Mandel-lab programme (2018-2024).** The decisive tests come from one group:
- Mandel, Karvetski and Dhami 2018 (a06-a09, a23): 50 UK analysts. First randomised trial on real analysts.
- Dhami, Belton and Mandel 2019 (a10, b01-b04): process analysis of the same data.
- Karvetski, Mandel and Irwin 2020 (b12-b14, a17): 147 online adults, ACH vs a factorised Bayes method.
- Karvetski and Mandel 2020 (a11-a13, a22, b08-b11): 227 online adults, 6 cases.
- Wilcox and Mandel (online 2023, print 2024; a14, a15, a29, a30, b15, b16): critical review.
- Dhami et al. 2024 (a20, a21, b20, b21): layout study, students and 62 Dutch military analysts.

Outside the group: Lehner 2008, Whitesmith 2020 (a18, b18), Maegherman et al. 2021 (a19, b19), Martin 2025 (b22).

**Theory critique (Wilcox and Mandel).** Four named flaws (a15, b16, a22):
1. ACH claims to follow Popper, but Popper's rule applies to universal claims. Popper also rejected assigning probabilities to hypotheses and coarse inconsistency scores.
2. Ignoring consistent evidence, including base rates, goes against Bayesian and likelihood logic.
3. "Consistency" is never defined. It may invite the representativeness heuristic and inside-view thinking.
4. It is cognitively burdensome, pulls attention from natural reasoning, and may hurt competent reasoners while helping weak ones (a conjecture, untested).

Chang, Berdini, Mandel and Tetlock 2018 add "bipolar biases" (fixing one bias may cause its opposite) and "noise neglect" (many vague steps add noise) (b24; cited only).

**Coulthart 2017.** A review of SAT evidence, cited via Martin 2025: of 12 SATs in the US primer only six had any empirical test, ACH among them (b25). Our SUBFIELDS.md row says this review found "moderate to strong support" for ACH. That was not verified and conflicts with every controlled test found. Treat as unchecked.

**LLM era (2023-2026).** ACH is used as a prompt skill or a pipeline stage: Coulthart, Keller and Young 2023 (one GPT-4 demo, c12), practitioner tools (c13, c14), AgentCDM (b26, b27, c08-c10), PRISM (c01-c04), HypoArena (a27, a28, c05-c07, d01, d02), EMR-ACH draft (c15), Adversary Brains (d13). See section 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Heuer's claim that ACH raises accuracy was never tested in the founding text | 0 experiments in ch. 8; 8 steps | Heuer 1999 (a01, a04, b23) | [E] |
| ACH did not improve probability accuracy for 50 UK analysts (4 tribes, 12 cues) | MAE vs naive Bayes: control .21 [.17,.26], ACH .26 [.22,.29]; diff .04, p=.14, d=.43 favouring control; random guess .33 | Mandel 2018 (a06, b05) | [E] |
| ACH did not raise the chance of picking the right top hypothesis | 9/25 (36%) vs 8/25 (33%); chi2(1,N=49)=.04, p=.845 | Dhami 2019 (b01) | [E] |
| No coherence gain for 227 online adults, 6 cases | judgment-choice match .74, method d=.15, p=.25; Bayes agreement phi .65, d=.06; MAD from Bayes .31, d=.13 | Karvetski and Mandel 2020 (a11, b08) | [E] |
| ACH worse than the same people's earlier no-method answers (147 adults, mushroom task) | unitarity F(1,141)=22.12, p<.0001; additivity F(1,141)=4.18, p=.04 | Karvetski, Mandel, Irwin 2020 (b12) | [S] |
| ACH somewhat less coherent in additivity | sum of 4 probabilities: control 1.54, ACH 1.77 (ideal 1.0), d=.45, p=.13; additivity violations ACH .82 vs .56, p=.08; quantity-disagreement share .73 vs .50, p=.04 | Mandel 2018 (a07, b05) | [S] |
| ACH analysts used base rates less | 3/25 (12%) vs 13/25 (52%), chi2=9.19, p=.002 | Dhami 2019 (b03) | [S] |
| ACH users weight non-diagnostic evidence about 30% as much as diagnostic | slope B=.502, SE .082, p<.001, about 32%; robust check slope 1.20, about 30% | Karvetski and Mandel 2020 (a13, b10) | [S] (measured only in ACH arm) |
| ACH made answers less consistent across identical cases | .22 [.19,.24] vs .18 [.16,.20]; F=3.86, p=.051, d=.20 | Karvetski and Mandel 2020 (a12, b09) | [S] borderline |
| ACH raised quality of cue-usefulness ratings but not accuracy | rating vs true gain r=.68 [.61,.75] vs .17 [-.02,.35], d=1.59, p<.001; link to MAE r=-.10 ACH vs -.42 control | Mandel 2018 (a08, b06) | [S] unreplicated |
| ACH raised attention to diagnosticity, sensitivity checks and cue listing | diagnosticity 20/25 vs 8/25, p=.001; sensitivity 15/25 vs 1/25, p<.001; all 12 cues listed 92% vs 68%, p=.034 | Dhami 2019 (b03) | [S] |
| Trained analysts broke the ACH rules | 20/25 used consistent evidence; only 5/25 inconsistent-only; 1/25 (4%) applied the scoring rule consistently; final conclusion matched own matrix 16/25 (64%) | Dhami 2019 (b02, a10, a14) | [S] |
| Untrained analysts build a matrix by themselves | 20/25 control reformatted data; 16/25 drew a matrix (14 with hypotheses as columns) | Dhami 2019 (b04) | [S] |
| Post-hoc statistics beat ACH | coherentize: MAE .23 to .15 (-35%); mean of 50 coherentized: .09 (-61%); gains mostly at group size 1-3; random data gains too | Mandel 2018 (a09, b07) | [E] |
| ACH users double counted correlated cues, more when correlation was salient | factorised-Bayes arm distance .14 (SD .19) high vs .27 (SD .25) low salience, t(53.7)=2.15, p=.036, d=.56; row-copying under ACH | Karvetski, Mandel, Irwin 2020 (b13) | [S] |
| Everyone under-updates | distance from 50/50: elicited .13 [.11,.14] vs Bayes .33 [.31,.35], t(226)=23.20, d=1.54; ACH no change | Karvetski and Mandel 2020 (b11) | [E] |
| Review: 6 experiments (7 articles), ACH vs no technique, none with an overall gain | 244 hits; accuracy no difference in 3 studies; worse on reliability, base rates, pseudo-diagnosticity | Wilcox and Mandel (a14, b15) | [E] |
| Confirmation-bias benefit only for non-analysts | Lehner N=24; Whitesmith 8/39 (21%) biased, no ACH effect; Maegherman N=191, 38% compliance, no effect | a16, a18, a19, b17-b19 | [C] (snippet-level) |
| Layout matters more than method | confirm-only choice by layout chi2(2)=9.43, p=.009, phi=.24; rows p=.003; ACH columns p=.327; text p=.048; N=161 | Dhami 2024 Study 1 (a20, b20) | [S] |
| Most real analysts show no confirmation bias | N=62: 19.4% confirm-only, 14.5% disconfirm-only, 66.1% balanced; credibility-sensitive 98% / 72.7% / 33.3% | Dhami 2024 Study 2 (a21, b21) | [S] |
| Field data: ACH use does not track accuracy | n=138 reports, r=-.08; timeline .28, Bayes .22, evidence table .19; ACH coding reliability .79 [.32,1.00] | Martin 2025 (b22) | [S] |
| LLM: ACH stage in PRISM adds little | Direct 58.1, CoT 57.2, filter+judge 63.8, +MMO profiles 70.5 (+6.7), +ACH 71.3 (+0.8); 250 items, 10 models; +0.8 inside rough SE of 1.3 | Lee 2026 (c01-c03, d15) | [S] |
| LLM: zero-shot ACH decider gives a small gain | +2.0 to +2.3 all-average vs unstructured decider about 0 (-0.1 to -0.7); trained versions +7.0 to +11.6 | Zhao 2025 AgentCDM (b26, c08) | [S] |
| LLM: rigid scaffold training hurts | MMLU / MMLU-Pro / ARC-C: full 78.5/65.2/96.0; vanilla 72.6/52.5/89.0; scaffold-only 68.1/49.4/84.0 | Zhao 2025 (b27, c09) | [S] |
| LLM: skill library with ACH gives no uniform gain | 15 models, 988 cases; agent-minus-baseline +88 to about -60; Spearman -0.10 with baseline strength | HypoArena 2026 (a27, c06, d01) | [S] |
| LLM: ACH-like weight updates matter least in an investigator agent | full 79.2 [72.7,83.7]; no structured investigation 72.8; no counterfactual critique 74.0; no hypothesis expansion 76.5; no weight updates 78.5; direct 67.3 | Marozzo and Lio 2026 (c19, c20) | [S] |
| LLMs show confirmation bias in rule discovery; disconfirming tests help | success 6-78% in 45 turns; FalsifyBench rho -0.779 (bias vs success), -0.937 (bias vs falsification rate) | Jhaveri 2026, Bertolazzi 2026 (c16, c18, d11) | [E] |
| Cheap disconfirm prompts help, with model-type limits | mean success 42% to 56%; Think-in-Opposites better in 11/11, Dual-Goal 8/11 and hurt non-thinking (Qwen3-14B .23 to .13; Qwen3-32B .33 to .10) | Jhaveri 2026 (c17, d12) | [S]/[C] |
| LLM incoherence comes from a missing shared record | separate chats: over 50% of scenarios violate for most model-axiom pairs; one dialogue: 10% or 1 of 30 | Filbry 2026 (d03) | [S] |
| Joint elicitation of all related events removes incoherence | 14-event panel in one query: near the rounding floor (5e-5); coherence varies about 100x across 15 models while Brier barely varies (.1966-.2157) | Andrews and Sarkar 2026 (d06, d07) | [S] |
| Same-model samples are correlated | 95% of answers identical across 5 passes; homogeneous vs heterogeneous panel -4.65 to -34.62 points | Andrews and Sarkar (d08); Shen and Yao (d09, d10) | [S] |
| Reasoning mode fixes most Bayes slips; heavy harness no longer helps | non-reasoning: success at least 30% below oracle; reasoning model matched oracle up to 10 evidence items; naive prompt matched BED-LLM | Filbry 2026 (d04, d05) | [S] |

## 4. Mechanisms and models

### 4.1 The ACH matrix as an algorithm

Input: H = hypotheses (3-7), E = evidence items (with credibility). Output: a ranking of H.
1. For each e in E and h in H, a judge writes C, I or N/A (optionally double marks).
2. Drop rows where all cells are equal (non-diagnostic).
3. For each h, score = count (or weighted sum) of I cells. Consistent cells are ignored.
4. Rank: fewest inconsistent = most likely.
5. Sensitivity: remove the 1-3 most influential evidence items and recompute.

Cost for an LLM: one cell call per (e, h) pair, so |E| x |H| calls. ACH-Grounding states that token cost grows as (evidence + hypotheses) squared (c14). With 12 cues and 4 hypotheses that is 48 cells.

### 4.2 Why the minus-count rule is wrong

Bayes in odds form: posterior odds = prior odds x product of likelihood ratios. The minus-count:
- drops the prior (base-rate use fell from 52% to 12%, b03),
- drops the "C" evidence, which carries real likelihood ratios above 1,
- treats all I marks as equal in size,
- assumes cue independence without checking (double counting, b13),
- gives no probability, so there is no coherence constraint.

The one real overlap with Bayes is that evidence with equal likelihood under all hypotheses should have no effect. ACH tells analysts this. In practice non-diagnostic evidence still moved judgments with weight about 30% (a13).

### 4.3 What people may genuinely gain

1. **Externalising evidence and hypotheses** in a table (a30). Untrained analysts do this unprompted (b04). Rows-as-hypotheses beat columns (a20).
2. **Diagnosticity rating.** ACH-trained people rated cue usefulness with r=.68 vs .17 (a08). It is the only measured process gain. It did not reach the final answer.
3. **Exhaustive listing** of cues: 92% vs 68% (b03).

### 4.4 Statistical repair that works (implementable)

From Mandel 2018 (a09) and Karvetski 2020 (b12, b14):
- Coherentize: rescale probabilities of exclusive, exhaustive hypotheses to sum to 1 (normalisation gave MAE .13). Cut error 35% on average.
- Aggregate: equal-weight mean over judges. 61% error cut with 50 analysts. Most gain by 2-3 judges, and part of it is variance reduction (random responses gain too).
- Coherence-weighted averaging did not beat equal weights.

For an LLM, normalisation is code. Aggregation needs diverse judges (see 6.4).

### 4.5 A Bayesian alternative that can be coded

A factorised Bayes method (b12): elicit P(cue | h) for each pair, combine by naive Bayes with the prior, then coherentize. In human data, Bayes computed from elicited parts, once aggregated, was the most accurate for groups over 7 (b14). ACH lost to it at most group sizes. For an agent this is the better "matrix": cells hold likelihoods, not C/I marks, and code does the arithmetic (as ACH-Grounding does, c14).

### 4.6 Failure modes to guard against

- Matrix as decoration: the final answer does not follow the matrix (64% matched in humans, b02).
- Candidate compression: rich analysis squeezed into a narrow final set that drops plausible candidates (d02).
- Burden: more steps, more noise (noise neglect, b24).
- Rigid scaffold: training on a fixed protocol hurt generalisation (c09).

## 5. What holds up

**Holds up [E].**
- No controlled study shows an overall accuracy gain from ACH over no technique (a14, b15). Three accuracy tests show no difference: Mandel 2018 (N=50), Karvetski, Mandel, Irwin 2020 (N=147), Karvetski and Mandel 2020 (N=227).
- Medium effect sizes in 2018 (d about .43 to .52) favour the control but are not significant. Read this as "no evidence of gain", not "proof of harm". N=25 per arm is underpowered (a23).
- Statistical repair (coherentize and aggregate) gives large gains (a09, b07, b12).
- Everyone under-updates (b11).

**Weak or failed replications.**
- Confirmation-bias reduction: positive only in Lehner 2008 for non-analysts (N=24); null for analysts, null in Whitesmith (8/39) and Maegherman (N=191, 38% compliance, floor effect) (a16, a18, a19). [C]
- The rating-quality benefit (r=.68 vs .17) comes from one study. The review says none of the observed benefits has been replicated (b16).
- Layout effect: one student sample, 90% female, mean age 20 (a20).

**Moderators.**
- Experience: Lehner found benefit only without analytic experience. Dhami 2024 Study 2 found real analysts mostly unbiased (66.1% balanced). A "helps weak, hurts strong" pattern is possible and untested (a22).
- Compliance: 20/25 broke the rules; 38% used the matrix in the legal study; 62% did not use it in another. Tests measure "ACH as used", which is what Heuer said he would ignore (a05).
- Layout: hypotheses in rows beat columns (a20).
- Salience of correlation raised double counting (b13).
- Cognitive reflection: CRT unrelated to additivity (r=-.12) in Study 2, but low CRT predicted confirm-only in Study 1 (Glass d=.54) (b21).

**Interventions that worked.** Coherentization (-35% error), aggregation (-61% with 50), normalisation (.13). A one-line disconfirm prompt in LLMs (c17). Hypotheses-in-rows layout (a20).

**Interventions that did not.** Full ACH training (half-day, 2 hours, short explanation). ACH as a rescoring step (coherence worse after than before, b12). Coherence-weighted aggregation beyond equal weights.

**Limits of the evidence base.**
- One research group produced most human data, so K01, K02, K05 are less independent than their counts.
- Samples are students, crowd workers and junior analysts (mean 14 months of experience).
- Tasks are tiny quantified puzzles with a naive-Bayes truth. There is no messy, accuracy-scored field study except Martin 2025 (correlational).
- Lehner 2008, Cheikes 2004, Whitesmith, Maegherman, Chang 2018 and Coulthart 2017 were seen only as snippets or through reviews.
- The review is not a pooled meta-analysis; effect sizes were too different.

## 6. Language models

**Big picture.** No study compares an ACH matrix prompt against a plain prompt on one model at equal tokens (d14, K20). All LLM evidence is 2023-2026, mostly preprints, with bundled pipelines. Token cost is not reported in PRISM, AgentCDM, HypoArena or SIA (critique), so equal-token claims are unsupported.

### 6.1 ACH as a pipeline stage or skill

- **PRISM** (c01-c04, d15). MuSR murder mysteries, 250 items, 10 LLMs (GPT-5.2 plus 9 open models, 8B-70B), temperature 0, one run. Direct 58.1; CoT 57.2; persona 58.2; persona+CoT 58.0; self-consistency (5 samples) 63.2 (+5.1). Full PRISM 71.3 (+13.2); GPT-5.2 from 58.0 to 80.0. Ablation: filter+judge 63.8 (+5.7); add MMO profiles 70.5 (+6.7); add ACH 71.3 (+0.8, 11% of the gain; MMO is 89%). The +0.8 is about 2 questions per model; my rough SE is 1.3 points; the paper gives no interval. Ensembles and debate did not beat the best single model with PRISM (top-3 78.4, all-10 76.0, structured debate 77.6 vs 80.0). Gain was +12.2 for small and large models alike.
- **AgentCDM** (b26, b27, c08-c10). A decider agent treats other agents' answers as competing hypotheses. Zero-shot ACH decider +1.9 over an unstructured decider; all-average 67.9 (+2.0) vs single agent 66.0 and unstructured 65.8. Trained versions: Qwen-7B-R1 74.5 (+8.6), AgentCDM 77.5 (+11.6). Ablation: scaffold-only training 68.1/49.4/84.0 is worse than a vanilla prompt 72.6/52.5/89.0. Weak models (Mistral-7B) lose accuracy as agents are added; GPT-4 gains. Table text is garbled (critique); quote to one decimal at most.
- **HypoArena** (a27, a28, c05-c07, d01, d02). 15 LLMs, 988 cases, 6 domains. Agent mode (choose from 12 analytic skills including ACH) vs a single-pass baseline. Shift runs from +88 (kimi-k2.5) to about -60 (claude-opus-4.6; figure label -58). Rho -0.10 with baseline strength. Judge: seed-2.0-pro; against 1,500 expert pairs Kendall tau .90. There is no per-skill ablation, no usage count and no token cost. Named failure: candidate compression. A separate Diagnostic Reasoning skill exists but was never run alone. The ACH skill uses Heuer's minus-count unchanged.
- **SIA, LLM-as-an-Investigator** (c19-c21, a26). Competing hypotheses plus a counterfactual challenger plus cited evidence. 79.2 [72.7,83.7] vs direct 67.3 and "think of competing explanations" 67.5. Dropping a part costs: structured investigation 6.4, counterfactual critique 5.2, follow-up questions 4.2, final adjudication 3.2, hypothesis expansion 2.7, weight updates 0.7. Listing alternatives alone gave +0.2. Holds on other backbones at a lower level (+6.2 and +7.7 over THK-interactive). SIA also asks more questions (5.2 vs 3.7), so some gain is extra information. The wrong-suggestion stress test has only 10 paired cases (80.0 to 76.0).
- **EviDx** (c22). Clinical agent with evidence states and an observer that blocks early stopping. Claude Sonnet 4.6 scores 66% on JAMA and 52% on DiagnosisArena. Small models gain on multiple choice, but their evidence recall fell (Llama3.1-8B 63.8% to 15.1%). Bundled; not an ACH test.
- **Yousuf et al. 2024** (b28). Hypothesis-and-evidence tree memory with GPT-3.5. Mixed results (METEOR Atlantic Storm .25 vs .34; Manpad .33 vs .27). Old model; the output stayed at surface summary.
- **Practitioner tools** (c12-c15, b29, d13). GPT-4 demo (Coulthart 2023): a first draft at entry-level quality, one run, no ground truth. Roberts and ACH-Grounding: LLM fills cells, code totals; no benchmarks. EMR-ACH: results TBD; the N=79 pilot collapses to the majority class (83.4%). Adversary Brains: design only.

### 6.2 Confirmation bias and falsification in LLMs

- Jhaveri et al. 2026 (c16, c17, d11, d12). 11 LLMs, Wason 2-4-6 style game, 80 episodes per model variant. Success 6-78%. More disconfirming tests (I:C ratio) go with more success, in thinking and non-thinking modes. Think-in-Opposites better in 11/11; Dual-Goal 8/11 and it hurt non-thinking Qwen3-14B (.23 to .13) and Qwen3-32B (.33 to .10). Mean success 42% to 56%. Significant for thinking models only. Cost 1,000-2,300 tokens per thinking turn vs 6-24 non-thinking. Distilling the behaviour transferred to a Blicket test.
- Bertolazzi et al. 2026 FalsifyBench (c18). 12 LLMs. GPT-5.2-Chat 75%, GPT-OSS-120B 68%, DeepSeek-V3.1 41%, GPT-5-Nano 12%. Confirmation bias vs success rho -.779 (p=.003). Negative testing is the main driver of the reasoning models' edge.
- Meaning: LLMs have the bias that ACH targets, and a cheap disconfirm rule helps. No test shows the full matrix is needed for that gain.

### 6.3 Bayesian updating and coherence

- Reasoning mode fixes Bayes slips on independent evidence. Without it, final success is at least 30% below an oracle; with it, Gemma-4-31B matched the oracle for up to 10 evidence items. A heavy BED-LLM harness no longer beat a plain in-context prompt on current reasoning models (d04, d05). This is the best direct support for schema 4b.
- Incoherence is a missing-record problem: separate chats violate probability rules in over 50% of 30 scenarios for most model-axiom pairs; one dialogue cuts it to 10% or 1 of 30 (d03). A full-panel query of 14 events reaches the rounding floor (d07). Incoherence differs about 100x between 15 models; Brier barely (d06). Irrelevant context raises incoherence by up to an order of magnitude; a statistics-style context lowers it (d08).
- Humans in a matrix were incoherent within one sitting (K05), so human and LLM patterns differ.

### 6.4 Correlated samples

95% of answers were identical across 5 passes of one model (d08). Wrong majorities collapse onto one wrong answer (d09). Heterogeneous three-model panels beat same-model panels by 4.7 to 34.6 points (d10). The LLM form of double counting is treating repeated samples as independent evidence. This matches G4.

### 6.5 What changed behaviour, by how much

| Change | Size | Evidence |
|---|---|---|
| Evidence filter + MMO profiles in a pipeline (MuSR) | +5.7 and +6.7 of +13.2 total | c02 |
| ACH matrix stage added last | +0.8 (inside noise) | c02, d15 |
| Zero-shot ACH decider | about +2 (all-average) | b26, c08 |
| Self-consistency, 5 samples | +5.1 | c03 |
| CoT | -0.9 | c03 |
| Reasoning mode | removes a gap of at least 30% in success | d04 |
| Think-in-Opposites and Dual-Goal | mean success 42% to 56% | c17 |
| Joint elicitation | incoherence to near zero | d07 |
| Structured investigation / counterfactual critique | -6.4 / -5.2 when removed | c20 |

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Evidence ids in brackets.

### Add now (established)

1. **Do not add a full ACH matrix step. Keep it in 4b.** Part: G7 / 4b. [E]. a14, b15, a06, a11, b12 (K01, K09). Nothing shows a gain at equal tokens; several results show harm.
2. **Normalise probabilities over exclusive hypotheses in code, never by the model.** Part: G5 / O-aggregate. [E]. a09, b07, d03, d07 (K05). Already in G5 (35% cut). This study confirms it on ACH-like tasks. When probabilities are needed, elicit all hypotheses in one call and keep one belief table in context.
3. **Keep the prior and base rates explicit. Never drop consistent evidence.** Part: G (evidence weighting). [E]. b03, a15, a13 (K02, K17). The minus-count rule is the thing not to copy.
4. **Seek disconfirmation on a signal, not on a schedule.** Part: G1 / S4. [E]. c16, c18, d11 (K14). G1 already limits when; the cheap rule itself is in Test first.
5. **Samples from one model are not independent evidence; do not count them as separate cues.** Part: G4. [E]. d08, d09, d10, b13 (K17, K19). Already in G4. The cue-side version (merge duplicate or correlated evidence before weighing) is in Test first.

### Test first (single-source or contested)

6. **Diagnosticity step: rate each cue by likelihood ratio, drop non-diagnostic cues.** Part: S3. [S]. a08, b06, b03, c02, d02 (K03, K11). The only human gain found; PRISM's evidence filter gave +5.7. Test as a code-checked filter, not a full matrix.
7. **Evidence filter plus profile structure (MMO-like) before judging.** Part: S2/S3. [S]. c02 (K11). Largest contributor in PRISM. Test per task family.
8. **Hypotheses-in-rows layout for evidence.** Part: S3 format. [S]. a20 (K06). Cheap. Humans only.
9. **Disconfirm-first rule (Think-in-Opposites style).** Part: G / O-falsify. [S]/[C]. c17, d12 (K14, K15). Test on a thinking and a non-thinking model; Dual-Goal hurt non-thinking models.
10. **Investigate-critique-adjudicate loop with a counterfactual challenger.** Part: S3/O. [S]. c20 (K13). The gain comes from the full loop, not from listing. Token cost not given.
11. **Check that the final answer follows the stated evidence table (code check).** Part: G2/G10. [S]. b02 (K04). 64% matched in humans. Measures decoration.
12. **Hypothesis expansion only when a check fails.** Part: S5/S6. [S]. c20 (-2.7 when removed). Consistent with G1.
13. **Model-conditional structure.** Part: G12. [C]. d05, b27, d12 (K15, K18). Re-test each step on a reasoning and a non-reasoning model; drop it if the plain prompt ties.
14. **Merge duplicate or correlated cues by code before weighing.** Part: G (conditional independence). [S]. b13, d09 (K17, K19). Humans double count under ACH; no LLM test.

## 8. Concrete tests on our bench

All arms at equal total tokens (count setup, matrix cells, aggregation). Use at least two models: one reasoning, one not. Report the paired difference with an interval, not a single run (PRISM's flaw, d15).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Mandel-style items: 3-4 hypotheses, 8-12 probabilistic cues, computable naive-Bayes posterior; generated by program (300+) | plain; ACH matrix (C/I/N-A, minus-count); likelihood matrix with code Bayes; plain + normalise | MAE vs Bayes; top-1 hit; base-rate use | ACH matrix equal to or worse than plain (humans .26 vs .21); likelihood matrix + code at least equal; normalise gives about 20-35% lower MAE |
| T2 | MuSR murder subset (250) plus one non-murder task (e.g. diagnosis MCQs) | filter+judge; +profiles; +ACH; self-consistency at the same tokens | accuracy, paired bootstrap | ACH stage within 1 point; self-consistency may match the pipeline |
| T3 | Planted non-diagnostic cues (equal likelihood across h) and planted base-rate cues | plain; ACH matrix; diagnosticity-only step | shift per planted non-diagnostic cue; base-rate use | matrix raises non-diagnostic weight (humans about 30%); diagnosticity-only lowers it |
| T4 | Correlated cue pairs (duplicate wording, perfect correlation) | plain; matrix; matrix + code dedupe | double-counting distance (as b13) | matrix worsens it; dedupe fixes it |
| T5 | Rule discovery (2-4-6 style) plus hypothesis-ranking | plain; Think-in-Opposites; full ACH; Dual-Goal | success; I:C ratio; tokens | TiO beats ACH per token on thinking models; Dual-Goal hurts non-thinking |
| T6 | Probability items with 2-4 related events | separate calls; joint call; running table in context; + coherentize | incoherence (sum error, Dutch-book gap); Brier | joint call gives near-zero incoherence at lower cost |
| T7 | Order/anchoring items: same evidence in two orders | plain; ACH; diagnosticity-first; disconfirm-first | order effect (belief difference) | ACH does not reduce order effects (Whitesmith) |
| T8 | Does the answer follow the table | ACH matrix then answer | share of runs where the answer matches the matrix top | below 100%; low match means decoration |
| T9 | Layout: rows vs columns vs prose | 3 prompts | confirm-only choice rate | rows lower, if the effect transfers |
| T10 | 2-3 samples from one model vs 2-3 varied prompts | equal tokens | accuracy; error overlap | small gain from varied prompts; near zero from same-model |

## 9. What does not transfer, and why

- **Working-memory rationale.** Heuer's reason is human working memory (a03). An LLM holds the full evidence list in context. The matrix as external memory has less to give. It may still help attention (untested).
- **Audit trail.** ACH's value to institutions is a record for other people. Our agent needs correct answers; G10 says reasoning text is not evidence.
- **Training and compliance results.** Half-day training, 38% compliance and 20/25 rule-breaking are human adherence problems. An LLM follows the prompt literally, which could make the minus-count rule worse (HypoArena uses it unchanged, a28).
- **Bias profile.** Analysts mostly show no confirmation bias (66.1% balanced). LLMs do in rule discovery (c16). A cheap prompt may fix this without a matrix.
- **Task toy-ness.** Human tests used fully specified puzzles. LLM benchmarks (MuSR, MMLU, forum threads) differ again. No transfer in either direction is shown.
- **Aggregation by 50 analysts.** The 61% gain needs many independent judges. LLM samples from one model are 95% identical (d08).
- **Training gains.** AgentCDM's +7 to +11.6 comes from RL training, not from the ACH prompt (b27). We do not train.
- **Cost model.** Cell-by-cell matrices grow as |E| x |H|. For us tokens are the budget (G7).
- **Base-rate neglect.** Humans dropped base rates under ACH. Unknown whether LLMs do; they follow instructions that say to ignore consistent evidence.

## 10. Open questions

1. Does an ACH-matrix prompt beat a plain prompt for one LLM at equal tokens on items with known posteriors? No study (K20, d14).
2. Does diagnosticity rating alone give the human gain (r=.68 vs .17), and does it help LLM accuracy? HypoArena has a Diagnostic Reasoning skill never run alone (d02).
3. Is PRISM's +0.8 real? One temperature-0 run, one task, no interval (d15).
4. How much of the HypoArena spread (+88 to -60) is ACH and how much the other 11 skills? Candidate compression is only qualitative (d01, d02).
5. Do LLMs double count correlated cues and give non-diagnostic cues about 30% weight? Does a matrix make it worse? Untested.
6. Does coherentize-and-aggregate work for 2-3 samples from one model at equal tokens? Joint elicitation fixes coherence (d07) but averaging does little (d08).
7. Disconfirm-first vs full ACH, head to head, and the harm to non-thinking models (d12).
8. Is there any accuracy-scored field or tournament study of ACH use beyond Martin 2025 (n=138, r=-.08)?
9. What exact numbers did Lehner 2008 and Cheikes 2004 report? Seen only through reviews.
10. Do 2026 papers test ACH as an anchoring or order-effect debiaser? None found in preprints (d14); journal sources returned HTTP 403.
11. Does ACH help weak reasoners and hurt strong ones (a22)? For LLMs, does it help small models and hurt large ones? PRISM shows equal gain by size (+12.2), but for the whole pipeline.
12. Does matrix layout (rows vs columns) matter for LLM attention?

## 11. Sources

[V] = opened and read this study. [M] = snippet, abstract or second-hand only.

- [V] Heuer (1999) Psychology of Intelligence Analysis, ch. 8. https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
- [V] Mandel and Tetlock (2018) Correcting judgment correctives in national security intelligence. Frontiers in Psychology 9:2640. https://www.frontiersin.org/articles/10.3389/fpsyg.2018.02640/full
- [V] Mandel, Karvetski, Dhami (2018) Boosting intelligence analysts' judgment accuracy. JDM 13(6). https://jbaron.org/journal/18/18803/jdm18803.html ; https://doi.org/10.1017/S1930297500006628
- [V] Dhami, Belton, Mandel (2019) The analysis of competing hypotheses in intelligence analysis. Applied Cognitive Psychology 33(6). https://strathprints.strath.ac.uk/69049/ (step-level counts for a10 come via the review)
- [V] Karvetski and Mandel (2020) Coherence of probability judgments from uncertain evidence: does ACH help? JDM 15(6). https://jbaron.org/journal/20/200430/jdm200430.html ; https://doi.org/10.1017/S1930297500008159
- [V] Karvetski, Mandel, Irwin (2020) Improving probability judgment in intelligence analysis. Risk Analysis 40(5). https://osf.io/preprints/psyarxiv/fb9ej_v1 (journal text blocked; preprint opened)
- [V] Wilcox and Mandel (2023/2024) Critical review of the Analysis of Competing Hypotheses technique. Intelligence and National Security. https://osf.io/preprints/psyarxiv/an32t ; https://osf.io/preprints/psyarxiv/an32t_v1
- [V] Dhami, Belton, De Werd, Hadzhieva, Wicke (2024) Effects of task structure and confirmation bias in alternative hypotheses evaluation. Cogn. Res. Princ. Implic. 9:37. https://link.springer.com/article/10.1186/s41235-024-00560-y
- [V] Martin (2025) Relationship between structured analytic techniques and intelligence analysis quality. https://osf.io/preprints/psyarxiv/7p9v4_v1
- [V] Zhao et al. (2025) AgentCDM. arXiv 2508.11995. https://arxiv.org/abs/2508.11995
- [V] Lee, Kang, Shin (2026) PRISM, ACL 2026. https://aclanthology.org/2026.acl-long.1056.pdf
- [V] Zhong et al. (2026) HypoArena. arXiv 2607.15766. https://arxiv.org/abs/2607.15766
- [V] Marozzo and Lio (2026) LLM-as-an-Investigator. arXiv 2606.13220. https://arxiv.org/abs/2606.13220
- [V] Zeng, Zhang, Zhang (2026) EviDx. arXiv 2608.24570. https://arxiv.org/pdf/2608.24570
- [V] Jhaveri, GX-Chen, Sucholutsky, Choi (2026) Failing to Falsify. arXiv 2604.02485. https://arxiv.org/abs/2604.02485
- [V] Bertolazzi, Tentori, Bernardi (2026) FalsifyBench. arXiv 2606.04751. https://arxiv.org/pdf/2606.04751
- [V] Filbry, Melo, Gal (2026) From Prompts to Posteriors. arXiv 2610.29331. https://arxiv.org/abs/2610.29331
- [V] Andrews and Sarkar (2026) Dutch Books for Language Models. arXiv 2609.02797. https://arxiv.org/abs/2609.02797
- [V] Shen and Yao (2026) Not All Test-Time Compute Is Evidence. arXiv 2610.23213. https://arxiv.org/abs/2610.23213
- [V] Evron (2026) Adversary Brains. arXiv 2610.35624. https://arxiv.org/abs/2610.35624
- [V] Yousuf et al. (2024) LLM Augmentations to support Analytical Reasoning over Multiple Documents. arXiv 2411.16116. https://arxiv.org/abs/2411.16116
- [V] Liu, Neubig, Andreas (2024) An Incomplete Loop. COLM. https://arxiv.org/pdf/2404.03028
- [V] Coulthart, Keller, Young (2023) What ChatGPT can and cannot do for intelligence. Lawfare. https://www.lawfaremedia.org/article/what-chatgpt-can-and-can-t-do-for-intelligence
- [V] Roberts (2025) LLM SATs FTW, and suprathermal ACH-Grounding (2024), as summarised at https://mattdot.github.io/sats4llms/concepts/analysis-of-competing-hypotheses
- [V] Aperstein, Remez, Apartsin (2026) EMR-ACH draft. https://apartsinprojects.github.io/EMR-ACH/paper/index.html
- [V] arXiv listing sweep, 2026-11-03. https://arxiv.org/search/?query=%22competing+hypotheses%22+language+model
- [M] Lehner, Adelman, Cheikes, Brown (2008) Confirmation bias in complex analyses, IEEE Trans. SMC-A 38(3); Cheikes et al. (2004) MITRE 04-0985. https://www.mitre.org/news-insights/publication/confirmation-bias-complex-analyses
- [M] Whitesmith (2020) Cognitive Bias in Intelligence Analysis: Testing the ACH Method. Edinburgh University Press (via Wilcox and Mandel).
- [M] Maegherman, Ask, Horselenberg, van Koppen (2021) Test of the ACH in legal decision-making. https://doi.org/10.1002/acp.3738
- [M] Chang, Berdini, Mandel, Tetlock (2018) Restructuring structured analytic techniques in intelligence. https://doi.org/10.1080/02684527.2017.1400230
- [M] Coulthart (2017) review of SAT evidence (via Martin 2025). https://osf.io/preprints/psyarxiv/7p9v4_v1
- [M] Pirolli and Good (2004) Evaluation of a computer support tool for ACH. https://www.cse.sc.edu/~mgv/BNSeminar/UITR.doc

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 6 established claims: 1 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E02.01-K01** (now single-source: the sources are not independent). All three experiments come from one research program (Mandel is an author of all; Karvetski of two of them, with the third by Mandel, Karvetski and Dhami), so 'two labs' is wrong, and the N=147 study found ACH decreased coherence, not 'no difference'; MAE .26 vs .21 (N=50, p=.14) and N=227 no advantage are correct.
- **E02.01-K02** (now single-source: the sources are not independent). Dhami 2019 (12% vs 52% using base rates, n=25 per group, p=.002) and Karvetski and Mandel 2020 (non-diagnostic evidence weight about 32% / 30%) both come from Mandel's group; also the Karvetski and Mandel participants were 227 graduates, not trained analysts.
- **E02.01-K05** (reworded: the sources support less). ACH-vs-control coherence difference was not significant in the 50-analyst study (sum 1.77 vs 1.54, p=.13); it was significant only in the separate 147-person study from the same group; the 5-sample averaging result was measured on GPT-OSS-120B only. MAE .23 to .15 and pool .09 verified. Corrected claim: In Mandel et al. 2018 both ACH and control probabilities summed above 1 (1.77 vs 1.54), a difference that was not significant (p=.13), while a separate 147-person study from the same group found ACH decreased coherence; coherentizing cut mean absolute error from .23 to .15 and averaging all 50 coherentized judgments gave .09. For LLMs (2026), judgments elicited in one dialogue violated probability rules far less than across separate chats (10% of scenarios for Gemini-2.5-Pro, 1 of 30 for Gemma), eliciting a full panel of 14 related events in one query brought incoherence near the rounding floor, and for GPT-OSS-120B averaging up to 5 samples helped only modestly because 95% of answers were identical.
- **E02.01-K09** (reworded: the sources support less). Heuer's quoted 2010 reply (via Mandel and Tetlock) was conditional: he would ignore testing that does not replicate how ACH is used in the Intelligence Community, not tests that failed; the two review sources share an author (Mandel). Heuer's 'increases the odds of getting the right answer' and 'proven process' are confirmed untested. Corrected claim: A critical review of six ACH experiments (Wilcox and Mandel) found no accuracy benefit and some harm, and no randomized test shows ACH improves accuracy; Heuer (1999) asserts that ACH 'increases the odds of getting the right answer' without citing a test, and per Mandel and Tetlock (2018) Heuer replied in 2010 that if testing did not replicate exactly how ACH is used in the Intelligence Community he would be inclined to ignore it and stick with common sense.
- **E02.01-K17** (reworded: the sources support less). Wilcox and Mandel's theory critique covers ignoring confirming evidence (including base rates) and Popper, but double counting of correlated cues is an empirical finding of Karvetski, Mandel and Irwin (same group) that the review only lists among harms, not a theory-level flaw they identify; the 0.14 vs 0.27 cue-distance figure is from the Karvetski preprint. Corrected claim: Wilcox and Mandel (2023) argue on theory grounds that ACH tells analysts to ignore consistent (confirming) evidence, including base rates, and their review lists as an empirical harm that ACH users double counted perfectly correlated cues, more so when the correlation was made salient (Karvetski, Mandel and Irwin 2020, same research group).
