"""The exam, owned by the harness. A candidate trains and saves its weights; this script loads the
candidate's model code and the saved weights, and computes plain next-token cross entropy on the
validation split with the harness's own loader, at a fixed window length, on the same tokens for
every candidate. The candidate's own evaluate() is never trusted: whatever it reported is compared
with this number and a mismatch fails the candidate.

Usage:
  python -I nano/exam.py --candidate cands/src/X.py --ckpt rung5/X/seed0/model.pt --out rung5/X/seed0
Writes <out>/exam.json: {val_loss, val_bpb, n_tokens, seq_len, self_report, mismatch, params_nonembed,
params_base, params_reported, error}.
The exam reads its validation windows into memory first and then seals the data (sys.audit("htsa.seal"):
under nano/launch.py no later read of the data folder is allowed), so the candidate's model code, loaded
after the seal, cannot read the validation split. It also recounts the non-embedding parameters from the
loaded weights (not from the candidate's report): over the baseline by more than PARAM_TOL, or more than
2% away from what the run reported, fails the candidate.
Requires the model to expose Config(**saved_config), GPT(cfg) and forward(idx) -> logits or
(logits, ...), with logits of shape [batch, seq, vocab >= 50257].
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import os
import sys
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

LAB = Path(os.environ.get("HTSA_LAB_ROOT", r"D:\AGI-lab"))
DATA_FULL = LAB / "data" / "fineweb"
EXAM_SEQ_LEN = 1024
EXAM_TOKENS = 2_000_000
EXAM_BATCH = 4
BYTES_PER_TOKEN = 0.2446      # tokens per byte for GPT-2 BPE on English web text (approx), as in train.py
PARAM_TOL = 0.10              # the same cap as rung 1 in nano/check.py: at most +10% non-embedding parameters
REPORT_TOL = 0.02             # a reported parameter count further than this from the recount is a mismatch
BASELINE = Path(__file__).resolve().parent / "train.py"


def load_candidate(path: Path):
    spec = importlib.util.spec_from_file_location("htsa_candidate", str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["htsa_candidate"] = mod
    spec.loader.exec_module(mod)          # defines classes; main() is not run (name != __main__)
    return mod


def val_tokens(seq_len: int = EXAM_SEQ_LEN, n_tokens: int = EXAM_TOKENS) -> np.ndarray:
    """The exam's slice of the validation split, copied into memory (read before the seal)."""
    d = np.memmap(DATA_FULL / "val.bin", dtype=np.uint16, mode="r")
    need = min(len(d), n_tokens + seq_len * EXAM_BATCH + 1)
    return np.array(d[:need])


def val_windows(data: np.ndarray, seq_len: int = EXAM_SEQ_LEN, n_tokens: int = EXAM_TOKENS, batch: int = EXAM_BATCH):
    d = data
    pos, seen = 0, 0
    while seen + seq_len <= n_tokens and pos + seq_len * batch + 1 <= len(d):
        xs, ys = [], []
        for _ in range(batch):
            xs.append(d[pos: pos + seq_len].astype(np.int64))
            ys.append(d[pos + 1: pos + seq_len + 1].astype(np.int64))
            pos += seq_len
        seen += seq_len * batch
        yield torch.from_numpy(np.stack(xs)), torch.from_numpy(np.stack(ys))


def nonembed_params(model: torch.nn.Module) -> int:
    """The harness's own count: every distinct parameter tensor, minus the token-embedding table (model.tok, as
    train.py's param_counts; else the largest nn.Embedding); a head tied to it is the same tensor and counts
    once, and any other embedding table (a bigram table) is counted, as rung 1 counts it."""
    seen, total = set(), 0
    for p in model.parameters():
        if id(p) not in seen:
            seen.add(id(p))
            total += p.numel()
    tok = getattr(getattr(model, "tok", None), "weight", None)    # the token table, as train.py's param_counts
    if not isinstance(tok, torch.nn.Parameter):          # (protected) counts it; any other table is counted
        tables = [m.weight for m in model.modules() if isinstance(m, torch.nn.Embedding)]
        tok = max(tables, key=lambda w: w.numel()) if tables else None
    return total - (tok.numel() if tok is not None else 0)


