# 05. Scientific discovery: theory and automated-discovery evidence (2026-10-13)

Evidence labels: **H** large controlled or independently replicated; **M** peer-reviewed or documented, single study or small n; **L** self-report, preprint, case study or press. "(inference)" marks my reasoning, not a finding.

## Bottom line

1. Theory says little about the mechanics of generating ideas but converges on three triggers: a surprising observation (Peirce, Kuhn, Dunbar), live rivals (Platt), and falsifiable novel predictions (Lakatos, Popper). [1][3][4][6][9]
2. LLM ideas look more novel than expert ideas but lose more after execution: AI-idea scores fell 1.05 to 1.98 points, human ideas 0 to 0.63. [11][12]
3. Judging is the weak link. Best LLM pairwise judge 53.3% vs 56.1% human inter-reviewer consistency [11]; LLM-judged novelty correlates -0.29 with later impact [14]; off-the-shelf LLMs are near chance at predicting which idea wins empirically [15].
4. With a cheap automatic evaluator (kernel timing, validation loss), LLM search and evolution works [39][40][41][42]. A training run is such an evaluator: spend runs on selection, LLM opinion only on triage.
5. Yield is a steep funnel: about 5,000 ideas, 1,100 run, 21 wins [29]; about 700 autoresearch edits, about 20 kept [43][44].

## 1. Theory, reduced to what generates ideas

- **Peirce, abduction** (conceptual). Abduction "is the only logical operation which introduces any new idea" and begins "The surprising fact, C, is observed" [1]. Magnani separates selective abduction (pick among known hypotheses) from creative abduction [3]; the "bad lot" worry: best-explanation choice is only as good as the pool [2]. Lever: seed ideation from a surprise; protect pool diversity.
- **Simon and Langley** (L-M). BACON simulated Kepler's third law, KEKADA the Krebs cycle [3][5], the latter via a focus-on-the-unexpected heuristic [9]; critics say such programs cannot decide which data matter or invent new concepts [3]. Lever: cheap rule operators (ratios, ablations) on run logs.
- **Kuhn, Lakatos** (conceptual). "Anomaly appears only against the background provided by the paradigm" [3]. Lakatos: a positive heuristic supplies hints for modifying refutable variants, anomalies can be set aside in temporary quarantine, and a programme is progressive only if novel predictions are corroborated [4]. Lever: log predictions first; budget by corroborated-prediction rate.
- **Platt, strong inference** (L). Rivals, crucial experiment, clean result, recycle [6]. Davis: "more an inspirational tract than the development of a formal scientific methodology"; critics find no evidence it explains scientific progress and note rival sets cannot be enumerated; Davis adds it is more often a social than an individual enterprise [7]. Only 21 of 100 sampled ecology and evolution studies tested more than one hypothesis [8]. Chamberlin: a working hypothesis becomes a "ruling" one [7]. Lever: force rivals; assign a challenger.
- **Dunbar in vivo** (M; 4 molecular-biology labs, 16 meetings). Of 99 analogies, 40 same-organism, 57 other-organism, 2 non-biological (used only to explain); 31 of 57 other-organism analogies rested on homology, 31 of 40 same-organism ones recalled a specific case, 22 of them the lab's own earlier experiments [9]. In four meetings of one lab, 18 of 70 findings were unexpected; the group logged 176 interactions on unexpected vs 23 on expected findings; 8 of 10 inconsistent surprises produced new hypotheses; early surprises on peripheral hypotheses were ignored [9]. Insight was "tinkering": small analogy, induction and deduction steps distributed across lab members [9]. Lever: near-domain analogy plus case memory; surprise triage; multi-agent critique.
- **Popper** (conceptual). Conceiving an idea seems "neither to call for logical analysis" [3], so conjectures-and-refutations supplies selection, not generation; Simonton's BVSR framework adds a generator: partially blind variation, then selective retention [10]. Lit2Test (2026) operationalises it: each proposal pre-commits the observation that would prove it wrong [17]. Lever: falsifier field plus volume with selection.

