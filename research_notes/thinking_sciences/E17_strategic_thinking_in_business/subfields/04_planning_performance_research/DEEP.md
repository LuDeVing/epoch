# Planning-performance research: deep document

*Subfield E17.04. Built from evidence_a-d.jsonl (ids a01-a22, b01-b37, c01-c27, d01-d21), claims.jsonl (K01-K23) and critique.md in this folder. Warning: no pooled effect size from any business meta-analysis was read (publishers blocked full text), and the founding comprehensiveness studies were never opened. Numbers are exact only where the evidence file records them from full text.*

## 1. What it is

Planning-performance research asks one question: do firms that plan formally do better than firms that do not? It started with Ansoff in the 1960s and grew into a large empirical literature from the 1970s to the 1990s. Since 1982 there have been at least six reviews or meta-analyses. The answer is "yes, a little, with conditions".

The subfield focus line says three things.
- The effect is positive in meta-analyses.
- It depends on formal analysis, option generation (comprehensiveness) and stakeholder management.
- Many firms did not use plans for key decisions (McKinsey 2006).

Comprehensiveness means producing many strategic options before selecting the course to follow (a01, c01). That maps to our agent: S3 Generate many, then S7 Select.

Three layers of evidence exist.
1. Firm-level field studies and meta-analyses (Armstrong 1982, Boyd 1991, Miller and Cardinal 1994, Shea-Van Fossen 2006, George 2019, Hamann 2022). Correlational. Mostly read at abstract level.
2. Field experiments on new ventures (Camuffo 2020, 2024). They randomise training in hypothesis testing, not planning as such.
3. LLM studies on planning and option generation (PlanBench, Tree of Thoughts, PlanSearch, Girotra, Vending-Bench). Proxy tasks. None measures firm performance.

Why it matters: it is the largest human literature on whether "plan first, many options, then choose" pays, and when it does not.

## 2. History and theories in depth

**Prescriptive era.** Ansoff (1965) *Corporate Strategy* set out planning as a formal analytic process (a20, snippet only). By 1979 an estimated 45% of Fortune 500 firms used some form of growth-share matrix (a05, Wikipedia).

**Early reviews.** Armstrong (1982) reviewed 15 comparisons: formal planning better in 10, informal better in 2 (b05, abstract; the abstract also says 12 studies). Pearce, Freeman and Robinson (1987) titled their review "the tenuous link" (a19, title only). Rhyne 1986, Bracker and Pearson 1986 and Bracker and Keats 1988 studied small firms (b06-b08, abstracts, no figures).

**Meta-analyses.**
- Boyd (1991): 29 samples, 2,496 organisations, nine performance measures. "Modest" (a07, c04, d02).
- Miller and Cardinal (1994): synthesis of more than 30 years, 26 studies (a09, b04). Exact r not read.
- Capon, Farley and Hulbert (1994): small positive relation that persists over a longer period (b03, abstract).
- Shea-Van Fossen, Rothstein and Korn (2006): 39 studies, 74 effect sizes, 5,223 firms. Standardised mean difference 0.257 (p<.001). After trim and fill: 0.109, CI -0.235 to 0.242, which includes zero (a03, c03).
- George, Walker and Monster (2019, *Public Administration Review*): 87 correlations from 31 studies. "Positive, moderate, and significant". Strongest for effectiveness and for formal planning. Holds in public and private sectors. Wikipedia says "almost 9,000" organisations (a10, b11, d03, a01).
- Hamann, Halw and Guenther (2022, *SMJ*): 183 independent samples, 84 new. Corrects for measurement error and dichotomisation. Effects stable over time and planning types. Larger for manufacturing, larger firms, high uncertainty-avoidance countries and high environmental uncertainty (b10, d04; abstract via Crossref).

**New ventures.** Delmar and Shane (2003): 223 Swedish ventures begun in the first 9 months of 1998; planning lowered disbanding (a12, b09, d05; abstract). Brinckmann, Grichnik and Kapsa (2010) meta-analysed planning in small firms (a11, b15, d06; no text). A Colombian study of 730 ventures (1997-2001) looked at planning under violence (b18, abstract).

