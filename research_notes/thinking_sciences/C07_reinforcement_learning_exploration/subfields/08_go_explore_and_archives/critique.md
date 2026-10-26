# Critique: Go-Explore and archives (C07.08)

Cross-checker pass. Sources re-opened this session (full PDF text): Go-Explore arXiv 1901.10995, the Nature version 2004.12919, Intelligent Go-Explore 2405.15143, Darwin Godel Machine 2505.22954, Time-Myopic Go-Explore 2301.05635, Bhatt et al. 2601.00042.

## Numbers re-checked (13 confirmed, 3 corrected or sharpened)

Confirmed against the PDF text:
1. Go-Explore Phase 1, no domain knowledge: 57% of 100 runs, mean 57,439 (CI 47,843-67,224), level 1 after mean 640M frames, 10.8 h.
2. Phase 1 with domain knowledge: mean 148,220 (CI 144,580-151,730), 50 runs; level 1 after 57.6M frames (0.9 h). Ratio 640/57.6 = about 11x.
3. Robustified: Montezuma 666,474 mean (arXiv), Pitfall 59,494 mean, max 107,363; 43,763 is the no-knowledge robustified mean.
4. Nature version: Montezuma 1,731,645, Pitfall 102,571, 83.6% of 55 games, beats Agent57 on 7 of 11 games, Freeway tie, policy-based 97,728 and 20,093, robot 99%, control ran 50 times more frames.
5. 51 of 57 best trajectories used the treasure-room bug; single-demonstration robustification 40%; prior best intrinsic score about 17,500 and 10% level-1.
6. IGE Game of 24: 100%, 70.8% faster than DFS, chi-square p<0.05 at 150 operations. Table 3 values (GPT-4 70/82/83/100; Llama 44/68/54/98; Sonnet 24/58/80/86) exact.
7. IGE Table 4 archive sizes: 18.5/203.5/22.4 without filter, 15.6/25.5/4.4 with. The column mapping that evidence a28 marked as inferred is now confirmed.
8. DGM: 50.0/38.0, ablations 23.0/14.0, 39.0/28.0, greedy 39.7/30.0; 51.3% vs 32.5% kept-edit-ability; 28.9% and 24.5% transfer; 20.0 to 50.0 SWE-bench; Polyglot 14.0 to 38.0 on the subset and 14.2 to 30.7 full.
9. Time-myopic Table 2 and Table 3 (Montezuma 695/2090 vs native 2303; Gravitar 2533/3161 vs 2130; Frostbite 3543/4476 vs 11,721; archive 2838.9 vs 566.0/248.3; Gravitar 7376 vs 381).
10. Bhatt et al.: 0 to 16 findings across 5 seeds, 1.8+/-1.3 vs 4.6+/-6.0, seed 42 gave 16, -94% with 161 findings, 96% collapse to one cell, 1054 attacks at N=100, N=20 saturation.

Corrections and sharpening:
- IGE Table 2 BabyAI column (evidence a26 and c04 left it incomplete; a layout-mode text extraction scrambles it). Raw-mode text gives: IGE 84; without action selection 24; without state selection 48; without archive filtering 64; without all three 4; without action history 72; classic Go-Explore 4. TextWorld Cooking: 92, 0, 76, 64, 0, 72, 0. Game of 24: 100, 68, 96, 93, 61, 33, 38. Claim K08 uses these.
- The "over 5 times larger" archive claim holds only for BabyAI (8.0x) and Cooking (5.1x). On Game of 24 the ratio is 1.2x. Evidence b13 and c03 say "5x to 8x" without this limit.
- Coin Collector "about 88%" is read from a figure, not a table; treat as approximate. The text says only that IGE was the only method to find the solution.
- The Nature paper's Montezuma 1,731,645 and the arXiv 666,474 are different versions with different settings; never mix them in one comparison.

## Contradictions and tensions between sources
- Learned keys (Latent Go-Explore, Time-myopic) are described by their authors as matching or beating native Go-Explore. The tables show native winning on Montezuma at 1M frames (2303 vs 695) and Frostbite (11,721 vs 3,543), and LGE finding about 5k cells vs the larger domain-knowledge count. K17 is marked contested.
- Reflexion: IGE says it hurts on long games; on Game of 24 it is the second best (83, and 80 for Sonnet). Both are in one paper, so the claim "Reflexion fails on long horizons" is one source's reading with a context-length hypothesis that was not tested.
- IGE says it beats Tree of Thoughts (74%); that number is from a different setting and is not comparable (b11 already flags this).
- Go-Explore papers say the simulator restore is not essential (policy-based version works), but the policy version scores 5x lower on Pitfall. Both statements are true; they answer different questions.

