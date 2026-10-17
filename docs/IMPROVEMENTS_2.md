# Second interrogation of the run

*2026-10-13. The rebuilt loop questioned again with its own method: every part, every aspect, open questions followed two levels down when the answer would change what gets built. This pass also questions the premises (what is measured, against what, and whether the result can mean anything). Answers come from the code and the recorded runs, not from hopes. Each improvement ends with a cost (small = under an hour, medium = a few hours, large = a day). The first pass is in IMPROVEMENTS.md; everything there is built.*

---

## 0. The premises, questioned upward

**Q: When the run finds a winner, what has been shown: that the method works, or that the model is good?**
Nothing separates them. The nano track has no control arm. The puzzle harness compares the scaffold against best-of-N at matched cost; the nano loop compares nothing against anything. A verified winner is evidence that Fable plus a verifier can improve a small trainer. It is not evidence that the map, the research, the interrogation or the selection contributed.
**Follow-up: what is the right control?** The same strong model, the same builder prompt, the same verification ladder, the same token spend, with no map, no research, no interrogation, no selection: ask for a change and a complete script, N times, from the existing "seeded" and "formal" implementation cards that already exist in the loop. Count verified wins and the share tagged new, per dollar.
**Follow-up: does the control need the overnight run too?** Yes, or the comparison stops at "checked", which is a weak signal. Both arms' pools go into one overnight batch.
→ **Improvement A. A `--arm plain` mode: N direct build calls through the existing cards, same ladder, same budget accounting, pooled into the same overnight run, reported side by side.** This is the difference between a demo and an experiment. *Small to medium.*

**Q: Is the exam trustworthy?**
No. The candidate runs its own exam. The diff check protects the text of `evaluate`, the loader's constructor and `sequential`, but a candidate may still: call `evaluate` on fewer tokens or after extra steps from inside `main`; read `val.bin` directly during training (the string appears in the loader, which is open to the data part); import `socket`, `urllib`, `subprocess` or `ctypes`, all standard library and therefore allowed; and report a `tokens` figure the verifier takes on trust. None of this needs malice. A model told "lower the validation loss" and given the validation file will, at some point, use it for learning-rate selection or early stopping. That is tuning on the test set and it looks like a win.
**Follow-up: what makes the exam external?** The trainer saves its weights at the end. A separate evaluator, owned by the harness, loads the candidate's model class, restores the weights, and runs the baseline's `evaluate` with the baseline's loader. The candidate's own `val_loss` becomes a self-report that is compared with the external number; a mismatch is a failure.
**Follow-up: what about the token budget?** The external runner cannot see batches, but it can audit two things cheaply: wall-clock must be within the step-time ratio measured at rung 2 times the baseline's full-run time, and the saved weights must not exist before the run. A candidate that trains longer than its step ratio allows is flagged.
→ **Improvement B. Exam integrity: a denylist of standard-library modules that give network, process or memory access; a scan of changed code for any reference to the validation split; checkpoint saving in the trainer; an external evaluator in the overnight runner that recomputes the exam from the saved weights; a wall-clock audit against the rung-2 step ratio.** *Medium.*

**Q: Is this the right regime to find anything in?**
The baseline trains 21 million parameters on 50 million tokens: 2.4 tokens per parameter, against roughly 20 at the compute-optimal point. Everything in this regime is severely undertrained. What wins here is "learn faster in the first minutes": optimiser, learning-rate schedule, initialisation, normalisation. Architectural ideas that pay off with more data are invisible. The first real run produced QK-norm, zero-init and sliding windows, which is exactly the profile this regime rewards.
**Follow-up: what fits in the same 31 minutes?** A 10-million-parameter model at 100 million tokens is about 10 tokens per parameter and the same wall-clock. It is still undertrained but twice as close to the regime where architecture matters, and the noise floor per run should be lower because the model sees more data.
**Follow-up: can a winner be checked for transfer without renting hardware?** Partly. A verified winner can be rerun at double the token budget on the same card: if the gain grows or holds, it is a real effect; if it shrinks toward zero, it was an early-training artefact.
→ **Improvement C. Two decisions for the owner, not code: (1) whether to move the baseline to a smaller model with more tokens; (2) adding a "double budget" scale check for verified winners, reported as the sign of the gain's slope.** *Small code once decided.*