**Decision-process school.** Fredrickson and Mitchell (1984) and Dean and Sharfman (1996) tested comprehensiveness against performance. Fredrickson (1984) extended it. Nutt (1993) coded 163 decisions for process and tactic (b16). None was readable; we know them by title and citation counts (a15-a17, b13, b14, b16, d07). The usual story is that comprehensiveness pays in stable settings and may hurt in unstable ones. Unverified here (K17).

**Critics.** Mintzberg (1994) *The Rise and Fall of Strategic Planning* argued planning is not strategy formation (a04, a20; Wikipedia only). Kahneman and Lovallo (1993) argued for the outside view because planners make bold forecasts (b19, abstract). Planning fallacy: 37 students predicted 33.9 days and took 55.5; about 30% finished within prediction (b20, Wikipedia). In a 1995 study 13% finished by their 50% date, 19% by their 75% date, 45% by their 99% date.

**Practice gap.** McKinsey Quarterly 2006, read in full (d01): N=796 executives, July to August 2006, firms with at least $500M revenue, weighted by GDP. Over 75% have a formal process. Fewer than 25% say it is key to their most important decisions. 52% say a small senior group including the CEO decides; 23% say they decide using the formal process. Fewer than half are satisfied with their approach to strategy.

**Experimental turn.** Camuffo, Cordova, Gambardella and Spina (2020, *Management Science*): 116 Italian startups, 59 treated and 57 control, 10 sessions, about one year, 16 data points (b17, d18). Treated firms learned to state hypotheses and test them. They did better and pivoted more than an intuition control. Same-group replication (2024, *SMJ*): four RCTs, 759 firms; more idea termination, non-linear pivot effect (d20). Independent Uruguay replication registered: two experiments of at least 116 each, running to Sept 2026 (d21).

