# Mapper, part 2: QUESTIONS and RANK AND LINK

Scope: parts (3) QUESTIONS and (4) RANK AND LINK of the mapper. SPLIT and FACTS (parts 1 and 2) are in `01_*.md`. MAINTENANCE and PEOPLE (parts 5 and 6) are in `03_*.md`. Here we assume a tree already exists, with facts attached to its parts.

Code today: `nano/tree.py` (node schema, `node_prompt`, `split_select`, off-map cards) and `nano/loop.py` (`ideate_round`, `_write_tree`, `_select_with_lanes`). Items marked "proposed" do not exist yet.

The three modes:

- Mode 1: a baseline artifact and an objective check exist (the language-model loop today).
- Mode 2: a check exists, no baseline. The team writes the first artifacts. The best one so far becomes the reference.
- Mode 3: no objective check. A panel of judges, the critics and people replace the verifier.

## 1. QUESTIONS

### 1.1 Three lines per part

Every part (a node under the root) carries three lines. They extend the current node fields `frame`, `assumptions`, `boundary`.

| Line | Node field | Content |
|---|---|---|
| does | `frame` (exists) | What the part does now, one or two sentences. |
| weak spot | `weak_spot` (proposed) | Where it loses, with the fact id that shows it. One sentence. |
| ask | `ask` (proposed) | One question, written as a problem. |

A weak spot without a fact id is marked `unsupported`. It still goes into the prompt, but its evidence is zero (see 2.1).

```
  part node
  +--------------------------------------------------+
  | does:      what the part does now                |
  | weak spot: where it loses  [fact f12, f14]       |
  | ask:       "How can X reach Y when Z holds?"     |
  +--------------------------------------------------+
        |  ask
        v
  helper questions (max 1 level of them, see 1.4)
        |
        v
  ideas -> tests -> results hang under the question they answered
```

### 1.2 A question is a problem, never a solution

A solution inside the question collapses the inventors onto one answer. The question states what must become true, not how.

Allowed:
- "How can the choice rule waste less room in nearly full bins?"
- "What lets the model use long context without paying for it at every layer?"
- "How can a review process stay fair when reviewers see only some entries?"

Disallowed:
- "Should we use best fit instead of first fit?" (names a mechanism)
- "How do we add a learned gate to attention?" (names a mechanism)
- "Add a second round of reviews to cut noise." (a command, not a question)

Enforcement is a lint on the planner output, run in `parse_planner` after JSON parsing (proposed `lint_ask`):
1. The `ask` must start with How, What, Why, Which, or When, and end with "?".
2. It must not contain a mechanism word from the profile's `levers`, `known_tricks`, or the artifact's own identifiers (function and class names from `boundary`).
3. It must not start with a verb in the imperative (Add, Use, Replace, Try, Switch).
4. It must be at most 30 words.

On failure, one repair call to the cheap model: "Rewrite as a problem; remove the mechanism." If the second attempt fails, the ask is replaced by a template from the weak spot: "How can <part> stop <weak spot>?" and the node is flagged `ask_template`.

### 1.3 Directions

Today a node has `directions` in `["inward", "outward"]`, and the root has `["upward"]`. The text for each lives in the profile's `directions` dict, with the generic fallback `_GENERIC_DIRECTIONS` in `tree.py`.

- Inward: keep the paradigm, treat the assumptions as fixed.
- Outward: remove or invert at least one assumption, and say which.
- Upward (root only): question the framing, propose a new success measure. Logged to `proposals_upward.jsonl`, never built.

A profile adds or renames a direction in two steps. It adds the name to `directions` in a node, and it adds a text under the same name in `PROFILE["directions"]`. A renamed direction keeps its role through a proposed map `direction_roles`: `{"within": "inward", "replace": "outward"}`. The roles drive `split_select` (inward share) and the long-shot lane. A new direction with no role gets its own round-robin pass and a share in the proposed `direction_shares`. In Mode 3, `upward` also covers "is this the right question?" and may be allowed on any part, not only the root.

### 1.4 Helper questions

Under a question the tree may hold helper questions (level four). Types, after Polya:

| Type | Form |
|---|---|
| special case | "What is the answer when only one bin is open?" |
| simpler version | "What is the answer with a fixed item size?" |
| work backwards | "What would a perfect packing look like, and which step first departs from it?" |
| drop one condition | "What changes if items may be moved after placing?" |

Who writes them:
- The mapper writes at most two helpers per question, only for questions where a profile fact says the part is the largest loss (top third by priority). Reason: helpers cost one cheap call each, and low-ranked parts do not earn them.
- The critics write helpers when a built idea fails. A failure mode becomes a helper under the question the idea answered ("why did it fail at late positions?"). This uses the existing three-level questioning of critics.
- Helpers obey the lint of 1.2.

