# How we got here

The thinking behind Epoch, in the order we had it. Every number below is from this repository's own runs and notes;
where a claim is ours and not yet measured, it says so.

## 1. The starting observation

AI agents are very good at general knowledge. Ask one about any field and it answers like a well-read graduate. What
they do not do well is come up with something new: a fact nobody had, a method nobody tried, a result that was not
already in the training data in some form.

And yet there is a spark. In 2026 OpenAI reported that an unreleased model, Astra, run as an agentic system, produced
results on ten long-standing open problems in mathematics (sphere-packing bounds, non-sofic groups, Connes's rigidity
conjecture among them), each with a Lean formalisation; independent review of the proofs was still pending when we
wrote this [1][2]. An Anthropic engineer then reported solving five of the same problems with Claude [3], and a
separate report credits Claude Fable 5 with helping to disprove the Jacobian conjecture, an open problem since 1939
[4]. None of these are Millennium Prize problems, and all of them are claims awaiting review. We took them as a reason
to try: the raw capability seems to be there, and the missing piece is how the thinking is organised.

One part of that organisation already works and is cheap: letting the agent read before it thinks. In Epoch, every
part of a problem gets a web search, newest sources first, and the findings arrive as structured facts with the
mechanism, the measured effect and where it was measured. This is one real entry from a run on 2026-10-18, for the
part "budget-aware prompting" of a problem about coding agents on long tasks:

```
queries:
  budget-aware tool-use agents test-time scaling budget tracker remaining tool calls
  coding agent remaining steps turn budget prompt SWE-agent cost limit awareness
  LLM agent context budget awareness remaining token countdown message long-horizon agents study
known:
  name:      Fixed turn limit with remaining-turn reminders (TRAE Agent)
  mechanism: After every step the agent is told how many turns it has left under a cap set at the
             25th, 50th or 75th percentile of baseline turn counts.
  effect:    At the 75th-percentile cap with reminders, solve rate was Claude 4 Sonnet 71% (baseline 75%),
             Gemini 2.5 Pro 65% (63%), GPT-4.1 57% (62%). Cost fell 23.6%, 68.3% and 38.4%. Without
             reminders at the same cap: 63%, 54%, 54%. So the reminder was worth about 8 to 11 points.
  where:     100-task SWE-bench Verified subset, each configuration run once; results depend on wording.
  url:       https://arxiv.org/html/2510.16786v2
```

(The paper it found is [5].)

The agents that invent ideas for that part see this before they write anything.

## 2. The real problem: thinking in a line

Why does an AI not come up with new ideas? Our answer: its thinking is linear. It talks to itself in tokens, one after
another, and each next token is the most likely continuation of what came before. The most likely continuation of an
idea is the obvious idea. Ask again and you get the same idea in different words. A 2024 study of research ideation
had a model produce four thousand ideas; they collapsed to about two hundred distinct ones [6]. Our own notes on this
are in `research_notes/idea_generation`.

People who are good at inventing do not think in a line. They have schemas: habits of directing thought that were
learned, named and studied. Experts represent a problem by its deep structure, not its surface (Chi, Feltovich and
Glaser, 1981 [7]). Seeing an example first narrows what people produce (Jansson and Smith, 1991: design fixation
[8]). Comparing two analogues and writing down the shared schema roughly doubles the chance of transferring it to a
new problem (Gick and Holyoak, 1983 [9]). People who generate ideas alone and pool them afterwards produce more and
better ideas than a group talking (Diehl and Stroebe, 1987 [10], and the meta-analyses since). The returns on ideas
are fat-tailed: at Bing's experiment platform the top 2 percent of ideas gave about 75 percent of the gains [11], so
the task is to find the best, not the average.

So the question became: what if we take the sciences that study how people direct their thoughts, build that schema
as a fixed script, and let the model only fill in the pieces?

## 3. The schema we built

Epoch is that script. Many separate agents, each with a narrow job, under a plain program that decides every step.
The agents never decide what happens next.

1. **Measure first, then read.** The baseline is measured before any idea exists. Then one reading call looks at
   how the field splits the problem and where it is weak, and reports structure, never fixes, because examples
   shown first narrow production.
2. **Map the problem.** One call draws a tree of parts, each with a frame (how it works today), its assumptions (the
   design choices a different approach could remove) and a boundary. Experts represent a problem by its deep
   structure, so the map is the first thing every later agent sees.
3. **Invent per part, alone.** Each part gets its own idea agents, each on a different card: a different way to look
   (remove, invert, port a known technique and adapt it, analogy with a typed mapping, doubt the map). They work
   independently and never see each other's output, so the pool is wide before anyone judges.
4. **Group.** Ideas are clustered by mechanism, not wording. Many words for one idea become one dot; what is left is
   the real spread.
5. **Argue.** Critics attack the chosen ideas three levels deep; the idea's author answers once, with a fact, a change
   or a test. An answer never blocks a build: the test decides.
6. **Build and test.** The best are built and checked on a ladder of cheap tests before anything expensive, with
   pre-registered rules, placebo candidates and known winners through the same ladder, so the verifier cannot be
   gamed and a false positive has a measured rate.