**Theory.** No formal model of why planning helps was found (a22, inference). The stated mechanisms are verbal: analysis improves information; options widen the search; stakeholder management secures commitment. Our agent can use the first two.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Planning has a positive, moderate link with performance | George 87 correlations / 31 studies; Boyd 29 samples / 2,496 firms "modest"; Hamann k=183. No pooled r read | a07, a10, b10, d02-d04 (K01) | Established in direction; size unknown |
| Effect shrinks after publication-bias correction | d=0.257 to 0.109, CI -0.235 to 0.242; 39 studies, 5,223 firms | a03, c03 (K02) | Single-source |
| Effect larger under high environmental uncertainty, in manufacturing, in larger firms | Hamann k=183; George: strongest for effectiveness and formal planning | b10, b11, d04 (K03) | Established (abstract level) |
| Formal planning better in most early comparisons | 10 of 15 formal better, 2 of 15 informal better | b05 | Old; abstract |
| Large firms bypass the plan for key decisions | N=796; >75% have a process; <25% key; 52% small group decides; 23% formal process | d01 (K19) | Established |
| Planning fallacy | 37 students: 33.9 days predicted vs 55.5 actual; ~30% on time | b20 (K06) | Single-source (Wikipedia) |
| Teaching hypothesis testing helps startups | 116 startups, 59/57; replication 759 firms in 4 RCTs | b17, d18-d21 (K05) | Single-source (one group) |
| Sample many, select with a checker | ToT Game of 24 (%): IO 7.3, CoT 4.0, CoT-SC(100) 9.0, ToT b=1 45, b=5 74; best of 100 CoT 49 | b28, c07, c08 (K07) | Established |
| Repeated sampling scales with a checker | SWE-bench Lite 15.9% to 56% at 250 samples; prior SOTA 43% | c10 (K07) | Established |
| Distinct plans lift best-of-k | LiveCodeBench pass@200 Claude 3.5 Sonnet 55.6 to 77.0; GPT-4o 60.6 to 73.0; Sonnet pass@1 40.3 | d10 (K20) | Established (needs a checker) |
| Plan step gives small gains on math | CoT 70.4, PS 72.9, PS+ 76.7 (PoT 73.5); StrategyQA 63.8 to 65.4; CSQA 65.2 to 71.9 | c05 (K09) | Single-source; old model |
| Self-planning helps code | HumanEval Pass@1 60.3 vs CoT 53.9; ground-truth plan 74.4 | c12 (K12) | Single-source |
| LLMs plan poorly alone | PlanBench GPT-4 206/600 (34.3%), Instruct-GPT3 41/600; verification 191/600 and 4/600; o1-preview Mystery 317/600 (52.8%), randomised 37.3%; Fast Downward 100% in 0.265 s | b30, b31 (K10) | Established |
| Verifier loop lifts planning | LLM-Modulo Blocks World 82% in 15 rounds, Logistics 70%, Mystery ~10% | c16 (K11) | Single-source |
| Self-consistency can hurt planning prompts | Blocksworld GPT-4 zero-shot 3.83; stacking prompt 59.3; self-consistency lowered scores | c17, c18 | Established |
| LLMs do not self-correct intrinsically | GPT-3.5 keeps answer 74.7%; more correct-to-wrong than wrong-to-correct | b33 (K08) | Established |
| LLM ideas rated higher | Purchase intent 40.4% students, 46.8% GPT-4, 49.3% GPT-4 with examples; 35 of top 40 from GPT-4; ~$0.63 per idea vs ~$25 | d08 (K16) | Established |
| LLM idea pools less diverse | Cosine similarity 0.255-0.432 (GPT-4 prompts) vs 0.243 human pool; baseline 0.377 | d09 (K16) | Established |
| LLM crowd matches human crowd | Brier 0.20 vs 0.19; 12 LLMs vs 925 people; 31 questions | d16 (K23) | Established |
| LLM judge agreement and bias | >80% agreement with humans; first-position bias | d15 (K23) | Established |
| Single-LLM strategic evaluation inconsistent | 60 business models, two studies; aggregates resemble experts. Correlations not read | b23, d17 | Abstract only |
| Extra reasoning can hurt | o1-preview 57.7% vs GPT-4o 94.0% (-36.3) on a 440-problem subset; GPT-4o with CoT -23.1 (p<.0001) | d12 (K21) | Established |
| Difficulty-scaled compute | ~4x less compute than best-of-N on MATH, PaLM 2-S* | d11 (K22) | Established (math) |
| Long-horizon business sims are high variance | Vending-Bench, 5 runs: Sonnet $2,217.93 (min $476), o3-mini $906.86, human $844.05 (one 5-hour run), Gemini 1.5 Pro $594.02, GPT-4o mini $582.33, GPT-4o $335.46 | b26, c23 (K14) | Established |
| Planner plus replanning raises web agent success | WebArena-Lite 9.85 to 29.63 to 57.58%; TheAgentCompany best 30.3% | b34, b35 (K13) | Contested |
| Complexity regimes | Plain wins low, reasoning wins medium, both ~0 at high | b36, c26 (K15) | Contested |

## 4. Mechanisms and models

No formal model of the planning-performance link exists in this literature (a22). The mechanisms below are implementable ones taken from the LLM evidence.

**4.1 Generate-then-select pipeline.** The field's "comprehensiveness" becomes: produce N options (S3), screen them against the same criteria (S4), choose in code or with an external check (S7), and record why (K19).
1. Draft M candidate options in separate calls, not one list, to avoid the similarity collapse (cosine 0.255-0.432 vs 0.243 human).
2. Deduplicate by an LLM similarity call plus a threshold; keep at least k distinct families.
3. Score each option against fixed criteria in several calls with varied order; take the mean in code (K23).
4. Where a checker exists (tests, simulator, solver), run it. Where none exists, aggregation is a weaker substitute.
5. The final answer must name the options compared. This closes the McKinsey gap where the plan exists but does not bind the decision.

**4.2 Plan before acting.** PlanSearch (d10) writes observations, then diverse plans in natural language, then code. Best-of-k success rises because plans differ; idea diversity predicts the gain. Ground-truth plans lift HumanEval to 74.4 (c12), so plan quality is the bottleneck. Implication: score plans on their own, before execution.

