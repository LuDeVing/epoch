# 11. Decision science: which ideas to test, and how much

Scope: bandits, Bayesian optimisation (BO), sequential testing, racing/Hyperband, value of information (VOI), R&D portfolio theory, surrogates, base rates. Researched 2026-10-13 for the HTSA nano loop (sketch, score, question, build, verify). Grades: **A** peer-reviewed, large real data; **B** peer-reviewed theory, simulation or single study; **C** preprint or self-reported; **D** my inference or arithmetic. [n] = Sources. The shared web-search quota ran out mid-session, so later checks were direct fetches; unverified items are listed at the end and excluded.

## Bottom line

1. Choosing ideas is a finite-armed, multi-fidelity, simple-regret problem (find the best idea, not maximise average reward). Successive halving, Pandora/Gittins ordering and top-two sampling fit it; UCB-style optimism does not [3][4][5]. GP-BO fits only an idea's continuous knobs [22].
2. Returns are fat-tailed (Bing: top 2% of ideas gave 74.8% of gains), so the best regime is lean: many ideas, few samples each, fast rejection [1][2].
3. Scoring ideas from text predicts execution poorly. Use surrogates as priors with uncertainty, never as gates [24][25][26].
4. Ladders help only if rung rank predicts final rank, and failures are documented: LR decay reorders optimizers [11], learning curves are often ill-behaved [10], Hyperband's edge over random search is small when early-vs-final Spearman is below 0.8 [9].
5. Peeking, winner's curse and baseline drift after promotion break fixed-threshold statistics [14][1][18].

## 1. Evidence

**Base rates**
- Web experiments (B): about 1/3 of Microsoft experiments are positive, 10-20% at Bing; winners move key metrics 0.1-1.0%. At alpha 0.05, power 0.8, a significant result is real 89% of the time with prior 1/3 but 3.1% with prior 1/500 [20]. My arithmetic (D): at alpha 0.01 the figures are 0.90, 0.62, 0.29 for priors 0.10, 0.02, 0.005.
- Bing tails (B): tail coefficient well below 3 makes the "lean" strategy optimal; testing 20% more ideas at fixed users gives +17.05% productivity; small-t ideas should be shrunk hard; Bing's offline triage showed no evidence of predicting online results [1].
- Drug funnel (A): 13.8% Phase I to approval, oncology 3.4%, 58-66% per phase [21].
- ML recipes: most Transformer modifications gave no meaningful gain in a shared setup (B) [13]. Even the best optimizers (Muon, Soap) shrink from about 1.4x to 1.1x speedup between 0.1B and 1.2B parameters against tuned baselines (B) [11]. In the 5-minute val_bpb autoresearch loop [23], a pure LLM loop plateaued at 0.956 after 875 experiments (start 1.0069); retained changes include n-gram memory -0.0275, QK-norm -0.0137, narrower model -0.0109, against a noise floor of 3-5e-4 (C) [22].

**Ladders and racing**
- Successive halving (SH): Karnin et al. for stochastic bandits, Jamieson and Talwalkar for hyperparameter tuning (B) [6]. Hyperband hedges the "n versus B/n" trade-off with several SH brackets (the last is plain random search), over 10x faster than BO baselines [7]; ASHA promotes asynchronously [8]; AlphaEvolve's "evaluation cascade" is the same device [31]. SH needs high cross-fidelity rank correlation: PriorBand's "high" cut-off is Spearman >= 0.8 at 10% of budget (B) [9]; about 15% of training-set-size learning curves are ill-behaved (C) [10]. DataDecide (B): ranking at one small scale picks the best data recipe about 80% of the time (150M to 1B, 25 corpora); no scaling-law method beat it [12].

**Sequential stopping**
- With abundant hypotheses the optimal policy is a two-threshold sequential test with very low power per hypothesis; quick rejection drives performance (B) [2]. Naive monitoring can raise Type I error fivefold at 10k samples (B) [14]; e-processes and confidence sequences stay valid under any stopping rule (B) [15]; e-BH controls false discovery rate under any dependence (B) [16].

**Value of information**
- Pandora index alpha solves EI(x; alpha) = cost; open in descending alpha, stop when the best found exceeds every remaining alpha. Bayesian-optimal for independent boxes, a heuristic for GPs; gains grow with dimension, none at d = 4, poor on Robot Pushing, lambda needs tuning (B) [3]. Lower cumulative regret forces higher simple regret [4]; top-two sampling is near-optimal for best-arm identification [5]. Full Bayesian experimental design is the general frame but computationally heavy [41].

