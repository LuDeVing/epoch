# Scenario evidence: deep document

*Subfield E17.03. Sources: evidence_a-d.jsonl (ids a01-d19), claims.jsonl (K01-K26), critique.md in this folder. Related subfields in the same run: Calibration and overconfidence, Premortem and prospective hindsight, Aggregation and extremizing, Debiasing and cognitive forcing, Planned versus emergent strategy, Search over thoughts. Sibling: 01_scenario_planning (the method itself).*

## 1. What it is

This subfield asks one question. Is there measured evidence that scenario planning works? "Works" can mean four things:

1. It changes how experts judge (mental models, confidence, option choice).
2. It reduces known biases (framing, overconfidence, anchoring).
3. It improves decisions or firm performance.
4. It improves implementation (the de Geus claim).

The short answer: the evidence is thin, and what exists is weak in design.

- The famous claims are anecdotal and come mostly from Shell. Shell credits scenarios for being ready for the 1970s oil shocks. No control group exists for this.
- The best adoption number (Diffenbach 1983: 68% of large US firms used scenarios, third most used long-range technique) is an adoption figure, not an effect. We know it only through Wikipedia (a11, b01). The original text was not obtained (d14).
- The de Geus audit (Shell, early 1980s) says weak strategic implementation came from decision processes after the scenarios, not from the scenarios. This is a case claim. No measured implementation rate with and without scenarios was found (d18).
- Controlled human tests are few. The best one read in full is Phadnis et al. 2015 (a01-a06): field experts, pre/post, no control group.
- Generic strategic planning has a meta-analysis (George, Walker, Monster 2019: r=.229). Scenario planning has none.
- For language models there is no controlled study of a Shell-style scenario step against a no-scenario arm at equal tokens (a24, b25, c26, K20). Neighbour work exists: one-prompt scenario steps in forecasting (null), wargame simulations, decision pipelines, forecasting systems.

Why it matters for our agent. The schema has operator O3 (decompose) and O8 (reframe the goal), and guardrail G7 (every element must pay for itself at equal tokens). This subfield's job is "caution on adoption". Scenario work is popular and plausible. Popularity is not evidence. We should not add a scenario operator on faith.

## 2. History and theories in depth

**Origins.** Kahn's stories at RAND (1950s-60s) came first. Wack built the Shell scenario system from 1971 (a14). He argued forecasts had started failing, sometimes by large margins, after the early 1970s. Shell's six-step recipe (per Wikipedia, b01): list drivers and assumptions, build a framework, write 7-9 mini-scenarios, cut to 2-3, draft them, identify issues. De Geus (1988, a13) framed planning as learning: the real product is a change in managers' mental models, not a forecast.

**Adoption surveys.** Diffenbach 1983 (Long Range Planning, June 1983) is reported as finding 68% of large organisations used scenarios (a11; d14 confirms the record, text not read). Klein and Linneman (1983, 1984) report about 150 of the Fortune 1000 industrials used multiple scenarios in formal planning, and that firms did not follow the rigorous procedure the literature recommends (d13, snippet). Both are use counts. Neither measures benefit or satisfaction.

**Theory of mechanism.** Schoemaker (1993, 1995; a09, a15) gave the behavioural case. Scenarios should counter three biases:
- anchoring on the status quo,
- availability (only the vivid futures come to mind),
- overconfidence from narrow ranges.

He cites Koriat, Lichtenstein, Fischhoff (1980): generating reasons against your answer can improve calibration. He also notes a risk: asking for reasons for extreme outcomes can shrink ranges through "incredulity" (the story seems too far fetched).

**Counter-theory: stories can inflate belief.** Four older results warn that vivid narratives push the wrong way:
- Conjunction fallacy (Tversky and Kahneman 1983; b11): adding detail makes a story seem more likely though logically less likely. Experts rated "Soviet invasion of Poland plus US break in relations" at about 4% against about 1% for the break alone. In the die problem 65% chose the longer sequence GRGRRR. In the Linda problem 57% still erred with clearer wording. A frequency format cut errors (Gigerenzer 1991).
- Imagination inflation (Garry et al. 1996; b15): imagining an event raised belief that it happened. Explaining it and adding sensory detail gave similar boosts. Pezdek and Eddy (2001) argued regression to the mean; Garry et al. (2001) rebutted.
- Planning fallacy (Buehler, Griffin, Ross 1994; b12): N=37 students. Standard estimate 33.9 days, best case 27.4, worst case 48.6, actual 55.5. About 30% finished on time. Writing best and worst case scenarios did not fix underestimates. Actual time exceeded even the worst-case average. Replication in interval form (b13): stated 99% dates were met 45% of the time (13% for 50% dates, 19% for 75%).
- Overconfidence (b14): 90% intervals hit about 50%; "100% certain" answers wrong about 20%.