## Weak spots
- Almost every strong LLM number comes from one group (Clune lab: IGE, DGM) and the same Game of 24 task. Independent replication is only GLoW (different benchmark, baselines at different budgets) and the red-team paper (different goal).
- IGE compares at equal environment steps or operations, not equal tokens. IGE makes extra model calls per step (choose state, choose action, judge novelty), so the equal-token claim, which our guardrail G7 requires, is untested. Cost is given per task (about 1.04 USD Game of 24, 2.01 USD BabyAI) but no baseline cost is read.
- DGM: one run per arm, about 22,000 USD and two weeks for a SWE-bench run, so no variance estimate. The baselines cost far less. The "objective hacking" appendix means part of the score may be gamed.
- Bhatt et al.: 28 runs over 6 questions, mostly seed 42, GPT-4o-mini only; the authors themselves flag that the seed-stabilisation result rests on one seed ordering.
- Ecoffet et al. mark their selection-weight heuristic result as "data not shown"; the weights were never isolated in an ablation. No direct MAP-Elites comparison.
- Derailment has one direct test (robot, 18 of 20). In Atari it is argued, not measured.
- Go-Explore results are on deterministic or restorable simulators; the text-game versions restore by replaying a stored command list, which is cheap and exact, unlike restoring a model's reasoning state.

## Only seen in snippets or not opened
- Evidence b28 (DGM safety note) was not opened: table-of-contents line only. Not used in claims.
- c25 (Arumugam and Griffiths 2025), c26 (AlphaEvolve, FunSearch, OpenEvolve secondary descriptions) were search summaries only; c27 is an absence check made with two web searches.
- c22 (Go-Browse), c23 (semi-parametric RL), c24 (maze exploration), c20-c21 (Rainbow Teaming), c18-c19 (GLoW) were read by the evidence agent but not re-opened by this checker; their numbers are taken on trust.

## GAPS (most decision-relevant first)
1. Does an IGE-style archive of partial solutions beat best-of-N and ReAct at EQUAL TOTAL TOKENS (including the extra state-selection and novelty-judging calls)? No source reports this.
2. Does an archive loop help on pure reasoning or code-step tasks with a checker (ARC-style, math proofs, program synthesis), beyond Game of 24? No measured result was found.
3. What state key works for a reasoning agent: raw text, normalised answer, plan skeleton, execution trace? Which key avoids the collapse seen in Bhatt (96% to one cell) and the bloat seen in native Go-Explore?
4. How should the resume point be chosen when the model is the selector: by model judgement, by score and few-children weight (DGM), by visit count? Is model selection biased toward familiar states, and does G8 (do not let the generating model be the final selector) apply to archive choice?
5. How large should the archive be, and who deletes entries? Does filtering by code (dedupe, dominance) match the model-based filtering that IGE credits for its BabyAI and TextWorld gains?
6. How much free exploration after resuming helps a language agent (the 20-step and 0.8-proportion settings in Yang et al. were for RL), and does a short burst beat resampling from scratch at equal tokens?
7. Does the archive gain shrink as the base model gets stronger (24 to 86 for Sonnet 3.5 vs 70 to 100 for GPT-4 on Game of 24)? Measure with current models; the evidence is from 2024 models.
8. Is resuming from a lower-scoring entry useful (DGM dips at iterations 4 and 56), or only an anecdote? Needs a controlled count over many runs.
9. How many parallel independent runs before diversity saturates for reasoning tasks (N=20 in the red-team setting)? Connects to quality-diversity (C07 sibling) and anytime search.
10. What fraction of archived "solutions" fail when re-run on a held-out or mutated input (the LLM analogue of robustification, 40% single-demo success in Go-Explore)? This ties archive entries to guardrail G3.

## Gap search results (2026-10-26)

