# Idea generation across twelve fields: what transfers to the nano loop

*2026-10-13. Synthesis of briefs 01–12 in this folder (cognitive psychology, analogy, design methods, evolutionary search, scientific discovery, mathematics, collective intelligence, science of science, LLM ideation, biological innovation, decision science, ML research practice). Each brief grades its own evidence; here "strong" means two or more fields with controlled or large-N support, "medium" one field with controlled support, "weak" preprints, single runs or self-reports. "Have / partial / new" is against the loop as built today (nano/loop.py and friends). Source numbers refer to the briefs.*

---

## 1. Where the fields converge

**C1. Ideas from one model are a small set wearing many words.** Four thousand research ideas held about 200 unique ones; 119 of 128 speedrun ideas collapsed onto two after reward training; larger models are less diverse than smaller ones; temperature, nucleus and "be creative" barely move it (01, 04, 07, 09, 10). What does move it: serial regeneration with earlier outputs visible, staged chain-of-thought (list many terse seeds, make each bolder and different, then elaborate), disjoint inputs per agent, and rejection of near-duplicates before anything is spent on them. **Strong.**

**C2. Nobody can rank ideas from their text.** The best LLM judge agreed with human reviewers 53% of the time against 56% between humans; LLM-judged novelty correlates negatively with later impact; ideation scores predict execution scores at r between −0.15 and 0.21; after 100 hours of execution the LLM ideas lost their novelty edge entirely (05, 07, 08, 09, 11). Only judges calibrated on experiment outcomes do better, and only after thousands of outcome pairs; a focused outcome memory lifted a training-code loop from 7.1% to 10.7% gain. **Strong.**

**C3. The verifier is the system, and everything that can game it will.** Verifier exploits in AlphaEvolve's maths study, a kernel "speedup" of 3.13x that fell to 1.49x after decontamination, a silent no-op accepted as a speedrun record, agents hard-coding answers, agents hiding the hard part in a placeholder, dev-set selection costing 9–13 points on test, rankings that invert between 1 and 40 seeds (04, 06, 09, 12). **Strong.** The remedies that recur: hidden evaluation, replication on fresh seeds before promotion, placebo and positive-control candidates run through the exact ladder, neutralised patches that must reproduce the baseline, logging the effective value of every knob a build claims to change.

**C4. Simple baselines compete with clever search.** Flat best-of-N matched iterated search on speedrun tasks; greedy matched tree search over 324 runs; sequentially-conditioned sampling matched or beat code evolution on most benchmarks; better operators beat better search policy (04, 05, 09, 10). What evolution does add, when it adds anything, is parent diversity and shared outcome lineage: archives beat greedy in every system that reported it, and a specialist loop with shared lineage found 16 valid improvements against 3 without it. **Medium to strong.** Any machinery we add must be gated against the plain and climb arms at matched cost, which the loop can now do.

**C5. Real improvements to training recipes are mostly ports, repairs and recombinations found by measuring a pathology.** The median speedrun record saves 1.1% of wall time; at least 11 of 92 are explicit ports; QK-norm, gating, MLA and mHC each started from a measured pathology; agents told to be novel "cannot improve the baseline"; every documented agent gain came from composing known techniques (05, 09, 12). **Strong.** Novelty is a property to measure and protect in a lane, not a quota to enforce on the main line.

**C6. Independent generation, then pooling.** Nominal groups beat interacting groups in meta-analysis; early exposure to others' ideas narrows categories; debate does not beat voting; personas give no accuracy gain; mixing model families raises diversity but can lower mean quality (01, 07, 09). **Strong.** Our isolated contexts are right. Exposure, when it comes, should be to measured outcomes, late, and ideally on request.

**C7. Analogy transfers structure only when it is assigned and mapped explicitly.** Unaided people notice far analogies 30% of the time; comparing two analogues and writing the shared schema doubles transfer; far sources raise variance, not the mean; strong LLMs gain from remote sources only at the far end; LLM judges of structural mapping disagree with humans (02, 05). **Medium to strong.**

**C8. Returns are fat-tailed and selection is a "find the best" problem.** The top 2% of ideas gave 75% of the gains at Bing; testing 20% more ideas raised productivity 17%; novel work has lower mean, higher variance and delayed credit; the right tools are successive halving, top-two sampling and index ordering, not optimism bandits; ladders only help when rung rank predicts final rank, and fixed-gap gates fail when curves cross (08, 11, 12). **Medium to strong.**

**C9. Method prompts do not beat plain ones.** No design method has strong evidence; a short "wild, outside the usual categories" prompt matched or beat TRIZ, C-K and SCAMPER prompts; creativity training halves after bias correction; incubation is a modest effect; the serial-order effect explains 3.5% of variance (01, 03). **Medium.** Structure should go into inputs and verification, not into instruction wording.

---

## 2. Where the evidence contradicts our design

