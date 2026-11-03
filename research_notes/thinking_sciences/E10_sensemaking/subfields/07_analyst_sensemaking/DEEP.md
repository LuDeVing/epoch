# Analyst sensemaking: deep document

*Subfield E10.07. Foraging loop and sense loop (Pirolli and Card 2005). Built from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01, b17, d07 ...) point to those files. Claim ids (K01 ...) point to claims.jsonl.*

## 1. What it is

Analyst sensemaking is how an intelligence analyst turns a large pile of raw documents into a defensible story. Pirolli and Card (2005) studied this with a cognitive task analysis of professional analysts. They wrote down what analysts did as a notional model with two nested loops. [a01]

- **Foraging loop.** Seek information, search and filter it, read it, extract snippets. The output is a smaller, more relevant set.
- **Sensemaking loop.** Fit the snippets into a schema (a representation), build a case from the hypotheses, and tell a story or take an action.

The data flow has six stores, in order: external data sources, shoebox (relevant subset), evidence file (snippets), schema, hypotheses, presentation. Processes sit between them: search and filter, read and extract, schematize, build case, tell story. [a02]

Work runs both ways. Bottom-up goes from data to theory. Top-down goes from theory back to data: a presentation can trigger re-evaluation, and a new hypothesis can trigger a new search. Back loops exist at every level. The mix is opportunistic, not a fixed order. [a03]

The paper also names "leverage points" where technology could help. Foraging side: explore, enrich and exploit under deadline, which is a precision-recall trade-off. Sensemaking side: problem structuring (generating and managing hypotheses), evidentiary reasoning (marshalling evidence for and against) and decision making. Named biases: perception biased toward existing schemas, failure to generate hypotheses, failure to weigh diagnosticity, and failure to focus on disconfirming evidence. [a04, a06, a07]

**Key fact: this is a notional model.** The paper is a conference paper that calls itself "broad brush" and "first results". It reports no sample size, no hours and no effect sizes. Nobody has tested the whole model. [a01, K01]

Why it matters for our agent. The schema (SCHEMA.md) has a represent step (S2), a generate/test cycle and a memory section. Pirolli and Card give a ready split between "fetch and filter evidence" and "fit evidence to a model", plus a named evidence store. The question for us is whether copying that split into an LLM agent helps accuracy at equal tokens. The 2023-2026 literature uses the model heavily as a design frame. It almost never isolates it as a variable. [critique gap 1]

## 2. History and theories in depth

**Roots in cost structure (1993).** Russell, Stefik, Pirolli and Card (1993) described the "cost structure of sensemaking": a learning loop with a generation loop (find a good representation), a data coverage loop (encode data into it), residue (items that do not fit) and a representation shift loop. P&C 2005 describes these four loops. I did not open the 1993 paper. [a09, M]

**Information foraging theory (1999).** Pirolli and Card (1999, Psychological Review 106(4)) argued that people shape their activity to maximise information gained per unit cost. Information lives in patches. Links carry "information scent", a cue to how valuable the patch behind them is. This is the foraging half of the 2005 model. Numbers not verified. [a10, M] A computational version for web navigation is SNIF-ACT (Fu and Pirolli 2007), an ACT-R model of link choice by scent. Not opened. [c25, M]

**Field observations (2001).** Patterson, Roth and Woods (2001) saw analysts start with broad document sets and narrow stepwise before reading. P&C 2005 uses this for the foraging loop. Not opened. [a19, M]

**The 2005 paper.** Cognitive task analysis of analysts. It adds the six stores, the two loops, the explore/enrich/exploit narrowing, and a cost-structure argument about experts. Experts set filters low (accept noise, so as not to miss faint signals) but reject unimportant items faster than novices because of prior schemas. Figure 6 plots information gained against time for expert versus less expert. The figure is notional. The text asserts it and gives no data. [a05, d15]

The expertise grounding cites chess (Simon and Chase 1973, master skill from patterns built over about 15,000 hours, quoted second-hand) and Klein's recognition-primed decision work. An earlier business-analyst case (Pirolli and Card 1999) found schemas around market players and application opportunities. [a08]

**Rival account: data-frame theory.** Klein, Moon and Hoffman (2006) say sensemaking is fitting data into a frame and a frame around the data. A frame defines what counts as data. Sensemaking elaborates, questions or replaces frames. P&C 2005 says its schema plays a similar role. This is covered by the "Sensemaking, data-frame model" subfield, so only the link is noted here. Not opened in this folder. [a11, M]

**First quantitative model (2013).** Lebiere, Pirolli and colleagues built an ACT-R model of the foraging and hypothesis-updating core on six IARPA ICArUS "AHA" tasks. These are map-based probability estimation from event reports, then feature layers (HUMINT, IMINT, MOVINT, SIGINT, SOCINT). The model predicts the presence and degree of four biases without engineering them. Confirmation bias is defined as a distribution peakier than the Bayesian optimum. Anchoring is flatter than optimum (insufficient move from the uniform prior). Biases arise from blended retrieval, partial matching and early utility-based layer selection. The original human data had N=45. A novel sample of N=103 Penn State students (graduate geospatial intelligence coursework) tested generalisation. [a12, a13] It tests a different model than P&C's loops: a model of data-frame-like probability tasks. [critique]

**Workspace and space-to-think line (2011-2024).** Andrews (2011) studied people using large high-resolution displays. Study 1: 8 students solved the VAST 2006 "Stegosaurus" scenario (230 simulated news stories plus images, a map, a spreadsheet; about 10 of 238 documents give ground truth). Fastest solution just under 1.5 hours, slowest close to 3.5 hours. Scores varied widely. Subject L1 spent the first 45 minutes laying out space. Study 2: 5 government-lab participants, observational. Study 3 compared large and small displays. [a15, a16, a17] North et al. (2024) later fed a human-built "space to think" to an LLM. [b22]

