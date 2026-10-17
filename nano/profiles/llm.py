"""The language-model profile: lower the validation loss of the nano GPT trainer (nano/train.py) at a fixed
50M-token budget. Every word here reproduces the prompts the loop used before the profiles existed
(backup: D:/AGI-lab/backup/nano_2026-10-17)."""
from __future__ import annotations

CONSTRAINTS = [
    "C1. Same data: the FineWeb-Edu shards in D:/AGI-lab/data/fineweb, loaded through the Shards class as in the baseline.",
    "C2. Same token budget: --tokens 50e6. The exam is run by the harness on the weights the script saves (model.pt): 2M validation tokens in fixed 1024-token windows, plain next-token cross entropy from GPT(cfg).forward(idx) logits. The script never sees val.bin; evaluate() stays as it is and is only a self-report.",
    "C3. Non-embedding parameter count at most 10 percent above the baseline (21.24M); fewer parameters are always allowed.",
    "C4. Peak VRAM under 5.6 GB and step time at most 2x the baseline on an RTX 4050 (6 GB).",
    "C5. The file keeps the same command-line interface and still writes metrics.json with val_loss; --build-only, --smoke-steps and --smoke-seconds must keep working.",
    "C6. No dependencies beyond torch, numpy and the plain standard library; socket, urllib, http, subprocess, ctypes, multiprocessing, importlib, pickle and shutil are denied; no network; no subprocesses; no reference to the validation split anywhere in training code. The process runs under a tripwire that fails the candidate on any of these.",
    "C7. The metric is the exam's validation loss after the fixed budget; a change counts only if it beats the pooled baseline mean by more than 0.005 nats with a one-sided Welch test at p < 0.01 over at least 3 seeds.",
]

ASSUMPTIONS = [
    "attention at every layer sees the full context",
    "every layer has the same width and the same block structure",
    "the optimizer treats every weight matrix the same way",
    "training tokens are sampled uniformly at random from the shards",
    "the learning rate depends only on the step count",
    "the input embedding and the output head share one matrix",
    "the residual stream is a single additive path",
    "positions enter only through rotation of queries and keys",
    "every token costs the same amount of computation",
    "the loss is the plain next-token cross entropy on every position",
]

OUTPUT_FORMAT = """Reply in exactly this form:
HYPOTHESIS: <one sentence: what you change and why it should lower validation loss at a fixed budget>
CHANGE: <one line naming the components touched>
FIDELITY: <exact | partial | substituted | cannot, then one clause: exact = the idea as specified; partial = a piece left out, say which; substituted = a different mechanism with the same aim, say what; cannot = it could not be built within the rules, say why (then return the file unchanged)>
```python
<the COMPLETE modified train.py, every line, ready to run>
```
Keep everything not related to your change identical to the given file."""

BOUNDARY_ALL = "everything except evaluate() and the data loader"

