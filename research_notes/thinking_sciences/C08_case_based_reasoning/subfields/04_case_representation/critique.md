# C08.04 Case representation: cross-check and critique

## Numbers re-opened this session (full text via pdftotext, arXiv PDFs)
Confirmed exactly:
1. Memento K table (K=0 59.9/72.2; K=1 63.6/77.9; K=4 64.5/78.5; K=32 63.9/78.1) and learning curve (no CBR 78.65 to 84.47; parametric 80.46 to 85.44). GAIA 87.88 val, 79.40 test. Component ablation (tools alone -18.0 F1 / -2.1 PM; planning +29.1 / +11.5; CBR +6.7 / +8.2) confirmed in text.
2. ReasoningBank WebArena overall: no memory 40.5, AWM 44.1, ReasoningBank 48.8, +MaTTS 51.8; Shopping 39.0 / 44.4 (AWM) / 49.7; judge accuracy 72.7%; MaTTS parallel 49.7 to 55.1.
3. ExpeL: insights vs retrieval-only 36/31 (HotpotQA), 50/55 (ALFWorld), 37/38 (WebShop). ALFWorld ablation table rows read ReAct 40.0, reasoning-similarity 48.5, random 42.5, ExpeL 59.0 (label mapping now confirmed from row order).
4. AWM: 23.5 to 35.5 on WebArena (+12.0 abs, +51.1% rel), 24.6% Mind2Web, AWM3.5 39.0/34.6 vs Synapse3.5 34.0/30.6; margin 8.9 to 14.0.
5. Dynamic Cheatsheet: Sonnet AIME 2024 23.3 to 50.0; AIME 2025 6.7 to 36.7; full-history 26.7; GPT-4o 20.0 to 40.0 (full-history 13.3); GPQA 59.6 / 63.6 / 68.7; Haiku 10.0 to 36.7.
6. Xiong et al.: fixed vs add-all vs strict (RegAgent 67.53 / 55.48 / 70.95; EHRAgent 16.75 / 13.05 / 38.50; AgentDriver 40.11 / 32.32 / 51.00; CIC-IoT 71.50 / 59.90 / 85.40).
7. CBR-RAG: 0.9141 vs No-RAG 0.8967; 1.94% gain; 2,124 pairs, 1,183 (57%) with no act reference.
8. Sarukkai: ALFWorld 0.73 to 0.89 (0.91 with DB curation per table; 0.93 in text with curation; see below), SQL 0.75 to 0.79, Wordcraft 0.55 to 0.64.

Corrections and small discrepancies:
- Sarukkai: evidence b13 says database curation lifts ALFWorld 0.89 to 0.91; c25 says 0.93 with curation. Both appear in the paper (0.91 is a table row, 0.93 is the best curated variant in the text). Cite as "0.91 to 0.93 depending on curation variant".
- Xiong: EHRAgent strict is 38.50 in the main table but 38.67 in the deletion table. Use 38.50 for the main comparison; the difference is a rounding or rerun artefact.
- ReasoningBank: Shopping score 49.7 is also the "k=1 retrieved item" score, so the "1 item best" and "full ReasoningBank" figures are the same cell, not two results.
- ExpeL HotpotQA ablation: row-to-value mapping in the pdf text is ambiguous (28.0, 29.0, 32.0, 32.0, 39.0 across five labels). Only ReAct 28.0 and ExpeL 39.0 are certain. Do not quote the hand-crafted vs reflections values.
- Evidence a14/b01/c20 (and a22/b22/c19) are duplicate reads of the same papers, so Memento, ReasoningBank, ExpeL, AWM, DS-Agent, Xiong and CBR-RAG count as one independent source each in claims.