**Q: Is the budget fair?**
The budget is tokens, and the step-time rule allows a candidate to be twice as slow. Twice as slow at the same tokens is twice the compute. A candidate that doubles the work per token and gains a little has not improved the recipe; it has bought the gain. The opposite also holds: a faster candidate is penalised by nothing and rewarded by nothing.
**Follow-up: what is a compute-matched verdict?** Train the baseline once at 50, 62.5, 75 and 100 million tokens to get its loss-versus-tokens curve. A candidate with step ratio r is then compared with the baseline at r times the tokens, interpolated. Four baseline runs, once, reused forever.
**Follow-up: the parameter rule?** It is symmetric: plus or minus ten percent. A candidate that drops a third of the parameters at equal loss is a finding and is rejected at rung 1. The rule exists to stop "make it bigger"; it should be at most plus ten percent, any reduction allowed.
→ **Improvement D. Asymmetric parameter rule now (trivial). A compute-matched verdict from a one-time baseline token-scaling curve (medium, GPU time).**

**Q: Does the recipe ever get better?**
No. Every run starts from the same `train.py`. If a run finds a winner, the next run can rediscover it, and the verdict ledger will tell it not to, so the next run will find the second-best thing, against the old baseline. Winners never compound.
**Follow-up: what does compounding need?** A promotion step: a verified winner becomes the new baseline, with the old one kept as a version; the profile is rebuilt; the pooled baseline noise is re-measured for the new baseline. The whole-recipe part's assumption that "the best recipe is a sum of the best parts" becomes testable: promote one winner, then see whether the other winners still win against the new baseline.
→ **Improvement E. A promote command: candidate in, new versioned baseline out, profile and baseline seeds rebuilt, the ledger marked with the baseline version each verdict was against.** *Small.*

**Q: What is "new"?**
A cluster is new when a cheap model finds no match in a brief that another cheap model built from a few web searches. "New" therefore means "not found", which is weaker than it sounds. It is adequate for steering selection. It is not adequate for claiming novelty to another person.
**Follow-up: what would be adequate?** For verified winners only, one strong-model call with search: "name the closest existing technique and state the difference"; and the run should report, as numbers, how many ideas were tagged new, how many of the built, checked and verified ones were, and how many matched the private obvious answers. These numbers exist in the logs and are summarised nowhere.
→ **Improvement F. A scorecard and a written report per run: counts and conversion rates at every stage (sketches, clusters, new, obvious, interrogated, built, rung by rung, checked, verified), cost, time, idea sources, prediction accuracy once K exists, and a novelty note per verified winner.** *Small.*

**Q: How noisy is each rung?**
Unknown, and the design pretends it is zero. Rung 3 and rung 4 compare a candidate with the baseline's curve at "the same seed". The seed fixes the data order, but the initial weights come from the global random stream, and any change to the model, even one extra parameter, shifts that stream. So "same seed" is not "same initialisation", and the gap at 45 or 240 steps contains initialisation noise of unknown size. The profile holds one curve per step count, from one seed. Today's profile also still holds the 12-step and 30-step curves from the dry run; the real run will recompute them.
**Follow-up: what is the cheap calibration?** Run the baseline at 240 steps with seeds 1 and 2 as well (about ten minutes). The spread of the three curves at each step is the noise floor; the long gap is then reported in units of that spread, and the thresholds for "promising" become statistical rather than guessed.
**Follow-up: can the long curve say more than one number?** Yes. The gap at 45, 120 and 240 steps gives a trend. A candidate whose advantage shrinks over the run is an early-training artefact that will likely lose at 50 million tokens; one whose advantage grows is the one to seed first overnight. Ranking by the extrapolated gap is free, given curves that are already recorded.
→ **Improvement G. Calibrated rungs: baseline curves from three seeds, gaps in units of the seed spread, a trend across the long curve, ranking by the extrapolated gap.** *Small, ten minutes of GPU.*

