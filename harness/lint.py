"""Prompt and view lint (ARCHITECTURE.md section 1, Pr10 and Pr5; section 3 /encode step 5).

Patterns live in harness/lint_patterns.yaml: "fail" (personas, stakes, bodily imperatives,
hidden-reasoning wording) and "warn" (be-creative wording). `lint_text` scans any text,
`lint_templates` scans every file in strategies/templates, and `lint_domain` checks a
low_prior view against a per-item domain-noun list.
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

import yaml

from . import config


@lru_cache(maxsize=4)
def _compiled(path: str) -> tuple[tuple[str, str, re.Pattern], ...]:
    """(id, severity, regex) triples from the patterns file (Pr10)."""
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    out = []
    for severity in ("fail", "warn"):
        for row in data.get(severity) or []:
            out.append((row["id"], severity, re.compile(row["pattern"], re.IGNORECASE)))
    return tuple(out)


def patterns(path: Path | None = None) -> tuple:
    return _compiled(str(path or config.LINT_PATTERNS_PATH))


def lint_text(text: str) -> list[dict]:
    """All pattern matches in text: [{pattern, severity, span: [start, end], match}] (Pr10)."""
    found = []
    for pid, severity, rx in patterns():
        for m in rx.finditer(text or ""):
            found.append({"pattern": pid, "severity": severity,
                          "span": [m.start(), m.end()], "match": m.group(0)})
    found.sort(key=lambda f: f["span"][0])
    return found


def lint_templates(templates_dir: Path | None = None) -> dict:
    """Lint every template file: {"fails": [...], "warns": [...]}, each finding tagged with file."""
    d = Path(templates_dir or config.TEMPLATES_DIR)
    fails, warns = [], []
    for p in sorted(d.glob("*.txt")):
        for f in lint_text(p.read_text(encoding="utf-8")):
            f = dict(f, file=p.name)
            (fails if f["severity"] == "fail" else warns).append(f)
    return {"fails": fails, "warns": warns}


def noun_regex(noun: str) -> re.Pattern:
    """Word-boundary, case-insensitive match of a noun and its simple plural (REP-02)."""
    return re.compile(r"\b" + re.escape(noun) + r"(?:s|es)?\b", re.IGNORECASE)


def lint_domain(text: str, nouns: list[str]) -> list[dict]:
    """Domain nouns still present in a low_prior view (Pr5: no domain cues, script-linted)."""
    found = []
    for noun in nouns:
        for m in noun_regex(noun).finditer(text or ""):
            found.append({"pattern": f"domain_noun:{noun}", "severity": "fail",
                          "span": [m.start(), m.end()], "match": m.group(0)})
    return found


def main() -> int:
    """python -m harness.lint: lint all templates; exit 1 on any fail."""
    res = lint_templates()
    for f in res["fails"] + res["warns"]:
        print(f"{f['severity']}\t{f['file']}\t{f['pattern']}\t{f['match']}")
    return 1 if res["fails"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