**X1. The 50% novelty quota and the "known gets no bonus" rule.** C5 says the main line of gains runs through adapted known techniques and recombination, and that novelty-forced generation produced nothing. Our selection reserves half the slots for "new" and gives known ideas no bonus. The evidence supports the opposite allocation: slots by expected yield learned from the ledger, with novelty protected in a 15–20% long-shot lane whose yield is tracked separately (08, 11, 12).

**X2. The 0.005-nat margin.** At the speedrun's measured slope, 0.005 nats is about 3–4% of training steps, against a median record of 1.1%. Most real small wins would be rejected outright and never composed. The fix is a second tier, "stackable": a smaller gain with p < 0.05 and the same sign on every rung, which feeds composition and promotion-by-accumulation but never counts as a win on its own (12).

**X3. The staged seeds in the overnight verdict are optional stopping.** Deciding whether to run seeds 1–2 and then 3–4 from the results so far inflates the false-verified rate; naive monitoring raises Type I error up to fivefold (11). The fix is either a pre-registered fixed design (every stage-2 entrant gets exactly 3 seeds, close calls get a separate, pre-declared confirmation) or an anytime-valid sequential e-test on paired seed differences.

**X4. Hand-set selection weights.** Angles, novelty, departure and cheap-test weights are guesses; "angles" may track obviousness since same-model agreement reflects shared priors (07). The evidence says calibrate on outcomes and otherwise keep selection to coverage plus a random component.

**X5. Showing lineage to generators.** SYNTHESIS.md keeps lineage out of generator prompts to avoid anchoring; the training-code evidence credits shared outcome lineage for most of the gains (09). The reconciliation both briefs suggest: outcomes only, never untested sketches; late rounds only; on request rather than pushed. That is close to what history_text does; it should be made an A/B rather than a rule.

**X6. Rationales in judging.** We bar stated reasons from ranking; one study loses 13 points of judge accuracy when the rationale is removed (09). Same answer: test, do not assume. Our judge-free design makes this moot until a judge is added.

**X7. Analogy card.** We ask for a one-line mapping; the evidence supports a typed mapping table checked by script, two analogues per context with the shared schema written first, assigned sources in distance bands, and ranking by executed outcome only (02).

---

## 3. Mechanisms, ranked

Grade = evidence strength across fields. Status: have / partial / new. Cost: small (hours), medium (a day), large. Rec: apply (build now), arm (build as an A/B against the plain and climb arms), later (needs data the ledger does not have yet), avoid.