**Evidence-quality critique.** Wulf, Meissner, Stubner (2010, d16): scenario processes vary widely, rely on unstructured workshops, are hard to replicate, and experts rarely disclose methods. Healey and Hodgkinson (2008, b09, not opened) and the Futures and Foresight Science 2022 paper (a19) argue for experiments and design science, and for telling conceptual from direct replication. Hodgkinson and Wright (2002, b08, recalled, not opened) is a failure case: a scenario intervention in one top team did not move strategy because of inertia and politics.

**Newer strand.** Since 2023, LLMs are used to draft scenarios (Jungwirth and Haluza 2023, a25; Spaniol and Rowland 2023, d10) and to forecast (Halawi 2024, Csaszar 2026). The question moved from "do scenarios help managers" to "does a scenario step help a model". That is the question our schema needs answered.

## 3. Core findings with exact numbers

Status: established = more than one source or a read meta-analysis; single-source = one opened study; contested = sources disagree; unverified = not opened or secondary only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| A one-shot scenario pass changes most expert judgments (field, no control) | Study I multi-scenario (Posttest B): 343 pairs, 189 changed (55.1%). Study I single-scenario (Posttest A): 419 pairs, 234 (55.8%). Study II multi: 285 pairs, 198 (69.5%). Study II single: 404 pairs, 288 (71.3%) | Phadnis et al. 2015 (a02-a05) | single-source (K01, K02) |
| Mean confidence does not change | Study I: chi2=5.65, df=3, p=0.13; highly certain 158 (46%) pre vs 157 (46%) post. Study II: 0.811 vs 0.814, p=0.979 | Phadnis 2015 (a02, a03) | single-source |
| Change follows the scenario's verdict | Useful: 39/62 (62.9%) more favourable vs 136/288 (47.2%) overall, p<0.001. Wasteful: 48/70 (68.6%) less favourable vs 152/288 (52.8%), p<0.001. Neutral: 75/156 (48.1%) more favourable | Phadnis 2015 (a04) | single-source |
| Highly confident experts change less | Study I: 70/193 (36.3%) vs about 70% at other levels, p<0.001. Study II: 19/52 (36.5%) | Phadnis 2015 (a05) | single-source (K03) |
| Multi-scenario exposure shifts to flexible options | Study III, 27 experts, 351 pairs: Option 1 229 (65.2%) to 176 (50.1%); Option 3 43 (12.3%) to 81 (23.1%), p<0.001; Option 4 26 (7.4%) to 40 (11.4%), p=0.056 | Phadnis 2015 (a06) | single-source (K04) |
| Confidence effects in older lab work disagree | Schoemaker 1993: MBA students widened ranges. Kuhn and Sniezek 1996: undergraduates more confident than controls. Numbers not read | via Phadnis (a07-a09) | contested (K05); unverified |
| Scenarios vs traditional tools, controlled | N=252 graduate students; framing bias reduced, decision quality higher. Cell sizes not read | Meissner and Wulf 2013 (d09) | single-source, abstract only (K23) |
| Pre/post mental-model change | 129 participants, 10 organisations, no control; moderate effects on several of 5 style factors | Glick et al. 2012 (a16) | single-source |
| Generic planning and performance | r=.229, 95% CI .186-.271; 87 correlations, 31 studies; I2=91.6%; r=.255 one effect per study; Egger flags publication bias, Begg does not | George, Walker, Monster 2019 (d01, d02) | established (K08) |
| Planning effect moderators | Meta-regression explains about 71% of variance; participatory planning weaker; multi-source data gives smaller effects; public/private and US/non-US no difference | George et al. 2019 (d02) | established (K24) |
| Foresight maturity and later profit | 83 firms (70 profit, 42 market cap). Vigilant firms 63% of outperformers vs 24% of underperformers. Profitability 16% vs 12% industry; market cap growth 75% vs 25%. No significance tests. 2008 cross-section sign reversed | Rohrbeck and Kum 2018 (d03, d04) | contested (K06) |
| Scenario use and firm performance | N=794 Italian SMEs, positive, stronger under high change; no coefficients seen. Phelps 2001: better finances, maybe worse customer service; sample unclear | Zanin and Corazza 2021 (b05); Phelps 2001 (b06, d15) | unverified |
| Systematic review | Mostly positive on thinking, decisions, learning, performance; some contradictory, adverse or null results. Study count not seen | Gokmen and McKiernan 2021 (b04) | contested |
| Adoption | 68% of large firms (Diffenbach 1983); about 150 of Fortune 1000 (Klein and Linneman) | a11, d13, d14 | unverified (secondary) |
| One-prompt scenario step in LLM forecasting: null | 100 questions, 4 models. Hypothetical Scenario Analysis -0.007 Brier, p=.411, adjusted .774. Premortem -0.008, adjusted .774. Compounds -0.001 to +0.004, adjusted p .79-.985 | Schoenegger et al. 2025 (d05, d06) | single-source (K22) |
| Frontier LLMs vs managers, prospective ranking | 30 projects, 870 comparisons. Gemini 2.5 Pro rho=.74; GPT-5 family .67-.71; best expert .45; worst .04; Prolific crowd .19 (346 managers). Gap to best expert p=.063. Value capture: 12 LLM/crowd evaluators above 83% of oracle; random 18.9%; Prolific 85% | Csaszar et al. 2026 (a21-a23) | single-source (K09, K10) |
| LLM forecasting vs crowd | Brier: random .250, crowd .149, best plain model .208, retrieval system .179. Accuracy 71.5% vs 77.0% | Halawi et al. 2024 (c08) | single-source |
| Combining LLM and human forecasts | Gains 17-28% with the human median | Schoenegger et al. 2024 (b17) | established (K12) |
| Reflection prompts cut LLM wargame escalation | Planning prompt -28%; de-escalation reflection -57%; temperature 0.5 -38%; 0.01 -48%; 10 runs per cell; Mistral-7B | Elbaum and Panter 2025 (c05) | single-source (K13) |
| LLM wargames vs experts | 214 experts, 48 teams; of 21 actions GPT-3.5 matched human frequency on 16, GPT-4 on 10, GPT-4o on 9 | Lamparth et al. 2024 (c02) | established with Rivera (K14) |
| Actor-name bias | Less escalation advised for China and Russia than US/UK; 7 models, 400 scenarios | Jensen et al. 2025 (c06) | single-source (K15) |
| LLMs rarely name the business problem type unprompted | 223 tasks, 16 models; best passes gate 27.9%; top two overlap 31.7%; routing over top 8 reaches 50.7% | KWBench 2026 (c16) | single-source (K17) |
| LLM business simulation | Net worth 9.0x spread ($20,856 to $188,488); 51% of runs lose money; best expert strategy $436,195 (2.3x best mean) | Business Arena 2026 (c14) | single-source (K18) |
| Decision scaffolds with enumerated states | DeLLMa up to +40% accuracy; PlanRAG +15.8% and +7.4%; K-Level win rate .65 in one game, K=3 hurt in another | c09, c11, c13 | contested (K16) |
| LLM breadth aids widen but do not improve accuracy | N=348; LLM use raised breadth, lowered depth and consensus, left accuracy unchanged (abstract only; startup evaluation, not scenarios) | Kanis et al. 2026 (d08) | single-source (K25) |
| Diversity of generation | Stratification: recall +0.05 over GPT-4o, KL -0.36 vs Llama 3; criteria prompting 37.5% recall on one set | c17, c18 | established that single prompts are low-diversity (K19) |

