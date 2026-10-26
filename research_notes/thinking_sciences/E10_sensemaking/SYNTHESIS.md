# Sensemaking: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" is the status in claims.jsonl, set before the stricter independence re-check. Treat each row as a candidate until that check is done. Two points matter for this field.

- Only 2 of the field's subfields are researched. The cognitive branch (Klein) is covered; the organisational, review, defence and manipulation branches are not.
- Both subfields lean on the same LLM papers (multi-turn loss of 39%, premature closure at about 70%, rule-discovery falsification). A claim counted "established" in both subfields may be one source counted twice. Section 2 merges such rows to avoid that.

Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Claim ids are global.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 01 Data-frame theory and frame activities (frame activities were folded in here) | [DEEP](subfields/01_data_frame_theory_and_frame_activities/DEEP.md) | 32 | 12 (+2 contested) |
| 03 Anomaly handling and fixation | [DEEP](subfields/03_anomaly_handling_and_fixation/DEEP.md) | 30 | 12 (+1 refuted, 4 contested) |
| **Total** | | **62** | **24** |

Each subfield has a UNKNOWNS.md: 16 test rows (E10.01-U1 to U16) and 20 test rows (E10.03-U1 to U20), 36 in all.

Not yet researched (from SUBFIELDS.md):

| Subfield | Why it matters |
|---|---|
| Weick's organisational sensemaking | rated Low for one agent; background only |
| Reviews that map the field (Maitlis and Christianson, Sandberg and Tsoukas) | Low; background only |
| Sensemaking in defence and safety | Low; background only |
| Analyst sensemaking (Pirolli and Card foraging and sense loops) | Medium; state and memory. Only touched through E10.01-K20 |
| Manipulated sensemaking (deep stories) | Medium; bears on S1 input hygiene. Only touched through E10.01-K22 |

## 2. Established findings, merged

