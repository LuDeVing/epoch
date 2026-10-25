# Troubleshooting and fault diagnosis: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" is the status in claims.jsonl, set before any stricter independence re-check. Treat each row as a candidate until that check is done. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Claim ids are global and cited exactly. Two of the field's subfields are researched, so this is a partial view.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 03 Hypothesis limits | [DEEP](subfields/03_hypothesis_limits/DEEP.md) | 29 | 10 (6 contested, 13 single-source) |
| 04 Troubleshooting search strategies | [DEEP](subfields/04_troubleshooting_search_strategies/DEEP.md) | 34 | 13 (4 contested, 17 single-source) |
| **Total** | | **63** | **23** |

Each researched subfield has a UNKNOWNS.md: 14 test rows (E08.03-U1 to U14) and 15 (E08.04-U1 to U15), 29 in all.

Not yet researched (from SUBFIELDS.md, no DEEP.md):

- Cognitive models of troubleshooting (Jonassen and Hung; Schaafstal)
- Expert-novice differences (Gott; Rasmussen)
- Surface-cue heuristics (skill, rule, knowledge)
- Model-based diagnosis (Reiter; de Kleer and Williams)
- Training systems and tutors (Jonassen; Lesgold)
- Complexity of expert troubleshooting (Sabuncu et al., ASEE)
- LLM help in hardware debugging (Hu and Ash 2026)
- Industrial fault detection (Isermann)

## 2. Established findings, merged

Status established only. Many are human results; for the agent they are design hints until tested on our model (section 5).

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | People hold only 3 to 5 hypotheses at once. Skill does not raise the count. Load lowers the count, and a lower count raises the probability sum over exclusive causes. The list should be an outside object, not a head or context. | E08.03-K01, E08.03-K05 | S1, memory | partly (S2 writes 1 to 4 candidate rules; no ledger object) |
| F2 | Lists feel complete. Stated chance that the true cause is listed is about 68%. People move little weight to "all other" when branches are hidden. | E08.03-K03 | G, S1 | no |
| F3 | LLMs under-use "none of the listed." False action on no-correct-option items is about 70% at baseline. Replacing the right option with "none" cut accuracy for all six models. Healthy systems get a false fault in 11 to 24% of runs (that last figure is single-source; see E08.04-K30). | E08.03-K10, E08.03-K23, E08.04-K13 | G, S9 | no (G6 pulls the other way; see C1) |
| F4 | LLM agents anchor on their first diagnosis. 65.6% of wrong round-1 diagnoses stayed wrong. 50.8% of correct ones fell by round 3. Information requests fall each round. Generic reasoning prompts do not lift the plateau. | E08.03-K11 | G1, S5, memory | partly (S5 caps rounds; no re-open rule) |
| F5 | LLMs accept a wrong supplied option, and an authority frame raises acceptance. Pressure over turns makes them drop right answers. The prompt defence works on strong models and barely on small ones. | E08.03-K24 | S1, G | partly (S1 input hygiene is [S]) |
| F6 | A differential list often holds the answer when top-1 is wrong (78.3% vs 52%). Models are better at the final answer than at differential reasoning. | E08.03-K12 | S3, S7 | partly (S4 harvest keeps dropped candidates) |
| F7 | Reminders and bias warnings do not reliably cut error and can over-correct. Prompt rules were echoed but not obeyed. Structural changes help more than text. Guardrails belong in code. | E08.03-K15, E08.04-K10 | G (code guardrails) | yes (4b bias checklists; section 1) |
| F8 | Independent LLM samples are mostly repeats. Distinct hypotheses grow well below linearly in K (7.89 unique at K=32; recall +0.131 from 1 to 5 draws). | E08.03-K20 | S3, G12 | partly (S3 many draws; no yield curve) |
| F9 | Skilled people rarely use textbook half-split. They open by function, run many cheap good/bad checks and anchor on a hunch. Half-split is a trained rule. | E08.04-K01 | O (test selection) | no |
| F10 | Half-split needs log2 N tests only for a single fault, linear chain, equal cost, reliable tests. Greedy information gain is exactly optimal at unit cost and equal priors, near optimal in practice, but can be arbitrarily bad in built cases. | E08.04-K04 | O (test selection) | no |
| F11 | Under cost, rank tests by probability per cost or information per cost. Exact optimum is NP-hard. Greedy is the standard design. | E08.04-K05 | O, G5 | no |
| F12 | Unaided LLMs choose poor tests. Many carry zero information, they keep asking after one candidate remains, and they pick the best split in a minority of turns. | E08.04-K06 | G5, O | partly (G5 says code selects; no test-selection module) |
| F13 | With candidate tracking and gain scoring in code and the model only proposing tests, success rises in closed-candidate games (FloDial 43.7 to 67.3; 20 Questions +37.4 points). Evidence uses simulated answerers. Asking the model to restate the live set helps but fails; the ledger belongs in code. | E08.04-K07, E08.04-K09 | G5, O, memory | partly (G5; no ledger, no gain scorer) |
| F14 | After a search routine fails, people and agents repeat it with a small change instead of switching method. | E08.04-K03 | G1, S6 | partly (S6 fires on "same error twice") |
| F15 | Greedy selection can lose to random when its probability or reliability model is wrong. | E08.04-K15 | G5 | no |
| F16 | Agents often answer correctly without a closed evidence path. Main run failures are misread data and incomplete exploration, not search order. Outcome accuracy overstates grounding (JRA 0.68, closure 0.21 and 0.15). | E08.04-K12 | G, S8 | partly (G3, G10) |
| F17 | Stopping is weak. People and agents keep probing after decisive evidence, commit after one abnormal signal, or over-diagnose healthy systems. | E08.04-K13 | S9, stop rule | partly (S8, S9; no diagnosis stop rule) |
| F18 | More steps are not better. Weak models use 3x steps for a fraction of accuracy. Step limits past about 5 added only tokens. Rounds show sharp diminishing returns. | E08.04-K14 | G11, G12 | yes (G11, G12) |
| F19 | Terms "topographic" and "symptomatic" drift between sources. Name tests by the reference they need. | E08.04-K02 | none (naming) | no (labels only) |

