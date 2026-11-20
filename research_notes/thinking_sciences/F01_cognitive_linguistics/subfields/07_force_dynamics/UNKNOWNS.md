# Force dynamics: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| F01.07-U1 | Does force-slot tagging of causal claims beat plain CoT? | Slot record (focal, opposer, tendency, balance, outcome) in S2 | S2 / O6 | K02 single-source, human-only; K18 warns of cost | 50 labelled vignettes + MoCa + CLadder rungs 2-3; plain CoT vs slot tagging; accuracy, parse failures, tokens | Gain >= 4 pp, CI above 0, parse failures not higher, on 2 of 3 sets | High |
| F01.07-U2 | Does a one-line principle prompt fix pragmatic causative traps, or was 188/188 leakage? | Principle line for known traps | G / S1 | K10 single-source, one paper, one model | 188 M-heuristic items; direct, CoT, one-line principle, long item trace; 2+ models | One-line arm >= 80% and within 10 pp of long trace on 2 models | High |
| F01.07-U3 | Does naming absences as forces reduce omissive-cause errors? | Absence-listing step | G / S2 | K05 established for humans; no LLM test | Omissive vs matched orthodox items; plain vs "list what was expected but missing"; error gap | Omissive-minus-orthodox error gap shrinks >= 30%, no drop on orthodox items | High |
| F01.07-U4 | Does a counterfactual-effort step make LLM blame human-like? | Effort step in attribution | S5 / O-attribution | K16 single-source, older OpenAI models | BoxLifters-style 55 items; plain vs counterfactual-effort step; correlation with human Ensemble | r rises >= .15 and exceeds .8 | Med |
| F01.07-U5 | Do LLMs show the human B-over-A chain blame pattern? | Chain-position check in attribution | S5 | K06 contested; human-only (Cheung 2026) | Chain-of-agents vignettes; plain vs structure prompt; ordering match, intent vs proximity | Model order matches humans on >= 80% of items; otherwise add the prompt only if it fixes mismatches | Med |
| F01.07-U6 | Does cause/allow/prevent typing with lookup composition improve chain judgments? | Typed link composition table | O3 / S2 | K03 contested; one lab; force ties causal model | Nine chain types as text; unaided vs table; match to human modal answer; "ambiguous" flag use | +10 pp on C/C, C/P, A/C cells and no harm on P/P | Med |
| F01.07-U7 | Do LLMs handle double prevention like humans (about 50/50) or collapse to one answer? | Ambiguity flag for P/P | G | K04 contested; no LLM data | P/P items, 3 wordings, 2 orders; answer distribution | Flag added only if answers swing > 25 pp with wording or order | Med |
| F01.07-U8 | Does typing objections as blocker vs reinforcer improve rebuttals? | Objection typing at impasse | S6 / O4 | K15 single-source; Talmy examples only | 40 arguments; free listing vs typed; blind rubric, length-normalised (G5) | Rubric gain >= 0.5 SD | Med |
| F01.07-U9 | Does naming the opposer (blocker) help planning and tool-use agents? | Blocker identification at S6 | S6 | Gap 7: no study; d13 analogy only | Tasks with hidden blocker; plain obstacle list vs opposer-and-strength check; success rate | Success +5 pp at equal tokens on 2 task families | Med |
| F01.07-U10 | Does a required state-change check cut false "step done" claims? | State-change check | S8 | K09 single-source; hand-built, 0 false positives on 35 movies | Tool-use traces with injected false completions; plain verify vs state-change check; false-accept rate | False accepts halve with <= 10% token overhead | Med |
| F01.07-U11 | Can LLMs label cause/enable/prevent on symbolic scenes? | Nothing yet (a baseline) | none | K17: no benchmark; CRAFT pre-LLM | CRAFT-style text scenes; plain vs typed; accuracy vs human 71.3% | Informative only; sets baseline for U1 and U6 | Low |
| F01.07-U12 | Does a guard against illusion of causality help? | No-effect evidence check | G calibration | K12 single-source; no CoT test | 1000 null-contingency items; plain vs "state evidence for no effect first"; median rating | Median drops >= 20 points without hurting true-effect items | Low |

## Open questions we cannot test on our bench yet
- Physical force reasoning from video or images: needs a vision benchmark and a physics engine; VLMs fail (K13). Unblock: add an engine tool (Mind's Eye style, +27.9 to +46.0) before testing any prompt.
- Independent replication of Wolff and Barbey composition: needs a non-Wolff human study. Unblock: run a small crowd replication, or find one the search missed.
- Talmy's psychological and social forces (urge, persuade, relent) for dialogue agents: no operational definition exists. Unblock: write annotation guidelines and a small dialogue set.
- ACL Anthology and Google Scholar search for LLM force-dynamic verb probing (gap 6): arXiv and OpenAlex were rate-limited. Unblock: query the Anthology directly.
- Current-model behaviour: most LLM evidence uses 2023-era models. Unblock: rerun the cited items on current models first.
- The 64% vs 8% order figure in Khemlani 2020 is unverified. Unblock: check the paper's table.

## Order to run
1. F01.07-U2: cheapest (188 existing items, prompt only) and it settles whether the only strong LLM result is real or leakage.
2. F01.07-U1: the central question for the subfield (does the slot scaffold pay at equal tokens), reusing items we already have.
3. F01.07-U3: tests the one human finding that is well established (K05) on the model.