Not re-opened (rely on the original agent's reading): Aha et al. 1991 table, Kolodner 1993, Aamodt and Plaza 1994, TextBFGS, Springdrift, CBR-to-SQL, DomAgent, Hu et al. leave-square-out, Zeng structural memory, Evo-Memory, Agent KB, Buffer of Thoughts.

## Contradictions between sources
- Abstract vs concrete: AWM, ReasoningBank, Dynamic Cheatsheet favour abstraction; ExpeL ALFWorld and DS-Agent favour concrete runnable cases. Task type (action-set heavy vs knowledge heavy) probably decides. Unresolved.
- Outcome label accuracy: ReasoningBank tolerates 50 to 90% judge accuracy; Xiong shows coarse judges give flat or falling curves. Different agents, different baselines.
- Failures: ReasoningBank says they help only with strategy-level distillation; ExpeL says failure/success pairs drive insights. Compatible, not contradictory.
- Value of memory itself: Memento shows the gap to no-CBR nearly closes by pass five; ReasoningBank shows memory worth +8 points. Different benchmarks and baselines.

## Weak spots
- Almost all results are single runs on one benchmark with no variance (exceptions: ExpeL standard errors, Sarukkai 3 seeds). WebArena effects of 2 to 4 points are within plausible noise.
- Test sets are small in several cases (CBR-RAG 32 queries; TextBFGS HumanEval-Hard about 45 items).
- No LLM study ablates individual case fields. Claim K20 records this.
- The original CBR founding studies (Kolodner, Aamodt-Plaza) are conceptual reviews with no human or machine experiments with numbers; the only classic numeric base is Aha et al. 1991 on attribute-vector data.
- Review papers (Hatalis 2025, Watson 2024, Feng 2023) report no measurements; treated only as definitions.
- Springdrift's evaluation is synthetic with keyword-overlap ground truth that favours the lexical signal.
- Frontier-model results (Claude, GPT-4.1) are mixed with older models (gpt-3.5, GPT-4o); transfer to our setting is uncertain.

## Seen only in snippets or garbled extracts
ExpeL HotpotQA ablation rows, DS-Agent Figure 6a and Table 2 values (figures, not text), Memento component details beyond those confirmed, Hu et al. Figure 7.

## GAPS
1. Which case field earns its tokens? Field-level ablations (problem, solution, outcome, explanation, context) in an LLM agent at equal tokens: none found.
2. Abstract lesson vs concrete worked example vs both: what task features decide, and does a combined record beat either?
3. Does case memory still add value once the agent gets equal-token retries or best-of-N without memory? (Memento's curve nearly converges; ReasoningBank best-of-N without memory gains only 39.0 to 42.2.)
4. How noisy can outcome labels be before memory hurts, measured with injected noise on a single benchmark with variance?
5. What retrieval key (task wording, error type, abstract structure) generalises across domains, tested on larger benchmarks than HumanEval-Hard?
6. Do wrong or misleading cases cause measurable harm with current frontier models (experience-following at modern scale), and what mitigations work?
7. Optimal bank size and eviction rule over long horizons (beyond 5 passes, beyond 3k items), with utility counts as in IB3?
8. Do case-based memory results transfer to reasoning puzzles (ARC, brainteasers) where problems rarely repeat, versus web and QA tasks where they often do?
9. How does memory benefit scale with model size (small models fail to use stored methods; large models may ignore them)?


## Gap search results (evidence_d.jsonl, d01 to d17; claims K22 to K31 added)
Search note: WebSearch quota ran out and the arXiv, Semantic Scholar and OpenAlex APIs returned rate-limit errors, so sources were found from known titles and opened as full PDFs (Xiong, MINJA, AgentPoison, Evo-Memory, Agent KB, ACE, Training-Free GRPO, Memp, CER, ReasoningBank appendix, DeMem). No ARC-specific memory paper was found.

1. Which case field earns its tokens: STILL OPEN. Closest are content-type ablations (CER dynamics vs skills: 37.7 full, 33.3 without skills, 35.1 without dynamics; Agent KB stage ablations). No problem/solution/outcome/explanation ablation (K21, K30).
2. Abstract vs concrete vs both: PARTLY CLOSED. Memp (GPT-4o ALFWorld test 56.43 script, 74.29 trajectory, 77.86 both) says both is best; script generalises, trajectory fits repeated tasks. Exception: Claude on TravelPlanner. Evo-Memory finds raw-experience retrieval competitive with abstract methods (K22, K04).
3. Memory vs equal-token retries: STILL OPEN, with a lean. CER shows sampling and memory are complementary (43.1 / 37.7 / 52.6), but sampling used more tokens. No equal-token test (K25).
4. Label noise: PARTLY CLOSED, contested. ACE gives a dose-response (harmful update every 5 steps still +5.4 over base; every step -4.0) and ReasoningBank is flat down to 50 percent judge accuracy, but both are single runs without variance. Xiong shows coarse judges lose to a frozen bank for raw-trajectory demos. Format appears to decide (K24).
5. Retrieval key across domains: STILL OPEN. Memp shows keys change results by 1 to 4 points and random items already help; one benchmark only (K23).
6. Harm from misleading cases at frontier scale: PARTLY CLOSED. Experience-following is confirmed (Xiong; MINJA above 95 percent injection with GPT-4/GPT-4o; AgentPoison about 80 percent attack success). Not tested on current frontier models. Measured mitigations: strict admission, utility deletion, merge and dedupe (K07 now established; K28).
7. Bank size and eviction: STILL OPEN. Small banks work (100 to 500); utility eviction helps only with reliable outcomes; nothing beyond about 4k items or 5 passes (K31).
8. Puzzle tasks: PARTLY CLOSED by indirect evidence. Evo-Memory gain tracks task similarity (r 0.56 to 0.72) and is small on AIME-25 and GPQA; Training-Free GRPO gives +2.7 and +5.4 on AIME for a 671B model. No ARC or brainteaser memory study found (K26).
9. Scaling with model size: PARTLY CLOSED, contested. Gains do not rise with model strength (ReasoningBank +8.3/+7.2/+4.6) and smaller models benefit most (Evo-Memory), but a 32B reasoning model lost (Training-Free GRPO) and strong-model memory helped a 14B model (Memp). K27 added; K19 now contested.

Caveats on the new evidence: single runs unless stated. Xiong Table 2 and Evo-Memory tables are garbled in text extraction, so only readable cells or prose figures are quoted. ReasoningBank judge-noise values are read from a plot.
