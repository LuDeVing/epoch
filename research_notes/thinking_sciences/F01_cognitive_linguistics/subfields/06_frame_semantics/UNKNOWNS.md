# Frame semantics: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| F01.06-U1 | Does writing the task as a frame (roles listed, blanks flagged) beat plain restatement on underspecified tasks? | A frame-listing step in S1/S2 | S1/S2 | K01 established as theory; K22 untested as scaffold; annotation-only evidence (b02, c07) | 60 tasks, 1-3 planted missing roles. Arms: plain restatement vs frame step. Metric: recall of planted gaps and final accuracy | Gap recall up 10+ points and final accuracy not lower, at equal tokens | High |
| F01.06-U2 | Does a role-based gap check beat a generic "what is missing" gate? | Role-checklist gate instead of generic gate | S1/S2 | Gap 2 untested; d07 gates are generic; d11 slot ontology indirect (single-source) | Same 60 tasks. Arms: role-list gate vs generic missing-info gate vs two extra attempts. Metric: gap recall, false positives on specified controls, accuracy | Role gate beats generic by 5+ points recall with false positives no worse | High |
| F01.06-U3 | Is a separate gate better than an inline reminder, and does the gain survive equal tokens? | Separate ask-or-assume gate call | S2 / ask-or-assume | K17: +8.2 points at 1.5-1.7x cost (d05, d06); single paper, SWE-bench, two models | 40 underspecified plus 20 specified tasks. Arms: inline reminder, separate gate, inline plus extra attempts at the gate's cost. Metric: accuracy, false positive rate | Gate beats the cost-matched arm by 4+ points accuracy | High |
| F01.06-U4 | Does asking (or labelling an assumption) raise final accuracy, not only asking rate? | Mandatory ask-or-labelled-assumption after a gap flag | S2 / G | K20: asking 0.52 to 0.90 but final answer 0.34 to 0.36 (d12) | Items where a simulated user supplies the role. Arms: guess, labelled assumption, ask. Metric: final accuracy | Ask or assume beats guess by 5+ points final accuracy | High |
| F01.06-U5 | Does an explicit peripheral-role list (means, instrument, time, place, cause, constraint) raise recall of planted peripheral gaps? | Fixed peripheral slots in the frame template | S1 | K07 established on annotation; b03 per-role F1 for 2025 models only; frontier models unmeasured (d16) | 30 tasks with a planted peripheral gap. Arms: core-only vs core plus peripheral slots. Metric: recall and precision of that gap | Recall up 10+ points with precision drop under 5 points | High |
| F01.06-U6 | Is the frame benefit frame-specific, or does any role list do as well? | FrameNet-style labelling only if it wins | S1 | K12 contested: WordNet matched FrameNet (c15); no role-list control exists (d17) | Same tasks. Arms: frame-labelled roles vs generic bullet slots vs nothing. Metric: gap recall, accuracy | Frame-labelled beats generic slots by 5+ points; else use generic slots | Med |
| F01.06-U7 | Does "absent" as a legal value in the role JSON cut invented fillers? | JSON template with stated/inferred/absent | S1 / G | K08 single-source: JSON-exist 0.471 vs XML 0.342; JSON-all precision 0.356 (b12) | 40 tasks. Arms: absent allowed vs all slots must be filled. Metric: precision of filled roles | Precision up 5+ points without recall loss over 3 points | Med |
| F01.06-U8 | Does tagging each filler stated or inferred cut silent wrong assumptions? | Stated/inferred tag, code-checked against task text | G | K21 human-only and second hand (d14, d15) | 40 tasks where a plausible wrong fill exists. Arms: tag required vs not. Metric: wrong inferred fills used unchecked; accuracy | Wrong silent fills down by a third, accuracy not lower | Med |
| F01.06-U9 | Does a neutral re-framing step reduce framing flips in frontier models? | Neutral restatement guard in S1 input hygiene | G / S1 | K16 contested: DeFrame works at 3B-14B (b27); FRAGILE says text fixes fail at 7-8B (d08); frontier untested | 30 paired gain/loss/neutral tasks. Arms: none, neutral restatement, DeFrame-style 4 steps. Metric: flip rate vs paraphrase noise floor | Flip rate falls 5+ points more than paraphrase baseline | Med |
| F01.06-U10 | Can the model write its own frame definition as well as a retrieved one? | Self-written frame definition at S1 | S1 | K10 single-source, frame ID only (b08); GPT-4o instructions scored 0.225 vs 0.471 (a21) | 30 tasks. Arms: self-written vs fixed template definition. Metric: gap recall; tokens | Within 3 points of fixed template at lower tokens | Low |
| F01.06-U11 | Do filled-frame exemplars beat more definitions? | Exemplar block in the S1 template | S1 | K06 single-source: shots +30 to +41 on roles (b05) | 30 tasks, matched tokens. Arms: definitions only vs one filled exemplar. Metric: gap recall | Exemplar arm wins by 5+ points | Low |
| F01.06-U12 | Does a frame step anchor later attempts (fixation) at S3? | A rule to hide the frame from attempt contexts, or keep it only in S2 | S3 / G | No frame study; SCHEMA S3 rationale | 40 tasks. Arms: attempts see frame vs attempts see bare task. Metric: attempt diversity, accuracy | Attempt diversity or accuracy better when frame is hidden by 5+ points | Med |
| F01.06-U13 | Does frame template trust fall off in unusual domains, so the S0 gate should switch it off? | Domain flag in S0 that skips the frame step | S0 | K09 established for annotation (a24, b09); not tested on reasoning | 30 usual and 30 unusual-domain tasks. Arms: frame step vs plain. Metric: accuracy by domain | Frame step loses on unusual tasks by 3+ points | Low |

## Open questions we cannot test on our bench yet

- Fillmore's primary 1976-1985 papers were never opened. Needs library access or a scan; unblock by finding the Seoul 1982 text or a reprint.
- Bower, Black and Turner 1979 numbers on script inference: PDF blocked (403). Unblock with another copy.
- 2026 frontier per-role F1 for peripheral roles (GPT-5, Claude 4.x, Gemini 2.5+): none published. Unblock by running a small annotation probe ourselves on the Killing frame set.
- Whether FrameNet frames help on agent planning benchmarks: no study; needs a planning bench with planted gaps.
- Real-user (not simulated) missing-information rates: all ask-or-assume results use LLM-simulated users and synthetic gaps.
- Hidden-state framing fixes need open weights; not testable with an API agent.
- EMNLP camera-ready of Devasier et al. not opened; numbers could differ from arXiv.
- Human data on whether people list roles before solving: none exists.

## Order to run

1. U1 with U2 on one shared item set: cheapest, and decides whether the frame step is worth anything over a generic gate.
2. U3 (and U4): the separate gate has the best published support (+8.2 points) but its cost is not tested at equal tokens.
3. U5: a one-line template change with the clearest evidence (peripheral roles missed most), so a quick win or quick drop.
