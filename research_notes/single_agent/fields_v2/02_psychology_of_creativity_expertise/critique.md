# Critique: psychology of creativity and expertise

## What the evidence supports
- Fixation on a familiar solution is real in humans (chess, two labs) and now shown in LLMs (preprints). It fits our own finding that samples from one model are correlated.
- Forced divergence helps where the task is open. The expertise literature adds a limit: when the familiar answer is a clear failure, people switch by themselves. Doubt should be triggered by a failure cue, not run on a schedule.
- Practice explains less of skill than the popular story says, but the size is disputed.

## What is missing that could change the agent design
1. No evidence on when the first answer is right. Our ARC and word-puzzle losses are the opposite case from Einstellung. The set has no human work on when to trust the first answer (fast intuition by experts, recognition-primed decisions, Klein; Kahneman and Klein on valid intuition). This is the largest gap, since it decides when to turn the schema off.
2. Nothing on evaluation. Creativity needs selection as well as generation. The Si 2025 execution result says novel ideas fail later. We have no source on how judges (human or LLM) pick good ideas, or on the cost of weak selection.
3. No evidence on the structure of expert problem solving beyond chess: how experts represent a problem before solving (Chi 1981 only, snippet).
4. Incubation is one meta-analysis. There is no test of an LLM analogue (a break, a re-prompt from scratch, a context reset).
5. Group work: only brainstorming. Nothing on structured disagreement, devil's advocate, or nominal-group-then-merge, which map to multi-call agents. The one claim that the group penalty can be removed is a search summary.

## What could be wrong
- Chess is one domain with clean right answers. Einstellung there may not transfer to open design or writing.
- LLM fixation claims are mostly 2026 preprints read at abstract level. Effect sizes are unknown.
- "Stronger models fall into traps less" (one preprint) could mean our forced-doubt gain shrinks with newer models. Our own measurements were on a specific model; they need a re-run when the model changes.
- The Macnamara line has overlapping authors. Three of the four deliberate-practice sources share a lead author, so "established" is softer than it looks.
- Persona results conflict (Huang vs Deng) and use different measures.
- The "Weisberg ordinary thinking" claim is a theory. Do not build a step on it.

## Claims that rest on memory, snippets or secondary summaries only
Getzels problem finding; Intelligence-creativity r=.17 (Kim); Luchins; Chase and Simon; Gobet and Simon; Chi 1981; Mullen 1991; Jansson and Smith; Derosa 2007; Feist 1998 (a-17, unused in claims); the Bilalic 2008 original. Unusable: 02-c-24 (no author, credibility 0), 02-c-21, b-13.

## Transfer risks
- Problem finding has no LLM test. Treat it as a hypothesis to measure, on open tasks only.
- Incubation, as a reset of context, is cheap to test.
- A rule that switches strategy on a failure cue needs a cue the agent can see. For single-answer tasks it often has none.

## Suggested measurement
Compare three arms on both task types: plain, always-doubt, and doubt-on-cue (only when a check fails or two independent samples disagree). Prediction from this field: doubt-on-cue should keep the open-task gain and avoid most of the single-answer loss.