**4.3 Search with evaluation.** Tree of Thoughts keeps b candidate thoughts per step and prunes them by the model's own evaluation. Breadth 5 beat breadth 1 (74% vs 45%) and best-of-100 CoT (49%). The task has a crisp success test, which is why model-based pruning worked.

**4.4 External verifier loop (LLM-Modulo).** The LLM proposes, a sound verifier critiques, the critique goes back as a prompt. 82% on Blocks World in 15 rounds, but about 10% on obfuscated Mystery, where proposals are not plausible enough. A verifier cannot rescue a proposer with no foothold (K11, matches G12).

**4.5 Difficulty-scaled budget.** Snell et al. bin problems by the model's own pass rate (five bins, 2048 samples per problem) and choose a method per bin: about 4x less compute than best-of-N. Search hurts on easy items. Hamann 2022 says the same for firms: planning pays more at high uncertainty. Implementation: a cheap difficulty probe (S0), then budget tiers.

**4.6 Replan on failure.** Plan-and-Act adds a planner then dynamic replanning: 9.85, 29.63, 57.58% (trained planner, so not a pure prompting result).

**4.7 Hypothesis-and-test loop.** Camuffo's treated startups state a hypothesis, define a falsifying test, run it, then persevere, pivot or terminate. Engineer form: before committing, list the claim the plan rests on, a cheap test, and a rule for which result flips the plan (G2, G3).

**4.8 Outside view.** Reference-class forecasting (Kahneman and Lovallo) corrects the planning fallacy. Engineer form: get base rates from similar cases before an inside-view estimate.

## 5. What holds up

**Holds up**
- Direction: the meta-analyses and early reviews lean positive. Strength is moderate or modest, not large.
- The practice gap (McKinsey, N=796), read in full.
- Sampling many and selecting with a checker: ToT, Large Language Monkeys, PlanSearch, all read in full.
- Diverse plans beat repeated sampling at equal attempts (PlanSearch); the authors state that compute-normalised plots agree.
- LLMs alone plan badly on classical planning; solvers and verifiers fix it.
- Self-grading is unreliable (Huang; Zheng position bias; Doshi inconsistency).
- Aggregation helps (12-LLM crowd matches humans).

**Fails or is contested**
- Publication bias: Shea-Van Fossen 2006 trims the effect to 0.109, CI crossing zero. Hamann 2022 and George 2019 report robust positive effects. Different corrections and samples. Unresolved.
- Folk view "plans fail in turbulence": Hamann finds the opposite (K03).
- Camuffo 2024 replication abstract leads with termination and pivots; "performs better" rests on the 2020 paper. It tests hypothesis testing, not planning, and is the same group. The second Italian trial lists both 257 and 250 as final count (d19).
- o1 on Mystery Blocksworld: 52.8% (Valmeekam 2024) vs 74.3% (Goh 2026). Not reconciled.
- Plan-and-Act 57.58% vs TheAgentCompany 30%: different benchmarks.
- BusiAgent +122% problem analysis: expert ratings of the authors' own system, BLEU 18.7 to 23.4. Weak (c25).
- Illusion of Thinking: critiques on token limits not opened (K15).

**Interventions that worked**
- Hypothesis-testing training for startups (humans).
- Diverse natural-language plans before code (with a checker).
- Verifier back-prompting (where the proposer is plausible).
- Stacking-specific prompts on Blocksworld: 3.83 to 59.3 (GPT-4). They encode the algorithm, so this is not generic planning.
- Knowledge-model prompting (Goh 2026): o1 Random Blocksworld 31.5 to 97.33, Mystery 74.3 to 83.3; o1-mini Mystery 19.1 to 16.83. One preprint.

**Interventions that did not**
- Self-consistency on planning prompts (lowered scores).
- Intrinsic self-correction.
- Chain of thought on tasks needing implicit judgment (d12).
- Longer reasoning on distractor or spurious-feature tasks (Gema 2025).
- Larger context in EcoGym, k=32 to 1024: no consistent gain (c24).

**Moderators.** Firm: size, sector, uncertainty (Hamann). Measure: effectiveness over financial (George). Venture: planning lowers disbanding (Delmar and Shane; size unread). LLM: difficulty bin, presence of a checker, task type (math vs judgment).

