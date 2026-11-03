# Scenario planning (Shell method): deep document

*Written 2026-11-03 from evidence_a-d.jsonl (a01-a34, b01-b25, c01-c26, d01-d16), claims.jsonl (K01-K20) and critique.md. Honest summary first: the human base is thin and second-hand, and no study tests the Shell funnel on an LLM. Most LLM numbers are about forecasting or ranking, not scenario construction.*

## 1. What it is

Scenario planning is a way to decide under uncertainty that cannot be reduced to a probability. Instead of one forecast, you build a few distinct, plausible stories about the future. Then you test plans against each story. The aim is to change the planner's mental model, not to predict.

The Shell six-step recipe, as given on Wikipedia (a01):

1. Name the drivers and assumptions.
2. Build a framework (which drivers matter most and are most uncertain).
3. Draft 7 to 9 mini-scenarios.
4. Cut them to 2 or 3.
5. Draft those in full.
6. Identify the issues they raise for decisions.

Three traits set it apart from other tools (Schoemaker 1993, a25): a script or narrative form; uncertainty spread across several models of the world rather than inside one; and splitting a complex future into discrete states.

Why it is in our study: the funnel shape (widen to many framings, cut by a rule, draft few in full, test decisions against them) is a candidate form for operator O8 (reframe the goal) and for open mode.

Caution on provenance. The "7 to 9 cut to 2 or 3" step could not be found in the readable parts of Wack's 1985 HBR articles (d02, d03; K19). It may be later practitioner tidy-up. Treat the funnel as our own design that borrows Shell's name, not as a proven Shell recipe.

## 2. History and theories in depth

**Kahn and RAND (1950s-60s).** Herman Kahn applied game theory to nuclear war at RAND and wrote stories of the future "as if told by people living in it" (a01, a06). He founded the Hudson Institute in 1961. His escalation ladder grew from 16 steps (1962) to 44 (1965). Books: On Thermonuclear War (1960, 14,000 copies in two months), On Escalation (1965), The Year 2000 (1967, with Wiener). This is the military and policy root. In France, Berger built La Prospective (a01).

**Wack and Shell (1971-73).** Pierre Wack (1922-1997) headed the business environment division of Shell's planning department. With Edward Newland he built the Shell system (a03, a05). Before this, Shell used the Unified Planning Machinery (UPM), a computer cash-flow planner introduced in 1965 with a six-year horizon. Commitments ran past that horizon and even near-term forecasts failed. Shell closed it in the early 1970s (a04, d04). Wack writes that forecasting worked reasonably in the stable 1950s-60s and that errors became frequent after the early 1970s (d02). The 1973 oil shock gave the method force (a01). Wikipedia says Shell "anticipated" two Arab-induced shocks (a05); no measured outcome stands behind that, and hindsight risk is high (d05).

Polyscene (2026) gives a simplified retelling of Shell's 1972 exercise (a11): two drivers (does the cartel stay coordinated; does the region stay peaceful) give four outcomes. Shell examined two families: disruption (war, embargo) and continuity (cartel decays, peace, growth). The conventional "surprise-free" case, a united cartel in a peaceful region, was the one the exercise was meant to challenge. The authors say this is their simplification, not Shell's own scenarios.

**Spread into practice.** Diffenbach (1983, via Wikipedia, a01/b20): alternate scenarios were the third most used long-range technique, used by 68% of large organisations. Wack taught it at Harvard Business School in 1983-84 (a03). Schwartz and Schoemaker (1991-95) made it a consulting method.

**Sister methods.**
- Cross-impact analysis (Gordon and Helmer 1966, a07): list 10 to 40 events, give each a probability, estimate a conditional probability per pair, check by simulation, run to get scenarios. SMIC 1974, Delphi plus cross-impact 1984. Can produce impossible probabilities from negative impacts.
- Morphological analysis (Zwicky, a08): list dimensions, list options per dimension, delete combinations that cannot coexist (cross-consistency). A box of 6 dimensions with 4 options each has 4^6 = 4,096 cells.
- Automation lines (a13): consistency-based combination (cross-impact balance, computer-aided morphological analysis), speed-ups of the manual workshop (fuzzy cognitive maps), planning-based generation (IBM Scenario Planning Advisor, Sohrabi 2018), and LLM drafting.

**Psychological theory of why it works (and fails).**
- Schoemaker 1993 (b01, abstract level): scenarios use one bias (the conjunction fallacy: richer stories feel more probable) to offset another (overconfidence). Four experiments: two on confidence ranges, two on belief coherence.
- Healey and Hodgkinson 2009, 2024 (a28, b04, b05): unskilful use anchors and confines thinking; building scenarios can add bias; confidence may shift unevenly (misplaced optimism or threat rigidity); negative emotion can override cognitive gains.
- Goodwin and Wright 2001 (a29, d01): scenario planning avoids subjective probabilities, but the step that evaluates strategies across scenarios is underdeveloped. Informal evaluation can pick inferior strategies. They propose decision analysis (score each strategy under each scenario).
- Audit inside Shell, early 1980s (de Geus, via Wikipedia, a02): decision making after the scenarios, not the scenarios, was the main cause of weak implementation.
- Self-defeating forecasts, and Schwartz's warning that assigning probabilities makes people fixate on the likeliest scenario (a02).

