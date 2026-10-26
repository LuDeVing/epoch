# Critique: D01.02 Proofs and refutations (cross-check)

Method: I re-opened the arXiv PDFs (pdftotext, saved on D:/research_scratch/D01.02, PDFs deleted afterwards) behind 12 numbers. I did not re-open Pease's thesis (Edinburgh repository), so all HRL / Theorem Modifier numbers are as the three searchers recorded them and are checked only against each other.

## Re-verified against the paper text
- Huang et al. 2024 (2310.01798): GPT-3.5 GSM8K 75.9 / 75.1 / 74.7; CommonSenseQA 75.8 / 38.1 / 41.8; GPT-4 GSM8K 95.5 / 91.5 / 89.0; oracle 84.3, 89.7, 29.0. Confirmed. 74.7% keep-rate sentence confirmed.
- Tyen et al. 2024 (2311.08516): GPT-4 52.87 overall; 255 wrong of 300; 11.11 / 23.53 on tracking shuffled objects and word sorting rows. Confirmed. Note: the +23.53 / -11.11 pair sits in the tracking-shuffled-objects row of the table; b09 attributed it to word sorting (the 11.11 sentence in the text is about word sorting). Treat the pair as "one task", not a cross-task figure.
- Olausson et al. 2024 (2306.09896): heatmap cells 1.05 (10 initial, 1 repair) and 0.97 (2 initial, 10 repairs) exist. Which of the several heatmaps (GPT-3.5 vs GPT-4, APPS split) each cell belongs to is not certain from the garbled layout; the "GPT-4 on APPS" label stays unconfirmed. Human feedback 52.60 vs GPT-4 33.30 confirmed (Table).
- Qiu et al. 2024 (2310.08559): ACRE 64.0 / 65.0 / 70.0 / 78.2 / 82.5 and task accuracy 28.0 -> 59.0 confirmed. List Functions 65.1 -> 62.4 and MiniARC 33.1 -> 18.7 confirmed. MiniSCAN task accuracy 0.0 -> 70.0 appears in the table at T=3,N=5; c22 said 46.0 (T=3,N=1) and b19 said "above 80 percent" for the symbolic case. The 70.0 is the best-supported figure; the 46.0 and 80 are not confirmed.
- Wang et al. 2024 (2309.05660): 17 / 23 / 30 / 33 / 45 confirmed. CORRECTION: c23 says "human-written hypotheses 23 percent without summary"; the paper has human-written at 45 and program-only at 23. c23's phrase is wrong.
- Kumar et al. 2024 SCoRe (2409.12917): 52.6 -> 41.4 (-11.2); SCoRe 60.0 -> 64.4 (+4.4); +15.6 and +9.1 abstract. Confirmed.
- Sinha et al. 2025 REFUTE (2502.19414): 324 samples, 304 authors; RandSearch 4.0 / 3.7 / 4.0 / 8.3; oracle 15.1 and 9.9; 35% incorrect-counterexample endings. Confirmed. CORRECTION to a22: the 35% is "of all samples" (on average), not "of failed runs". Also a22 says "o3-mini (high) with code-execution feedback" is best; the paper's best RandSearch is 8.3 and the 44-48.7 are solve rates of other rows. Keep the 8.3 / 48.7 contrast as stated in K14 with that caveat.
- Li et al. 2025 COUNTERMATH (2502.10454): 1,216 pairs, 1,025 SFT samples, 95.4 annotation agreement, 41.8, 59.0, 60.1, 80.7 (R1 by row order in the garbled table; the text says 80.7 for the strongest model), 38.3 -> 41.1 F1, examples 74.2 -> 79.4, strict 30.2 -> 31.1. Confirmed. The judge-accuracy 97% in a20 refers to the training-data step (rationale extraction check), not to the benchmark.
- Zouak et al. 2026 (arXiv 2610.02444): 4,707 / 6,748 / 97.7%; Pass@1 0.30 / 0.35 / 0.50 / 0.50 (dense, sparse); Pass@8 0.49 / 0.64 / 0.68 / 0.67; paired delta +0.199 [0.13, 0.27]; truth probe 0.27 -> 0.00 with SFT; probe 0.36 / 0.21 / 0.73 / 0.84. Confirmed. NUANCE: a24 says dense vs sparse gap 33 +/- 8 points; c14 says dense and sparse are equal. Both are right: equal on the counterexample benchmark, different on the truth probe under the training-style prompt (dense 0.34 vs sparse 0.65 as the paper states). Also a23 says "SFT delta CI not significant": the paper gives 0.30 -> 0.35; no contradiction.
- Chuharski et al. (arXiv 2412.16177): 757 / 420 / 109 (25.95%) / 40 (9.52%) / 271 (64.52%) and 26.60 / 4.64 / 4.49 / 81.86 / 49.44 / 37.76 confirmed. CORRECTION: model names. The paper uses gpt-4o-2024-05-13 (ChatGPT), Claude Sonnet, Gemini 1.5; a27 said "GPT-4" and c12 said "Claude 3.5 Sonnet and Gemini 1.5 Flash". The paper text says "Claude Sonnet, Gemini 1.5, GPT-4 APIs" in one place and gpt-4o in another, so the paper itself is inconsistent. The 26.60% etc. are per-model shares of unique conjectures with no counterexample found (25 of 94, 11 of 237, 4 of 89).
- Shinn et al. 2023 Reflexion (2303.11366): HumanEval 91.0 vs 80.1 confirmed; false-positive 16.3% vs 1.4% confirmed. CORRECTION to b11: MBPP Python is 77.1 vs 80.1 (not 77.0 vs 80.0); the table is garbled, so the other rows (Rust 68 vs 60, 75.4 vs 70.9, Leetcode Hard 15.0 vs 7.5) match only by reading order.

