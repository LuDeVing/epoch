"""Mode 3 test profile (docs/GENERIC_SPEC.md section 6): a design question with no objective check.

"Design a fair review process for a hackathon." A candidate is a written proposal (markdown) with five sections:
CLAIM, FROM THE FACTS TO THE IDEA, FROM THE IDEA TO THE RESULT, WEAK POINTS, PROPOSED TEST. The panel checker
(nano/checks/panel.py) judges each proposal blind, K judges on the criteria below, plus people's opinions from
control.json with a bounded weight. The run's output is a ranked list of proposals, not a verified artifact.
"""
from __future__ import annotations

# Facts the proposals reason from; a proposal must cite at least one (rung 0 lint). Ids are stable.
FACTS = [
    ("F1", "process", "The event has about 60 teams and 12 volunteer judges, each free for at most 4 hours."),
    ("F2", "assign", "A judge who reviews a team from their own company or school tends to score it higher."),
    ("F3", "assign", "Judges who see projects late in a session score them lower on average than early ones."),
    ("F4", "rubric", "Without a written rubric, two judges agree on the better of two projects about 6 times in 10."),
    ("F5", "rubric", "A demo slot is 5 minutes; a judge needs about 3 more minutes to write a score and a note."),
    ("F6", "aggregate", "Raw scores from different judges are on different scales: some judges never give below 6."),
    ("F7", "aggregate", "Teams talk to each other; a team that learns the rubric can polish what it rewards."),
    ("F8", "appeal", "Last year 9 teams complained about the result and no one could say how their score was made."),
    ("F9", "appeal", "Results must be announced within 2 hours after the last demo."),
]


def _facts(node: str) -> str:
    return " ".join(f"[{i}] {t}" for i, n, t in FACTS if n == node)


TREE = [
    {"id": "root", "name": "a fair review process for a hackathon", "parent": None,
     "frame": "Volunteer judges watch short demos and score projects; prizes go to the top scores. Known: " + _facts("process"),
     "assumptions": ["every project is judged by the same kind of judge", "a score is a number on one scale",
                     "the review happens on the day only"],
     "boundary": "everything", "directions": ["upward"]},
    {"id": "assign", "name": "who reviews which project", "parent": "root",
     "frame": "Judges pick the tables they visit; there is no rule about conflicts or order. Known: " + _facts("assign"),
     "assumptions": ["any judge can review any project", "the order of visits does not matter",
                     "judges declare their own conflicts"],
     "boundary": "the assignment of judges to projects and the order of visits", "directions": ["inward", "outward"]},
    {"id": "rubric", "name": "what a judge scores", "parent": "root",
     "frame": "Each judge gives one overall score from 1 to 10 after the demo, with no written rubric. Known: " + _facts("rubric"),
     "assumptions": ["one overall score is enough", "the demo shows what matters", "judges score right after the demo"],
     "boundary": "the rubric, the form a judge fills in, the time per review", "directions": ["inward", "outward"]},
    {"id": "aggregate", "name": "how scores become a ranking", "parent": "root",
     "frame": "Scores are averaged per project and the top averages win. Known: " + _facts("aggregate"),
     "assumptions": ["an average of raw scores is fair", "every judge's scale is the same",
                     "a ranking is computed once, at the end"],
     "boundary": "the rule that turns scores into a ranking, and any calibration of judges", "directions": ["inward", "outward"]},
    {"id": "appeal", "name": "transparency and appeals", "parent": "root",
     "frame": "Teams see only the final ranking; there is no way to question a score. Known: " + _facts("appeal"),
     "assumptions": ["teams do not need to see their scores", "an appeal would take too long",
                     "a published process is easier to game"],
     "boundary": "what teams see, the feedback they get, and the appeal step", "directions": ["inward", "outward"]},
]
for _n in TREE:      # every node says which default part it refines (tree.resolve_scope); here, itself
    _n["refines"] = _n["id"]

INTERFACE = ("A proposal in markdown with exactly these five sections, in this order: CLAIM, FROM THE FACTS TO THE IDEA, "
             "FROM THE IDEA TO THE RESULT, WEAK POINTS, PROPOSED TEST. It cites at least one known fact by its id "
             "(for example [F4]). It describes a process that volunteers can run on the day.")

OUTPUT_FORMAT = """Reply in exactly this form:
HYPOTHESIS: <one sentence: the claim of your proposal>
CHANGE: <one line naming the parts of the review process the proposal changes>
FIDELITY: <exact | partial | substituted | cannot, then one clause: exact = the idea as specified; partial = a piece left out, say which; substituted = a different mechanism with the same aim, say what; cannot = it could not be written within the rules, say why>
```markdown
CLAIM:
<one or two sentences: what the process is and what it achieves>

FROM THE FACTS TO THE IDEA:
<the chain from known facts, cited by id like [F2], to this design; one step per line>

FROM THE IDEA TO THE RESULT:
<the chain from the design to the outcome on each criterion; one step per line>

WEAK POINTS:
<where the design could fail, and who could exploit it>

PROPOSED TEST:
<a small, cheap test that would show whether the design works, and what result would refute it>
```
Write the whole proposal. Plain words, short sentences."""