**Structured analytic techniques and the ACH argument (2004-2021).** After the 2004 US intelligence reform act, structured analytic techniques became staple training while testing lagged. [b09] Heuer's Analysis of Competing Hypotheses (ACH) is the best known. Mandel and Tetlock (2018) argue that these methods were never tested, that Heuer defended ACH on common sense, and that Heuer said (2010) he would be inclined to ignore a test that did not replicate exactly how ACH is used. [b06] Prior ACH tests were small, had no control group, or used few accuracy measures. Lehner et al. (2008) found ACH reduced confirmation bias in non-analysts but had no effect on analysts. Convertino et al. (2008) had no control group. Kretz et al. (2012) lacked appropriate controls. [b05] A separate subfield (ACH) covers this in depth; here it matters because it is the sensemaking-loop operation most often tested.

**LLM era (2023-2026).** Two uses of the model appear.
1. As a design frame for human tools: Sensecape, Selenite, Marco, InterDeepResearch, the Tang et al. workspace work. [a21, a22, b20, c23, a25]
2. As an architecture for agents: InForage (information-gain rewards), SCOUT (separate evidence state), "Structure Liberates" (eight stages as a trajectory format), DeepNews (wide retrieval plus schema), PatchScout (patch switching), EviDx, SHELDON and SIA (hypothesis and evidence records). [a29, c04, a27, a30, d10, c15, c16, d07]

Several position papers (Cheng and Houben 2026, Jain 2026, Patterson et al. 2025) discuss risks (early anchoring, automation bias, sycophancy) without measurements. [c20, c21, c22, K18]

## 3. Core findings with exact numbers

