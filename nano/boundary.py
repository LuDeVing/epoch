"""Rung 0 of the checker: does a candidate change only what its part is allowed to change?

The builder is told "code this change may touch: <boundary>; everything outside it stays identical".
This module makes that sentence a test. Both files are parsed; every top-level function, class and
method is compared by its normalised source (comments and formatting ignored). Each changed symbol
must be covered by the boundary text, by the wiring allowance (adding a config field or wiring a new
module into GPT/Block), or be a new name. A fixed protected set can never change: it is the exam and
the data loader. New imports must come from the standard library, torch or numpy (constraint C6).

Result: {"ok": bool, "changed": [...], "added": [...], "removed": [...], "violations": [...],
         "bad_imports": [...]}; violations are human-readable lines that go straight into the
revision feedback.
"""
from __future__ import annotations

import ast
import re
import sys

# the exam and the data pipeline: never changed by any part (constraints C1, C2, C6)
PROTECTED = {"evaluate", "Shards.sequential", "Shards.__init__", "param_counts"}
# wiring a new component always needs these; allowed for every part
WIRING = {"Config", "GPT.__init__", "Block.__init__", "<module>"}
ALLOWED_IMPORTS = {"torch", "numpy", "math", "time", "json", "argparse", "dataclasses", "pathlib", "os",
                   "sys", "typing", "functools", "itertools", "collections", "random", "contextlib", "copy",
                   "statistics", "re", "struct", "io", "abc", "enum", "warnings", "inspect", "operator"}
# standard-library modules that give network, process or raw memory access: never, whatever the part
DENIED_IMPORTS = {"socket", "urllib", "http", "ftplib", "smtplib", "telnetlib", "xmlrpc", "requests", "httpx",
                  "aiohttp", "subprocess", "ctypes", "multiprocessing", "importlib", "pty", "ssl", "asyncio",
                  "paramiko", "shutil", "pickle", "marshal", "code", "codeop", "runpy"}
DANGEROUS_CALLS = {"os.system", "os.popen", "os.execv", "os.execl", "os.spawnl", "os.spawnv", "os.startfile",
                   "os.fork", "exec", "eval", "__import__", "compile", "breakpoint"}
VAL_RE = re.compile(r"""val\.bin|["']val["']|Shards\(\s*["']val["']|eval_tokens\s*=|evaluate\(""")


def symbols(src: str) -> dict[str, str]:
    """Map 'name' or 'Class.method' -> normalised source; '<module>' holds the other top-level statements."""
    tree = ast.parse(src)
    out: dict[str, str] = {}
    other: list[str] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out[node.name] = ast.unparse(node)
        elif isinstance(node, ast.ClassDef):
            body_other = []
            for sub in node.body:
                if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    out[f"{node.name}.{sub.name}"] = ast.unparse(sub)
                else:
                    body_other.append(ast.unparse(sub))
            out[node.name] = "\n".join(body_other)            # class-level fields and decorators
        else:
            other.append(ast.unparse(node))
    out["<module>"] = "\n".join(other)
    return out


def imports(src: str) -> set[str]:
    tree = ast.parse(src)
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            mods.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            mods.add(node.module.split(".")[0])
    return mods


def dangerous_calls(src: str) -> list[str]:
    """Names of forbidden calls in a symbol's source (os.system, exec, eval, ...)."""
    out = []
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        f = node.func
        name = None
        if isinstance(f, ast.Name):
            name = f.id
        elif isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name):
            name = f"{f.value.id}.{f.attr}"
        if name in DANGEROUS_CALLS and name not in out:
            out.append(name)
    return out


def _covered(sym: str, boundary_tokens: set[str]) -> bool:
    """A symbol is covered when the boundary names it (qualified) or its whole class; a bare method
    name in the boundary never covers that method on another class."""
    low = sym.lower()
    cls = low.split(".")[0]
    return low in boundary_tokens or cls in boundary_tokens


def check_boundary(baseline_src: str, candidate_src: str, boundary: str | None) -> dict:
    try:
        base, cand = symbols(baseline_src), symbols(candidate_src)
    except SyntaxError as e:
        return {"ok": False, "changed": [], "added": [], "removed": [], "bad_imports": [],
                "violations": [f"candidate does not parse: {e}"]}
    changed = sorted(k for k in base if k in cand and base[k] != cand[k])
    added = sorted(k for k in cand if k not in base)
    removed = sorted(k for k in base if k not in cand)
    stdlib = set(getattr(sys, "stdlib_module_names", set()))
    bad_imports = sorted(m for m in imports(candidate_src)
                         if m in DENIED_IMPORTS or (m not in ALLOWED_IMPORTS and m not in stdlib))
    violations: list[str] = []
    # dangerous calls and validation-split references anywhere in changed or new code
    for k in changed + added:
        src_k = cand.get(k, "")
        for call in dangerous_calls(src_k):
            violations.append(f"{k} calls {call}, which is not allowed")
        if k not in PROTECTED and k != "<module>":
            before = len(VAL_RE.findall(base.get(k, "")))
            if len(VAL_RE.findall(src_k)) > before:        # only NEW references count; main() already calls the exam once
                violations.append(f"{k} adds a reference to the validation split or the exam; training code may not touch either")
    for k in changed + removed:
        if k in PROTECTED:
            violations.append(f"{k} is protected (the exam and the data loader never change)")
    for k in removed:
        if k not in PROTECTED:
            violations.append(f"{k} was removed; the baseline symbol must stay (it may be left unused)")
    low = (boundary or "").strip().lower()
    free = low == "" or low.startswith(("everything", "any part", "all parts", "all ", "any "))
    if not free:
        tokens = {t.strip(".") for t in re.findall(r"[a-z_][a-z0-9_.]*", low)} - {""}
        if "train loop" in low or "training loop" in low or "main(" in low:
            tokens.add("main")                        # the loop lives in main()
        for k in changed:
            if k in PROTECTED or k in WIRING or _covered(k, tokens):
                continue
            violations.append(f"{k} changed but lies outside this part's boundary ({boundary})")
    for m in bad_imports:
        violations.append(f"import of {m} is not allowed (only the standard library, torch and numpy)")
    return {"ok": not violations, "changed": changed, "added": added, "removed": removed,
            "bad_imports": bad_imports, "violations": violations}