## 4. Mechanisms and models

Five mechanisms, each with an implementation note.

**M1. Direction-of-evidence shift (Phadnis).** The scenario acts as a piece of evidence. The expert re-judges each option given that world. Judgments move toward the scenario's verdict for that option (62.9% and 68.6% moved the expected way vs about 47-53% base). Implementation: for each candidate option, ask "in this world, better or worse" and record a sign per world. Code tallies signs across worlds. This is a robustness table, not a forecast.

**M2. Flexibility shift under several worlds.** After several worlds, experts moved away from the most committed option toward flexible ones (Option 3 from 12.3% to 23.1%). Implementation: tag each option with a commitment level and count in how many worlds each option holds. When worlds disagree, prefer options that survive in more worlds. This is a robust-option rule, close to minimax regret.

**M3. Confidence does not move on average, but high confidence resists change.** Aggregate confidence stayed flat (0.811 vs 0.814). Highly certain people changed only about 36% of the time vs about 70%. So scenario exposure does not repair overconfidence in experts. Consequence: do not rely on a scenario step for calibration. Calibration needs a separate, code-based check (see sibling subfield Calibration and overconfidence).

**M4. Narrative inflation.** Rich scenarios raise perceived probability through detail (conjunction fallacy, imagination inflation). Implementation: keep scenarios short, list them as exclusive branches, set probabilities by code that normalises to 1 (G5), and not by the vividness of the story. Use a frequency format ("out of 100 worlds").

