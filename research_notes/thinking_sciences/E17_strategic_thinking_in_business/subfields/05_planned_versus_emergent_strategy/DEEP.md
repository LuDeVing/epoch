# Planned versus emergent strategy: deep document

*Subfield E17.05. Sources: evidence_a-d.jsonl (ids a01-a29, b01-b25, c01-c27, d01-d22), claims.jsonl (K01-K26), critique.md. Status marks: [E] established, [S] single-source, [C] contested. [V] = page or PDF text opened, [M] = snippet, metadata or memory only. The human-strategy side is mostly abstracts and metadata. The LLM side is mostly read from arXiv PDFs.*

## 1. What it is

Mintzberg's claim: strategy is a pattern in a stream of decisions, not only a plan. This gives three kinds of strategy.

- **Intended strategy**: what leaders meant to do.
- **Realized strategy**: the pattern that actually appears in what was done.
- **Deliberate**: intended and realized.
- **Unrealized**: intended but not realized.
- **Emergent**: realized but never intended.

Realized = deliberate + emergent. The vocabulary of the 1985 paper is recalled, not read in full (a04, d07). The abstract confirms a continuum and eight types.

The second idea (1994): planning is analysis ("finding the dots"). Strategy formation is synthesis ("connecting the dots"). Planning coordinates, measures and communicates. It does not create strategy (a11, b03, b21; all via Wikipedia).

The opposing school (Ansoff, Chandler, the design school) says strategy is formulated first and implemented after. Ansoff adds that the more turbulent the setting, the more real-time adaptation is needed (a07, a29).

**Why this matters for our agent.** The schema already has a plan-then-act graph (S1 to S8) and a look-back state S9. The question is how fixed the plan should be, and what the agent should do with the gap between its first plan and what it actually did. No published LLM study tests deliberate versus emergent strategy as such (c26, K17). What exists are plan-versus-react-versus-replan ablations in agent papers. The mapping to Mintzberg is ours, not the authors'.

Three kinds of evidence are in this file:
1. Human strategy theory and field studies. Qualitative cases, a few meta-analyses, mostly not opened in full.
2. Entrepreneurship trials (plan or experiment).
3. LLM agent studies, 2022-2026: ReAct, ADaPT, Plan-and-Act, AdaPlanner, Reflexion, business-simulation benchmarks.

## 2. History and theories in depth

**1978, Mintzberg, "Patterns in Strategy Formation" (Management Science) [V, abstract] (a01, a02).** Two cases: Volkswagenwerk 1934-1974 and the US government in Vietnam 1950-1973. Three conclusions. (1) Strategy formation is the interplay of a dynamic environment and bureaucratic momentum, with leadership in between. (2) Strategies follow life cycles and change-continuity cycles. (3) The gap between intended and realized strategy is the heart of the matter. Crossref counts 2,354 citing works. No numbers; two cases only.

**1983-1991, Burgelman (a09, a10).** Field study of internal corporate venturing, then a model with two processes. Induced: top-down, fits the current strategy. Autonomous: bottom-up initiatives, selected later by management. Data come from Intel. One firm, no tests, survivor risk.

**1984, Pascale on Honda (a15, a16).** The best-known emergence story. American Honda was founded in 1959. In 1960 a Boise dealer sold more Honda 50s than six Los Angeles dealers together, after adding knobby tires and a larger rear sprocket to sell it as a trail bike [V, Wikipedia]. Pascale told it as accident (the plan was large bikes). A rival account (Goold, 1996) disputes the facts [M, memory]. The famous case is itself contested and told after the fact.

**1985, Mintzberg and Waters, "Of strategies, deliberate and emergent" (SMJ) [V, abstract only] (a03, d07, b01).** Deliberate and emergent are the two ends of a continuum, not a dichotomy. Eight types: planned, entrepreneurial, ideological, umbrella, process, unconnected, consensus, imposed. The full text was blocked (HTTP 403). How "deliberateness" was measured is not verified. Definitions of umbrella (broad targets, others fill details), process (leaders control process, not content) and imposed (from environment) are from memory (a05). 3,027 citing works.

**1990-1991, the design-school dispute (a06, a07, a08).** Mintzberg 1990 attacks the design school: conscious control by the chief executive, a simple informal model, explicit simple strategies, full formulation before implementation. Ansoff 1991 says the critique is weak on method and fact. Mintzberg replies "Learning 1, planning 0". Argued in prose; not settled by data. Both are parties to the dispute.

**1994, "The Rise and Fall of Strategic Planning" (b21, a11).** Planning is analysis, strategy is synthesis. Planning done far from the front line is the weak form.

**1997-2000, Levinthal; Gavetti and Levinthal (a26) [M, memory].** Simulation on rugged (NK) landscapes. Local search is emergent and experience-driven. Cognitive search uses a simplified map of the landscape. Combining a rough map first with local search second does best. This is evidence by model, not by field data. Results depend on ruggedness.

