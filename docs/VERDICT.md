# How a result becomes a result

*The statistics and the controls behind the ladder and the overnight verdict, in plain words. Built 2026-10-13 from the research in `research_notes/idea_generation/` (briefs 04, 06, 11, 12).*

## Why the rules exist

Every system in the literature that lets an AI propose and test changes ends up fooled by its own verifier: speed-ups that vanish after decontamination, records that were silent no-ops, agents that hard-code answers, wins on one seed that invert on forty. The remedies are the same everywhere: hide the exam, replicate before promotion, run placebos and known winners through the same pipe, log what a change actually did, and never let the test's decision rule depend on peeking at the data unless the rule was built for it.

## Controls, every run

Three control scripts go up the same ladder as every candidate at the start of each run:

- **A placebo**: the baseline with a different data-order seed. It must never win. If it does, the ladder or the verdict is calling noise a result.
- **A known winner**: zero-initialised output projections, a change with a documented small gain. It should pass. If it is rejected, the ladder has a measured false negative.
- **A known loser**: both learning rates times ten. It must fail.

Two more positive controls, QK-norm and a parameter-matched ReLU² feed-forward, can be added. The overnight runner can send any of them through the full verdict with `--controls`, which measures the night's own false-positive rate and power. Controls never enter the pool or the selection; the report shows their outcome. A control that stops before the learning rung (at the boundary, the build or the timing check) tested nothing, and is reported as broken rather than as a pass.

## The silent no-op

A candidate whose loss curve is identical to the baseline's at every step changed code that training never reads. The ladder fails it at rung 3 with that reason. The public speedrun log contains exactly such a "record".

The rule can only fire when two runs of the same code give the same numbers. On this GPU they do not: the same recipe re-run with the same seed drifts by about 0.01 in loss within twelve steps, which is well below the spread between seeds but far above the rule's tolerance. So on this machine a silent no-op passes the ladder and is caught one stage later, by the overnight verdict, as a fail or a close call; it costs GPU time, never a false win. The structural detector now exists: before any card time a reach audit runs one forward and backward pass on the processor; a parameter the change added that receives no gradient, or a model-code change whose output at initialisation is identical to the original's with no parameter added, fails at the build rung.

## The overnight verdict

Each candidate is trained for the full budget from several random starts; seed i of the candidate is paired with seed i of the pooled baseline, which share the data order. The exam is run by the harness on the saved weights.

**The test.** For each new seed the run computes an e-value: the evidence that the candidate beats the baseline by at least the margin, under a Gaussian model with the noise taken from the pooled baseline. An e-value is valid at every moment: seeds can be added or stopped on the evidence so far, and the chance of wrongly calling a win stays at most alpha. A p-value does not have this property, which is why the earlier staged design was wrong.

- **verified**: e-value at least 100 (alpha 1%) for a margin of 0.005 nats, at least 3 seeds, and it survives the e-BH correction across the night's candidates.
- **stackable**: e-value at least 20 (alpha 5%) for a margin of 0.002 nats, at least 3 seeds, and the gap had the same sign at every rung. A stackable change is too small to be a win on its own but real enough to compose: it feeds composition and promotion by accumulation.
- **close call**: better than the baseline mean but neither.
- **promising**: better, with fewer than 3 seeds so far.
- **fail**: not better.

**Seeds.** Every candidate gets seed 0. A candidate worse than the baseline's worst seed stops there. Otherwise seeds are added while the candidate is still promising or a close call, up to the maximum, and stopped early for futility if the first two seeds are both below the baseline's worst. Because the test is anytime-valid, none of this inflates the false-verified rate.

**Calibration.** The rule was tuned by simulation on 2026-10-13: with five baseline seeds and up to five candidate seeds, the false-verified rate under optional stopping is 0.7% at a nominal 1%; power is 74% for an effect of three noise units and 92% with eight seeds. The simulation treats runs as independent; sharing the data order between paired seeds only makes the real test more conservative.

**Compute matching.** A candidate that is slower per step at the same tokens spent more compute. With `--scaling-curve` the baseline is also trained at 1.25, 1.5 and 2 times the tokens, and each candidate's gain is reported against the baseline at its own compute, as a delta beside the verdict.

**Scale check.** With `--scale-check`, winners are trained again at double the tokens, both sides; a gain that does not hold there is flagged.

**Tuned-baseline duel.** With `--duel`, optimiser, schedule and initialisation ideas face a baseline whose weight decay and learning rate were tuned the same way as the candidate's, at half budget, before the verdict. Claimed optimiser gains in the literature shrink by a third or more under this rule.

## The ladder's own honesty

- A long-shot lane (20% of builds by default) is drawn at random from step-outside, analogy, adapt and new clusters, with a lenient first learning gate. Its yield is reported separately, so novelty is protected without being forced on the main line.
- A hedge lane (off by default) sends a random share of candidates that failed the matched-step gap straight to the long run and the night, so the ladder's false-reject rate can be measured.
- A fidelity probe diagnoses every checked candidate and checks whether the quantity its sketch named actually moved in the stated direction.
- A novelty gate stops near-duplicates of built ideas before any GPU time, and builds a random tenth of them anyway to measure the gate.
- Each round's discovery curve, new idea clusters per agent and per card, is recorded; cards whose sketches keep landing in the same clusters are retired.

## The critic, measured

The pre-mortem critic can be calibrated on planted flaws (`python -m nano.critic_check`): five mutants of the original with a known failure class, the two known winners and the placebo go through the pre-mortem blind. Fable's first calibration (2026-10-13): it named the planted class on 4 of 5 mutants, but it also raised high or medium objections of nearly every class against the known winners and two high ones against the placebo, so its severity does not separate a flawed idea from a good one. Reading: the critic's objections are a checklist worth resolving by measurement, which is how the loop uses them, and never a gate. The calibration file is memory/critic/<model>.json.
