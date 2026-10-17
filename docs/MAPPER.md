# The mapper

What the mapping step does, as the code runs it on 2026-10-17. Code: `nano/tree.py` and
`plan_tree` in `nano/loop.py`. Only the nano loop (the LLM-training problem) has a mapper;
the ARC and NoveltyBench arms do not.

## 1. What it is

- The mapper cuts the problem into parts, once, at the start of a run.
- The problem is: change `nano/train.py` so the model trains better.
- A part is a region of that file (for example: attention, the MLP, the optimizer).
- The parts exist so that idea agents can be pointed at different regions instead of all
  writing about the same one.

## 2. What goes in

One prompt, built by a script, with four pieces:

1. A fixed instruction: return 6 to 9 parts as JSON; each part has `id`, `name`, `frame`,
   `assumptions` (3 to 5), `boundary`.
2. `problem.md`, written earlier by the encode step: the goal, the owner's purpose line,
   the scope (which parts may change), the measured size and speed of the baseline, the
   hard rules C1 to C7.
3. `diagnostics.md`: one page of numbers from a 100-step instrumented run of the baseline
   (loss by position, loss by word frequency, per-layer gradient norm, output size,
   attention entropy, loss curve). Cut at 6000 characters. Produced by `nano/diagnose.py`,
   cached per baseline version.
4. The whole `nano/train.py`.

The instruction also names a lens, one sentence on how to look at the file:

| lens | what it says |
|---|---|
| parts | the parts of the recipe: inputs/outputs, mixing, per-token, depth, optimization, data, objective |
| dataflow | the path of one token: file, sampling, embedding, each transformation, loss, gradient, update |
| dynamics | phases of training: first steps, bulk, cooldown |
| bottlenecks | where capacity, compute or signal is wasted |
| failures | how a small model trained briefly fails |

- `--lens` sets it. Without `--lens`, replicate number modulo 5 picks it (replicate 0 = parts).

The mapper does not get: the web research, the frontier digest, earlier runs' results,
or the anomaly rows. Those come after the map.

## 3. The call

- One call, role `encode`, the strong model (`--model`, Fable in the real runs).
- Output cap 2500 tokens.
- Measured on arch-2 (2026-10-13): 16,142 tokens, $0.40, 2,287 output tokens.
- Logged to `prompts/<id>.txt`, `calls/<id>.json`, and one ledger row with card `plan`.

## 4. What comes back and how the script cleans it

The reply is a JSON array of parts. `parse_planner` then:

- takes the first `[ ... ]` in the text; no JSON means failure;
- drops any entry missing `id`, `name`, `frame` or a list of `assumptions`;
- trims: id to 16 chars (lowercase, a-z 0-9 _), name 60, frame 400, each assumption 160,
  at most 5 assumptions, boundary 200;
- sets `parent = "root"` and `directions = ["inward", "outward"]` on every part;
- fails if fewer than 4 parts survive;
- puts the fixed `root` node first and the fixed `recipe` node last.

Then `plan_tree`:

- on failure, or if `--only-nodes` names parts that none of the planned names resolve to,
  uses the hand-written `DEFAULT_TREE` (7 parts) and logs a decision row;
- appends the fixed `off the map` node, unless the run is scoped with `--only-nodes`;
- writes `problem_tree.json`.

## 5. The shape of the tree

- Root, then one row of parts. Nothing deeper. No code creates a part under a part.
- Every part has `parent = "root"`.

```
 root  (fixed; direction: upward = question the framing)
   |-- part 1
   |-- part 2
   |-- ...
   |-- part N
   |-- recipe       (fixed; home for ideas that touch two parts)
   '-- off the map  (fixed; agents that work without the map)
```

## 6. The three fields of a part

| field | meaning | used by |
|---|---|---|
| frame | how this part works now, 1 to 2 sentences | every idea agent on the part |
| assumptions | design choices a different design could remove | outward agents must break one |
| boundary | the functions and classes a change may touch | rung 0 rejects a build outside it |

Example from arch-2, part `seq_attention_heads`:

- frame: 6 query heads and 6 key/value heads of dim 64, no QK normalization, no gating,
  no learned value or output scaling.
- assumptions: six heads of 64 is right for d=384; query and key magnitudes are free, so
  logits reach 20 in deep layers; full causal attention in every layer; attention output goes
  straight to the residual with no value-residual or gate.
- boundary: `Attention.__init__`, `Attention.forward`, `Config.n_head`, `n_kv_head`,
  `sliding_window`.

