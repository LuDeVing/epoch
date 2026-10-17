"""Mechanical composition of two candidates that changed disjoint parts of the script.

The boundary checker already knows which functions, classes and methods each candidate changed. When
two checked candidates touch disjoint sets, their changes can be spliced together by script, at zero
model cost: every top-level symbol comes from whichever candidate changed it (or from the baseline),
new symbols from both are added, new imports are unioned, and class-level fields (Config) are merged
statement by statement. If both changed the same symbol in different ways, there is no mechanical
composite (None): combining them would need a model build, which is not implemented.

compose(baseline_src, a_src, b_src) -> {"source": str, "from_a": [...], "from_b": [...]} | None
"""
from __future__ import annotations

import ast


def _top(src: str) -> tuple[ast.Module, list[tuple[str, ast.AST]]]:
    tree = ast.parse(src)
    items = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            items.append((node.name, node))
        else:
            items.append(("<stmt>", node))
    return tree, items


def _text(src_lines: list[str], node: ast.AST) -> str:
    start = node.lineno - 1
    if getattr(node, "decorator_list", None):
        start = min(d.lineno for d in node.decorator_list) - 1
    return "\n".join(src_lines[start: node.end_lineno])


def _norm(node: ast.AST) -> str:
    return ast.unparse(node)


def _class_parts(node: ast.ClassDef) -> dict[str, ast.AST]:
    out = {}
    for sub in node.body:
        if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out[sub.name] = sub
        elif isinstance(sub, ast.AnnAssign) and isinstance(sub.target, ast.Name):
            out[f"field:{sub.target.id}"] = sub
        elif isinstance(sub, ast.Assign) and len(sub.targets) == 1 and isinstance(sub.targets[0], ast.Name):
            out[f"field:{sub.targets[0].id}"] = sub
        else:
            out[f"stmt:{_norm(sub)[:60]}"] = sub
    return out


def _merge_class(base: ast.ClassDef, a: ast.ClassDef, b: ast.ClassDef, lines_a: list[str], lines_b: list[str],
                 lines_base: list[str]) -> tuple[str | None, list[str], list[str]]:
    """Merge a class part by part. Returns (source, taken_from_a, taken_from_b) or (None, .., ..) on conflict."""
    pb, pa, pbb = _class_parts(base), _class_parts(a), _class_parts(b)
    names = list(pb) + [n for n in pa if n not in pb] + [n for n in pbb if n not in pb and n not in pa]
    from_a, from_b, body = [], [], []
    for n in names:
        nb, na, nbb = pb.get(n), pa.get(n), pbb.get(n)
        sa = _norm(na) if na is not None else None
        sb = _norm(nbb) if nbb is not None else None
        sbase = _norm(nb) if nb is not None else None
        a_changed = sa != sbase
        b_changed = sb != sbase
        if a_changed and b_changed and sa != sb:
            return None, [], []
        if a_changed and na is not None:
            body.append(_text(lines_a, na)); from_a.append(f"{base.name}.{n}")
        elif b_changed and nbb is not None:
            body.append(_text(lines_b, nbb)); from_b.append(f"{base.name}.{n}")
        elif nb is not None and not (a_changed and na is None) and not (b_changed and nbb is None):
            body.append(_text(lines_base, nb))
        # a symbol removed by one side and untouched by the other is dropped (rare; the checker forbids removals)
    dec = [lines_base[d.lineno - 1] for d in base.decorator_list]
    header = lines_base[base.lineno - 1]
    return "\n".join(dec + [header] + body), from_a, from_b