**M5. Diverge then converge.** Breadth aids widen representations but do not by themselves raise accuracy, and they lower consensus (Kanis 2026, Schoenegger 2025). A convergence step must follow. Implementation: S3 generates K scenarios in fresh contexts. G4 says samples from one model are not independent, so seed with distinct strata as SimpleStrat does: the model lists axes of variation, code picks one cell per sample. S7 selects by a code check, not by a model judge.

**Working scaffold patterns from decision papers.**
- DeLLMa (c09) is scenario analysis written as code: (1) enumerate unknown states, (2) forecast their probabilities, (3) elicit utility, (4) take expected utility in code. Up to +40% decision accuracy vs plain and chain-of-thought, larger gains with more actions.
- PlanRAG (c13): plan, retrieve, re-plan on failure. Removing re-planning cost 10.8 points in one scenario and 0.9 in another.
- K-Level reasoning (c11): model the other side's likely move recursively. Helps in some games; K=3 hurt in one.
These are the closest working analogues of a scenario operator for LLMs.

**Why Shell might work (hypothesis only).** Shell uses scenarios repeatedly, with managers inside the loop. Phadnis used one-time sessions and says so (a01, a10). Transfer to an agent is unclear. An agent has no organisational follow-through, so the de Geus point has no counterpart in a single-answer task.

## 5. What holds up

**Held up.**
- Scenario exposure changes judgments in a predictable direction (one source, three field studies, no control).
- Planning in general has a small to moderate positive link with performance (r about .23, 31 studies), with high heterogeneity and a publication-bias signal. It is the only meta-analytic number in the area.
- Common-source bias inflates self-reported benefits (George et al. 2019; the sign flip in Rohrbeck and Kum 2018).
- Plain-prompt LLM outputs have low diversity; stratified generation improves coverage.
- LLM wargame behaviour differs from experts and is unstable (more than 50% score swings in one turn in some runs).

**Failed or null.**
- Schoenegger 2025: scenario analysis and premortem prompts did not improve LLM forecasts (-0.007 and -0.008 Brier, adjusted p=.774). Base-rate prompts helped; Bayesian-reasoning prompts hurt. A secondary summary (d07, not opened) says no complex strategy beat the basic prompt.
- Phadnis: no confidence change overall.
- Kanis 2026: LLM use did not change foresight accuracy.
- Planning fallacy: best and worst case scenarios did not fix underestimates (b12).
- Hodgkinson and Wright 2002: one intervention failed on inertia and politics (recalled only).

**Contradictions.**
- Confidence: Schoemaker (wider), Kuhn and Sniezek (more confident), Phadnis (no change). Only Phadnis was read.
- Number of scenarios: about 3 per the Wikipedia rule, 2-3 per Shell, 8 vs 4 in a secondary summary of the Strategy Science paper. No experiment varied the number (d19).
- More samples help in DeLLMa but K=3 hurt in K-Level reasoning.
- Csaszar: crowd rank correlation .19 (near random) yet value capture 85%. Correlation and value capture can diverge.

**Moderators.**
- Prior confidence (high confidence resists change).
- Scenario verdict (useful or wasteful vs neutral).
- Single-source vs multi-source performance data (smaller effects with several sources).
- Environmental change (Zanin: stronger under high change; not verified).
- Participatory vs other planning (weaker).
- Time lag (Rohrbeck and Kum: sign reversal in the cross-section).

**Interventions that worked.** Short de-escalation reflection prompt in LLM wargames (-57%); low temperature (-48%); base-rate prompting in LLM forecasting; retrieval plus ensembling (Brier .208 to .179); averaging LLM and human medians (17-28% accuracy gain); enumerate-states-then-expected-utility scaffold.

