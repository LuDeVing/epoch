"""Reach audit, before any GPU time: does the change do anything, and is every new parameter trained?

Each changed symbol is first sorted by what it touches, from the candidate's own call graph:
- forward: reachable from GPT (the model, its blocks and the loss);
- optimizer: reachable from build_optimizers (Muon, newton_schulz5, ...);
- schedule: reachable from lr_mult;
- untestable here: main and what only main uses, the data loader and the exam, and Config fields
  whose values changed (they may act only through the training loop);
- neutral: module-level statements, new Config fields, helpers nothing calls.
Then one test per kind, on the CPU, candidate against baseline, each built from its own script with
the same seed:
- forward: one short forward pass at initialisation, and again after the same random nudge to every
  shared parameter (a gain at one acts only once it moves);
- optimizer: up to three optimizer steps from the same weights on the same batch; the update must
  differ from the baseline's;
- schedule: lr_mult on a grid of steps; the values must differ.
Verdicts:
- dead_path: a trainable parameter the candidate added receives no gradient (never used in the forward
  pass, or detached), or a frozen one (requires_grad=False) never changes the output;
- no_effect_suspect: every changed symbol is of a tested kind and every test shows no difference, and
  no parameter was added or removed: a path never taken or a value never read (the silent no-op the
  learning rung cannot see on a card whose runs are not bit-reproducible);
- ok: otherwise, with the facts recorded (kinds, new parameters, identity at initialisation).
Runs under nano/launch.py like every candidate process. Writes reach.json; the checker decides.
Design: research_notes/single_agent/thinking_parts/06_reasoning.md item 7; docs/VERDICT.md (the no-op gap).
"""
from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import os
import sys
from pathlib import Path

TESTED = {"forward", "optimizer", "schedule"}
UNTESTABLE = {"loop", "data", "config"}
DATA_SYMBOLS = {"Shards", "evaluate", "param_counts"}