## 2. Automated discovery, 2024-2026

**Idea quality**
- Si et al. (49 writers, 79 reviewers, 298 blind reviews; M-H) [11]: AI vs human novelty 5.64 vs 4.84 (p<0.01), excitement 5.19 vs 4.55 (p<0.05), feasibility 6.34 vs 6.61 (n.s.), overall 4.85 vs 4.68 (n.s.); AI plus human rerank overall 5.34 (p<0.05). 4,000 seed ideas per topic gave 200 unique. Caveats: NLP prompting ideas only, underpowered for feasibility, human ideas were roughly the writers' top 43%. Human inter-reviewer consistency 56.1% (NeurIPS'21 66.0%, ICLR'24 71.9%).
- Execution follow-up (43 projects, 24 AI, 19 human, 100+ h each; M) [12]: AI ideas dropped novelty -1.05, excitement -1.76, effectiveness -1.88, overall -1.98; human -0.01, +0.08, -0.05, -0.63 (difference in drops p<0.05). Post-execution project-level gaps were not significant at n=43; across 181 reviews humans led on excitement, effectiveness, soundness and overall (p=0.01). Idea-stage scores weakly predicted execution scores.
- 13 experts judged 24% of 50 LLM research documents paraphrased or heavily borrowed; detectors missed them (M, small) [13].
- HindSight (30-month follow-up; L) [14]: LLM-as-judge saw no difference between retrieval-augmented and vanilla ideation (p=0.584); impact scoring rated retrieval 2.5x higher; impact correlated -0.29 with LLM-judged novelty.
- Outcome prediction (1,585 test pairs; M) [15]: off-the-shelf LLMs near chance; fine-tuned GPT-4.1 with retrieval 77% (NLP 64.4% vs 48.9% for 25 experts). LLM judges favor their own text [16].
- Generation aids (L): Nova's retrieval planning gave 3.4x more unique novel ideas [18]; MOOSE-Chem splits chemistry hypotheses into inspiration retrieval, composition, ranking [19].

**End-to-end systems**
- Sakana AI Scientist: v1 under $15 per paper, self-reported "near-human" reviewer [20]. Independent test: 42% of experiments failed on coding errors, micro-batching for SGD labelled novel, median 5 citations [21] (M). v2: one of three papers averaged 6.33 at an ICLR workshop (workshops typically accept 60-70% [23]; the Nature version cites 70% [25]), withdrawn by prior agreement; none met Sakana's main-track bar [22][23]; critics note humans chose what to submit [24].
- Google co-scientist (M, self-reported plus wet lab) [26]: Elo tournament with multi-turn debate for top hypotheses; the Evolution agent writes new hypotheses and never overwrites parents; Elo rose with compute over 203 goals; Elo-top answers hit 78.4% on GPQA diamond; experts (11 goals) gave novelty 3.64/5, impact 3.09/5. The authors warn Elo has no independent ground truth and "may favour results with attributes that do not necessarily align with scientists' preferences". Wet lab: 3 of 5 expert-picked AML drugs active (KIRA6 the reported hit among 3 novel candidates); drugs for 2 of 3 liver-fibrosis targets active; the cf-PICI hypothesis matched an unpublished result (n=1, answer known to the authors).
- FutureHouse (L-M): Robin proposed ripasudil for dry AMD, semi-autonomously [27]. Kosmos: 79.4% of statements accurate but 57.9% for synthesis vs 85.5% data analysis and 82.1% literature (102 statements); it invents unorthodox metrics and conflates significance with value [28].
- DeepScientist (L-M) [29]: 20,000+ GPU-hours, about 5,000 ideas, about 1,100 validated, 21 innovations; success 1-3%, about 60% of failed trials stopped by implementation errors, about $150 per finding.
- AutoDiscovery (L) [30]: MCTS rewarded by Bayesian surprise found 5-29% more LLM-judged surprising results; about two-thirds also surprised experts (surprise is not correctness).
- Audits: four failure modes (wrong benchmark, leakage, metric misuse, post-hoc selection) in two open-source AI scientists, better caught from logs and code than papers [31]; coding agents fabricated or invalidated results in about 80% of MLR-Bench cases [32]; LLMs score poorly at experimental design and model discovery, and explicit statistical models did not reliably help [33]; strong baselines struggle on most DiscoveryWorld tasks [34]. Coscientist planned and ran cross-coupling reactions [35] (execution, not hypothesis generation; inference).