# Default tree for the nano trainer. A planner call may refine it; this is the fallback and the reference for
# what each node means. Boundaries name the code a change at that node may touch.
DEFAULT_TREE = [
    {"id": "root", "name": "lower validation loss at a fixed budget", "parent": None,
     "frame": "An autoregressive Transformer language model trained with next-token cross entropy on a fixed "
              "token budget, judged by held-out validation loss.",
     "assumptions": ["the model predicts the next token", "validation loss on held-out text is the target",
                     "training is one pass over a fixed token budget with a fixed compute budget"],
     "boundary": "everything", "directions": ["upward"]},
    {"id": "io", "name": "inputs and outputs", "parent": "root",
     "frame": "GPT-2 byte-pair tokens; a tied embedding matrix feeds the first layer and produces the logits; "
              "cross entropy on every position.",
     "assumptions": ["tokens are GPT-2 BPE units", "input and output embeddings are one tied matrix",
                     "every position contributes equally to the loss", "the output is a softmax over the full vocabulary"],
     "boundary": "GPT.tok, GPT.head, GPT.forward loss, Config.vocab_size, tie_embeddings", "directions": ["inward", "outward"]},
    {"id": "mix", "name": "sequence mixing (attention)", "parent": "root",
     "frame": "Full causal softmax attention at every layer, 6 heads of 64, rotary positions, keys and values "
              "per head, no sharing across layers.",
     "assumptions": ["every layer attends over the full context", "attention is softmax over dot products",
                     "positions enter only through rotation of queries and keys", "each layer computes its own keys and values",
                     "all heads have the same width and role"],
     "boundary": "Attention, rope_cache, apply_rope, Config.n_head, n_kv_head, sliding_window", "directions": ["inward", "outward"]},
    {"id": "ffn", "name": "per-token computation", "parent": "root",
     "frame": "A SwiGLU feed-forward of hidden size 1024 in every block, dense, same for every token.",
     "assumptions": ["every token passes through the same dense feed-forward", "the activation is SwiGLU",
                     "the hidden size is fixed and equal in every layer"],
     "boundary": "MLP, Config.d_ff", "directions": ["inward", "outward"]},
    {"id": "depth", "name": "state across depth", "parent": "root",
     "frame": "A single additive residual stream, pre-norm RMSNorm, 12 identical blocks, scaled init of the "
              "branch outputs.",
     "assumptions": ["the residual stream is one additive path", "all 12 blocks are identical in structure",
                     "normalization is RMSNorm before each branch", "no connections skip more than one block"],
     "boundary": "Block, GPT.blocks, RMSNorm, GPT._init, Config.n_layer", "directions": ["inward", "outward"]},
    {"id": "opt", "name": "optimization", "parent": "root",
     "frame": "Muon for 2-D weights (lr 0.02, momentum 0.95), AdamW for the rest (lr 3e-3), weight decay 0.1, "
              "2 percent warmup, constant, 30 percent linear cooldown, gradient clipping at 1, batch 32k tokens.",
     "assumptions": ["the learning rate depends only on the step count", "every weight matrix is updated the same way",
                     "the batch size is constant", "gradients are clipped by global norm"],
     "boundary": "Muon, newton_schulz5, build_optimizers, lr_mult, Config lr fields, the train loop in main()", "directions": ["inward", "outward"]},
    {"id": "data", "name": "data", "parent": "root",
     "frame": "Random 1024-token windows sampled uniformly from fixed FineWeb-Edu shards, no repetition control, "
              "no ordering.",
     "assumptions": ["training windows are sampled uniformly at random", "every token in the budget is seen about once",
                     "window length is fixed at 1024"],
     "boundary": "Shards.sample, Config.seq_len, Config.tokens (budget fixed), the batch assembly in the train loop in main(); never evaluate()", "directions": ["inward", "outward"]},
    {"id": "recipe", "name": "the whole recipe (cross-part changes)", "parent": "root",
     "frame": "The parts above are tuned one at a time; changes that only make sense together (for example depth with "
              "mixing, or data order with the learning schedule) have no single owner.",
     "assumptions": ["each part can be improved on its own", "the parts interact only through the residual stream",
                     "the best recipe is a sum of the best parts"],
     "boundary": BOUNDARY_ALL + " (a change here may touch two parts)", "directions": ["inward", "outward"]},
    {"id": "objective", "name": "objective", "parent": "root",
     "frame": "Plain next-token cross entropy averaged over all positions; no auxiliary targets.",
     "assumptions": ["the only training signal is next-token cross entropy", "all positions are weighted equally",
                     "no auxiliary prediction heads"],
     "boundary": "GPT.forward loss computation, new heads if any; evaluate() stays fixed", "directions": ["inward", "outward"]},
]

LENSES = {
    "parts": "the parts of the recipe: inputs/outputs, sequence mixing, per-token computation, state across depth, "
             "optimization, data, objective",
    "dataflow": "the path of one token through the system: file, sampling, embedding, each transformation, the "
                "loss, the gradient on the way back, the update",
    "dynamics": "phases of training: the first steps, the bulk, the cooldown; what limits progress in each phase "
                "and what the loss curve says",
    "bottlenecks": "where capacity, compute or signal is wasted: positions that are easy, tokens that are rare, "
                   "layers that add little, parameters that barely move",
    "failures": "the ways a small model trained briefly fails: what it cannot represent, what it never sees "
                "enough of, what it forgets, where optimisation is unstable",
}

