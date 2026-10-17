"""Mechanism tests that need no training: do the two new ideas (the gain-tied input lookup and the
magnitude-as-temperature final norm) have the lever they assume, and does the trained combined model use them?

Three kinds of test, all on saved weights and held-out text, minutes on a CPU:
  premise   on the trained BASELINE: does the final norm's gain drift from one (the tying idea's lever)? does a
            token's residual magnitude predict how hard the token is (the temperature idea's lever)?
  post-hoc  on the trained BASELINE: fit the temperature's two parameters after training, on one half of the
            held-out text, and measure the loss on the other half: a direct effect test with no retraining.
  lesion    on the trained COMBINED model: switch one mechanism off at a time and measure how much loss the model
            loses: how much it came to rely on each part (reliance, not the counterfactual gain).

    python -m nano.mechanism_tests --combined-script llmcandidates/combined_all.py \
        --combined-ckpt D:/AGI-lab/runs/arch-2__nano__gpt2_50m__scaffold__r0/rung5/combined_all/seed0/model.pt \
        --baseline-ckpt D:/AGI-lab/runs/nano_baseline_full/v1/seed0/model.pt --tokens 262144 --device cpu
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import os
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

os.environ.setdefault("HTSA_LAB_ROOT", "D:/AGI-lab")
ROOT = Path(__file__).resolve().parent.parent
LAB = Path(os.environ["HTSA_LAB_ROOT"])


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def load_model(script: Path, ckpt: Path, name: str, device):
    mod = load_module(script, name)
    ck = torch.load(ckpt, map_location="cpu")
    cfg = mod.Config(**{k: v for k, v in ck["config"].items() if k in mod.Config.__dataclass_fields__})
    model = mod.GPT(cfg)
    model.load_state_dict(ck["state_dict"])
    model.to(device).eval()
    return mod, cfg, model


def val_windows(n_tokens: int, seq_len: int = 1024, offset: int = 0):
    data = np.memmap(LAB / "data" / "fineweb" / "val.bin", dtype=np.uint16, mode="r")
    n = n_tokens // seq_len
    xs, ys = [], []
    for i in range(n):
        s = offset + i * seq_len
        xs.append(np.asarray(data[s: s + seq_len], dtype=np.int64))
        ys.append(np.asarray(data[s + 1: s + seq_len + 1], dtype=np.int64))
    return torch.from_numpy(np.stack(xs)), torch.from_numpy(np.stack(ys))


def token_losses(logits, y):
    return F.cross_entropy(logits.float().view(-1, logits.size(-1)), y.view(-1), reduction="none").view(y.shape)


# ---------------------------------------------------------------- forwards with switches
def baseline_pieces(mod, model, cfg, idx):
    """The baseline forward split open: the residual stream before the final norm, and the logits."""
    B, T = idx.shape
    cos, sin = mod.rope_cache(T, cfg.d_model // cfg.n_head, cfg.rope_theta, idx.device)
    x = model.tok(idx)
    for b in model.blocks:
        x = b(x, cos, sin)
    return x, model.head(model.norm(x))


def combined_forward(mod, model, cfg, idx, tying=True, temperature=True, bigram=True, second_pass=True, lens=True,
                     docpos=True):
    """combined_all.py's forward with each mechanism switchable (mirrors its GPT.forward)."""
    B, T = idx.shape
    cos, sin = mod.rope_cache(T, cfg.d_model // cfg.n_head, cfg.rope_theta, idx.device)
    if docpos:
        t = torch.arange(T, device=idx.device).view(1, T)
        starts = torch.where(idx == 50256, t + 1, torch.zeros_like(t))
        starts = F.pad(starts[:, :-1], (1, 0)).cummax(dim=1)[0]
        positions = t - starts
        cos, sin = cos[positions], sin[positions]
    e = model.tok(idx)
    if tying:
        e = e * model.norm.weight
    x = model.lens(e) if lens else e
    for b in model.blocks:
        x = b(x, cos, sin)
    if second_pass:
        for b in model.blocks[cfg.n_layer // 2:]:
            x = b(x, cos, sin, second_pass=True)
    if temperature:
        h = model.norm(x)
    else:
        h = F.rms_norm(x, (x.size(-1),), model.norm.weight, model.norm.eps)
    if bigram:
        h = h + model.bigram_proj(model.tok2(idx))
    return model.head(h)


def mean_loss(fn, X, Y, bs=8):
    tot, n = 0.0, 0
    with torch.no_grad():
        for i in range(0, X.size(0), bs):
            logits = fn(X[i: i + bs])
            tot += float(token_losses(logits, Y[i: i + bs]).sum())
            n += Y[i: i + bs].numel()
    return tot / n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline-script", default=str(ROOT / "nano" / "train.py"))
    ap.add_argument("--baseline-ckpt", default=str(LAB / "runs" / "nano_baseline_full" / "v1" / "seed0" / "model.pt"))
    ap.add_argument("--combined-script", default=str(ROOT / "llmcandidates" / "combined_all.py"))
    ap.add_argument("--combined-ckpt", default=None)
    ap.add_argument("--tokens", type=int, default=262144)
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    device = torch.device(a.device)
    torch.set_num_threads(max(1, min(8, os.cpu_count() or 1)))
    t0 = time.time()
    report: dict = {"tokens": a.tokens, "device": a.device}
    X, Y = val_windows(a.tokens)
    X, Y = X.to(device), Y.to(device)
    half = X.size(0) // 2

    # ------------------------------------------------ baseline: premises and the post-hoc temperature
    bmod, bcfg, base = load_model(Path(a.baseline_script), Path(a.baseline_ckpt), "mt_base", device)
    g = base.norm.weight.detach().float()
    report["gain_drift"] = {"mean": round(float(g.mean()), 4), "std": round(float(g.std()), 4), "min": round(float(g.min()), 4),
                            "max": round(float(g.max()), 4), "share_outside_0.8_1.2": round(float(((g < 0.8) | (g > 1.2)).float().mean()), 4),
                            "read": "the tying idea needs the gain to leave one; a gain that stays near one gives it nothing to act on"}
    log_rms_all, loss_all = [], []
    with torch.no_grad():
        for i in range(0, X.size(0), 8):
            h, logits = baseline_pieces(bmod, base, bcfg, X[i: i + 8])
            log_rms_all.append(0.5 * (h.float().square().mean(-1) + 1e-6).log())
            loss_all.append(token_losses(logits, Y[i: i + 8]))
    log_rms = torch.cat(log_rms_all)
    tl = torch.cat(loss_all)
    base_loss = float(tl.mean())
    r = torch.corrcoef(torch.stack([log_rms.flatten(), tl.flatten()]))[0, 1]
    q = torch.quantile(log_rms.flatten(), torch.tensor([0.2, 0.4, 0.6, 0.8]))
    bucket = torch.bucketize(log_rms.flatten(), q)
    per_bucket = [round(float(tl.flatten()[bucket == k].mean()), 4) for k in range(5)]
    report["magnitude_premise"] = {"corr_logrms_vs_tokenloss": round(float(r), 4), "mean_loss_by_rms_quintile_low_to_high": per_bucket,
                                   "baseline_loss_on_these_tokens": round(base_loss, 4),
                                   "read": "a token's residual magnitude carries confidence only if the loss moves across the quintiles"}
    # post-hoc two-parameter temperature: fitted by streaming gradient steps on the first half of the windows
    # (the logits of 260k tokens would not fit in memory), tested on the second half
    pa = torch.zeros((), requires_grad=True)
    pb = torch.tensor(math.log(math.expm1(1.0)), requires_grad=True)
    opt = torch.optim.Adam([pa, pb], lr=0.05)
    for epoch in range(6):
        for i in range(0, half, 8):
            with torch.no_grad():
                h, logits = baseline_pieces(bmod, base, bcfg, X[i: i + 8])
                lr_chunk = 0.5 * (h.float().square().mean(-1) + 1e-6).log()
            opt.zero_grad()
            s_ = F.softplus(pa * lr_chunk + pb).unsqueeze(-1)
            loss = token_losses(logits.float() * s_, Y[i: i + 8]).mean()
            loss.backward()
            opt.step()
    before_t, after_t, n_t = 0.0, 0.0, 0
    with torch.no_grad():
        for i in range(half, X.size(0), 8):
            h, logits = baseline_pieces(bmod, base, bcfg, X[i: i + 8])
            lr_chunk = 0.5 * (h.float().square().mean(-1) + 1e-6).log()
            s_ = F.softplus(pa * lr_chunk + pb).unsqueeze(-1)
            before_t += float(token_losses(logits, Y[i: i + 8]).sum())
            after_t += float(token_losses(logits.float() * s_, Y[i: i + 8]).sum())
            n_t += Y[i: i + 8].numel()
    before, after = before_t / n_t, after_t / n_t
    report["posthoc_temperature_on_baseline"] = {"fitted_a": round(float(pa), 4), "fitted_b": round(float(pb), 4),
                                                 "test_half_loss_before": round(before, 4), "test_half_loss_after": round(after, 4),
                                                 "delta": round(after - before, 5),
                                                 "read": "two parameters fitted after training; a negative delta is the effect with no retraining at all"}

    # ------------------------------------------------ combined: learned temperature and lesions
    if a.combined_ckpt:
        cmod, ccfg, comb = load_model(Path(a.combined_script), Path(a.combined_ckpt), "mt_comb", device)
        gc = comb.norm.weight.detach().float()
        report["combined_learned"] = {"temperature_a": round(float(comb.norm.a), 4), "temperature_b": round(float(comb.norm.b), 4),
                                      "temperature_scale_at_unit_rms": round(float(F.softplus(comb.norm.b)), 4),
                                      "gain_std": round(float(gc.std()), 4), "gain_share_outside_0.8_1.2": round(float(((gc < 0.8) | (gc > 1.2)).float().mean()), 4),
                                      "lens_distance_from_identity": round(float((comb.lens.weight.detach().float() - torch.eye(ccfg.d_model)).norm()), 4),
                                      "bigram_table_rms": round(float(comb.tok2.weight.detach().float().pow(2).mean().sqrt()), 5)}
        full = mean_loss(lambda x: combined_forward(cmod, comb, ccfg, x), X, Y)
        lesions = {}
        for name, kw in (("tying_off", {"tying": False}), ("temperature_off", {"temperature": False}), ("bigram_off", {"bigram": False}),
                         ("second_pass_off", {"second_pass": False}), ("lens_off", {"lens": False}), ("docpos_off", {"docpos": False})):
            lesions[name] = round(mean_loss(lambda x, kw=kw: combined_forward(cmod, comb, ccfg, x, **kw), X, Y) - full, 4)
        report["combined_lesions"] = {"full_loss": round(full, 4), "baseline_loss_same_tokens": round(base_loss, 4),
                                      "loss_increase_when_switched_off": lesions,
                                      "read": "how much the trained model relies on each part; large = load-bearing, near zero = the model routes around it"}
    report["wall_s"] = round(time.time() - t0, 1)
    out = Path(a.out) if a.out else LAB / "runs" / "hand" / "mechanism_tests.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=1), encoding="utf-8")
    print(json.dumps(report, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