Many rows are human results. For the agent they are design hints until tested on our model (section 5). Rows merge claims that come from the same papers.

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | Reframing is rare and driven by a trigger (surprise, conflict, failed explanation). People mostly grow one frame by adding anchors. Revising without a trigger is costly: wrong LLM answers show far more thought switches, and one model changed 98.7% of answers when asked to revise. No trigger-versus-always arm exists. | E10.01-K02 | G1, O8 | partly (G1 doubt only on a signal; no measured trigger) |
| F2 | People notice anomalies and give them extra attention. The failure comes after: explaining away, blaming the method, local patching. Theory change is the rare response. | E10.03-K01 | G3, S2 | partly (G3 held-out check; no explain-away guard) |
| F3 | Without an outside signal, model-only checking is weak. Tool or run-based critique beats no-tool critique in every row tested. For 2026 models the gain from a no-tool revision follows checkability (rho 0.65), not difficulty (rho 0.05), and still breaks some right answers. | E10.01-K07, E10.01-K26 | G2, S5 | yes (G2 revise only from real output; 4b unstructured self-reflection) |
| F4 | Prompt-only debiasing of anchoring fails. Chain of thought, "ignore the anchor" and reflection gave no significant gain; more thinking tokens did not help. Showing anchors from both sides helped partly. | E10.01-K12, E10.03-K18 | G1, 4b | yes (4b bias checklists and debiasing instructions) |
| F5 | Models commit early on staged or multi-turn information and do not recover. Average drop 39%; over 55% of answers are committed in the first two turns; restating facts recovers only 15 to 20%; lower temperature and "wait" instructions do not fix it. Wrong early diagnoses stay wrong (65.6% persist) while the reasoning looks good. | E10.01-K14, E10.03-K12, E10.03-K13 | S1, S3, memory | no |
| F6 | Early salient distractors cut diagnostic accuracy more than late ones (premature closure by order). | E10.03-K05 | S1 | partly (S1 input hygiene moves suggestive material; order effect not named) |
| F7 | Frontier models rarely abstain or ask when the correct option is missing or the case is underspecified (false action about 70%; a short safety prompt cuts it to about 48%). Premature closure is the default on ambiguous cases. | E10.01-K13, E10.03-K14 | G6, new exit | no (G6 pushes the other way; see section 3 C1) |
| F8 | Clarify and abstain operators have a time window. Goal clarification loses nearly all value after the first 10% of a run; input clarification lasts to about 50%. Late clarification is worse than never asking. | E10.03-K29 | S0, new operator | no |
| F9 | Models accept a correction better when it carries an alternative explanation. Bare retraction leaves most of the influence. In humans a full cure is rare; the backfire effect is refuted (section 6). | E10.03-K06 | S5, O8 | no |
| F10 | LLMs confirm more than they falsify on rule discovery. Success tracks the disconfirming-test ratio. A counterexample prompt raised discovery from 42% to 56%; Think-in-Opposites helped in 11 of 11 settings. Outside rule games the evidence is correlational only. | E10.01-K10 | S7, S4 | partly (S7 counterexample search is marked E; test choice at S4 is not) |
| F11 | Counter-evidence that is coherent is accepted; if prior-consistent evidence is also present, models favour it, and order matters. Models adopt wrong retrieved context over a correct prior more than 60% of the time; adoption falls as the context strays further from truth and as prior confidence rises. | E10.03-K10, E10.03-K11 | G4, S1 | partly (G4 samples not independent; no source-versus-prior rule) |
| F12 | Source credibility, not truth, drives LLM updating. Anti-sycophancy prompts cut useful updating as much as harmful updating. An authority-limiting frame cut misleading-clue flips (49.8% to 19.1%). Corrupted tool returns are adopted 35 to 68% of the time; verify-by-call helps with little cost; "compare with prior" lowers accuracy on correct returns. | E10.03-K16 | G4, G6, S1 | partly (S1 input hygiene covers material in the task, not tool returns) |
| F13 | Experts differ from novices by questioning source quality, discarding data points and elaborating longer before naming the frame. The process is shared; the knowledge differs. This is behaviour only. No accuracy test exists (E10.01-K32). | E10.01-K03 | G (first frame) | no (kept as a test, not a rule) |
| F14 | Frame activities (elaborate, question, compare, preserve, reframe, seek) are not clean or ordered. They overlap, coders disagree, and extra ones appear (abandon the search, rapid switching). Do not build a fixed pipeline of activities. | E10.01-K04 | S6 design | no |
| F15 | A prompted step to question the first diagnosis raised human accuracy on easier cases (76.8% vs 60.1%). The effect on hard cases was small and not significant, and calibration did not improve. | E10.01-K06 | O8, S5 | partly (conflicts with 4b for LLMs; see C2) |
| F16 | The comparison technique ACH did not improve coherence or reduce bias in three studies. How the evidence is laid out did matter (hypotheses in rows: 39% vs 62 to 67% picked the confirming hypothesis). Trained analysts were mostly not biased. | E10.01-K16 | O (compare) | yes (4b full competing-hypotheses matrix); the layout finding is new |
| F17 | No source gives numeric trigger rules for reframing. Klein 2023 gives no tau, strain count, anomaly tolerance or frame limit. Every threshold must be tuned on our logs and marked [O] or [D]. | E10.01-K25 | S6 | partly (S6 triggers are code-set; no tuning rule recorded) |
| F18 | Fixation rates in simulated anaesthesia depend on the denominator: 63% of subjects made at least one fixation error (n=30), but 20.5% of unplanned incidents (27 of 132). Compare rates only on the same unit. | E10.03-K22 | section 6 logging | no |

Counts: 24 established claims, all placed (F1 to F18). F17 (E10.01-K25) has one independent source; its "established" label is a design rule and not a measured effect.

## 3. Contradictions between subfields

