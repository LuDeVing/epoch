# Critique: planned versus emergent strategy (E17.05)

## Numbers re-opened against the arXiv PDFs
Confirmed: ReAct ALFWorld 71 / 45 / 37 and worst-trial 48, gain 33-90% mean 62 (a18, c01). Reflexion 22% absolute on ALFWorld, hallucination plateau 22% (a21, c03, c04). ADaPT ALFWorld 71.6 / 57.5 / 43.3, WebShop P&E 17.0 and ReAct 32.0, TextCraft depth 2 26.9 to 78.2 and depth 3 1.8 to 38.7 (a20, b17, c07). TravelPlanner GPT-4 0.6% (c12). PlanBench GPT-4 206/600 = 34.3%, Mystery 26/600 (c10). Vending-Bench 2,217.93 / min 476 / human 844.05 / 102 and 67 days (b11, c17). ReWOO 64% fewer tokens, +4.4, 40.8 vs 42.4, 9795 vs 1986 tokens (b18). Csaszar +0.14 SD p<0.001, accept +5 p=0.003, 309 plans, 250 evaluators, 2,500 evaluations (a23).

## Corrections
1. a22 says "no planner 9.85%". In the Plan-and-Act table 9.85 is the UNTUNED base executor. The fair no-planner baseline is the fine-tuned executor at 36.36 / 36.97 (c05 has this right). So: static planner adds about 6.7 points (36.97 to 43.63), dynamic replanning a further 10.31 (to 53.94), CoT to 57.58. a22's implied planner gain (9.85 to 43.63) is overstated. Claim K09 uses the corrected reading.
2. c05 and c06 name the authors "Wang et al."; the first author is Erdogan (Erdogan, Lee, Kim et al.). c06's "+34.39 (9.85 to 44.24)" mixes untuned and planner-trained rows; treat as a planner-training effect, not planning in general.
3. a23 lists "+3 points invest p=0.007" and drops that interest in introduction (+3 pts) has p=0.094, not significant. The 2.55 is on a 0-100 scale, so the investment effect is about 2.6 points. c20 is right.
4. b19 says TravelPlanner best prompting 0.7% (GPT-3.5); c12 says GPT-4 0.6%. Both appear in the PDF tables (0.6 and 0.7); they are different models, not a contradiction.
5. a14 attributes the five Ps to 1998 (Strategy Safari) while the primary literature dates them 1987; keep the 1987 date.
6. c05 table 1 labels vary across a22/c05; the ReAct paper reports WebShop 40.0 (a18) while c01 cites 28.7 for IL+RL; different rows, not conflict.

## Contradictions and weak spots
- Planning vs learning at firm level: Mintzberg (qualitative, two cases) vs meta-analytic positive planning effect (b04). Effect size never opened; b22 (Miller and Cardinal 1994) not opened. The human-strategy side of this dossier is the weakest.
- Almost all human-side lines are metadata (Crossref citation counts, Wikipedia). Mintzberg and Waters (1985) full text was never read (a04, a05, b01 blocked). Pascale/Honda, Quinn, Brews and Hunt, Levinthal were from memory (opened:false).
- Entrepreneurship planning papers (b05-b07, b23, b24) unopened; sample sizes are recalled, not verified.
- LLM side is rich but tests plan-vs-react, not strategy in the Mintzberg sense. Models differ (PaLM-540B, GPT-3.5, Llama-70B fine-tuned), so cross-paper ranking of "planned vs reactive" is not valid; only within-paper ablations are.
- Single-source for the strongest planning-vs-replanning claim (Plan-and-Act), and it needs fine-tuning.
- Snippet-only: c24 (Strategy Science 2026), c25 (trendslop), a28; b14/b15/b16 (2026 benchmarks, one run per scenario, small samples) are fragile.
- Vending-Bench human baseline is one run.

