# Multi-layer problem trees: what the literature does, and what it means for HTSA

Written 2026-10-17 from eight web searches and three papers read in full. Status of our code: the map is one
level (root plus a row of parts) and nothing adds a second level. See `docs/MAPPER.md`.

## 1. Why we do not have it

History, not a decision. `nano/tree.py` was written on 2026-10-11 as one planner call plus a default list,
with "recursion into sub-parts" filed under "not yet" in `docs/PROBLEM_TREE.md`. Both real runs (arch-2,
skel-1) produced their results from a one-level map, so nothing forced the issue. The four-level design in
`docs/TEAM_OF_RESEARCHERS.md` was written on 2026-10-17, after both runs.

## 2. What the literature does

### Consulting issue trees (the oldest practice)
- Root question, then branches that are mutually exclusive and collectively exhaustive (MECE).
- Depth 2 to 4 levels. Stop when a leaf is something one person could test in about a week.
- Build the issue tree first; convert only the highest-priority leaves into hypotheses.
- Deeper than 4 levels "adds bookkeeping rather than decision value".
- Sources are practitioner playbooks, not peer-reviewed.

### HTN planning (the formal version)
- Abstract tasks are refined by "methods" into sub-tasks until only primitive actions remain.
- Decomposition is lazy: refine the task you are about to work on, not the whole tree up front.
- More than one method per task is normal; choosing one is a search decision.

### AI Scientist-v2 (Sakana, 2025): the closest automated-research system
- A tree of experiment nodes. A node holds code, plan, error trace, metrics, figures, and a status
  (buggy or non-buggy).
- Four stages: preliminary prototype, hyperparameter tuning, research agenda, ablations. Each stage's root
  is the best node carried forward from the previous stage.
- Expansion is best-first by an LLM judge weighing metrics, training dynamics and plot quality. A buggy
  parent gets a debugging child; a working parent gets a refinement child.
- Numbers: max debug depth 3; node budgets 21, 12, 12, 12 per stage; 1 hour max per node; 15 hours per paper.
- Replication nodes rerun a parent on new seeds; aggregation nodes combine replicates into statistics.
- Caution for us: the judge is an LLM. Our critic calibration says LLM judgement of ideas is near chance.
  There it judges measured results, which is a different thing.

### Adaptive Graph of Thoughts (2025)
- A node is either evaluated directly or, if a check says it is "complex", expanded into a nested sub-graph.
- They used depth 1, at most 3 layers of at most 3 nodes, and found it enough. No ablation on depth.
- The rule "expand only what needs it" is the point.

### MCTS with progressive widening (2025 to 2026)
- The number of children a node may have grows sublinearly with how often it was visited:
  children allowed = c * visits^alpha, alpha between 0 and 1. No branch can eat the budget early.
- Refinements: make widening depend on the node's score, not only its visit count (ExTS); count
  in-flight evaluations as visits when runs are parallel (AutoSR); anneal exploration as the budget runs
  out (BG-MCTS).

### Iris (2026): revisable knowledge after experiments, on MLE-Bench
- Knowledge is a set of claims. Each claim has: text, scope (where it applies), pointers to supporting and
  refuting evidence, and a status: active, qualified (scope narrowed by later evidence), invalidated.
- After every action a summarizer writes attempt, observation, implication. A manager then adds, updates
  or invalidates claims. Nothing is deleted.
- "Epistemic actions" are probes run only when the evidence does not distinguish the next steps, progress
  stalls, or an unexpected result must be traced. They produce evidence without changing the solution.
- Ablation: removing the knowledge layer cost 13.4 points of any-medal rate (66.7 to 53.3 on 15 tasks).

### Google co-scientist (2025 to 2026)
- Hypotheses deduplicated through a proximity graph, ranked by an Elo tournament of debates, evolved by
  simplifying, combining and deliberately diverging.
- A meta-review feeds common criticisms back to generation so later rounds do not repeat them.
- Critics of the system raise homogenization of ideas as the main risk.

## 3. What converges across all of them

1. Start shallow: 2 levels, leaves that are testable.
2. Deepen lazily, only where a rule says the node earned it (visits, score, or a complexity check), with
   children capped by progressive widening.