**ML-training-specific**
- MLGym (13 tasks, M): agents improve baselines mainly via hyperparameters and "do not generate novel hypotheses, algorithms, architectures, or substantial improvements" [36]. RE-Bench (M-H): at 2 h agents score about 4x humans; humans overtake by 8 h and reach about 2x at 32 h [37].
- NanoGPT speedrun reproduction (M) [38]: without hints agents recover under 20% of known speedups; pseudocode hints lift o3-mini to 0.43; flat best-of-M generally matches iterated search. AIRA-dojo: operator and search design raised MLE-bench Lite medals 39.6% to 47.7% [39].
- AlphaEvolve (L-M, self-reported) [40]: program database, Flash/Pro ensemble, automated evaluators; 23% faster kernel, 1% less Gemini training time. Eureka (M): evolutionary LLM search beat human-written rewards on 83% of 29 tasks [41].
- Karpathy's autoresearch: one editable file, fixed 5-minute budget, keep only lower val_bpb, simplicity rule, "think harder" when out of ideas [42] (primary). Secondary reports (L): about 700 edits, about 20 kept, time-to-GPT-2 2.02 to 1.80 h, kept changes transferred depth 12 to 24, validation-overfit worry [43][44].

## 3. Pattern across studies

- Novelty rises but quality does not follow: execution erases the advantage [12], LLM-judged novelty anti-correlates with impact [14], and a 2026 survey finds AI weakest on genuinely novel ideas [45]. Failures sit in execution (implementation errors [29][21], fabricated results [32]).
- Gaps (inference): no published ablation of debate or tournament against best-of-N in idea loops; no ML-training test of strong-inference branching or surprise-driven ideation.

## 4. What would transfer to an LLM-driven idea loop

Setting: nano-replica training recipe, 20-30 min per run on one RTX 4050, 3 seeds per claimed gain, win = beat baseline by more than 2 seed SD, plain-agent arm at matched spend [L1]. That is 2-3 runs per hour versus autoresearch's 12 [42], so triage matters.

**M1. Prediction-first proposals with a falsifier (Lakatos, Popper, Peirce).** Each idea carries a mechanism sentence, predicted validation-loss delta with interval, the observation that would falsify it, and the rival it beats; no fields, no run. Split budget across themes by corroborated-prediction rate. Basis: [4][17]; learned outcome prediction beats chance only after supervised training [15]. Expected (inference): fewer vague ideas (the one infeasibility termination in [12] was a vague idea) and a labelled set for calibrating judges. Measure: interval coverage vs nominal 80%, Brier score on sign, Spearman(predicted, realized), share killed pre-run.

**M2. Anomaly ledger and an "explain the surprise" agent (Peirce, Dunbar, KEKADA).** After each run compute surprise = |realized - predicted| / seed SD plus curve anomalies (loss spikes, norm outliers). At z>2 replicate on a new seed first (seed noise is large at this scale [L1]), then require 3 rival explanations and the one run that separates them; two linked surprises trigger a model-level revision; early peripheral surprises are logged, not chased. Basis: [9][30][5]; autoresearch's reported finds were oversights such as a missing QKNorm scale [44]. Expected (inference): surprise-seeded follow-ups win more often than prior-seeded ones; mainly escapes tuning plateaus. Measure: seed-robust wins per 10 runs, surprise-seeded vs prior-seeded; time to rediscover hidden ladder items [L1]. Drop if ratio is below 1.2.

