# A10.08 Problem finding: cross-check critique

## Numbers re-opened (from text saved under D:/research_scratch/A10.08)
1. Meta-analysis (a16-a18, Abdulla 2016 dissertation): r=.22, CI .11-.32, k=40, N=6,649, 196 effects, Q(195)=15,480.27, I2=98.74%. Confirmed. Outlier removal .220 to .196 (r=.99, N=2,636) confirmed. Egger t=5.52 confirmed. Age: children .297, adolescents .113 (CI .039-.185), adults .207. Confirmed.
2. CORRECTION to a18: the fluency moderator (r=.314) has CI -.084 to .625, so it is not distinguishable from zero; only originality (.291) and flexibility (.149) are clearly positive. Also the creativity-measure moderator was not significant (DT .196, product .248).
3. Reiter-Palmon and Murugavel (a23/b08): F(1,63)=2.06, p=.078, eta2=.03 confirmed as printed. NOTE: F(1,63)=2.06 corresponds to a two-tailed p near .16, so the reported .078 looks one-tailed. Treat as no effect.
4. Si et al. (b18 vs c11): per review 4.84 / 5.64 / 5.81 (N=109 reviews each); per idea 4.86 / 5.62 / 5.78 (N=49). Both are right; c11 mixes the two sets of conditions. Use per-idea means with the per-idea N.
5. Shin et al. (b14, b15, c01, c02): N=456 recruited, 280 kept; experts 12.54% more novel (p=.01); free-form 20.84% gap not significant. Confirmed. Test statistic is reported as Z in b15 and t in c02; the paper's symbol did not survive text extraction, so do not quote it.
6. QuestBench "not sure" rates 1.4%, 4.6%, 0.7% against 41.8% (a31): confirmed.
7. Edwards and Schuster (a33): 54.8 / 61.2 / 70.4 / 69.4, p=.621 confirmed. Added: Kimi K2.6 interactive baseline was only 47.2% from instruction failure, so the "interactive" comparison depends on the model.
8. van de Kamp (b04/b05): variance partition 0.89 and 31% explained confirmed in the chapter text. Sample is 11 students.
9. Linnell and Reiter-Palmon (b13): N=155, beta .41 and .29 confirmed.
10. MiP overthinking (c08): direction (longer, rarely abstain, o1 an exception) confirmed; the "2x to 4x" token figure was NOT found in the text and stays unverified.

## Contradictions between sources
- Original Getzels follow-up: 5, 6, 7, 11 or 18 years and 27 of 31 or all 31 located, depending on source. No primary text seen.
- Meta-analysis says children show stronger links than adults, against Arlin's post-formal idea; the drop in adolescents (.113) is unexplained and may be sampling noise.
- Divergent thinking vs problem finding: positive (Artley r=.47, Hoover .34 to .41) vs negative (Arlin fluency -.18, Lee and Cho -.17). Quality and quantity scores diverge.
- LLM novelty: positive when raters judge generated ideas (Si, 2024) vs null when LLM helps people reframe (Shin, 2025). Different tasks, so not a refutation, but no study bridges them. LLM judges are unreliable on both (a28, b19).
- Dorst-frame prompt: preferred in N=7 (b16) vs null in N=280 (b14, with a structured Dorst arm). Outcome measures differ.

## Weak spots
- The core human evidence rests on one 2016 dissertation meta-analysis (heterogeneity 98.7%) and secondary descriptions of the 1976 study. The primary book and its coefficients were never opened.
- No direct replication of the still-life experiment; all "replications" are conceptual with N of 11 to 77.
- Most LLM evidence tests neighbours (asking questions, spotting missing premises, rewriting), not problem finding in the Getzels sense. No LLM version of the paradigm exists (a35).
- Several LLM items are preprints with no peer review (a28, a29, a33, b17, c19, c20).
- c13 authors unverified; c19 and c22 not opened (opened false).
- a27, b01, b02 are web summaries only (opened false).

## Seen only in snippets
a27, b01, b02 (follow-up counts), c19 (FirstResearch), c22 (Loose LIPS "0.99 bits"). Treat as leads.