The real map of arch-2 had 9 parts: two for inputs/outputs, two for attention, one MLP,
three for depth (wiring, norms, init), plus recipe. Optimizer, data and objective were absent
because the scope froze them.

## 7. How the map is used in the run

- Ideation: for each part and each direction (inward, outward) one agent gets that part's
  three fields and the common problem text. Inward: keep the assumptions. Outward: remove or
  invert one and say which. Root gets two upward agents.
- Off the map: a share of agents (`--off-tree-share`, default 0.4) get no part. Cards: blank
  (no map), gaps (what did the map miss), doubt (which fact in the map is wrong).
- Every prompt ends with: the map is one reader's notes, not an order.
- Research: one web brief per part, cached per part id.
- Selection: build slots are dealt round-robin across parts, starting with the parts that
  have had the fewest.
- Boundary check: rung 0 diffs each build against its part's boundary.
- Accounting: sketches, clusters, built, checked per part and direction, in
  `problem_tree.json` and the report.

## 8. How the map changes after round 1

All by script rules. None adds a level.

- Interrogation finds what an idea silently assumes; the line is appended to the part's
  assumptions (`assumptions_added`).
- An off-map idea that passes the ladder becomes a new part under root (`promote_win`).
- With `--replan`, round 2 calls the planner again with round-1 history and the critics'
  objections. The new list replaces the old. Parts are matched by id or exact name; matched
  parts keep their id and their added assumptions. Unmatched old parts, including promoted
  wins, are dropped.

## 9. What the mapper does not do

- No root-cause analysis: it describes parts, it does not say where the loss is lost or why.
- No causal chain: no field links a part to a measurement or to the loss. Causal chains are
  written later, per idea, in interrogation.
- No research before the map: web briefs are per part, so they run after it.
- No sub-parts, questions or helper questions. The four-level tree in
  `docs/TEAM_OF_RESEARCHERS.md` is design, not code.
- The model never decides the structure. It proposes a list; scripts wrap, trim, fall back,
  merge and promote.

## 10. Knobs

