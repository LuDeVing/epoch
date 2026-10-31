# Critique: A13.04 Capacity hypothesis test (cross-check)

Claims file: claims.jsonl (A13.04-K01 to K18). Evidence read: evidence_a, evidence_b, evidence_c (evidence_d was empty).

## 1. Re-opened numbers (this pass, from text saved under D:/research_scratch/A13.04/)

Confirmed:
- Little et al. 2014: 130 recruited, slope 0.004, t(34)=2.87, p<.01, r2=.20 (PMC3968765).
- Smolen and Chuderski 2015: segmented adjusted R2 = .17 (N=347); quadratic adjusted R2 = .14 (N=347) and .23 (N=939), F(1)=134.68 and 11.71 (PMC4547002).
- Harrison et al. 2015: 208 with complete data, n=103 and n=105 in the two orders, repeated r=.50 vs novel r=.36, z(205)=-2.29, p=.02.
- Frischkorn and Oberauer 2021: ordinal agreement .91 to .98 between Pearson and point-biserial patterns; Pearson .33 to .41.
- Webb et al. 2023: OR=1.88 (p=.005, CI 1.21-2.91) generative; OR=6.27 (p=2.3e-8) multiple choice; unique rules OR=.61 (humans), .25 (GPT-3).
- REL (arXiv 2604.12176): 45% drop for REL-A as RC goes 3 to 9; 93% drop for REL-B1 (RC 5 to 20); RC explains 24/32/44% of explainable variance; 0.4% change from more test-time tokens on REL-C.
- NeuroCognition: one factor 75% of variance; text RAPM humans 0.430 (MC) and 0.444 (Gen).

Corrections:
1. Harrison et al. N: b19 said N=99 (snippet). Full text says 208 complete cases (103 + 105). a12 was right; b19 is wrong and should not be cited.
2. Smolen N=939 sample: the WM score there is the mean of short-term memory and relational integration tasks, NOT complex span (complex span exists only for the N=347 subsample). The 939 sample contains the 347 (both come from Chuderski 2013, 2015). Treat the two samples as overlapping and the WM measures as different. Evidence lines b03, c04 present them as two samples.
3. Smolen R2 figures differ by model, not by source: segmented .17/.22 (b03, a11) versus quadratic .14/.23 (c04). Both are right. Use the model name when quoting.
4. NeuroCognition human RAPM: the text-RAPM human figure comes from a pilot of N=9 per format. The 0.814 image figure is NOT from their humans; it is quoted from Zhang et al. The N=11 humans are for spatial working memory. a21 and c19 blur this. The statement "humans do better on image" rests on a borrowed number.
5. a21's SWM "humans .878 (hard)" is from the N=11 set; the c19 text shows 0.900 overall without history and 0.981 to 0.982 with full history. Different conditions, not a conflict.
6. b25 has a truncated phrase "93% on the ..."; the 93% figure is REL-B1 (history task), not a Raven task. Use c14 wording.
7. Dokic et al. 2025 (Intelligence 108, 101874): only title, DOI and volume were confirmed this pass (Crossref has no abstract). The N=543, task and null result are from the abstract page read by earlier agents. The review's study count is still unknown.

Not re-opened this pass (taken from the earlier agents, marked opened:true there): Unsworth and Engle quartiles (a02-a04), Chuderski 2013 and 2015, Colom 2015, Melby-Lervag 2016, Salthouse and Pink 2008. A Europe PMC pull of Melby-Lervag returned nothing usable.

## 2. Contradictions between sources

- Little 2014 (rising slope) vs Unsworth and Engle 2005, Smolen 2015, Dokic 2025 (flat or inverted U). Partly reconciled: Little needs a composite WM with r=.56. Smolen explains the rest by floor and ceiling. Frischkorn argues all of it is uninformative about capacity.
- Wiley 2011 (new rules drive the link) vs Harrison 2015 (opposite sign) and Smolen 2015 (no difference).
- Chuderski 2013/2015 (time lowers the WM-Gf link) vs Colom 2015 (not monotone, N=302). Different time ranges: Chuderski halves the time; Colom uses 20, 30, 40 min.
- Shojaee 2025 (collapse at high complexity) vs Lawsen 2025 (design artefact). Lawsen is preliminary.
- Gong 2024 (n-back capacity about 3) vs Hu and Lewis 2025 (task misunderstanding; strong models handle 10-back).
- K01 is labelled established for the empirical pattern, but K03 says that pattern does not test the hypothesis. Read them together: the item-wise null is solid, its meaning is weak.