Status: **established** = two or more independent sources or an opened primary with clear statistics; **single-source**; **contested**.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| P&C 2005 is a notional two-loop model; no sample, counts or effect sizes | none reported | a01, a02, a03, d15 | established (as a statement of its type) |
| "Experts gain information faster" (Figure 6) has no data | notional graph | d15 | established |
| Explore/enrich/exploit narrowing is a design claim only | no measured test | a04, a05 | single-source |
| ACT-R model of data-frame tasks, S1 match to Bayesian rational, model vs human (novel N=103) | T1 81.7 vs 80.7; T2 68.5 vs 78.9; T3 72.1 vs 79.7; T4 94.4 vs 87.6; T5 84.5 vs 84.5; T6 85.3 vs 88.3 | a13 (Lebiere 2013, Table 6) | single-source |
| Same model, resource allocation (S2), Task 3 | model 34.7 vs human 73.8 (clear miss) | a13 | single-source |
| Large display helps structuring (N=8, alpha 0.1, no correction) | structures 15.75 vs 9 (p=.004); structural events 96.9 vs 45.3 (p=.011); complex structures 4.35 vs 0.875 (p=.065); coverage 18.53% vs 13.12% (p=.061); analytic performance not significant | a17 (Andrews 2011) | established (weak) |
| Human-built space to think improves LLM summary score (out of 90) | docs only 45.2 (correctness 11.0/30, quality 34.2/60) vs with space 68.5 (19.5/30, 49.0/60) | b22 (North 2024) | single-source |
| Sensecape: concepts explored (N=12 within) | 68.3 (SD 49.1) vs 22.8 (SD 7.7), t(11)=3.1, p=.01; prompts 7.3 vs 5.8 (p=.37); nodes 26.8 vs 23.5 (p=.45) | a21, b13, c13 | established |
| Sensecape: hierarchy and revisits | levels 4.3 vs 2.6 (p=.02); revisits 12.8 vs 0.7 (p<.01) | b14 | established |
| Sensecape: preference | 9 of 12 preferred it for deeper understanding; for broad understanding 6 preferred baseline, 1 no preference | b15 | established |
| Selenite (N=12 within) | 840.3 s (SD 102.7) vs 1319.3 s (SD 120.0), 36.3% faster, F(1,20)=102.5, p<.01; valid criteria 12.93 vs 6.79 (+90.4%); precision 98.8% vs 78.4%; recall 73.0% vs 30.4%; option extraction 100% | a22, c14 | established |
| Marco: speed vs accuracy (N=16 within) | 249.6 s vs 297.3 s (16% faster, p=.004); accuracy 88.1% (SD 10.1) vs 91.9% (SD 8.3), chi2(1)=3.35, p=.067 | b20 | single-source |
| Participatory prompting, 15 non-experts with Bing Chat | qualitative; benefits and barriers mapped to the two loops | b21 | single-source |
| ACH did not help trained UK analysts (N=50, 25 per group) | MAE control 0.21 vs ACH 0.26, d=0.43, p=.14, t(45.9)=1.49; random responding 0.33; analysts 0.23 (d=0.95 vs random) | b01 (Mandel et al. 2018) | contested |
| ACH improved rating of evidence usefulness but not forecasts | usefulness rating d=1.59, p<.001; tracking vs accuracy r(24)=-.10, p=.63 | b02 | single-source |
| Unpacking effect not reduced by ACH | unpacking factor above 1 in both groups; control d=0.96; ACH M=1.77, d=1.69; group difference n.s. | b03 | single-source |
| Coherence correction beats the method | coherentized MAE 0.15 vs raw 0.23 (35% drop, d=0.96); with aggregation 61%; gain d=1.37 ACH group vs d=0.69 control | b04, b08 | single-source |
| ACH training in 191 law students: no change in question preference | both groups preferred exonerating questions; no confirmation bias in either group | b25, with b05 | established |
| GPT-4 on a fictional terror-plot task (one case, workshop paper) | key facts: crowd 17 (all comprehensive); holistic 6 (0 comprehensive); step-by-step 9 (5 comprehensive). Hypotheses of 15: crowd 4 (all comprehensive); holistic 10 (6 comprehensive); step-by-step 3 comprehensive | b10, c11, d16 | single-source |
| Global questions: graph summaries vs vector RAG | comprehensiveness win rate 72-83% (p<.001); podcast graph 8,564 nodes / 20,691 edges; news graph 15,754 / 19,520 | a23 (GraphRAG) | single-source |
| Context size and grounding in financial news (20 topics x 5 sizes = 100 reports) | hallucination-free: under 10k chars below 20%; 15k 40%; 30k 85%; 40k 90%. Blind test 3 of 12 accepted vs 0 of 10 | a30, c17, d14 | single-source |
| SCOUT on long-text QA (LOOGLE-V2) | SCOUT 78.7 at 29.7k tokens (ablation table gives 78.2); Gemini-3-Pro 68.5 at 273.9k; GPT-5.1-chat 58.6; GPT-4.1 56.8; Claude Code agent 63.4 at 25.3k; MemAgent 46.0; ReadAgent 27.7; accuracy per k tokens 2.63 vs 0.25 | c04 | single-source |
| SCOUT ablations (full 78.2) | no separate epistemic state 70.5 (-7.7) at 28.3k tokens; no document access 17.7 (-60.5); no file tools 74.2 (-4.0); no grounding 75.5 (-2.7) | c05, d13 | single-source |
| SCOUT training, foraging interface vs plain answer SFT (two backbones) | plain SFT about +1.2, -0.5 / -0.7, +1.6; SCOUT-interface SFT +27.1, +13.0 / +25.1, +10.4 (column reading uncertain) | c06 | single-source |
| InForage (3B, PPO, information-gain reward), mean EM over 8 sets | InForage 41.0; Search-o1 35.6; Self-RAG 31.8; IRCoT 29.4; plain RAG 26.5; RL without retrieval 19.9; vanilla 12.9 | c01, a29 | single-source |
| PatchScout, prompt-only patch switching, coverage % at 10,000 pages (Universities / Fortune 500 / Law / Autism) | No-reseed 1.7 / 3.0 / 1.0 / 1.5; Fixed-reseed 16.1 / 18.4 / 72.6 / 30.8; Scent-EMA 15.5 / 24.6 / 86.8 / 35.3; Threshold 14.8 / 23.8 / 85.3 / 39.1 | d10 | single-source |
| PatchScout at matched tokens vs trained DeepResearcher-7B | coverage DeepResearcher 0.3 / 0.8 / 1.0 / 17.3 vs Scent-EMA 5.6 / 7.6 / 40.1 / 12.8; pages visited 78, 56, 28, 64 vs 951, 1223, 1664, 1491 | d11 | single-source |
| PatchScout ablations (coverage %) | Scent-EMA 15.5 / 24.6 / 86.8 / 35.3; Random-reseed 4.6 / 2.2 / 25.4 / 9.0; Upfront-scout 1.2 / 2.0 / 11.7 / 12.0; Random-forager 8.3 / 6.6 / 28.9 / 10.5 | d12 | single-source |
| LLMs confirm instead of falsify (11 models, Wason rule discovery, 45 turns) | success 6% to 78%; positive correlation between incompatible:compatible test ratio and success | b17 | single-source |
| Counterexample prompts raise discovery | average 42% to 56%; Qwen3-8B thinking 0.21 to 0.36 (TiO) and 0.40 (Dual-Goal), I:C 0.15 to 0.35; Qwen3-32B thinking 0.413 to 0.613 (TiO) and 0.600 (Dual-Goal), turns to success 10.83 to 6.38, I:C 0.14 to 0.54 | b18, b19, d01 | single-source |
| Same prompts on non-thinking models | Qwen3-32B non-thinking 0.325 baseline, Dual-Goal 0.100, TiO 0.362. Paired tests: thinking Dual-Goal +0.148 (p<2e-5), TiO +0.123 (p<2e-5); non-thinking Dual-Goal -0.060 (p=.0065, harmful), TiO +0.063 (p=.0033) | d01, d02 | single-source |
| Blicket transfer (same authors, 192 episodes, TiO) | thinking: 8B 0.32 to 0.40; 14B 0.50 to 0.61; 32B 0.57 to 0.86; R1-Llama-70B 0.41 to 0.43; QwQ-32B 0.80 to 0.82. Non-thinking: 8B 0.11 to 0.19; 14B 0.25 to 0.20; 32B 0.64 to 0.56 (worse) | d04 | contested |
| Tokens per turn rise with the falsify prompts | Qwen3-8B 1088 vs about 2142; Qwen3-32B 1030 vs 1472; episode totals not reported | d03 | single-source |
| SIA (hypothesis and evidence record + counterfactual critic), 100 forum diagnosis cases, final score /100 [95% CI] | SIA 79.2 [72.7, 83.7]; THK-int 72.8 [66.8, 79.8]; Ask-5 72.3; ReAct 69.0; THK 67.5; BAS 67.3; ToT 61.5. Questions asked 5.2 vs 3.7. Other backbones 75.4 vs 69.2 and 76.1 vs 68.4 | d07 | single-source |
| SIA ablations (final / potential) | full 79.2 / 89.2; no structured investigation 72.8 / 84.7; no counterfactual critique 74.0 / 85.5; no follow-up questions 75.0 / 85.0; no hypothesis expansion 76.5 / 79.3; no final adjudication 76.0 / 89.2; no weight updates 78.5 / 88.5 | d08 | single-source |
| SIA anchoring test (10 paired cases) | final 80.0 vs 76.0 with a wrong user conjecture; exact diagnosis 6/10 vs 5/10; wrong cause chosen 2/10 | d09 | single-source |
| ACH-style matrix prompt for the decider (AgentCDM) | zero-shot ACH about +2.0 over single agent, +1.9 over unstructured decider on MMLU, MMLU-Pro, ARC-C; voting rules about +0.0 to +0.1; trained AgentCDM +8.6 to +11.6. Scaffolding-only training 68.1 vs vanilla 72.6 (MMLU); full 78.5 | d05, d06 | single-source |
| EviDx (evidence state + observer blocking early stop), 100-case subsets | Qwen3-8B 18% to 44% (JAMA); Llama3.1-8B 17% to 31%; Sonnet 4.6 66% (JAMA), 52% (DiagnosisArena); Llama3.1-8B evidence-cognition score 63.8% to 15.1% | c15 | single-source |
| SHELDON (dual search over hypotheses and observations) | DiagnosisArena 84.00 vs RLM 78.00 and Codex 76.00; ORCA-Bench 66.67 vs 40.00; ARC-AGI-2 59.17 vs EvoX 47.50 at $2.5 per task. Of 59 root causes, 40 from exploring, 19 from refining | c16 | single-source |
| Constrained sensemaking order for ideation (8 open-weight families, 120,000 trajectories) | Hindsight +2.0% plan quality over Foresight; most diverse in all 8 families; Hindsight spends more on Schema (+4.2 pts), Foraging (+3.7), Elaboration (+1.7) | a27, a28, c08, c10 | single-source |
| Incremental workspace-driven report refinement (35 workspace pairs) | targeted-refinement precision/recall: baseline 0.752/0.858; VIS-Act 0.975/0.782; VIS-ReAct 0.951/0.887 | a25 | single-source |
| Spatial steering user study (N=14) | incremental refinement steady gain; regeneration baseline plateaus, variance grows; regeneration omitted 4 of 9 keywords for one person | a26 | single-source |
| SOC field log of GPT-4 use | 3,090 queries, 45 analysts, 10 months; 93% map to NICE competencies; most interactions 1-3 turns | a24 | single-source (descriptive) |
| Patch-switching is linearly decodable from LLM activations | switch probability vs patch depletion r about 0.31 or more, p<.0001; AUC anticipatory 0.72, event 0.87 (Gemma-9B); 699 human vs 699 Llama sequences | c18, c19 | established (two groups) |
| InterDeepResearch (15 users) | Likert 1-5: understanding agent process 4.80, ease 4.60, backtrace 4.33, satisfaction 4.33 | c23 | single-source |