| # | Mechanism | Briefs | Grade | Status | Cost | Rec |
|---|---|---|---|---|---|---|
| 1 | **Pre-registered verdict design**: fixed 3 seeds per stage-2 entrant, separate pre-declared confirmation for close calls, or an anytime-valid e-test on paired differences | 11, 06 | strong | partial | small | apply |
| 2 | **A/A audit and positive controls**: placebo candidates (no-op refactor, reseeded stream) and known winners (QK-norm, ReLU², untied head, value embeddings) through the exact ladder every run; report false-positive rate and recall | 06, 12, 04, 11 | strong | new | small | apply |
| 3 | **Intervention checks**: log the effective value of every knob a build claims to change; a neutralised patch must reproduce the baseline; a fidelity probe at rung 3 (did the named measurement move?) | 12, 06 | strong | new | medium | apply |
| 4 | **Stackable tier and composition-by-accumulation**: gain > 0.002, p < 0.05, same sign on rungs 3–5 → eligible for compose.py and for promotion only in combination; leave-one-out pruning after each composition | 12, 08 | strong | new | small | apply |
| 5 | **Novelty gate before GPU**: reject sketches and diffs near-identical to anything built (normalised-diff hash exists; add a lexical-vector similarity on mechanism text), audit 10% of rejects | 04, 09, 10 | strong | partial | small | apply |
| 6 | **Discovery curve and proposal-map audit**: new clusters per 10 contexts with a stop rule; per-card unique-cluster yield; retire cards that keep landing in the same clusters | 01, 07, 10 | medium | new | small | apply |
| 7 | **Staged sketching**: terse seeds → bolder and different → elaborate survivors, inside one call; serial regeneration with the agent's own earlier sketches visible | 09, 01 | medium | new | small | arm |
| 8 | **Outside-the-categories exclusion list**: round-2 contexts get the cluster names already covered, with a "different from these" instruction, outcomes only | 03, 01, 09 | medium | partial | small | arm |
| 9 | **Long-shot lane instead of a novelty quota**: 15–20% of build slots to step-outside and analogy clusters, lenient first gate, own yield ledger, logged propensities; main slots by learned yield | 11, 08, 12 | strong | partial | small | apply |
| 10 | **Outcome memory for selection**: pairwise "A vs B from the same baseline" with one-line past attempts within similarity; calibrate.py weights replace hand-set ones once ~100 builds exist; keep a random component | 09, 07, 11 | strong | partial | medium | later (needs ~100 builds) |
| 11 | **Port-and-adapt card**: three known techniques with their adaptation moves (zero-init, last-k layers, fewer channels, sharing, gate read-out); return an adapted variant | 12, 05 | strong | partial | small | apply |
| 12 | **Diagnostic panel extension and sketch targeting**: add max attention logit, first-token mass, recall-token loss, update-norm spread; every sketch names the cell it moves and by how much | 12, 06 | medium | partial | medium | apply |
| 13 | **Identity-at-init wrapper with gate read-out**: new paths as x + tanh(a)·f(x), a = 0; log a per layer; free attribution | 12 | medium | new | small | arm |
| 14 | **Tuned-baseline duel** for optimiser, schedule and init ideas: equal tuning of weight decay and LR for both sides before the verdict | 12, 11 | strong | new | medium | apply |
| 15 | **Analogy upgrade**: typed mapping table with a script lint, two analogues per context with the shared schema first, assigned distance bands, ranked by executed outcome only | 02 | medium | partial | medium | arm |
| 16 | **Calibrated rung gates and hedge lane**: thresholds from measured rung→overnight rank correlation; 10–15% of overnight slots skip rungs; Pandora-index ordering of the night | 11, 04 | medium | partial | medium | later (needs ~30 overnight pairs) |
| 17 | **Scale-transfer check** for winners: 2× tokens and one width up and down; compute-multiplier k must stay ≥ 1 | 12, 06, 04 | strong | partial (--scaling-curve) | small | apply |
| 18 | **Metric-validity tags**: ideas whose benefit lies outside validation loss at this window (long context, routing, inference) need a secondary probe | 12 | medium | new | small | apply |
| 19 | **Parent sampling by lineage**: revise and recurse parents chosen by descendants' outcomes and few children, not only by rung reached; keep an archive of distinct non-winners | 04, 10, 09 | medium | partial | medium | arm |
| 20 | **Program-space search on a short function** (LR/WD schedule, per-layer multipliers, token-frequency loss weights) with continuous z fitness and a random-search arm | 06, 04, 12 | medium | new | medium | arm |
| 21 | **Variant curriculum** for shortlisted ideas: specialise, generalise, relax, strengthen, lemma; boundary filter, rung 3 screen | 06 | weak | new | medium | later |
| 22 | **Environment-shift round on stall**: change tokens, data mix or width; re-rank the archive there; re-verify in the original | 10, 04 | weak | new | medium | later |
| 23 | **Atypicality score** from technique tags against a reference corpus; "conventional core plus one atypical link" template | 08 | medium | new | medium | later |
| 24 | **Cross-family sketch arm**: a quarter of contexts to Sonnet, allocated by new-cluster yield; no personas | 07, 09 | medium | new | small | arm |
| 25 | **Map re-planning between rounds**: retire falsified assumptions, split or merge parts from the ledger and objections | 03 | weak | partial | small | arm |
| 26 | **Measured-contradiction cards**: mine gain-versus-cost trade-offs from the ledger and diagnostics; ask for sketches that separate them by phase, layer or condition | 03 | weak | new | small | arm |
| 27 | **Three independent pre-mortems with different evidence packs**, union of objections | 07 | medium | partial | small | arm |

**Avoid, on the evidence:** any LLM rating of novelty or quality as a score (C2); personas, debate and temperature tricks (C1, C6); method-faithful TRIZ, C-K or SCAMPER prompts (C9); "farther is better" analogies (C7); trusting small-scale parity for attention-pattern ideas without a scale check (12); optional stopping (X3); a deep ladder with uncalibrated gates (C8); novelty-forced generation on the main line (C5).

---

## 4. What to apply now

In order, each a day or less, all testable against the plain and climb arms with the report's comparison table:

1. **Fix the statistics** (1, 2, 3): a pre-registered verdict design, placebo and positive-control candidates through the ladder every run, knob logging and a neutralised-patch control. This is cheap and it is what turns a "verified" into something a stranger can believe.
2. **Change what a win is** (4, 17, 18): the stackable tier feeding composition and promotion-by-accumulation, the scale-transfer check for winners, metric-validity tags.
3. **Change how slots are allocated** (9, 5, 6): a long-shot lane in place of the novelty quota, the novelty gate before GPU, the discovery curve and per-card yield audit.
4. **Aim the generators at what works** (11, 12, 14): the port-and-adapt card, the extended diagnostic panel with named targets per sketch, the tuned-baseline duel for optimiser ideas.
5. **Run as arms, not defaults** (7, 8, 13, 15, 19, 24, 27): staged sketching, the exclusion list, the identity-at-init wrapper, the analogy upgrade, lineage-based parent sampling, a cross-family sketch arm, independent pre-mortems.
6. **After the ledger has data** (10, 16, 20–23, 25, 26): outcome-calibrated selection, calibrated rung gates and the hedge lane, program-space search, variant curricula, environment shifts, atypicality scoring, map re-planning, contradiction cards.

Two things the synthesis cannot settle and only runs can: whether shared outcome lineage helps or anchors in this loop (X5), and whether the second interrogation generation pays for itself against building more candidates (C4, C8). Both are one flag away from being an experiment.
