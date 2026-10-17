# 12. Communication and steering: how a thinking system explains itself and how a human steers it

*Prepared 2026-10-13. Grades: **A** meta-analysis or large controlled study; **B** one primary source with controls or logs; **C** vendor, secondary summary or small qualitative study; **D** my reading of the code, or inference. [n] = Sources, marked by depth read. The shared search quota ran out after 9 searches; later items were fetched by known URL.*

## Bottom line

1. **Explanations are a conditional good.** They raise acceptance of advice right or wrong [6] (B), add nothing over the bare prediction in a meta-analysis [7] (A), and cut over-reliance only where checking gets cheaper [2] (B).
2. **"Why this, not that" helps skill, not over-reliance** [1] (B). In fact-checking it protected against wrong explanations but cost accuracy when they were right [3] (B).
3. **Model prose is the weakest explanation.** Longer is more confident, not more discriminating [4]; reasoning traces name the driving cue 25 to 39% of the time [11] (B). Our selection is a script, so compute its explanation (D).
4. **Hunches pay as inputs, not overrides.** Human+AI teams lose to the best single party on decision tasks and win on creation tasks [13] (A); the gain comes from information the human has and the system lacks [12] (B).
5. **Ask rarely, at boundaries, with a choice.** Pages few and actionable [29] (C); reports need a next step and a benchmark [28] (A); summaries must be computed [24] (B).

## 1. Explanations: when they help, mislead, over-rely

| Result | Src | Grade |
|---|---|---|
| Explanations raised acceptance of AI advice, right or wrong, with no complementary gain. Meta-analysis: XAI beats nothing, not the bare prediction | [6][7] | B / A |
| Over-reliance fell only where checking got cheaper; explanation difficulty and pay also moved it (5 studies, n=731) | [2] | B |
| Contrast with the predicted human choice: skill 0.47 vs 0.39 (effect size 0.35, CI 0.11 to 0.60), accuracy equal, over-reliance unchanged, predicted vs random foil p=0.09, stronger for open-minded thinkers; one task, crowd, short term (n=628) | [1] | B |
| LLM explanation as accurate as reading passages (0.74 vs 0.73) in 1.0 vs 2.5 min, but 0.35 when wrong, below the 0.49 no-evidence baseline on the same claims; both sides shown: gap 0.52 to 0.17, minus 0.14 when right, no better than passages (n=80) | [3] | B |
| Long vs short explanations: confidence up (BF 25), no discrimination gain (AUC 0.54 vs 0.57; n=301). First-person "I'm not sure, but" cut agreement and raised accuracy; impersonal hedges did not reach significance (n=404, preregistered) | [4][5] | B |
| Forcing deliberation cut over-reliance but was rated worst (n=199); human feedback and AI questions lowered performance through load (n=108) | [8][9] | B |

Rules for the loop (D): compute, do not narrate (catalogue EVL-16 [33]); contrast against the foil the reader holds, only near the cut line; say how far to trust the line, in first person when calibration is poor; one line of evidence for and one against (evaluative AI, a position paper [10]).

## 2. Steering: where a human hunch pays

| System | Result | Grade |
|---|---|---|
| Agent Laboratory: review and free-text notes after each subtask [14] | External reviewers: co-pilot +0.58 overall (quality +0.75) but significance -0.05, contribution +0.03; co-pilots rated the tool lower (usefulness -0.55) citing trouble steering agents to their vision | B, small n |
| Magentic-UI [15] | Simulated helper on GAIA: 30.3% to 51.9% (with task side-information) or 42.6% (model only), asked in 10% and 4% of tasks. 12 users edited plans for preferences, found low-risk approvals unnecessary, wanted questions grouped | B / C |
| Cocoa, shared plan with human- or agent-owned steps [16] | Steerability up (4 vs 3, p=0.005), ease equal, output-inspection time 54.1% to 33.6% (n=16; field n=7) | B |
| Claude Code logs [17] | Agent stops: offer a choice of approaches 35%. Human interrupts: add missing context or corrections 32%. Experienced users auto-approve more (20% to 40%+) and interrupt more (5% to 9% of turns). "May not be stopping at the right moments" | C |
| CoExBO [18] | Human preferences enter Bayesian optimisation; even adversarial advice converges to the plain optimiser; every pick explained | B |

