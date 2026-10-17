"""Generate text from a trained candidate: load its script and weights, tokenize a prompt with the GPT-2 tokenizer,
sample with temperature and top-k. A 21M-parameter model trained on 50M tokens writes like a model that size: it
completes phrases and keeps a topic for a sentence or two; it does not answer questions.

    python -m nano.sample --script llmcandidates/strongest_plus_ours.py \
        --ckpt D:/AGI-lab/runs/hand/ref/strongest_plus_ours/seed0/model.pt --prompt "The history of Rome" --tokens 80
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

import torch
import torch.nn.functional as F


def load(script: Path, ckpt: Path, device):
    spec = importlib.util.spec_from_file_location("sample_mod", script)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["sample_mod"] = mod
    spec.loader.exec_module(mod)
    ck = torch.load(ckpt, map_location="cpu")
    cfg = mod.Config(**{k: v for k, v in ck["config"].items() if k in mod.Config.__dataclass_fields__})
    model = mod.GPT(cfg)
    model.load_state_dict(ck["state_dict"])
    return model.to(device).eval(), cfg


@torch.no_grad()
def generate(model, idx, n_tokens: int, temperature: float, top_k: int, seq_len: int):
    for _ in range(n_tokens):
        ctx = idx[:, -seq_len:]
        logits, _ = model(ctx)
        logits = logits[:, -1, :].float() / max(1e-4, temperature)
        if top_k:
            v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
            logits[logits < v[:, [-1]]] = float("-inf")
        probs = F.softmax(logits, dim=-1)
        nxt = torch.multinomial(probs, num_samples=1)
        idx = torch.cat([idx, nxt], dim=1)
    return idx


def main() -> int:
    import tiktoken
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", required=True)
    ap.add_argument("--ckpt", required=True)
    ap.add_argument("--prompt", default="The")
    ap.add_argument("--tokens", type=int, default=80)
    ap.add_argument("--temperature", type=float, default=0.8)
    ap.add_argument("--top-k", type=int, default=50)
    ap.add_argument("--samples", type=int, default=1)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    a = ap.parse_args()
    torch.manual_seed(a.seed)
    device = torch.device(a.device)
    model, cfg = load(Path(a.script), Path(a.ckpt), device)
    enc = tiktoken.get_encoding("gpt2")
    ids = torch.tensor([enc.encode(a.prompt)], dtype=torch.long, device=device)
    for i in range(a.samples):
        out = generate(model, ids, a.tokens, a.temperature, a.top_k, cfg.seq_len)
        text = enc.decode(out[0].tolist())
        print(f"--- sample {i + 1} ---\n{text}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