**Interventions that did not work.** Scenario and premortem prompts for forecast calibration; best/worst-case narratives for planning time; extra instructions in wargame briefings (model-specific and inconsistent; GPT-3.5 became more likely to fire after the priorities were added).

**Not read, so not counted.** Meissner and Wulf cell values, Schoemaker 1993, Kuhn and Sniezek, Phelps 2001, Chermack studies (about 90 managers, snippet), Kozachek 2026, Time Machine (6 trials, 222 participants, snippet).

## 6. Language models

**No direct test.** No study compares a Shell-style scenario operator with a no-scenario arm at equal tokens on a measured outcome (a24, b25, c26, K20). An arXiv search on scenario planning and language models gave 9 hits, none testing a scenario step (b25).

**The one near-direct test is null.** Schoenegger et al. 2025 (d05, d06): 100 binary ForecastBench questions, 4 models, control Brier .208 to .227. Hypothetical Scenario Analysis -0.007 (p=.411, adjusted .774). Premortem -0.008. Combined with step-back -0.001; with premortem +0.004. Base-rate prompts improved accuracy. A superforecaster-written odds-ratio prompt moved results, and made them worse. Limits: one prompt per idea, single call, not a multi-step operator; only 100 questions; Brier effects are tiny and intervals were not extracted.

**Forecasting level.** Plain models are weak: best plain Brier .208 vs crowd .149 (Halawi). Retrieval plus ensembling reaches .179. On a prospective ranking task, frontier LLMs beat managers (rho .74 vs best expert .45; gap p=.063, not clearly significant). ForecastBench found expert forecasters beat the best LLM (p<0.001, b18). So the level depends on task and date. A structured belief-state agent (Murphy 2026, d17) topped compared agents on ForecastBench; its text never mentions scenarios.

**Scenario generation.** Jungwirth and Haluza 2023 (a25, a26): GPT-3 gave four Ukraine scenarios with stated probabilities (40%, 20%, 10%, first unclear) without being told about the war. It also scored its own consistency (100% for two scenarios, 66.67% for one) and confirmed co-authorship. Not a valid test: the model generated and graded its own output (a G8 violation). McIntosh 2026 (c23, snippet): ChatGPT 4o scored a 1976 report; the second-most-pessimistic scenario fitted best (88%), the most optimistic worst (40%). Spaniol and Rowland 2023 is opinion (d10). Kozachek 2026 compares human and GPT scenarios; no numbers (d11).

**Decision scaffolds.** DeLLMa: up to +40% accuracy; human agreement with its state forecasts about 65-70%; agriculture 73.3%, stock 64.2%; smaller gains on stocks; a 64-sample DeLLMa can beat zero-shot o1-preview per the text (c10). PlanRAG +15.8% and +7.4%. K-Level mixed. DeFine (c12) uses factor profiles and retrieved past cases for buy/sell calls.

**Wargames.** All five models in Rivera et al. escalated, with sudden jumps (10 runs per condition; some more than 50% in one turn). Lamparth et al.: LLMs agree with experts at a high level, differ in specifics, are more aggressive and more sensitive to scenario changes, and ignore player traits. More simulated dialogue raised aggressiveness toward human level for GPT-3.5 and GPT-4 but inflated action counts. Elbaum and Panter: a cheap prompt cut escalation 28-57% (Mistral-7B only, 10 runs per cell). Jensen et al.: country bias. These show LLM scenario answers can be unstable and actor-dependent. They do not show scenarios improve accuracy.

**Problem recognition and operating quality.** KWBench: best model passes the problem-type gate on 27.9% of 223 tasks; top two overlap 31.7%. Business Arena: 9x spread, 51% of runs lose money, a human strategy beats every model by more than 2x. Models show stable operating styles (under-investing, margin-focused, volume, stranded). Implication: scenarios run on a wrongly framed problem are polished work on the wrong problem.

**Breadth and consensus.** Kanis 2026: LLM aid widened breadth, cut depth and consensus, accuracy unchanged (abstract only). Together with Schoenegger this points to a convergence step.

