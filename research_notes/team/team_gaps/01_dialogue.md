# Gap 01: Should the author answer the critic? (two-way dialogue)

Date: 2026-10-17. Method: abstracts fetched live (V = verified on the arXiv abstract page). Everything marked M is from memory and must be checked before it is quoted. Full-paper tables were NOT opened.

## Bottom line

Free-form debate between equals gives small, unreliable gains over cheap baselines (self-consistency, one strong prompt). Dialogue helps most when it is anchored to something checkable: a tool result, a quote, a test. Without that anchor, models agree with each other, or talk themselves out of right answers. For HTSA, a long argument is not worth it. One short, anchored reply round is.

## Evidence table

| # | Claim | Evidence | Numbers | Source URL | Status |
|---|---|---|---|---|---|
| 1 | Debate beats single-shot on math and facts | Du et al 2023: several model copies answer, read each other, revise over rounds. Same prompts across tasks. | Abstract: "significantly enhances" reasoning, "reduces fallacious answers". Table values (roughly arithmetic 67 -> 82, GSM8K 77 -> 85) are M. Typical setup 3 agents, 2 rounds (M). | https://arxiv.org/abs/2305.14325 | V (qualitative), M (numbers) |
| 2 | Debate helps a weak judge find truth, if debaters are strong | Khan et al 2024: judge sees two debaters, one defending the truth. | Non-expert LLM judge 76% with debate vs 48% naive. Human judge 88% vs 60% naive. Consultancy (one-sided) was worse than debate (M, no number). More persuasive debaters raised judge accuracy. | https://arxiv.org/abs/2402.06782 | V |
| 3 | Debate counters "degeneration of thought" | Liang et al 2023: self-reflection locks in once confident. Two debaters plus a judge. | Gains on counter-intuitive arithmetic and translation (no numbers on page). Works only with adaptive stopping and moderate "tit for tat". LLM judges favour same-model debaters (bias). | https://arxiv.org/abs/2305.19118 | V (no numbers) |
| 4 | Irving 2018: debate is a safety proposal; truth wins if the judge can check a small piece | Theory plus MNIST toy: judge sees a few pixels the debaters pick. | Sparse classifier accuracy 59.4% -> 88.9% with debate on 6 pixels (M). | https://arxiv.org/abs/1805.00899 | M |
| 5 | Debate is not reliably better than cheap baselines | Smit et al 2024: compare MAD protocols to self-consistency and ensembling. | No consistent win. MAD is sensitive to hyperparameters. Tuned "agreement level" can beat all non-debate protocols. | https://arxiv.org/abs/2311.17371 | V |
| 6 | One good prompt matches discussion | Wang et al 2024: single agent with strong prompt vs best discussion method. | Near equal. Discussion wins only when the prompt has no demonstrations. | https://arxiv.org/abs/2402.18272 | V (no numbers) |
| 7 | Self-correction without outside feedback fails on reasoning | Huang et al 2023. | Abstract: performance "even degrades". Table: GSM8K about flat (75.1 -> 74.7), CommonSenseQA falls a lot (about 75.8 -> 38) with GPT-3.5 (M). | https://arxiv.org/abs/2310.01798 | V (direction), M (numbers) |
| 8 | Debate collapses to the majority, right or wrong | Estornell and Liu 2024 (shared misconceptions, majority pressure); Wynn et al 2025 "Talk isn't always cheap" (right agents flip to wrong under peer pressure); sycophancy literature. | No number I can quote. | search "Multi-LLM Debate: Framework, Principals, and Interventions" and "Talk Isn't Always Cheap" | M, not opened |
| 9 | Critic with tools beats critic without | CRITIC: model checks its own output with search or code interpreter, then revises. | Abstract: "consistently enhances". Paper shows tool feedback is the part that matters; no-tool self-critique gave little or negative gain (M). Kamoi et al 2024 survey agrees: self-correction works with reliable external feedback (M). | https://arxiv.org/abs/2305.11738 | V (claim), M (ablation) |
| 10 | Refine loops: gains fade fast | Self-Refine: about +20% absolute average across 7 tasks, mostly round 1-2 (M). Reflexion: HumanEval 91% pass@1 vs 80% GPT-4 baseline, with unit-test feedback as the signal (M). | Most gain in first revision, little after round 2-3 (M). | https://arxiv.org/abs/2303.17651 ; https://arxiv.org/abs/2303.11366 | M |
| 11 | AI reviewer roughly matches human reviewers on accept/reject | AI Scientist reviewer. | Abstract: "near-human". Balanced accuracy 0.65 vs 0.66 human, F1 0.57 vs 0.49 (M). Ceiling is low: human to human agreement is also modest. | https://arxiv.org/abs/2408.06292 | V (claim), M (numbers) |
| 12 | Do rebuttal rounds change the verdict? | No strong LLM-only evidence found. In human review, rebuttals move scores a little (small share of papers change; M). NeurIPS consistency experiments show review noise is large (M). | Not quantified. Treat as unknown. | not fetched | M, gap |
| 13 | Authentic dissent changes minds; assigned devil's advocate does not | Nemeth et al 2001: authentic minority dissent raised divergent thinking and new solutions. Assigned devil's advocate made people defend their first view more (M). | Effect sizes not recalled. | Nemeth, Brown, Westwood 2001, Eur J Soc Psych | M |
| 14 | In real labs, reasoning is distributed and driven by unexpected data | Dunbar 1995/1997 in-vivo study of 4 molecular biology labs: a large share of findings were unexpected; lab meetings with analogy and disagreement reinterpreted them; the data, not the argument alone, triggered change (M). | About half of results were unexpected (M). | Dunbar, "How scientists really reason", 1997 | M |