def compose(baseline_src: str, a_src: str, b_src: str) -> dict | None:
    try:
        tb, items_b = _top(baseline_src)
        ta, items_a = _top(a_src)
        tc, items_c = _top(b_src)
    except SyntaxError:
        return None
    lb, la, lc = baseline_src.splitlines(), a_src.splitlines(), b_src.splitlines()
    base_syms = {n: node for n, node in items_b if n != "<stmt>"}
    a_syms = {n: node for n, node in items_a if n != "<stmt>"}
    c_syms = {n: node for n, node in items_c if n != "<stmt>"}
    from_a, from_b, out = [], [], []
    # module-level statements: the baseline's, plus new ones from a and b (imports, constants), after the last
    # import; an assignment to a name the baseline also assigns is a CHANGE of that statement, not a new one
    def target(node):
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            return node.target.id
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            return node.targets[0].id
        return None
    base_stmts = [node for n, node in items_b if n == "<stmt>"]
    base_norm = {_norm(s) for s in base_stmts}
    base_targets = {target(s): s for s in base_stmts if target(s)}
    assign_override: dict[str, tuple[str, str]] = {}          # name -> (text, side)
    for side, items, lines in (("a", items_a, la), ("b", items_c, lc)):
        for n, node in items:
            if n != "<stmt>":
                continue
            t = target(node)
            if t and t in base_targets and _norm(node) != _norm(base_targets[t]):
                if t in assign_override and assign_override[t][0] != _text(lines, node):
                    return None                                   # both sides changed the same constant differently
                assign_override[t] = (_text(lines, node), side)
    extra = []
    for n, node in items_a:
        if n == "<stmt>" and _norm(node) not in base_norm and not (target(node) in base_targets):
            extra.append(_text(la, node)); base_norm.add(_norm(node)); from_a.append("<module>")
    for n, node in items_c:
        if n == "<stmt>" and _norm(node) not in base_norm and not (target(node) in base_targets):
            extra.append(_text(lc, node)); base_norm.add(_norm(node)); from_b.append("<module>")
    inserted_extra = False
    main_guard = None
    for n, node in items_b:
        if n == "<stmt>":
            txt = _text(lb, node)
            if "__name__" in txt and "__main__" in txt:
                main_guard = txt
                continue
            t = target(node)
            if t and t in assign_override:
                txt, side = assign_override[t]
                (from_a if side == "a" else from_b).append(f"<module>.{t}")
            out.append(txt)
            if not inserted_extra and isinstance(node, (ast.Import, ast.ImportFrom)):
                # keep going until the last import; insert extras after the import block
                nxt = items_b[items_b.index((n, node)) + 1] if items_b.index((n, node)) + 1 < len(items_b) else None
                if nxt is None or not (nxt[0] == "<stmt>" and isinstance(nxt[1], (ast.Import, ast.ImportFrom))):
                    out.extend(extra); inserted_extra = True
            continue
        nb, na, nc = node, a_syms.get(n), c_syms.get(n)
        sbase, sa, sc = _norm(nb), (_norm(na) if na is not None else None), (_norm(nc) if nc is not None else None)
        a_changed, c_changed = (sa is not None and sa != sbase), (sc is not None and sc != sbase)
        if a_changed and c_changed and sa != sc:
            if isinstance(nb, ast.ClassDef) and isinstance(na, ast.ClassDef) and isinstance(nc, ast.ClassDef):
                merged, fa, fb = _merge_class(nb, na, nc, la, lc, lb)
                if merged is None:
                    return None
                out.append(merged); from_a += fa; from_b += fb
                continue
            return None
        if a_changed:
            out.append(_text(la, na)); from_a.append(n)
        elif c_changed:
            out.append(_text(lc, nc)); from_b.append(n)
        else:
            out.append(_text(lb, nb))
    if not inserted_extra:
        out = extra + out
    new_a = [(n, node) for n, node in items_a if n != "<stmt>" and n not in base_syms]
    new_c = [(n, node) for n, node in items_c if n != "<stmt>" and n not in base_syms and n not in a_syms]
    # new symbols go before main() so main can see them
    idx = next((i for i, t in enumerate(out) if t.startswith("def main(")), len(out))
    adds = [_text(la, node) for _, node in new_a] + [_text(lc, node) for _, node in new_c]
    from_a += [n for n, _ in new_a]
    from_b += [n for n, _ in new_c]
    out = out[:idx] + adds + out[idx:]
    if main_guard:
        out.append(main_guard)
    src = "\n\n\n".join(out) + "\n"
    try:
        ast.parse(src)
    except SyntaxError:
        return None
    return {"source": src, "from_a": from_a, "from_b": from_b}


def compose_many(baseline_src: str, sources: list[str]) -> dict | None:
    """Fold several candidates together pairwise (a+b, then (a+b)+c ...). None on the first conflict."""
    if not sources:
        return None
    acc = {"source": sources[0], "from_a": [], "from_b": []}
    taken: list[list[str]] = [[]]
    for src in sources[1:]:
        r = compose(baseline_src, acc["source"], src)
        if r is None:
            return None
        taken.append(r["from_b"])
        acc = {"source": r["source"], "from_a": acc["from_a"] + r["from_a"], "from_b": r["from_b"]}
    return {"source": acc["source"], "parts": taken}


def leave_one_out(baseline_src: str, sources: list[str]) -> list[dict]:
    """For a composite of n >= 3 parts, every (n-1)-composite, so each part can be priced by removal."""
    out = []
    for i in range(len(sources)):
        rest = sources[:i] + sources[i + 1:]
        r = compose_many(baseline_src, rest) if len(rest) > 1 else {"source": rest[0], "parts": []}
        if r:
            out.append({"without": i, "source": r["source"]})
    return out