---

## 1. The problem file and the rules

**Q: Who enforces each rule?** C1 same data: nothing (a candidate may read any file). C2 same budget: the candidate's own step count. C3 parameters: rung 1. C4 memory and speed: rung 2. C5 interface: rung 1. C6 no new dependencies, no network, no reading the exam: the import rule only, and it allows the standard library's network modules. C7 the metric: the candidate's own `evaluate`.
Three of seven rules rest on the candidate's good behaviour. → covered by **B**.

**Q: Are the rules shown to every agent in a useful form?** They are shuffled for sketch agents, unshuffled for builders. Fine.

## 2. The map

**Q: Does the same map give the same blind spots every run?** Yes. The planner draws one map per run from one framing ("parts of the recipe"), and the defaults are a module list. Two runs will look in the same places.
**Follow-up: what else could the map follow?** Data flow (what happens to a token from file to loss), learning dynamics (what changes in the first, middle and last third of training), information bottlenecks (where capacity is wasted), failure modes (what the loss curve says). Each lens produces different parts and different assumptions.
→ **Improvement H1. The planner prompt takes a lens; replicates and later runs rotate lenses; the map records which lens drew it.** *Small.*

**Q: Does memory from earlier runs reach the right part?** Ledger entries are injected by part id. The planner invents ids; the default map uses "mix", a planner might say "attention". The injection would miss. The ledger is short.
→ **Improvement H2. Inject the whole ledger into every brief as a "tried before" block, regardless of part.** *Trivial.*

## 3. Research

**Q: What kind of knowledge does research bring?** Only "what has been tried on this part of this kind of model". That is the knowledge that makes ideas safe, not the knowledge that makes them new. Nothing in the run looks outside the field. The seed-word card is the only cross-domain input and a random noun is a weak one.
**Follow-up: what is the strong form?** Structured analogy: for each part, find problems in other fields with the same shape (mixing information across a sequence resembles message passing, filtering, routing in networks; a learning-rate schedule resembles annealing, control, dosing; the residual stream resembles a ledger, a bus, an accumulator), and for each analogue, the mechanism the other field uses and the mapping back. This is the best-documented source of genuinely new ideas in the creativity research behind this project and it is absent.
→ **Improvement I. An analogy research call per part (cheap model with search: "what other fields solve a problem of this shape, and how") and an analogy sketch card that receives the analogues with an explicit mapping and must propose mechanisms carried across.** *Small to medium.*

**Q: Does research ever check its own coverage?** No. Nothing tells whether the brief missed half the record. The modern-architecture digest carries the speedrun list, which covers the main gap. Acceptable for now.

## 4. Sketching

**Q: What does an ideation agent know about how the baseline actually behaves?** Nothing. It sees the script and the rules. It does not see a loss curve, which positions in the sequence are hardest, which tokens, whether late layers contribute, whether attention is sharp or flat, whether gradients are balanced across layers. Every idea is theorised from the text of the program. A human researcher would first look at the measurements and ask where the model is weakest; the run never does.
**Follow-up: what measurements are free?** One instrumented baseline run, once, at profile time: loss by position bucket, loss by token-frequency bucket, per-layer gradient norms and activation scale, attention entropy per layer, the shape of the loss curve (where it bends), tokens per second. A compact table, under a page.
**Follow-up: who should see it?** A new "diagnosis" ideation card ("here is how the model behaves; where is it weakest and why; propose changes that target that"), every interrogation call, and the planner, so the map can follow the evidence.
→ **Improvement J. A diagnostics script run with the profile; its table fed to a diagnosis card, to the interrogations and to the planner.** *Medium.*