## 3. Contradictions between subfields

| # | Where they disagree | How to resolve |
|---|---|---|
| C1 | **Stop and commit vs missing cause.** E08.04-K13 and E08.04-K07 stop when the candidate set is a singleton. E08.03-K10, E08.03-K23 and E08.03-K02 say the true cause is often not on the list, and models never say "none." SCHEMA G6 forbids abstaining on the first pass. | A singleton stop is safe only if the list is known complete. Add a missing-cause check before the singleton stop. G6 needs an exception: abstain or say "no fault" only when named checks pass. Tests: E08.03-U1, E08.04-U3, E08.04-U4. |
| C2 | **Closed list vs open space.** E08.04-K07 shows gain from code scoring on closed sets. E08.04-K08 (contested) and E08.04-K28 show no gain on open sets. E08.03-K02 and E08.03-K20 say real cause spaces are larger than any list. | The scaffold needs an enumerable set. Find the size where it stops helping: E08.04-U6. Until then use it only on closed lists. |
| C3 | **Breadth.** E08.03-K20 says independent draws repeat and grow sublinearly. SCHEMA S3 and A01 F10 say many independent draws then select. E08.03-K21 (contested) says a bare "something different" step did not help, yet SCHEMA S3 has code assign untried directions. | S3 gains need diversity forced by structure, not by request. Concept-first is the open candidate: E08.03-U2, E08.03-U4. |
| C4 | **Ledger: keep or cost.** E08.03-K18 says a removal-reason ledger stops silent loss of a found diagnosis but cut top-1 from 60 to 40 (10 cases, one model). E08.03-K11 says free-form updates anchor. E08.04-K09 says the ledger helps and belongs in code. | Contested between retention and top-1. Run the three-arm test: E08.03-U5, E08.03-U13. |
| C5 | **Challenger roles.** E08.03-K13 (contested) reports big gains from devil's advocate and facilitator roles. E08.03-K26 and SCHEMA G9 say debate gives 1.3 to 2.7 points at equal compute. No diagnosis task has a same-token control. | Keep G9 for now. Test tracker and challenger against self-consistency: E08.03-U8. |
| C6 | **Counterexample prompting.** E08.03-K25 (single-source) says counterexample prompting raised discovery from 42% to 56%. A01 section 3 (C4) and A01 F12 say LLMs rarely find falsifying cases and prompting a search barely helps. E08.03-K25 also says thinking mode raised success without raising the disconfirming ratio. | Both fit if code runs the refuting test. Test: E08.03-U7. Do not add a bare "find a counterexample" instruction. |
| C7 | **Extra reasoning.** E08.04-K11 (contested): reasoning lifted questioning in 20-Questions (0.08 to 0.94) but did nothing for HAProxy fault isolation at 10x tokens. A01 C2 and C3 show the same split. | Cap by class and step. Test reasoning at test selection only: E08.04-U11, E08.03-U11. |
| C8 | **Is half-split worth teaching?** E08.04-K01 says experts do not use it. E08.04-K04 and E08.04-K05 say it is optimal under named conditions. E08.04-K16 says the label did not speed repair. E08.04-K17 and E08.04-K33 say a fixed method plus functional breakdown doubled solved faults. | Not a real conflict. Humans do not need it; the agent can get it free in code. The structured-method gain cannot be assigned to half-split. Test: E08.04-U1, E08.04-U12. |
| C9 | **Coarse first vs symptom first.** E08.04-K22 (contested) recommends normal-reference narrowing first. E08.04-K29 shows symptom matching fixating on a look-alike part. | Grain is open: E08.04-U13, E08.04-U8. |
| C10 | **Confidence as a signal.** E08.03-K19 (confidence and accuracy R2 = 0.03) agrees with SCHEMA 4b and A01 C6. No conflict, but E08.04-K27 uses expected belief change as a stop signal, which relies on the model's own probabilities. | Check that belief estimates are calibrated before trusting a belief-change stop: E08.04-U5, E08.03-U9. |