## 6. Language models

**Classical planning.** PlanBench: GPT-4 206/600 (34.3%), Instruct-GPT3 41/600 (6.8%); verification 191/600 and 4/600. Earlier version: best LLM about 12% executable plans, average about 3%; humans 78% (39 of 50); human plus LLM suggestion 18 of 22 vs 17 of 23 unaided (c13, c14). o1-preview: Mystery Blocksworld 317/600 (52.8%), o1-mini 19.1%, randomised 37.3%; Llama 3.1 405B 62.6% on plain Blocksworld; Fast Downward 100% in 0.265 s. NATURAL PLAN: Trip Planning GPT-4 31.1%, Gemini 1.5 Pro 34.8%, GPT-4o 3.7%, all under 5% at 10 cities; Gemini 1.5 Pro with 1 to 800 shots 2.7% to 39.9% (c19). TravelPlanner: two-stage final pass rate 0.6% at best, sole-planning about 4.4% (c20). GameBench: GPT-4 with CoT best, below humans (b37).

**What changed it.** Verifier loops (82% / 70%). Task-specific prompts (3.83 to 59.3). Knowledge-model prompts (Goh). Solvers (100%). Reasoning models (o1 52.8%, a large jump from GPT-4 but unreliable under obfuscation).

**Plan-first prompts.** Plan-and-Solve (text-davinci-003): +2.5 over CoT for PS and +6.3 for PS+ on math; +1.6 on StrategyQA. Error profile of 46 GSM8K CoT failures: 27% semantic misunderstanding, 12% missing step, 7% calculation (c06). Self-planning code: +6.4 over CoT.

**Option generation and ideas.** Girotra: GPT-4 ideas rated 46.8% vs 40.4% purchase intent; 49.3% with examples; 35 of top 40; about 800 ideas per hour. Meincke: baseline GPT-4 pool is less diverse (0.377 vs 0.243); CoT-style prompts close most of the gap; persona (Steve Jobs 0.368) and HBR tools (0.387) changed little. Cristofaro and Giardino 2026 studied GenAI and cognitive biases with 273 professionals (b25, abstract only). Doshi 2024: single evaluations inconsistent; aggregates resemble experts.

**Search and compute.** ToT 74% (Game of 24, GPT-4). Large Language Monkeys 15.9 to 56%. PlanSearch 55.6 to 77.0 at pass@200; with public-test filtering it reaches 77.1% at pass@20. LATS HumanEval 92.7% (c27).

**Overthinking.** o1-preview -36.3 points on implicit statistical learning (d12). Gema 2025: inverse scaling on four task groups, budgets 0 to 16,384. QwQ and R1 give 2 to 4 solution rounds on most items (d14).

**Business simulation.** Vending-Bench: huge variance. Best mean $2,217.93 but minimum $476, and some runs sold zero units. Failures are long-horizon coherence. EcoGym: Claude-Sonnet-4.5 vending net worth 1843.62 vs a Gemini-3 row near 11,272; DAU 1595 vs human experts 1,404. TheAgentCompany: best 30.3% full completion.

**Forecasting and judgment.** 12-LLM crowd Brier 0.20 vs 925 humans 0.19. Best single model GPT-4 0.15; worst Mistral-7B 0.24 (d16).

**Gaps.** No LLM study measures option count against final decision quality on strategy tasks at equal tokens. No study tests plan-first vs direct at equal tokens on open-ended judgment with a current model.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = stored experience. Evidence ids refer to the evidence files; K ids to claims.jsonl.

### Add now (established)