Search tools: WebSearch quota ran out after one query. Semantic Scholar, OpenAlex and arXiv search returned 429. Papers were found through the Semantic Scholar citation list of IGE (one call) and known arXiv ids, then opened as full PDF text (pdftotext) under D:/research_scratch/C07.08 (PDFs deleted). 18 new evidence lines in `evidence_d.jsonl` (d01 to d18), all opened. Claims K23 to K36 added; K07, K09, K10, K12, K13, K16 and K21 got updated text or evidence. Table numbers that came out misaligned in layout mode were re-read in raw mode (SOAR Table 1, Mind Evolution Table 2).

### Closed or mostly closed
- **Gap 4 (resume rule, G8): mostly closed.** DGM, ShinkaEvolve and HGM all pick the resume point by a code rule, and all three beat best-score-only (K26). A model judge was not compared with a code rule anywhere, but GLoW shows a model with global context beats a model on single states (d05). G8 holds by construction when the selector is code. Final answer picks: a vote or reward model stalls while coverage rises (41.4% vs 98.4% on MATH), and a separate discriminator beat the search's own value (84% vs 73%) (K33).
- **Gap 9 (how many parallel runs): closed for checkable tasks.** The N=20 plateau is a count of attack types. Solved-problem coverage keeps rising log-linearly (K32). Plateaus appear at about 500 calls (ARC, repeated sampling) to 5.2k attempts (SOAR 7B).
- **Gap 6 (burst length): partly closed.** GLoW: 3 bursts of 50 steps per selection was best, 1 and 5 worse (K29). Still missing: a short burst vs restart-from-root at equal tokens.
- **Gap 5 (archive size, who deletes): partly closed.** Embedding dedupe at 0.95 gave most of the gain; the model judge added little (K27). Archive sizes 10 to 50 in Shinka. Single task, figure only, so no effect size.

### Partly answered
- **Gap 1 (equal total tokens): one result, negative.** Graviet and Shah: retry 17/25 vs snapshot archive 6/25 at 1M tokens per seed (K23). The selector was a heuristic, not IGE's model, and the baseline was retry only. So IGE-style selection vs best-of-N and ReAct at equal tokens is still unmeasured. Near-equal cost on Jericho (GLoW paper): IGE wins on 2 of the 7 games I listed by large margins and ties or loses on others (K07 caveat).
- **Gap 2 (reasoning and code with a checker): partly answered, not for Go-Explore itself.** AB-MCTS (ARC at 128 calls: sampling best), SOAR (6k candidates: refine beats sampling), Mind Evolution (planning: beats best-of-N, cost reported). Pattern: wide first, deep later (K24, K25). No proof-step or math-step archive with a model selector was found (K21 updated).
- **Gap 3 (state key): still open as a head-to-head.** Neighbouring keys that work: URL, output grid, diff vs full snapshot by where the progress lives (K31). Nobody compared text, normalised answer, plan skeleton and execution trace.
- **Gap 7 (stronger model): not measured at the current frontier.** Mixed neighbours: SOAR gain does not shrink 7B to 123B; SWE-Search relative gain smallest for GPT-4o; Haiku 4.5 test negative. K10 text updated, still single-source.
- **Gap 8 (resume from a lower scorer): mechanism supported, count missing.** HGM shows own score predicts descendants weakly (r 0.28 to 0.44) (K13 updated). No count of how often low-score resumes reach the final answer.
- **Gap 10 (failure share on mutated input): open.** SOAR notes hard-coded, brittle programs and filters them; no rate reported anywhere (K34).

### New cautions from this pass
- Archive loops cost tokens to build and to resume. Graviet shows budget fragmentation and wrong-state attractors (K30). Our design must count root cost and keep a challenge step.
- Feeding the whole archive to the generator hurt (K28).
- Almost all new numbers use calls or candidates as the budget, not tokens, and 2024 to early 2025 models. Only Graviet (Haiku 4.5, 2026) is recent.
- Not opened: no new paper that claims an IGE-style archive on math or proofs; search quota prevented a broader sweep, so that absence is again a limit of the tools.

### Updated priority for our own measurement
1. Archive arm vs repeated sampling vs best-of-N vs retry at equal total tokens on a checkable set (ARC-style plus a math or code set), with root cost counted. This is the only way to settle gap 1.
2. Same arm with two model strengths (gap 7).
3. Three state keys on that set (gap 3), with cell count and largest-cell share logged.
4. Log, for every resume, the source entry's score, children count and result, to get the lower-scorer count (gap 8) and the mutated-input failure share (gap 10) for free.