## 4. Mechanisms and models

Each mechanism is written so it can be coded.

**4.1 The six-store pipeline (P&C 2005).** Keep these as named stores in code, not one blob of context.
1. `external`: documents, search index, files.
2. `shoebox`: ids of items judged relevant after a cheap filter.
3. `evidence`: short snippets, each with a source anchor (document id and span).
4. `schema`: a structured representation of the problem (entities, relations, timeline, or a table of candidate answers).
5. `hypotheses`: candidate explanations or answers, each linked to the evidence rows that support or contradict it.
6. `presentation`: the final answer, built only from `hypotheses` plus linked `evidence`.

Transitions are plain functions: `search_filter(query) -> shoebox`, `read_extract(shoebox) -> evidence`, `schematize(evidence) -> schema`, `build_case(schema) -> hypotheses`, `tell(hypotheses) -> presentation`. Back loops are edges chosen by code on a signal. A gap between hypotheses and evidence sends control to `search_filter`. A snippet that fits no schema slot is residue (the 1993 idea) and sends control to `schematize`. P&C do not say what the signal is. The schema's G1 says it must be a check, not a schedule.

**4.2 Foraging as patch choice (information foraging).** Treat the retrieval budget as patches (a source, a query family, a document). For each patch keep a running gain estimate (new facts per fetch). Stay while gain is above a threshold. Switch when it falls. PatchScout does this with an LLM scoring links for scent (batches of up to 16) and an exponential moving average of realised yield. The simplest switch is a fixed page count. [d10]
```
gain_ema = init
loop:
  items = fetch(patch)
  new = count(facts in items not already in evidence)
  gain_ema = a*new + (1-a)*gain_ema
  if gain_ema < thr: patch = next_patch()   # or stop if budget/answer-ready
```
InForage puts the same idea into training: a reward for information gain per retrieval plus an efficiency penalty (PPO, Qwen2.5-3B). [c01] That needs RL, which our program does not do. PatchScout is the prompt-only form.

**4.3 Separate epistemic state (SCOUT).** Keep a compact store of claims with source anchors that is not the action history. Each cycle: diagnose gaps against the query, then either explore (fetch more) or update the store. The program rewrites the store; it is not left as raw chat history. Merging it back into a ReAct-style log cost 7.7 points at about equal tokens. [c04, c05, d13]

**4.4 Hypothesis and evidence record with a counterfactual critic (SIA, SHELDON).** Keep two linked spaces. Hypotheses point to the observations they explain. Observations point to the hypotheses they support. A critic step asks "what observation would break the leading hypothesis, and which observations does it fail to explain?" Unexplained observations spawn new hypotheses. SHELDON: 40 of 59 root causes came from exploring, 19 from refining. SIA: dropping the critic cost 5.2 points, dropping the structured state 6.4, dropping numeric weight updates only 0.7. [c16, d07, d08] Numeric weights on hypotheses are not worth building.

**4.5 Incompatible-test step (Failing to Falsify).** Before an experiment, the model names the current best hypothesis, then proposes a test whose result would contradict it. Code measures the incompatible:compatible ratio of tests. In thinking models this ratio rose from 0.14 to 0.54 (Qwen3-32B) and success from 0.413 to 0.613. [b17, d01] It raised tokens per turn (1030 to 1472 for 32B), though turns to success fell. [d03]

**4.6 Stop gate against premature closure (EviDx).** An observer refuses a final answer until uncertainty is low and evidence coverage is enough. Uncertainty there comes from model-stated beliefs, which may be unreliable (schema G10 and the 4b row on verbal confidence). A code-counted coverage rule (every hypothesis has at least one linked supporting or contradicting evidence row) is safer. [c15]

**4.7 Incremental refinement instead of regeneration.** When the workspace changes, update only the affected parts of the output. Code computes the diff, because the LLM could not reliably find differences between two workspaces. [a25, a26]

