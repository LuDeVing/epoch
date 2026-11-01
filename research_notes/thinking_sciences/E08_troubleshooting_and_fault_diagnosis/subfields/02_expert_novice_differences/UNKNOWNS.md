# Expert-novice differences: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E08.02-U1 | Does distilled strategy text beat no text on novel faults? | Distilled strategy lessons in S0 memory | memory/S0 | K27, K16; contested; same-system time split, tools confounded; Trace2Policy shows harm to strong models | No text / 3 raw traces / distilled text; held-out novel fault families, code-checked; accuracy and tokens; strong and weak model | Beats no text by 3+ pts on novel items on at least the weak model, and does not lose on the strong model | High |
| E08.02-U2 | Does a "what do the symptoms rule out" step build a better first hypothesis set? | Problem-space step in S1/S2 for diagnosis items | S1/S2 | K02; human-only (Johnson 1987, Lesgold); no LLM test | Plain vs forced rule-out step (3 candidates); items with 2-3 plausible causes; first-hypothesis hit rate and accuracy | Hit rate up 10+ pts and accuracy not down | High |
| E08.02-U3 | Does enumerating alternatives cut anchoring at equal tokens? | Enumerate-alternatives check after a first anomaly | G1 / S6 | K11, K20; DiagGuard +10.5 median, single-source, tokens not matched | Plain / enumerate step / extra sampling at same tokens; items with persistent decoy; accuracy drop decoy vs no decoy | Decoy drop shrinks by 5+ pts vs both other arms | High |
| E08.02-U4 | Does a verify-before-act guard reduce wrong changes? | No repair until a localising test output is cited | G (verify) | K06, K28; Gott 1995 swap counts (50 vs 3 vs 8), R2Act; small groups, one benchmark | Plain vs guard; diagnose-and-repair items; premature actions and recovery validity | Recovery validity up 3+ pts and no accuracy loss | High |
| E08.02-U5 | Is evidence closure a better selector than a vote? | Code-computed closure as tie-breaker in S7 | G / S7 | K29, K10; evaluation only (OpenRCA 2.0, Cloud-OpsBench); single-source for selection | N=5 attempts; pick by vote / confidence / closure; accuracy of picked answer | Closure beats vote by 3+ pts on 2 item sets | Med |
| E08.02-U6 | How large must the memory write gate set be? | Fixed gate size rule for memory writes | memory write | K26, K17; gate shown helpful in 2 sources; sizes 40 and 139 are within noise of a 2% threshold | 12-window loop; no gate / inner / inner+outer; held-out 40 / 140 / 400; final-window accuracy and bad writes passed | Smallest size where bad-write pass rate under 10% and final accuracy at least that of the 400 arm | High |
| E08.02-U7 | Does rule-first with a checked override avoid dropping correct candidates? | Override only after a named conflict check on raw evidence | S0 / S6 | K30; one source, one model family (Qwen) | Free override vs checked override; items where recalled rule is right about 80%; overrides vs corrections, accuracy | Net corrections minus overrides improves, accuracy up 2+ pts | Med |
| E08.02-U8 | Does tagging lessons as device-specific vs reusable help on a new system? | Tag field on stored lessons | memory | Gott 1992 qualitative (a15); no test | Untagged vs tagged lessons; new system sharing function; accuracy | Tagged wins by 3+ pts cross-system, no loss in-system | Med |
| E08.02-U9 | Which Sherlock part carries the gain: system model, strategy list or verify rule? | Keep only the part that pays | memory/S0 | K31; no ablation; Hydrive vs F-15 confounded; developer data | Four arms: model only / strategy only / verify only / all; held-out systems; accuracy and premature actions | A single part gets at least 80% of the all-arms gain | Med |
| E08.02-U10 | Does a typed action space with preconditions fix repair errors? | Typed repair step | G | K28; 67.9% wrong operation, one benchmark, one group | Free-text plan vs typed op + precondition check; R2Act-style items; recovery validity | Validity up 10+ pts | Med |
| E08.02-U11 | Does a forced strategy switch after fruitless checks help? | Switch rule at impasse, tied to O1-O8 | S6 / O | K05; human-only, Johnson 1995 review, no counts | Fixed vs forced switch after 3 fruitless checks; stalled items; accuracy and steps | Gain on stalled items of 5+ pts with no loss elsewhere | Low |
| E08.02-U12 | Does cost-aware test choice (split per cost) beat nearest test? | Cost-weighted test ranking computed in code | S4 | a09 only; human-only, no LLM test | Nearest vs split-per-cost; items with test catalogue and costs; cost to localise | Cost down 15%+ at equal accuracy | Low |
| E08.02-U13 | Does expert persona fail on diagnosis? | Nothing; confirms the exclusion in 4b | none | K21, K32; factual QA only | Persona vs none; diagnosis items | Not an add. Expect no gain; if persona gains 3+ pts on diagnosis, reopen | Low |
| E08.02-U14 | Does a typed system model (dependency graph) at equal tokens help in our domain? | System-model slot in S0 for classes that have one | S0/memory | K12; GALA 74 vs 48, ORCA-bench source code 9-16 pts; authors' own methods | Graph/model given vs not, same tokens; items with known structure | Gain of 5+ pts and tokens not above plain | Med |

## Open questions we cannot test on our bench yet

- Independent replication of Johnson 1987 and Gott 1995: needs human participants or new literature search (APIs were rate limited). Unblock by re-running the search and by opening the Sherlock reports in full.
- Chase and Simon and Chi et al. numbers: primary texts were blocked. Unblock with library access.
- Agents versus human experts on the same faults: no data set exists. Unblock by building a small set with human expert solution traces.
- Cross-system transfer of distilled memory: OpsHarness gains are in-system. Needs a bench with at least two unrelated systems.
- Rule-to-model switching (Rasmussen) as detectable agent behaviour: only a proxy exists. Unblock with trajectory labels.
- Multi-turn aptitude vs reliability (Bi vs Laban): needs the Laban paper read and a common task.
- Independent field replication of tutoring-style gains for LLM agents: nothing to run until U1 and U9 are done.

## Order to run

1. U6 (gate size): cheap, decides how every later memory test is safeguarded, and two sources already say a gate matters.
2. U1 (distilled strategy text vs no text on novel faults): the largest possible gain and the central contested claim.
3. U3 (anti-anchor at equal tokens): matches the best-measured agent failure (about 10 points under decoys) and tests a plain-compute control.