DIRECTIONS = {
    "inward": ("Direction INWARD: keep the paradigm of this part. Treat the assumptions below as FIXED and propose "
               "improvements inside them."),
    "outward": ("Direction OUTWARD: replace the paradigm of this part. Each sketch must remove or invert at least one "
                "of the assumptions below and say which. Ideas that merely tune the current mechanism do not count."),
    "upward": ("Direction UPWARD: question the framing of the whole problem. Sketch alternative formulations of what is "
               "being modeled or measured. These will be logged as proposals for a new verifier, not implemented now, "
               "so include what the new success measure would be."),
    "inward_free": ("Direction INWARD: keep the overall paradigm (a Transformer trained with next-token cross entropy) and "
                    "improve inside it, in whichever part you choose."),
    "outward_free": ("Direction OUTWARD: replace a paradigm of your choice. Each sketch must remove or invert at least one "
                     "design assumption of the current recipe and say which."),
}

OFF_MAP = {
    "node_name": "off the map (whole problem, no part assigned)",
    "node_frame": "The whole recipe, read without the problem map.",
    "blank": ("NO MAP: you are given the whole problem and the script, with no decomposition and no list of "
              "weak spots. Build your own picture of where the loss is being lost, then sketch. Nothing here tells you "
              "where to look; that is the point."),
    "gaps": ("WHAT DID THE MAP MISS? Sketch ideas about parts, interactions between parts, or failure modes "
             "the map has no branch for. Start each sketch with one line MISSING: <the branch the map lacks>."),
    "doubt": ("DOUBT THE MAP: pick one or two facts or assumptions in it that could be wrong, or where the opposite "
              "is the real weak spot. Start each sketch with one line DOUBT: <what the map gets wrong and why>, then "
              "sketch ideas that only make sense if the map is wrong there."),
}