| # | Where they disagree | How to resolve |
|---|---|---|
| C1 | **Abstain or commit?** G6 says never abstain on the first pass. E10.01-K13 and E10.03-K14 say models commit when they should say "no option fits". E10.03-K29 says late clarification is worse than none. | Different cases. G6 is about nothing passing a check. K13 and K14 are about a missing option or missing facts. Keep G6, add a code gate for "no option fits" early in the run. Decide with E10.03-U12. |
| C2 | **Does questioning the first answer help?** E10.01-K06 (humans, easy cases) says yes. SCHEMA 4b and E10.01-K07 say unstructured self-reflection breaks as many as it fixes. Contested E10.03-K08 reports gains from a neutral "Wait" (50.0 to 57.6) and 2026 models gain on checkable items. | Resolve by checkability, not by model age. Question only when a run or lookup exists. Decide with E10.01-U6 and E10.03-U6. |
| C3 | **Is intrinsic self-correction dead?** E10.01-K07 (2023: lowers accuracy; 2026: gains tracking checkability) against contested E10.03-K08 and single-source E10.03-K23 (telling the model its draft is wrong leaves the pull). | Not contradictory if gains come from verifiable tasks only. Keep G2. Treat "Wait" markers as untested (E10.03-U6). |
| C4 | **Disconfirming tests.** E10.01-K10 marks the falsification effect established. E10.03-K17 (contested) and E10.03-K30 (single) call the LLM evidence correlational and untested outside rule games. | They cite the same data. Established for rule discovery in humans and LLMs; open for diagnosis and debugging. Decide with E10.01-U4 and E10.03-U11. This also fits A01 synthesis C4: the model alone rarely finds falsifying cases, so code should run the search. |
| C5 | **Is there a lasting fixation gap?** E10.01-K15 and E10.03-K15 are both contested and use the same group and one 100-item set (50% in 2024 to 75% in 2026 vs physicians 66%). | One finding counted twice. Treat as unresolved. Decide with E10.01-U14 and E10.03-U20 before building trap scaffolds. |
| C6 | **Surfacing doubt costs accuracy.** Single-source E10.01-K29 (prompting for unresolved conflicts: accuracy 30.1 to 23.2) and E10.03-K16 (anti-sycophancy prompts cut useful updating) against F7 and F12 (safety and authority prompts help). | Every stand-firm or doubt prompt trades one error for another. Each test must report both sides (E10.03-U10 does). |
| C7 | **Trigger rule vs trigger evidence.** E10.01-K02 is established (reframe only on a trigger). E10.03-K25 (contested) says no trigger is validated; E10.01-K25 says no numbers exist. | The rule (G1) is supported. The trigger is not. Test five triggers together (E10.03-U4, E10.01-U3). |
| C8 | **Role-split debate.** E10.03-K19 recovered 71.3% of wrong first answers but had no control. SCHEMA G9 says no debate. | Keep G9. Allow only a matched-token test at an impasse (E10.03-U19). |
| C9 | **Structure beats prose?** Single-source E10.01-K28 (state held by controller 8.6 to 86.1; same procedure written in the prompt stayed near zero) fits G5 and G10. Single-source E10.01-K20 (staged states help) comes from trained or golden-reasoning setups. | Only the code-held part is a strong lead. Keep the two tests separate (E10.01-U2, U15). |
| C10 | **Cross-field: confidence as a signal.** A01 synthesis C6 bars stated confidence. E10.01-K06 shows prompted questioning gave no calibration gain, which agrees. E10.03-K25 lists "graded confidence loss" as a candidate trigger (human data). | Agent confidence stays barred. Use code counts such as failed checks and mismatches instead. |
| C11 | **Cross-field: counterexample search.** A01 C4 says LLMs find falsifying cases poorly. E10.01-K10 shows a prompt raising discovery. | Consistent only if code runs the test and the model reads the result. |

No other field has a SYNTHESIS.md yet, so cross-field checks cover A01 only. Check against A12 (insight), C09 (diagnosis), E08 and E09 when they land.

## 4. Recurring mechanisms

| # | Mechanism | Where it shows | What it means for the agent |
|---|---|---|---|
| M1 | **First-frame lock-in.** The first reading decides what is noticed and what counts as data. | E10.01-K14, E10.03-K05, E10.03-K12, E10.03-K13 | Keep the frame as an editable object. Hold the commit slot open until a minimum evidence set. |
| M2 | **Noticed, then explained away.** The anomaly is seen, then blamed on the method or patched. | E10.03-K01, E10.01-K13 (single-source companions E10.03-K27, E10.01-K29) | Make each excuse cost a check. Keep an open-anomaly list in code. |
| M3 | **Own text pulls.** A model rereads its own earlier output with more trust than a user's. | E10.01-K07, E10.01-K12, E10.03-K18 (single-source: E10.03-K09, E10.03-K23) | Re-derive in a fresh context. Do not annotate "this is wrong". |
| M4 | **An outside signal beats a model check.** | E10.01-K07, E10.01-K26 | Revision and doubt steps need a run, a lookup or a held-out test (G2, G3). |
| M5 | **Source credibility beats truth.** | E10.03-K10, E10.03-K11, E10.03-K16 | Control how tool returns and retrieved text are framed. Measure valid updates too. |
| M6 | **Every guard has a price.** Stand-firm prompts and doubt prompts both cause errors on the other side. | E10.03-K16, E10.03-K14; single-source E10.01-K29 | Report both error types in each test. |
| M7 | **No trigger has a validated number.** | E10.01-K25, E10.03-K25 | Tune thresholds on our logs. |
| M8 | **Timing matters.** Early commit, early clarification and early distractors are worse than late ones. | E10.03-K05, E10.03-K12, E10.03-K29 | Put the gates early in the run and keep them in code. |