**4.8 Step decomposition of a holistic read (Li et al.).** Fact extraction first, hypothesis generation second, both over the same documents. Holistic runs merged the steps (facts pulled while selecting documents, hypotheses while extracting facts). Splitting raised fact coverage from 6 to 9 of 17. [b10, b11, c11]

**4.9 Community summaries (GraphRAG).** For corpus-wide questions, build an entity graph, detect communities, pre-write a summary per community, then answer by combining summaries. This is memory, not reasoning. [a23]

**4.10 Constrained order (Hindsight).** Fix the stage order so the plan is conditioned on a known outcome. The effect is small (+2.0%). [a27]

## 5. What holds up

**Whole-model support.** None. No paper tests the foraging/sense split as a variable against a single mixed loop at equal tokens. Lebiere 2013 tests a related ACT-R model, not P&C's loops, and misses resource allocation badly (34.7 vs 73.8). [K01, K16, critique gap 1]

**Moderate support for pieces.**
- *A written evidence state helps on long documents.* SCOUT -7.7 at equal cost (70.5 vs 78.2). SIA -6.4 without structured investigation. Different tasks and backbones, each a single preprint. Untested where documents fit in context. [d13, d08]
- *Falsification prompts help thinking models on rule discovery.* The second task (Blicket) is mixed (32B non-thinking 0.64 to 0.56) and is by the same authors. No independent replication. [d04]
- *Switching patches helps.* PatchScout: no-reseed 1.7 vs 15.5 coverage on Universities; Law 1.0 to 86.8. But Fixed-Reseed gets most of it (16.1, 72.6). Scent adds a small, inconsistent increment (loses on Universities, 15.5 vs 16.1). [d10]

**Failures and nulls.**
- ACH on analysts: null, direction against ACH (MAE 0.26 vs 0.21, d=0.43, p=.14, N=50). [b01] Lehner 2008 null on analysts. [b05] Law students N=191: null. [b25] Design caveat: Heuer would ignore a test that is not faithful. So the status is "contested", not refuted. [b06]
- ACH raised accurate rating of evidence usefulness (d=1.59) but forecasts did not follow (r=-.10). A better rationale did not mean a better answer. [b02]
- Faster is not more accurate. Marco 16% faster with 88.1 vs 91.9% accuracy. Sensecape: 6 of 12 preferred baseline chat for broad understanding. [b20, b15]
- Rigid structure can hurt. AgentCDM scaffolding-only 68.1 vs plain prompt 72.6. [d06]
- Falsify prompt "Dual-Goal" hurt non-thinking models (-0.060, p=.0065). [d02]
- One-directional bias warnings may shift thresholds and create the mirror bias, not better thinking. [b07]
- Figure 6 (expert speed advantage) has no data. [d15]
- Human-AI teams often do not beat the best individual. [c21]

**Moderators.**
- Thinking vs non-thinking mode: falsify prompts help the first, not reliably the second. [d02]
- Context volume: grounding rose from 40% to 85% between 15k and 30k characters, but it is one factor with 20 reports per cell and no variance. [d14]
- Task type: SCOUT on very long text; SIA and SHELDON on diagnosis; PatchScout on corpus collection. Cross-comparison is not possible.
- Topic sparsity: on the Autism topic the trained DeepResearcher beat Scent-EMA at matched tokens (17.3 vs 12.8). [d11]
- Commercial deep-research tools reach 92-93% coverage on the Law topic from one report, far above PatchScout's token-matched 40.1%. [d11]

**Interventions that worked (with caveats).** Written evidence state (SCOUT), counterfactual critic (SIA), incompatible-test prompts for thinking models, patch switching, hypothesis plus observation dual space (SHELDON), coherence correction of probabilities (-35% error, human data), incremental update by code.

**Interventions that did not work.** ACH matrix for human analysts; ACH training for law students; a rigid scaffold alone for a trained model; Dual-Goal on non-thinking models; numeric weight updates on hypotheses (0.7 points).

## 6. Language models

**How they behave.**
- *They confirm.* Eleven LLMs in a rule-discovery loop propose tests that fit their current guess. Success ranged from 6% to 78% in 45 turns. More confirmation went with lower success. [b17]
- *They merge the steps.* Given a sensemaking task, GPT-4 pulls facts while picking documents and jumps to hypotheses while extracting facts. [b11]
- *They compress.* Holistic GPT-4 covered 6 key facts versus 17 for the crowd, none comprehensive. Specific details were lost: an account and bank fact became "has financial ties". Hypotheses were more numerous (10 vs 4) but the crowd's were fully comprehensive. [b10, b12] One case, one model, no statistics, a 2024 workshop paper. [d16]
- *They lose long context.* Frontier long-context models degrade from 64K to 1M tokens while a foraging agent stays flat (figure only, no extracted values). [c07]
- *Their search activity looks like patch foraging.* Switching between semantic categories follows patch depletion, and a linear probe decodes a switch (AUC 0.72 anticipatory, 0.87 event in Gemma-9B). Steering raised switching to 0.68 (item level) and 0.45 (category level). Models of 7B to 9B on a simple fluency task. [c18, c19]
- *A wrong user conjecture hurts only a little if held as a hypothesis.* SIA: 80.0 vs 76.0. [d09]
- *They cannot reliably diff two workspaces.* So code does the diff. [a25]
- *Early AI insight may anchor users.* Position claim only. [c22, b24]

**What changed results, and by how much** (all single-source).