1. **Bind the final choice to the compared options** (S7, G10). The output lists the options considered and why one won. [E] d01, K19.
2. **Generate options in separate calls, deduplicate, require distinct families before selecting** (S3). One prompt listing N is less diverse. [E] d09, d10, K16, K20. The gain was proven with a checker; the diversity measure is what transfers.
3. **Selection by code with an external check, not by the generating model** (G5, G8, S7). [E] b33, c17, d15, K08, K23. Already in the schema; this adds evidence.
4. **Where a checker exists, spend tokens on many short attempts plus the checker** (G11, S4). [E] c07, c10, K07.
5. **Feed verifier output into the revision** (G2, S4 to S3). [S] c16 (K11) for the numbers; direction agrees with b33.
6. **Budget by difficulty; do not search on easy items** (G12, S0). [E] d11, d12, d13, K21, K22. Hamann (K03) supports it only by analogy.
7. **Route formal planning subtasks to a solver when one exists** (tool use). [E] b30, b31, K10.
8. **If a model must rank options, aggregate several judge calls in code** (G4, G5). [E] d15, d16, d17, K23. Vary order and role.
9. **Long-horizon runs: several seeds, report the minimum as well as the mean** (bench practice, memory). [E] b26, c23, K14.

### Test first

- **Plan-first vs direct at equal tokens on open-ended judgment** (S1/S2 to S3). [S] c05, c12 (K09, K12); K21 against. Old models, math or code only.
- **Number of options N** (S3). [C] K17 unverified; K20 shows gain only with a checker. Find where returns flatten.
- **Hypothesis-and-test step before committing** (O verify, S8). [S] b17, d20, K05. Same group; tests human training.
- **Replan on failure vs fixed plan** (S6). [C] b34, b35, K13.
- **Outside-view step for estimates** (G, memory). [S] b20, b19, K06.
- **Difficulty-scaled planning on judgment items** (G12). [S] K22 (math only).
- **Option quality filter without a checker** (S7). [C] d17 (abstract only).
- **Stakeholder step** (S1). [C] a01 names stakeholder management as a moderator; no agent analogue tested.

## 8. Concrete tests on our bench

All arms at equal total tokens, setup cost counted (G7). Report paired differences with CIs and the minimum across seeds.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Plan-first | Open-ended judgment and multi-step items with a key | (a) direct, (b) 150-token plan then answer | Accuracy, paired difference | 0 to +3 points on judgment; larger on multi-step; a drop on easy items is plausible (K21) |
| T2 Option count | Items with several valid routes and a checker | N=1, 3, 6, 12 options, select in code | Pass rate; distinct families | Rises then flattens; find the knee |
| T3 Separate calls vs one list | Idea or strategy items | One call listing N vs N calls plus dedupe | Distinct-family count; checker or panel score | More diversity (reference gap 0.255-0.432 vs 0.243 cosine); gain in score if a checker exists |
| T4 Selector | Option sets with an expert key | Generator picks / fresh-call judge / mean of 5 shuffled judges in code / external checker | Agreement with key; top-1 hit rate | Checker > mean of 5 > single judge >= self-pick (K08, K23) |
| T5 Difficulty-scaled budget | Mixed-difficulty set | Flat vs small for easy, large for medium, capped for hard | Accuracy at equal total tokens | Gain from reallocation (Snell ~4x on math); smaller on judgment |
| T6 Verifier back-prompt | Constraint or planning items | Plain resample vs back-prompt with checker output | Pass rate at equal N | Higher, except where the proposer has no foothold |
| T7 Hypothesis-test step | Forecasting or diagnosis items | Plan-then-act vs hypothesis, cheap test, then act | Accuracy; Brier | Small gain only if the test is runnable (G2, G3) |
| T8 Outside view | Duration and quantity estimates | Inside view vs reference class first | Log error; calibration | Lower bias |
| T9 Binding check | Any decision item | Final answer with vs without a required "options compared" field | Share of answers matching a compared option; accuracy | Same accuracy, fewer unsupported answers |
| T10 Replan | Multi-step agentic items | Fixed plan vs replan after a failed check | Success rate over 5+ seeds | Gain where failures are visible; none otherwise |

## 9. What does not transfer, and why