**1978-80, Quinn (logical incrementalism) and Lindblom 1959 (a27) [M].** Small steps within a stated direction. Close to the schema's attempt-check-revise loop.

**1999, Brews and Hunt (a28) [M]; Moncrieff and Markides (a13) [V, Wikipedia].** Planning and learning are not opposed. Planning with flexibility did well in unstable settings (recalled, unverified).

**2001, Sarasvathy, effectuation (a17, b09) [V, secondary].** Experienced founders on a hypothetical venture paid less attention to prediction, limited loss, and built partnerships. 13,617 citing works. Critics: no stated boundary conditions, mostly cross-sectional questionnaires (Arend et al. 2015). No head-to-head test against planning.

**2019-2023, the meta-analyses (d01-d03).** George, Walker and Monster (2019): r = .229. Hamann et al. (2023): 183 samples, larger under high uncertainty (abstract only). Details in section 3.

**2020-2022, scientific approach to startups (d05, d06).** Camuffo et al. randomised trial of 116 Italian startups. Koning, Hasan and Chatterji on A/B testing. Direction only.

**Competing explanations for "planning helps".** (a) Plans turn abstract goals into concrete steps (b05). (b) Plans signal legitimacy to readers (b07, listed, not opened). (c) Survivor bias in observational studies. (d) Single-source survey inflation (d01 flags this).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Strategy is a pattern; realized differs from intended | Two cases (VW 1934-74, Vietnam 1950-73). No effect sizes | a01, a02 (Mintzberg 1978) | [S] qualitative |
| Deliberate and emergent are a continuum; 8 types | 8 types named | a03, d07 (Mintzberg and Waters 1985) | [E] as theory, abstract only |
| Planning-performance link is positive, small to moderate | r = .229, 95% CI [.186, .271], 87 correlations in 31 studies, I2 = 91.6%, tau2 = .032; per study r = .255 [.177, .333] | d01 (George et al. 2019) | [E] direction; effect modest |
| Moderators of that link | Constant (formal, effectiveness, single source) .417. Participation -.129 (p<.05). Efficiency -.357 (p<.01). Sector, country not significant. About 71% of variance explained. Egger test significant (2.651, p<.001) | d02 | [E] |
| Planning effect larger under high uncertainty and in larger firms | 183 samples, 84 new; no effect sizes read | d03 (Hamann et al. 2023) | [S] abstract only |
| Older meta-analyses (Miller and Cardinal 1994; Brinckmann 2010) | Not opened. Citations 603 and 521 | d04, b06, b22 | not verified |
| Planning reduces venture disbanding | Swedish ventures, N about 223 recalled | b05 (Delmar and Shane 2003) | [S] not opened |
| Scientific approach raises performance and pivots | 116 Italian startups, 16 data points over about a year; no extra dropout. No effect size read | d05 | [S] direction |
| A/B testing links to page views and launches | IV and synthetic control; no N read | d06 | [S] direction |
| ReAct beats act-only | ALFWorld (134 games) best trial 71%, Act 45%, BUTLER 37%; worst ReAct trial 48%; gain 33-90%, mean 62% | a18, c01 | [E] |
| ReAct trails CoT on some QA | HotpotQA EM CoT 29.4, ReAct 27.4, ReAct-to-CoT-SC 35.1. FEVER CoT 56.3, ReAct 60.9, CoT-SC-to-ReAct 64.6 | a18 | [E] hybrid beats pure |
| ReAct failure type | Reasoning error 47% of ReAct failures vs 16% of CoT (200 sampled, HotpotQA) | a18, c02 | [S] not re-verified |
| Plan-first prompt (Plan-and-Solve) | text-davinci-003. Arithmetic avg: zero-shot CoT 70.4, PS 72.9, PS+ 76.7, manual CoT 77.6. Missing-step errors 12% to 7% (N=100) | a19 | [E] helps coverage, not meaning |
| Static plan vs reactive, mixed | ADaPT (GPT-3.5): ALFWorld ReAct 43.3 = P&E 43.3; WebShop ReAct 32.0, P&E 17.0; TextCraft ReAct 19.0, P&E 27.0 | a20, b17, c07, c08 | [E] task decides |
| Plan only when stuck | ADaPT: ALFWorld 71.6, WebShop 44.0, TextCraft 52.0; TextCraft depth 3 1.8 to 38.7, depth 2 26.9 to 78.2 | a20, c07, c08 | [E] |
| Revisable plan beats static plan | WebArena-Lite: fine-tuned executor, no planner 36.97; static planner 43.63; + dynamic replanning 53.94 (+10.31); + CoT 57.58. Untuned executor 9.85 | a22, c05, c06 (critique corr. 1) | [S] needs fine-tuning |
| Plan with predicted observations, rewrite on mismatch | AdaPlanner: ALFWorld 91.79% (GPT-3), 80.60% (gpt-3.5-turbo); MiniWoB++ 91.11%; without code-style interface ALFWorld 81 to 46 | d15 | [S] |
| Promote verified successes into the plan | AdaPlanner skill discovery: ALFWorld nearly doubles, MiniWoB++ about +15. AWM +24.6% (Mind2Web), +51.1% (WebArena) relative. ExpeL insights beat hand-written | d16, d19, d20 | [E] with verifier |
| Plan-first saves tokens | ReWOO over 6 benchmarks: 64% fewer tokens, +4.4 points. HotpotQA tokens 9795 vs 1986; cost per 1k queries $21.29 vs $3.97 | b18, c14 | [E] when steps independent |
| Plan-first under tool failure | ReAct 40.8 to 0; ReWOO 42.4 to 13.2 (artificial failure) | b18 | [E] weak test |
| Learning loop needs a real check | Reflexion: ALFWorld 130/134 in 12 trials; HumanEval 91.0 vs 80.1; MBPP 77.1 vs 80.1 (worse); no significant WebShop gain | a21, c03 | [E] |
| Self-correction without oracle fails | GPT-3.5 GSM8K 75.9 to 95.5 with oracle, to 74.7 without; CommonSenseQA 75.8 to 41.8 | d17, d18 | [E] |
| LLMs plan poorly alone | PlanBench GPT-4 206/600 (34.3%); Mystery Blocksworld 26/600 (4.3%); replanning 48.1%, reuse 65.3%, goal reformulation 76.8-87%. TravelPlanner GPT-4 0.6% (best prompting 0.7%, GPT-3.5). With verifier up to 15 rounds: Blocks World 82%, Logistics 70%, Mystery about 10% | c10, c12, b19 | [E] older models |
| Long-horizon business agents derail | Vending-Bench, 5 runs: Claude 3.5 Sonnet $2,217.93 (min $476); o3-mini $906.86; human $844.05 (1 run); Gemini 1.5 Pro $594.02. Days to sales stop: 102, 86, human 67 | b11, c17, c18 | [E] |
| Memory helps long-horizon agents, model-dependent | EcoGym Gemini-3-Pro: none 11282, working 13679, symbolic 15567, episodic 18939, Mem0 15406. Flash: none 5676, working 10099. Context 32-1024 no consistent gain | b13, d12 | [S] |
| Thinking mode | Gemini-3-Flash DAU 1194 to 1396 | b12, d12 | [S] |
| Rankings unstable across runs and backbones | CEO-Bench 3 runs: rule-based $15.8M; best model $12.6M; GPT-5.6 Sol other two runs bankrupt near day 190; 3 models bankrupt every run | d10 | [E] |
| Plan edits and contingencies in top agents | Targeted R&D share: 88%, 51%, 25%, 19%, 11% by model; "if" frequency higher in top two (proxy) | d11 | [S] correlational |
| Boldness is the weak part, not plan validity | Can-LLMs-Be-CEOs: valid plans 13/13 to 11/13; overall 73.86 to 63.87; one run per scenario | b14, d13 | [S] |
| Reflection below CoT on consulting | EnterpriseBench: Self-Refine and Reflexion below CoT; best method flips by backbone; judge-human r = 0.71 (20 cases), 0.887 (500 transcripts) | b15, d14 | [E] |
| Fixed Plan-and-Execute weakest protocol | Router 0.708 vs best fixed 0.669; Plan-Execute 0.550; oracle 0.754; simulated oracle | b20 | [S] |
| Plan momentum | 39% average drop multi-turn, unreliability +112%, aptitude loss about 15%, 15 models, 200,000+ conversations | d21 | [S] chat tasks |
| Drift modes | MAST: 14 modes, 1600+ traces, kappa 0.88; reasoning-action mismatch 13.2%, unaware of termination 12.4% | d22 | [S] rough |
| LLM plans rated above entrepreneurs' | +0.14 SD (p<0.001); accept +5 (p=0.003); investment +2.55 on 0-100 (p=0.007); interest in intro +3 (p=0.094, ns); vs rejected plans +7/+8/+6; vanished vs accepted; 309 plans, 10 used, 250 investors, 2,500 ratings | a23, c20 | [E] but ratings only |
| LLM scores track investor scores | r = 0.52, R2 0.29; ICC 0.51 vs 0.25 between single VCs; 731 plans, 138 text-only, 541 evaluations | c21 | [S] |
| Fashion bias in LLM advice | HBR: 7 tensions, favours differentiation, augmentation, long-term. Pilot 240 runs: Claude Sonnet 4.5 resists adversarial instruction 75.0% vs GPT-4o 27.5%; GPT-4o flips 72% to 98% with context | d08, d09 | [S] original unopened |
| GPT-4 on strategy tasks | DCF price $28, then $96, correct about $35; o1-preview same answer on resubmission | c22 | [S] case |