| flag | default | effect |
|---|---|---|
| `--lens` | rotates by replicate | which lens sentence goes in the prompt |
| `--no-planner` | off | skip the call, use `DEFAULT_TREE` |
| `--only-nodes a,b` | none | scope: only these parts may change; no off-map node |
| `--off-tree-share` | 0.4 | share of idea contexts without a part |
| `--replan` | off | redraw the map in round 2 |
| `--no-diagnostics` | off | skip the instrumented run; the mapper then gets no measurements page |
| `--diag-steps` | 100 | steps of the instrumented baseline run |
| `--anomaly-seeds` | 3 | seeds of that run (seed 0's page goes to the mapper) |

## 11. Worked example: the arch-2 run, start to finish

Real run, 2026-10-13, batch `arch-2`, replicate 0, mapper Fable, scope `io,mix,ffn,depth`.
Folder: `D:\AGI-lab\runs\arch-2__nano__gpt2_50m__scaffold__r0`.

### Step A. Encode writes the problem statement (1 model call, earlier)

`problem.md`, abridged:

```
GOAL: change nano/train.py so that, trained for exactly 50M tokens on the same data,
      its validation loss is lower than the baseline's.
PURPOSE: ideas that would make the strongest open-source language model; this small
      recipe is the test bench, so every idea must say why it would hold at large scale.
SCOPE OF THIS RUN: only these parts may change; optimization, data, the whole recipe,
      objective stay exactly as they are:
      - inputs and outputs: GPT.tok, GPT.head, GPT.forward loss, Config.vocab_size, ...
      - sequence mixing: Attention, rope_cache, apply_rope, Config.n_head, ...
      - per-token computation: MLP, Config.d_ff
      - state across depth: Block, GPT.blocks, RMSNorm, GPT._init, Config.n_layer
BASELINE (measured): 21,243,264 non-embedding params; 1.07 s/step.
HARD CONSTRAINTS C1..C7 (same data, hidden exam, params <= +10%, step <= 2x, same CLI,
      no network, win = 0.005 nats at p < 0.01 over 3+ seeds)
```

### Step B. Script measures the baseline (no model call, GPU, cached)

`diagnostics.md`, abridged:

```
loss by position     0-64: 5.94 | 64-256: 6.47 | 256-1024: 6.41   (late - early +0.46)
loss by frequency    top-100 words 3.06 (42% of tokens) ... rarest 11.77
grad norm (attn)     layer 0: 0.908   layers 1-11: 0.04 to 0.07
attention entropy    0.975 at layer 0 -> 0.834 at layer 11
residual RMS         1.78 -> 9.01 across the 12 blocks (x5.1)
max attention logit  9 at layer 0 -> 20 at layer 11
recall tokens        4.47 vs 6.68 for the rest
+ a 12-row table (layer | grad attn | grad mlp | RMS | entropy) + loss curve
```

### Step C. Script assembles the prompt (23,583 characters)

```
Decompose the following problem into parts for a research search. Return ONLY a JSON
array of nodes {"id", "name", "frame", "assumptions": [3-5 short sentences],
"boundary": "<which functions or classes a change may touch>"} with 6 to 9 parts.
Draw the map through this lens: the parts of the recipe: inputs/outputs, sequence
mixing, per-token computation, state across depth, optimization, data, objective.
Frames describe the CURRENT design in one or two sentences; assumptions are the
design choices a different paradigm could remove; boundaries name functions and
classes of the script.

GOAL:
<problem.md>

HOW THE BASELINE BEHAVES (measured):
<diagnostics.md>

SCRIPT:
```python
<all of nano/train.py>
```
```

Lens is `parts` because replicate 0 and no `--lens`.

### Step D. The call (1 model call)

- Fable, role `encode`, output cap 2500.
- Result: 16,142 tokens total, 2,287 output, $0.40.
- Reply, first entries (abridged):

```
[
 {"id": "io_embed_head",
  "name": "Inputs and outputs: tied embedding and output head",
  "frame": "Tokens enter through a single 50304 x 384 embedding table that is also
            the output projection; the final RMSNorm feeds this tied head ...",
  "assumptions": ["The input embedding and output head must share one matrix at scale 1.",
                  "The logits are computed at full vocab width with no temperature,
                   no softcap and no per-token scaling.",
                  "The embedding is read once at layer 0 and never re-injected.",
                  "Frequency-rank structure of the vocabulary (rank 0-100 covers 42%
                   of tokens) is not used to shape the head or the loss."],
  "boundary": "GPT.tok, GPT.head, GPT.norm, GPT.forward loss computation,
               Config.vocab_size, Config.tie_embeddings"},
 {"id": "seq_rope_positions", ...},
 {"id": "seq_attention_heads", ...},
 {"id": "token_mlp", ...},
 {"id": "depth_block_wiring", ...},
 {"id": "depth_normalization", ...},
 {"id": "depth_init", ...},
 {"id": "io_loss_shape", ...}
]
```

Two things to notice. The measurements became assumptions ("42% of tokens", "logits grow
to 20"). The scope removed three parts: no optimizer, data or objective node.

### Step E. Script cleans and wraps (no model call)

- 8 entries parsed; all had the four required keys.
- `seq_rope_positions` became `seq_rope_positio` (16-char id cap); likewise
  `seq_attention_he`, `depth_block_wiri`, `depth_normalizat`.
- `root` put first, `recipe` put last. (The off-map node did not exist on 2026-10-13.)
- Scope check: `io`, `mix`, `ffn`, `depth` each resolved to at least one planned name
  ("inputs and outputs: ...", "sequence mixing: ...", "per-token computation: ...",
  "state across depth: ..."), so the planned map was kept.
- `problem_tree.json` written.

### Step F. The tree

```
root  lower validation loss at a fixed budget                 [upward]
  |-- io_embed_head      tied embedding and output head        [inward, outward]
  |-- seq_rope_positio   rotary position encoding              [inward, outward]
  |-- seq_attention_he   multi-head attention layout           [inward, outward]
  |-- token_mlp          SwiGLU MLP                            [inward, outward]
  |-- depth_block_wiri   block structure and residual stream   [inward, outward]
  |-- depth_normalizat   RMSNorm placement and parameters      [inward, outward]
  |-- depth_init         weight initialization                 [inward, outward]
  |-- io_loss_shape      loss shaping within forward           [inward, outward]
  '-- recipe             cross-part changes                    [inward, outward]
```

### Step G. The tree hands out the work (rest of round 1)

- Research: 8 web briefs, one per part, on Sonnet.
- Ideation: 24 contexts, 237 sketches. Counted from `ideas.jsonl`: 16 contexts on the
  research card (8 parts x 2 directions, each reading its part's brief) and 8 on the
  diagnosis card (one per part, inward, reading the measurements). No upward context
  produced a sketch. Interrogation later added 12 contexts and 72 offshoot sketches.
- Each context's prompt carried its part's frame, assumptions and boundary, for example
  for `seq_attention_he` outward:

```
PART UNDER STUDY: Sequence mixing: multi-head attention layout
CURRENT DESIGN OF THIS PART: Each block runs 6 full query heads and 6 key/value heads
  of dim 64 with no QK normalization, no gating, and no learned value or output scaling
CODE THIS PART MAY TOUCH: Attention.__init__, Attention.forward, Config.n_head,
  Config.n_kv_head, Config.sliding_window
ASSUMPTIONS OF THIS PART:
- Six heads of 64 dims is the right head count and width for d=384.
- Query and key magnitudes are left free, so max attention logits can grow to 20.
- Full causal attention over all 1024 positions is used in every layer.
- Attention output goes straight to the residual with no value-residual, gate, or
  head-wise scaling.

Direction OUTWARD: replace the paradigm of this part. Each sketch must remove or
invert at least one of the assumptions below and say which.

This map is one reader's notes, not an order: ...
```

- Clustering: 131 clusters, each tagged with its part and direction.
- Counts written back to the tree, per part and direction (from `problem_tree.json`):

```
part                 inward sketches/clusters   outward sketches/clusters
io_embed_head        15 / 12                    13 / 6
seq_rope_positio     13 / 9                      7 / 4
seq_attention_he     14 / 11                    20 / 11
token_mlp             8 / 8                     18 / 14
depth_block_wiri     15 / 9                      8 / 4
depth_normalizat     30 / 13                     8 / 3
depth_init           21 / 11                     8 / 2
io_loss_shape        32 / 12                     7 / 2
recipe                0 / 0                      0 / 0
```

### Step H. The tree grows by rule (interrogation)

Interrogation of chosen ideas wrote ASSUMES lines; the script appended them to the part.
`seq_attention_he` went from 4 assumptions to 12, for example:

```
- Key=value is applied uniformly in all 12 layers, including layer 0 whose attention
  is nearly flat and the deep layers whose attention is sharp.
- The value is the current token's key with no mixing from other layers or positions.
```

The run was stopped by control file after interrogation (builds done by hand), so no
promotion and no re-plan happened. The tree stayed as in step F, with longer
assumption lists.

### Step I. What this map led to

The arch-2 sketches were built by hand into 14 single-idea files and one combined file on
the plain recipe; the combined file gave a verified gain of 0.009 nats over 4 seeds.

The final model (7 percent lower perplexity) came from a later run, `skel-1`, where the
same mapper read the frontier skeleton instead. Same lens, same procedure, a different
map, because the script was different:

```
root
  |-- io_embed_head      tied embedding, stream read-out, logits
  |-- attn_latent_kv     latent KV compression and expansion
  |-- attn_rope_norm     decoupled rotary dims and QK-norm
  |-- attn_heads_outpu   head count, head structure, output projection
  |-- mlp_swiglu         SwiGLU MLP
  |-- depth_stream_mix   four-stream Sinkhorn residual mixing
  |-- depth_norm_init    normalization placement and initialization
  |-- depth_layer_stac   layer count and block layout
  '-- recipe
```

Two of the final model's parts sat in that map as unpicked clusters: "narrow keys, wide
values" under `attn_latent_kv` inward, and "signed linear reads" under
`depth_stream_mix` inward. Neither was selected for a build by the run; both were found
by reading the full sketch catalogue afterwards. The map put them in the right place; the
selection did not pick them.

## 12. Worked example: a round-2 re-plan (mock-dry15, not a real run)

With `--replan`, round 2 repeats steps C to E with two additions to the prompt: the
history text (what was built, passed, failed, and why) and up to 20 critic objections.
In the dry run of 2026-10-14 the mock planner answered with the old parts plus a new
part `sched`; the script matched the old parts by id, kept their added assumptions, and
logged `{"step": "replan", "parts": [..., "sched"]}`. If the planner's reply had been
unusable, the log line would have been `planner output unusable; map kept`.

## 13. Files

- `nano/tree.py`: `DEFAULT_TREE`, `LENSES`, `planner_prompt`, `parse_planner`,
  `resolve_scope`, `node_prompt`, `OFF_TREE_NODE`, `promote_win`, `split_select`.
- `nano/loop.py`: `plan_tree`, `_ensure_off_node`, `replan_tree`, `_write_tree`.
- `nano/diagnose.py`: the measurements page.
- Run folder: `problem_tree.json`, `prompts/<id>.txt`, `calls/<id>.json`, `state.json`
  decisions with step `plan` or `replan`.
