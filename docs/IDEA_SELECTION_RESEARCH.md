# Picking the right ideas: what went wrong, what the evidence says, what to change

Written 2026-10-17. Inputs: the skel-1 selection log, the existing brief
`research_notes/thinking_parts/08_selection.md` (its evidence [1]-[34] is not repeated here), and ten web
searches with three papers read in full. Selection code: `ideate.cluster_score`, `ideate.select_clusters`,
`tree.split_select`, `loop._select_with_lanes`, `loop._novelty_filter`.

## 1. What actually happened in skel-1 (from `selection.jsonl`, 237 rows)

| reason recorded | clusters |
|---|---|
| picked by score (main) | 14 |
| picked by the long-shot lane | 10 |
| scored at or above the cut, but the turn went to another part ("slots exhausted") | 106 |
| below the cut | 107 |

The final model's parts, as the selector saw them:

| cluster | part | score | cut | outcome |
|---|---|---|---|---|
| Signed linear reads | depth_stream_mix inward | 1.733 (rank 3 in part) | 0.95 | slots exhausted |
| Narrow keys, wide values | attn_latent_kv inward | 0.90 | 0.95 | below the cut by 0.05 |
| Depth-lag signed reads (delay-line precursor) | depth_stream_mix outward | 0.20 | 0.867 | below the cut |
| Self-excluding shifted KV + sink | attn_latent_kv outward | 0.95 | 0.867 | slots exhausted |

Scores: picked-main mean 1.74 (0.87 to 3.65); below-the-cut mean 0.56 (-0.4 to 0.9).

Diagnosis, in three parts:

1. **The score has no signal inside the plausible tier.** 106 clusters scored at or above the cut and lost
   only because another part's turn came first. Among those 106 the round-robin, not the score, decided.
   The signed reads were rank 3 in their part; the part got fewer slots than that.
2. **The score measures convergence and cheapness, not effect.** Its largest term is "how many different cards
   produced this idea". The delay line scored 0.2 because one context wrote it once. Agreement across
   angles is evidence of obviousness as much as of quality.
3. **Only 24 of about 130 plausible ideas got a test.** The ladder (rung 3 = 45 steps, about a minute of
   GPU) is cheap; the build in front of it (one strong-model call, about 35k tokens) is what limits the count.

So the failure was not "the wrong ranking". It was "a ranking that cannot rank, followed by a fair draw,
with too few tickets".

## 2. What the evidence says

### Judging ideas from text is weak, and stays weak with better models
- Frontier models predict real experiment outcomes at 14-26% on SciPredict (2026), about the same as domain
  experts' 20%; unlike experts, their confidence does not track their accuracy.
- Pairwise "which of two ideas scores higher on this benchmark": GPT-5 57-61%; untrained open models
  20-30%; a model fine-tuned on about 10,600 labelled pairs reaches 71-77% (2605.21491). The gain comes from
  outcome data, not from reasoning.
- The ideation-execution gap (Si, Hashimoto, Yang, ICLR 2026; 43 experts, 100+ hours per idea): the ideas
  rated most novel and exciting before execution lost the most after it. Correlation between ideation-stage
  scores and execution-stage scores: -0.3 to +0.2. Excitement at ideation was negatively correlated with
  the outcome for AI ideas.
- Human panels: grant reviewer agreement ICC about 0; percentile score explains under 1% of later output
  across 102,740 funded grants (brief 08, [18]-[20]).
- Our own critic calibration: finds the planted flaw 4 of 5 times, objects to good ideas just as hard.

### What does predict
- **A pilot.** Preference models at 65-69% on text rise to 78-84% after a 5-minute pilot (brief 08, [26]).
- **In-environment outcome records.** Raw (change, gain) records from the same environment lift rank
  correlation to 0.64-0.90; records from other environments do not transfer (brief 08, [28]).
- **Lineage success.** Selecting by clade success correlates 0.78 with realised value against 0.29 for
  parent score alone (HGM, brief 08, [32]).
- **Measured premise.** The ideas that became QK-norm, mHC and gating started from a measured pathology,
  not from a judged sketch (brief 12).

### How to allocate tests when the cheap test is noisy
- Successive halving / Hyperband / ASHA: evaluate everyone at the cheapest fidelity, keep the top 1/eta,
  spend eta times more on those, repeat. The theory gives the budget at which the true best survives.
- Known weakness: fixed halving mis-allocates when early performance poorly predicts final performance.
  We have measured exactly this: looped depth and the zero-init bigram head looked bad at 45 and 240 steps
  and helped at 50M tokens. The remedy in the literature is racing with adaptive allocation (DyHPO) and a
  randomised hold-out of eliminated candidates to measure the false-reject rate.

### Inside the plausible tier, randomise and spread
- Partial lotteries above a quality bar are now used by the ERC, British Academy, FWF and others; the FWF
  analysis found the lottery element shifted funding toward interdisciplinary and novel proposals. No trial
  yet shows higher-rated proposals produce better outcomes than near-threshold ones.
- Set selection: P(at least one win) is monotone submodular; greedy marginal gain with a redundancy penalty is
  within 1-1/e of optimal; equal weights beat fitted weights at small n (brief 08, [1]-[10]).
- Creators forecast others' ideas better than managers do (Berg 2016, 339 circus professionals against
  13,000 audience members), but not their own. The practical form is a peer vote.
- Pairwise comparison is easier, faster and needs fewer judges than rating, with near-identical rankings
  (Clark et al. 2018); the forecasting paper above requires order-swap consistency and reaches 85% on it.

## 3. What to change, in order

