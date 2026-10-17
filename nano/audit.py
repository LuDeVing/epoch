"""Reach audit, before any GPU time: does the change do anything, and is every new parameter trained?

One short forward and backward pass on the CPU, candidate against baseline, each built from its own
script with the same seed. Verdicts:
- dead_path: a parameter the candidate added receives no gradient (never used in the forward pass, or
  detached), so the idea is not what was built;
- no_effect_suspect: the model code changed, yet the forward pass at initialisation is identical to the
  original's and no new parameter exists: a path never taken or a value never read (the silent no-op the
  learning rung cannot see on a card whose runs are not bit-reproducible);
- ok: otherwise, with the facts recorded (new parameters, identity at initialisation).
Runs under nano/launch.py like every candidate process. Writes audit.json; the checker decides.
Design: research_notes/thinking_parts/06_reasoning.md item 7; docs/VERDICT.md (the no-op gap).
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path

MODEL_SYMBOLS = {"GPT", "Block", "Attention", "MLP", "RMSNorm", "rope_cache", "apply_rope"}


def load(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def build(mod, seed: int):
    import torch
    torch.manual_seed(seed)
    cfg = mod.Config()
    model = mod.GPT(cfg)
    model.train()
    return cfg, model


def model_code_changed(changed: list[str], baseline_symbols: set[str]) -> bool:
    for sym in changed:
        top = sym.split(".")[0]
        if top in MODEL_SYMBOLS or top not in baseline_symbols:      # a known model class, or a new symbol
            return True
    return False


def run(candidate: str, baseline: str, changed: list[str], tokens: int = 64, batch: int = 2) -> dict:
    import torch
    torch.set_num_threads(max(1, min(4, os.cpu_count() or 1)))
    base_mod = load(baseline, "htsa_audit_base")
    cand_mod = load(candidate, "htsa_audit_cand")
    cfg_b, mb = build(base_mod, 0)
    cfg_c, mc = build(cand_mod, 0)
    shapes_b = {n: tuple(p.shape) for n, p in mb.named_parameters()}
    shapes_c = {n: tuple(p.shape) for n, p in mc.named_parameters()}
    new = [n for n, s in shapes_c.items() if shapes_b.get(n) != s]
    removed = [n for n in shapes_b if n not in shapes_c]
    vocab = min(int(cfg_b.vocab_size), int(cfg_c.vocab_size))
    g = torch.Generator().manual_seed(1)
    x = torch.randint(0, vocab, (batch, tokens), generator=g)
    if vocab > 50256:
        x[:, tokens // 2] = 50256        # one end-of-text token, so document-aware changes have something to act on
    y = torch.roll(x, -1, dims=1)
    with torch.no_grad():
        logits_b, loss_b = mb(x, y)
    logits_c, loss_c = mc(x, y)
    loss_c.backward()
    dead = [n for n, p in mc.named_parameters() if n in new and (p.grad is None or float(p.grad.abs().sum()) == 0.0)]
    if dead:
        # a parameter behind a zero-initialised one gets no gradient at step 0 but does once the other moves
        # (a zero table feeding a projection); take one tiny step on everything that has a gradient and look again
        with torch.no_grad():
            for _, p in mc.named_parameters():
                if p.grad is not None:
                    p.add_(p.grad.sign(), alpha=-1e-3)
        mc.zero_grad(set_to_none=True)
        _, loss_c2 = mc(x, y)
        loss_c2.backward()
        dead = [n for n in dead if (dict(mc.named_parameters())[n].grad is None
                                    or float(dict(mc.named_parameters())[n].grad.abs().sum()) == 0.0)]
    same_shape = tuple(logits_b.shape) == tuple(logits_c.shape)
    forward_identical = bool(same_shape and torch.allclose(logits_b, logits_c.detach(), atol=1e-6, rtol=1e-5))
    if forward_identical and not new and not removed:
        # identical at initialisation is not the same as identical: a change that only acts once a shared
        # parameter leaves its starting value (a gain at one, a scale at zero) shows up when both models get the
        # same random nudge on every common parameter; a dead marker stays identical under any nudge
        gen = torch.Generator().manual_seed(7)
        pc = dict(mc.named_parameters())
        with torch.no_grad():
            for n, pb in mb.named_parameters():
                if n in pc and tuple(pc[n].shape) == tuple(pb.shape):
                    noise = torch.randn(pb.shape, generator=gen) * (0.05 * float(pb.std()) + 1e-3)
                    pb.add_(noise)
                    pc[n].add_(noise)
            lb2, _ = mb(x, y)
            lc2, _ = mc(x, y)
        forward_identical = bool(torch.allclose(lb2, lc2, atol=1e-5, rtol=1e-4))
    base_syms = {n.split(".")[0] for n in shapes_b} | MODEL_SYMBOLS | {"Config", "Shards", "Muon", "build_optimizers", "lr_mult", "main", "evaluate", "param_counts"}
    mcc = model_code_changed(changed, base_syms)
    if dead:
        verdict = "dead_path"
    elif forward_identical and mcc and not new and not removed:
        verdict = "no_effect_suspect"
    else:
        verdict = "ok"
    return {"verdict": verdict, "new_params": new[:40], "removed_params": removed[:40], "dead_params": dead[:40],
            "forward_identical": forward_identical, "same_logit_shape": same_shape, "model_code_changed": mcc,
            "changed": changed[:40], "loss_base": round(float(loss_b), 4), "loss_cand": round(float(loss_c), 4),
            "tokens": tokens, "batch": batch}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", required=True)
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--changed", default="", help="comma-separated symbols the candidate changed (from the boundary diff)")
    ap.add_argument("--tokens", type=int, default=64)
    ap.add_argument("--batch", type=int, default=2)
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    changed = [c.strip() for c in a.changed.split(",") if c.strip()]
    try:
        res = run(a.candidate, a.baseline, changed, a.tokens, a.batch)
    except Exception as e:  # noqa: BLE001
        res = {"verdict": "error", "error": f"{type(e).__name__}: {str(e)[:300]}"}
    (out / "reach.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps(res))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
