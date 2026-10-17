"""Refresh the frontier digest: what the strongest open language models do now, written by the research model
with web search, as facts with sources. The digest goes in front of every idea context (nano/loop.py), so it is
kept short. One research call, about 0.6M research-model tokens (pages are re-read on every search turn).

    python -m nano.refresh_digest                       # architecture focus, writes nano/docs/frontier_digest.md
    python -m nano.refresh_digest --focus "architecture and training" --out some/other.md

The previous digest, if any, is kept beside the new one as <out>.prev.md.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import time
from pathlib import Path

os.environ.setdefault("HTSA_LAB_ROOT", "D:/AGI-lab")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

HERE = Path(__file__).resolve().parent
DEFAULT_OUT = HERE / "docs" / "frontier_digest.md"

PROMPT = """You are writing a reference digest for engineers who improve a small (21M-parameter, 50M-token) language-model
training recipe. They want to know what the STRONGEST OPEN-WEIGHT language models do right now, so they can port a
component down to their scale or deliberately go past it. Today is {today}.

Search the web. Cover the newest and strongest open-weight models, with special care for the Chinese labs:
DeepSeek, Qwen (Alibaba), Kimi (Moonshot), GLM (Zhipu / Z.ai), MiniMax, Xiaomi MiMo, Tencent Hunyuan, ByteDance Seed,
StepFun, InternLM, Baichuan, and also Meta Llama, Mistral, OpenAI gpt-oss, Google Gemma, NVIDIA Nemotron, Allen AI OLMo,
and any model released in the last few months that beats them on open benchmarks. Prefer technical reports, model cards and
papers over news. Focus: {focus}.

Write the digest between the lines DIGEST BEGIN and DIGEST END, in markdown, AT MOST 60 lines, as follows:
1. A first line: "As of {today}. Sources: ..." naming the main reports with their dates.
2. "## The strongest open models now": one line per model, newest first (name, lab, date, size and active parameters,
   the one or two things it does differently), at most 12 models.
3. "## Components, with measured effects": one line per component (attention variant, mixture-of-experts design and
   routing, normalisation and residual scheme, embeddings and output head, positional scheme, depth tricks such as
   layer sharing or parallel blocks, multi-token prediction, long-context tricks, anything else structural), each line
   giving: what it is, which models use it, the measured effect where a report states one, and one source URL.
4. "## Not settled": five or fewer lines on what the reports disagree about or leave open.
Facts only, no advice, no copying of marketing claims; a number must come from a report. Every line with a claim ends
with a source URL in parentheses. Do not include anything you could not find a source for.
"""


def main() -> int:
    from harness import llm
    from nano import research
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="sonnet", help="the research model (retrieval, not invention)")
    ap.add_argument("--backend", default="cli_json")
    ap.add_argument("--focus", default="architecture only: what is computed per token, how tokens mix, how depth composes, "
                                       "inputs and outputs; skip optimisers, data mixtures, post-training and RL")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    a = ap.parse_args()
    out = Path(a.out)
    today = time.strftime("%Y-%m-%d")
    log_dir = Path(os.environ["HTSA_LAB_ROOT"]) / "memory" / "digest" / "calls"
    log_dir.mkdir(parents=True, exist_ok=True)
    r = llm.call(PROMPT.format(today=today, focus=a.focus), role="research", call_id=f"digest_{int(time.time())}",
                 model=a.model, max_tokens=6000, backend=a.backend, log_dir=log_dir,
                 meta={"card": "digest", "note": "frontier digest refresh"},
                 tools=research.RESEARCH_TOOLS, max_turns=40, timeout=1800)
    text = r.text or ""
    m = re.search(r"DIGEST BEGIN\s*\n(.*?)\nDIGEST END", text, flags=re.S)
    body = (m.group(1) if m else text).strip()
    if len(body) < 400:
        print("digest too short; nothing written. Raw reply:\n" + text[:2000])
        return 1
    lines = body.splitlines()
    if len(lines) > 80:
        body = "\n".join(lines[:80])
    if out.exists():
        out.with_suffix(".prev.md").write_text(out.read_text(encoding="utf-8"), encoding="utf-8")
    out.write_text(f"# Frontier digest: what the strongest open language models do now\n\n{body}\n", encoding="utf-8")
    print(f"wrote {out} ({len(body.splitlines())} lines); tokens {r.usage.total_tokens:,} ({a.model})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