## 4. Mechanisms and models

**4.1 Intended-versus-realized ledger (an implementable Mintzberg measure).**
- At plan time, code stores the plan as an ordered list of steps, each with a predicted observation and a success check.
- During the run, code appends each executed action and observation.
- After the run, code aligns the two lists. Output: the share of final solution steps that were in the first plan (deliberate share), the share added during the run (emergent share), and the share of planned steps never done (unrealized share).
- Realized = deliberate + emergent. The measure is ours. The paper's own measurement is unverified (a04, d07).
- Use: a log field for S9, and a way to ask whether emergent steps that were kept correlated with success.

**4.2 Replan trigger on mismatch (AdaPlanner design) (d15).**
- The plan lists predicted observations.
- If the real observation matches, fold it in (in-plan refinement) and continue.
- If it contradicts the prediction, rewrite the plan from the point of the mismatch (out-of-plan refinement).
- This is gated by a signal, which fits G1. Plan-and-Act replans every step (a22), which is a schedule. No study compares the two at equal tokens.

**4.3 Decompose on failure only (ADaPT) (a20).**
- Try the task directly with an executor.
- If the executor fails, ask the planner to split it into sub-tasks. Recurse to a depth limit (dmax 3 or 4).
- Control flow is in code. Gain depends on executor strength.