| Change | Task | Effect | Token control |
|---|---|---|---|
| Separate epistemic state (SCOUT) | long-document QA | +7.7 points (70.5 to 78.2) | about equal (28.3k vs 29.7k) |
| Structured investigation state (SIA) | diagnosis | +6.4 (72.8 to 79.2) | no, more calls |
| Counterfactual critic (SIA) | diagnosis | +5.2 (74.0 to 79.2) | no |
| Think-in-Opposites, thinking Qwen3-32B | rule discovery | 0.413 to 0.613 | tokens per turn up 43%; turns to success down |
| Same prompts, non-thinking | rule discovery | Dual-Goal -0.060; TiO +0.063 | not reported |
| Step-by-step vs holistic (GPT-4) | fact extraction, one case | 6 to 9 facts of 17 | not reported |
| Patch switching (PatchScout) | corpus collection | e.g. Law 1.0 to 86.8 coverage | matched in Table 8 |
| ACH-style decider prompt (zero-shot) | MCQ knowledge | about +2.0 | no |
| Info-gain reward (InForage, RL) | multi-hop QA, 3B | EM 41.0 vs 35.6 | training required |
| Hindsight ordering | ideation plans | +2.0% | n/a |
| GraphRAG over vector RAG | global questions | 72-83% win rate | n/a |
| Human-built space to think given to LLM | summaries, score /90 | 45.2 to 68.5 | n/a |

**Caveats.** Backbones differ (3B, 72B, API models). Several results are 2025-2026 preprints with no replication seen. Model names such as GPT-5.6-terra were taken from the sources and not verified further. SCOUT's two tables differ by 0.5 (78.7 vs 78.2). LLM judges score SIA. [critique]

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema part: G guardrail, S state, O operator, memory.

### Add now (established)

Very little in this subfield is established for an agent. The items below cost nothing or protect against known problems.

1. **Report speed and accuracy separately, and gate any shortcut on accuracy parity.** G7 (pay for itself). [E] b20, b15 (K06). Marco was 16% faster but 3.8 points less accurate; Sensecape users preferred chat for broad questions.
2. **Keep the full ACH matrix in section 4b "not to add".** O (hypothesis comparison). [C, leaning E for humans] b01, b05, b25 (K07, K10). The new LLM evidence is small and not token-matched (d05, d07), so it goes to testing, not to adding.
3. **Do probability normalising in code (already G5).** G5. [S here, supported elsewhere] b04, b08 (K09). The 35% error cut is human data; our schema already cites it.
4. **Tag every logged step as forage or sense, without changing behaviour.** Section 6 logging. [S] a01-a03 (K01). Free. It gives the data needed for test U2. Do not treat the tags as an effect until tested.
5. **Do text and diff comparisons in code, not by model.** G2/G5. [S] a25.
6. **Treat the P&C model as a design frame, not as evidence.** [E] a01, d15 (K01, K27). Do not cite Figure 6 or "experts forage faster".

### Test first (candidates, not yet adding)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Separate written evidence state (claims with anchors) vs the same notes kept in context | memory / S2 | [S] | c04, c05, d13, d07, d08 (K03, K23) |
| T2 | Forced forage/sense split vs one mixed loop | S structure | [S], untested | a01, critique gap 1 (K01) |
| T3 | "Test that would break the leading hypothesis" step, thinking mode only, only on a failed check or impasse | G (confirmation), O | [S] | b17, b18, d01, d02, d04 (K11, K22) |
| T4 | Counterfactual critic on a hypothesis/evidence record | O / S6 | [S] | d07, d08 (K23) |
| T5 | Gain-per-fetch stop and patch switch | O1/O2, S0 budget | [S] | d10-d12, c01 (K04, K25) |
| T6 | Step-wise extraction (facts first, hypotheses second) | S1/S2 | [S] | b10, b11, c11 (K12) |
| T7 | Stop gate on code-counted evidence coverage | S8 | [S] | c15 (K21) |
| T8 | Community-summary memory for global questions | memory | [S] | a23 (K13) |
| T9 | Persistent structured workspace vs flat scratchpad | memory | [S] | a17, b22 (K17) |
| T10 | Context volume vs redundancy | memory | [S] | a30, d14 (K26) |
| T11 | ACH-style matrix with freedom to deviate | O | [C] | d05, d06, b01 (K07, K24) |
| T12 | Hindsight-style synthesis order | O | [S], small | a27 (K15) |

Do not build: numeric weights on hypotheses (0.7 points, d08), forced matrices with no room to deviate (d06), model-stated entropy as a stop signal (G10, section 4b).

## 8. Concrete tests on our bench

All arms get the same total token cap, setup counted (G7). Report accuracy, tokens and a paired-bootstrap interval. Use at least 100 items per arm where the pool allows, since most source effects are 2 to 8 points.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 evidence state | multi-document QA that fits in context, plus one long-context set | (a) plain model with notes in context; (b) program-written evidence file with anchors, model reads only the file plus question | accuracy; tokens | long set +5 to +8 (SCOUT); in-context set 0 to +3; null is plausible |
| T2 forage/sense split | multi-hop QA needing both retrieval and a conclusion | (a) mixed ReAct loop; (b) forced forage phase (cap k fetches) then sense phase on the shoebox; (c) free alternation | accuracy; share of tokens per phase | 0 to +4; may hurt when the first query is wrong |
| T3 falsify step | rule-discovery or ARC-like hypothesis items with a held-out check; thinking and non-thinking modes | (a) plain; (b) one incompatible-test proposal on failure only; (c) the same every turn | success at turn cap; incompatible:compatible ratio; tokens to success | thinking +0.10 to +0.20; non-thinking about 0 or negative; (c) worse than (b) per G1 |
| T4 counterfactual critic | diagnosis / abductive items with an answer key | (a) hypothesis list only; (b) plus critic "what would break the leader, what is unexplained"; (c) plus written record | accuracy; tokens | +3 to +6 (SIA); tokens rise, so match by cutting samples |
| T5 gain-per-fetch | multi-hop QA with a retrieval tool | (a) fixed fetch count; (b) stop or switch when the last fetch added no new fact; (c) no stop | accuracy per 1k tokens | (b) equals (a) accuracy at 10-30% fewer tokens; small |
| T6 stepwise extraction | document sets with a fact answer key | (a) holistic; (b) facts then hypotheses | fact recall; comprehensive-fact count | +3 facts of 17 (b10); many cases needed (source had one) |
| T7 coverage gate | diagnosis items with early-closure errors | (a) no gate; (b) refuse answer until each hypothesis has linked evidence | accuracy; premature-answer rate | small; hurts if budget runs out (G6 forces a best answer) |
| T8 community memory | corpus-wide "main themes" questions | (a) flat retrieval; (b) community summaries | rubric scoring where possible; pairwise only with a blinded, length-normalised judge (G5) | win rate 70%+ if source holds; judge noise is the risk |
| T9 workspace | tasks with 10+ interacting entities | (a) flat scratchpad; (b) typed table of entities and relations | accuracy | 0 to +5 |
| T10 volume vs redundancy | grounded long-form synthesis | (a) 15k chars; (b) 30k; (c) 30k deduplicated to 15k unique; (d) 15k padded with duplicates to 30k | claim-level support rate | shows whether the cliff is volume or novelty |
| T11 ACH matrix | items with several plausible answers | (a) free reasoning; (b) matrix with allowed deviation | accuracy | +0 to +2; keep out of schema if under +2 |

