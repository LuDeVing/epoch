"""Stage envelopes for the token budget: which stage a call belongs to, and whether a call is affordable
without eating the builds' floor. The dry runs showed a round can spend a fifth of the budget on ideas and
then build nothing; the floor stops that (research_notes/thinking_parts/09_control.md C1)."""
from __future__ import annotations

SHARES = {"research": 0.05, "ideation": 0.20, "judging": 0.05, "interrogation": 0.20, "build": 0.40, "reserve": 0.10}
BUILD_EST = 17_000      # a build call: the script plus a full rewrite, about 5k in and 12k out


def stage_of(card: str) -> str:
    c = (card or "").lower()
    if c.startswith("sketch"):
        return "ideation"
    if c.startswith("deepen") or c.startswith("premortem"):
        return "interrogation"
    if c in ("cluster", "merge", "prior"):
        return "judging"
    if c in ("research", "analogy_research", "plan", "replan", "defaults"):
        return "research"
    if c in ("implement", "revise", "fix", "program", "compose") or c.startswith("impl") or c.startswith("control") or c == "tune":
        return "build"
    return "other"


def afford(spent: int, est: int, budget: int, stage: str, build_spent: int, shares: dict | None = None) -> tuple[bool, str]:
    """Can this call be paid for? A non-build call must also leave the builds their floor (the build share of
    the budget not yet spent on builds). Returns (ok, reason)."""
    sh = shares or SHARES
    if spent + est > budget:
        return False, "budget"
    if stage != "build":
        floor_left = max(0, int(sh.get("build", 0.4) * budget) - build_spent)
        if spent + est + floor_left > budget:
            return False, "build floor"
    return True, ""


def affordable_slots(spent: int, budget: int, k: int, est_build: int = BUILD_EST) -> int:
    """How many of k build slots the remaining budget can pay for (at least one when anything is left)."""
    left = budget - spent
    if left <= 0:
        return 0
    return max(1, min(k, left // max(1, est_build)))