**Critique.** The method is called subjective and untested; evidence is anecdotal and mostly from Shell (a01, a02). Decades-long timescales make proof hard. A counter-attempt is the "black box" paper (2020, b10, not opened). A review of reviews (Cordova-Pozo and Rouwette 2023, 173 citations, b09/d08, not opened) is cited by Polyscene as showing mixed evidence on debiasing (a14).

## 3. Core findings with exact numbers

Status key: E established (2+ independent sources or directly read), S single source, C contested, U unverified.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Business scenario use is widespread | 68% of large organisations used alternate scenarios (1983 survey; third most used long-range tool) | Diffenbach 1983 via Wikipedia (a01) | S, second-hand |
| No controlled effect size on firm performance obtained | None found; Phelps 2001 (171 cites), Meissner and Wulf 2013 (124 cites), Cordova-Pozo 2023 (173 cites) exist but unread | b08, d07, d08, K01 | E that evidence is thin; effect size unknown |
| Scenarios and confidence: lab vs field | Lab (Schoemaker 1993): overconfidence offset. Field (Phadnis 2015, 3 field experiments): no aggregate change in confidence; judgment moved with how an investment fared in the scenario used; experts preferred more flexible options. N and effects not read | a25, a26, b01, b02 | C |
| Rich narratives raise felt probability | 65% chose GRGRRR over RGRRR; experts 1981: joint Poland event 4% vs 1% single; counts format cut errors from 85% to about 20% | Tversky and Kahneman 1983, Gigerenzer 1991 via Wikipedia (a09) | E |
| Strategy evaluation after scenarios is the weak step | Qualitative; de Geus audit; Goodwin and Wright 2001; Hodgkinson and Wright 2002 (one top team, largely failed) | a02, a27, a29, d01 | E (qualitative) |
| LLM beats humans at ranking live ventures | Spearman with outcome: Gemini 2.5 Pro 0.74; GPT-5 family 0.67-0.71; best human 0.45; other expert 0.04; Prolific crowd 0.19. 30 projects, 870 pairwise comparisons per model, 346 managers plus 3 MBA investors. Gemini minus best human 0.29, p=0.063 (significant only at 90%) | Csaszar, Peterson, Wilde 2026 (a18, b11) | S |
| Same, preregistered replication | 26 projects; model rank correlation between the two samples 0.54 over 19 models; lower absolute correlations. Same team, not independent | a20 | S |
| Averaging and human+LLM teams did not beat best model | Best human + Gemini 0.67 vs Gemini 0.74; Gemini + GPT-5 Mini 0.77 (+0.03, n.s.). Crowd captured 85% of oracle value for portfolios of about 5 picks | a19, b12 (b12 misstates the 0.71, see critique) | S |
| LLM plans rated slightly above entrepreneurs | 250 investors, 10 plans: +0.14 SD (p<0.001); +5 points "accept" (p=0.003); rejected plans +7 points accept | Csaszar et al. 2024 (a16) | S |
| LLM rubric scores agree with investor judges | 138 plans, 541 evaluations, mean r = 0.52, about the level of judge-judge agreement | a17 | S |
| LLM forecasting near the crowd, below superforecasters | Brier (lower better): random 0.250; best plain model 0.208; Halawi system 0.179 vs crowd 0.149 (accuracy 71.5% vs 77.0%); Soru pipeline 0.186 vs GPT-4o 0.236 vs superforecasters 0.150 (150 forecasts, test 72); ForecastBench superforecasters 0.096, public 0.121, best LLM without crowd info 0.136 | b18, c07, c08, c10 | E (4 sources) |
| 12-LLM ensemble equals a human crowd | 12 models vs 925 humans, 31 questions, equivalent within medium-effect bounds; acquiescence bias (mean forecast above 50%) | Schoenegger et al. 2024 (b19, c11) | S |
| Human median shown to model helps; LLM helps humans | Median exposure raised accuracy 17-28%; 991 participants with an LLM assistant forecast 24-28% better (41% / 29% without one outlier item), even with an overconfident assistant | b19, c12 | S each |
| System + crowd average best | Beat either alone in every setting (Halawi) | b18, c08 | S |
| Plain prompting near chance | Only GPT-4 and Claude-2 series beat 0.25 by more than 0.02 among 14 LMs | c09 | S |
| LLM open output is homogeneous | NoveltyBench: many models under 3 distinct answers in 10 queries (20 models). Infinity-Chat: same-prompt similarity usually above 0.8; min-p: 81% of pairs above 0.7, 61.2% above 0.8; cross-model 71-82%. LLM Delphi: top themes identical in 12 of 12 experiments | c18, c19, c03 | E |
| LLM-assisted workshops: more scenarios, not wider range | 10 workshops, about 250 professionals, 170 drafts; 80% mention technology, 61% techno-optimistic | Ferrer i Pico et al. 2026 (b15, abstract only) | S |
| Models sense incoherence internally but rate it poorly | Probes 80%+, best 0.958 (Qwen2.5-72B); written coherence-rating accuracy 0.52-0.77; mean gap 1.66 points of 7, four of six models under 1 point; 25 incoherent stories | de Langis et al. 2025 (b16) | S |
| A targeted contrast step beat a generic balance prompt (wargame) | Escalation 6.37 baseline; de-escalation reflection 2.76 (-57%); planning reflection 4.61 (-28%); temp 0.5: 3.96 (-38%); temp 0.01: 3.33 (-48%); 50-word context only -8%. Mistral-7B, 10 runs per arm, p<0.05 | Elbaum and Panter 2025 (b17, b24) | S |
| Symbolic diversity planner: scenario count grows with budget | Conflicts board outcomes 5, 8, 9, 11 at budgets 4, 5, 6, 7; budget 5 run 8.4 s; 3 wars by 2026 each end a scenario; none of the 10 pairs left at peace fought; Suez set misses Jan 2024 production stops | Polyscene 2026 (a10, a12, b13) | S |
| Small RL model matches big ones on plausible future news | 48.90% vs DeepSeek-V3-671B 48.81% vs base 47.66%; event timing 0.7780 vs 0.7503; gaps under 2 points, no variance reported | Time-R1 2025 (a21, a22, c13) | S, doubtful |
| Scenario-planning finance items show an expert gap | 246 test items, 88.6% calculation; o1-preview 60.1, claude-3.5-sonnet 47.2, gpt-4o 46.3, Llama-3.1-8B 22.3; experts 75.8 | XFinBench 2025 (c05) | S, name overlap only |
| Practice pilots: speed and cost | State pilot: 8 vs 4 scenarios, cost down about 60%, staff hours down 60-70%; GPT-4 Time Machine: discussion on 70%+ of scenarios, 222 participants; architecture scenarios 10-15% over-engineered, coverage 80-100% | c02, a30, a31 | S, no quality test |
| No controlled test of LLM + Shell six-step | arXiv searches (40 and 7 hits) found none | b21, c24, K05 | S (absence, partial) |

