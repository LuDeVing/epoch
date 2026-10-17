"""A computed cost and headroom card for the recipe: where the parameters and the compute go, and how much
room the rules leave. Analytic, from the Config values in the script and the measured profile; no torch.
Shown to every idea agent, interrogator, critic and builder, so "spend the headroom" means a number.
(research_notes/thinking_parts/01_representation.md R1, 04_generation.md G3; creative_genius D2 EXISTENCE.)
"""
from __future__ import annotations

import re

CARD_GB = 6.0


def _val(src: str, field: str) -> float | None:
    m = re.search(rf"^\s+{re.escape(field)}: (?:float|int) = ([0-9.eE+-]+)", src, flags=re.M)
    return float(m.group(1)) if m else None


def breakdown(src: str) -> dict | None:
    """Parameters and forward FLOPs per token by component, from the Config values of a GPT-2-style script."""
    L, d, h, ff, V, T = (_val(src, k) for k in ("n_layer", "d_model", "n_head", "d_ff", "vocab_size", "seq_len"))
    kv = _val(src, "n_kv_head") or h
    if None in (L, d, h, ff, V, T):
        return None
    L, d, h, ff, V, T, kv = int(L), int(d), int(h), int(ff), int(V), int(T), int(kv)
    hd = d // h
    attn_proj = d * d * 2 + 2 * d * (kv * hd)          # q and o full width; k and v at the kv width
    mlp = 3 * d * ff                                   # SwiGLU: gate, up, down
    norms = 2 * d
    per_block = attn_proj + mlp + norms
    params = {"attention projections": L * attn_proj, "feed-forward": L * mlp, "norms": L * norms + d, "embeddings (tied)": V * d}
    nonembed = L * per_block + d
    # forward FLOPs per token: 2 per multiply-add; attention scores and values over the causal half of T
    flops = {"attention projections": L * 2 * attn_proj, "attention scores and values": L * 2 * 2 * (T / 2) * d,
             "feed-forward": L * 2 * mlp, "output head": 2 * d * V}
    total = sum(flops.values())
    return {"n_layer": L, "d_model": d, "n_head": h, "head_dim": hd, "d_ff": ff, "vocab": V, "seq_len": T,
            "params": params, "params_nonembed": nonembed, "per_block": per_block, "attn_proj_per_block": attn_proj,
            "mlp_per_block": mlp, "flops_per_token": flops, "flops_total": total}


def card(src: str, profile: dict | None = None, param_tol: float = 0.10, step_cap: float = 2.0) -> str:
    b = breakdown(src)
    if not b:
        return ""
    prof = profile or {}
    measured = prof.get("params_nonembed")
    step_s = prof.get("step_s")
    vram = prof.get("peak_vram_gb")
    lines = ["COST AND HEADROOM (computed from the script and today's measurements):"]
    p = b["params"]
    lines.append(f"- parameters: {b['params_nonembed']:,} non-embedding (attention projections {p['attention projections']:,}, feed-forward {p['feed-forward']:,}, norms {p['norms']:,}); "
                 f"embeddings {p['embeddings (tied)']:,} tied; one block is {b['per_block']:,} (attention {b['attn_proj_per_block']:,}, feed-forward {b['mlp_per_block']:,})"
                 + (f"; measured {int(measured):,}" if measured else ""))
    f = b["flops_per_token"]
    tot = b["flops_total"]
    lines.append("- forward compute per token: " + ", ".join(f"{k} {100 * v / tot:.0f}%" for k, v in f.items())
                 + f" (shape {b['n_layer']} layers x {b['d_model']} wide, {b['n_head']} heads of {b['head_dim']}, feed-forward {b['d_ff']}, context {b['seq_len']})")
    base_p = int(measured or b["params_nonembed"])
    room = int(base_p * param_tol)
    lines.append(f"- headroom in parameters: +{room:,} ({param_tol:.0%} of the original) before the cap: about {room / b['per_block']:.2f} of a block, "
                 f"or widening the feed-forward by {int(room / (3 * b['d_model'])):,}, or {int(room / (2 * b['d_model'] * b['d_model'])):,} more full-width projections per layer; shrinking is always allowed")
    if step_s:
        lines.append(f"- headroom in time: the step takes {step_s:.2f}s today and may take up to {step_cap * step_s:.2f}s ({step_cap:.0f}x); a change that costs more than that fails the timing check")
    if vram:
        lines.append(f"- headroom in memory: {vram:.2f} GB used of the card's {CARD_GB:.0f} GB; about {max(0.0, CARD_GB - vram - 0.4):.1f} GB free after a safety margin")
    lines.append("- the exam: validation loss at a fixed budget of tokens; a win is at least 0.005 nats below the original over three seeds, a stackable gain at least 0.002")
    return "\n".join(lines)


def interleave_lane(pool: list, is_lane, every: int = 5) -> list:
    """Reserve one slot in every `every` for the best candidate from the ambitious lane, so a lane
    candidate is examined even when it ranks below the safe ones (creative_genius/06, R2)."""
    main = [x for x in pool if not is_lane(x)]
    lane = [x for x in pool if is_lane(x)]
    out = []
    while main or lane:
        for _ in range(every - 1):
            if main:
                out.append(main.pop(0))
        if lane:
            out.append(lane.pop(0))
        elif not main:
            break
    return out