**Portfolio and exploration**
- Scientists' actual strategy is over 3x costlier than the best alternative; the optimal one is about 10x better than random and turns riskier as a field matures (B, simulation) [36]. Tolerance of early failure raised high-impact output (B) [38]; novel papers show higher citation variance, delayed recognition and more top-1% hits long run (B) [37]; research productivity falls, over 18x researchers for Moore's law (A) [39]. RE-Bench: agents score 4x humans at 2 hours, humans win at 8-32 hours, which suggests agents' edge is breadth (my reading) [40]. LLM ideation is repetitive: 200 of 4,000 seed ideas were unique [25].

**Surrogates steering LLM generation (2024-26)**
- Large Discovery Model (LDM, Aug 2026): an LLM proposes, a GP (RBF over LLM-identified knobs of train.py) with EI/UCB selects; 2.4x larger val_bpb reduction than LLM-only reflection (0.0727 vs 0.0301); the "discover" step that adds dimensions matters (C: no seed count or significance tests, evaluation-count matching not stated) [22]. Text to outcome: fine-tuned LM 77% pairwise accuracy (63.6% on unpublished ideas), off-the-shelf o3 near chance (B) [26]; ideation vs execution scores correlate -0.15 to 0.21, AI "excitement" -0.39 (B) [24]; LLM rankers 53.3% vs reviewers 56.1% (B) [25]. Text regressors trained on Vizier logs beat traditional regression models (B) [27]; LLAMBO helps most when data are sparse (B) [28]; LLM-embedding regression rivals GP-BO on strings and hyperparameters (C) [29]; INSTINCT swaps the GP for a neural bandit on transformer features because GPs struggle in high dimension (B) [30]; dimension-scaled lengthscale priors rescue vanilla BO (B) [34]. The pairing of search policy and operator set matters on MLE-bench lite (medal rate 39.6% to 47.7%) (C) [33]; ShinkaEvolve adds novelty rejection and a bandit over LLMs (C) [32].

## 2. What did not work

- Fixed-gap rung gates under rank flips and ill-behaved curves [9][10][11]; small-scale or single-codebase wins that did not transfer [13][11].
- Text-level quality scoring [24][25][26]; Bing's offline triage [1].
- Optimising against a proxy: gold score falls past a point [35]. LDM itself shows a region where the surrogate was confident and wrong, and needs manual kernel/feature design [22].
- BO limits: Pandora index no better at low dimension, poor on Robot Pushing [3]; GP cost cubic in observations [22].
- Non-stationary bandits: with a fixed variation budget regret grows as T^(2/3) instead of log T, and is linear if variation scales with T [18]; abrupt-change lower bound, sliding-window/discounted UCB match it up to logs [19]. Promotion changes the baseline, so arm payoffs drift; the pure LLM loop saturates [22].
- Cumulative-regret optimisers are the wrong objective for best-idea search [4].

## 3. What would transfer to an LLM-driven idea loop

Context (project docs): rung 4 is about 5 minutes, an overnight run about 31, on one 6 GB laptop GPU, so verification seeds are the scarce resource.

**M1. Calibrated successive-halving ladder with a hedge lane.** Promote on P(final gap > margin | rung data) >= tau_k, from a regression fitted on logged (rung-3 gap, rung-4 gap, slope, step ratio) to overnight pairs, with noise from the baseline-seed pool, instead of "k x noise" gates. Keep about a third per rung. Send 10-15% of overnight slots through a skip-rung lane (random or near-miss), Hyperband's s = 0 bracket. Compare at matched LR-schedule phase (constant LR plus cooldown [17]) and pair candidate and baseline on identical init and data order (D). *Effect (D, my Gaussian simulation):* a top-third cut of 30 keeps the true best with p = 0.75 at rung-final correlation 0.5, 0.90 at 0.7, 0.96 at 0.8; a 30>12>5>2 ladder with 0.5/0.7/0.9 keeps it 64%. *Measure:* Spearman(rung 4, overnight) per batch, target >= 0.8 [9]; hedge-lane win rate; GPU-minutes per verified win.