**Q: Does anyone check the predictions?** No. Every sketch carries a prediction and a test; both are used only as a selection heuristic (cheap-test words). When a candidate is measured, nobody compares the number with what was predicted. That is the one place the run could learn which agents, cards and kinds of idea are trustworthy, and it could tell the next round "your prediction was X, the measurement was Y".
→ **Improvement K. Prediction tracking: parse numeric predictions about parameters, step time and loss gap where present; compare with the measured values at rungs 1 to 4; record accuracy per card and per idea; feed the comparison into the history that later rounds and interrogations read; show it on the dashboard and the scorecard.** *Medium.*

**Q: Are the ways in sufficiently different?** The plain, stripped, digest, research and seed cards all see the same full problem text, and all come from one model. The differences are real but modest. The analogy card (I) and the diagnosis card (J) add two ways in that differ in kind, not in wording.

## 5. Grouping, tagging and selection

**Q: Where do the selection weights come from?** From judgement, this week. One run's data cannot calibrate them. After a few runs the ledger will say which features (angles, novelty, departure, obvious) predicted survival at each rung.
→ **Improvement L. A calibration script over the ledger: survival rate per feature, reported, and offered as new weights. No automatic change until the owner accepts.** *Small, later.*

**Q: Is the "cheap test" term doing anything?** Every idea goes through the same ladder regardless of its test line, and the term rewards the words "smoke", "60", "memory". It is a leftover from the puzzle harness. Harmless, but it can be gamed by any agent that learns the words. Drop it or keep it at a low weight. *Trivial, noted.*

## 6. Interrogation

**Q: Who asks the questions?** The same model that answers them and the same model that had the idea. Its blind spots survive the questioning. The "how could it fail" question is one of many and is answered by an agent that likes the idea.
**Follow-up: what is the cheap counter?** One adversarial call per interrogated idea whose only job is to make it fail: break a constraint, find the silent cost, name the experiment that would embarrass it. Its output goes to the builder as "watch for" and to the selection as a count of unanswered objections.
→ **Improvement M. A pre-mortem call per interrogated idea, one strong-model call, its objections carried to the builder and shown next to the idea.** *Small.*

**Q: Do the facts reach the verifier?** No. The "builder must know" list and the test line are for the builder. A claim such as "adds 1,536 parameters" or "step time unchanged" is checkable at rungs 1 and 2 and would be checked by K.

**Q: Is depth two, fan-out one the right shape?** It is a chain. The first build-relevant open question is followed; the second never is. With the questions now marked, a fan-out of two at depth one and one at depth two costs five calls instead of three and covers the two most important doubts. A setting, not a change. *Noted.*

## 7. Building

**Q: What happens when a build fails at rung 0 or 1?** The candidate waits a full round for a revision. A boundary violation or a syntax slip is a one-call fix; waiting a round wastes the slot and, in a two-round run, half the chance.
→ **Improvement N. An immediate fix: a rung 0 or rung 1 failure triggers one revision in the same round, with the exact violations or error, before verification continues.** *Small.*

**Q: Can two winners be combined?** Today only by a later idea. But the boundary checker already knows which functions and classes each candidate changed. Two checked candidates with disjoint changed sets can be merged by script, with zero model cost, and the merge put through the ladder. This is the cheapest new candidate the run can make, and it tests the whole-recipe assumption directly.
→ **Improvement O. Mechanical composition of disjoint checked candidates after each round, plus a "combine" card for overlapping pairs.** *Small to medium.*

**Q: Is the same script ever verified twice across runs?** Yes, if two runs build the same change. The ledger stores ids, not source hashes.
→ **Improvement P. Store the source hash with every pool entry and ledger row; at verification, reuse an earlier verdict for an identical script.** *Small.*

## 8. The ladder

Covered by G (calibration and trend). One more: **Q: does rung 2 time the right thing?** Three steps include the first step's warm-up for both baseline and candidate equally, so the ratio is fair, but the absolute numbers are inflated. Report the ratio, not the seconds. *Trivial.*

