# The five team gaps: what the research says (2026-10-17)

Sources: 01_dialogue.md, 02_persistent_expertise.md, 03_generality.md, 04_problem_finding.md, 05_evidence.md.
Most rows in those files were checked against arXiv abstracts, not full papers; numbers marked "memory" there
are leads, not facts. Nothing below contradicts what HTSA has built; each gap has a fix the research supports,
with conditions.

## 1. No real dialogue

- Free-form multi-agent debate gives small, unreliable gains; it often does not beat self-consistency and tends to
  collapse to the majority or the more confident agent. Self-correction without outside feedback can make reasoning
  worse.
- Debate helps when the judge has a checkable anchor (Khan et al.: a weak judge went from 48% to 76%).
- Refine loops gain mostly in the first revision, then fade.
- Fix: one anchored reply round. The author may only concede, rebut with a quoted fact, or propose a measurement.
  Every standing objection becomes a test. Cap at two exchanges, stop when nothing changes. The critic stays a
  checklist, never a gate (it is calibrated: finds planted flaws 4 of 5 times, objects to good ideas as hard).
  Run a no-dialogue arm and keep the round only if the objective test favours it.

## 2. No persistent expertise

- Memory helps modestly; the large gains (ExpeL 40 to 59% on ALFWorld, Voyager 15x faster milestones) come from
  repeated task types or storable code, not open research.
- Quality beats volume: adding every record lost to a fixed memory on four agents; gating plus deletion gave about
  10 points over naive growth. Agents copy retrieved errors. Whole-file rewrites lose detail ("context collapse").
- Memory narrows exploration (documented), and LLM ideation is already low-diversity (about 5% unique ideas).
- Fix: one memory file per part with five sections (sourced, dated facts; tried and why it failed; calibrated
  priors; condition-to-action cues; open questions). Structured markdown, read whole, capped at a few thousand
  tokens. The agent proposes a delta; a curator checks it against run artefacts and appends; no rewrites.
  Anti-fixation: a "failed framings" section, one ignores-memory proposal per round, memory phrased as evidence not
  rules, a no-memory control arm.

## 3. One problem type

- Every system that transfers shares one interface: a runnable scorer plus a small editable artifact (AlphaEvolve:
  50+ problems, matched the best known on about 75%, beat it on about 20%; Eureka: 29 environments, 83% above
  human rewards). Without a scorer, results drop; template-free research agents score low (AI Scientist v2: 1 of 3).
- No paper compares a model's first decomposition with a hand-written one: "the mapper generalises" is untested
  everywhere, not only here.
- Minimum problem definition: goal with direction, editable artifact with boundaries, scorer with smoke stage,
  timeout and tolerance, validity check separate from the score, budget and baseline. HTSA's profile has these.
- Fix: the first real non-LLM run, bin packing, three arms at equal scorer calls: profile only, full method,
  best-of-N without a mapper. Check that the mapper's tree differs from the default, that the full method beats
  best-of-N, that the verifier rejects planted wrong solutions, that no prompt still names the LLM problem, and
  the spend per accepted improvement.

## 4. Problem finding is weak

- People who spend longer finding the problem produce more original work (Getzels and Csikszentmihalyi). Hamming
  and Alon: feasibility and a reasonable attack matter as much as importance.
- Automatic goal generators (POET, OMNI, OMNI-EPIC) filter for learnable and interesting; learnable alone gives
  trivial tasks. Learning progress works as a task-selection signal in curricula; untested for research questions.
- LLM ideas are rated more novel than human ideas (5.64 vs 4.84, Si et al., 79 reviewers) but only about 5% are
  unique, and the best LLM judge of ideas is near chance (53%). No source lets a system safely choose its own
  top-level goal.
- Fix: pick the next question by P(resolve) x gain x novelty / cost, with P(resolve) from past yield, gain from
  tree priority and what the answer unblocks, novelty as dissimilarity to questions already asked, plus a
  learning-progress bonus per branch. Reserve about one round in five for upward proposals or high-novelty
  questions. Show the top three, person may veto, proceed by default. Guardrails: every question enters with a
  test, a threshold and a failure condition; budget cap per question; each pick traces to the given goal; a person
  approves any change to the success measure; a hold-out the chooser never sees.

## 5. Evidence base is small

- No fixed seed count is required; the standard is to report uncertainty (interval estimates, IQM). Strong
  baselines erase gains (Dacrema: 6 of 7 reproducible neural recommenders lost to simple heuristics). The task set
  can change which method wins ("benchmark lottery").
- Accepted systems had checkable results (AlphaEvolve, FunSearch), blinded human panels (Si et al.), or many tasks
  (MLE-bench, 75).
- What HTSA's evidence supports: a diversity win on NoveltyBench, a single-seed architecture positive, a tie on
  ARC. Not supported: general superiority over a strong baseline, better answer quality, a robust architecture gain.
- Cheapest credibility steps, no GPU: (1) state the claim honestly with a published seed spread next to the 7%;
  (2) per-prompt NoveltyBench distribution with a paired bootstrap interval, from existing logs; (3) rescore
  utility on a 20-prompt sample with an independent judge or a blinded human panel, since Opus judged it;
  (4) pre-register a prediction before the next run; (5) a second problem with a code scorer (bin packing);
  (6) tune the plain baseline as hard as the method; (7) release run logs.

## Order of work

1. Bin packing real run, three arms (gaps 3 and 5 at once).
2. NoveltyBench: bootstrap intervals from logs; independent re-judging of 20 prompts.
3. Per-part memory with a curator and the anti-fixation guards.
4. Anchored reply round in deepen.py, with a no-dialogue arm.
5. Next-question scoring with the human veto.