## 5. Merged tests

Each row merges UNKNOWNS rows that share items or arms. All tests run at equal tokens against plain. Order follows both subfields' own "order to run".

| # | Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|---|
| T1 | Outside run vs text re-check, by checkability | E10.01-U6, E10.03-U6 | Arms: none; text re-check; re-check with run or lookup; neutral "Wait"; colleague framing. Split items checkable and not. Metric: gain and right-to-wrong flips by class. | High |
| T2 | Trigger comparison for reframe | E10.01-U1, E10.01-U3, E10.03-U4, E10.03-U17 | Planted rule drift plus transient-noise tasks. Arms: never; fixed-step; always; streak with cooldown; mismatch; repeat-failure; strain count with k. Log length growth as a side signal. Metric: time to reframe, false reframes, accuracy. | High |
| T3 | Staged evidence: restart, withheld commit, hygiene block | E10.03-U7, E10.03-U8, E10.03-U15 | Same tasks all-at-once vs sharded. Arms: patch; restate-all; fresh restart; restart plus commit slot withheld; early distractor in a marked block. Metric: share of all-at-once accuracy recovered, tokens. | High |
| T4 | Dropped hypothesis: delete, replace, cascade | E10.03-U1, E10.03-U2, E10.03-U3 | 40 tasks where the first hypothesis is refuted mid-run. Arms: annotate wrong; annotate plus replacement cause; delete and re-derive; cascade to dependents. Metric: lingering use of the dropped claim, accuracy. | High |
| T5 | Frame object held by code, with open-anomaly list | E10.01-U2, E10.01-U7 | Arms: free text; object in context; object held by code; plus a list of open anomalies resolved or parked by code. Metric: accuracy, consistency, accuracy on no-conflict items. | High |
| T6 | Forced disconfirming test beyond rule games | E10.01-U4, E10.03-U11 | Rule discovery plus diagnosis and debugging items. Arms: free test; forced test of what the leader predicts will fail; token-matched extra confirming test. Metric: success, conclusive falsification, tokens. | High |
| T7 | Tool-return trust: authority frame, verify, prior check | E10.03-U10, E10.03-U9, E10.03-U13, E10.03-U14 | 50/50 valid and corrupted returns. Arms: plain; verify-by-call; authority frame; reliability label; operator after a repeated failure; trace detector; agreement-based rule. Metric: corrupted adoption and valid-update loss. | High |
| T8 | No-fit and early clarification gate | E10.03-U12 | 60 answerable and unanswerable twins. Arms: plain; safety prompt; no-fit gate; clarify goals in the first 10%. Metric: false commit rate, abstain rate on answerable. | High |
| T9 | Evidence-conditioned commit gate and predict-then-compare | E10.01-U5, E10.03-U5 | Arms: fixed-step stop; self-agreement stop; expected-observations gate; written expected result compared after the action. Metric: pass rate, tokens. | Medium |
| T10 | Fixation baseline on our model | E10.01-U14, E10.03-U20 | Our own trap items plus mARC items. Reasoning off, short, long, graph. Metric: trap-subset accuracy per class, tokens. Decides whether easy-trap scaffolds are needed at all. | Medium |
| T11 | Reframe quality and operator set | E10.01-U8, E10.01-U9, E10.01-U12 | Arms: free reframe; reframe must change a stated assumption (score by prediction dissimilarity); extra operators (park, discount source, patch); "list two other groupings first". Label our anomaly handling first. | Medium |
| T12 | Expert steps, data-versus-inference split, neutral restatement, goal wording | E10.01-U10, E10.01-U11, E10.01-U13, E10.03-U16 | Ablate each alone on labelled sets at equal tokens; keep only a step that wins by 2 points or more. | Low |
| T13 | Role-split devil's advocate at an impasse | E10.03-U19 | Matched-sample arms: self-consistency; devil's advocate; tutor against closure. Must win by 10 points or G9 stays. | Low |
| T14 | Price on auxiliary excuses | E10.03-U18 | Planted true anomaly plus tempting excuse. Arms: free excuse; excuse requires a check. Metric: wrong dismissal rate, extra tokens. | Low |
| T15 | Staged states and blended-retrieval memory | E10.01-U15, E10.01-U16 | Staged states vs free reasoning on abductive puzzles; blended vs single-case retrieval with an anchoring index. | Low |

