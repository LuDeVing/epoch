"""Control candidates: placebos and positive controls that go through the exact ladder (and, on
request, the overnight verdict) so the run reports its own false-positive rate and its power.

Placebo: the baseline recipe with a different data-order seed. It must NOT win; if it ever does, the
ladder or the verdict is calling noise a result.
Positive controls: changes with documented gains at small scale (modded-nanogpt and the gated
attention and QK-norm literature), written against this script. They SHOULD pass the ladder; a
control the ladder rejects is a measured false negative.
Known loser: a change that must fail (learning rate x10). It measures that the ladder rejects harm.

Every control is built from the current baseline text by string substitution, so it follows the
baseline when it is promoted. A substitution that no longer matches makes that control unavailable
(reported, not fatal).
"""
from __future__ import annotations

import re

from nano.ideate import is_llm, vword

# The LLM profile's controls, written against nano/train.py. Another profile may supply its own in vocab "controls"
# (same shape); without them, controls whose anchors do not match its artifact are left out silently.
CONTROLS = {
    "placebo_order": {
        "kind": "placebo", "expect": "pass_ladder_no_win",
        "hypothesis": "control: identical recipe, different data-order seed (placebo)",
        "edits": [('    train = Shards("train", cfg.seq_len, cfg.seed)', '    train = Shards("train", cfg.seq_len, cfg.seed + 7919)')],
        # the seed is changed where the training shards are made, not inside Shards.__init__, which is protected
    },
    "zero_init_proj": {
        "kind": "positive", "expect": "pass_ladder",
        "hypothesis": "control: zero-initialise the two residual-branch output projections (known small gain)",
        "edits": [("            nn.init.normal_(b.attn.wo.weight, std=0.02 / math.sqrt(2 * cfg.n_layer))\n"
                   "            nn.init.normal_(b.mlp.w_down.weight, std=0.02 / math.sqrt(2 * cfg.n_layer))",
                   "            nn.init.zeros_(b.attn.wo.weight)\n            nn.init.zeros_(b.mlp.w_down.weight)")],
    },
    "qk_norm": {
        "kind": "positive", "expect": "pass_ladder",
        "hypothesis": "control: RMSNorm on queries and keys per head before RoPE (QK-norm, known gain)",
        "edits": [("        self.wo = nn.Linear(cfg.n_head * self.hd, cfg.d_model, bias=False)\n        self.window = cfg.sliding_window",
                   "        self.wo = nn.Linear(cfg.n_head * self.hd, cfg.d_model, bias=False)\n        self.window = cfg.sliding_window\n"
                   "        self.qn, self.kn = RMSNorm(self.hd), RMSNorm(self.hd)"),
                  ("        q, k = apply_rope(q, cos, sin), apply_rope(k, cos, sin)",
                   "        q, k = self.qn(q), self.kn(k)\n        q, k = apply_rope(q, cos, sin), apply_rope(k, cos, sin)")],
    },
    "relu2_mlp": {
        "kind": "positive", "expect": "pass_ladder",
        "hypothesis": "control: ReLU-squared MLP with a matched parameter count in place of SwiGLU (known at small scale)",
        "edits": [("        self.w_gate = nn.Linear(cfg.d_model, cfg.d_ff, bias=False)\n"
                   "        self.w_up = nn.Linear(cfg.d_model, cfg.d_ff, bias=False)\n"
                   "        self.w_down = nn.Linear(cfg.d_ff, cfg.d_model, bias=False)",
                   "        hidden = (3 * cfg.d_ff) // 2\n"
                   "        self.w_up = nn.Linear(cfg.d_model, hidden, bias=False)\n"
                   "        self.w_down = nn.Linear(hidden, cfg.d_model, bias=False)"),
                  ("        return self.w_down(F.silu(self.w_gate(x)) * self.w_up(x))",
                   "        return self.w_down(F.relu(self.w_up(x)).square())")],
    },
    "lr_x10": {
        "kind": "loser", "expect": "fail_ladder",
        "hypothesis": "control: learning rate x10 for both optimisers (must fail)",
        "edits": [("    lr: float = 0.02                 # Muon learning rate (matrix params)", "    lr: float = 0.2                 # Muon learning rate (matrix params)"),
                  ("    lr_adam: float = 3e-3            # AdamW learning rate (embeddings, norms)", "    lr_adam: float = 3e-2            # AdamW learning rate (embeddings, norms)")],
    },
}