## 9. What does not transfer, and why

- **Human tool gains (Sensecape, Selenite, Marco).** They measure human speed, breadth and preference at N=12 to 16, often against self-built baselines. Our agent has no human to be faster. Only the idea of an up-front overview carries over, as a test. [K05, K06]
- **The ACH human null.** Analysts under time pressure with a matrix differ from an LLM that fills a matrix in one call. The null does not prove the matrix fails for LLMs, and it does not prove it works. [K07]
- **Expert-novice claims.** Figure 6 is notional. Do not build expertise-speed logic on it. [K27]
- **Information scent as a learned reward.** InForage needs PPO training. We do not train. PatchScout is the only prompt-only analogue, and its gain over a fixed count is small. [K04, K25]
- **Coherence-correction numbers.** The 35% and 61% error cuts are for human probability judgments over four hypotheses. Models differ in how incoherent they are. [K09]
- **ACT-R fits.** Matching human bias profiles on map probability tasks says nothing about LLM accuracy. [K16]
- **SOC field log.** Descriptive; no accuracy or outcome measure. [K19]
- **Activation probes for foraging.** Interpretability of 7B to 9B models on animal fluency. It shows a patch-depletion signal exists. It does not show a scaffold helps. [K20]
- **Large display.** The human benefit is more space for spatial memory. Agent context is not spatial. Only the idea of a persistent structured external store might carry. [K17]
- **Position papers.** Anchoring and automation bias are plausible but unmeasured. [K18]
- **Open-ended story building.** Our bench items mostly have checks. P&C's open-ended product does not.

## 10. Open questions

1. Does a forced forage/sense split beat a single mixed loop at equal tokens? No paper isolates it. SCOUT's nearest proxy splits action log from evidence state, not forage from sense. [d13]
2. Does a written evidence state beat the same notes in context when the task fits in context? Partly closed for long text and diagnosis only.
3. Is the falsification gain replicated outside rule discovery, by other authors, and at equal total tokens? Blicket was mixed and by the same authors. [d04]
4. Does an ACH matrix help LLMs on analyst-style items at equal tokens? Evidence is MCQ and diagnosis, not token matched. [d05, d07]
5. Does scent beat a fixed count of fetches for stopping to answer (not for corpus collection)? [d10]
6. Do expert analysts gain information faster than novices in measured data? Figure 6 is notional; no data found. [d15]
7. Can Li et al. (holistic vs step-by-step, one case, GPT-4) be reproduced with current models and many cases? [d16]
8. Is DeepNews' 30k-character cliff volume or redundancy? One factor, 20 reports per cell. [d14]
9. Can Andrews' structure effect (15.75 vs 9) become an agent workspace that helps? Alpha 0.1, N=8. [a17]
10. Do the SCOUT and SIA ablations survive other backbones and token-matched controls? SIA ablations are a single run with no CIs.
11. Search limits: the gap search could not use the Semantic Scholar and OpenAlex APIs (rate limits), so "none found" means none seen.

## 11. Sources

[V] = opened and read. [M] = snippet or citation only.