Depth rule: parts (1), sub-parts (2), questions (3), helper questions (4). A fifth level never exists. If a helper needs sub-helpers, it is promoted to the root of a new tree, linked to its origin by a `spawned_from` link.

### 1.5 Phrasing by mode

| Mode | Weak spot cites | Ask is about |
|---|---|---|
| 1 | a measured gap against the baseline | closing that gap under the fixed check |
| 2 | the gap between the current best and a bound or a naive reference | getting the first artifact past the check, then raising the best |
| 3 | a criterion the panel scored low, or a critic's objection | satisfying a named criterion; no number is promised |

In Mode 3 each ask also names the criterion it serves ("for fairness: ..."), because no score exists to carry the meaning.

## 2. RANK AND LINK

### 2.1 Priority

```
priority(part) = unused_capacity(part) * evidence(part)      both in 0..1
```

Unused capacity: how much headroom is left in the part, relative to what has already been spent on it.

```
unused_capacity = headroom / (1 + attempts_on_part)
headroom (Mode 1,2) = share of the total gap to the target that the part's facts attribute to it
headroom (Mode 3)   = mean panel deficit on the criteria the part serves (1 - score/max)
attempts_on_part    = built ideas under the part so far, counting only ones that passed rung 1
```

Evidence: how much of the headroom claim is backed by something the team can check.