**4.4 Plan-first without re-observation (ReWOO) (b18).**
- The model writes the whole tool plan with placeholders. Code runs the tools. The model reads the evidence once.
- Cheap. Fails when a step depends on a surprising earlier result.

**4.5 Router by task type (b20, c27).** No fixed form wins. Pick plan-first when steps are independent and the world is stable (ReWOO, TextCraft). Pick reactive or replan-on-mismatch where observations matter (WebShop, Plan-and-Act). The bandit router result is from a simulated oracle and is weak support.

**4.6 Two-path model (Burgelman) (a10).**
- Induced path: follow the plan.
- Autonomous path: a small probe budget for side attempts.
- Selection by code run, not by the model's taste. Honda's Boise dealer is the analogy (a15).

**4.7 Promotion rule (d16, d19, d20).** A pattern from execution enters the plan or memory only after code-verified success, preferably repeated. ExpeL found unverified reflections hurt. Tag every stored lesson verified or unverified.

**4.8 Plan-momentum break (d21, a01).** Mintzberg's "bureaucratic momentum" has an LLM counterpart: early commitment, then no recovery. Proposed trigger: when a new observation contradicts a stated plan prediction, restart from a short recap rather than patching the old draft. No published trigger exists; this is ours.

**4.9 Strategy as search, representation, aggregation (a24).** Csaszar et al.: search is trial on a landscape, representation is a simplified model, aggregation combines weak solutions. Mapping to our states: restate problem = representation, operators = search, vote in code = aggregation. The mapping to planned-versus-emergent is our reading.

## 5. What holds up

**Holds up.**
- Planning has a small to moderate average link to performance, r about .23 (d01). It is strongest for goal achievement and weakest for efficiency. The two main meta-analyses agree on direction.
- Pure forms lose to hybrids in agent studies. ReAct plus CoT-SC (35.1) beats either alone on HotpotQA. Plan plus replanning beats plan alone (a22). Adaptive decomposition beats both static plan and reactive loop (a20).
- Reflection and learning loops help only with a hard check (d17, d18, a21, d19, b15).
- LLMs generate plans poorly alone and do better with an external verifier (c10, b19). Revising an existing plan is easier than writing one (replanning 48.1% vs generation 34.3% on PlanBench).
- Long-horizon business agents are high-variance. Run-to-run spread is as large as the gap between models (d10, b11).

**Contested or weak.**
- Mintzberg versus Ansoff was never resolved by data (K03). The meta-analytic positive effect does not refute Mintzberg's claim, which is about where strategy comes from, not whether plans correlate with results.
- The "planning is weaker in turbulence" intuition is not supported by Hamann et al. (larger effect under high uncertainty). Only the abstract was read. George et al. did not test dynamism.
- Heterogeneity is very high (I2 91.6%), Egger test flags bias, and single-source surveys inflate the effect.
- Honda is disputed (a16). Effectuation has weak causal evidence (b09).
- Brinckmann 2010, Miller and Cardinal 1994, Delmar and Shane, Camuffo effect sizes: not opened (K16).

**Failed or null.**
- Static up-front plan on WebShop: 17.0 vs ReAct 32.0 (a20).
- Reflexion on MBPP: 77.1 vs 80.1 (a21). No significant WebShop gain.
- Self-correction without oracle: GSM8K 75.9 to 74.7, CommonSenseQA 75.8 to 41.8 (d17).
- Reflexion and Self-Refine below CoT on consulting (b15).
- Longer context gave no consistent gain in EcoGym (d12).
- LLM-plan rating advantage vanished against accepted plans (c20).

**Moderators.**
- Task structure: compositional with known structure favours plan (TextCraft, ReWOO). Surprising environment favours reactive (WebShop).
- Executor strength: ADaPT gains depend on it.
- Model family: memory type, best method and fashion-bias behaviour flip across backbones (d12, d14, d09).
- Verifier availability: governs every learning-loop result.
- Plan-and-Act's gain needed fine-tuning of planner and executor.

