# A06.11 Case-based reasoning: cross-check critique

Checker re-opened the full text of ExpeL (2308.10144), Memento (2508.16153), ReasoningBank (2509.25140), Xiong et al. (2505.16067), AWM (2409.07429), Voyager (2305.16291), Sarukkai (2505.00234), Memp (2508.06433) and Loewenstein, Thompson, Gentner 1999. PDFs deleted after extraction.

## Confirmed (matched the paper text or table)
- ExpeL Table 3: ALFWorld ReAct 40.0, reasoning-similarity 48.5, random 42.5, ExpeL 59.0; HotpotQA ReAct 28.0, hand-crafted 32.0, with reflections 29.0, gpt-3.5 insights 32.0, ExpeL 39.0.
- Memento: GAIA 87.88 (Pass@3 validation), 79.40 test from the validation-built bank; no-CBR 78.65 to 84.47 and parametric 80.46 to 85.44 over five rounds; K table (K=0 59.9/72.2, K=4 64.5/78.5, K=32 63.9/78.1).
- ReasoningBank WebArena overall (Gemini flash): 40.5 / 42.1 / 44.1 / 48.8 / 51.8; judge accuracy 72.7%.
- Xiong Table: fixed / add-all / strict for all four agents, all as in a22.
- AWM 35.5 vs 23.5 (and 51.1% relative); Voyager top-1 80.2 +- 3.0, top-5 96.5 +- 0.3; Sarukkai 73 to 89, 55 to 64, 75 to 79, 0.93, AutoManual 0.79.
- Memp ALFWorld GPT-4o: 42.14 / 56.43 / 74.29 / 77.86; TravelPlanner hard-constraint 12.88 no memory, 6.72 random, 8.95 key=query, 8.25 key=AveFact.
- Loewenstein: 15/16 compromises, 3/16 principle; Exp 2 13/27 vs 5/31.

## Corrections made
1. a26 (Memento ablation) labels a column K=2 with 63.6/77.9. The table has K=1 at 63.6/77.9 and K=2 at 63.7/78.1. b07 and c02 are right. Claims use K=1.
2. a25 and a26 list the Memento first author as Wang. The paper is Zhou et al. (b07, c01 correct).
3. a10 says about 10 percent solve Duncker alone and about 85 percent with a hint. The second-hand text in Loewenstein 1999 gives 41% applying the solution spontaneously after the fortress story and around 85% after the hint. The 10% no-analog baseline was not in the opened page. Use 41% to 85% for the retrieval-failure effect. a10 stays opened:false for the originals.
4. a14 attaches "chi-square p < .005" to the contingency-contract rate (48% vs 16%). In the paper the chi-square (N = 45, p < .005) is for schema quality (63% vs 19% of dyads with schema rating above 1.0). The contract rate test is reported at p < .01.
5. c11 labels the ExpeL Reflexion rows 40.3 to 54.4 as "retrieve-only". In Table 2 the 40.3 to 54.4 row is ReAct+Reflexion; retrieve-only is 54.5 to 60.4; full ExpeL is 59.0 to 64.2 (a18 correct).
6. ExpeL text says reason-similarity retrieval "slightly drops"; the table gap is 10.5 points (59.0 to 48.5) and random is 16.5 below. Claim K04 uses the table.
7. b04 AveFact GPT-4o row (76.02 / 8.25) is identical to the Trajectory row in a different Memp table (76.02 / 8.25). Possibly the same configuration reported twice; not a conflict, but the two "key" results are not independent.

## Contradictions between sources
- Abstraction vs raw cases: AWM, ReasoningBank, Memp favour distilled units; ExpeL found retrieval-only (55) above insights-only (50) on ALFWorld; the independent ReasoningBank run reproduced AWM at +3.6, +0.9, -0.9 against AWM's own +12 (K09 contested).
- Judge noise: Xiong says a coarse judge hurts; ReasoningBank says 50 to 100% judge accuracy gives similar results (K07 contested). The ReasoningBank test is a simulation on one subset.
- Weak models: several papers show reuse failing for small or weak models; Evo-Memory says smaller models benefit most (K13).
- Memory and hard constraints (Memp) fell below no memory while soft scores rose. Other studies report only the headline metric.

## Weak spots
- Almost every LLM-CBR result is from the group that proposes the method. Independent re-runs exist only for AWM and Synapse (inside ReasoningBank).
- Single runs, no confidence intervals in ReasoningBank, Dynamic Cheatsheet (30-question AIME), CBR-RAG (32 questions, embedding cosine not factual accuracy), Memento K sweep (tuned on test data).
- Memento CBR margin shrinks with rounds and the no-CBR arm itself gains 5.8 points; Pass@3 is not single-shot.
- Table extraction by pdftotext scrambled some cells (Xiong deletion table, ExpeL Table 3 row order). Numbers used in claims were cross-checked on at least two lines.
- No test isolates "retrieve a subgoal solution" from "retrieve a whole task". Nearly all studies retrieve whole tasks or trajectories.
- No human experiment on case-based planning with a modern sample size; the human evidence (Gick and Holyoak, Gentner 1993, Ross 1984) was never opened in the original and is second-hand or unopened.

## Seen only in snippets or not opened
Aamodt and Plaza 1994 (not opened, a32, b30, c24); Gick and Holyoak 1980/83 originals (a10, b31); Gentner, Rattermann, Forbus 1993 (a11); Ross 1984 (b32); Hammond CHEF (c25) and Smyth and Keane 1998 (c26) from memory; Agent KB (a30, abstract and introduction only); Zeng et al. structural memory (a31, tables not read); CASCADE, Evo-Memory, DS-Agent, Buffer of Thoughts, Dynamic Cheatsheet, KATE, Gan et al., Yin and Leake, Yasunaga were not re-opened by the checker (opened by earlier agents, numbers not re-verified). The 2025 review (b29, c07) has no new measurements.