All 36 unknown ids are covered. Cross-cutting: every test above also needs the SCHEMA section 7 baseline, one extended-thinking attempt at equal tokens.

## 6. Not to add

| Idea | Why not | Claim ids | Status |
|---|---|---|---|
| Copying the ACH matrix as is | No gain in coherence or bias in three studies | E10.01-K16 | already in 4b |
| Prompt-only debiasing: chain of thought, "ignore the anchor", generic reflection | No significant gain; more thinking did not help | E10.01-K12, E10.03-K18 | already in 4b |
| Backfire-effect handling | Refuted; a large replication found none | E10.03-K07 | new |
| Bare retraction of a bad hypothesis | Leaves most of the influence; an alternative explanation works far better | E10.03-K06 | new |
| "Wait" or "do not commit yet" instructions to stop early commitment | Did not stop it in MINT; withholding the slot is the untested remedy | E10.03-K12 | new |
| Anti-sycophancy prompts as a general fix | Cut useful updating about as much as harmful updating | E10.03-K16 | new |
| Self-agreement across runs as a stop signal | Runs can agree and be wrong | E10.01-K27 (single-source), G4 | already in G4 |
| Numbers copied from Klein's second-hand sources (up to 3 frames, 3 to 4 anchors, any tau) | Never verified; the sources give no thresholds | E10.01-K25 | new |
| Evaluative AI (show evidence for and against) as a feature | No gain in the first behavioural test; rival result unopened | E10.01-K17 (contested) | new |
| Role-split debate | G9; the one gain had no control | E10.03-K19 | already in G9 |
| Training falsification into the model | Outside the scope of the prompt and scaffold | E10.01-K11 | new |
| Weick's organisational sensemaking (identity, social talk, retrospective stories) | A single agent has none of these | SUBFIELDS.md | new |
| Hard-coding human fixation rates as targets | Rates depend on the denominator | E10.03-K22 | new |

## 7. Gaps

- **Coverage.** Five of seven listed subfields are unresearched. The Pirolli and Card loops (analyst sensemaking) and manipulated sensemaking (S1 hygiene) are the two worth doing next.
- **Founding papers unread.** Klein, Moon and Hoffman 2006 and Klein et al. 2007 were never opened. Chinn and Brewer 1993 and 1998 were blocked (403). Dunbar 1993 and Trickett 2009 not opened. Every statement about what the theory claims is second hand.
- **No tested prediction.** The data-frame theory has only been coded onto transcripts. The Plausibility Transition Model made no tested prediction (E10.01-K18).
- **Independence.** The same LLM papers support claims in both subfields. The independence re-check is pending.
- **Human samples are tiny.** Several effects (noticing high, patching high) rest on 3, 6 or 11 people. A small human panel on our items would show whether the LLM pattern differs.
- **What an anomaly is for an LLM.** Failed check, violated prediction or odd tool output: not defined. Label our logs first (E10.01 open questions).
- **No independent fixation benchmark.** Only mARC, from one group.
- **Token cost.** Most gain figures omit cost, so none can be judged at equal tokens yet.
- **Frontier models.** Several 2026 results name models we cannot cross-check; rerun key arms on the models we deploy.
- **Cross-field.** Compare with A12 (insight), C09 (model-based diagnosis), E08 and E09 when their syntheses exist.

**Audit (code check, 2026-10-26):** E10.01-K25 had only one opened source and are now single-source, not established. Treat their rows above as unconfirmed.