## What this means for HTSA

- Our critic finds planted flaws 4 times in 5 but also attacks good ideas. High recall, low precision. An unanchored critic plus an unanchored author gives a tie, or collapse to whoever sounds surer.
- Our earlier finding (anchored comparison works, unanchored self-judging rationalises) matches rows 7, 9 and 2: the gain comes from a concrete anchor.
- Our objective test is the strongest anchor there is. Real labs (row 14) change their minds on data, not on talk alone.

## Ranked: what to adopt

1. **One anchored reply round, author to critic, then build.** Author answers each objection with one of three typed moves: (a) concede and change the plan, (b) rebut with a quoted fact from the code or task, (c) propose a measurement that would settle it. No free prose debate. About one extra call per idea. Evidence: rows 2, 9, 10 (gain is mostly in the first revision).
2. **Turn every unresolved objection into a test.** The critic's reply to a type (c) move is only: "that settles it" or "that does not settle it, because X". Then the builder runs it. The critic stays a checklist, not a gate.
3. **Critic sees test results AFTER its first objections, then amends.** First pass is blind to results (keeps recall clean, avoids anchoring on success). After the test, a short post-mortem records which objections the result confirmed or refuted. Log it as calibration data (precision per objection type). Row 14 supports data-triggered updating.
4. **Cap at 2 exchanges; stop early when nothing changes.** Rows 3 and 10: adaptive stopping, fast diminishing returns.
5. **Keep the critic a fixed role whose job is to find flaws; do not rotate in a role-played devil's advocate.** Row 13: assigned dissent hardens views. Our critic has measured recall, the nearest thing to authentic dissent.
6. **Run the cheap baseline arm.** Same ideas, no dialogue, objections as checklist, versus one reply round. Adopt only if the objective test favours the reply round. Rows 5 and 6: debate often loses to self-consistency at equal cost.

## Avoid

- Open-ended multi-round debate between same-model agents. Shared blind spots, majority collapse, sycophancy (rows 5, 8).
- Letting the critic update on the author's confidence or rhetoric. Require a quoted fact or a measurement.
- Using the reply as a gate: a persuasive reply must not skip a test, and a failed rebuttal must not block a build. Measurement decides.
- An LLM judge from the same model as a debater (row 3 bias).
- Counting critic approval as evidence of quality. The critic hits good ideas as hard as bad ones, so agreement is noise.
- Quoting any M number in a report before checking it against the full paper.

## Open gaps

- Full-paper tables were not opened (Du, Huang, CRITIC, AI Scientist, Self-Refine).
- No clean study found of LLM rebuttal rounds changing a review verdict. We could measure it ourselves: A/B on our own ideas.
- Nemeth and Dunbar numbers are from memory.
