"""Prompt and view lint (ARCHITECTURE.md section 1, Pr10 and Pr5; section 3 /encode step 5).

Patterns live in harness/lint_patterns.yaml: "fail" (personas, stakes, bodily imperatives,
hidden-reasoning wording, creativity instructions) and "warn" (step-by-step boilerplate).
`lint_text` scans any text, `lint_templates` scans every file in strategies/templates, and
`lint_domain` checks a low_prior view or prompt against the original item's domain nouns.

The domain lint does not share its matcher with encode.neutralize: neutralize generates the
surface forms of each noun and substitutes them; the lint splits the rendered text into words
and maps each word back to its candidate base forms (regular and irregular plurals,
possessives), so a form or a text field that neutralize missed is still caught.
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


# irregular plurals (singular -> plural); "-man" compounds and the f/fe/y rules are handled by rule
IRREGULAR_PLURALS = {
    "man": "men", "woman": "women", "child": "children", "person": "people", "foot": "feet",
    "tooth": "teeth", "mouse": "mice", "goose": "geese", "ox": "oxen", "louse": "lice",
    "die": "dice", "cactus": "cacti", "fungus": "fungi", "nucleus": "nuclei", "radius": "radii",
    "criterion": "criteria", "phenomenon": "phenomena", "index": "indices", "matrix": "matrices",
    "vertex": "vertices", "analysis": "analyses", "axis": "axes", "crisis": "crises",
    "thesis": "theses", "medium": "media", "bacterium": "bacteria",
}
_SINGULAR_OF = {v: k for k, v in IRREGULAR_PLURALS.items()}
_VOWELS = set("aeiou")
_WORD = re.compile(r"[A-Za-z]+")


def plural_forms(word: str) -> set[str]:
    """Lower-case surface forms of one noun: itself, regular plurals and irregular plurals."""
    w = word.lower()
    forms = {w, w + "s", w + "es"}
    if w in IRREGULAR_PLURALS:
        forms.add(IRREGULAR_PLURALS[w])
    if w.endswith("man"):
        forms.add(w[:-3] + "men")
    if len(w) > 1 and w.endswith("y") and w[-2] not in _VOWELS:
        forms.add(w[:-1] + "ies")
    if w.endswith("fe"):
        forms.add(w[:-2] + "ves")
    elif w.endswith("f"):
        forms.add(w[:-1] + "ves")
    return forms


def base_forms(token: str) -> set[str]:
    """Candidate base forms of one word as written (the inverse direction of plural_forms)."""
    t = token.lower()
    out = {t}
    if t in _SINGULAR_OF:
        out.add(_SINGULAR_OF[t])
    if t.endswith("men"):
        out.add(t[:-3] + "man")
    if t.endswith("ies"):
        out.add(t[:-3] + "y")
    if t.endswith("ves"):
        out |= {t[:-3] + "f", t[:-3] + "fe"}
    if t.endswith("es"):
        out.add(t[:-2])
    if t.endswith("s") and not t.endswith("ss"):
        out.add(t[:-1])
    return out


def noun_forms(noun: str) -> set[str]:
    """Surface forms of a (possibly multi-word) noun; only the last word is inflected. A noun
    listed in a plural form ("cities") also yields its singular and the singular's plurals."""
    words = noun.lower().split()
    if not words:
        return set()
    head, last = words[:-1], words[-1]
    lasts: set[str] = set()
    for b in (base_forms(last) if len(last) > 3 else {last}):
        lasts |= plural_forms(b)
    return {" ".join(head + [x]) for x in lasts}


def noun_regex(noun: str) -> re.Pattern:
    """Word-boundary, case-insensitive match of every surface form of a noun (REP-02). Used by
    encode.neutralize to substitute; lint_domain checks by base forms instead."""
    alts = sorted(noun_forms(noun), key=len, reverse=True)
    body = "|".join(r"\s+".join(re.escape(p) for p in a.split()) for a in alts)
    return re.compile(r"\b(?:" + body + r")\b", re.IGNORECASE)


def lint_domain(text: str, nouns: list[str]) -> list[dict]:
    """Domain nouns still present in a low_prior view or prompt (Pr5: no domain cues,
    script-linted). Single-word nouns: each word of the text is mapped to its base forms and
    compared with the noun's base forms. Multi-word nouns: phrase match."""
    found = []
    single: dict[str, str] = {}
    for noun in nouns:
        n = " ".join(str(noun).lower().split())
        if not n:
            continue
        if " " in n:
            for m in noun_regex(n).finditer(text or ""):
                found.append({"pattern": f"domain_noun:{n}", "severity": "fail",
                              "span": [m.start(), m.end()], "match": m.group(0)})
            continue
        for b in base_forms(n) if len(n) > 3 else {n}:
            single.setdefault(b, n)
    for m in _WORD.finditer(text or ""):
        hit = next((single[b] for b in sorted(base_forms(m.group(0))) if b in single), None)
        if hit:
            found.append({"pattern": f"domain_noun:{hit}", "severity": "fail",
                          "span": [m.start(), m.end()], "match": m.group(0)})
    found.sort(key=lambda f: f["span"][0])
    return found


def main() -> int:
    """python -m harness.lint: lint all templates; exit 1 on any fail."""
    res = lint_templates()
    for f in res["fails"] + res["warns"]:
        print(f"{f['severity']}\t{f['file']}\t{f['pattern']}\t{f['match']}")
    return 1 if res["fails"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
