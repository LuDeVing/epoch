# HTSA walkthrough: one problem, start to finish

This follows a single run of the scaffold on a small ARC-style puzzle, showing what each
step writes to disk, who sees what, and how the answer is decided. Then a second, shorter
example shows the same loop pointed at "develop a better LLM algorithm" the way stage 4
of the plan does it. Numbers are illustrative but realistic for the Sonnet CLI backend.

Legend for the drawings:

    [box]   a model call (fresh context, sees only the arrows going into it)
    (file)  a file in the run folder   runs/<run-id>/...
    ===>    information that may flow      --x-->  information that must never flow

---

## Part 1. The puzzle

The item (what the harness holds; the key is the test output):

    train pair 1          train pair 2          test
    in        out         in        out         in        out (KEY, scorer only)
    1 0 0     0 0 1       2 2 0     0 2 2       4 0 0     0 0 4
    0 1 0 --> 0 1 0       0 0 0 --> 0 0 0       4 0 0 --> 0 0 4
    0 0 1     1 0 0       3 0 0     0 0 3       0 5 0     0 5 0

The rule is "mirror left-right". The system is never told that. Before anything runs, the
harness strips the key:

    item ----strip_key()----> item without test_output ----> every prompt and file below
      |
      +---- test_output ----> score.py only, after answer.json exists

---

