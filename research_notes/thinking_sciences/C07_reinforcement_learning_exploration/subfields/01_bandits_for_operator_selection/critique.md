# Critique: Bandits and Thompson sampling for operator selection (C07.01)

Cross-check done 2026-10-26. Sources re-opened as PDF text: OPTS (2503.01163), TRIPLE (2402.09723), DYTS (2004.10874), Kaufmann et al. (1205.4217), AB-MCTS (2503.04412), PAK-UCB (2410.13287), Auer et al. 2002, Chapelle and Li 2011, da Costa et al. 2008, Simonides thesis 2026.

## Numbers re-checked and confirmed
1. Chapelle and Li delay table (a10): UCB 24,145 to 226,220; ratios 2.65 to 3.82. Confirmed.
2. OPTS averages (a29, b14): 39.52 manual, 20.73 APET, 48.43 EvoPrompt(DE), 52.87 OPTS(APET), 53.87 OPTS(US), 55.67 OPTS(TS). Confirmed. Task 8 on GPT-4o mini 2.67 to 52.33 and "ruin names" 27.17 to 67.67 confirmed.
3. TRIPLE (c04, b17): SH/CR +15/+12 (GPT-3.5), +15/+16 (Llama2) over Uniform; +5/+3 and +6/+7 over UCB; 9.7/13.5/17.4 at 10 evals per prompt. Confirmed in the paper text.
4. LLaMEA thesis (c10): Random 0.8304 (SD 0.0148), UCB 0.8453 (0.0296), SW-UCB-L 0.8235, Geometric-S 0.8470, SW-UCB-S 0.8417. Confirmed; N=6 per row.
5. Da Costa (a23, a24): T=200 uniform scenario 7.36/9.19/9.46/8.18/9.75/9.79 and Boolean 7.90/8.13/8.19/7.50/7.57/7.71 confirmed.
6. AB-MCTS Table 1 (c07): repeated sampling 15.0 and 18.6 on ARC-AGI vs AB-MCTS-M 12.3 and 16.0; CodeContest GPT-4o 40.6 vs 37.9; mean rank 3.5 / 2.3 / 2.7. Confirmed.
7. Auer UCB1 Theorem 1 (a02): bound 8 sum ln n / Delta_i + (1 + pi^2/3) sum Delta_j. Confirmed (the evidence line's wording is right).
8. Kaufmann et al. Theorem 1 (a07): form with ln T + ln ln T confirmed.
9. DYTS 16/19 IGD and 18/19 HV (a27): the paper says this. Confirmed as a claim, but see contradictions.
10. PAK-UCB Sudoku/HumanEval figures (c22): numbers exist in the text.

## Corrections
- OPTS text says TS beats US by "about 1.7%" and APET by "2.7%"; the Table 2 averages give 1.80 and 2.80 points. Use the table. The units are accuracy points, not relative percent (48.43 to 52.87 is +4.4 points, 48.43 to 55.67 is +7.2).
- New fact missing from the evidence: with the GA-based EvoPrompt (OPTS paper Table 10) the averages are 48.40 plain, 51.34 APET, 52.89 uniform, 53.48 TS. TS over uniform is only +0.59 there. This makes the "bandit beats uniform" effect weaker than a29 and b14 suggest.
- PAK-UCB (c22): the Sudoku (70.82 vs 50.42, 86.85 vs 93.6) and HumanEval figures are success rates of the two base models, not of the router. They show the models are complementary; they do not show the bandit's gain. Read c22's claim that the learner "can beat the single best" as the authors' aim, with the router's own numbers only in figures.
- a30 states "pool of 10, budget 50". The TRIPLE text I opened gives pool 30 with budget 150, and pool 150 with budget 100. I could not find the pool-10 setup. Treat a30's pool-10 line as unconfirmed.
- a02/a05 note about garbled formulas: a02 is fine; a05 (UCB1-Normal) not rechecked.
- Evidence lines a09/b06/b07, a06/b05, a07/b03/b04, a28/a29/b14/b15/b16/c01/c02/c03 are the same papers read repeatedly. Counted as one source each in the claims.

## Contradictions between sources
- DYTS (a27, b12): text says DYTS is best on UF8 for IGD, but the printed IGD table marks MOEA/D-GRA and IRA better on UF8 (and the text admits UF9). So "16 of 19" is not consistent with the table.
- ShinkaEvolve (b20, c09): caption says the bandit "slightly improves" over uniform, takeaway says "significantly outperforms". No numbers.
- Pryzant et al. (c06) put UCB at or above successive rejects and halving; TRIPLE (c04) puts BAI rules above UCB. Theory favours BAI for fixed budgets.
- Kuleshov and Precup (b08) found tuned epsilon-greedy and Boltzmann beating UCB; Chapelle and Li and Kaufmann et al. find TS best. Kuleshov did not include TS and tuned per setting.
- TIDE (c12): removing UCB is best of three ablations at size 50 and worst at size 200, so the bandit's value depends on problem size.
- Meta-Reasoner (b21, c15): text and table disagree on the ToT figures.

## Weak spots
- Almost all strong theory is for horizons of 10^4 to 10^7 pulls. Our agent has a few dozen. Only da Costa (50 and 200 pulls), TRIPLE (5 to 30 evaluations per prompt) and the LLM studies (50 iterations or 400 evaluations) speak to small budgets, and none has a Thompson-sampling arm at a horizon under 50.
- No LLM paper tested bandit vs uniform vs fixed at equal tokens with 10 or more seeds. The best-supported LLM result is that the gain over uniform is 0 to 2 points.
- Reward design (binary improvement vs relative gain vs extreme value) is untested head to head with TS; only Fialho-group papers (not opened) argue for extreme-value credit.
- The Sun and Li, Simonides, TIDE, Deliberate Evolution, CoEvo-AHD and AdaEvolve papers are preprints or a master's thesis.

## Only seen in snippets or summaries (not opened as full text)
a01 and b27 (Lai and Robbins, via restatements), b24, b25, b26, c26, c27, c28. Also b17-b19, b20, b21, b22 were read through fetch summaries; the Meta-Reasoner, AdaEvolve, ShinkaEvolve, Prompt Duel, Deliberate Evolution, TIDE, CoEvo-AHD, EVOLvE, Krishnamurthy, TextBandit, Semantic Bandits, Berdica and TI-UCB numbers were not re-checked in this pass.

## GAPS
1. At a horizon of 20 to 60 pulls and 6 to 10 arms, how does Thompson sampling with a weak prior compare to UCB1, uniform, and a fixed best-guess operator? (No source reports it; run it on our own logs.)
2. What reward should credit an operator: binary improvement, relative gain, extreme-value (max recent gain), or a delayed 2-3 step lineage score? Need a head-to-head with TS.
3. Does a stall-triggered forced switch of operator add more than any bandit rule, at equal tokens? (AdaEvolve and Deliberate Evolution hint yes, with 3 seeds or one seed.)
4. Do operator values depend on state (S0-S9 or parent quality) enough that a state-keyed bandit beats a global bandit on small budgets? (LLaMEA says value falls with parent fitness.)
5. How much prior information should operators start with (informative Beta priors from past tasks) and does a wrong prior hurt at 30 pulls? (Russo et al. only simulate 1000 periods.)
6. Does the TS-over-uniform gap in OPTS (+1.8 DE, +0.59 GA) survive 10 or more seeds and a significance test, and is it present at equal API calls?
7. For choosing among final candidate answers or prompts, is successive halving better than bandit sampling at about 5 evaluations each on reasoning tasks like ARC and BrainTeaser?
8. Is a window or discount needed at all for few-dozen-pull runs, or does plain TS with capped counts (C near 20 to 50) do as well? (DYTS used C=100 at thousands of evaluations.)
9. Can the LLM's own stated preference be used as a prior for the bandit (not as the chooser) and does that beat both? (OPTS and Meta-Reasoner show LLM-as-chooser is weaker, but not LLM-as-prior.)

## Gap search results (2026-10-26)

Search tools: WebSearch quota was used up and arXiv, OpenAlex and Semantic Scholar APIs returned 429, so sources were found by known arXiv ids, HAL and Crossref. 19 evidence lines are in `evidence_d.jsonl` (d01 to d19); 13 are papers whose PDF text I read this pass, 4 are my own simulations (marked "local simulation") and 2 are my own re-analyses of OPTS tables. Claims K22 to K29 were added; K17 was changed to contested; K05, K10, K12, K15, K18, K21 got extra evidence. All PDFs under `D:/research_scratch/C07.01/` were deleted.

| Gap | Result | Status |
|---|---|---|
| 1. TS vs UCB1 vs uniform vs fixed guess at 20 to 60 pulls | Simulation only (d15). Flat-prior TS beats uniform by 6 to 33 percent in regret; tuned epsilon-greedy and UCB c=0.5 often beat flat TS; a fixed guess right 30 percent of the time beats all flat-prior learners at 8 arms. No real-log result. | Partly closed (simulation); real logs still needed |
| 2. Reward design | Extreme (max of last 10) beats average in the Fialho group's SAT and artificial tests, but is risk-taking with bandits and helps mostly at long epochs; rank credit (AUC, sum of ranks) is robust to scale (d04 to d06). Relative-gain, state-keyed weights worked in Deliberate Evolution (d10). No head-to-head with Thompson or delayed lineage credit. | Still open for Thompson; direction known |
| 3. Stall-triggered switch vs bandit | Mixed. AdaEvolve (3 runs) says stall-triggered meta-guidance outweighs the bandit (d09). Deliberate Evolution says the state-keyed policy (uniform costs 23x) outweighs the stagnation monitor (1.8x) (d10). Neither isolates a plain forced switch at equal tokens. | Open, now contested |
| 4. State-keyed vs global bandit | No head-to-head. Only a hand-built 4-state table (d10). Contextual TS guarantees vacuous below T = d^3 (d13, my arithmetic). | Open |
| 5. Prior strength and wrong prior | Theory: loss bounded by 2 H^2 TV B (d03); meta-prior errors at horizon 200 not catastrophic (d02). Simulation at T=30: wrong prior up to strength 8 costs 0.2 to 0.5 successes, right prior saves 0.9 to 2.4 (d16). | Mostly closed for guidance (cap near 4 to 8); real prior errors not tested |
| 6. OPTS gap significance | Task-level paired test: DE +1.79, t=2.61, sign 18-7, Wilcoxon p=0.008; GA +0.60, t=0.96, 12 wins vs 14 losses (d07, d08). Equal API calls and seed-level tests not possible from tables. | Partly closed: real for DE, not for GA |
| 7. Halving vs bandit for final choice | Simulation: ties within 0.03 to 0.04 in P(best), beats plain UCB1 only with many candidates (d18). Jamieson and Talwalkar concerns converging curves (d14). No ARC or BrainTeaser run. | Open for real tasks; simulation says no clear winner |
| 8. Window or cap needed? | Literature starts at 200 pulls (d11, d12). Simulation: caps 5 to 50 change nothing at 30 to 60 pulls (d17). | Closed in simulation: use plain TS |
| 9. LLM as prior | One related study (d01): LLM-generated pre-training data cut regret 14 to 20 percent at T=1000 (contextual bandit). No comparison to LLM-as-chooser or at small horizons. | Open, with a hopeful sign |

### New caveats from this pass
- Simulation results (d15 to d18) are my own and depend on the arm distributions I chose; standard errors were not computed. They set hypotheses, not facts.
- The OPTS task-level tests treat 27 tasks as independent samples of seed-averaged scores; they cannot say anything about seed noise.
- Deliberate Evolution's ablation table does not state its number of runs; a separate 3-run check gives NMSE variance 9e-10 at mean 4e-4, which makes the 1.8x stagnation effect larger than run noise if the ablation used a single run.
- Fialho-group results come from one group and were tuned by racing on the evaluation instances.
- Not found: any Thompson-vs-extreme-credit comparison, any state-keyed bandit vs global bandit, any LLM-as-prior vs LLM-as-chooser test, any bandit study at 20 to 60 pulls with real operator logs.
