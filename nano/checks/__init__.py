"""Checkers: one module per kind of objective check (docs/GENERIC_SPEC.md section 3).

    from nano.checks import get_checker
    ck = get_checker(profile)        # imports nano/checks/<profile.checker>.py, builds its class

A checker module names its class in CHECKER (e.g. CHECKER = "ScriptChecker"); without that, the first
class in the module whose name ends in "Checker" (other than the protocol) is used.
"""
from __future__ import annotations

import importlib

from nano.checks.base import Checker, lower_is_better  # noqa: F401


def get_checker(profile) -> Checker:
    name = str(getattr(profile, "checker", "") or "llm").strip()
    mod = importlib.import_module(f"nano.checks.{name}")
    cls_name = getattr(mod, "CHECKER", None)
    if cls_name is None:
        cls_name = next((k for k, v in vars(mod).items() if isinstance(v, type) and k.endswith("Checker")
                         and k != "Checker" and v.__module__ == mod.__name__), None)
    if cls_name is None:
        raise ImportError(f"nano.checks.{name} defines no checker class")
    args = dict(getattr(profile, "checker_args", None) or {})
    return getattr(mod, cls_name)(profile, **args)