- **Firm performance.** The meta-analyses link planning to profit, growth or survival over years. Our bench has no such outcome. We take the process claims, not the effect size.
- **Stakeholder management.** It works through people and commitment. A single agent has none, unless the task models stakeholders.
- **Planning cost.** Firms pay in time and meetings. The agent pays in tokens; G7 already covers it.
- **Causality.** Better firms may plan more. That flaw does not apply to an agent we control, but it means the human numbers are not causal.
- **The McKinsey bypass.** Humans override plans through politics and seniority. An agent bypasses by ignoring the field; a code-level binding check handles it.
- **Trained planners.** Plan-and-Act's gain uses a trained planner; we do not train.
- **Task-specific prompts.** The Blocksworld 3.83 to 59.3 jump encodes the algorithm.
- **Checker-dependent results.** ToT, Large Language Monkeys and PlanSearch need success tests. Strategy tasks seldom have them.
- **Old models.** PS+ and the PlanBench GPT-4 figures come from 2022-2023 models.
- **Wikipedia-sourced human facts** (planning fallacy details, Mintzberg, Ansoff) are secondary.

## 10. Open questions

1. What are the pooled r, CI and I2 in Boyd, Miller and Cardinal, George and Hamann? Does the effect survive bias correction (Shea-Van Fossen says no)? Wiley blocked every route.
2. What did Fredrickson and Mitchell 1984 and Dean and Sharfman 1996 find, and does comprehensiveness reverse under instability? Unread.
3. Do Delmar and Shane and Brinckmann give effect sizes for new ventures, and for which moderators?
4. Does the option-count gain hold for an LLM on open-ended strategy tasks at equal tokens?
5. Does plan-first beat direct on current reasoning models for open-ended judgment at equal tokens?
6. Does planning pay more under high uncertainty for LLM agents, as Hamann reports for firms?
7. What replaces a ground-truth checker for business options? Doshi's correlations need reading.
8. Will the independent Camuffo replication (Uruguay, to Sept 2026) show the effect?
9. Why do Goh 2026 (74.3%) and Valmeekam 2024 (52.8%) differ for o1 on Mystery Blocksworld?
10. Do critiques of Illusion of Thinking on token limits change the three-regime picture?
11. What did Cristofaro and Giardino 2026 (273 professionals) find on GenAI and bias in market entry? Abstract only.

## 11. Sources

[V] = opened in full or page text; [M] = abstract or snippet only. Some Wikipedia pages are marked opened in the files; that is weak evidence.