## 3. Weak spots

- Almost all human evidence is Raven APM, mostly one lab group (Unsworth/Engle, Chuderski/Smolen). The same Chuderski datasets feed Chuderski 2013, 2015 and Smolen 2015, so these are not independent.
- Smolen and Chuderski also wrote the time-pressure papers; Frischkorn and Oberauer are the only fully separate theory source.
- Carpenter, Just and Shell 1990 and Kyllonen and Christal 1990 were never opened (a01, a17, c28).
- LLM evidence is thin and mostly 2026 preprints (REL, Patil, NeuroCognition, Gong 2026). REL used three models and 30x30 matrices; no human control. No LLM study tests the item-wise correlation design on its own terms.
- Output-length limits confound several LLM difficulty results (Lawsen; NeuroCognition disabled reasoning on two models).
- Melby-Lervag is one meta-analysis; effect depends on control group type (0.05 vs 0.20).
- No LLM study measures an LLM analogue of capacity (for example model size or context) against item demand with a proper mean-capacity sweep, which is what Frischkorn says is needed.

## 4. Seen only in snippets

a25 (backward digit span, 15 LLMs), b19 (Harrison N=99, wrong), b23 (Unsworth 2024 attention control, 90 samples), b24 (Kovacs and Conway), a14 (Embretson 1995), a17 (Kyllonen and Christal values from memory), a01, a06 (Salthouse 1993 via citations).

## GAPS