Principles (D): route the human to what the system lacks [12]; at boundaries where editing is cheap, before spend [16]; as hypotheses with bounded downside [18]; never as a veto on measured results [13]; keep ideation independent, since showing interim solutions narrowed search in a field experiment [33]; ask only when value beats cost [19], at task breakpoints (annoyance 56% below worst timing) [20].

## 3. Reports that enable action

- **Commitments buy trust in method, not novelty.** Registered Reports: 44% positive results vs 96% in a random sample of the standard literature [25] (B). 353 reviewers rated 29 RRs above 57 matched papers on rigor (+0.99) and analysis (+0.97), novelty +0.13 with a CI spanning zero [26] (B). Preregistration without a specific analysis plan did not curb p-hacking, and 60% of EEG/ERP preregistrations were followed or disclosed deviations vs 92% of RRs [27] (C, secondary).
- **Traceability is necessary, not sufficient.** Kosmos cites every statement to code or literature; scientists judged 79.4% accurate [22] (B). An independent test of an AI-scientist pipeline: 42% of experiments failed on coding errors, micro-batching flagged as novel, some numbers fabricated [23] (B).
- **Summaries overgeneralise:** 4.85x the odds of broad claims vs human summaries; asking for accuracy raised the odds (OR 1.90); newer models were worse [24] (B).
- **Feedback:** 292 trials, median +2.7% (IQR 0.0 to 8.6), pooled +6.2% (4.1 to 8.2); larger with low baseline, a specific action plan, comparison to top performers (not the average), interactive delivery; repeated delivery smaller [28] (A).

## 4. Progress, interrupts and failures

- Raw logs are not oversight: humans needed over 1.5 h to read agent transcripts and lost to LLM monitors [32] (C). Kosmos (12 h, 200 rollouts) delivers a traceable end report, not a feed [22].
- Pause at checkpoints or blockers [21] (C); interrupt "as little as possible" [15]; over- and under-asking both occur [17][15].
- Every page actionable; over-alerting made the Bigtable team miss real faults [29] (C). Burn-rate paging: 14.4x over 1 h (2% of budget), 6x over 6 h (5%), ticket at 1x over 3 days, short window one twelfth of long [30] (C). SOC analysts report alarm burnout and desensitisation (20 to 21 people) [31] (B).
- **Gap:** no controlled study found on live dashboards changing outcomes when overseeing autonomous runs, or on hunch injection in an LLM idea pipeline. Indirect: repeated feedback weakens [28]; Agent Lab users wanted better inspection of intermediate results [14].

## Where the loop stands (D)

control.json is read only at five boundaries per round (ideated, clustered, deepened, built, verified), so a fresh run's round-1 research and sketching cannot be steered; `pause` blocks indefinitely. `note` (600 characters) travels only inside loop.history_text(), empty until builds exist, so it reaches no round-1 agent and no builder. Selection stores score and rank only (ideate.select_clusters); slots go round-robin by part and direction (tree.split_select), so drops have several causes and only the near-duplicate gate logs one. REPORT.md is a funnel with no summary, glossary, decision section or deviation log; the dashboard is read-only and prints decisions as raw JSON.

## Improvement ideas for this part

**Have, keep:** controls section, prediction and fidelity counts, per-winner novelty note, lanes by yield, discovery curve, e-values, by-card and by-part tables. Cost scale: small under an hour, medium a few hours, large a day.

**I1. Selection ledger: why chosen, why dropped, against which foil. Partial** (score, rank, novelty_skip, merged_from exist).
*Mechanism:* cluster_score returns its components; split_select, _select_with_lanes, _novelty_filter and the done/exclude sets log one reason per cluster per round (picked, long-shot draw, below cut, slots exhausted, owner-excluded, near-duplicate of X, built, merged), the runner-up it lost to, and the one-term change that would flip it. Code writes selection_ledger.jsonl; REPORT.md prints "Chosen and dropped". *Effect:* choices auditable in a minute. *Cost:* medium, no model calls. *Measure:* every cluster has a reason; "why was X not built?" answered in under 2 min vs over 10 from raw JSON.