**Interventions that worked.** Replan on mismatch or failure; decompose on failure; code-verified skill promotion; external verifiers; episodic memory on the stronger model; hypothesis-and-test training for startups (direction only).

**Interventions that did not.** Intrinsic self-reflection; adding unverified reflections; more context length; richer prompts against trendslop (HBR, unverified). Scheduled replanning was never shown better than gated replanning, but it was also never tested at equal tokens.

## 6. Language models

**ReAct, reactive loop (a18, c01, c02).** PaLM-540B few-shot. ALFWorld best trial 71% vs Act 45%. HotpotQA ReAct 27.4 is below CoT 29.4. Failures: reasoning error and repeated steps 47% vs 16% for CoT. The paper says combining both wins.

**Plan first (a19, b18).** Plan-and-Solve lifts zero-shot arithmetic from 70.4 to 72.9 (PS) and 76.7 (PS+). Gains are mostly on arithmetic. On commonsense it stays below few-shot CoT (CSQA 71.9 vs 78.3). ReWOO uses 64% fewer tokens with +4.4 points, but breaks when plans cannot adapt.

**Plan versus reactive versus adaptive (a20).** GPT-3.5. Fixed plan equals or loses to ReAct on two of three tasks. Plan-on-failure beats both on all three, gains up to 28.3, 27 and 33 points.

**Replanning (a22, d15).** Plan-and-Act: +10.31 for dynamic replanning over static plan, but fine-tuned, synthetic data, web tasks. AdaPlanner: 91.79% ALFWorld (GPT-3), 80.60% (gpt-3.5-turbo). Interface matters: without code-style interface 81 to 46.

**Planning ability itself (c10, c12, b19).** GPT-4: 34.3% Blocksworld, 4.3% obfuscated, 0.6% TravelPlanner. Verifier loops reach 82%. These are early models. Later reasoning models were not measured here.

**Learning from outcomes (a21, d17-d20).** Reflexion 130/134 on ALFWorld, HumanEval 91.0 vs 80.1. Gains vanish with vague feedback and can reverse. Workflow and skill memory add +24.6% and +51.1% relative (AWM) with success signals.

**Long-horizon business simulation (b11-b16, d10-d14).**
- Vending-Bench: mean $2,217.93 with minimum $476 for the best model; some runs end at about 18 days; failures not tied to full memory (r = 0.167).
- CEO-Bench: every model below the rule-based baseline ($15.8M); only three above the $1M start in their best run.
- EcoGym: no model wins all three environments. Episodic memory lifts Gemini-3-Pro from 11282 to 18939.
- Can-LLMs-Be-CEOs: plans are valid, boldness is poor (under-reallocation).
- EnterpriseBench: rankings flip with backbone.
- Ovezmyradov: models crossed a point of no return in periods 4 to 8 (single run each).
- Top CEO-Bench agents keep editing a written plan with if-then contingencies, but this is correlational (d11).

**Failure modes (d21, d22, c18).** Plan momentum (39% drop). Step repetition, unaware of termination, reasoning-action mismatch. Derailment from misread state (assumed an order arrived; believed a drought meant failure; about 1,300 messages without tool calls).

**Strategy writing (a23, c21, c22, c23).** LLM plans are rated slightly above entrepreneurs' (+0.14 SD) and LLM scores correlate 0.52 with investors. This is plans as text. Nothing shows they survive action. GPT-4 can do market research and framing but failed a DCF (price $28, then $96). Analysis-style work is mechanisable; synthesis and arithmetic need checks.

**Bias.** Trendslop (d08, d09): preference for fashionable options; pilot shows model-specific behaviour. Single working paper, original unopened.

**Caveat.** Models, tasks and training differ across papers. Only within-paper ablations compare plan forms validly (critique).

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Revise or replan only from a failed check or contradicted prediction, not on a schedule. Plan on demand (decompose when the executor fails). | G1, O3 | [E] | a20, b17, c07, c08, c27, d15 (K08, K10) |
| A2 | Store lessons in S9 and memory only when a checkable outcome supports them. Tag verified versus unverified. | S9, memory | [E] | a21, d17, d18, d19, b15 (K07, K21) |
| A3 | Use an external check or code verifier on plan steps. The model proposes, code verifies. | G2, G5 | [E] | c10, b19, c12 (K12) |
| A4 | Treat plan depth as a dial, not a switch. Hybrid of plan and reactive loop. Do not choose a pure form for all tasks. | S0 mode choice | [E] | a03, a18, a20, d07 (K02, K05, K08) |
| A5 | Persist verified state in code (ledger, running totals). Detect repeated steps and silent drift. | G, memory | [E] | b11, c17, c18, c02, c04, d22 (K06, K13) |
| A6 | Evaluate any plan-versus-react scaffold with at least 3 runs per setting and 2 backbones. Report mean and worst run. | G7 | [E] | d10, d12, d14, b11 (K24) |
| A7 | Do not judge a plan by how good its text looks. Judge by what it changes in action. | G10 | [E] | a23, c20, b07 (K15) |
| A8 | Plan-first with no re-observation as a cheap mode, only where steps are independent and tools reliable. | G7 cost | [E] | b18, c14 (K11) |
| A9 | Promote an unplanned success into reusable memory only after verified success (log the promoted pattern). | S9, memory | [E] with verifier | d16, d19, d20 (K22) |