**M3. Strong-inference branching with computed information gain (Platt, Chamberlin).** For each confirmed win list at least 3 mechanism rivals; pick the next run by expected information gain over a small explicit Bayesian table, not LLM intuition [33]; a separate challenger agent owns the rivals [7]; flag any hypothesis above 0.8 prior with no discriminating test. Basis: [6][7][8]. Expected (inference): fewer unexplained wins, better composition and transfer, at extra run cost. Measure: bits per run; share of kept changes with a confirmed mechanism; transfer of kept changes to a second scale (autoresearch reported depth 12 to 24 for about 20 changes [44]).

**M4. Tournament triage with debate, calibrated on outcomes (co-scientist).** Elo over pending proposals (start 1200), order-swapped pairs, judges from at least 2 model families, multi-turn debate only for top-k; it allocates screening runs and never declares wins; the judge is re-scored on every completed run. Basis: [26]; counter-evidence [11][14][15][16]; one human reranker lifted AI overall 4.85 to 5.34 [11]. Expected (inference): helps only if judge-outcome rank correlation is positive, else equals random. Measure: Kendall tau and AUC of tournament score vs realized delta; top-quartile vs random kept-rate; auto-disable if AUC is below 0.55 after 50 ideas; add a human-rerank arm (top 10 per day).

**M5. Evolution by offspring with an archive (co-scientist Evolution, AlphaEvolve).** Children are combinations, simplifications, move-away or literature-grounded variants of top diffs; parents are never edited; archive by mechanism class with 3-4 islands; keep the simplicity rule (removal at equal loss is a win [42]). Basis: [26][40][39][41]; but flat best-of-M matched iterated search at hint levels 1-3 [38]. Expected (inference): gain over flat best-of-N unproven here; main payoff is composing independently validated diffs. Measure: seed-robust wins per GPU-hour, evolution arm vs flat best-of-N arm at equal tokens, at least 3 loop seeds.