## Contradictions between evidence lines
1. Monster-barring threshold: a09 says a minimum near 10%; b03 says low threshold up to 30-40%; c03 says best minimum 30-40%. I cannot resolve this without the thesis. Do not use any threshold number.
2. HRL session settings: a07 says 20 theory-formation steps per phase; c01 says 10; b05/c06 give HR 300 steps for Theorem Modifier, a12 gives 3000. Unresolved.
3. Number theory monster-barring "97%" is a degenerate score (b03, c03): the system flagged almost nothing. a09 reports it as a plain result. Treat as not meaningful.
4. Werndl is dated 2009 in a19 and 2013 in c09. The Philosophia Mathematica paper is 2009 (from memory, not re-opened). Same finding.
5. a28 and c11 (lecture notes) describe the loop without any measurement; they are the same source type and count as zero independent evidence.

## Weak spots
- Almost all of the Lakatos-specific evidence is one source: Pease's thesis, scored by the program's own interestingness measure, no baseline, three toy domains, few modifications per session. That is why most claims are single-source.
- The LLM evidence supports the pieces (executable feedback, location, calibration) but not the Lakatos typing itself. No test of global/local typing, lemma-incorporation or monster-barring with an LLM.
- Many LLM papers use different models, so cross-paper rankings (b23) are suggestive only.
- 2026 arXiv items (Zouak, Li 2026, Ke, Zheng, QED, CIll) are recent, unreviewed, mostly single groups. b22 is a paper rejected from ICLR 2026. Weight them low.
- Items mentioned only through snippets or abstract page: a29 (Pease et al. 2017 dialogue-game paper, abstract only, opened false) and c29 (STP v2 abstract, opened false). Not used in claims.
- Not re-opened this session: Pease thesis, Martin and Pease 2013, Werndl, Davis 2021 review, Colton and Pease 2004, LeanConjecturer, Lyra, AutoGraphForge, CIll, Huang 2025 hypothesis validation, QED, Self-Debug, CRITIC, Self-Refine. Their numbers are as recorded.