Note on A1: the failure-trigger evidence (ADaPT) is established. That on-surprise replanning beats scheduled replanning at equal tokens is not; it is test T2 below.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Explicit intended plan with predicted observations, diffed against the realized trace; log deliberate, emergent and unrealized shares | S9, memory | [S] | d15, d11, d22, a01 (K01, K26) |
| T2 | Replan every step vs on failure vs on mismatch at equal tokens | G1, S5, S6 | [S] | a22, d15 (K09, K26) |
| T3 | Plan-momentum break: restart from a recap on contradiction | S6 | [S] | d21, a01 (K23) |
| T4 | Probe budget (Burgelman autonomous path): a small share of tokens on side attempts, selected by code | S3, O | [S] | a10, a15, c16 (K04) |
| T5 | Each plan step carries a hypothesis and a pivot rule | S1, S9 | [E] human, [S] LLM | d05, d06 (K20) |
| T6 | Plan helps more under hidden state or noise than on stable tasks | S0 | [C] | d03 (K19) |
| T7 | Forced counter-case and forced choice before strategy-like advice | S7 | [S] | d08, d09 (K25) |
| T8 | Boldness check: compare plan magnitude to stated state | S4 | [S] | b14, d13 |
| T9 | Reference-class correction of the agent's own cost and time estimates from past runs | S9, memory | [C] | b10 (planning fallacy; no LLM test) |

## 8. Concrete tests on our bench

All arms get the same total token budget, including setup and any replans. At least 3 seeds per arm and 2 backbones (A6). Report mean, worst run and cost.

1. **Plan-versus-trace diff (T1).**
   - Items: multi-step ARC-style or long-horizon items where a first plan is possible (10+ steps), plus any bench item with partial hidden state.
   - Arms: (a) no plan, ReAct-style loop; (b) plan only; (c) plan with predicted observations plus code diff, replan on mismatch.
   - Metric: solve rate, tokens per solved item, deliberate/emergent/unrealized shares.
   - Expected: (c) beats (b) by a few points; (a) wins on stable-structure items. No effect would show the diff costs more than it gives.
2. **Replan timing (T2).**
   - Items: same set as test 1.
   - Arms: replan every step; replan on failed check; replan on prediction mismatch; never.
   - Metric: solve rate at equal tokens; number of replans.
   - Expected: on-failure and on-mismatch beat every-step at equal tokens because every-step spends budget. Plan-and-Act's +10.31 may shrink without fine-tuning.
3. **Plan-momentum break (T3).**
   - Items: items where an observation midway contradicts the plan.
   - Arms: patch the old plan; restart from a recap after contradiction.
   - Metric: recovery rate after contradiction.
   - Expected: restart wins; the 39% multi-turn drop suggests patching carries bias.
4. **Probe budget (T4).**
   - Items: items with a hidden better route (class with a cheap side attempt).
   - Arms: all tokens on the plan; 80/20 plan versus code-selected probes.
   - Metric: solve rate, share of wins coming from probes.
   - Expected: small gain, only where the class has some success (G12).
5. **Hypothesis per step (T5).** Arms: plain plan; plan with a hypothesis and pivot rule per step. Metric: pivots, early stops, solve rate. Expected: more early stops of bad branches; variance up (d06 notes both tails rise).
6. **Plan value by environment (T6).** Items: matched stable and noisy variants. Arms: plan versus no plan. Metric: plan benefit on each. Expected from Hamann: larger benefit on the noisy variant; if reversed, the human result does not transfer.
7. **Lesson memory with and without verifier (K21).** Arms: no notes; notes only after verified outcome; notes always. Metric: later-item solve rate. Expected: verified-only best; always-notes can hurt (ExpeL).
8. **Counter-case forcing on advice items (T7).** Items: strategy-style choice items with a known better option under given context. Arms: plain; forced counter-case then choice. Metric: choice matches context-appropriate option. Test per model.
9. **Boldness check (T8).** Items: resource-allocation items with a stated state. Arms: plain plan; plan plus code check of magnitude versus rule. Metric: score against rule baseline.

## 9. What does not transfer, and why