## GAPS
1. Does keeping an explicit written intended plan and diffing it against the realized action trace (the Mintzberg gap) improve long-horizon task score at equal tokens versus no plan or plan-only?
2. What is the effect size and moderator structure in the George, Walker and Monster (2019) planning meta-analysis (and Miller and Cardinal 1994, Brinckmann 2010)? Are effects weaker in dynamic environments?
3. When should the agent replan: every step, on failure, or on surprise? Need an equal-token test, not Plan-and-Act's fine-tuned setting.
4. Do unplanned successes found during execution help if promoted into the plan (Burgelman/Honda mechanism), measured in any LLM agent study?
5. What does Mintzberg and Waters (1985) actually claim in the full text (eight types, how deliberateness is measured)? Needs the paper or a faithful summary.
6. Does Reflexion-style note memory help only with a hard verifier, and what happens with vague feedback on strategy-like tasks (S9 target)?
7. Do the 2026 business-game benchmarks (EcoGym, CEO-Bench, EnterpriseBench, Ovezmyradov) show plan-vs-react differences by model, with more than one run per setting?
8. What did Camuffo (2020) and Koning (2022) measure about scientific/experimental strategy versus planning in startups, with real N and effects?
9. Is there any study on LLM "trendslop" or strategic-advice bias (2026) with numbers that bears on over-planning or fashionable advice?
10. How does plan commitment (momentum) interact with detecting an outside signal to break pattern, and can that be operationalized as a trigger in the scaffold?


## Gap search results
Evidence is in evidence_d.jsonl (d01-d22). New claims K18-K26; K02, K03, K09, K13, K14, K16, K17 got extra evidence ids, K03 now states the effect size. Search budget: WebSearch was used 3 times (the shared budget then ran out); the OpenAlex, Semantic Scholar and arXiv search APIs returned HTTP 429, so arXiv PDFs were fetched directly by id.

1. Explicit plan diffed against the action trace at equal tokens: STAYED OPEN. No controlled study found. Nearest: AdaPlanner (d15, plan with predicted observations, rewrite on mismatch), CEO-Bench weekly plan memo (d11, correlational), MAST drift modes (d22). Claim K26 holds the proposed three-arm test.
2. Meta-analysis effect sizes: CLOSED for George et al. 2019 (d01, d02: r = .229, CI .186-.271, k = 87 in 31 studies, I2 91.6%; moderators listed). Dynamic-environment moderator: not tested there; Hamann et al. 2023 (d03) says the effect is larger under high uncertainty, abstract only. Miller and Cardinal 1994 and Brinckmann 2010: STAYED OPEN (paywalled, d04 metadata only).
3. When to replan, equal-token test: STAYED OPEN. Only the trigger design (AdaPlanner mismatch) was found; no equal-token comparison.
4. Promote unplanned successes into the plan: PARTLY CLOSED. AdaPlanner skill discovery (d16), AWM (d20), ExpeL (d19) all help where a verifier exists (K22). No test in business strategy.
5. Mintzberg and Waters 1985 full text: PARTLY CLOSED. Abstract confirms continuum and the eight types (d07). Full text blocked (HTTP 403); how deliberateness is measured is still not verified.
6. Reflexion-style memory and vague feedback: CLOSED for the direction (d17, d18, d19, d14, K21): help needs a hard check; on rubric-judged consulting cases Reflexion and Self-Refine stay below CoT.
7. 2026 business-game benchmarks with more than one run: MOSTLY CLOSED. CEO-Bench (3 runs per model), EcoGym (5 and 3 runs), EnterpriseBench (4 backbones), Can-LLMs-Be-CEOs (1 run, so weak) (d10-d14, K24). EnterpriseBench run counts per cell were not found. None directly compares plan versus react.
8. Camuffo 2020 and Koning 2022: PARTLY CLOSED. Camuffo N = 116 startups, 16 data points, performance and pivots up, no extra dropout (d05); Koning abstract gives direction only (d06). Numeric effect sizes were not seen in either.
9. Trendslop: PARTLY CLOSED. HBR study known only through a search summary (d08, opened false); a Zenodo pilot gives 240 runs and model-specific numbers (d09). Original numbers unverified; the 11% figure stays unverified.
10. Plan momentum and outside-signal trigger: PARTLY CLOSED. Early commitment is documented (d21: 39% drop, unreliability +112%) and the integration-boldness trade-off (d13). No published trigger. K23 and K26 propose tests.

Net: closed 6 and the George et al. part of 2; mostly closed 7; partly closed 4, 5, 8, 9, 10; open 1, 3 and the older meta-analyses in 2. Caution: CEO-Bench, EcoGym and similar 2026 papers were read from their PDFs only and not cross-checked elsewhere.
