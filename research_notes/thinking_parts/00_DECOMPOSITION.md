# Thinking, decomposed into parts

*2026-10-14. The HTSA method applied to thinking itself. The map below is drawn through the lens "the faculties a thinker uses between meeting a problem and knowing an answer". For each part: what the loop does today, the assumptions behind it, which code owns it, and the weak points already known. Research agents take one part each (briefs 01–12 in this folder); the synthesis of improvement ideas is 00_IDEAS.md.*

Already researched and should not be repeated: the twelve field briefs in `research_notes/idea_generation/` (summarised in `00_SYNTHESIS.md` there), the two reports on human thought in `reports/`, and the 137-mechanism catalogue in `research_notes/mechanism_catalog.md`. The question for each part now is narrower: *how do strong thinkers and the best 2024–2026 systems do THIS part, where is our implementation of it weak, and what concrete change follows.*

---

## 1. Representation: how the problem is encoded

**Today.** A problem file (goal, measured baseline, seven rules), a map of parts drawn once per run through a lens (`nano/tree.py`), each part with a frame, assumptions and a code boundary; a diagnostics table of how the baseline behaves (`nano/diagnose.py`); the script itself, in full, in most prompts.
**Assumptions.** One textual encoding fits every agent. Parts are regions of code. The map is drawn once. The full script is the right level of detail for every call. Numbers in a table are the right form for diagnostics.
**Weak points.** The same encoding for a sketcher, a questioner and a builder; no alternative encodings (dataflow graph, cost table, dependency structure); nothing re-encodes a stuck problem.

## 2. Attention and framing: what gets looked at, in what order

**Today.** Coverage by round-robin over parts and directions (inward, outward, upward); cards as ways in; lenses rotate by replicate; exclusion lists and skip lists; a discovery curve retires attractor cards (`nano/loop.py ideate_round`, `nano/novelty.py`).
**Assumptions.** Equal attention per part is right. The card set is fixed. Framing is set before thinking starts and does not move during a round.
**Weak points.** No notion of where the problem's leverage is; no re-framing on failure inside a round; attention is allocated by a schedule, not by evidence.

## 3. Memory: what is kept, and what reaches whom

**Today.** Within a run: history text (what was built and what happened), facts from interrogation, objections, discovered assumptions, caches. Across runs: research briefs (7 days), the experiments ledger (verdicts), a verdict memory keyed by source hash, promoted baselines. Retrieval is "the whole block for the part" (`nano/research.py`, `nano/loop.py history_text`, `nano/deepen.py knowledge_text`).
**Assumptions.** Memory is text blocks. Relevance is by part id or by recency. Everything a later agent might need can be pasted into its prompt.
**Weak points.** No retrieval by similarity or by need; no consolidation (facts never get merged or contradicted); no forgetting policy; no episodic memory of *how* a win was found.

## 4. Generation: producing candidates

**Today.** Independent sketch agents, 5 to 8 sketches each, from different ways in; interrogation offshoots; staged sketching as an arm; program-space search as an arm; composition by script (`nano/ideate.py`, `nano/loop.py`, `nano/compose.py`).
**Assumptions.** Variation comes from inputs. Sampling is left to the model. A sketch is five lines of text. The right unit of generation is "an idea for one part".
**Weak points.** Collapse onto a few modes (measured in the literature at ~5% unique); no explicit operators beyond cards; no generation at the level of mechanisms or of experiments rather than code changes.

## 5. Abstraction and analogy: moving between levels

**Today.** An analogy research call per part and an analogy card with a typed mapping; the map's frames and assumptions as the abstract level; "what is this an instance of" is not asked anywhere (`nano/research.py analogy_*`, `nano/ideate.py MAPPING_FORMAT`).
**Assumptions.** Analogues are found by a web search from the part's description. One mapping per sketch. Abstraction happens inside a single call.
**Weak points.** No schema library; no explicit "abstract the problem, then search" step; no reuse of abstractions across runs; no checking that a mapping is structural rather than lexical beyond a lint.