**Diversity.** Single prompts give low diversity (Chen 2024: criteria prompting raised coverage, still below human). Surface metrics measure wording, not approach (c19). Temperature raises noise, not coverage (c18).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Never adopt a thinking step because it is widely used. A scenario operator must beat a no-scenario arm at equal tokens on held-out items before it ships. | G7 (already stated; this is the case for it) | [E] | d01, d02, d04, K06, K24 |
| Grade any scenario benefit with resolved outcomes or an outside grader, never the agent's own rating. | G2, G8 | [E] | d02, d04, a26, K24 |
| Probabilities over exclusive branches are set and normalised by code, not by story detail. | G5 | [E] | b11, b15 |
| Do not count on a scenario or premortem prompt to fix calibration. Use a separate code-checked calibration step. | G, S4 | [E] direction (Phadnis plus null); strength [S] | d05, d06, a02, a03 |
| Generate several futures only from stratified seeds (axes listed first, one cell per sample, fresh context each). | S3 (G4) | [E] | c17, c18, K19 |
| Report variance across seeds when testing any scenario step. | G7 | [E] | c01, c02, K14 |
| Combine model output with a simple human or prior baseline where one exists. | O7 aggregation | [E] | b17, c08, K12 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Scenario operator (3 worlds, option sign per world, robust option by code) vs no-scenario arm | O3 / S3-S4 | [S] | a04, a06, d05, K01, K04, K22 |
| Base rate first, then scenario | O3 | [S] | d05, K22 |
| Flexible-option preference when worlds disagree | O3 | [S] | a06, K04 |
| Number of scenarios 1 vs 2-3 vs 5 | O3 | [C] | c09, c11, K16, K26 |
| Problem-recognition step before any scenario work | S0 / O1 | [S] | c16, K17 |
| Diverge then converge with code selector | S3-S7 | [S] | d08, d05, K25 |
| Framing-invariance check (gain vs loss frame must agree) | G / O8 | [S] | d09, K23 |
| Neutral vs named actors | G (bias) | [S] | c06, K15 |
| Short de-escalation or reflection line on high-stakes choices | G | [S] | c05, K13 |
| Revision of high-confidence answers after scenario prompts | G1 | [S] | a05, K03 |

## 8. Concrete tests on our bench

All arms get the same token budget. Where an arm uses scenarios, the plain arm gets the same tokens as extra independent samples (G7).

1. **Scenario operator vs plain, forecasting.** Items: 100+ resolved binary questions after the model cutoff (ForecastBench style). Arms: (a) plain, (b) base rate first, (c) base rate then 3 stratified scenarios with code-normalised branch probabilities, (d) plain with extra samples averaged. Metric: Brier and 80% interval hit rate, with 95% bootstrap intervals. Expected: (b) beats (a); (c) vs (b) near zero (0.00 to -0.01 Brier) per Schoenegger.
2. **Option robustness.** Items: 40 decisions with 4 options (2 committed, 2 flexible) and a known payoff table across 3 worlds. Arms: scenario-sign table with robust choice vs plain. Metric: expected regret against the true world draw. Expected: gain only where worlds disagree; none where one option dominates.
3. **Number of scenarios.** Same items, 1, 2, 3, 5 worlds at equal tokens. Metric: accuracy against tokens. Expected: flat or inverted U, peak at 2-3 if the Shell rule holds.
4. **Framing invariance.** 60 paired gain and loss frames of one decision. Arms: plain vs scenario pass. Metric: rate of answer disagreement between frames. Expected: scenario arm lowers disagreement (Meissner and Wulf direction).
5. **Problem recognition gate.** Items: KWBench-style tasks. Arms: plain vs a first step that names the strategic structure before scenarios. Metric: gate pass rate and final rubric score. Expected: pass rate rises from about 28%; final score rises only if recognition is correct.
6. **Confidence resistance.** Items: 100 questions with answer plus confidence. Arms: plain vs scenario pass. Metric: change rate among answers above 0.9 confidence vs below, and Brier. Expected: high-confidence answers change less (as a05); Brier flat (as a02, a03).
7. **Actor-name bias.** 100 scenarios with actors swapped. Arms: named, neutral labels, neutral plus a swap-and-compare check in code. Metric: advice disagreement under swap. Expected: the check lowers disagreement.
8. **Diverge then converge.** Metrics: scenario diversity (embedding distance plus approach-level judge) and final accuracy. Expected: breadth up; accuracy up only with a code selector.

## 9. What does not transfer, and why