**I2. Hunch channel, typed, scoped, tested like any idea. Partial** (note, skip_nodes, exclude_clusters).
*Mechanism:* control.json gains `hunches:[{id, part, stage (ideate|select|build|verify), mode, text, expires}]`, plus a pre-run hunches.json read before the map is drawn. Modes: `seed` (an extra "owner" way in for one sketch agent in that part, others stay blind), `lane` (one bounded owner build slot per round, yield reported like the long-shot lane), `constraint` (that part's builder only), `veto` (with reason). Nothing can mark a result verified. A what-if preview re-runs selection. *Effect:* context the loop cannot have enters the right part before spend; independence kept. *Cost:* large. *Measure:* delivery log shows 100% reach; owner-lane vs main-lane checked rate by card (Fisher test after about 20 hunches).

**I3. Decision inbox with defaults. New.**
*Mechanism:* each boundary writes at most three items to inbox.json with options, a default and a deadline: close calls (within epsilon of the cut, with the foil), build-relevant questions interrogation answered "unknown", a winner awaiting promotion. The run never blocks; defaults apply at the deadline. *Effect:* attention goes where the system is least sure, once per boundary [19][15][17]. *Cost:* medium, after I1. *Measure:* answer rate; share of answers differing from the default (about 0 after 3 runs: drop that item type); wall-clock lost waiting (target 0).

**I4. Newcomer run brief at the top of REPORT.md. New.**
*Mechanism:* template filled from report.json: one-line result with best candidate and cost; "can I trust this" (controls, predictions held x of y, fidelity, noise floor, seeds); change since last run; what it needs from you; next action with cost; six-term glossary (learn z, long z, extrap z, step ratio, lane, rung). An optional model pass may reword, but every number must occur in report.json or the template ships [24][22]. *Effect:* a newcomer can act without HOW_IT_WORKS. *Cost:* small. *Measure:* five-question probe scored by someone new; number check 100%.

**I5. Tiered alerts: page, ticket, note. Partial** (collapse alarm, controls section).
*Mechanism:* four pages only. (a) A control misbehaves (placebo or known loser passes, known winner fails twice): page, auto-pause. (b) Yield burn: clusters and checked candidates per 100k tokens, paging when a stage window and the last 10 minutes both fall below a third of the run's first stage with over 20% of budget spent [30]. (c) Collapse persisting two windows. (d) First verified or stackable winner. All else is a report ticket. Each page states its action and cost; repeats suppressed; alerts unanswered for 3 runs are deleted [29]. *Effect:* few interrupts, each actionable; a runaway or a broken ladder is caught within one stage. *Cost:* medium. *Measure:* at most 3 pages per run, half followed by action; seeded faults in a mock run (passing placebo, dead stage, runaway spend) caught 100%.

**I6. Registered-report-style run record. Partial** (rules in docs and verdict.py, controls, novelty note, e-BH: have).
*Mechanism:* at start write commitments.json (rules, margin, alpha, seeds, baseline hash, weights and whether calibrated, slots, model) and hash it into state.json; log every control.json edit to control_log.jsonl; REPORT.md prints commitments, deviations, candidates tested and the e-BH level, and per winner a reproduction card (script hash, seeds, command), diff, closest known technique with URL, near misses and what would falsify it [25][26][27]. *Effect:* a reader can trust the method and repeat the result, and novelty claims stay modest. *Cost:* small to medium. *Measure:* a second person reproduces one winner from the card alone; report.json equals a recomputation.

**I7. Dashboard from monitor to control surface. Partial** (rich read-only panels).
*Mechanism:* POST /api/control (atomic write, localhost) for hunches, inbox answers and pause; a top strip answering healthy / needs me / changed in the last hour; call table and idea map collapsed; ledger links replace raw JSON; each candidate shown against the best known winner, not the run average [28][16]. *Effect:* steering and reading in one place; fewer glances, more decisions. *Cost:* medium. *Measure:* logged opens and expands; time on probe questions; share of sessions followed by a control action within 10 minutes.

**I8. Explanation audit and stated reliability. Partial** (near-duplicate audit, calibrate.py).
*Mechanism:* each ledger line carries the AUC of score against ladder outcome once 100 builds exist, in first-person wording when weak [5][4]; build a random tenth of below-cut clusters anyway, as the novelty gate does. *Effect:* the ledger cannot become a confident wrong explanation [3]. *Cost:* small after I1. *Measure:* audited-drop vs chosen pass rate at rung 3; a gap near zero means the score explains little, and the line says so.

**Testing all of it:** a six-question probe battery (best candidate and trust, why X was not built, what it needs from me, cost, which control failed, next step) answered from artifacts by a newcomer, old report against new, scoring correctness and minutes.

## Sources

Explanations
1. Bucinca et al. 2025, contrastive explanations: https://arxiv.org/abs/2410.04253 (full)
2. Vasconcelos et al. 2023, explanations can reduce over-reliance: https://arxiv.org/abs/2212.06823 (full)
3. Si et al. 2024, LLM explanations in fact-checking: https://arxiv.org/abs/2310.12558 (full)
4. Steyvers et al. 2025, LLM calibration gap: https://arxiv.org/abs/2401.13835 (full)
5. Kim et al. 2024, "I'm not sure, but...": https://arxiv.org/abs/2405.00623 (abstract)
6. Bansal et al. 2021, does the whole exceed its parts: https://arxiv.org/abs/2006.14779 (abstract)
7. Schemmer et al. 2022, meta-analysis of XAI utility: https://arxiv.org/abs/2205.05126 (abstract)
8. Bucinca et al. 2021, cognitive forcing functions: https://arxiv.org/abs/2102.09692 (abstract)
9. Chen, Luo, Sra 2025, interface design: https://arxiv.org/abs/2501.16627 (abstract)
10. Miller 2023, evaluative AI: https://arxiv.org/abs/2302.12389 (abstract)
11. Anthropic 2025, chain-of-thought faithfulness: https://www.anthropic.com/research/reasoning-models-dont-say-think (page)

Steering
12. Hemmer et al. 2024, complementarity: https://arxiv.org/abs/2404.00029 (abstract)
13. Vaccaro, Almaatouq, Malone 2024, when human+AI combinations are useful: https://doi.org/10.1038/s41562-024-02024-1 (numbers via summary https://mitsloan.mit.edu/ideas-made-to-matter/when-humans-and-ai-work-best-together-and-when-each-better-alone)
14. Schmidgall et al. 2025, Agent Laboratory: https://arxiv.org/abs/2501.04227 (full)
15. Mozannar et al. 2025, Magentic-UI: https://arxiv.org/abs/2507.22358 (full, first two thirds)
16. Feng et al. 2026, Cocoa: https://arxiv.org/abs/2412.10999 (full, first half)
17. Anthropic 2026, measuring AI agent autonomy: https://www.anthropic.com/research/measuring-agent-autonomy (page)
18. Adachi et al. 2024, CoExBO: https://arxiv.org/abs/2310.17273 (abstract)
19. Horvitz 1999, mixed-initiative principles: https://erichorvitz.com/chi99horvitz.pdf (full)
20. Adamczyk and Bailey 2004, if not now, when: http://interruptions.net/literature/Adamczyk-CHI04-p271-adamczyk.pdf (full)
21. Anthropic 2024, building effective agents: https://www.anthropic.com/engineering/building-effective-agents (page)

Reporting
22. Mitchener et al. 2025, Kosmos: https://arxiv.org/abs/2511.02824 (abstract)
23. Beel, Kan, Baumgart 2025, evaluating Sakana's AI Scientist: https://arxiv.org/abs/2502.14297 (abstract)
24. Peters and Chin-Yee 2025, generalisation bias in LLM summaries: https://pmc.ncbi.nlm.nih.gov/articles/PMC12042776/ (full)
25. Scheel, Schijen, Lakens 2021, excess of positive results: https://osf.io/preprints/psyarxiv/p6e9c (abstract via OSF API)
26. Soderberg et al. 2021, quality of registered reports: https://osf.io/preprints/metaarxiv/7x9vy (abstract via OSF API)
27. Preregistration (science): https://en.wikipedia.org/wiki/Preregistration_(science) (secondary; cites van den Akker 2023)
28. Ivers et al. 2026, Cochrane audit and feedback: https://www.cochrane.org/CD000259/EPOC_audit-and-feedback-effects-on-professional-practice-and-healthcare-outcomes (summary page)

Failures
29. Google SRE book ch. 6: https://sre.google/sre-book/monitoring-distributed-systems/ (full)
30. Google SRE workbook, alerting on SLOs: https://sre.google/workbook/alerting-on-slos/ (page)
31. Alahmadi et al. 2022, SOC analysts and alarms: https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi (abstract)
32. Anthropic 2025, SHADE-Arena: https://www.anthropic.com/research/shade-arena-sabotage-monitoring (page)
33. Local: research_notes/mechanism_catalog.md (EVL-16); idea_generation/07_collective_intelligence.md; nano/ code; docs/HOW_IT_WORKS.md