def table() -> dict:
    """The active profile's controls."""
    c = vword("controls", {})
    return c if isinstance(c, dict) and c else CONTROLS


def _spec(name: str) -> dict:
    return table().get(name) or CONTROLS[name]


def build(baseline_src: str, names: list[str] | None = None) -> dict[str, dict]:
    """Return {name: {"source", "kind", "expect", "hypothesis"}} for every control whose edits apply."""
    out = {}
    tab = table()
    report_missing = tab is not CONTROLS or is_llm()
    for name, spec in tab.items():
        if names and name not in names:
            continue
        src = baseline_src
        ok = True
        for old, new in spec["edits"]:
            if src.count(old) != 1:
                ok = False
                break
            src = src.replace(old, new, 1)
        if not ok:
            if not report_missing:
                continue                                  # the LLM controls on another profile's artifact
            out[name] = {"source": None, "kind": spec["kind"], "expect": spec["expect"], "hypothesis": spec["hypothesis"],
                         "unavailable": "an edit anchor no longer matches the baseline"}
            continue
        out[name] = {"source": src, "kind": spec["kind"], "expect": spec["expect"], "hypothesis": spec["hypothesis"]}
    return out


def judge_overnight(name: str, verdict_status: str | None) -> dict:
    """Did the control behave as it should in the overnight verdict (no ladder there)?"""
    spec = _spec(name)
    v = verdict_status or "none"
    if v in ("error", "none"):
        return {"ok": False, "note": f"control did not complete overnight ({v}); the night itself is suspect"}
    if spec["expect"] == "fail_ladder":
        bad = v in ("verified", "stackable", "close_call", "promising")
        return {"ok": not bad, "note": ("KNOWN LOSER " + v.upper() + ": the verdict is calling a loser a result") if bad else f"loser rejected overnight ({v})"}
    if spec["expect"] == "pass_ladder":
        good = v in ("verified", "stackable", "close_call", "promising")
        return {"ok": good, "note": f"known winner {v} overnight" if good else f"known winner not better overnight ({v}): a measured false negative"}
    bad = v in ("verified", "stackable")
    return {"ok": not bad, "note": f"PLACEBO {v.upper()}: the verdict is calling noise a result" if bad else f"placebo did not win overnight ({v})"}


def judge(name: str, status: str, verdict_status: str | None = None, rung: int | None = None) -> dict:
    """Did the control behave as it should? Returns {"ok", "note"}. A control that fails before the
    learning rung (boundary, build, timing) never tested anything: that is a broken control, not a pass."""
    spec = _spec(name)
    if status != "checked" and rung is not None and rung < 3:
        return {"ok": False, "note": f"control never reached the learning rung (stopped at rung {rung}); the control itself is broken"}
    if spec["expect"] == "fail_ladder":
        return {"ok": status != "checked", "note": "known loser passed the ladder" if status == "checked" else "rejected as it should be"}
    if spec["expect"] == "pass_ladder":
        if status != "checked":
            return {"ok": False, "note": "positive control rejected by the ladder (a false negative)"}
        return {"ok": True, "note": "passed the ladder" + (f"; overnight {verdict_status}" if verdict_status else "")}
    # placebo
    if status != "checked":
        return {"ok": True, "note": f"placebo stopped at the ladder ({status}); fine unless it happens often"}
    if verdict_status in ("verified", "stackable"):
        return {"ok": False, "note": f"PLACEBO {verdict_status.upper()}: the verdict is calling noise a result"}
    return {"ok": True, "note": "placebo passed the ladder and did not win" + (f" ({verdict_status})" if verdict_status else "")}