- [V] McKinsey Quarterly (2006) Improving strategic planning. https://www.jorgejuanfernandez.com/archives/Improving%20strategic%20planning,%20McKinsey%20Quarterly%202007.pdf
- [V] Shea-Van Fossen, Rothstein, Korn (2006), repository page. https://scholars.nova.edu/en/publications/thirty-five-years-of-strategic-planning-and-firm-performance-rese/
- [V] Boyd (1991), repository page. https://experts.nau.edu/en/publications/strategic-planning-and-financial-performance-a-metaanalytic-revie/ ; [M] DOI https://doi.org/10.1111/j.1467-6486.1991.tb00286.x
- [M] George, Walker, Monster (2019). https://doi.org/10.1111/puar.13104
- [M] Hamann, Halw, Guenther (2022). https://doi.org/10.1002/smj.3476
- [M] Miller and Cardinal (1994). https://doi.org/10.2307/256804
- [M] Schwenk and Shrader (1993). https://doi.org/10.1177/104225879301700304
- [M] Capon, Farley, Hulbert (1994). https://doi.org/10.1111/j.1467-6486.1994.tb00335.x
- [M] Armstrong (1982). https://doi.org/10.1002/smj.4250030303
- [M] Bracker and Pearson (1986) https://doi.org/10.1002/smj.4250070603 ; Bracker and Keats (1988) https://doi.org/10.1002/smj.4250090606 ; Rhyne (1986) https://doi.org/10.1002/smj.4250070504
- [M] Delmar and Shane (2003). https://doi.org/10.1002/smj.349
- [M] Brinckmann, Grichnik, Kapsa (2010). https://doi.org/10.1016/j.jbusvent.2008.10.007
- [M] Song et al. (2011) https://doi.org/10.1111/j.1540-5885.2011.00822.x ; Rudd et al. (2008) https://doi.org/10.1016/j.jbusres.2007.06.014
- [M] Fredrickson and Mitchell (1984) https://doi.org/10.2307/255932 ; Dean and Sharfman (1996) https://doi.org/10.2307/256784 ; Fredrickson (1984) https://doi.org/10.2307/256039 ; Nutt (1993) https://doi.org/10.1287/orsc.4.2.226
- [M] Pearce, Freeman, Robinson (1987); Ansoff (1965); Mintzberg (1994): no URL recorded.
- [M] Kahneman and Lovallo (1993). https://doi.org/10.1287/mnsc.39.1.17
- [M] Colombia ventures study (2014). https://doi.org/10.1002/smj.2113
- [V] Wikipedia: Strategic planning https://en.wikipedia.org/wiki/Strategic_planning ; Henry Mintzberg ; Strategic management ; Business plan ; Planning fallacy (same domain)
- [M] Camuffo et al. (2020) https://doi.org/10.1287/mnsc.2018.3249 ; Camuffo et al. (2024) https://doi.org/10.1002/smj.3580
- [V] AEA RCT Registry 2205 https://www.socialscienceregistry.org/trials/2205 ; 15080 https://www.socialscienceregistry.org/trials/15080 ; 6578
- [V] Girotra et al. (2023). https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2023/08/LLM-Ideas-Working-Paper.pdf
- [V] Meincke, Mollick, Terwiesch (2024). https://arxiv.org/abs/2402.01727
- [M] Doshi et al. (2024). https://doi.org/10.1002/smj.3677
- [M] Cristofaro and Giardino (2026). https://doi.org/10.1177/14761270261457350
- [V] Wang et al. PlanSearch (2024). https://arxiv.org/abs/2409.03733
- [V] Snell et al. (2024). https://arxiv.org/abs/2408.03314
- [V] Liu et al. (2025). https://arxiv.org/abs/2410.21333
- [V] Gema et al. (2025). https://arxiv.org/abs/2507.14417
- [V] Chen et al. (2025). https://arxiv.org/abs/2412.21187
- [V] Zheng et al. (2023) LLM-as-a-judge. https://arxiv.org/abs/2306.05685
- [V] Schoenegger et al. (2024). https://arxiv.org/abs/2402.19379
- [V] Wang et al. (2022) Self-consistency. https://arxiv.org/abs/2203.11171
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601
- [V] Wang et al. (2023) Plan-and-Solve. https://arxiv.org/abs/2305.04091
- [V] Valmeekam et al. PlanBench (2022) https://arxiv.org/abs/2206.10498 ; (2023) https://arxiv.org/pdf/2302.06706 ; (2024) https://arxiv.org/abs/2409.13373
- [V] Kambhampati et al. LLM-Modulo (2024). https://arxiv.org/abs/2402.01817
- [V] Huang et al. (2023). https://arxiv.org/abs/2310.01798
- [V] Stechly et al. (2025). https://arxiv.org/pdf/2405.04776
- [V] Zheng et al. NATURAL PLAN (2024). https://arxiv.org/pdf/2406.04520
- [V] Xie et al. TravelPlanner (2024). https://arxiv.org/pdf/2402.01622
- [V] Goh, Kos, Goel (2026). https://arxiv.org/pdf/2602.03900
- [V] Brown et al. Large Language Monkeys (2024). https://arxiv.org/pdf/2407.21787
- [V] Jiang et al. Self-planning (2025). https://arxiv.org/pdf/2303.06689
- [V] Plan-and-Act (2025). https://arxiv.org/abs/2503.09572
- [V] TheAgentCompany (2025). https://arxiv.org/abs/2412.14161
- [V] Backlund and Petersson Vending-Bench (2025). https://arxiv.org/abs/2502.15840
- [V] EcoGym (2026). https://arxiv.org/pdf/2602.09514
- [V] Wang and Zhang BusiAgent (2025). https://arxiv.org/pdf/2508.15447
- [V] Shojaee et al. Illusion of Thinking (2025). https://arxiv.org/abs/2506.06941
- [V] Costarelli et al. GameBench (2024). https://arxiv.org/abs/2406.06613
- [V] Zhou et al. LATS (2024). https://arxiv.org/pdf/2310.04406