### R1. Test instead of rank: make the cheap test the selector
The one thing with strong evidence is a pilot. Rung 3 costs a minute. The bottleneck is the build.
- **Patch sketches.** The sketch format gets an optional PATCH block for ideas the inventor can write in
  under about twenty lines (soft-cap was one line, narrow keys two, value residual six). A script applies the
  patch to the baseline and files it as a candidate with card `patch`; rungs 0 to 3 run on it with no builder
  call. Ideas whose patch fails or that need engineering go to a builder as today.
- **Cheap builder for the rest.** Building is translation; the user's rule already puts mechanical roles
  on the cheap model. A cheap build is about a tenth of the cost. The strong model keeps revisions of near
  misses.
- **Successive halving on top.** Every plausible cluster to rung 3 (about 130 x 1 min = 2 h of GPU);
  the top third by learning gap to the long run (240 steps); the top five to the night. The hand-run of
  2026-10-15 (18 quick tests decided the final model) is this procedure done by hand.
- **Hedge for late payoff.** The hedge lane (a random share of rung-3 failures sent to the long run and the
  night) is on by default once tests are cheap, so the false-reject rate of the short test is measured.
- Measure: share of eventual winners present in the tested set; P(at least one verified win) per run.

### R2. Fix the draw inside the plausible tier (no model calls; brief 08 I1 and I4)
- Replace strict part round-robin with greedy marginal gain: score minus a penalty per pick already in the
  part minus a similarity penalty to picks, builds and ledger entries. Inward/outward shares stay as caps.
  Any part's best cluster can then win a slot; today it cannot when the part's turn is late.
- Treat the "slots exhausted" tier as what it is: a lottery. Draw from it uniformly with logged
  propensities, at least two draws per round, so the ledger gets rows the score did not choose. This is the
  only way to ever learn whether the score has signal (range restriction otherwise hides it).
- Measure: replay on the skel-1 sketches offline; the new slate must contain signed reads and narrow keys
  at the same k, and the maximum pairwise similarity of the slate must fall.

### R3. Put measurement into the score, take eloquence-adjacent terms out (brief 08 I2, I3, I6)
- **Premise term.** When TARGET names a diagnostic cell, score the distance of the baseline's measured value
  from the reference. Zero for "validation loss only". This is a free pilot: it says whether the lever the
  idea pulls exists in the measurements. The skeleton's four streams being nearly unused at initialisation
  was exactly such a cell, and every winner restructured the streams.
- **Outcome term.** Families = (part, TARGET cell) plus built neighbours by text similarity; a Beta
  posterior per family from the ledger (ladder failure, regression, improvement), Thompson-drawn into the
  score. One line per attempt; failure reasons are not fed back (they lowered accuracy in [27]).
- **Shrink the angle term.** Agreement across cards stays a positive signal but capped, because at 237
  sketches it mostly measures what is obvious.
- Measure: leave-one-run-out Spearman of score against realised learn_z, once 30+ builds exist.

### R4. A forecaster only as a gated tie-break, never a gate (brief 08 I7)
- At the cut line only (ranks k-2 to k+3), a cheap model of another family compares stripped sketches
  pairwise in both orders; strict consistency; it orders near-ties and never rejects.
- It stays off until its selective accuracy over the last 30 resolved pairs exceeds 0.55, and goes off
  again after a baseline promotion until re-measured. Expected ceiling without training data: about 60%.
- Not to build now: fine-tuning a forecaster. The evidence that it works used 10k labelled pairs; we have
  under 20 builds.

### R5. A peer vote as a comparison arm (Berg)
- The inventors are the creators. After clustering, each cheap-model call gets ten stripped sketches from
  other parts and ranks them pairwise; votes enter as one more term, logged, never as a gate.
- Measure: vote-weighted slate against score slate against random, by realised learn_z, over ten runs.
  If it does not beat random it goes.

### What not to do
- An LLM gate on sketches (the ideation-execution gap and SciPredict say it discards the wrong ones).
- Fitted selection weights before about 100 builds (1/N beats fitted weights at small n).
- Rewarding stated excitement or novelty in the score (negatively correlated with outcome for AI ideas).

## 4. Expected effect and how we would know
- R1 turns a 24-of-130 draw into a 130-of-130 pilot; the hand-run of 2026-10-15 is the existence proof
  that the pilot finds the winners the score missed.
- R2 and R3 are offline-replayable on the skel-1 and arch-2 sketch catalogues already on disk before any
  model call: the test is whether the known winners enter the slate at the same k.
- The number that settles it over time: P(at least one verified win per run) and the share of winners
  that were in the tested set, both already derivable from the ledger.

## Sources
- SciPredict: https://arxiv.org/abs/2604.10718
- Forecasting research success by comparative evaluation: https://arxiv.org/html/2605.21491
- The ideation-execution gap (Si, Hashimoto, Yang): https://arxiv.org/html/2506.20803
- Can LLMs generate novel research ideas (2024): https://arxiv.org/pdf/2409.04109
- Berg 2016, creative forecasting: https://mackinstitute.wharton.upenn.edu/2016/balancing-on-the-creative-high-wire/
- Pairwise vs Likert (Clark et al. 2018): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5749798/
- Successive halving / Hyperband overview: https://D2L.AI/chapter_hyperparameter-optimization/sh-intro.html
- Racing with adaptive allocation (DyHPO): https://proceedings.neurips.cc/paper_files/paper/2022/file/57b694fef23ae7b9308eb4d46342595d-Paper-Conference.pdf
- Randomised selection above a threshold: https://arxiv.org/pdf/2506.19083
- Partial lotteries in funding (Nature Index): https://www.nature.com/nature-index/news/luck-of-the-draw
- Evolutionary archives, islands and MAP-Elites (GigaEvo): https://arxiv.org/pdf/2511.17592v1
- Brief 08 and its 34 references: `research_notes/thinking_parts/08_selection.md`