- **Shell-style continual practice.** Shell runs scenarios repeatedly with managers acting on them. Our agent answers single items. The implementation gap (de Geus) has no counterpart.
- **Firm performance results.** Planning and foresight studies measure firms over years, use self-report, carry confounds, and mix scenarios with all planning. They cannot become an agent test.
- **Adoption figures.** 68% of firms using a method says nothing about benefit, and our source is secondary.
- **Group effects.** Workshop discussion, voting and vetoes (Phadnis) are social. Our agent is one model. G9 rejects debate and G4 says samples are not independent.
- **Wargame escalation studies.** They concern escalation, not scenario quality. Useful for stability and bias, not accuracy.
- **Csaszar and Kanis.** They test judgment and breadth, not a scenario step.
- **Human mental-model change.** For a prompt-driven model there is no persistent mental model to change, unless memory stores it.
- **Narrative persuasion.** The human risk (vivid story, inflated belief) is an untested analogue for LLMs. Do not assume its size.

## 10. Open questions

1. Does a multi-step scenario operator beat no-scenario at equal tokens on calibration? No study exists (only the one-prompt null).
2. What do Meissner and Wulf 2013 and Schoemaker 1993 report (cell values, interval widths)?
3. What exactly does Kanis 2026 find, with effect sizes?
4. Causal performance effects of scenario use (Phelps 2001, Zanin 2021), with effect sizes.
5. Original Diffenbach 1983 numbers and later adoption and satisfaction surveys.
6. Best number of scenarios, in humans and in LLM sampling.
7. Any measured implementation-rate effect (de Geus follow-through).
8. How diverse and plausible are LLM scenarios vs human ones (Kozachek 2026; Time Machine, 222 participants)?
9. Can a scaffold remove actor-name bias?
10. Do Phadnis's direction-of-evidence and flexibility shifts appear in LLMs?
11. Does base rate then scenario beat base rate alone (K22)?

## 11. Sources

[V] opened this session (full or partial text). [M] snippet or metadata only.