## GAPS
1. Does an explicit open-mode phase (explore many framings before committing) beat commit-first at equal tokens on open-ended agent tasks, rated blind by humans? No LLM test of the Getzels paradigm exists.
2. Under what conditions does an O8 reframe help? Candidate boundaries: cue inconsistency (Reiter-Palmon), task type (step-back helps physics, not GSM8K), user expertise (Shin). Needs a matched-token gating experiment.
3. Is the missing-information check (S1) worth its tokens? Edwards shows +8 points with a separate detector on code; is it replicated on non-code tasks, and what is the false-alarm cost on well-specified items?
4. How can reframe quality be scored without a same-model LLM judge, given the novelty mirage and near-chance judge accuracy? Which cheap proxy (downstream solution success, expert panel, dedupe count) tracks human ratings?
5. What do the primary coefficients of the 1976 study and its follow-ups actually show (r values, N per cell, how problem finding was scored)? Obtain the book or the 1971 Csikszentmihalyi and Getzels paper.
6. Does reframing raise harmful output or constraint violations in agents as it does in people (beta .29)? Needs a measured harm rate with and without O8.
7. Why is the problem-finding to creativity link weakest in adolescents (r=.113) and strongest in children? Is the age pattern real or a moderator confound (domain, measure)?
8. Do structured frame templates (Dorst nine steps, Abdulla and Cramond hierarchy) beat a plain "restate the problem" prompt for LLMs at equal tokens? One tiny positive study (N=7) and one large null exist.
9. Can program-side information-gain scoring of candidate clarifying questions (Battleship results) transfer to open problems where the hypothesis space cannot be enumerated?
10. Are reasoning models' early suspicion of a missing premise (c09) exploitable by an early-exit rule that converts suspicion into a clarifying question, and what does it save in tokens?

## Gap search results

Evidence in evidence_d.jsonl (d01 to d19, 16 opened, 3 not). Claims K27 to K37 added; K09, K13, K16, K17 and K23 amended. Search tools were limited (arXiv keyword API weak, OpenAlex refused anonymous use), so a null result is not proof of absence.

Closed or mostly closed
- Gap 9 (information-gain questions on open problems): answered in part. Exact scoring needs an enumerable space (Battleship, d08). For open spaces, sampling the model's own candidate solutions and splitting them works (d07: 20-questions with free guesses, 48 code tasks) but the gain shrinks for stronger models and costs more calls. K17 raised to established (3 sources). Not tested: truly open design problems.
- Gap 10 (early exit on suspicion): half closed. A keyword-based stop rule saves 38 to 70% of tokens on ill-posed items at 1 to 6% false stops (d05, 12 models). Generic early exit saves 12 to 22% (d06). Still missing: turning the stop into a clarifying question and measuring final answer quality. The unverified "2x to 4x" figure (c08) stays unverified.
- Gap 3 (S1 worth its tokens): partly. Non-code support exists (d10: structured ask-or-answer 88.0 vs 57.9 average at equal passes) and code costs of missing info are 8 to 20 pass@1 points (d11). The false-alarm side shows a real cost: a check carried in the main prompt lowered success 28.6 to 27.0 on average and up to 13 points on hard tasks (d09), and the structured agent lost accuracy where the user had already answered (d10, Qwen P 96.6 to 85.3). Design consequence: run S1 as a separate call or trigger. No first-turn false-alarm rate on fully specified items was found.

Narrowed, still open
- Gap 5 (primary coefficients): half closed, still second-hand. Moore (1985) gives the scoring recipe, r=.65 (N=31) and r=.42; Abdulla gives r=.54 for the 1971 paper (d02, d03). The three disagree on which pair is which. The book and the 1971 paper remain unopened; the only full copy found was on an unofficial host and was not used. K28 marked contested.
- Gap 4 (scoring reframes): judge limits confirmed with a non-same-family judge (d13: tau .31 elaboration, .17 novelty, about 0 surprise; metrics at or below .29). One candidate proxy, quality-gated distinct-output count (d14) and CreativeDC's Vendi count against expert clusters (d12), is plausible but never validated on reframes. Open.
- Gap 1 (open-mode vs commit-first): one small supportive test, CreativeDC (d12: 12 vs 8 distinct high-utility tasks, 96.67% of 20 novelty pairs, 3 experts). Tokens not matched, one domain. Open.
- Gap 2 (when O8 helps): one more boundary (d17: surface rewording helps weak models on varied phrasing; the recovery number is inflated by only rewording failures). No matched-token gating test. Open.
- Gap 6 (harm from reframing): no measured rate for benign reframing. Nearest are adversarial: verse lifted attack success 8.08% to 43.07% (d15); tool-framing cut refusals 10.9 to 40.2 points (d16, abstract only). Open.
- Gap 7 (age pattern): re-read the tables (d04): adolescents 26 effects vs 47 children vs 123 adults; age is confounded with domain; effects are nested; the regression residual Q looks inconsistent with the stated I2. Treated as unexplained noise (K36). Open, low value.
- Gap 8 (templates vs plain restate): no new test found (d19). Open.

Corrections noted while working
- The 1976 study is dated 1964 in Moore's text and the 1971 paper is cited as the formal report; secondary sources mix these.
- d10 and d05 tables came out garbled from PDF text; row labels were inferred and said so in limits.
- d16 and d18 are search-snippet level (opened false).