CRITERIA = [
    "Fairness: every team has the same chance, and no judge's bias, conflict or position in the order decides a result.",
    "Cost in reviewer time: the process fits 12 volunteer judges with at most 4 hours each, and organisers can run it.",
    "Resistance to gaming: a team that knows the process cannot raise its rank without making a better project.",
    "Clarity: a team and a new judge can understand the process in two minutes and see how a score was made.",
]

_BOUNDARY_ALL = "the whole review process: assignment, rubric, aggregation, transparency and appeals"

PROFILE = {
    "name": "review_process",
    "mode": "no_check",
    "title": "design a fair review process for a hackathon",
    "goal": ("Design a fair review process for a one-day hackathon with about 60 teams and 12 volunteer judges. The "
             "process says who reviews which project, what a judge scores, how scores become a ranking, and what teams "
             "see and can question. There is no objective score: each proposal is judged blind by a panel on fairness, "
             "cost in reviewer time, resistance to gaming and clarity, and people may add their opinions."),
    "aim": "Learn whether the research loop can rank written proposals on a design question that has no objective check.",
    "score": {"name": "panel score", "direction": "higher", "unit": "points of 10", "margin": 0.5, "alpha": 0.05,
              "min_seeds": 1},
    "facts": [{"id": i, "node": n, "text": t} for i, n, t in FACTS],
    "vocab": {
        "artifact": "review process proposal", "artifact_file": "proposal.md", "language": "markdown",
        "run": "panel review", "score_phrase": "a fairer, cheaper, harder to game and clearer review process",
        "parts": "parts of the review process", "recipe": "review process",
        "cheap_test": "a dry run of the process on five past projects with two volunteer judges",
        "cost_axes": "judge hours per project, organiser hours",
        "first_check": "the blind panel's reading",
        "targets": ["bias from conflicts of interest", "bias from the order of demos", "judges on different scales",
                    "teams polishing what the rubric rewards", "complaints after the result", "panel score only"],
        "scope_default": "a one-day hackathon with about 60 teams and 12 volunteer judges",
        "levers": "assignment of judges, order of visits, rubric, time per review, calibration, aggregation, feedback, appeals",
        "known_tricks": ("Known practices: written rubrics with anchors, conflict-of-interest declarations, rotating "
                         "the order of visits, z-scoring each judge, pairwise comparisons, a shortlist then a final "
                         "panel, published criteria, short written feedback, an appeal window."),
        "boundary_all": _BOUNDARY_ALL,
        "artifact_short": "proposal", "artifact_long": "proposal for a hackathon review process",
        "goal_short": "making the review process fairer, cheaper in judge time, harder to game and clearer",
        "system": "process", "narrow_examples": "one track, the first round of judging, the final pitches",
        "planner_hint": "boundaries name the steps of the review process a proposal may change",
        "boundary_rules": "", "identity_rule": "",
        "reference_what": "practices from conference peer review and hackathon guides",
        "reference_use": "adapt a practice only if it fits volunteer judges on one day",
        "gain_phrase": "the panel score", "field": "event organisation",
        "observables": "the scores judges give, the time each review takes, agreement between judges, complaints",
        "scope_other": "online hackathons, larger events, juries of experts, long review periods",
        "tune_examples": "minutes per review, judges per project, the size of the shortlist, the appeal window",
        "viable": "a process volunteers can run on the day", "win_short": "is judged fairer and cheaper",
        "score_short": "the panel score",
        "leap_rules": ("who judges whom, what a score is, when judging happens, what teams see, whether every project "
                       "gets the same review, who decides the final ranking"),
        "probe": "a quick dry run with two judges on past projects",
        "weak_points": "conflicts of interest, the order of demos, judges' scales, teams that game the rubric, late appeals",
        "adapt_moves": ("the way good practices are adapted: try it on one track first, keep the old step as a fallback, "
                        "make it shorter, give judges a one-page guide, add a check that shows whether it worked"),
        "separations": "by track, by judge, by time of day, by team size",
        "cheap_words": ["dry run", "past projects", "two judges", "quick", "small", "pilot", "cheap", "one track"],
        "cost_questions": "judge hours, organiser hours, tools needed, time to the result",
        "full_run": "used at a real hackathon",
        "ladder_metrics": "panel_score, panel_sd, learn_z",
        "sources": "studies of peer review, hackathon organiser guides, conference review reports, voting theory",
        "size_word": "event size",
        "setting_words": ("review reviewer reviewers judge judges judging hackathon team teams project projects score "
                          "scores scoring rubric pitch demo demos fairness fair gaming ranking appeal"),
        "setup": "this exact setup (one day, about 60 teams, 12 volunteer judges with 4 hours each)",
        "delta_name": "panel score",
        "same_change_example": "a different rubric for the same step is new",
        "problem_brief": ("a review process for a one-day hackathon (about 60 teams, 12 volunteer judges; proposals are "
                          "judged blind on fairness, reviewer time, resistance to gaming and clarity)"),
        "measured_numbers": "scores, hours, agreement between judges, complaints",
        "leap_operators": {
            "rulebreak": "list eight rules of this part as testable sentences (every project gets the same judges; a score is one number; judging happens after the demo; teams never see scores; the average decides); rank them by how much of the process depends on each; drop or invert exactly one and say what must change so the event still runs; the leap is that change.",
            "subtract": "for each step of this part write what happens if it is removed, and what the facts say it buys; keep the two removals you can defend; reinvest the freed judge time in one named alternative; the leap is a removal plus its reinvestment.",
            "literalize": "find a place where the facts or the frame say one thing behaves like another (judging as voting, a rubric as a contract, an appeal as a trial); set the two sides equal; derive one consequence nobody stated; the leap is the process change that tests it.",
            "remeasure": "list the numbers this part took over from habit (5-minute demos, 1 to 10 scores, 3 judges per project, one round); pick two; derive from the facts what the value should be here; the leap replaces the habit by the derived value.",
            "rerepresent": "describe this part in a different form (as an election, as a tournament, as a market, as a measurement with noise); name one change that is natural in that form and awkward in the current one; the leap is that change, brought back into the process.",
            "limit": "push one quantity of this part to its limit (one judge, every judge for every team, no rubric, a 100-point rubric, instant results); say what breaks first and which fact would show it; the leap is the fix the limit case suggests.",
            "import": "keep the process and add one mechanism from a far field (sports refereeing, clinical trials, auctions, ecology) aimed at a known problem; write the shared structure first, then the instantiation and where the correspondence breaks; the leap is the instantiation.",
            "existence": "assume a process exists that halves the complaints at no extra judge time; give three mechanisms that could be it and, for each, what a dry run on past projects would have to show; the leaps are those mechanisms.",
        },
    },
    "constraints": [
        "C1. A proposal has the five sections CLAIM, FROM THE FACTS TO THE IDEA, FROM THE IDEA TO THE RESULT, WEAK POINTS "
        "and PROPOSED TEST, and cites at least one known fact by its id.",
        "C2. About 60 teams and 12 volunteer judges; no judge works more than 4 hours.",
        "C3. Results are announced within 2 hours after the last demo.",
        "C4. No paid tools; a shared spreadsheet and paper forms are available.",
        "C5. The process must be explainable to teams before the event starts.",
        "C6. There is no objective score: proposals are ranked by a blind panel on fairness, reviewer time, resistance "
        "to gaming and clarity, with people's opinions at a bounded weight.",
    ],
    "assumptions": [
        "every project is judged by the same kind of judge",
        "one overall score per review is enough",
        "an average of raw scores is fair",
        "teams do not need to see their scores",
        "the order of demos does not matter",
        "judges declare their own conflicts",
    ],
    "tree": TREE,
    "lenses": {
        "parts": "the parts of the review process: who reviews which project, what a judge scores, how scores become "
                 "a ranking, transparency and appeals",
        "dataflow": "the path of one project: it is assigned to judges, demoed, scored, the scores are combined, the "
                    "result is announced, the team sees it and may question it",
        "dynamics": "phases of the day: the first demos when judges are fresh, the middle, the last demos, the "
                    "deliberation, the announcement",
        "bottlenecks": "where judge time is lost or fairness leaks: waiting between tables, writing notes, judges on "
                       "different scales, late demos, unclear criteria",
        "failures": "the ways a review process fails: conflicts of interest, order effects, gaming the rubric, "
                    "results nobody can explain, appeals that come too late",
    },
    "boundary_all": _BOUNDARY_ALL,
    "artifact": {"path": None, "interface": INTERFACE, "skeleton": "nano/profiles/templates/proposal_skeleton.md",
                 "output_format": OUTPUT_FORMAT, "entry": "a markdown proposal"},
    "checker": "panel",
    "checker_args": {"criteria": CRITERIA, "judges": 3, "people_weight": 0.25, "min_score": 4.0},
    "docs": {},
    "diagnostics": "",
}