- [V] Phadnis, Caplice, Sheffi, Singh 2015, SMJ 36(9). https://sheffi.mit.edu/sites/sheffi.mit.edu/files/2017-06/Phadnis-etal_Scenario-effects_SMJ.pdf
- [V] Sheffi, Phadnis, Caplice 2016, MIT practitioner summary. https://sheffi.mit.edu/sites/sheffi.mit.edu/files/2017-05/How%20Scenario%20Planning%20Influences%20Strategic%20Decisions%20%281%29_1.pdf
- [M] Kuhn and Sniezek 1996. https://doi.org/10.1002/(sici)1099-0771(199612)9:4<231::aid-bdm240>3.0.co;2-l
- [M] Schoemaker 1993. https://doi.org/10.1002/smj.4250140304
- [V] Schoemaker 1995, MIT Sloan Management Review. https://sloanreview.mit.edu/article/scenario-planning-a-tool-for-strategic-thinking/
- [V] Wikipedia, Scenario planning. https://en.wikipedia.org/wiki/Scenario_planning
- [V] de Geus 1988 (opening only). https://hbr.org/1988/03/planning-as-learning
- [V] Wack 1985 (opening only). https://hbr.org/1985/09/scenarios-uncharted-waters-ahead
- [V] Glick et al. 2012 (abstract level). http://www.emerald.com/ejtd/article/36/5/488-507/25288
- [M] Meissner and Wulf 2013 full text https://doi.org/10.1016/j.techfore.2012.09.011 ; [V] abstract page https://ideas.repec.org/a/eee/tefoso/v80y2013i4p801-814.html
- [M] Phelps, Chan, Kapsalis 2001. https://doi.org/10.1016/s0148-2963(99)00048-x
- [M] Futures and Foresight Science 2022. https://doi.org/10.1002/ffo2.146
- [V] Rohrbeck and Kum 2018. https://www.epicpeople.org/wp-content/uploads/2024/01/Article-Corporate-foresight-and-its-impact-on-firm-performance-A-longitudinal-analysis.pdf
- [V] George, Walker, Monster 2019. https://repub.eur.nl/pub/120708
- [V] Gokmen and McKiernan 2021. https://strathprints.strath.ac.uk/id/eprint/76934
- [V] Zanin and Corazza 2021 (abstract page). https://ideas.repec.org/a/fan/macoma/vhtml10.3280-maco2021-002008.html
- [M] Hodgkinson and Wright 2002. https://doi.org/10.1177/0170840602236014
- [M] Healey and Hodgkinson 2008. https://doi.org/10.1177/0170840607088022
- [V] Wulf, Meissner, Stubner 2010. https://www.uni-marburg.de/de/fb02/professuren/bwl/strategy/forschung/publikationen-1/ap-no-6-scenario-based-approach-to-strategic-planning.pdf
- [M] Klein and Linneman. https://emeraldinsight.com/insight/content/doi/10.1108/eb045683/full/html
- [M] Diffenbach 1983 catalogue record. https://searchworks.jioinstitute.edu.in/articles/edsggo__edsgcl.2788283
- [V] Wikipedia summaries: https://en.wikipedia.org/wiki/Conjunction_fallacy ; https://en.wikipedia.org/wiki/Planning_fallacy ; https://en.wikipedia.org/wiki/Overconfidence_effect ; https://en.wikipedia.org/wiki/Imagination_inflation
- [M] Chermack and Nimon 2008 via WEF. https://www.weforum.org/stories/2023/09/strategic-foresight-research-insights/
- [V] Csaszar, Peterson, Wilde 2026. https://arxiv.org/pdf/2602.01684
- [V] Jungwirth and Haluza 2023. https://www.opastpublishers.com/open-access-articles/aibased-scenario-generation-for-future-planningan-exploratory-study-using-gpt3.pdf
- [M] XFinBench (Zhang, Cao, Liao 2025). https://arxiv.org/abs/2508.15861
- [M] Kanis, Mann, Stumpf-Wollersheim 2026, Strategy Science. https://pubsonline.informs.org/doi/full/10.1287/stsc.2025.0442
- [V] Halawi et al. 2024. https://arxiv.org/abs/2402.18563
- [V] Schoenegger et al. 2024 (silicon crowd). https://arxiv.org/abs/2402.19379
- [V] Karger et al. ForecastBench. https://arxiv.org/abs/2409.19839
- [V] Schoenegger, Jones, Tetlock, Mellers 2025. https://arxiv.org/abs/2506.01578
- [M] Secondary summary of forecasting strategies. https://www.themoonlight.io/review/can-language-models-use-forecasting-strategies
- [V] Murphy 2026 (BLF). https://arxiv.org/abs/2604.18576
- [V] Rivera et al. 2024. https://arxiv.org/abs/2401.03408
- [V] Lamparth et al. 2024. https://arxiv.org/abs/2403.03407
- [V] Elbaum and Panter 2025. https://arxiv.org/abs/2508.01056
- [V] Jensen et al. 2025 (CFPD). https://arxiv.org/abs/2503.06263
- [V] Li, Li, Zhou 2026. https://arxiv.org/abs/2603.16642
- [V] Liu et al. 2024 (DeLLMa). https://arxiv.org/abs/2402.02392
- [V] Wang et al. 2024 (K-Level). https://arxiv.org/abs/2402.01521
- [V] Fu et al. 2024 (DeFine). https://arxiv.org/abs/2410.01772
- [V] Lee et al. 2024 (PlanRAG). https://arxiv.org/abs/2406.12430
- [V] Business Arena 2026. https://arxiv.org/abs/2608.08621
- [V] KWBench 2026. https://arxiv.org/abs/2604.15760
- [V] Chen et al. 2024. https://arxiv.org/abs/2311.09799
- [V] Wong et al. 2024 (SimpleStrat). https://arxiv.org/abs/2410.09038
- [V] Anonymous 2026 (surface vs approach diversity). https://arxiv.org/abs/2606.29985
- [V] WiA-LLM 2025. https://arxiv.org/abs/2509.04791
- [V] Spaniol and Rowland 2023 (opinion piece; judged as such in d10). https://doi.org/10.1002/ffo2.148
- [M] Kozachek 2026. https://doi.org/10.1016/j.futures.2025.103705
- [M] Wong 2025 education scenarios. https://doi.org/10.1007/s44217-025-00692-3
- [M] McIntosh 2026. https://doi.org/10.1108/fs-02-2025-0027
- [M] Morozumi and Hayashi 2026. https://doi.org/10.5220/0014452200004052
- [M] Rosen 2025. https://doi.org/10.1016/j.futures.2025.103566
- [M] The Time Machine, Future Internet 2025. https://doi.org/10.3390/fi17010048
