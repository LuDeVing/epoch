"""Look at the data before theorising: one instrumented run of the baseline, written as a one-page
table that ideation, interrogation and the planner all read.

Measured on the baseline at a few points of a short run (default 100 steps):
  - the loss curve and where it bends
  - loss by position in the window (early / middle / late tokens)
  - loss by token frequency (the 100 most frequent tokens, the next 900, the next 9,000, the rest)
  - per layer: gradient norm of the attention and MLP weights, the RMS of the block's output, and
    the attention entropy (normalised by log of the context length: 1 = flat, 0 = one-hot)
Plain statements are derived from the numbers (ratios, where the minimum is); no interpretation.

Usage: python -I nano/diagnose.py --out <folder> [--steps 100]
Writes diagnostics.json and diagnostics.md. Standard-library + torch + numpy only; runs on the card.

These measurements belong to the language-model profile. torch, numpy and the trainer are imported only when a
run is diagnosed, so text(), cell_of() and fidelity() work for any profile; on a profile without diagnostics
text() returns "" and cell_of() names no cell.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from pathlib import Path

import importlib.util

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nano.ideate import has_diagnostics, vword  # noqa: E402,F401

np = torch = F = T = None          # loaded by _load() when a run is diagnosed
_orig_sdpa = None


def _load() -> None:
    global np, torch, F, T, _orig_sdpa
    if torch is None:
        import numpy as _np
        import torch as _torch
        import torch.nn.functional as _F
        np, torch, F = _np, _torch, _F
        _orig_sdpa = F.scaled_dot_product_attention
    if T is None:
        from nano import train as _T
        T = _T


def _unit() -> str:
    try:
        from nano.ideate import PF
        return str((getattr(PF.current(), "score", None) or {}).get("unit") or "nats")
    except Exception:  # noqa: BLE001
        return "nats"


def text(baseline: dict | None = None, path: str | None = None, cap: int = 6000) -> str:
    """The measured-behaviour text the prompts read (a profile's "diagnostics" hook): the diagnostics.md of the
    baseline measurement (path, or baseline["diagnostics_md"]). "" when the profile has no diagnostics or
    nothing was measured."""
    if not has_diagnostics():
        return ""
    p = path or (baseline or {}).get("diagnostics_md")
    if not p:
        return ""
    try:
        return Path(p).read_text(encoding="utf-8")[:cap]
    except Exception:  # noqa: BLE001
        return ""


def load_script(path: str):
    """Diagnose a candidate script instead of the baseline: load it as a module under the same name
    contract (Config, GPT, Shards, build_optimizers, lr_mult, Muon)."""
    global T
    spec = importlib.util.spec_from_file_location("htsa_diag_target", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["htsa_diag_target"] = mod
    spec.loader.exec_module(mod)
    T = mod
    return mod

POS_BUCKETS = [(0, 64), (64, 256), (256, 1024)]
FREQ_BUCKETS = [(0, 100), (100, 1000), (1000, 10000), (10000, 10 ** 9)]
_entropy: list[float] = []
_maxlogit: list[float] = []
_firstmass: list[float] = []
_capture = {"on": False}


def _sdpa_with_entropy(q, k, v, attn_mask=None, dropout_p=0.0, is_causal=False, scale=None, **kw):
    if _capture["on"]:
        with torch.no_grad():
            qq, kk = q[:1].float(), k[:1].float()
            d = qq.shape[-1]
            s = (qq @ kk.transpose(-1, -2)) / math.sqrt(d) if scale is None else (qq @ kk.transpose(-1, -2)) * scale
            Tq = s.shape[-1]
            mask = torch.ones(Tq, Tq, dtype=torch.bool, device=s.device).tril() if (is_causal or attn_mask is None) else attn_mask
            if attn_mask is not None and attn_mask.dtype == torch.bool:
                mask = attn_mask
            s = s.masked_fill(~mask, float("-inf"))
            p = torch.softmax(s, dim=-1)
            ent = -(p * torch.log(p.clamp_min(1e-12))).sum(-1)          # [1, H, T]
            norm = torch.log(torch.arange(1, Tq + 1, device=s.device).float()).clamp_min(1e-6)
            _entropy.append(float((ent / norm).mean()))
            _maxlogit.append(float(s.masked_fill(~mask, 0.0).max()))
            _firstmass.append(float(p[..., 1:, 0].mean()))                 # attention mass on the first token
    return _orig_sdpa(q, k, v, attn_mask=attn_mask, dropout_p=dropout_p, is_causal=is_causal, scale=scale, **kw)


def token_ranks(vocab: int, n_tokens: int = 20_000_000) -> np.ndarray:
    """Rank of every token id by frequency in the first n_tokens of the first train shard (0 = most frequent)."""
    files = sorted(T.DATA_DIR.glob("train_*.bin"))
    d = np.memmap(files[0], dtype=np.uint16, mode="r")
    counts = np.bincount(np.asarray(d[:n_tokens], dtype=np.int64), minlength=vocab)
    order = np.argsort(-counts)
    ranks = np.empty(vocab, dtype=np.int64)
    ranks[order] = np.arange(vocab)
    return ranks


def diagnose(steps: int = 100, seed: int = 0) -> dict:
    _load()
    cfg = T.Config(seed=seed)
    torch.manual_seed(seed)
    np.random.seed(seed)
    torch.backends.cuda.matmul.allow_tf32 = True
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.bfloat16
    model = T.GPT(cfg).to(device)
    opts = T.build_optimizers(model, cfg)
    train = T.Shards("train", cfg.seq_len, cfg.seed)
    ranks = torch.from_numpy(token_ranks(cfg.vocab_size)).to(device)
    accum = max(1, cfg.batch_tokens // (cfg.micro_batch * cfg.seq_len))
    total_steps = max(1, int(cfg.tokens // cfg.batch_tokens))
    probe_x, probe_y = train.sample(cfg.micro_batch, device)         # a fixed probe batch (train data)
    act_rms: dict[int, float] = {}

    def hook(i):
        def _h(_m, _i, out):
            if _capture["on"]:
                act_rms[i] = float(out.detach().float().pow(2).mean().sqrt())
        return _h
    for i, b in enumerate(model.blocks):
        b.register_forward_hook(hook(i))
    F.scaled_dot_product_attention = _sdpa_with_entropy
    T.F.scaled_dot_product_attention = _sdpa_with_entropy

    def recall_mask(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
        """Targets whose (previous token, token) bigram already occurred earlier in the same window."""
        B, L = y.shape
        prev = x
        key = prev.long() * 65536 + y.long()
        out = torch.zeros_like(y, dtype=torch.bool)
        for b in range(B):
            seen = set()
            for t in range(L):
                k = int(key[b, t])
                if k in seen:
                    out[b, t] = True
                seen.add(k)
        return out

    def update_spread() -> dict:
        """Spread of per-tensor update sizes from the last optimizer step: max/median of ||dw||/||w||."""
        ratios = []
        for name, p in model.named_parameters():
            prev = prev_params.get(name)
            if prev is None or p.numel() < 1000:
                continue
            d = (p.detach().float() - prev).norm()
            ratios.append(float(d / (prev.norm() + 1e-12)))
        if not ratios:
            return {"max": None, "median": None}
        ratios.sort()
        return {"max": round(ratios[-1], 5), "median": round(ratios[len(ratios) // 2], 5)}

    prev_params: dict = {}

    def probe(step: int) -> dict:
        model.zero_grad(set_to_none=True)
        _entropy.clear(); _maxlogit.clear(); _firstmass.clear()
        _capture["on"] = True
        with torch.autocast("cuda", dtype=dtype, enabled=(device == "cuda")):
            logits, _ = model(probe_x, probe_y)
        _capture["on"] = False
        tok_loss = F.cross_entropy(logits.float().view(-1, logits.size(-1)), probe_y.view(-1), reduction="none").view(probe_y.shape)
        loss = tok_loss.mean()
        loss.backward()
        pos = torch.arange(cfg.seq_len, device=device)[None, :].expand_as(probe_y)
        by_pos = {f"{a}-{b}": round(float(tok_loss[(pos >= a) & (pos < b)].mean()), 3) for a, b in POS_BUCKETS if b <= cfg.seq_len}
        rm = recall_mask(probe_y, probe_x)
        recall_loss = round(float(tok_loss[rm].mean()), 3) if rm.any() else None
        nonrecall_loss = round(float(tok_loss[~rm].mean()), 3) if (~rm).any() else None
        gates = {n: round(float(p.detach().float().abs().mean()), 4) for n, p in model.named_parameters() if "gate" in n and p.numel() <= 64}
        r = ranks[probe_y]
        by_freq = {}
        for a, b in FREQ_BUCKETS:
            m = (r >= a) & (r < b)
            if m.any():
                by_freq[f"rank {a}-{min(b, cfg.vocab_size)}"] = {"loss": round(float(tok_loss[m].mean()), 3), "share": round(float(m.float().mean()), 3)}
        layers = []
        for i, b in enumerate(model.blocks):
            ga = math.sqrt(sum(float(p.grad.float().norm()) ** 2 for p in b.attn.parameters() if p.grad is not None))
            gm = math.sqrt(sum(float(p.grad.float().norm()) ** 2 for p in b.mlp.parameters() if p.grad is not None))
            layers.append({"layer": i, "grad_attn": round(ga, 4), "grad_mlp": round(gm, 4),
                           "act_rms": round(act_rms.get(i, 0.0), 3),
                           "attn_entropy": round(_entropy[i], 3) if i < len(_entropy) else None,
                           "max_logit": round(_maxlogit[i], 2) if i < len(_maxlogit) else None,
                           "first_token_mass": round(_firstmass[i], 4) if i < len(_firstmass) else None})
        emb = float(model.tok.weight.grad.float().norm()) if model.tok.weight.grad is not None else None
        model.zero_grad(set_to_none=True)
        return {"step": step, "probe_loss": round(float(loss), 4), "by_position": by_pos, "by_frequency": by_freq,
                "recall_loss": recall_loss, "nonrecall_loss": nonrecall_loss, "recall_share": round(float(rm.float().mean()), 3),
                "layers": layers, "grad_embedding": round(emb, 4) if emb is not None else None,
                "update_spread": update_spread(), "gates": gates}

    probes = [probe(0)]
    losses: list[float] = []
    t0 = time.time()
    model.train()
    for step in range(1, steps + 1):
        m = T.lr_mult(step - 1, total_steps, cfg)
        for o in opts:
            for g in o.param_groups:
                g["lr"] = (cfg.lr if isinstance(o, T.Muon) else cfg.lr_adam) * m
        loss_acc = 0.0
        for _ in range(accum):
            x, y = train.sample(cfg.micro_batch, device)
            with torch.autocast("cuda", dtype=dtype, enabled=(device == "cuda")):
                _, loss = model(x, y)
            (loss / accum).backward()
            loss_acc += loss.item() / accum
        if cfg.grad_clip:
            torch.nn.utils.clip_grad_norm_(model.parameters(), cfg.grad_clip)
        if step in (max(1, steps // 2), steps):
            prev_params = {n: p.detach().float().clone() for n, p in model.named_parameters() if p.numel() >= 1000}
        for o in opts:
            o.step()
        model.zero_grad(set_to_none=True)
        losses.append(loss_acc)
        if step in (max(1, steps // 2), steps):
            probes.append(probe(step))
            prev_params = {}
    wall = time.time() - t0
    # where the curve bends: the step after which the per-10-step improvement halves
    knee = None
    seg = [sum(losses[i: i + 10]) / len(losses[i: i + 10]) for i in range(0, len(losses), 10)]
    for i in range(1, len(seg) - 1):
        if (seg[i - 1] - seg[i]) > 0 and (seg[i] - seg[i + 1]) < 0.5 * (seg[i - 1] - seg[i]):
            knee = i * 10
            break
    return {"steps": steps, "seed": seed, "wall_s": round(wall, 1), "loss_curve": [round(l, 4) for l in losses],
            "knee_step": knee, "probes": probes, "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}


def statements(d: dict) -> list[str]:
    """Plain arithmetic statements from the final probe; no interpretation."""
    out = []
    unit = _unit()
    last = d["probes"][-1]
    first = d["probes"][0]
    bp = last["by_position"]
    if bp:
        keys = list(bp)
        out.append(f"At step {last['step']}, loss by position: " + ", ".join(f"{k}: {v}" for k, v in bp.items())
                   + f" (late minus early: {bp[keys[-1]] - bp[keys[0]]:+.3f} {unit}).")
    bf = last["by_frequency"]
    if bf:
        ks = list(bf)
        out.append("Loss by token frequency: " + ", ".join(f"{k}: {v['loss']} ({v['share']:.0%} of tokens)" for k, v in bf.items())
                   + f"; rarest minus most frequent: {bf[ks[-1]]['loss'] - bf[ks[0]]['loss']:+.3f} {unit}.")
    L = last["layers"]
    if L:
        ga = [l["grad_attn"] for l in L]
        gm = [l["grad_mlp"] for l in L]
        ent = [l["attn_entropy"] for l in L if l["attn_entropy"] is not None]
        rms = [l["act_rms"] for l in L]
        out.append(f"Gradient norms by layer (attention): first {ga[0]}, last {ga[-1]}, min at layer {ga.index(min(ga))}, "
                   f"max at layer {ga.index(max(ga))}; (MLP): first {gm[0]}, last {gm[-1]}.")
        if ent:
            out.append(f"Attention entropy (1 = flat): layer values {ent}; lowest at layer {ent.index(min(ent))} ({min(ent)}), "
                       f"highest at layer {ent.index(max(ent))} ({max(ent)}).")
        out.append(f"Residual stream RMS after each block: first {rms[0]}, last {rms[-1]} (growth x{rms[-1] / max(rms[0], 1e-6):.1f}).")
    out.append(f"Probe loss fell from {first['probe_loss']} at step 0 to {last['probe_loss']} at step {last['step']}"
               + (f"; the per-10-step improvement halved after step {d['knee_step']}." if d.get("knee_step") else "."))
    if last.get("recall_loss") is not None:
        out.append(f"Recall tokens (bigram already seen in the window, {last.get('recall_share', 0):.0%} of targets): loss {last['recall_loss']} "
                   f"against {last.get('nonrecall_loss')} for the rest.")
    L = last["layers"]
    if L and L[0].get("max_logit") is not None:
        ml = [l["max_logit"] for l in L]
        fm = [l["first_token_mass"] for l in L]
        out.append(f"Max attention logit by layer: {ml} (largest at layer {ml.index(max(ml))}); first-token attention mass: {fm}.")
    us = last.get("update_spread") or {}
    if us.get("max") is not None:
        out.append(f"Update size per step (||dw||/||w||): median {us['median']}, max {us['max']} (spread x{us['max'] / max(us['median'], 1e-9):.0f}).")
    if last.get("gates"):
        out.append("Learned gates (mean |a|): " + ", ".join(f"{k}={v}" for k, v in list(last["gates"].items())[:12]) + ".")
    return out


# the measured cells a sketch may name as its TARGET, and how to read each from a diagnostics json
CELLS = {
    "rare": lambda d: list(d["probes"][-1]["by_frequency"].values())[-1]["loss"] if d["probes"][-1]["by_frequency"] else None,
    "late": lambda d: list(d["probes"][-1]["by_position"].values())[-1] if d["probes"][-1]["by_position"] else None,
    "entropy": lambda d: sum(x["attn_entropy"] for x in d["probes"][-1]["layers"][-4:] if x["attn_entropy"] is not None) / 4,
    "rms": lambda d: d["probes"][-1]["layers"][-1]["act_rms"] / max(d["probes"][-1]["layers"][0]["act_rms"], 1e-6),
    "grad": lambda d: max(x["grad_attn"] for x in d["probes"][-1]["layers"]) / max(min(x["grad_attn"] for x in d["probes"][-1]["layers"]), 1e-9),
    "logit": lambda d: max(x["max_logit"] for x in d["probes"][-1]["layers"] if x.get("max_logit") is not None),
    "first": lambda d: sum(x["first_token_mass"] for x in d["probes"][-1]["layers"] if x.get("first_token_mass") is not None) / len(d["probes"][-1]["layers"]),
    "recall": lambda d: d["probes"][-1].get("recall_loss"),
    "update": lambda d: (d["probes"][-1].get("update_spread") or {}).get("max"),
}
CELL_WORDS = {"rare": ("rare", "frequency", "infrequent"), "late": ("late", "position", "far"), "entropy": ("entropy",),
              "rms": ("rms", "residual"), "grad": ("gradient", "grad"), "logit": ("logit",), "first": ("first-token", "first token", "sink"),
              "recall": ("recall", "bigram", "copy"), "update": ("update", "norm spread")}


def cell_of(target: str) -> str | None:
    if not has_diagnostics():
        return None
    t = (target or "").lower()
    for cell, words in CELL_WORDS.items():
        if any(w in t for w in words):
            return cell
    return None


def fidelity(target: str, cand: dict, base: dict) -> dict:
    """Did the quantity the sketch named move, and in the stated direction?"""
    cell = cell_of(target)
    if not cell:
        return {"checkable": False, "note": "no diagnostic cell named"}
    try:
        cv, bv = CELLS[cell](cand), CELLS[cell](base)
    except Exception:  # noqa: BLE001
        return {"checkable": False, "note": f"cell {cell} missing"}
    if cv is None or bv is None:
        return {"checkable": False, "note": f"cell {cell} missing"}
    t = target.lower()
    wants_down = any(w in t for w in ("lower", "reduce", "down", "less", "smaller", "decrease", "flatten"))
    wants_up = any(w in t for w in ("raise", "increase", "up", "more", "higher", "sharpen"))
    moved = (cv - bv) / (abs(bv) + 1e-9)
    ok = None
    if wants_down:
        ok = moved < -0.02
    elif wants_up:
        ok = moved > 0.02
    return {"checkable": ok is not None, "cell": cell, "candidate": cv, "baseline": bv, "relative_change": round(moved, 4), "ok": ok}


def markdown(d: dict) -> str:
    L = [f"# How the baseline behaves ({d['steps']} steps, seed {d['seed']}, measured {d['ts']})", ""]
    L += [f"- {s}" for s in statements(d)]
    last = d["probes"][-1]
    L += ["", f"| layer | grad norm attn | grad norm mlp | output RMS | attention entropy |", "|---|---|---|---|---|"]
    for l in last["layers"]:
        L.append(f"| {l['layer']} | {l['grad_attn']} | {l['grad_mlp']} | {l['act_rms']} | {l['attn_entropy']} |")
    curve = d["loss_curve"]
    pts = [0, len(curve) // 4, len(curve) // 2, 3 * len(curve) // 4, len(curve) - 1]
    L += ["", "loss curve: " + ", ".join(f"step {p + 1}: {curve[p]}" for p in pts if 0 <= p < len(curve))]
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--steps", type=int, default=100)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--script", default=None, help="diagnose this candidate script instead of the baseline")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    _load()
    if a.script:
        load_script(a.script)
    d = diagnose(a.steps, a.seed)
    (out / "diagnostics.json").write_text(json.dumps(d, indent=1), encoding="utf-8")
    (out / "diagnostics.md").write_text(markdown(d), encoding="utf-8")
    print((out / "diagnostics.md").read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