## Part 2. The whole run in one picture

    +---------------------------------------------------------------------------+
    |  harness/think.py (python; no model inside)                               |
    |  budget B = 20 x plain-CoT tokens = 20 x 2,400 = 48,000 tokens            |
    +---------------------------------------------------------------------------+
         |            |             |              |              |
         v            v             v              v              v
     [encode x2]  [defaults]    [probe x3]   [generators x5]   [judge]
         |            |             |              |              |
         v            v             v              v              v
    (problem.md) (private/      agreement     (cands/*.jsonl)  (judgments.jsonl)
    (constraints   defaults.json)  per answer                       |
     .json)       never routed                                      v
                                                          verify top 3 with arc_exec
                                                                    |
                                                                    v
                                                            (verify.jsonl) --> stop?
                                                                    |
                                                  yes: (answer.json)   no: round 2 / reset

Token budget bar for this run (filled as calls return):

    0        10k       20k       30k       40k       48k (cap)
    |=========|=========|=========|=========|=========|
    [enc 4.1k][probe 6.9k][gen 15.2k][judge 2.6k][verify 0]  = 28.8k used, stop at round 1

---

## Part 3. Step by step

### Step 1: encode (two calls plus a script merge)

Call A and call B are identical prompts in fresh contexts. Each writes goal, facts and a
checklist. A script merges the checklists (union, order kept). They agreed closely, so the
third "resolve" call is skipped.

    [encode A] --+
                 +--> merge (script) --> (problem.md), (constraints.json)
    [encode B] --+

problem.md (abridged):

    GOAL: find the rule that maps each input grid to its output grid and apply it to the test input.
    FACTS:
      1. Grids are 3x3 in every example.
      2. Pair 1 input has a diagonal of 1s from top-left to bottom-right.
      3. Pair 1 output has the diagonal from top-right to bottom-left.
      4. Pair 2 input has 2 2 0 on the top row; output has 0 2 2.
      5. Pair 2 input has a 3 at bottom-left; output has it at bottom-right.
      6. Colours never change between input and output.
    CHECKLIST (hard constraints):
      C1. The rule reproduces both training outputs exactly.
      C2. The rule keeps grid size.
      C3. The rule does not change colours.
    BAR: required verification = demo_match on every train pair.

Encode cost: 4,100 tokens, charged to the run and to every arm that reuses this encoding.

### Step 2: the obvious answers go in a locked drawer

A separate fresh call lists the first five answers that come to mind:

    [defaults] --> (private/defaults.json):
        1. flip the grid left-right
        2. rotate 90 degrees
        3. transpose
        4. shift everything one column right
        5. swap the first and last columns

This file is never copied into any sandbox and never appears in a prompt:

    (private/defaults.json) --x--> any generator   --x--> the judge   --x--> the verifier

Why keep it then? Two reasons. A script marks which words in the problem text also appear
in the defaults, so views can be de-cued. And at the end the harness reports whether the
winning answer was an obvious one. Here it was: "flip" is default 1. That's fine; the point
is that generators were not steered toward it.

### Step 3: build the checker

For ARC the checker is the two train pairs plus the executor:

    (verifier) = sha256(train pairs) = 3f9c...; type = demo_match
    arc_exec.py runs a candidate program in a subprocess:
        python -I runner.py   (10 s timeout, output capped, no network)
        transform(pair1.in) == pair1.out ?   transform(pair2.in) == pair2.out ?

### Step 4: probe (three independent plain calls)

    [probe 1] --> program: flip left-right   --> predicted test grid G_flip
    [probe 2] --> program: flip left-right   --> G_flip
    [probe 3] --> program: transpose         --> G_transpose

    clusters: { G_flip: 2, G_transpose: 1 }     agreement(G_flip) = 2/3 = 0.67

Cost: 3 x 2,300 = 6,900 tokens. Nothing is decided yet; this only calibrates confidence later.

### Step 5: generate (five cards, five fresh contexts, in parallel)

Each call gets the goal, the facts in some order, the constraints, and the card's own input.
No call sees another call, the defaults, or any score.

    card         extra input                         what came back (ARC: a program)
    ---------    --------------------------------    ------------------------------------------
    seeded       "Starting point: river"             1. flip left-right    2. flip top-bottom
    low_prior    facts with nouns blanked:           1. transpose
                 "X1 moves from side A to side B"
    transform    operator = negate, applied to       1. reverse each row   2. swap columns 1 and 3
                 "the rule is geometric" -> solver
                 works on "the rule is NOT geometric"
                 -> gets: "recolour by position";
                 revise step pulls it back to C1-C3
    formal       "write 1-3 python programs           1. rotate 90   2. flip left-right
                 transform(grid) -> grid"
    memory_blind a random card (this time: seeded     1. flip left-right
                 again with "lantern")

The seeded card with "river" gave flip left-right. Did the word do anything? Probably not.
That's expected: seeded is the undirected control; its job is to be the thing the directed
cards must beat on average. The ledger will tell us over many runs.

Each generator writes its candidates to (cands/<call>.jsonl):

    {"id": "c_a1", "text": "def transform(g): return [r[::-1] for r in g]", "card": "seeded",
     "operator": "none", "seed": "river", "perm": 3, "round": 1, "origin": "spoken",
     "parent_ids": [], "lineage_id": "c_a1", "program": "...", "pred": null}

Cost: 5 calls, 15,200 tokens.

### Step 6: dedup

Candidates are executed on the test input to get their predicted grid, then collapsed by
predicted grid:

    before: 9 candidates          after: 5 clusters
      flip LR  x4  --> cluster K1 (representative c_a1)
      flip TB  x1  --> K2
      transpose x1 --> K3
      rotate 90 x1 --> K4
      swap cols x1 --> K5   (same grid as flip LR on 3x3? no: identical here -> merged into K1)

    dup_rate = 4/9 = 0.44  (logged; above 0.5 would count toward stagnation)

(clusters.jsonl) gets one row per cluster with the member ids; this is what the graph reads.

### Step 7: judge (one blind call)

The judge sees problem.md and the five representatives, stripped to id and text, in two
shuffled orders. It never sees cards, seeds, positions or anyone's reasoning.

    (judgments.jsonl)
    id     p_raw  spread
    c_a1   0.80   0.05      flip LR
    c_b1   0.40   0.10      transpose
    c_d1   0.30   0.00      rotate 90
    c_a2   0.25   0.15      flip TB
    c_c2   0.35   0.05      recolour by position

Important: p_raw is logged and used for nothing at P0. The confidence that orders
verification is the probe agreement from step 4:

    conf(c_a1) = agreement(G_flip) = 0.67    conf(c_b1) = 0.33    everyone else = 0.0

Cost: 2,600 tokens.

### Step 8: verify the top three by confidence

    queue by conf: c_a1 (0.67), c_b1 (0.33), c_d1 (0.00, tie broken by p_raw)

    c_a1 flip LR     : pair1 ok, pair2 ok  --> matched 2/2 --> status verified, vtype demo_match
    c_b1 transpose   : pair1 ok, pair2 FAIL --> 1/2 --> fail, feedback record written
    c_d1 rotate 90   : pair1 FAIL, pair2 FAIL --> 0/2 --> fail

    (verify.jsonl) row for c_b1:
    {"id": "c_b1", "status": "fail", "verification_type": "demo_match", "partial_score": 0.5,
     "feedback_record": {"failing_pairs": [{"pair_index": 1, "first_mismatches":
        [[0,1,2,0],[0,2,2,0],[2,0,0,2],[2,2,0,3]]}], "passed": 1}}

Verification cost 0 model tokens: the program ran locally.

Surprise check: did anything with high confidence fail? No. (If c_a1 had failed with
conf 0.67 < hi 0.8, still no surprise row. A surprise is logged only above 0.8.)

### Step 9: stop rule

    best = c_a1, status verified
    P(correct | verified, agreement 0.67) = 0.67 under the P0 identity map
    T = 0.67  -->  0.67 >= 0.67  -->  STOP, return answer

If agreement had been 1/3, the run would continue: round 2 with the revise card fixing
c_b1 from its feedback record, plus a fresh seeded call, until a verified candidate reached
T, the round cap (3) or the budget (48k).

### Step 10: answer and records

    (answer.json)
    {"status": "solved", "answer": [[0,0,4],[0,0,4],[0,5,0]], "verification_type": "demo_match",
     "cand_id": "c_a1", "spent_tokens": 28800, "rounds": 1}

    (state.json) decision log, one row per cycle:
    cycle 1: {"round": 1, "step": "verify", "action": "stop", "signal": "verified+agreement>=T",
              "spent": 28800, "pop": ["c_a1","c_b1","c_d1","c_a2","c_c2"]}

    memory/ledger.jsonl gets 5 generator rows + 3 verification rows, e.g.
    {"run_id": "...", "card": "seeded", "operator": "none", "round_type": "first", "seed": "river",
     "tokens": {"total_tokens": 3040}, "agreement": 0.67, "verification_type": "demo_match",
     "status": "verified", "cand_id": "c_a1", ...}

Then, outside the run, score.py reads the key: answer == test_output --> correct.

### The idea graph for this run (graph.py --render draws this as a page)

    round 1
    -------
    seeded ---- c_a1 flip LR  [VERIFIED] ====== same cluster ====== c_e1 flip LR (memory_blind)
                                        ====== same cluster ====== c_d2 flip LR (formal)
    seeded ---- c_a2 flip TB  [unverified]
    low_prior - c_b1 transpose [FAIL 1/2]
    transform - c_c2 recolour  [unverified]
    formal ---- c_d1 rotate 90 [FAIL 0/2]

    cluster K1: 3 members, 3 independent roots (seeded, memory_blind, formal), 2 non-seeded

Three independent lineages landed on the same answer. That "independent roots" count is what
the I3 idea turns into a calibration feature later, once there's data to validate it.

---

## Part 4. Who saw what (the invariants, drawn)

    item with key ---strip---> item ---+--> [encode A/B] --> problem.md --+--> [generators]
                                        |                                 +--> [judge]
                                        +--> [defaults] --> private/ --x--> nobody else
                                        +--> [probe]
    generators' outputs ---> cands ---> [judge] (ids and text only)
                                   ---> verify (programs run locally)
    other candidates  --x--> any generator          (except: revise gets ONE parent + feedback)
    scores, p_raw     --x--> any generator, --x--> the stop rule
    key               --x--> anything except score.py

Every arrow with an x is tested in harness/tests: the end-to-end test greps every prompt
file for the key and for the defaults text.

---

## Part 5. Same item, the other arms (what the comparison looks like)

The harness runs the same item through the nulls at the same budget:

    arm              calls   tokens   answer           correct?
    plain CoT        1       2,400    flip LR          yes
    best-of-N vote   12      28,800   flip LR (9/12)   yes
    best-of-N +verify 12     28,800   first verified   yes
    scaffold         11      28,800   flip LR verified yes

This item is too easy to separate the arms; everything solves it. The experiment lives in
the items where plain fails: the comparison across 40 to 150 items is "solve rate at matched
tokens, scaffold minus the stronger best-of-N, with a bootstrap interval". If that interval
includes zero, the scaffold's structure is not earning its cost, and the per-card ablations
say which part to cut.

---

## Part 6. The hard version: "develop a better LLM algorithm"

Typed as a prompt, that goal has no checker, so the P0 loop abstains, correctly. Stage 4
turns it into something the same loop can verify: a nano-scale model training run.

### Encode becomes an experiment spec

    GOAL: lower validation loss of the nano baseline at a fixed budget.
    FIXED: 20M params, 100M tokens of FineWeb-Edu, context 1024, 3 seeds, same hardware.
    CHECKLIST:
      C1. parameter count within 10 percent of baseline
      C2. same token budget
      C3. mean val loss over 3 seeds beats baseline mean by > 2 seed SD
    BAR: required verification = execution (the training run), C3.
    DEFAULTS (private): bigger batch; more layers; longer warmup; swap AdamW for Muon;
                        add sliding-window attention.

A candidate is now a code diff against train.py, not a grid program.

### The loop, redrawn for this case

    [generators x5: diffs] --> dedup by diff hash --> [judge ranks diffs blind]
            |
            v
    verify = apply diff, train 3 seeds (10 min each on the RTX 4050), compare:

        candidate                               seed1   seed2   seed3   mean    vs base   result
        baseline                                3.412   3.418   3.409   3.413   --        --
        D1 data-difficulty LR schedule (seeded) 3.431   3.440   3.425   3.432   +0.019    fail
        D2 mix residual streams (low_prior)     crash   crash   crash   --      --        fail
        D3 encoder-decoder split (transform)    3.401   3.409   3.399   3.403   -0.010    fail (< 2 SD = 0.012)
        -> no verified candidate; D3 is a near miss; feedback = loss curves + the SD gap

    round 2: revise(D3, operator=specialize) -> "split only the top half of layers"
             lemma card (if on): tries to prove "the gap appears after 60% of training"
             on the three D3 runs' curves; a proved lemma becomes a fact for later cards
             decompose card (if on): parts = attention / optimizer / data order,
             2 attempts each, combinations assembled by script, accepted only if the
             WHOLE model trains better

        D3b specialize                          3.395   3.398   3.391   3.395   -0.018    VERIFIED

    stop: verified diff with a lineage transform -> revise(specialize)

### What comes out

    (answer.json): the diff, the three-seed table, the lineage, the tokens spent
    memory/experiments/ledger.jsonl: every diff tried, hypothesis, seeds, verdict
    strategy stats after 20 such runs: transform and revise produce the wins on this
    family; schedule ideas never pass -> the allocator shifts budget accordingly

Then one scale step up on rented hardware before anyone calls it a finding. That step is
the difference between "a trick that works at 20M params" and a result.

### What the loop will not do

It will not invent a new architecture from a sentence. It searches the space of checkable
changes, with directed cards instead of blind mutation, memory of what worked, and a
verifier that is a real training run. The claim under test is that this beats spending the
same tokens on undirected sampling. Nothing in the design assumes the answer is yes.
