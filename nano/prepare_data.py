"""Prepare the nano training data: a FineWeb-Edu subset tokenized with the GPT-2 BPE.

Streams documents from HuggingFaceFW/fineweb-edu (sample-10BT) so nothing large is downloaded,
tokenizes with tiktoken, and writes uint16 shards:
    D:/AGI-lab/data/fineweb/train_*.bin   (train tokens, 50M per shard)
    D:/AGI-lab/data/fineweb/val.bin       (held-out tokens, fixed)
Each document is followed by the <|endoftext|> token. Deterministic given the stream order.

Usage: python nano/prepare_data.py --train-tokens 120e6 --val-tokens 3e6
"""
from __future__ import annotations

import argparse
import os
import time
from pathlib import Path

import numpy as np

DATA_DIR = Path(os.environ.get("HTSA_LAB_ROOT", r"D:\AGI-lab")) / "data" / "fineweb"
SHARD_TOKENS = 50_000_000


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--train-tokens", type=float, default=120e6)
    ap.add_argument("--val-tokens", type=float, default=3e6)
    ap.add_argument("--dataset", default="HuggingFaceFW/fineweb-edu")
    ap.add_argument("--name", default="sample-10BT")
    args = ap.parse_args()

    import tiktoken
    from datasets import load_dataset

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    enc = tiktoken.get_encoding("gpt2")
    eot = enc.eot_token
    ds = load_dataset(args.dataset, name=args.name, split="train", streaming=True)

    want_val, want_train = int(args.val_tokens), int(args.train_tokens)
    buf: list[int] = []
    n_docs = 0
    t0 = time.time()
    val_done = False
    shard_idx = 0
    written_train = 0

    def flush(path: Path, toks: list[int]) -> None:
        arr = np.asarray(toks, dtype=np.uint16)
        arr.tofile(path)
        print(f"[data] wrote {path.name}: {len(arr):,} tokens", flush=True)

    for doc in ds:
        text = doc.get("text") or ""
        ids = enc.encode_ordinary(text) + [eot]
        buf.extend(ids)
        n_docs += 1
        if not val_done and len(buf) >= want_val:
            flush(DATA_DIR / "val.bin", buf[:want_val])
            buf = buf[want_val:]
            val_done = True
        while val_done and len(buf) >= SHARD_TOKENS and written_train < want_train:
            flush(DATA_DIR / f"train_{shard_idx:03d}.bin", buf[:SHARD_TOKENS])
            buf = buf[SHARD_TOKENS:]
            shard_idx += 1
            written_train += SHARD_TOKENS
        if n_docs % 5000 == 0:
            print(f"[data] {n_docs:,} docs, {written_train + len(buf):,} train tokens buffered, "
                  f"{time.time() - t0:.0f}s", flush=True)
        if val_done and written_train >= want_train:
            break
    if val_done and buf and written_train < want_train:
        remaining = min(len(buf), want_train - written_train)
        flush(DATA_DIR / f"train_{shard_idx:03d}.bin", buf[:remaining])
        written_train += remaining
    print(f"[data] done: {n_docs:,} docs, {written_train:,} train tokens, val {want_val:,}, "
          f"{time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
