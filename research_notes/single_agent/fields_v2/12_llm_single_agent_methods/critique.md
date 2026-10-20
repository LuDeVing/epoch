# Critique: single-agent LLM reasoning methods

## What the set supports
- Self-correction without outside feedback does not work (5 papers). With a real checker it works. This fits our ARC and word-puzzle losses: our doubt step had no checker.
- CoT helps on math and symbolic tasks (Sprague meta-analysis). It can hurt where deliberation hurts people (one study).
- Longer thinking can hurt, and reasoning models overthink easy items. Two lines, both partly preprints.
- Written reasoning is often not the real cause of the answer (3 papers). Do not use it as proof.
- Debate and multi-agent gains are weak. Fine for us: we use one agent.

## What is missing
1. Almost nothing tests OPEN-ENDED quality, where our schemas won (NoveltyBench 3.18 to 9.63). No source here explains why forced divergence helps or when it stops. Diversity-prompting and creativity-benchmark work is absent.
2. No equal-token comparisons. Tree of Thoughts, Self-Refine, Self-Discover and Reflexion use weak baselines. Our data shows a method can win on accuracy and lose at equal cost.
3. Thin evidence on modern models. Most gains come from the GPT-3.5, GPT-4 and PaLM era. Only Meincke, Gema and Shojaee use current reasoning models.
4. Nothing on WHEN to switch a scaffold on. Our key finding is task-dependent. Router and difficulty-estimation work is only touched through Snell, which needs a trained PRM.
5. Verifier-free selection among samples is the exact gap our correlated-sample problem creates. Only Brown's plateau note speaks to it.

## What could be wrong
- Counting: the a, b and c files re-fetch the same 25 or so papers. I counted papers, not lines, so independent-source counts are small. Several "established" labels rest on 2 to 5 papers from one community.
- Almost every line is abstract level. No table numbers were checked in full text. Headline numbers (+17.9, 4% to 74%, 91%) are each paper's best case.
- Shojaee (Apple) drew public criticism of its puzzle setup (output limits). I could not verify the rebuttals from this set, so treat it as contested in practice.
- Gema tasks are synthetic. Liu covers six tasks. Both may not transfer.
- Reflexion uses external feedback; Self-Refine conflicts with later work. Credibility lowered.
- Kim et al. (60% shared wrong answers) is one leaderboard.

## Memory or snippet only
12-c-02 is a search summary. The old brief's claims "CoT gains only above about 100B parameters" and the Graph of Thoughts and LATS numbers are not confirmed here. Wang 2022 numbers come from the abstract.

## Effect on agent design
Use a checker or external feedback before any doubt step. Use CoT for math, symbolic or multi-step items only. Cap thinking length. Do not trust agreement between samples. For open tasks, rely on our own divergence result, which this field does not explain.