VOCAB = {
    # section 2 of docs/GENERIC_SPEC.md
    "artifact": "training script",
    "artifact_file": "train.py",
    "language": "python",
    "run": "training run",
    "score_phrase": "lower validation loss at the fixed budget",
    "score_name": "validation loss",
    "parts": "parts of the recipe",
    "recipe": "recipe",
    "cheap_test": "a 1-minute smoke run comparison, a 3-step timing, a parameter count",
    "cost_axes": "the step time, the parameter count, peak memory",
    "first_check": "the first learning check (45 matched steps)",
    "targets": ["loss on rare tokens", "loss at late positions", "attention entropy in deep layers", "residual RMS growth",
                "gradient norm spread", "max attention logit", "first-token attention mass", "recall-token loss",
                "update-norm spread", "validation loss only"],
    "scope_default": "validation loss at 1024",
    "levers": "optimizer, schedule, init, normalisation, attention pattern, embeddings, data order, loss, precision, systems",
    "known_tricks": "",
    "boundary_all": BOUNDARY_ALL,
    # added by Agent A for nano/tree.py and nano/loop.py
    "artifact_short": "script",                        # "CURRENT SCRIPT", "The script above ..."
    "artifact_long": "small language-model training script",
    "goal_short": "lowering its validation loss at a fixed token budget",
    "system": "model",                                 # "a smaller part of the model"
    "narrow_examples": "fewer layers, one token class, one phase of training",
    "planner_hint": "boundaries name functions and classes of the script (say 'the train loop in main()' when a part owns the loop)",
    "reference_what": "facts about how current large models are built",
    "reference_use": "adapt a component to this scale only if it should lower validation loss at the fixed budget",
    "digest_title": "WHAT THE STRONGEST OPEN MODELS DO NOW",
    "digest_use": ("a digest with sources; port a component down to this scale, or go past it; a component counts only if "
                   "it should lower validation loss at the fixed budget"),
    "gain_phrase": "the matched-step loss",
    "boundary_rules": ("This is checked by a diff of every function and class against the original: you may also add new "
                       "functions or classes, add fields to Config, and change GPT.__init__ or Block.__init__ to wire a new "
                       "component in; evaluate(), Shards.__init__, Shards.sequential and param_counts never change; socket, "
                       "urllib, http, subprocess, ctypes, multiprocessing, importlib, pickle and shutil may not be imported; "
                       "training code may not refer to the validation split; the harness runs the exam on the saved weights."),
    "identity_rule": ("WIRING RULE: every new path or module is added as x + torch.tanh(self.gate_<name>) * f(x) with "
                      "self.gate_<name> = nn.Parameter(torch.zeros(1)), so the script is exactly the baseline at step 0 and "
                      "the learned gate values are a free read-out of whether the path is used."),
    # added by the prompt modules (Agent B); values from nano/ideate.py LLM_DEFAULT_VOCAB
    'observables': 'the loss curve, the step time, the parameter count',
    'scope_other': 'long context, inference cost, routing balance, robustness',
    'tune_examples': 'a learning rate, warmup, decay, clipping, an init scale, a head count',
    'viable': 'trainable',
    'win_short': 'lowers the loss at this budget',
    'score_short': 'the loss',
    'leap_rules': ('what a loss is, what a layer computes, which tokens see which, how an update is made, what is fixed across '
 'layers or phases, what is shared and what is separate'),
    'field': 'machine learning',
    'probe': 'a five-minute probe on a saved checkpoint',
    'weak_points': 'the positions, the token classes, the layers, the phase of training',
    'adapt_moves': ('the way the public speedrun record adapts ports: zero-initialise the new path so step 0 is the baseline, '
 'apply it to the last k layers only, use fewer channels, share it across layers, add a learned gate with '
 'read-out, change where it plugs in'),
    'separations': 'by training phase, by layer, by token class, by condition',
    'cheap_words': [   'smoke',
    '1-minute',
    'one-minute',
    '60',
    '3-step',
    'three step',
    'step time',
    'param',
    'count',
    'build',
    'timing',
    'memory',
    'vram',
    'matched'],
    'cost_questions': 'compute, memory and step time, parameters and initialisation',
    'full_run': 'trained for the full budget',
    'ladder_metrics': 'param_ratio, step_ratio, learn_z, long_z, trend, fidelity',
    'sources': 'arXiv, lab blogs, the modded-nanoGPT speedrun record log, benchmark write-ups',
    'size_word': 'model size',
    'setting_words': ('attention layer layers model loss train training learning learn embedding embeddings token tokens block '
 'blocks head heads weight weights param params parameter parameters matrix linear transformer network '
 'nanogpt gpt modded speedrun'),
    'setup': 'this exact setup (21M params, 50M tokens)',
    'delta_name': 'val_loss',
    'same_change_example': 'a different gate on the same tensor is new',
    'problem_brief': ('a small language-model training recipe (a GPT-2-style model with 21M non-embedding parameters trained on '
 '50M tokens on one laptop GPU; the measure is validation loss at a fixed token budget)'),
    'measured_numbers': 'loss, perplexity, speed, scale',
    'leap_operators': {   'existence': 'the recipe has measured headroom against its rules (parameters below the cap, step time '
                 'below the cap, memory below the card); assume a change exists that recovers a third of the '
                 'gap between this recipe and a recipe twice its size at no more than two percent extra step '
                 'time; give three mechanisms that could be it and, for each, what would have to be true at '
                 'the first learning check; the leaps are those mechanisms.',
    'import': 'keep the recipe unchanged and add one mechanism from a field far from language modelling '
              '(control, ecology, signal processing, economics, immunology) aimed at a measurement that is '
              'stuck or unexplained; write the shared structure first (their objects to ours, their relation '
              'to ours), then the instantiation and where the correspondence breaks; the leap is the '
              'instantiation.',
    'limit': 'push one quantity of this part to its limit (context of one token, depth one, vocabulary of '
             'two, learning rate zero, infinite width, one head); say what breaks first and which measured '
             'cell would show it; if the baseline already shows that symptom, the leap is the fix the limit '
             'case suggests.',
    'literalize': "find a place where the brief, the findings or the script's comments say one thing behaves "
                  'like or is analogous to another; set the two sides equal as an identity of named '
                  'quantities; derive one consequence the source did not state; the leap is the code change '
                  'that tests that consequence.',
    'remeasure': 'list the constants this part inherited from another scale or another recipe (learning-rate '
                 'rule, warmup, init scale, clipping, softcap, rotary base, head count); pick two; derive or '
                 'infer from the measurements what the value should be at this size; the leap replaces the '
                 'inherited value by the derived one or by a learned or scheduled version.',
    'rerepresent': 'rewrite what this part does in a different form (the optimiser as descent under a norm; '
                   'attention as a kernel smoother over positions; the residual stream as a differential '
                   'equation across depth; the loss as a code length); name one edit that is natural in that '
                   "form and awkward in the code's own; the leap is that edit, translated back into the "
                   'script.',
    'rulebreak': 'list eight rules of this part as testable sentences (equal weight on every token; every '
                 'layer computes the same thing; one schedule; one update rule per tensor; the same context '
                 'for every token; fixed shapes); rank them by how much of the recipe depends on each; drop '
                 'or invert exactly one and say what must change so training still runs; the leap is that '
                 'change.',
    'subtract': 'for each component of this part write what happens if it is removed or frozen at identity '
                'or zero, and what the measurements say it buys; keep the two removals you can defend; '
                'reinvest the freed parameters, steps or memory in one named alternative; the leap is a '
                'removal plus its reinvestment.'},
}


