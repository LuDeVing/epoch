"""Rung 0 of the checker: does a candidate change only what its part is allowed to change?

The builder is told "code this change may touch: <boundary>; everything outside it stays identical".
This module makes that sentence a test. Both files are parsed; every top-level function, class and
method is compared by its normalised source (comments, docstrings and formatting ignored; a class
also by its bases, keywords and decorators, a function by its decorators). Each changed symbol
must be covered by the boundary text, by the wiring allowance (adding a config field or wiring a new
module into GPT/Block), or be a new name. A fixed protected set can never change: it is the exam and
the data loader. New imports must come from the standard library, torch or numpy (constraint C6).
Changed and new code (module level included) may not add: a forbidden call, a way around the
import rule or the launcher's stubs (sys.modules, __import__, __builtins__, from os import system,
getattr on a module with a computed name), frame or garbage-collector introspection, torch.from_file,
or a reference to the validation split, also when the name is built from pieces ('va' + 'l').
This is a sieve, not a proof: nano/launch.py enforces the same rules at run time.

Result: {"ok": bool, "changed": [...], "added": [...], "removed": [...], "violations": [...],
         "bad_imports": [...]}; violations are human-readable lines that go straight into the
revision feedback.
"""
from __future__ import annotations

import ast
import copy
import re
from collections import Counter
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
VAL_WORD = re.compile(r"(?i)(^|[^a-z0-9_])val(\.bin|[^a-z0-9_]|$)")
# attribute names that reach processes, raw memory, the hook's frames or an unaudited file read
RISKY_ATTRS = {"system", "popen", "startfile", "execv", "execve", "execl", "execle", "execlp", "execvp", "execvpe",
               "spawnl", "spawnv", "spawnve", "spawnlp", "spawnvp", "posix_spawn", "fork", "forkpty", "kill", "killpg",
               "__import__", "__builtins__", "__subclasses__", "__globals__", "__closure__", "__code__", "cell_contents",
               "f_globals", "f_locals", "f_back", "tb_frame", "gi_frame", "_getframe", "settrace", "setprofile",
               "addaudithook", "get_objects", "get_referrers", "get_referents", "from_file", "_C", "monitoring"}
RISKY_NAMES = {"__import__", "__builtins__", "exec", "eval", "compile", "globals", "breakpoint"}
# getattr/setattr on these with a computed name is a way around the static check
MODULE_NAMES = {"os", "sys", "builtins", "nt", "posix", "io", "gc", "mmap", "torch", "np", "numpy", "importlib",
                "subprocess", "socket", "ctypes", "shutil", "runpy", "inspect", "types"}


def _strip_docstrings(tree: ast.AST) -> ast.AST:
    """Docstrings are documentation: an edit to one is not a change to the code."""
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            body = node.body
            if body and isinstance(body[0], ast.Expr) and isinstance(getattr(body[0], "value", None), ast.Constant) \
                    and isinstance(body[0].value.value, str):
                node.body = body[1:] or [ast.Pass()]
    return tree


def symbols(src: str) -> dict[str, str]:
    """Map 'name' or 'Class.method' -> normalised source; '<module>' holds the other top-level statements.
    A class's entry holds its header (bases, keywords, decorators) and its non-method statements."""
    tree = _strip_docstrings(ast.parse(src))
    out: dict[str, str] = {}
    other: list[str] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out[node.name] = ast.unparse(node)                 # decorators included
        elif isinstance(node, ast.ClassDef):
            body_other = []
            for sub in node.body:
                if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    out[f"{node.name}.{sub.name}"] = ast.unparse(sub)
                else:
                    body_other.append(ast.unparse(sub))
            header = copy.copy(node)
            header.body = [ast.Pass()]
            out[node.name] = "\n".join([ast.unparse(header)] + body_other)   # bases, decorators, class-level fields
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


def _fold(node: ast.AST) -> str | None:
    """A string the code builds from constants ('va' + 'l', f'{x}/val.bin' parts, ''.join([...]))."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Mod)):
        a, b = _fold(node.left), _fold(node.right)
        if a is not None or b is not None:
            return (a or "") + (b or "")
    if isinstance(node, ast.JoinedStr):
        return "".join(v.value for v in node.values if isinstance(v, ast.Constant) and isinstance(v.value, str)) or None
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "join" and node.args \
            and isinstance(node.args[0], (ast.List, ast.Tuple)):
        parts = [_fold(e) for e in node.args[0].elts]
        if any(x is not None for x in parts):
            return "".join(x or "" for x in parts)
    return None


def _root_name(node: ast.AST) -> str | None:
    while isinstance(node, ast.Attribute):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def risky(src: str) -> list[str]:
    """Findings (with repeats) for one symbol's source: ways around the import rule, the stubs or the
    audit hook, and references to the validation split. Docstrings are not code and are skipped."""
    try:
        tree = _strip_docstrings(ast.parse(src))
    except SyntaxError:
        return []
    out: list[str] = []
    inner: set[int] = set()                              # parts of a larger folded string: counted once, on the whole
    for node in ast.walk(tree):                          # breadth first: a whole expression comes before its parts
        if isinstance(node, ast.ImportFrom) and node.module:
            for al in node.names:
                if al.name in RISKY_ATTRS or al.name == "*":
                    out.append(f"imports {al.name} from {node.module}")
        elif isinstance(node, ast.Attribute):
            if node.attr in RISKY_ATTRS:
                out.append(f"uses .{node.attr}")
            elif node.attr == "modules" and _root_name(node.value) == "sys":
                out.append("uses sys.modules")
        elif isinstance(node, ast.Name) and node.id in RISKY_NAMES:
            out.append(f"uses {node.id}")
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("getattr", "setattr", "delattr", "hasattr") \
                and len(node.args) >= 2:
            name = node.args[1]
            target = _root_name(node.args[0])
            if isinstance(name, ast.Constant) and isinstance(name.value, str):
                if name.value in RISKY_ATTRS or (name.value == "modules" and target == "sys"):
                    out.append(f"{node.func.id} of {name.value}")
            elif target in MODULE_NAMES:
                out.append(f"{node.func.id} on the module {target} with a computed name")
        if id(node) in inner or not isinstance(node, (ast.Constant, ast.BinOp, ast.JoinedStr, ast.Call)):
            continue
        folded = _fold(node)
        if folded is None:
            continue
        if not isinstance(node, ast.Constant):
            inner.update(id(c) for c in ast.walk(node) if c is not node)
        if VAL_WORD.search(folded):
            out.append("val")
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
    # dangerous calls, ways around the sandbox and validation-split references anywhere in changed or new
    # code, module level included; only NEW findings count (main() already calls the exam once)
    for k in changed + added:
        src_k = cand.get(k, "")
        calls = dangerous_calls(src_k)
        for call in calls:
            violations.append(f"{k} calls {call}, which is not allowed")
        if k in PROTECTED:
            continue
        new = Counter(risky(src_k)) - Counter(risky(base.get(k, "")))
        val_new = new.pop("val", 0) or len(VAL_RE.findall(src_k)) > len(VAL_RE.findall(base.get(k, "")))
        if val_new:
            violations.append(f"{k} adds a reference to the validation split or the exam; training code may not touch either")
        for what in new:
            if what.startswith("uses ") and what[5:] in calls:
                continue                                   # already reported as a call
            violations.append(f"{k} {what}, which is a way around the sandbox and is not allowed")
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