**M6. Inspiration retrieval, composition and experiment memory (MOOSE-Chem, Dunbar, Nova).** Two calls: retrieve k near-domain inspirations (adjacent architectures, speedrun records, the loop's own ledger), then compose with a diagnosed bottleneck of the baseline. Confine far-field analogy to explanation (2 of 99 analogies [9]). Basis: [19][18][9]; retrieval-augmented ideas scored 2.5x on hindsight impact while the LLM judge saw no difference [14]; hints lifted recovery from under 0.20 to 0.43 [38]. Expected (inference): more distinct, feasible, less duplicated ideas. Measure: unique ideas per 100 (embedding clusters), prior-art scoop-check rate, ladder rediscovery with vs without retrieval.

**M7. Diversity gate and funnel accounting.** Cluster proposals by mechanism class, module touched and predicted effect; only the best per cluster enters screening; per-class quotas; log proposed, deduped, screened, 3-seed confirmed, transferred. Basis: 200 unique of 4,000 [11]; funnels [29][43]. Expected (inference): fewer duplicate runs, more wins per GPU-hour. Measure: duplicate ratio, GPU-hours per confirmed win, implementation-failure rate (about 60% of failures in [29]).

**M8. Independent auditor and confirmation stage.** A separate agent, blind to the proposer's rationale, re-runs top wins on fresh seeds and a held-out shard, checks equal tokens and parameters, metric definition, leakage and post-hoc selection from logs and code [31], and injects sham null ideas to estimate false positives. Basis: [31][32][28][21]; overfitting worry [43]. Expected (inference): fewer false positives, an honest shrinkage estimate. Measure: confirm-stage replication rate; winner's-curse shrinkage (mean search delta minus mean confirm delta); sham false-positive rate (target under 5%).

## 5. Caveats

Evidence is mostly NLP, biomedicine and large-run ML, not 20M-parameter nano runs where seed noise is large [L1]. Developer-reported results dominate; independent checks [12][21] are less flattering. Autoresearch numbers come from press and blogs. Several 2026 items [14][17][45] are preprints.

## Sources

[1] SEP Peirce on abduction. https://plato.stanford.edu/entries/abduction/peirce.html
[2] SEP Abduction. https://plato.stanford.edu/entries/abduction/
[3] SEP Scientific Discovery. https://plato.stanford.edu/entries/scientific-discovery/
[4] SEP Lakatos. https://plato.stanford.edu/entries/lakatos/
[5] Kulkarni and Simon, KEKADA (listing only; fetch blocked). https://kilthub.cmu.edu/articles/journal_contribution/The_processes_of_scientific_discovery_the_strategy_of_experimentation/6618701
[6] Platt's steps. https://en.wikipedia.org/wiki/Strong_inference
[7] Davis 2006. https://escholarship.org/uc/item/88f9r3j5
[8] Betini 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5319344/
[9] Dunbar, How scientists think. https://sites.cc.gatech.edu/classes/AY2013/cs7601_spring/papers/Dunbar.pdf
[10] Simonton, BVSR. https://en.wikipedia.org/wiki/Dean_Keith_Simonton
[11] Si 2024. https://arxiv.org/abs/2409.04109
[12] Si 2025, Ideation-Execution Gap. https://arxiv.org/abs/2506.20803
[13] Gupta, plagiarism. https://arxiv.org/abs/2502.16487
[14] HindSight. https://arxiv.org/abs/2603.15164
[15] Predicting research outcomes. https://arxiv.org/abs/2506.00794
[16] LLM self-preference. https://arxiv.org/abs/2404.13076
[17] Lit2Test. https://arxiv.org/abs/2608.22948
[18] Nova. https://arxiv.org/abs/2410.14255
[19] MOOSE-Chem. https://arxiv.org/abs/2410.07076
[20] AI Scientist v1. https://arxiv.org/abs/2408.06292
[21] Beel, independent evaluation. https://arxiv.org/abs/2502.14297
[22] AI Scientist v2. https://arxiv.org/abs/2504.08066
[23] The Decoder. https://the-decoder.com/ai-generated-paper-passes-peer-review-before-planned-withdrawal/
[24] TechCrunch. https://techcrunch.com/2025/03/12/sakana-claims-its-ai-paper-passed-peer-review-but-its-a-bit-more-nuanced-than-that
[25] AI Scientist, Nature 2026. https://arxiv.org/abs/2606.15497
[26] Google co-scientist. https://arxiv.org/abs/2502.18864
[27] Robin. https://arxiv.org/abs/2505.13400
[28] Kosmos. https://arxiv.org/abs/2511.02824
[29] DeepScientist. https://arxiv.org/html/2509.26603
[30] AutoDiscovery. https://arxiv.org/abs/2507.00310
[31] More You Automate, Less You See. https://arxiv.org/abs/2509.08713
[32] MLR-Bench. https://arxiv.org/abs/2505.19955
[33] BoxingGym. https://arxiv.org/abs/2501.01540
[34] DiscoveryWorld. https://arxiv.org/abs/2406.06769
[35] Coscientist. https://arxiv.org/abs/2304.05332
[36] MLGym. https://arxiv.org/abs/2502.14499
[37] RE-Bench. https://arxiv.org/abs/2411.15114
[38] LLM Speedrunning Benchmark. https://arxiv.org/html/2506.22419
[39] AIRA-dojo. https://arxiv.org/abs/2507.02554
[40] AlphaEvolve. https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
[41] Eureka. https://arxiv.org/abs/2310.12931
[42] autoresearch. https://github.com/karpathy/autoresearch ; https://github.com/karpathy/autoresearch/blob/master/program.md
[43] VentureBeat. https://venturebeat.com/technology/andrej-karpathys-new-open-source-autoresearch-lets-you-run-hundreds-of-ai
[44] Phil Schmid. https://www.philschmid.de/autoresearch
[45] Auto-Research survey. https://arxiv.org/abs/2605.18661
[L1] Local file: C:/Users/User/Desktop/AGI/EXPERIMENT_PLAN.md