- [V] Pirolli and Card (2005), The sensemaking process and leverage points for analyst technology. https://www.phibetaiota.net/wp-content/uploads/2014/12/Sensemaking-Process-Pirolli-and-Card.pdf
- [V] Slide summary of Pirolli and Card (2005), cross-check only. https://www3.cs.stonybrook.edu/~mueller/teaching/cse591_visAnalytics/sensemaking.pdf
- [M] Pirolli and Card (2005), ResearchGate listing. https://www.researchgate.net/publication/215439203
- [M] Russell, Stefik, Pirolli and Card (1993), The cost structure of sensemaking. https://doi.org/10.1145/169059.169209
- [M] Pirolli and Card (1999), Information foraging, Psychological Review 106(4). https://doi.org/10.1037/0033-295X.106.4.643
- [M] Klein, Moon and Hoffman (2006), Making sense of sensemaking. https://doi.org/10.1109/MIS.2006.75
- [M] Patterson, Roth and Woods (2001), Predicting vulnerabilities in computer-supported inferential analysis. https://doi.org/10.1007/s101110100022
- [M] Kang and Stasko and related field studies, as cited by Andrews (2011). No URL.
- [M] Fu and Pirolli (2007), SNIF-ACT. https://doi.org/10.1080/07370020701493509
- [M] Lebiere et al. (2013), ACT-R sensemaking model, reference entry. https://doi.org/10.1155/2013/921695
- [V] Lebiere, Pirolli, Thomson, Paik, Rutledge-Taylor, Staszewski and Anderson (2013), ACT-R sensemaking model. https://pmc.ncbi.nlm.nih.gov/articles/PMC3835765/
- [V] Andrews (2011), Space to Think: Sensemaking and Large, High-Resolution Displays. https://vtechworks.lib.vt.edu/bitstreams/297627ea-c93a-4c89-8daa-4567077aed52/download
- [V] North et al. (2024), Space to Think as a Common Ground for Human-AI Sensemaking. https://people.cs.vt.edu/naren/papers/SpacetothinkCHISensemaking2024.pdf
- [V] Suh, Min, Palani and Xia (2023), Sensecape. https://arxiv.org/abs/2305.11483
- [V] Liu, Wu et al. (2023/2024), Selenite. https://arxiv.org/abs/2310.02161
- [V] Edge et al. (2024), GraphRAG, from local to global. https://arxiv.org/abs/2404.16130
- [V] Singh et al. (2025), LLMs in the SOC. https://arxiv.org/abs/2508.18947
- [V] Tang et al. (2025), Agentic reasoning and refinement through semantic interaction. https://arxiv.org/abs/2510.02157
- [V] Tang et al. (2026), Semantic Prompting. https://arxiv.org/abs/2604.19971
- [V] Mooney, Kim, Lee and Kang (2026), Structure liberates. https://arxiv.org/abs/2605.00557
- [V] Qian and Liu (2025), Scent of Knowledge (InForage). https://arxiv.org/abs/2505.09316
- [V] Jiang (2025), Workflow is all you need (DeepNews). https://arxiv.org/abs/2512.10121
- [V] Mandel, Karvetski and Dhami (2018), Boosting intelligence analysts' judgment accuracy. https://doi.org/10.1017/S1930297500006628
- [V] Mandel and Tetlock (2018), Correcting judgment correctives in national security intelligence. https://doi.org/10.3389/fpsyg.2018.02640
- [V] Maegherman, Ask, Horselenberg and van Koppen (2021), Test of ACH in legal decision-making. https://research.vu.nl/en/publications/test-of-the-analysis-of-competing-hypotheses-in-leg
- [V] Li, Bonepalli and Mohanty (2026, CHI 2024 workshop), What to make sense of in the era of LLMs. https://arxiv.org/abs/2603.08604
- [V] Marco (2024), Collection-centric information foraging with LLMs. https://arxiv.org/abs/2405.01501
- [V] Participatory prompting study of GenAI data analysis (2024). https://arxiv.org/abs/2407.02903
- [V] Cheng and Houben (2026), Who's Sense is This? https://arxiv.org/abs/2603.17643
- [V] Zhang et al. (2026), SCOUT. https://arxiv.org/abs/2605.04496
- [V] Zeng, Zhang and Zhang (2026), EviDx. https://arxiv.org/abs/2608.24570
- [V] Joshi, Shethia and Lam (2026), SHELDON. https://arxiv.org/abs/2610.18025
- [V] Leckie, Todd and Foster (2026), Signatures of semantic search in LLM activations. https://arxiv.org/abs/2609.35599
- [V] Lacosse, Duarte, Todd and McNamee (2026), Emerging human-like strategies in LLM fluency. https://arxiv.org/abs/2603.01822
- [V] Patterson et al. (2025), Sensemaking in novel environments. https://arxiv.org/abs/2503.07783
- [V] Jain (2026), Collaborative causal sensemaking. https://arxiv.org/abs/2512.07801
- [V] Pan et al. (2026), InterDeepResearch. https://arxiv.org/abs/2603.12608
- [V] Jhaveri et al. (2026), Failing to Falsify. https://arxiv.org/abs/2604.02485
- [V] Zhao et al. (2025), AgentCDM. https://arxiv.org/abs/2508.11995
- [V] Marozzo and Lio (2026), LLM-as-an-Investigator (SIA). https://arxiv.org/abs/2606.13220
- [V] West and Dragut (2026), PatchScout. https://arxiv.org/abs/2611.00169

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 8 established claims: 4 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E10.07-K01** (reworded: the sources support less). The paper itself confirms a notional, preliminary model (two loops, six data stores, back loops, no sample size or statistics, derived from interviews and protocols with several analysts); but a01-a03 are one document, and 'never been tested as a whole' rests only on a failed search note (a31), not on a source. Corrected claim: Pirolli and Card 2005 present a notional two-loop model (foraging loop, sensemaking loop, six data stores, back loops at every level) derived from a preliminary cognitive task analysis of several intelligence analysts, with no reported sample size, counts or effect sizes; no direct test or replication of the whole model was found in this search.
- **E10.07-K17** (reworded: the sources support less). Table 4.1 comes from a 16-subject study (8 per condition), not N=8 total, and the same study found no difference in analytic score, so 'helps human sensemaking' is wider than the data (more structures only; alpha was set at p<0.1). Corrected claim: Large display space changed how people structured their workspace (n=16, 8 per group): more structures, 15.75 vs 9 (p=.004, t-tests with alpha .1), with coverage only borderline (18.53% vs 13.12%, p=.061) and no significant difference in analytic score.
- **E10.07-K20** (now single-source: the sources are not independent). Both papers share co-author Peter M. Todd and are sibling studies of the same task (semantic fluency); the AUC values 0.72/0.87 come from the first paper alone and are maximum values for Gemma-9B only; the second paper's probe on real human sequences was weak (AUROC 0.57) and only strong on contrastive datasets (0.96-0.98).
- **E10.07-K21** (reworded: the sources support less). Numbers are right (SHELDON 84.00 vs RLM 78.00, Codex 76.00), but SHELDON is a general scientific-reasoning harness (diagnosis, root-cause, ARC-AGI-2), EviDx has no dual search, and EviDx's baseline is its own single agent with gains clearest on multiple choice and open-ended diagnosis still limited. Corrected claim: SHELDON, a general dual-search (hypothesis and observation) harness, scores 84.00 on DiagnosisArena vs 78.00 for RLM and 76.00 for Codex; separately, EviDx's evidence scaffold with an observer harness improves multiple-choice diagnosis over its single-agent baseline (e.g. Qwen3-8B 18% to 44% on JAMA) while open-ended diagnosis stays limited.
- **E10.07-K22** (now single-source: only one opened source, code check).
- **E10.07-K27** (now single-source: only one opened source, code check).