def load(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def build(mod, seed: int, **small):
    import torch
    torch.manual_seed(seed)
    cfg = mod.Config()
    for k, v in small.items():                         # a smaller model for the optimizer test (CPU time)
        if hasattr(cfg, k):
            setattr(cfg, k, v)
    model = mod.GPT(cfg)
    model.train()
    return cfg, model


def _references(src: str) -> tuple[dict[str, set[str]], set[str]]:
    """Top-level names each top-level symbol refers to (type annotations ignored), and the set of
    top-level names. A class's methods count as the class."""
    tree = ast.parse(src)
    for node in ast.walk(tree):                         # annotations are not calls: GPT in "model: GPT" is no edge
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            node.returns = None
            for a in node.args.args + node.args.kwonlyargs + node.args.posonlyargs:
                a.annotation = None
            for a in (node.args.vararg, node.args.kwarg):
                if a is not None:
                    a.annotation = None
    tops = {n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
    refs: dict[str, set[str]] = {}
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = n.body if isinstance(n, ast.ClassDef) else [n]
            names = {x.id for b in body for x in ast.walk(b) if isinstance(x, ast.Name)}
            if isinstance(n, ast.ClassDef):
                names |= {x.id for b in n.bases for x in ast.walk(b) if isinstance(x, ast.Name)}
            refs[n.name] = (names & tops) - {n.name}
    return refs, tops


def _reach(refs: dict[str, set[str]], roots: set[str]) -> set[str]:
    seen, todo = set(), [r for r in roots if r in refs]
    while todo:
        s = todo.pop()
        if s in seen:
            continue
        seen.add(s)
        todo.extend(refs.get(s, set()) - seen)
    return seen


def config_kind(base_mod, cand_mod) -> str:
    """'neutral' when Config only gained fields; 'config' when an existing field's value changed."""
    from dataclasses import asdict
    try:
        b, c = asdict(base_mod.Config()), asdict(cand_mod.Config())
    except Exception:  # noqa: BLE001
        return "config"
    return "config" if any(k in c and c[k] != v for k, v in b.items()) or set(b) - set(c) else "neutral"


def classify(changed: list[str], cand_src: str, base_mod=None, cand_mod=None) -> dict[str, list[str]]:
    """Changed symbol -> the kinds of code it touches."""
    try:
        refs, tops = _references(cand_src)
    except SyntaxError:
        return {s: ["loop"] for s in changed}
    fwd = _reach(refs, {"GPT"})
    opt = _reach(refs, {"build_optimizers"})
    sch = _reach(refs, {"lr_mult"})
    loop = _reach(refs, {"main"})
    out: dict[str, list[str]] = {}
    for sym in changed:
        top = sym.split(".")[0]
        if top == "<module>":
            out[sym] = ["neutral"]
            continue
        if top == "Config":
            out[sym] = [config_kind(base_mod, cand_mod)] if base_mod is not None else ["config"]
            continue
        if top in DATA_SYMBOLS:
            out[sym] = ["data"]
            continue
        kinds = [k for k, s in (("forward", fwd), ("optimizer", opt), ("schedule", sch)) if top in s]
        if not kinds:
            kinds = ["loop"] if (top in loop or top == "main") else ["neutral"]   # a helper nothing calls is neutral
        out[sym] = kinds
    return out


def model_code_changed(changed: list[str], baseline_symbols: set[str]) -> bool:
    """Kept for callers of the old interface: True when any changed symbol is new or a model class."""
    model = {"GPT", "Block", "Attention", "MLP", "RMSNorm", "rope_cache", "apply_rope"}
    return any(s.split(".")[0] in model or s.split(".")[0] not in baseline_symbols for s in changed)


def _as_list(opts) -> list:
    return list(opts) if isinstance(opts, (list, tuple)) else [opts]


def update_differs(base_mod, cand_mod, x, y, steps: int = 3) -> bool | None:
    """Same weights, same batch, the candidate's and the baseline's optimizers: does any parameter end up
    different within `steps` steps? One layer is enough (the optimizer acts per tensor) and keeps the CPU
    cost to seconds. None when the two models cannot be compared parameter by parameter."""
    import torch
    cfg_b, mb = build(base_mod, 0, n_layer=1)
    cfg_c, mc = build(cand_mod, 0, n_layer=1)
    pb, pc = dict(mb.named_parameters()), dict(mc.named_parameters())
    if set(pb) != set(pc) or any(pb[n].shape != pc[n].shape for n in pb):
        return None
    with torch.no_grad():
        for n in pb:
            pc[n].copy_(pb[n])
    ob, oc = _as_list(base_mod.build_optimizers(mb, cfg_b)), _as_list(cand_mod.build_optimizers(mc, cfg_c))
    for _ in range(steps):
        for m, opts in ((mb, ob), (mc, oc)):
            m.zero_grad(set_to_none=True)
            _, loss = m(x, y)
            loss.backward()
            for o in opts:
                o.step()
        if any(not torch.equal(pb[n].detach(), pc[n].detach()) for n in pb):
            return True
    return False


def schedule_differs(base_mod, cand_mod) -> bool:
    cfg_b, cfg_c = base_mod.Config(), cand_mod.Config()
    total = max(1, int(cfg_b.tokens // cfg_b.batch_tokens))
    grid = sorted({0, 1, 2, total // 4, total // 2, 3 * total // 4, max(0, total - 2), total - 1}
                  | set(range(0, total, max(1, total // 97))))
    try:
        for s in grid:
            if abs(float(base_mod.lr_mult(s, total, cfg_b)) - float(cand_mod.lr_mult(s, total, cfg_c))) > 1e-12:
                return True
    except Exception:  # noqa: BLE001   a new signature or an error: not a no-op we can prove
        return True
    return False


def run(candidate: str, baseline: str, changed: list[str], tokens: int = 64, batch: int = 2) -> dict:
    import torch
    torch.set_num_threads(max(1, min(4, os.cpu_count() or 1)))
    base_mod = load(baseline, "htsa_audit_base")
    cand_mod = load(candidate, "htsa_audit_cand")
    kinds = classify(changed, Path(candidate).read_text(encoding="utf-8"), base_mod, cand_mod)
    touched = {k for ks in kinds.values() for k in ks}
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
    params_c = dict(mc.named_parameters())
    trainable_new = [n for n in new if params_c[n].requires_grad]
    frozen_new = [n for n in new if not params_c[n].requires_grad]
    dead = [n for n in trainable_new if params_c[n].grad is None or float(params_c[n].grad.abs().sum()) == 0.0]
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
        dead = [n for n in dead if (params_c[n].grad is None or float(params_c[n].grad.abs().sum()) == 0.0)]
    # a frozen parameter is not trained by design; it is dead only when changing it never changes the output
    with torch.no_grad():
        ref, _ = mc(x, y)
        for n in frozen_new[:10]:
            p = params_c[n]
            keep = p.detach().clone()
            p.add_(torch.randn(p.shape, generator=torch.Generator().manual_seed(3)) * (0.5 * float(keep.abs().mean()) + 0.1))
            moved, _ = mc(x, y)
            p.copy_(keep)
            if torch.allclose(ref, moved, atol=1e-6, rtol=1e-5):
                dead.append(n)
    same_shape = tuple(logits_b.shape) == tuple(logits_c.shape)
    forward_identical = bool(same_shape and torch.allclose(logits_b, logits_c.detach(), atol=1e-6, rtol=1e-5))
    if forward_identical and not new and not removed:
        # identical at initialisation is not the same as identical: a change that only acts once a shared
        # parameter leaves its starting value (a gain at one, a scale at zero) shows up when both models get the
        # same random nudge on every common parameter; a dead marker stays identical under any nudge
        gen = torch.Generator().manual_seed(7)
        cfg_c, mc = build(cand_mod, 0)
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
    tests: dict[str, bool | None] = {}
    if "forward" in touched:
        tests["forward"] = not forward_identical or bool(new) or bool(removed)
    if "optimizer" in touched:
        tests["optimizer"] = update_differs(base_mod, cand_mod, x, y)
    if "schedule" in touched:
        tests["schedule"] = schedule_differs(base_mod, cand_mod)
    testable = bool(touched & TESTED) and not (touched & UNTESTABLE)
    no_effect = testable and not new and not removed and all(v is False for v in tests.values())
    if dead:
        verdict, reason = "dead_path", "new parameters never affect the output: " + ", ".join(dead[:5])
    elif no_effect:
        what = " and ".join(f"the {k} {'pass at initialisation' if k == 'forward' else 'update' if k == 'optimizer' else 'learning rates'}"
                            for k in tests)
        verdict, reason = "no_effect_suspect", (f"the change touches {', '.join(sorted(touched & TESTED))} code, yet {what} "
                                                "are identical to the original's and no parameter was added: the change does "
                                                "nothing (a path never taken, or a value never read)")
    else:
        verdict, reason = "ok", ""
    return {"verdict": verdict, "reason": reason, "kinds": kinds, "tests": tests, "new_params": new[:40],
            "removed_params": removed[:40], "dead_params": dead[:40], "frozen_new_params": frozen_new[:40],
            "forward_identical": forward_identical, "same_logit_shape": same_shape,
            "model_code_changed": "forward" in touched, "changed": changed[:40],
            "loss_base": round(float(loss_b.detach()), 4), "loss_cand": round(float(loss_c.detach()), 4),
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