## 6. Elaboration and reasoning: working an idea through

**Today.** Interrogation chains: as many questions as needed, answers with facts, assumptions, offshoots, open questions marked build-relevant, followed two levels down; facts go to the builder; the builder reasons in one call writing a whole file (`nano/deepen.py`, builder prompt in `nano/loop.py`).
**Assumptions.** A question list covers the aspects. Depth 2, fan-out 1. Facts as bullet text. The builder can hold the whole script and the idea at once.
**Weak points.** No explicit model of the mechanism (why it should work, as a causal chain that can be checked piece by piece); no simulation or back-of-envelope calculation step; no decomposition of the build into steps with checks.

## 7. Critique and doubt

**Today.** Pre-mortem calls (one to three evidence packs) producing objections by severity; prediction tracking against measurements; fidelity probes; placebo and positive controls (`nano/deepen.py premortem_*`, `nano/predict.py`, `nano/controls.py`).
**Assumptions.** Doubt is a separate agent's job. Objections are text the builder reads. A prediction is a number to compare.
**Weak points.** Objections are never resolved, only forwarded; no adversarial *test* is generated from an objection; no calibration of the critic itself (does it predict failures?).

## 8. Judgement and selection

**Today.** A weighted score over angles, novelty, failure, obviousness, departure, cheap test, size and metric-blindness; a long-shot lane; a novelty gate; weights from the ledger once data exists (`nano/ideate.py select_clusters`, `nano/tree.py split_select`, `nano/calibrate.py`).
**Assumptions.** A linear score is enough. Coverage across parts is a good proxy for a good portfolio. The ledger will eventually calibrate the weights.
**Weak points.** No portfolio reasoning (ideas chosen one at a time, not as a set); no cost awareness in the score (build cost, verification cost); no value-of-information ordering.

## 9. Control and planning

**Today.** Fixed rounds; a token budget; stage markers; a control file for pause, stop, skip and notes; resume; allocation of calls between stages fixed by flags (`nano/loop.py _rounds`, `_stage`, `load_state`).
**Assumptions.** Two rounds is right. The split of effort between research, sketching, questioning, building and testing is the same for every problem and every round. Stopping is by budget or rounds.
**Weak points.** No stop rule based on yield; no reallocation when a stage is unproductive; no plan at all, only a schedule.

## 10. Learning and adaptation

**Today.** History and discovered assumptions inside a run; ledger verdicts and sourced facts into the briefs; selection weights from the ledger; promotion of winners into the baseline; retirement of attractor cards (`nano/calibrate.py`, `nano/promote.py`, `nano/research.py ledger_entries`).
**Assumptions.** Learning is text injection plus a few weights. Credit goes to ideas, not to the processes that produced them. Lessons are not written anywhere as lessons.
**Weak points.** Nothing learns which *questions*, *cards* or *analogies* led to wins; no post-mortem of a run; no transfer of lessons between problems.

## 11. Metacognition: knowing what one does not know

**Today.** A discovery curve and a collapse alarm; budget estimates per call; an "unknown" allowed in interrogation answers; abstention exists in the puzzle harness, not in the nano loop (`nano/novelty.py discovery`, `nano/deepen.py`).
**Assumptions.** Stagnation shows in cluster counts. Confidence is not needed because measurement decides.
**Weak points.** No confidence attached to ideas, facts or predictions; no detection of "we keep proposing the same family"; no decision to stop, widen, or change the problem; no awareness of its own biases (homogenisation, anchoring) beyond the collapse alarm.

## 12. Communication and steering

**Today.** A live dashboard, a per-run report with the funnel and controls, the plain-language documents, a control file for steering (`nano/dashboard.py`, `nano/report.py`, `docs/`).
**Assumptions.** A human reads the report after the run. Steering is coarse (pause, skip, note).
**Weak points.** No explanation of *why* an idea was chosen or dropped in human terms; no way for a human to inject a hunch into the right part at the right stage; no summary that a newcomer could act on.