- **Firm-level performance results.** Meta-analyses (r = .229) measure survey-based organisational outcomes over years in firms and public bodies. They say nothing about a 20-step agent episode. Use them only as a prior.
- **Honda, Intel and VW stories.** Told after the fact, single firms, survivor bias. The scaffold cannot copy a narrative.
- **Mintzberg's measures of deliberateness.** Not verified (full text blocked). We designed our own ledger.
- **Founders' effectuation and lean-startup methods.** Rest on human experience, social partnerships and costly real tests. Our tests are cheap and code-checked, so the boundary condition (tests costly, results unreadable) does not apply the same way (b08).
- **Camuffo and Koning.** Training effects on people and platform adoption. Not a change in a prompt.
- **LLM plan ratings (Csaszar).** Rated text by investors, 10 plans, GPT-3.5. It shows text quality, not adaptation.
- **Game-theory strategic reasoning (Kader and Lee, a25).** "Strategic" there means modelling other players (p-beauty contest: GPT-o1 4.42 vs GPT-4 2.39). Different construct.
- **Plan-and-Act's numbers.** Fine-tuned planner and executor on synthetic data. Our agent does not train.
- **Old-model numbers.** GPT-3.5 and PaLM-540B results (ADaPT, ReAct, PlanBench) may shift with current reasoning models. The direction (replan on signal) is likely stable; the sizes are not.
- **Business-sim benchmarks.** 2026 papers, one to five runs, LLM judges. Rankings are fragile.
- **Router result (b20).** Headline uses a simulated latent oracle.

## 10. Open questions

1. Does an explicit intended plan diffed against the realized trace improve long-horizon score at equal tokens? No controlled study found (K26).
2. When to replan: every step, on failure, or on surprise? No equal-token comparison exists.
3. What is the full effect-size structure of Hamann et al. 2023, Miller and Cardinal 1994 and Brinckmann 2010? Only abstracts or metadata read.
4. Is the planning benefit really larger in uncertain environments, and what does it mean for agents with hidden state?
5. How did Mintzberg and Waters measure deliberateness? Full text blocked.
6. What are the numeric effects in Camuffo (2020) and Koning (2022)?
7. What are the original HBR trendslop numbers? The "about 11 percent" figure is unverified.
8. Does promoting an unplanned success into the plan help in business-like tasks without a hard verifier?
9. Can an outside-signal break trigger be built and does it beat patching?
10. Do newer reasoning models still show the static-plan-loses-to-reactive pattern?
11. Is Strategy Science 2026 (Back Bay Battery) a useful benchmark? Only a search summary seen (c24).
12. Does the Honda account hold up (Pascale versus Goold)?

## 11. Sources

**Human strategy literature**
- [V, abstract] Mintzberg 1978, Patterns in Strategy Formation. https://api.crossref.org/works/10.1287/mnsc.24.9.934 (a01, a02)
- [V, abstract] Mintzberg and Waters 1985, Of strategies, deliberate and emergent. https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html ; https://doi.org/10.1002/smj.4250060306 (a03, a04, a05, b01, d07; definitions beyond the abstract are [M])
- [V, abstract] Mintzberg 1990, The design school. https://api.crossref.org/works/10.1002/smj.4250110302 (a06)
- [V, abstract] Ansoff 1991, Critique of Mintzberg. https://api.crossref.org/works/10.1002/smj.4250120605 (a07)
- [V, metadata] Mintzberg 1991, Learning 1, planning 0. https://api.crossref.org/works/10.1002/smj.4250120606 (a08)
- [V, metadata] Burgelman 1983. https://api.crossref.org/works/10.2307/2392619 (a09)
- [V, abstract] Burgelman 1991. https://api.crossref.org/works/10.1287/orsc.2.3.239 (a10)
- [V, Wikipedia] Strategic planning (Mintzberg 1994 summary; George et al. mention). https://en.wikipedia.org/wiki/Strategic_planning (a11, b04, b21)
- [V, Wikipedia] Strategic management. https://en.wikipedia.org/wiki/Strategic_management (a12, a13, b03)
- [V, Wikipedia] Strategy. https://en.wikipedia.org/wiki/Strategy (a14)
- [V, Wikipedia] Honda Super Cub. https://en.wikipedia.org/wiki/Honda_Super_Cub (a15)
- [M] Pascale 1984, Honda story, California Management Review, recalled (a16)
- [V, Wikipedia] Effectuation (Sarasvathy 2001; Dew 2009; Arend 2015). https://en.wikipedia.org/wiki/Effectuation (a17, b09)
- [M] Levinthal 1997; Gavetti and Levinthal 2000; March 1991, recalled (a26)
- [M] Quinn 1978/1980; Lindblom 1959, recalled (a27)
- [M] Brews and Hunt 1999, recalled (a28)
- [V, Wikipedia] Igor Ansoff. https://en.wikipedia.org/wiki/Igor_Ansoff (a29)
- [V, Wikipedia] Henry Mintzberg. https://en.wikipedia.org/wiki/Henry_Mintzberg (b02)
- [V, Wikipedia] Lean startup; Business plan. https://en.wikipedia.org/wiki/Lean_startup ; https://en.wikipedia.org/wiki/Business_plan (b08, b10)