1. Does any LLM study vary model size or context capacity across several levels and test item-demand curves, as Frischkorn and Oberauer's design requires (peak should shift with capacity)? If none, can we run it at equal tokens on our agent?
2. What is the actual study count, inclusion rule and effect pattern in the Dokic et al. 2025 systematic review, and which studies did it count as supportive?
3. Has anyone replicated Little et al. 2014 with a multi-task WM composite and a different Raven form? If not, is the single positive result a chance finding?
4. For LLMs, does relational complexity (REL) predict failure better than empirically fitted IRT difficulty? Does fitted difficulty rank items the same way for different models?
5. Does the Webb 2023 unique-rule effect (rule diversity, not total count) hold for current reasoning models and for image-based Raven items?
6. Is the REL relational-complexity collapse affected by output-length limits and decomposition prompts (Lawsen's critique)? What happens when the agent decomposes by code (O3) at fixed tokens?
7. Does a time or token cap shift LLM failures towards hard items, as Chuderski found for humans (17.6% vs 3.7% late-item loss)? Compare Chuderski with the Colom failure to replicate.
8. What do Carpenter et al. 1990 and Kyllonen and Christal 1990 actually report (goal management, rule taxonomy, latent correlations .80 to .88)? Verify from the originals.
9. Are attention-control rivals (distractor interference) a better model of LLM failure than capacity? Hu and Lewis and Gong 2026 (readout under interference) suggest yes; test with a distractor-length sweep.
10. Can a rule-count budget rule be shown to lose to an empirical-difficulty budget at equal tokens on our own task bank?


## Gap search results (evidence_d.jsonl d01 to d18; claims K19 to K25 added; K01, K02, K06, K08, K10, K13, K17 updated)

Tool limits in this pass: WebSearch quota ran out after two queries; the arXiv API and Semantic Scholar were rate-limited; OpenAlex needed a key. Work was done through arXiv listing pages, PMC, Europe PMC, Crossref and a repository record. Full texts were read for Little 2014, Patil 2026, Ravulapalli 2026, REL, Webb 2024, Lawsen, Zhou 2026, Easy2Hard-Bench, Agent Psychometrics, Lewis and Mitchell, MaRs-VQA, Ghaffari 2026.

1. LLM size or context sweep against item demand: STILL OPEN (partial). Two sweeps exist, neither is the Frischkorn design. Patil 2026 (7 models, 8B to 235B): the parallel-branch collapse sits at 20 to 30 for every model, so the threshold did not move with size (d06, K19). Ravulapalli 2026: binding capacity K50 grows with parameters (exponent 0.82, R2 .73, up to 3B) but Pythia stays at k 3 to 6 from 410M to 12B (d07, K20). No study joins a capacity score to reasoning item demand (d18, K21; limited by the exhausted search quota). Running it on our agent remains the only route.
2. Dokic 2025 study count and coding: HALF CLOSED. The abstract (d01) says mixed evidence, a majority null, Little the main positive; it names Burgoyne 2019, Salthouse 1993, Unsworth 2014, Unsworth and Engle 2005, Wiley 2011 as null. The count, the inclusion rule and the table were not reachable. Do not quote a count.
3. Replication of Little 2014: CLOSED with a split verdict. Little reports its own second study with RSPM and a new sample (supplement not read; effect reduced with a weaker WM measure). Independent tests are null: Burgoyne 2019 (complex span and visual arrays, d02) and Dokic 2025 (d01). Treat the finding as replicated inside one lab, not outside; K02 is now "contested". Little's own simulation says the slope appears only when overall WM-Raven r is high (slope .0002 at rho .1 to .0016 at rho .9), so a null at moderate r is weak evidence either way.
4. REL vs fitted IRT, and cross-model agreement of fitted difficulty: STILL OPEN. Nobody was found who pits relational complexity or rule count against fitted IRT on matrices. Related facts: fitted IRT difficulty matches human pairwise judgment at 94.2% on GSM8K but 73.7% and 73.4% on ARC and Winogrande, and GPT-4 ranks agree with it only at Spearman .61, .22, .16 (d16); LLM-judged task features reach AUC .74 to .84 vs oracle IRT .92 to .95 (d17, K24). Cross-model rank agreement of fitted difficulty was not tested in anything found.
5. Webb 2023 unique-rule effect for reasoning models and images: STILL OPEN. Only plain GPTs on counterfactual alphabets (Lewis and Mitchell, d14; Webb reply, d11). MaRs-VQA (d15) shows attribute count gives a big easy-hard gap (57.78% to 21.74% for GPT-4o with CoT) but a non-monotone middle.
6. REL collapse vs output limits and code decomposition: PARTLY CLOSED. Output limits are a real confound (Lawsen: Lua function at N=15 in under 5,000 tokens, preliminary, d12). Code fixed an indexing step (Webb 2024, GPT-4 + code vs humans P=.496, d11) but did not remove the REL decline when the model still held the joint set (GPT-5.4 + RDKit recall .109, .094, .079; different model from the no-tool arm, so unpaired, d10). New claim K22 (contested): code helps when it does the binding; it does not help if the model must still carry the set.
7. Token cap shifts failures to hard items: PARTLY CLOSED. Zhou 2026 (d13): optimal budget 1.0K at MATH Level 1 to 7.5K at Level 5; AIME R1-32B 41.4% at 2K, 55.6% at 10K, 53.1% at 16K; 67.5% of 80 inspected negative flips are true overthinking. Direction matches Chuderski for hard items; the Colom (non-monotone) pattern has an LLM echo in the overthinking dip at high budgets. No Raven-type LLM version exists.
8. Carpenter et al. 1990 and Kyllonen and Christal 1990: STILL OPEN. Neither original could be opened. Second-hand from Little: rule tokens explained 57% of item-accuracy variance; the rule taxonomy and two production-system models are confirmed as described (d04). The .80 to .88 latent correlations remain unverified (d05). K25 carries this as single-source.
9. Attention control vs capacity in LLMs: PARTLY CLOSED. Binding-capacity paper finds interference and capacity not clearly linked (Spearman -0.473, p=.142; +0.20, p=.56, n=11; d08). Ghaffari 2026 (d09): accuracy needs an evidence margin growing with log of the effective distractor count; same-format distractors hurt most. Supports testing a distractor-count dial separately from load, but no direct comparison of the two accounts on one reasoning task exists.
10. Rule-count budget vs empirical-difficulty budget at equal tokens: STILL OPEN (needs our own run). Evidence points one way: structure predictors fall short of fitted ones (K24), attribute count is non-monotone (d15), and cap benefit depends on difficulty class (K23). Design: 1PL difficulty from several agent variants on the bank; arm A gives tokens by rule count, arm B by fitted difficulty, same total tokens; also a third arm with both as features.

Net: gaps 3 closed; 2, 6, 7, 9 partly closed; 1, 4, 5, 8, 10 open. Two cautions raised: the Little result is a same-lab replication only, and the Dokic study count must not be quoted.
