"""The exam, owned by the harness. A candidate trains and saves its weights; this script loads the
candidate's model code and the saved weights, and computes plain next-token cross entropy on the
validation split with the harness's own loader, at a fixed window length, on the same tokens for
every candidate. The candidate's own evaluate() is never trusted: whatever it reported is compared
with this number and a mismatch fails the candidate.

Usage:
  python -I nano/exam.py --candidate cands/src/X.py --ckpt rung5/X/seed0/model.pt --out rung5/X/seed0
Writes <out>/exam.json: {val_loss, val_bpb, n_tokens, seq_len, self_report, mismatch, error}.
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


def load_candidate(path: Path):
    spec = importlib.util.spec_from_file_location("htsa_candidate", str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["htsa_candidate"] = mod
    spec.loader.exec_module(mod)          # defines classes; main() is not run (name != __main__)
    return mod


def val_windows(seq_len: int = EXAM_SEQ_LEN, n_tokens: int = EXAM_TOKENS, batch: int = EXAM_BATCH):
    d = np.memmap(DATA_FULL / "val.bin", dtype=np.uint16, mode="r")
    pos, seen = 0, 0
    while seen + seq_len <= n_tokens and pos + seq_len * batch + 1 <= len(d):
        xs, ys = [], []
        for _ in range(batch):
            xs.append(d[pos: pos + seq_len].astype(np.int64))
            ys.append(d[pos + 1: pos + seq_len + 1].astype(np.int64))
            pos += seq_len
        seen += seq_len * batch
        yield torch.from_numpy(np.stack(xs)), torch.from_numpy(np.stack(ys))


@torch.no_grad()
def run_exam(candidate: Path, ckpt: Path) -> dict:
    mod = load_candidate(candidate)
    saved = torch.load(ckpt, map_location="cpu", weights_only=True)   # tensors and plain containers only
    cfg = mod.Config(**saved["config"])
    model = mod.GPT(cfg)
    missing, unexpected = model.load_state_dict(saved["state_dict"], strict=False)
    if missing or unexpected:
        return {"error": f"state dict mismatch: missing {list(missing)[:5]} unexpected {list(unexpected)[:5]}"}
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device).eval()
    dtype = torch.bfloat16 if str(getattr(cfg, "dtype", "bfloat16")) == "bfloat16" else torch.float16
    losses, n = [], 0
    for x, y in val_windows():
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
    return {"val_loss": round(val, 4), "val_bpb": round(val / math.log(2) * BYTES_PER_TOKEN, 4),
            "n_tokens": n, "seq_len": EXAM_SEQ_LEN, "batches": len(losses)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", required=True)
    ap.add_argument("--ckpt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--self-report", default=None, help="metrics.json written by the candidate (optional)")
    ap.add_argument("--tolerance", type=float, default=0.02)
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    try:
        res = run_exam(Path(a.candidate), Path(a.ckpt))
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
        except Exception:  # noqa: BLE001
            pass
    (out / "exam.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps(res))
    return 0 if "error" not in res else 1


if __name__ == "__main__":
    raise SystemExit(main())