**Meta-analyses and entrepreneurship**
- [V full text] George, Walker, Monster 2019. https://repub.eur.nl/pub/120708/Repub_120708_O-A.pdf (d01, d02)
- [V, abstract] Hamann, Halw, Guenther 2023. https://econpapers.repec.org/RePEc:bla:stratm:v:44:y:2023:i:7:p:1803-1819 (d03)
- [M] Miller and Cardinal 1994. https://doi.org/10.1002/smj.4250150605 ; https://doi.org/10.2307/256804 (b22, d04)
- [M] Brinckmann, Grichnik, Kapsa 2010. https://doi.org/10.1016/j.jbusvent.2008.10.007 (b06)
- [M] Delmar and Shane 2003. https://doi.org/10.1002/smj.349 (b05)
- [M] Planning for the market, 2004. https://doi.org/10.1016/j.jbusvent.2003.11.001 (b07)
- [V, abstract] Camuffo et al. 2020. https://doi.org/10.1287/mnsc.2018.3249 (d05); [M] b23, https://doi.org/10.1287/mnsc.2019.3270
- [V, abstract] Koning, Hasan, Chatterji 2022. https://www.nber.org/papers/w26278 (d06); [M] b24, https://doi.org/10.1287/mnsc.2021.4072
- [M] Coverage note on classic meta-analyses (b25)

**LLM and AI studies**
- [V] ReAct, Yao et al. 2022. https://arxiv.org/abs/2210.03629 (a18, c01, c02)
- [V] Plan-and-Solve, Wang et al. 2023. https://arxiv.org/abs/2305.04091 (a19, c13)
- [V] ADaPT, Prasad et al. https://arxiv.org/abs/2311.05772 (a20, b17, c07, c08, c09, c27)
- [V] Reflexion, Shinn et al. 2023. https://arxiv.org/abs/2303.11366 (a21, c03, c04)
- [V] Plan-and-Act, Erdogan et al. 2025. https://arxiv.org/abs/2503.09572 (a22, c05, c06)
- [V] Csaszar, Ketkar, Kim 2024. https://arxiv.org/abs/2408.08811 (a23, a24, c20, c21)
- [V] Kader and Lee 2025. https://arxiv.org/abs/2412.13013 (a25)
- [V] Vending-Bench. https://arxiv.org/abs/2502.15840 (b11, c17, c18)
- [V] EcoGym. https://arxiv.org/abs/2602.09514 (b12, b13, d12)
- [V] Can LLMs Be CEOs. https://arxiv.org/abs/2606.17459 (b14, d13)
- [V] EnterpriseBench. https://arxiv.org/abs/2609.37658 (b15, d14)
- [V] Ovezmyradov, AI Playing Business Games. https://arxiv.org/abs/2509.26331 (b16)
- [V] ReWOO. https://arxiv.org/abs/2305.18323 (b18, c14)
- [V] LLMs Can't Plan, LLM-Modulo. https://arxiv.org/abs/2402.01817 (b19, c11)
- [V] IMACS router. https://arxiv.org/abs/2607.25446 (b20)
- [V] AdaPlanner. https://arxiv.org/abs/2305.16653 (c15, d15, d16)
- [V, abstract] Voyager. https://arxiv.org/abs/2305.16291 (c16)
- [V] PlanBench. https://arxiv.org/abs/2206.10498 (c10)
- [V] TravelPlanner. https://arxiv.org/abs/2402.01622 (c12)
- [V] Project Vend. https://www.anthropic.com/research/project-vend-1 (c19)
- [V] Lechner et al. 2024, CMR Berkeley. https://cmr.berkeley.edu/2024/09/can-genai-do-your-next-strategy-task-not-yet (c22)
- [V] Strategic management analysis by LLM. https://arxiv.org/abs/2409.06643 (c23)
- [M] Strategy Science 2026 summary. https://www.ebsco.com/articles/history/f0c5b23d-3ecc-504d-ab15-4624d69dae08/how-well-can-ai-do-strategy-empirical-benchmarking-using-strategy-simulations (c24)
- [M] Trendslop blog summary (404). https://zby.github.io/commonplace/sources/researchers-asked-llms-strategic-advice-trendslop/ (c25); HBR summary https://www.ebsco.com/articles/business-and-management/2b719c91-ae1b-588d-9ad1-2be2f30e67ec/researchers-asked-llms-for-strategic-advice-they-got-trendslop-in-return (d08)
- [V, record page] Lerer 2026 Zenodo pilot. https://zenodo.org/records/19867851 (d09)
- [V] CEO-Bench, Chen et al. 2026. https://arxiv.org/abs/2606.18543 (d10, d11)
- [V] Huang et al. 2024, LLMs cannot self-correct yet. https://arxiv.org/abs/2310.01798 (d17)
- [V] Kamoi et al. 2024. https://arxiv.org/abs/2406.01297 (d18)
- [V] ExpeL. https://arxiv.org/abs/2308.10144 (d19)
- [V, abstract] Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (d20)
- [V] Laban et al. 2025. https://arxiv.org/abs/2505.06120 (d21)
- [V] MAST, Cemri et al. 2025. https://arxiv.org/abs/2503.13657 (d22)
- [V] arXiv search gap note. https://arxiv.org/search/?query=LLM+strategic+management+business+strategy&searchtype=all (c26)