7. **Remember.** What each part taught, what was tried, what to expect and the dead ends are written per part and
   read first by the next run. The team also proposes its next questions; a person can veto or choose.

People sit inside this: they add facts and files the agents read as evidence, steer the next round, and each has an
agent that reads what the team changed and explains it to them.

## 4. Did it make the thinking better? The benchmark

We tested the thinking schema alone, without any building or training, on NoveltyBench [12], a public benchmark of
creative prompts where ten answers are generated per prompt and judged for how many are genuinely distinct and
how good they are (curated split, 100 prompts, k = 10, the official v1.1 judge prompts).

Same model, Claude Haiku, three ways:

| arm | distinct answers of 10 | utility of 10 | generation tokens per prompt |
|---|---|---|---|
| Haiku, plain | 3.18 | 3.13 | 36,554 |
| Haiku, told in context to be diverse | 8.28 | 6.16 | 39,804 |
| Haiku, our schema | 9.63 | 5.90 | 41,177 |

Our schema against plain Haiku, paired over the 100 prompts: +6.45 distinct answers (95 percent interval 5.99 to
6.88; better on 98 prompts, worse on 0) and +2.77 utility (2.46 to 3.06; better on 95). Against the in-context
baseline: +1.35 distinct (0.87 to 1.88), utility within noise (-0.26, interval -0.71 to +0.19). Token use was 13
percent above plain and 3 percent above in-context; the arms were not capped to equal tokens.

So the same small model, with its thoughts organised by the schema, gave three times as many distinct answers of
nearly twice the quality, for about one eighth more tokens. Two honest notes: the judges were Opus through the
Claude CLI rather than the benchmark's official judge, and the CLI's sampling settings differ from the official
protocol, so the absolute numbers are not comparable with the published table; the paired differences are what we
stand on. The full tables are in `D:\AGI-lab\results\nb` on the lab machine.

A negative result we keep next to it: a variant that forced doubt and reframing on word puzzles made Haiku worse
(about 92 percent to 75 percent on a dev set), because where the first answer is usually right, forced doubt only
costs. The schema helps where the first answer is usually not the best one.

## 5. Then: use it for research

If the schema makes a model's thinking wider and better, the next question is whether a team of such agents can do
research, working alongside people. We gave the team the hardest test we could run on a laptop: improve the strongest
open language-model architecture.

The baseline was the dense skeleton of the strongest 2026 open models (DeepSeek-V4 and Kimi K3), scaled down to 21
million parameters. Every model was trained from scratch on one laptop GPU (RTX 4050, 6 GB) on the same 50 million
tokens of FineWeb-Edu, with the same optimizer, schedule, data order and loss, and graded on 2 million held-out tokens
no training script ever reads. Only the architecture could change. Training ran under a sandbox: no network, no
subprocesses, no access to the exam data.

The team read the skeleton's code and three instrumented runs of its behaviour, drew its map, and ran 24 idea
contexts: 275 sketches, 98 clusters, 10 questioned three levels deep, 19 chosen for building. Each idea was built as
its own file and trained 300 steps on the same seed and data (18 quick tests). Clear winners were combined; anything
neutral, worse, bigger or slower was left out. A prior-art search then judged each winner by mechanism, not name.

What was tested, gap to the skeleton at 300 steps (lower is better):

| helped | gap | hurt or neutral | gap |
|---|---|---|---|
| delay line with signed reads | -0.081 | stream-relative MLP writes | +0.053 |
| depth buckets with an embedding stream | -0.067 | one stream plus a 13th layer | +0.034 |
| delay line | -0.065 | word-frequency prior | +0.021 |
| value residual | -0.050 | attention sink | +0.017 |
| narrow keys, wide values | -0.022 | stronger stream mixing | +0.008 |
| logit soft-cap | -0.016 | gated key-value latent | +0.007 |

What went into the final model, and what it is:

- **Depth delay line**: the skeleton's four parallel residual streams start as a cyclic shift, so stream j holds the
  state j layers back and a layer can read what each recent layer added. New as a combination; a variant of the
  window DenseFormer (2024) gets another way [13].
- **Signed reads**: layers combine the streams with free weights, so they can subtract one stored state from
  another. A variant of Hyper-Connections (2024) [14].
- **Value residual**: every layer mixes its attention values with the first layer's. Known (ResFormer [15], the
  modded-nanogpt speedrun [16]); the team found it by measurement, not by name.
- **Narrow keys, wide values**: 32 key and 96 value dimensions per head instead of 64 and 64. A variant of what
  latent attention already allows; "Thin Keys, Full Values" (2026) shrinks keys the same way [17].
- **Logit soft-cap**: known (Gemma 2 [18]).

The result, at the same parameter count (21.24 million), the same tokens and the same data:

| model | exam loss | change |
|---|---|---|
| frontier skeleton | 4.0939 | |
| skeleton + the team's combination | 4.0281 | -1.6 percent loss, -6.4 percent perplexity |
| the same, hybrid (one stream kept as the raw embedding) | **4.0212** | **-1.8 percent loss, -7.0 percent perplexity** |