## 4. Mechanisms and models

Each mechanism is stated so it can be coded. Tags: [H] measured on humans, [L] measured on LLMs, [D] design inference only.

**4.1 The funnel (widen, cut, draft, test).** [D] for LLMs.
1. Name 4 to 8 drivers (things that shape the outcome) and the assumptions held fixed.
2. Rate each driver for importance and uncertainty. Pick the two highest on both (Wack's two-axis framework). Two axes with two poles each give 4 cells.
3. Generate 7 to 9 one-line mini-scenarios across the cells.
4. Cut to 2 or 3 by a rule applied in code (4.3).
5. Draft each survivor in full: a causal path from the present to the end state.
6. List the decision issues each raises (a robustness table, 4.5).

**4.2 Scenario = plan, set = diversity.** [L, symbolic] Polyscene (a10): a scenario is a plan from a stated present state. Two scenarios differ if they end in different values on the chosen drivers. Five criteria are coded as trajectory constraints (LTLf/PDDL3 in clingo): plausible (each step uses a legal event schema), internally consistent, relevant (touches drivers), challenging (departs from the surprise-free path), differentiated (the set differs on outcomes). The engine returns one scenario per reachable outcome within a cost budget. No probabilities, no ranking. Implementation cue for us: keep a typed event list and a small driver-state vector, make "different end state" a code check, and let budget (number of event steps) be the cost knob. Limits: factorial growth with budget (many narratives differ only in event order), unmodelled events never appear, one analyst-written model.

**4.3 Cut rules for 7-9 to 2-3.** [D] No head-to-head exists (d11). Three candidates:
- Wack axes: keep the scenarios in the cells of the two most important, most uncertain drivers.
- Maximum distance: greedy farthest-point selection on embeddings (the Time-R1 pipeline uses a greedy diversity filter, a21). Code does it, so G5 holds.
- Model self-ranking: risky. Same-prompt similarity above 0.8 (c19) means near-duplicates may survive, and G5/G8 bar a model as final selector.

**4.4 Diversity forcing.** [L] Plain sampling yields few distinct answers (c18, c19, c03). NoveltyBench found in-context regeneration (showing earlier outputs) roughly matched humans, while paraphrasing and system prompts only marginally helped (c18). So: show prior drafts when asking for the next one, assign named drivers or opposite-sign poles per slot, and check distinctness in code by embedding clusters. Persona sampling inside one model keeps the base-model bias (c04); G4 already says personas are not independent.

**4.5 Robustness table.** [H, conceptual] Rows are candidate actions, columns are surviving scenarios, cells are scored outcomes. Goodwin and Wright (d01) propose decision analysis for exactly this. Pick by worst case, regret, or flexibility; Phadnis found experts moved toward more flexible options after scenarios (a26). For an LLM, cell scores need an external check or a second sample, since written ratings are weak (b16, d12).

**4.6 Contrast step.** [L, one study] A targeted prompt telling the model to think privately about the opposite course (de-escalation) beat a generic balance prompt (b17, b24). Mechanism guess: it supplies a specific counter-trajectory instead of an unspecific instruction to be careful. Not isolated.

**4.7 Consistency check.** [L] Models carry an internal incoherence signal (probes 80%+) but do not report it in ratings (b16). Options: external constraints listed as data and checked in a second pass; a cross-consistency matrix from morphological analysis (a08); cross-impact (a07). Not tested at equal tokens.

**4.8 Probability handling.** [H] Schwartz warns that attaching probabilities makes people fixate on the likeliest story (a02). The conjunction effect says detail inflates felt probability (a09). The counts format ("out of 100") cut conjunction errors from 85% to about 20% (a09). Code should normalise probabilities over mutually exclusive scenarios (G5; Soru checked exclusive events sum to 100% or less, c07).

**4.9 Draft-then-adjust.** [L/H] Models improved when shown the human median (17-28%, b19); humans improved with an assistant (24-28%, c12); system-plus-crowd average beat either (c08). Pattern: a second view arriving after an initial draft helps. Counter: Csaszar found no gain from averaging (a19). Task and aggregator differ.

## 5. What holds up

**Replications and failures.**
- Confidence effect: the one direct conflict. Lab work (Schoemaker 1993; Kuhn and Sniezek 1996, b03) against a field null (Phadnis 2015, 3 field experiments). Moderator named: prior confidence. Sample sizes and effects were not read. Status C.
- Csaszar 2026: a preregistered second sample gave a similar pattern with lower correlations (26 projects); model-rank stability only 0.54 over 19 models (a20). Same team. The headline p=0.063 does not pass 5%.
- Hodgkinson and Wright 2002: a published failed top-team intervention, noting that failures are rarely published (a27). Single case, authors were the facilitators.
- Time-R1: the gap of 0.09 points over DeepSeek-V3 is far below plausible noise; "consistent gains" overreaches (critique item 8).
- No other replication or meta-analysis was reached. The 2023 review of reviews and the 2020 "black box" paper are unopened.

**Moderators and boundary conditions.**
- Driver model: scenario sets depend on it; unmodelled events never appear (a12, b23).
- Search budget: a small budget misses outcomes needing longer chains (5 to 11 outcomes across budgets 4 to 7).
- Prior confidence moderates human judgment shifts (a26).
- Crowd certainty: Halawi's system beats the crowd when the crowd is unsure (Brier 0.199 vs 0.246 for crowd between 0.3 and 0.7; 22% of forecasts), loses when the crowd is certain, is worse near resolution, and hedging near 0.5 cost 0.04 Brier even with 7% higher accuracy (c08, c22).
- Fluent output is over-trusted unless the design forces users to contest it (Girona, b15).
- Technology theme in 80% of LLM drafts (b15).

**Interventions that worked.**
- Targeted contrast prompt (-57% vs -28% generic) in a small-model wargame (b17).
- Lower temperature (-48% at 0.01) in the same game. This says some "effect" is just reduced variance (b17).
- Retrieval, prompt selection and ensembling to get near-crowd forecasts (b18).
- Pipeline with probability weighting and exclusivity checks (Brier 0.186 vs 0.236; c07).
- Showing earlier outputs for diversity (c18).
- Decision analysis after scenarios (proposed, not tested; d01).

**Interventions that did not work.**
- Generic risk-balance prompt (only -28%, b17); a 50-word context (-8%).
- Persona sampling inside one model (c03, c04).
- Paraphrase and system-prompt variation for diversity (c18).
- Averaging and human+LLM teams on Csaszar's ranking task (a19).
- Reasoning models did not fix coherence rating (b16).
- Retrieved knowledge on XFinBench future items (little help, even negative for GPT-4o; c06).

**Net.** The human evidence for the funnel's benefit is anecdotal and mixed (K01, E). The robust parts are the failure modes: detail inflates felt probability (E), the evaluation step is weak (E), LLM output is homogeneous (E).

## 6. Language models

**There is no direct test of the Shell six-step on an LLM** (K05, b21, c24). What exists, by kind:

*Judgment of futures (not scenario building).*
- Ranking live ventures: frontier models 0.67-0.74 Spearman vs best human 0.45 and crowd 0.19 (a18). Small N, narrow proxy. Model rank stability across samples 0.54 (a20). LLM plan ratings: +0.14 SD over entrepreneurs' plans (a16); LLM rubric scores correlate 0.52 with judges (a17).
- Forecasting: plain models near chance; best plain 0.208 Brier; scaffolded systems 0.179-0.186; crowd 0.149; superforecasters 0.096-0.150 (b18, c07, c10). ForecastBench projects parity with superforecasters near Arena score 1406 (CI 1346-1633) or 6.49e26 FLOP, from about 10 models, p=0.046 (c10). Models given the crowd value did best (c10, c23).
- What changed the numbers: retrieval plus prompt selection plus ensembling (about -0.03 Brier vs best plain, b18); logprob-weighted pipeline (-0.05 vs vanilla, c07); human median shown (+17-28% accuracy, b19).

*Scenario generation.*
- Single-prompt illustration: GPT-4 gave three scenarios for business schools, and repeats appeared after many scenarios (a15).
- LLM Delphi: same top themes in 12 of 12 experiments, one small model, no accuracy test (c03).
- Girona: more scenarios, not wider range; 80% tech, 61% techno-optimistic; over-trust in fluent output (b15).
- Time-R1: embedding similarity to later news; all models within a 2-point band (a21).
- Pilots: 8 vs 4 scenarios, cost -60%, hours -60-70% (c02); no quality test.
- Architecture preprint: coverage 80-100%, over-engineering 10-15%, expert score 7-8 of 10 (a31).
- Diversity ceiling: NoveltyBench under 3 distinct in 10 for many models, with bigger models often less diverse; Infinity-Chat similarity above 0.8 (c18, c19).

*Consistency.* Written coherence ratings 0.52-0.77 accuracy vs internal probes 80%+ (b16). LLM drafts "often fail to stay consistent" (Polyscene claim, relayed, a14).

*Simulation and contrast.* Mistral-7B wargame: contrast prompt -57% (b17). Generative agents: memory, planning and reflection each raised believability (TrueSkill 29.89 full vs 21.21 ablated; crowdworkers 22.95; c16). This measures believability, not forecast skill.

*Long-horizon planning.* EcoGym: no model leads across three business sims; weak at strategy or at execution (c25, snippet only). XFinBench scenario-planning items: o1-preview 60.1 vs experts 75.8 (c05).

*Other.* SPARC (2602.16671), a four-stage scenario pipeline for C unit tests, claims gains over vanilla on 59 subjects (listing only, c24).

**Reading across.** Scaffolds help forecasting modestly. Plain prompting does not give scenario diversity. Nothing yet shows that scenario structure itself improves accuracy or decisions for an LLM. Whether the effects hold on Claude-class models is not measured in the scenario-specific studies (d13).

## 7. What our agent should take

Schema labels: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

Almost nothing here is new to SCHEMA.md; these are confirmations and cautions.

1. **Do not add the Shell funnel on the strength of Shell.** [E] The human evidence is anecdotal, no effect size exists, and there is no LLM test. Keeps G7 (must pay for itself at equal tokens). Evidence: K01, K05, a01, a02, b21.
2. **Count distinct framings in code.** [E] When any step asks the model for several alternatives (O6, O8, open mode), measure distinctness by embedding clusters and drop near-duplicates; do not ask the model whether they differ. Fits G4, G5, G8. Evidence: K09, c18, c19, c03, c04.
3. **Do not use rich narratives as evidence for probability.** [E] Detail inflates felt probability. Keep any probability over mutually exclusive branches normalised in code (G5) and keep the narrative out of the selector's view. Evidence: K03, a09, a25, a28.
4. **If a decision follows scenarios, never pick by narrative appeal.** [E, qualitative] Evaluation after scenarios was the weak step in practice. Schema part: S and O8. Evidence: K04, a02, a27, a29, d01. The extra robustness step itself waits for the test in section 8 (T4).
5. **Do not trust model self-rated coherence for gating.** [S, consistent with G2, G10] Evidence: K12, b16. Use code checks on listed constraints.

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Six-step funnel as O8 (reframe) vs plain prompt and best-of-N | O8 | [S] design only, benefit [C] | K05, K19, K20, a01, d11 |
| Cut rule: Wack axes vs max-distance (code) vs self-rank | O8, G5 | [C] none measured | d11, a10, a21 |
| Diversity forcing: prior drafts shown, named drivers, opposite-sign seeds | O8, open mode | [S] | c18, c03, b15, K09 |
| Robustness table (action x scenario), cells checked by second sample or code | S, O8 | [C] | d01, d12, b16, K04 |
| Targeted contrast step vs generic balance prompt | O8 | [S] one 7B model | b17, b24, K11 |
| External consistency check on drafted scenarios | G, memory (constraint list) | [S] | b16, a10, K12 |
| Scenario step effect on calibration (Brier before and after 2-3 scenarios) | S, O8 | [C] | a25, a26, K02 |
| Forced non-technology / opposite-sign driver to widen range | O8 | [S] | b15, K10 |
| Pairwise ranking of candidate framings as cheap scorer (outcome-known items only) | G5, O8 | [S] | a18, a20, K06 |
| Draft-then-adjust with a counter-draft | O8 | [S] | b19, c12, K17, K08 |

## 8. Concrete tests on our bench

All arms at equal total tokens, same items, same seeds, setup cost counted (G7). Report effect size with a bootstrap interval, not only a mean. Items come from the bench: ARC and BRAINTEASER items, open-mode items scored by embedding spread and a blind rubric, and resolved-question sets for calibration.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Impasse items on ARC and BRAINTEASER where the first attempt fails | (a) plain retry, (b) best-of-N, (c) six-step funnel (9 mini-framings, cut to 3 by code, draft, test), (d) plain two-framing prompt | Solve rate at impasse; tokens | Small or null on single-answer items (LLM reframing null in one large test, SCHEMA O8). Funnel at most equals best-of-N. Run to confirm the null. |
| T2 | Open-mode ideation items | Funnel with max-distance cut vs Wack-axes cut vs self-rank cut vs plain sampling | Embedding clusters among the 3 survivors; blind rubric on usefulness | Max-distance and Wack axes beat self-rank; self-rank keeps near-duplicates (similarity above 0.8). |
| T3 | Request for 7-9 mini-scenarios | Plain sampling vs show-prior-drafts vs named drivers vs opposite-sign seeds | Distinct clusters out of 7-9; share mentioning technology | Prior-draft display and named drivers raise the distinct count; opposite-sign seeds cut the technology share. |
| T4 | Decision items with a known-best action | Choose after scenarios by narrative vs robustness table vs table with second-sample cells | Pick of best action; regret | Table beats narrative pick; second-sample cells beat single-sample cells given weak self-ratings. |
| T5 | Resolved forecast questions (post-cutoff) | Plain probability vs probability after writing 2-3 contrasting scenarios vs same plus code-normalised exclusive probabilities | Brier; calibration slope | Unknown. Human lab and field conflict. Expect small gain from normalisation, null or slightly worse from scenarios alone. |
| T6 | Same as T5, forced contrast | Generic "consider risks" vs targeted "opposite future" step, temperature held fixed | Brier; share of changed answers that were wrong at first | Targeted beats generic only if the wargame effect is not just variance reduction. |
| T7 | Scenario drafts with seeded contradictions | Model self-rating vs second-pass listed constraints vs code constraint check | Contradictions caught; false alarms | External check beats self-rating (rating accuracy 0.52-0.77). |
| T8 | Candidate framings with known downstream outcome | Pairwise rank by model vs random vs code heuristic | Spearman with outcome | Pairwise rank above random; still not the final selector (G8). |
| T9 | Items from T1 and T5 | Draft then adjust after a counter-draft vs single draft vs average of two drafts | Accuracy or Brier | Small gain from counter-draft; averaging same-model drafts no better than one (G4). |

Run T3 and T2 first (cheap, measurable in code). T1 is the gate: if the funnel does not beat best-of-N at equal tokens on T1 and T2, it stays out of O8.

## 9. What does not transfer, and why

- **Workshop social function.** Shell's gain was claimed to come from changing executives' mental models through conversation. An LLM has no persistent mental model to change between runs. The learning mechanism does not transfer; only the structure might.
- **Decades-long horizons and no ground truth.** Our bench has checkable answers. Scenarios are not predictions, so scoring them by accuracy misses their stated purpose; the bench can only score by outcome or by spread.
- **Human biases as the target.** Scenarios counter overconfidence and tunnel vision in people. LLM biases differ (acquiescence, homogeneity, tech optimism). The same step may not fix them.
- **Probabilities avoided on purpose.** Shell avoids probabilities. Our guardrails need explicit probabilities over exclusive options (G5). Resolve by keeping probability use in code.
- **Narrative quality.** LLMs write fluent stories. Fluency is the hazard (conjunction effect, over-trust in b15), not the goal.
- **Forecasting results.** Brier and ranking studies measure judgment of known categories, not scenario building. Csaszar's Kickstarter ranking is not strategic reframing.
- **Small-model findings.** The wargame (Mistral-7B, 10 runs) and the LLM Delphi (gpt-4o-mini) may not hold for stronger models.
- **XFinBench "scenario planning".** Name overlap only; it is financial calculation (88.6%), not the Shell method.
- **Park et al. generative agents.** Believability scores, not scenario quality.
- **Polyscene.** A symbolic engine over a hand-built model. It transfers as design (diversity by end state, budget knob), not as a drop-in, since our tasks lack a domain model.

## 10. Open questions

1. Does the six-step funnel beat plain and best-of-N at equal tokens on any item class? (Own experiment; the main gap.)
2. Which cut rule works for an LLM (Wack axes, max-distance, self-rank)?
3. How many truly distinct mini-scenarios can an LLM produce, and which forcing lifts it most?
4. Do scenarios change LLM calibration the way Schoemaker (offset overconfidence) or Phadnis (no change) report for people?
5. What is the effect size of scenario planning on firm or decision outcomes in primary studies (Phelps 2001, Meissner and Wulf 2013, Cordova-Pozo and Rouwette 2023)? Full texts not read.
6. Which steps of the six-step recipe are Wack's and which are later tidy-up (Wack 1985 full text, Wilkinson and Kupers 2013, Chermack 2017)?
7. Does an LLM-built robustness table fix the post-scenario decision weakness, or reproduce narrative bias?
8. Can an external symbolic check beat model self-rating for scenario consistency at equal tokens?
9. Does the technology-optimism bias survive forced opposite-sign drivers, and does it appear in Claude-class models?
10. Does a targeted contrast step beat a generic one beyond wargames and beyond a 7B model, and is its gain more than variance reduction?
11. Is the rank stability across model samples (0.54) a property of the task or of 26-30 items?
12. Is the Time-R1 gap (0.09 points) real at all?

## 11. Sources

[V] = opened by an earlier agent or the cross-checker (page or PDF text read). [M] = snippet, record or abstract only. Some [V] items were only landing-page intros; limits are in the evidence files.

- [V] Wikipedia, Scenario planning. https://en.wikipedia.org/wiki/Scenario_planning (a01, a02)
- [V] Wikipedia, Pierre Wack. https://en.wikipedia.org/wiki/Pierre_Wack (a05, d05)
- [V] Wikipedia, Herman Kahn. https://en.wikipedia.org/wiki/Herman_Kahn (a06)
- [V] Wikipedia, Cross-impact analysis. https://en.wikipedia.org/wiki/Cross-impact_analysis (a07)
- [V] Wikipedia, Morphological analysis. https://en.wikipedia.org/wiki/Morphological_analysis_(problem-solving) (a08)
- [V] Wikipedia, Conjunction fallacy. https://en.wikipedia.org/wiki/Conjunction_fallacy (a09)
- [V, intro only] Wack 1985, Scenarios: Uncharted waters ahead. https://hbr.org/1985/09/scenarios-uncharted-waters-ahead (a03, d02)
- [V, intro only] Wack 1985, Scenarios: Shooting the rapids. https://hbr.org/1985/11/scenarios-shooting-the-rapids (d03)
- [V, intro only] Wilkinson and Kupers 2013, Living in the futures. https://hbr.org/2013/05/living-in-the-futures (a04, d04)
- [V] Abdelwahed, Espasa, Meneguzzi 2026, Polyscene. https://arxiv.org/abs/2610.28102 and https://arxiv.org/pdf/2610.28102 (a10-a14, b13, b14, b23)
- [V] Csaszar, Ketkar, Kim 2024, AI and strategic decision-making. https://arxiv.org/abs/2408.08811 (a15-a17)
- [V] Csaszar, Peterson, Wilde 2026, Strategic foresight of LLMs. https://arxiv.org/abs/2602.01684 (a18-a20, b11, b12)
- [V] Time-R1, arXiv 2505.13508. https://arxiv.org/abs/2505.13508 (a21, a22, c13, c14; author attribution inconsistent between lines)
- [V] Bertolotti and Mari 2025, LLM-based Delphi. https://arxiv.org/abs/2502.21092 (a23, a24, c03, c04)
- [V] de Langis et al. 2025, Mary, the cheeseburger-eating vegetarian. https://arxiv.org/abs/2512.07777 (b16)
- [V] Elbaum and Panter 2025, Managing escalation. https://arxiv.org/abs/2508.01056 (b17, b24)
- [V] Halawi et al. 2024, Approaching human-level forecasting. https://arxiv.org/abs/2402.18563 (b18, c08, c09, c22)
- [V] Schoenegger et al. 2024, Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379 (b19, b25, c11, c20)
- [V, abstract page] Schoenegger et al. 2024, AI-augmented predictions. https://arxiv.org/abs/2402.07862 (c12)
- [V] Karger et al. 2025, ForecastBench. https://arxiv.org/pdf/2409.19839 (c10, c23)
- [V] Soru and Marshall 2025, log probabilities for forecasting. https://arxiv.org/abs/2501.04880 (c07, c21)
- [V] XFinBench 2025. https://arxiv.org/pdf/2508.15861 (c05, c06)
- [V] Zhang et al. 2025, NoveltyBench. https://arxiv.org/pdf/2504.05228 (c18)
- [V] Jiang et al. 2025, Artificial Hivemind / Infinity-Chat. https://arxiv.org/pdf/2510.22954 (c19)
- [V] Park et al. 2023, Generative agents. https://arxiv.org/pdf/2304.03442 (c16, c17)
- [V, abstract] He and Lim 2026, From control to foresight. https://arxiv.org/pdf/2603.11677 (c15)
- [V, abstract page] Spaniol and Rowland 2023, AI-assisted scenario generation. https://econpapers.repec.org/RePEc:wly:fufsci:v:5:y:2023:i:2:n:e148 (c01)
- [V, summary page] Picavet et al. 2025, state government pilot. https://research.qut.edu.au/centre-for-future-enterprise/?p=8262 (c02)
- [V] arXiv listing searches 2026-11-01. https://arxiv.org/search/?query=%22scenario+planning%22+LLM&searchtype=all (b21, c24)
- [V] Crossref metadata and citation counts, 2026-11-03. https://api.crossref.org/works (d01, d06-d09, d15)
- [M] Schoemaker 1993, Multiple scenario development. https://doi.org/10.1002/smj.4250140304 (a25, b01)
- [M] Phadnis, Caplice, Sheffi, Singh 2015. https://doi.org/10.1002/smj.2293 (a26, b02)
- [M] Kuhn and Sniezek 1996. https://doi.org/10.1002/(SICI)1099-0771(199612)9:4<231::AID-BDM240>3.0.CO;2-L (a33, b03)
- [M] Healey and Hodgkinson 2009. https://doi.org/10.1093/oxfordhb/9780199290468.003.0030 (a28, b04)
- [M] Healey and Hodgkinson 2024. https://doi.org/10.1093/oxfordhb/9780197501061.013.23 (b05)
- [M] Hodgkinson and Wright 2002. https://doi.org/10.1177/0170840602236014 (a27)
- [M] Goodwin and Wright 2001 (abstract via Crossref). https://doi.org/10.1111/1467-6486.00225 (a29, d01)
- [M] Meissner and Wulf 2013. https://doi.org/10.1016/j.techfore.2012.09.011 (a34, b06, d07)
- [M] Chermack, Lynham, van der Merwe 2006/2007. https://doi.org/10.1016/j.techfore.2006.03.004 (b07)
- [M] Phelps, Chan, Kapsalis 2001. https://doi.org/10.1016/S0148-2963(00)00152-4 (b08, d09)
- [M] Cordova-Pozo and Rouwette 2023. https://doi.org/10.1016/j.futures.2023.103153 (a32, b09, d08)
- [M] Scenario planning: evidence to counter black box claims (2020). https://doi.org/10.1016/j.techfore.2020.120156 (b10)
- [M] Chermack 2017, Foundations of scenario planning. https://doi.org/10.4324/9781315641232 (d06)
- [M] Ferrer i Pico et al. 2025, The Time Machine. https://doi.org/10.3390/fi17010048 (a30)
- [M] Ferrer i Pico et al. 2026, Participatory strategic foresight. https://doi.org/10.3390/systems14091060 (b15)
- [M] Generative AI for future architecture scenario planning, Research Square preprint. https://doi.org/10.21203/rs.3.rs-6449315/v1 (a31)
- [M] EcoGym 2026. https://arxiv.org/abs/2602.09514 (c25)
- [M] Practitioner pieces (Finkenstadt HBR, others). https://pure.psu.edu/en/publications/ai-assisted-scenario-generation-for-strategic-planning/ (c26)

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 4 established claims: 2 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E17.01-K04** (reworded: the sources support less). Goodwin and Wright 2001 say strategy evaluation is 'one underdeveloped element' and informal evaluation may select inferior strategies; Wikipedia's de Geus audit statement carries a 'clarification needed' tag; Hodgkinson and Wright 2002 report a largely unsuccessful scenario/cognitive-mapping intervention with a top team, which is not shown to be about post-scenario decision making; none says scenario creation was not a weak point. Corrected claim: Strategy evaluation across scenarios is described as an underdeveloped element of scenario planning (Goodwin and Wright 2001: informal evaluation may select inferior strategies); Wikipedia reports that de Geus's early-1980s audit blamed decision-making after the scenarios for poor strategic implementation (tagged 'clarification needed'); Hodgkinson and Wright 2002 report their own largely unsuccessful scenario intervention with a top management team.
- **E17.01-K07** (reworded: the sources support less). All Brier numbers verify (Halawi .179/.149/.208; ForecastBench .096/.122/.136; Soru .186/.236), but Soru's 0.150 is a reference average for superforecasters on different questions, not a same-question comparison, and Schoenegger et al. found only 'not statistically different' / equivalent within medium-effect bounds on 31 questions, not equal. Corrected claim: LLM forecasting is near human-crowd level but below superforecasters: Halawi's retrieval system scores Brier 0.179 vs crowd 0.149 (best plain model 0.208, random 0.250); a 12-LLM ensemble was not statistically different from 925 human forecasters on 31 questions (equivalent within medium-effect bounds); ForecastBench superforecasters score 0.096 vs 0.122 for the best LLM on the 200-item subset (0.136 without crowd information); Soru and Marshall's pipeline scores 0.186 vs 0.236 for vanilla GPT-4o on its own 72-question test set (a reference superforecaster average of 0.150 comes from other questions).
- **E17.01-K03** (now single-source: only one opened source, code check).