## GAPS
1. Does typing a counterexample as global/local/both and choosing repair by type beat an untyped "reflect and fix" loop, and a best-of-N control, at equal tokens, for an LLM on seeded flawed proofs? (No study; the main test.)
2. What triggers the switch from repair to surrender for an LLM? Pease found surrender (limit 0) best on average; is there a cheap signal (plausibility, claim scope left, number of exceptions) that predicts when repair is worth the tokens?
3. How far can a claim be narrowed before the repair is empty? Is there a measurable scope-shrinkage threshold (the thesis's "problem of content") and does a guard on it improve outcomes?
4. Can an LLM be made to locate the failing lemma (local counterexample) without an executor, e.g. by independent re-derivation of each step, and what is the cost against executing?
5. How often do LLM repair loops silently change the claim (monster-barring in disguise), measured on a seeded set, and does a statement-fidelity check remove the drift without lowering repair success?
6. Hidden-lemma discovery: do Pease's two surprise tests (use of construction ancestry) have an LLM equivalent, and does it find the hidden assumption better than asking "what did the proof assume?"
7. What do the 2017 Lakatos dialogue-game and argumentation-semantics results (Pease, Budzynska et al.) say about multi-agent challenge and response, and were they ever evaluated? (Only abstract seen.)
8. What are the thesis's true monster-barring thresholds and HR step counts (contradictions 1 and 2), and do the Theorem Modifier results replicate with a modern prover and an LLM proposing the restriction?
9. Does a persistent counterexample store (Davis knots, AutoGraphForge) reduce wasted refutation rounds for an LLM compared with rederiving counterexamples each round?
10. Which of the 2026 counterexample benchmarks (REFUTE, COUNTERMATH, SymCE) can be used as a cheap equal-token test bed for our refute operator, and what is the false-refutation rate of a prompt-only agent on their true items?

## Gap search results

Sources opened in this pass: the Pease thesis (PDF from the Edinburgh archive, text read in chapters 9, 10, 12, 13) and arXiv PDFs or HTML for ProcessBench, FaithSieve, Repair-Retry, Pythagoras-Prover, the Isabelle contract paper, the round-trip autoformalisation paper, the Self-Correction Illusion, AutoGraphForge, and REFUTE and COUNTERMATH again. The web search quota ran out and the arXiv, Semantic Scholar and OpenAlex APIs were rate limited, so no new forward-citation sweep was possible. Evidence is in evidence_d.jsonl (d01-d17); new claims are K24-K34.

Closed or mostly closed
- Gap 8 (thresholds and step counts): closed for the thesis. The barring minimum differs by experiment (30-40% single agent, 0-10% multi-agent, 40-50% average in mixed runs, 15% coded default). HR steps: 10 or 20 per phase depending on the experiment (the surrender study used 20 steps x 10 phases); Theorem Modifier used 3000 steps with Otter and MACE at 10 s. 300 is not in the thesis. Still open: a modern prover with an LLM proposing the restriction (no study found).
- Gap 10 (test bed): answered by design. REFUTE has only incorrect solutions, so it cannot measure false refutation. COUNTERMATH can, through its True-labelled items and macro F1, but the paper reports no direct rate. A prompt-only false-refutation number still has to be measured by us.
- Gap 4 (locate without an executor): answered by FaithSieve at equal tokens. Reading-only methods gain 0.5 to 4.5 points over a plain judgement; a formal pipeline gains about 10 points at 152 times the tokens. ProcessBench shows reasoning models locate far better than chat models.

Partly answered
- Gap 2 (surrender trigger): Pease found relative interestingness, plausibility 0.7 and zero modifications the best signals, but scored by the agents' own interestingness (circular), and scope left was not useful. On the LLM side, repair is worse than restart at equal tokens in Lean (d06, d08) and helps where the error is local and mechanical (d07). No study tests a stop rule.
- Gap 5 (silent claim drift): drift is real (16 of 100 declarations; 15-45% meaning drift), and a protected-statement diff check worked in a case study. No seeded-set rate and no test that the check preserves repair success.
- Gap 6 (hidden-lemma surprise tests): the definitions are now exact (d04). One worked example, no LLM equivalent, no comparison with the plain question.
- Gap 9 (counterexample store): AutoGraphForge gives the dynamics (big first round, fixed point, shared store matters) but no store-versus-rederive arm and no LLM.
- Gap 3 (scope shrinkage): the thesis names the problem of content as future work, and the domain-of-application signal was not useful. No measured threshold or guard.

Still open
- Gap 1 (typed repair vs untyped reflect vs best-of-N): no study found. d06 and d08 raise the bar: the control must include restart, with input tokens counted.
- Gap 7 (2017 dialogue game): the publisher PDF was blocked (bot check, 403). The record shows a worked example and no quantitative evaluation. The body was not read.

New cautions from this pass
- The restart finding comes from Lean provers with a clean verifier. Informal conjecture repair may differ. The 2026 preprints (Repair-Retry, FaithSieve, Self-Correction Illusion, the Isabelle audit) are single groups with small samples (11 sequential problems; 30 tasks per cell). Treat the numbers as direction, not size.
- The conditional fix rates quoted in d07 were computed by the reader from cumulative counts in the paper, not reported by the authors.
- K10 (repair about break-even with fresh sampling) rests on APPS code repair. The Lean result is clearly worse for repair, so break-even is not general.