**M2. Breadth set by the measured tail.** Estimate the tail index of standardised overnight gaps (Hill estimator, bootstrap CI). If the upper bound is below 3, move budget from interrogation depth to more distinct builds and report shrunk (empirical-Bayes) gaps, not raw winners. *Effect:* +17% productivity for +20% ideas at Bing [1]; ours unknown until estimated (D). *Measure:* tail CI; verified wins per GPU-hour at two breadth settings randomised by run; calibration slope of predicted vs realised overnight gap (below 1 means winner's curse).

**M3. Anytime-valid overnight verdicts.** Replace the 1-3-5-seed Welch p < 0.01 staging (data-dependent run counts, i.e. optional stopping) with a two-threshold sequential e-process on paired seed differences, variance taken from the pooled baseline runs, plus e-BH across the night's candidates [16]; reject at the lower boundary after 1-2 runs; allocate extra seeds by top-two sampling [5]. *Effect:* validity first (nominal 1% false-verified) at equal or fewer seeds (D). *Measure:* A/A audit, 50-100 unchanged-baseline "candidates" through the exact rule; false-verified rate and mean seeds, before and after.

**M4. Pandora ordering and stopping for builds and the overnight queue.** Replace "best five-minute gap first" by index alpha_i solving E[(g_i - alpha)+] = lambda * c_i, with g_i ~ N(mu_i, s_i) from M1 and c_i the measured run minutes (start logging mu, s, c); run in descending alpha_i; end the night when the best verified gain exceeds the largest remaining alpha. Lambda is the nats-per-GPU-minute exchange rate, tuned to the nightly budget [3]. *Effect:* cheap uncertain candidates move earlier, slow safe ones later; optimal only under independence and calibrated posteriors (D). *Measure:* offline replay on logged nights, GPU-minutes until the night's best candidate has run.

**M5. Two surrogates, used as priors.** (a) Knob level: GP + EI over 2-3 continuous knobs of a passing idea (LR, init scale, window size) with rung 4 as evaluator, which is LDM's setting and the strongest evidence [22]. (b) Idea level: sketch embedding reduced to about 10 dimensions, with dimension-scaled lengthscale priors [34], plus tags (part, direction, card, new/known/obvious, validated elsewhere, parameter delta, step ratio, baseline version) and a zero-shot LLM score as one feature [28]; GP or Bayesian logistic; targets: pass rung 4, overnight gap. Let it steer only when leave-one-run-out AUROC exceeds 0.6 with CI above 0.5; extends calibrate.py. Ideas validated elsewhere succeed more often than home-grown ones [20], so the "new" bonus should be learned, not hand-set. *Effect:* small lift at 300 verdicts or fewer, since 64-77% pairwise needed thousands of training pairs [26]; main value is its uncertainty, which feeds M6 (D). *Measure:* AUROC, Brier, top- vs bottom-quartile pass-rate ratio.

**M6. Explicit long-shot lane.** Reserve about 15-20% of round-1 build slots (floor 10%), chosen by Thompson draw from the M5 posterior or at random among step-outside and analogy clusters; lenient first gate (runs and learns, no near-baseline test at rung 3); one repair attempt; its own yield ledger with logged selection propensities; raise the share when exploit yield falls [36][39]. A 1-in-500 prior means a long-shot win needs replication before promotion [20]. *Effect:* protects the top-2% tail that exploit rankings miss (D), consistent with [1][36][37]. *Measure:* verified and non-obvious wins per GPU-minute by lane; randomised picks give unbiased off-policy estimates of M5's value.

**M7. Drift guard at promotion.** Version every verdict by baseline and key the hash memory by (script hash, baseline version) so old verdicts are not reused; discount old observations in M5 and per-card yield tables (sliding window or discount [19]); re-queue the top-k rejected close calls against the new baseline (already built, so GPU time only); re-measure noise. *Effect:* stops stale priors ranking ideas against a baseline that no longer exists (D). *Measure:* share of re-queued close calls that flip; surrogate calibration before vs after promotion.

**M8. Simple-regret allocation across pipeline stages.** Treat interrogation depth, sketch contexts and builder variants as arms, objective cost per verified win, allocated by top-two sampling or SH using the plain/climb arms [4][5]. *Effect:* shows which stages pay (D); RE-Bench hints breadth beats depth for agents [40]. *Measure:* verified wins per dollar with intervals over several runs; retire arms by e-value.

## Limits

- LDM is a preprint with self-reported gains on continuous knobs. I found no source showing a text-embedding surrogate predicts recipe-change outcomes; [26] is the nearest.
- The simulation assumes Gaussian, independent rung noise; the PPV arithmetic assumes power 0.8.
- Not verified, excluded: patent and venture-capital power-law figures, the optimizer's-curse paper, NIH percentile-score studies, 70/20/10 portfolio rules.

## Sources

- [1] Azevedo et al. 2020, A/B Testing with Fat Tails (JPE). https://ideas.repec.org/a/ucp/jpolec/doi10.1086-710607.html ; full text https://www.gwern.net/doc/statistics/decision/2019-azevedo.pdf
- [2] Schmit, Shah, Johari 2019, Optimal Testing in the Experiment-rich Regime. https://arxiv.org/abs/1805.11754
- [3] Xie et al. 2024, Cost-aware BO via the Pandora's Box Gittins Index. https://arxiv.org/abs/2406.20062
- [4] Bubeck, Munos, Stoltz, Pure Exploration for Multi-Armed Bandits. https://arxiv.org/abs/0802.2655
- [5] Russo, Simple Bayesian Algorithms for Best Arm Identification. https://arxiv.org/abs/1602.08448
- [6] Karnin, Koren, Somekh 2013, Almost Optimal Exploration in Multi-Armed Bandits. https://proceedings.mlr.press/v28/karnin13.html ; Jamieson, Talwalkar 2016, Non-stochastic Best Arm Identification and Hyperparameter Optimization. https://proceedings.mlr.press/v51/jamieson16.html
- [7] Li et al. 2018, Hyperband. https://jmlr.org/papers/v18/16-558.html ; brackets https://arxiv.org/abs/1603.06560
- [8] Li et al. 2020, ASHA. https://arxiv.org/abs/1810.05934
- [9] Mallik et al. 2023, PriorBand (appendix D.1.5). https://arxiv.org/abs/2306.12370
- [10] LCDB 1.1, learning curves are ill-behaved. https://arxiv.org/abs/2505.15657
- [11] Wen et al. 2025, Fantastic Pretraining Optimizers. https://arxiv.org/abs/2509.02046
- [12] Magnusson et al. 2025, DataDecide. https://arxiv.org/abs/2504.11393
- [13] Narang et al. 2021, Do Transformer Modifications Transfer? https://arxiv.org/abs/2102.11972
- [14] Johari, Pekelis, Walsh, Always Valid Inference. https://arxiv.org/abs/1512.04922
- [15] Ramdas et al. 2023, Safe anytime-valid inference. https://arxiv.org/abs/2210.01948
- [16] Wang, Ramdas, False discovery rate control with e-values. https://arxiv.org/abs/2009.02824
- [17] Hagele et al. 2024, Scaling laws beyond fixed durations. https://arxiv.org/abs/2405.18392
- [18] Besbes, Gur, Zeevi, Non-stationary bandits. https://arxiv.org/abs/1405.3316
- [19] Garivier, Moulines, UCB for non-stationary bandits. https://arxiv.org/abs/0805.3415
- [20] Kohavi et al. 2014, Seven Rules of Thumb. https://www.exp-platform.com/Documents/2014%20experimentersRulesOfThumb.pdf
- [21] Wong, Siah, Lo 2019, clinical trial success rates. https://pmc.ncbi.nlm.nih.gov/articles/PMC6409418/
- [22] Yu et al. 2026, Large Discovery Models. https://arxiv.org/abs/2608.15669
- [23] Karpathy, autoresearch. https://github.com/karpathy/autoresearch
- [24] Si, Hashimoto, Yang 2025, Ideation-Execution Gap. https://arxiv.org/abs/2506.20803
- [25] Si, Yang, Hashimoto 2024, Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109
- [26] Wen et al. 2025, Predicting Empirical AI Research Outcomes. https://arxiv.org/abs/2506.00794
- [27] Song et al. 2024, OmniPred. https://arxiv.org/abs/2402.14547
- [28] Liu et al. 2024, LLAMBO. https://arxiv.org/abs/2402.03921
- [29] Nguyen et al., LM embeddings can be sufficient for BO. https://arxiv.org/abs/2410.10190
- [30] Lin et al. 2024, INSTINCT. https://arxiv.org/abs/2310.02905
- [31] Novikov et al. 2025, AlphaEvolve (section 2.4). https://arxiv.org/abs/2506.13131
- [32] Lange et al. 2025, ShinkaEvolve. https://arxiv.org/abs/2509.19349
- [33] Toledo et al. 2025, AI Research Agents for ML (MLE-bench). https://arxiv.org/abs/2507.02554
- [34] Hvarfner et al. 2024, Vanilla BO in high dimensions. https://arxiv.org/abs/2402.02229
- [35] Gao et al. 2022, Reward model overoptimization. https://arxiv.org/abs/2210.10760
- [36] Rzhetsky et al. 2015, Choosing experiments. https://pmc.ncbi.nlm.nih.gov/articles/PMC4664375
- [37] Wang, Veugelers, Stephan, Bias against novelty. https://www.nber.org/papers/w22180
- [38] Azoulay et al., Incentives and creativity. https://www.nber.org/papers/w15466
- [39] Bloom et al. 2020, Are ideas getting harder to find? https://www.aeaweb.org/articles?id=10.1257/aer.20180338
- [40] Wijk et al., RE-Bench. https://arxiv.org/abs/2411.15114
- [41] Rainforth et al., Modern Bayesian Experimental Design. https://arxiv.org/abs/2302.14545