## GAPS (most decision-relevant first)
1. Does a library of solved subgoals (not whole tasks) retrieved by similarity beat no library at equal tokens on reasoning benchmarks (math, ARC-like, code)? No paper tests subgoal-level reuse.
2. Which retrieval key works best for subgoals: problem text, plan, or abstract relation description? Only ExpeL tests keys (task vs reasoning step), on one benchmark.
3. What is the size of experience-following harm when stored cases are wrong at 10 to 50 percent, and does code-verified admission remove it? Xiong and ReasoningBank disagree on judge noise.
4. Do distilled strategies beat raw solved cases when run by someone other than the method's authors? Only one independent AWM re-run exists, with mixed signs.
5. How many retrieved cases at equal total tokens, and does the optimum shift with model size? Memento tuned K on test data; others vary little.
6. Does retrieval help or hurt when the new problem is dissimilar to every stored case? Is a similarity threshold gate (skip lookup) better than always retrieving? Evo-Memory only gives a correlation across few datasets.
7. Do original human studies (Gick and Holyoak 1980/83, Gentner 1993, Ross 1984) replicate with exact numbers, and did large replications (for example Many Labs style analogy studies) shrink the 85 percent hinted effect?
8. Does adaptation-guided retrieval (retrieve by cost to adapt, Smyth and Keane 1998; later case-base maintenance work) beat nearest-neighbour similarity for LLM agents?
9. Does revising a retrieved case from real failing output beat copying it, outside DS-Agent's Kaggle setting? Only one ablation (rank 2.08 vs 2.58 vs 3.41).
10. Do memory gains survive removing test contamination and templated tasks (ALFWorld) when measured on fresh, structurally different problems?

## Gap search results (evidence_d.jsonl d01-d18; claims K22-K28 added, K01 K04 K05 K07 K08 K09 K12 K15 updated)

Search tools: WebSearch budget was used up. arXiv, Semantic Scholar and OpenAlex search APIs were rate-limited (shared IP), so papers were found by known arXiv id and by Europe PMC and Crossref. Full texts opened via arxiv.org PDF and Europe PMC XML. Not opened (paywalled or blocked): the original Gick and Holyoak 1980/83, Gentner et al. 1993, Ross 1984, Smyth and Keane 1998 (sciencedirect returned 403; not worked around).

1. Subgoal library vs no library: PARTLY CLOSED. LEGO-Prover (50.4 vs 47.1, miniF2F) and ReGAL (helpers vs whole retrieved programs, +11.5 on LOGO) test sub-task reuse with verification. Neither matches tokens or compute, and neither is math word problems, ARC or general code. K22. Equal-token test still open.
2. Retrieval key: PARTLY CLOSED. Skill-KNN (abstract skill description beats raw text, 78.3 vs 74.6 Spider) and EPR (usefulness-trained beats similarity, 31.9 vs 26.0 BREAK) point the same way. Semantic parsing only; subgoals untested. K23, K04 upgraded to established.
3. Harm from wrong cases: STILL OPEN as a dose-response. New: Evo-Memory all-failures-stored (ExpRAG ALFWorld 0.59 to 0.25), MINJA and AgentPoison (poison is cheap), GSM-IC and Power of Noise (near-miss context hurts). No 10/30/50 percent curve. K07 stays contested.
4. Distilled vs raw by others: NO INDEPENDENT WIN. Evo-Memory's re-implementation puts AWM at the History level (0.30/0.53) below raw ExpRAG (0.46/0.63); Dynamic Cheatsheet's raw-retrieval arm sometimes falls below its memory-free arm. Caveat: Evo-Memory ported AWM itself. K09 stays contested.
5. Best K at equal tokens, model-size shift: STILL OPEN. Only Many-shot ICL (verified examples plateau near 25, unfiltered peak near 125 then fall) and Mallen (gate helps only above 10B parameters). K26 single-source.
6. Dissimilar items and a similarity gate: PARTLY CLOSED by analogy. Mallen shows a gate beats always-retrieve for large models; Evo-Memory BabyAI shows memory below baseline. No test of a similarity-threshold gate on case lookup. K25 single-source.
7. Human studies: PARTLY CLOSED. Originals not opened. Two 2026 papers: Geneva retrieval-gap (Exp 1 surface wins, d=0.84; Exp 2 structure wins when cue is a familiar relational category, d=0.82) and a Barcelona Fortress-to-Radiation re-run (5% spontaneous, 36% hinted with one story; 63% spontaneous after inventing an analogous story). The 41 and 85 percent figures were not reproduced, but the design differs, so it is not a failed replication. K01 now contested; K27 added. No Many-Labs-scale replication found.
8. Adaptation-guided retrieval: STILL OPEN. Smyth and Keane not opened. EPR is the nearest tested idea (retrieve by usefulness).
9. Revise vs copy: STILL OPEN. DS-Agent re-read: the ablation removes feedback re-ranking and adjustment as a bundle, one setting. K15 stays single-source.
10. Contamination and templated tasks: STILL OPEN. Evidence is circumstantial: gains concentrate on Game of 24 (PAL alone 64.0 vs BoT 82.4), ALFWorld and PDDL, correlate with task similarity (r=0.717 and 0.563), and vanish or turn negative on BabyAI. No paper removes contamination. K28.

Remaining corrections: d02's source line does not name authors (not captured from the page). Evo-Memory tables were scrambled in text extraction; only cleanly parsed Gemini 2.5 Flash rows are quoted.