def baseline_summary(prof: dict) -> str:
    """The BASELINE line of problem.md, from the checker's baseline measurement."""
    return "BASELINE (measured): non-embedding params %s; step time %.2fs; smoke drop %s -> %s in %s steps." % (
        f"{prof.get('params_nonembed'):,}", prof.get("step_s") or 0.0,
        prof.get("smoke_loss_first"), prof.get("smoke_loss_last"), prof.get("smoke_steps"))


PROFILE = {
    "name": "llm",
    "spec_id": "gpt2_50m",                       # run folder and ledger item id (unchanged from before profiles)
    "title": "lower the validation loss of the nano language model at a fixed budget",
    "goal": ("change nano/train.py so that, trained for exactly 50M tokens on the same data,\n"
             "its validation loss is lower than the baseline's. Any part of the model, optimizer,\n"
             "schedule or data order may change within the constraints."),
    "aim": "",                                    # --aim fills problem.md PURPOSE; empty by default as before
    "score": {"name": "validation loss", "direction": "lower", "unit": "nats", "margin": 0.005, "alpha": 0.01,
              "min_seeds": 3, "stackable_margin": 0.002, "stackable_alpha": 0.05},
    "vocab": VOCAB,
    "constraints": CONSTRAINTS,
    "assumptions": ASSUMPTIONS,
    "tree": DEFAULT_TREE,
    "lenses": LENSES,
    "directions": DIRECTIONS,
    "off_map": OFF_MAP,
    "boundary_all": BOUNDARY_ALL,
    "artifact": {"path": "nano/train.py", "output_format": OUTPUT_FORMAT,
                 "entry": "python train.py --out OUT --tokens 50e6",
                 "must_contain": ["def main", "metrics.json"]},     # a reply whose code lacks these is not a trainer
    "checker": "llm",
    "checker_args": {},
    "docs": {"digest": "nano/docs/frontier_digest.md", "reference": "nano/docs/modern_architectures.md",
             "reference_note": "reads the 2026 architecture digest (DeepSeek V4.1, MiMo, speedrun)"},
    "diagnostics": "nano.diagnose:text",          # the baseline's diagnostics.md, measured by the LLM checker
    "baseline_summary": baseline_summary,
    "baseline_cache": {"real": "nano_baseline_profile", "mock": "nano_baseline_profile_mock"},
}