## 4. Recurring mechanisms

| Mechanism | Where it shows | Agent consequence |
|---|---|---|
| **Completeness illusion.** The visible list is taken as the whole space. | E08.03-K03, E08.03-K10, E08.03-K23, E08.04-K13 | Code owns an "other / missing" slot and a forced check on it. |
| **Fixation and anchoring.** First hypothesis or first routine persists after failure. | E08.03-K11, E08.03-K15, E08.04-K03, E08.04-K29 | Repeat detector and forced switch in code (G1 signal). |
| **Working memory is the limit, so move the list outside.** | E08.03-K01, E08.03-K05, E08.04-K09 | Candidate ledger in code, model fills slots only. |
| **Models propose, code scores.** | E08.04-K06, E08.04-K07, E08.04-K12 | Test-selection module: model writes k tests, code picks by gain. |
| **Instructions fail, structure works.** | E08.03-K15, E08.04-K10 | Every guardrail enforced by code, never by a text rule. |
| **Diminishing returns on steps and draws.** | E08.03-K20, E08.04-K14 | Cap steps and draws per class. |
| **Closed-set dependence.** Gains need an enumerable candidate set. | E08.04-K07, E08.04-K08, E08.04-K28 | S0 gate on set size. |
| **Estimate quality bounds the gain.** | E08.04-K15, E08.04-K27, E08.03-K03 | Audit probabilities before using them to rank or stop. |

## 5. Merged tests

All rows at equal tokens, selector tokens charged (E08.04-K34).

| Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|
| MT1 Missing-cause check and no-fault exit | E08.03-U1, E08.04-U4 | Seeded faults with the true cause absent in half and healthy systems in half; free list vs forced "is the cause missing" step vs re-sampling; score false-commit, false-fault and missed-fault rates. | High |
| MT2 Code-chosen vs model-chosen tests (core) | E08.04-U1, E08.04-U2, E08.04-U7 | Seeded single-fault chains and a priced 12-fault matrix; arms free, half-split, filter only, scoring only, filter + scoring, gain-per-cost; score tests to isolation, wasted tests, total cost. | High |
| MT3 Stop rule | E08.04-U3 | Fixed cap vs singleton vs belief-change vs singleton + one verifying test; run on lists with and without the true cause (links MT1). | High |
| MT4 Estimate quality | E08.04-U5, E08.03-U9 | Greedy with true, model-made and corrupted tables vs random; code floor on "other" mass; score tests and Brier. | High |
| MT5 Scope gates | E08.04-U6, E08.04-U15 | Fault lists of 8 to 512 on 3 backbones, model vs scaffold; find the crossover size and the strong-model cutoff. | High |
| MT6 Breadth and generation | E08.03-U2, E08.03-U3, E08.03-U4, E08.03-U10 | K draws, permuted order, N = 3/6/12, concept-first, coarse vs fine lists; score cumulative distinct true causes and top-1. | High |
| MT7 Staged anchoring and ledger | E08.03-U5, E08.03-U13, E08.03-U14, E08.03-U12 | 60 three-stage faults, half misleading at stage 1; free update vs ledger with reasons vs re-rank vs evidence-gated switch vs mark-not-drop; score recovery, retention, regressions, top-1. | High |
| MT8 Supplied hypothesis and refuting step | E08.03-U6, E08.03-U7, E08.04-U8 | No/wrong/right supplied hypothesis, with and without a code-run refute-the-leader test and a switch after two failed confirmations; score info requests, switches, look-alike share. | High |
| MT9 Challenger vs self-consistency | E08.03-U8 | Self-consistency vs tracker + challenger vs each alone, same tokens; score coverage and top-1. | Med |
| MT10 Verify each bisect split | E08.04-U9 | Judge error 0 to 10%; single pass vs boundary re-test vs vote of 3 vs code oracle; score end-to-end success. | Med |
| MT11 Intake, system model, grain, memory | E08.04-U10, E08.04-U12, E08.04-U13, E08.04-U14 | Crisp vs vague reports; strategy text vs functional breakdown in code; coarse vs cost-chosen grain; raw cases vs runbooks. | Med |
| MT12 Where reasoning goes | E08.04-U11, E08.03-U11 | None vs selection only vs everywhere; differential-first vs plain CoT on strong and weak models. | Low |

Run order, following both UNKNOWNS files: MT2 first (no study has measured it), then MT1, MT6, MT7.

## 6. Not to add

| Idea | Why not | Claim ids |
|---|---|---|
| "Beware anchoring" or "be careful" prompts, cognitive-forcing text | No reliable effect; can over-correct; echoed but not obeyed | E08.03-K08, E08.03-K15, E08.03-K27, E08.04-K10 |
| Differential-first instruction | No gain for GPT-4 (+2.2, not significant); cost GPT-3.5 8 points (2023 models; recheck is MT12) | E08.03-K22 |
| Confidence as a stop or doubt signal | R2 = 0.03 in humans; SCHEMA 4b | E08.03-K19 |
| Imitating the human 3 to 5 hypothesis cap | It is a memory limit, not a goal | E08.03-K01 |
| Teaching the agent "half-split" as a prompt rule | Humans do not use it; the label alone did not speed repair; do it in code if MT2 passes | E08.04-K01, E08.04-K16 |
| Handing the model a supplied list as a premise | Wrong options are accepted | E08.03-K24 |
| Role personas and debate | Small or no gain at equal compute (G9); only the tracker and falsifier are tested in MT9 | E08.03-K13, E08.03-K26 |
| A bare "give something different" step | No coverage gain; precision fell | E08.03-K21 |
| Citing Rasmussen or Morris and Rouse for a hypothesis count | Primary texts unread | E08.03-K28 |
| Topographic and symptomatic as module names | Terms drift; name tests by the reference they need | E08.04-K02 |
| More steps or rounds past the knee | Only tokens | E08.04-K14 |
| Outcome-only scoring | Hides missing evidence paths | E08.04-K12 |

## 7. Gaps

- Eight of ten field subfields have no DEEP.md (section 1). Model-based diagnosis is the most relevant: it would give a code-run reasoner and multi-fault handling.
- Almost all search evidence uses a simulated answerer and a closed list. No noisy or intermittent real instruments (E08.04-K18, flaky tests).
- No study counts tests to isolation for an LLM against a half-split or cost-weighted optimum (E08.04-K23).
- Human data are thin and small. Rasmussen, Gugerty and Goldbeck primary texts were not reachable. Expert-novice evidence is N = 3 vs 3 (E08.04-K29).
- Most LLM results are 2026 preprints, often with LLM judges and medical tasks. Few are non-medical fault tasks.
- All tests assume a single fault. Multiple simultaneous faults are not covered.
- Dollar-priced test results (SDBench) may not transfer to token-priced tests (E08.04-K31).
- Cause-key deduplication needs a validated "same cause?" judge (E08.03 open questions).
- Only one synthesis exists besides this one (A01), so cross-field checks are limited to A01. The E09 subfields (hypotheses in debugging, LLM debugging) should be compared once they have syntheses.