One seed; the gap is about twenty times the seed-to-seed spread measured on the plain recipe. On the plain GPT-2-style
recipe, an earlier combination from the same method gave 0.0089 nats, about 0.9 percent lower perplexity, verified
over four seeds.

What the team learned about the architecture is itself a finding: every clear winner restructured the four residual
streams or the flow between layers; ideas that changed the inside of one layer were mostly neutral. The skeleton's
four streams were nearly unused at initialisation, and giving them a job is where the room was. Known speedrun tricks
mostly did not transfer: of four tested, only the value residual helped.

## 6. What this shows, and what it does not

This is the only realistic test we could afford: one model size, one seed on the skeleton rows, 50 million tokens, a
laptop. Gains at this scale do not automatically hold at scale, and a second seed of the final model is the cheapest
next step. Of the ideas with a measured gain, one is new as far as the prior-art search found, four are variants of
published work, two are known.

What it does show: a team of agents whose thinking is organised by a schema taken from the sciences of human
invention produced a measured improvement to the strongest open architecture, found some of it by restructuring
existing methods and some of it from ideas of its own, filtered out the ideas that hurt, and explained what it
learned. The same team, pointed at a folder of notes about a clinic's front desk or a coding agent's failures,
produces ranked proposals with the facts they rest on and the test that would settle each. That is the potential we
are building on.

## Sources

1. The Decoder, 2026: OpenAI announces Astra by releasing ten solutions to previously unsolved problems.
   https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/
2. Zvi Mowshowitz, 2026: OpenAI's unreleased model Astra solves ten major open mathematics problems, with the
   caveats on review. https://thezvi.substack.com/p/openais-unreleased-model-astra-solves
3. The Hans India, 2026: OpenAI claims Astra solved 10 difficult math problems; Anthropic says Fable solved 5.
   https://www.thehansindia.com/technology/tech-news/openai-claims-its-astra-model-solved-10-difficult-math-problems-anthropic-says-fable-solved-5-1104627
4. CoinDesk, 2026-07-21: Claude's Fable 5 and the Jacobian conjecture.
   https://www.coindesk.com/tech/2026/07/21/claude-s-fable-5-just-solved-an-87-year-old-math-problem-and-it-matters-for-bitcoin
5. Turn budgets and remaining-turn reminders for coding agents (TRAE Agent), 2025. https://arxiv.org/abs/2510.16786
6. Si, Yang and Hashimoto, 2024: Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109
7. Chi, Feltovich and Glaser, 1981: Categorization and representation of physics problems by experts and novices.
   Cognitive Science 5(2), 121-152. https://doi.org/10.1207/s15516709cog0502_2
8. Jansson and Smith, 1991: Design fixation. Design Studies 12(1), 3-11.
9. Gick and Holyoak, 1983: Schema induction and analogical transfer. Cognitive Psychology 15(1), 1-38.
   https://www.gwern.net/doc/psychology/1983-gick.pdf
10. Diehl and Stroebe, 1987: Productivity loss in brainstorming groups. Journal of Personality and Social Psychology
    53(3), 497-509. https://doi.org/10.1037/0022-3514.53.3.497
11. Kohavi et al., 2014: Seven rules of thumb for web site experimenters.
    https://www.exp-platform.com/Documents/2014%20experimentersRulesOfThumb.pdf
12. NoveltyBench, 2025. https://arxiv.org/abs/2504.05228
13. Pagliardini et al., 2024: DenseFormer, depth weighted averaging (NeurIPS 2024). https://arxiv.org/abs/2402.02622
14. ByteDance Seed, 2024: Hyper-Connections (ICLR 2025). https://arxiv.org/abs/2409.19606
15. Zhou et al., 2024: Value residual learning (ResFormer). https://arxiv.org/abs/2410.17897
16. modded-nanogpt, the speedrun's hyper-connections port, PR 230. https://github.com/KellerJordan/modded-nanogpt/pull/230
17. Yao et al., 2026: Thin keys, full values. https://arxiv.org/abs/2603.04427
18. Gemma 2 technical report, 2024. https://arxiv.org/abs/2408.00118

The project's own reading on these fields, with many more sources, is in `research_notes/idea_generation`
(twelve briefs and a synthesis), `research_notes/creative_genius` and `research_notes/How the brain generates new ideas`.

## Files

- The benchmark: `harness/noveltybench.py`; results on the lab machine in `D:\AGI-lab\results\nb`.
- The model result: `docs/RESULTS_FRONTIER_MODEL.md`, with the final models in `llmcandidates/`.
- The schema in detail: `docs/HOW_IT_WORKS.md`, `docs/TEAM_OF_RESEARCHERS.md`, `docs/MAPPER.md`.
- The research behind the schema: `research_notes/idea_generation` (twelve fields and a synthesis),
  `research_notes/How the brain generates new ideas`, `research_notes/creative_genius`.
- An example run on a folder problem: `examples/RESULTS-agent-long-tasks-2026-10-18.md`.