3. Results attach to the node they tested as claims with scope and status, revised when later evidence
   contradicts them. Nothing is deleted; it is invalidated or lowered.
4. Stages matter: prototype, tune, research agenda, ablations.
5. Dedup and meta-review keep later generations from re-proposing the same things.

## 4. What we already have that they lack

- The off-map share (blank, gaps, doubt cards): a hedge against the tree pulling everyone to the same spots.
- The leap quota and the long-shot lane.
- Controls every run (placebo, known winner, known loser) and an anytime-valid verdict.
None of the systems above has the first two; the co-scientist critics name exactly that gap.

## 5. Recommendation for HTSA

### At the start: two levels
```
root
 |-- part  (frame, assumptions, boundary)                 <- what we have now
 |     |-- question: a measured weak spot, with the number behind it
 |     |-- question: ...                                   <- new: 2 to 4 per part, drawn from the
 |                                                            diagnostics page and the research brief
```
- The sub-mapper writes questions, not sub-parts. Example: "why do late positions lose 0.46 nats",
  "why is the layer-0 attention gradient 15x the rest".
- A question is testable by construction and gives inventors a target instead of a region.
- This also brings root-cause analysis into the map: a question names a symptom and asks for its cause.

### After each round: append and revise, Iris-style
- Every build result becomes a claim under the question it tested: text, scope (this size, this budget),
  evidence pointers (run folder, candidate id), status active.
- A later contradicting result qualifies or invalidates the earlier claim. The ledger already holds the raw
  rows; the missing piece is the claim layer with status and the revision step.
- Failures become child questions ("why did X not help"), not deleted branches.

### Deepen lazily, by rule
- A question may get children only when it has been visited enough and produced something:
  children allowed = floor(c * visits^0.5), and only for questions whose builds passed or whose claims
  conflict. Cap at 4 levels.
- A quiet branch is lowered in priority, never deleted.
- Do not use an LLM judge of sketches to decide what to expand. Use measured yield.

### Probes before builds for unresolved questions
- When a question's claims conflict, run a measurement (a diagnosis, a lesion, a five-minute probe), not
  a build. This is Iris's epistemic action, and our diagnosis card made structural.

### Keep
- Off-map share, leap quota, long-shot lane, controls, pre-registered verdict.

## 6. What this needs in code (not built)

1. Node schema: allow `parent` to be a part id; add `depth` and a node `kind` (part, question, claim).
2. A sub-mapper call scoped to one part: its three fields, its sketches, its brief, its measurements;
   returns 2 to 4 questions. Script enforces boundary inside the parent and depth cap.
3. Claim records with status under questions, written by script from verify records; a revision step
   per round.
4. `split_select` walks the leaves; a subtree's slot count is the sum over its children.
5. `resolve_scope` includes descendants; `replan_tree` keeps subtrees; `promote_win` attaches under the
   owning part.
6. Rendering: indent by depth in `tree_text` and the dashboard; yield per subtree in the report.

## Sources

- AI Scientist-v2: https://arxiv.org/html/2504.08066v1 and https://github.com/sakanaai/ai-scientist-v2
- Iris, Beyond Solution-Centric Search: https://arxiv.org/html/2608.02143v1
- Adaptive Graph of Thoughts: https://arxiv.org/html/2502.05078v1
- Exploit More, Explore Smarter (quality-conditioned widening): https://arxiv.org/pdf/2608.23848
- AutoSR (pending-aware widening): https://arxiv.org/pdf/2608.16876
- Budget-aligned tree search: https://arxiv.org/pdf/2602.09574
- Issue trees and MECE playbook: https://thinkinsights.net/playbooks/problem-structuring-hypothesis-driven-consulting-playbook-issue-trees-mece
- Issue tree definition: https://www.casestar.io/definitions/issue-tree
- HTN planning lecture notes: https://cw.fel.cvut.cz/wiki/_media/courses/pui/13-htn.pdf
- Google co-scientist: https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/
- The Batch on co-scientist: https://www.deeplearning.ai/the-batch/ai-co-scientist-an-agent-that-generates-research-hypotheses-aiding-drug-discovery