def baseline_params(path: Path = BASELINE) -> int:
    """The baseline trainer's count under the same rule, built without memory (meta device)."""
    spec = importlib.util.spec_from_file_location("htsa_exam_baseline", str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["htsa_exam_baseline"] = mod             # dataclasses look the module up while defining Config
    spec.loader.exec_module(mod)
    try:
        with torch.device("meta"):
            model = mod.GPT(mod.Config())
    except Exception:  # noqa: BLE001
        model = mod.GPT(mod.Config())
    return nonembed_params(model)


@torch.no_grad()
def run_exam(candidate: Path, ckpt: Path, params_base: int | None = None) -> dict:
    data = val_tokens()
    if params_base is None:
        params_base = baseline_params()
    sys.audit("htsa.seal")                # from here on the data folder is closed (nano/launch.py)
    mod = load_candidate(candidate)
    saved = torch.load(ckpt, map_location="cpu", weights_only=True)   # tensors and plain containers only
    cfg = mod.Config(**saved["config"])
    model = mod.GPT(cfg)
    missing, unexpected = model.load_state_dict(saved["state_dict"], strict=False)
    if missing or unexpected:
        return {"error": f"state dict mismatch: missing {list(missing)[:5]} unexpected {list(unexpected)[:5]}"}
    recount = nonembed_params(model)
    if recount > params_base * (1 + PARAM_TOL):
        return {"error": f"the weights hold {recount:,} non-embedding parameters, {recount / params_base - 1:+.1%} over the "
                f"baseline's {params_base:,}; at most +{PARAM_TOL:.0%} is allowed", "params_nonembed": recount,
                "params_base": params_base}
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device).eval()
    dtype = torch.bfloat16 if str(getattr(cfg, "dtype", "bfloat16")) == "bfloat16" else torch.float16
    losses, n = [], 0
    for x, y in val_windows(data):
        x, y = x.to(device), y.to(device)
        with torch.autocast("cuda", dtype=dtype, enabled=(device == "cuda")):
            out = model(x)
        logits = out[0] if isinstance(out, (tuple, list)) else out
        if logits.shape[-1] < 50257 or logits.shape[:2] != x.shape:
            return {"error": f"logits of shape {tuple(logits.shape)} are not a distribution over the vocabulary"}
        loss = F.cross_entropy(logits.float().reshape(-1, logits.shape[-1]), y.reshape(-1))
        losses.append(loss.item())
        n += y.numel()
    if not losses:
        return {"error": "no validation windows"}
    val = float(np.mean(losses))
    if not math.isfinite(val):                # a NaN loss would also slip past the self-report comparison
        return {"error": f"the validation loss is {val} (not a finite number)", "params_nonembed": recount,
                "params_base": params_base}
    return {"val_loss": round(val, 4), "val_bpb": round(val / math.log(2) * BYTES_PER_TOKEN, 4),
            "n_tokens": n, "seq_len": EXAM_SEQ_LEN, "batches": len(losses), "params_nonembed": recount,
            "params_base": params_base}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", required=True)
    ap.add_argument("--ckpt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--self-report", default=None, help="metrics.json written by the candidate (optional)")
    ap.add_argument("--tolerance", type=float, default=0.02)
    ap.add_argument("--params-base", type=int, default=None, help="baseline non-embedding parameters (default: count nano/train.py)")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    try:
        res = run_exam(Path(a.candidate), Path(a.ckpt), a.params_base)
    except Exception as e:  # noqa: BLE001
        res = {"error": f"{type(e).__name__}: {str(e)[:300]}"}
    rep = Path(a.self_report) if a.self_report else (Path(a.ckpt).parent / "metrics.json")
    if rep.exists():
        try:
            m = json.loads(rep.read_text(encoding="utf-8"))
            res["self_report"] = m.get("val_loss")
            res["tokens_reported"] = m.get("tokens")
            if res.get("val_loss") is not None and m.get("val_loss") is not None:
                res["mismatch"] = abs(float(m["val_loss"]) - res["val_loss"]) > a.tolerance
            res["params_reported"] = m.get("params_nonembed")
            if res.get("params_nonembed") is not None and m.get("params_nonembed") is not None and                     abs(float(m["params_nonembed"]) - res["params_nonembed"]) > REPORT_TOL * res["params_nonembed"]:
                res["error"] = (f"the run reported {int(m['params_nonembed']):,} non-embedding parameters; the weights "
                                f"hold {res['params_nonembed']:,}")
        except Exception:  # noqa: BLE001
            pass
    (out / "exam.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps(res))
    return 0 if "error" not in res else 1


if __name__ == "__main__":
    raise SystemExit(main())