## 9. The overnight verdict

Covered by B (external exam), D (compute matching), E (promotion). **Q: what does the night do with its idle time?** With few candidates, the card idles after the staged seeds. The baseline token-scaling curve (D) and extra baseline seeds (G) are the right filler, in that order. *Noted for the runner.*

## 10. Running it

**Q: What happens at a crash or a stop two hours in?** Everything on disk is kept; nothing can be resumed. The next run starts from zero and pays again. The sketches, clusters, interrogations and history are all in files.
→ **Improvement Q1. Resume: reload a run folder's state and continue from the next stage.** *Medium.*

**Q: Can the owner steer without stopping?** No. The dashboard is read-only. The owner has stopped runs by hand when they went wrong; a stop loses the spend.
→ **Improvement Q2. A control file in the run folder, read at stage boundaries: pause, skip a part, exclude an idea, a note that every later agent reads.** *Small.*

## 11. What the run says about itself

**Q: What numbers does the run report at the end?** Candidates, checked, tokens, seconds, and a ranked list. Not how many ideas it had, how many were new, how many were obvious, how many were questioned, how many built, where they failed, what it cost per checked candidate, or how its predictions fared. Those are the numbers the owner needs to show anyone. → **F**.

---

## Ranked list

| # | Improvement | Why it matters | Cost |
|---|---|---|---|
| 1 | A: plain-arm control | Without it, nothing can be attributed to the method | small-medium |
| 2 | G: calibrated rungs, trend ranking | The ladder's thresholds are guesses; seed noise is unmeasured | small + 10 min GPU |
| 3 | B: exam integrity (denylist, val scan, checkpoint, external evaluator, wall-clock audit) | The candidate currently runs its own exam | medium |
| 4 | J: diagnostics before ideation | Nobody looks at how the model actually behaves | medium |
| 5 | I: analogy research and card | The only cross-domain input is a random noun | small-medium |
| 6 | E: promote winners into the baseline | Winners never compound | small |
| 7 | F: scorecard and report per run | The run's results exist only in logs | small |
| 8 | N: immediate fix for rung 0–1 failures | A one-call fix waits a round | small |
| 9 | O: mechanical composition of disjoint winners, combine card | The cheapest new candidate the run can make | small-medium |
| 10 | K: prediction tracking | The one place the run could learn whom to trust | medium |
| 11 | Q1/Q2: resume and a control file | A stop loses the spend; no steering | medium |
| 12 | P: cross-run dedup by source hash | Same script verified twice | small |
| 13 | H1/H2: map lenses; ledger into every brief | Same blind spots every run; memory can miss its part | small |
| 14 | M: pre-mortem call | The idea's author answers its own doubts | small |
| 15 | D: asymmetric parameter rule now; compute-matched verdict later | Smaller models are rejected; slower ones are not charged | trivial + medium |
| 16 | L: weight calibration from the ledger | Weights are guesses | small, later |
| 17 | C: regime and scale check | Decisions for the owner | small once decided |

**Status 2026-10-13:** all seventeen built. A (nano/loop.py --arm plain|climb), G (nano/verdict.py, three-seed profile, z-gaps, trend), B (nano/launch.py tripwire and wall cap, train-only data folder, nano/exam.py external exam, denied modules and validation-split scan in nano/boundary.py), J (nano/diagnose.py and the diagnosis card), I (analogy research and card in nano/research.py), E (nano/promote.py, nano/version.py), F (nano/report.py), N (same-round fix), O (nano/compose.py), K (nano/predict.py), Q (control.json and --resume), P (verified_by_hash.json), H (planner lenses, ledger into every brief), M (pre-mortem call), D (asymmetric parameter rule; --scaling-curve in batch_verify), L (nano/calibrate.py), C (owner's decision, not code).

**Two decisions only the owner can make:** whether to move to a smaller model with more tokens (C), and whether the compute-matched verdict (D) is worth four extra baseline runs.