| Mode | Evidence = 1.0 | Lower values |
|---|---|---|
| 1 | a measured effect with a source and a noise estimate (z above the check's margin) | 0.5 measured without noise estimate; 0.25 from literature only; 0 unsupported |
| 2 | the same, against the current best | the reference moves, so evidence decays by 0.8 per time the best changes without a fresh measurement |
| 3 | judges agree on a low score (spread small) and at least one critic objection stands | 0.5 judges only; add a people term below; 0.2 one opinion |

Mode 3 people term: `evidence = 0.6 * judge_agreement + 0.4 * vote_signal`. `vote_signal` is the net votes on the weak spot ("this matters"), capped at 10 votes, scaled to 0..1, and each person counts once. A voter with no stake in the part counts fully. Votes can raise evidence to at most 0.8 alone; only a critic or judge can reach 1.0. This follows the rule "people steer, tests decide": in Mode 3 the panel plays the tests.

Priority is stored as `priority` and `priority_why` (both factors) in `problem_tree.json`, next to the existing `stats`.

### 2.2 From priority to contexts and slots

Today every part gets `per_node` contexts per direction in round 1 and 1 in later rounds, flat. Proposed: weighted by priority, with a floor.

```
  priority per part
        |
        v
  normalise to weights w_i  (sum 1; floor 0.5/N so no part gets zero)
        |
        +--> idea contexts:  n_i = round(w_i * C_on)  (at least 1 per direction)
        |        C_on = contexts on the map; C_off added after (share below)
        |
        v
  sketches -> clusters per part/direction
        |
        v
  split_select(k_main, inward_share):
     inward pass  : round robin over parts, order = fewest slots so far,
                    ties by seeded shuffle  (counts carried across rounds)
     outward pass : same
        |
        +--> proposed: counts are divided by w_i, so a heavy part is
        |    visited earlier and more often, but never alone
        v
  main slots  +  long-shot lane (longshot_share)  ->  builders
```

The off-map share is applied after ranking. `ideate_round` computes `n_off = n_on * s / (1 - s)` from the on-map count. Ranking therefore changes how the on-map contexts are dealt, and not how many off-map ones there are. The share `s` itself moves by yield (`_shift_off_share`, +0.1 or -0.05, range 0.2 to 0.6). The off-map pseudo-node `offtree` takes part in the round robin like a part, with a fixed weight equal to `s`, never ranked. A high-priority part cannot starve it.

### 2.3 Links

A link is an edge `{from, to, kind, why, source}`. Kinds:

| Kind | Meaning | Made by |
|---|---|---|
| `shares_fact` | two parts cite the same fact | mapper |
| `interacts` | a change in one alters the other (from a cross-part cluster or a contradiction) | mapper, clusterer merge |
| `spawned_from` | new tree from depth overflow | mapper |
| `win_from` | an off-map win became a branch (`promote_win`) | loop |

Mutual links (A points at B and B at A) change dealing as follows. The pair is a pair-group. The group's weight is the larger of the two weights, not the sum, so a cluster of linked parts does not take extra slots. One of the group's contexts per round is a "joint" context, built on the node `recipe` (the cross-part node that profiles already have), with both parts' frames in the prompt. The rest of the group's slots are split as usual.

A one-way link raises the target's evidence by 0.1 when the source part has a built win, because a win next door is a hint.

### 2.4 Quiet branches

A branch with no new sketch, cluster or test result for two rounds has `quiet = true`. Its weight is multiplied by 0.5, but never below the floor in 2.2, so it still gets one context per direction in the next rounds. Nothing is deleted. Any new fact, vote, critic note, link or off-map win clears `quiet` and restores the weight on the next ranking.

## 3. Configuration

### 3.1 Questions

| Knob | Default | Key or flag | Effect |
|---|---|---|---|
| directions per node | `["inward","outward"]` | `directions` in node schema | which passes a part takes part in |
| direction texts | generic | `PROFILE["directions"]` | wording per direction |
| parts per plan | 6 to 9 | planner prompt text | how many questions exist |
| ask lint | on | `ask_lint` (proposed) | reject mechanism words |
| helpers per question | 2 | `helpers_max` (proposed) | cost vs. depth |
| helper top fraction | 0.33 | `helpers_top` (proposed) | which parts earn helpers |
| max depth | 4 | `max_depth` (proposed) | where a new tree starts |

### 3.2 Rank and link

| Knob | Default | Key or flag | Effect |
|---|---|---|---|
| contexts per part x direction, round 1 | 1 | `--per-node`, `loop.per_node` | breadth of round 1 |
| inward share of slots | 0.6 | `--inward-share`, `loop.inward_share` | inward vs outward build slots |
| off-map share | 0.4, range 0 to 0.6 | `--off-tree-share`, `loop.off_tree_share` | contexts with no map |
| new-idea quota | 0.5 | `new_share` argument of `split_select` | share of slots for ideas new against the brief |
| long-shot share | loop default | `loop.longshot_share` | lane outside ranking |
| priority weights on/off | off | `--rank-weights` (proposed) | flat dealing vs. weighted |
| weight floor | 0.5 / N | `rank_floor` (proposed) | minimum per part |
| quiet rounds | 2 | `quiet_rounds` (proposed) | when a branch is lowered |
| quiet factor | 0.5 | `quiet_factor` (proposed) | how much it is lowered |
| vote cap | 10 | `vote_cap` (proposed, Mode 3) | influence of people |
| people weight | 0.4 | `vote_weight` (proposed, Mode 3) | vote vs. panel in evidence |

## 4. Worked examples

### 4.1 Language model (Mode 1)

Parts: embeddings, attention, MLP, depth/norm, optimizer, data, loss, whole recipe. Facts: loss at late positions is 0.12 nats above early ones; the optimizer gap to a tuned run is unmeasured.

- Attention: headroom 0.35, attempts 0, evidence 1.0 (measured, z 4). Priority 0.35.
- Optimizer: headroom 0.30, evidence 0.25 (literature only). Priority 0.075.
- Ask for attention: "How can late tokens use earlier context at a cost the step budget allows?" (no mention of RoPE, windows, or gates.)

Weights after the floor give attention 3 contexts, optimizer 1. Attention and MLP link `interacts` through a cluster that touched both; one joint context goes to `recipe`. Off-map share stays 0.4.

### 4.2 Bin packing (Mode 1)

Parts: choice rule, bin state, when to open, item statistics, tie-breaking, whole rule. A fact: bins above 0.9 fill account for most of the waste above the lower bound.

- Choice rule: priority high (measured). Ask: "How can the rule waste less room in nearly full bins?"
- Item statistics: no measurement, evidence 0.25. Ask: "What can the rule know about future items from past ones?" stays low until a diagnosis context finds a signal.
- Tie-breaking is quiet after two empty rounds. It gets one context per direction. An off-map "doubt" card later says ties matter at full bins. A `win_from` link raises it again.

### 4.3 Hackathon review process (Mode 3)

Goal: "design a fair review process for a hackathon." No check, no baseline. Parts: reviewer assignment, scoring rubric, handling conflicts of interest, calibration between reviewers, appeals, time per entry.

Panel of three judges scores each part's criteria (fairness, effort, speed). Calibration scores 2 of 5 with judges in agreement (0.9); two people vote it matters; one critic objects. Evidence `0.6 * 0.9 + 0.4 * 0.2 = 0.62`. Headroom 0.6. Priority 0.37, the top. Ask: "How can two reviewers give the same entry the same score?" (not: "use a shared rubric"). Helper by Polya: "What if every reviewer saw only one criterion?" Assignment and calibration link `interacts`: one joint context. The upward pass asks whether "fair" means equal treatment or equal outcome. Proposals go to the people, who may change the criteria.

## 5. Open decisions

1. Should the lint block the plan or only repair it? Blocking is stricter but can stall a run.
2. Weighted dealing changes a tested behaviour (flat `per_node`). Run it as an arm against flat before making it the default.
3. Is `attempts_on_part` counting the right thing? A part with many failed tries may deserve less, or more, attention.
4. Mode 2: how fast should evidence decay when the best artifact changes?
5. Mode 3: the vote cap and the 0.4 people weight are guesses. They need a test with real voters.
6. Should `upward` be allowed on every part in Mode 3, or only at the root?
7. Who sets a link's kind when the clusterer and the mapper disagree?
8. Should the off-map pseudo-node's weight follow the share exactly, or keep its own floor?
