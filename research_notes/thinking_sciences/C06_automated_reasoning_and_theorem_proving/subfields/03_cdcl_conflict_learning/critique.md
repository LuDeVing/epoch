# Critique and cross-check: CDCL and no-goods (C06.03)

Cross-checker pass, 2026-10-26. Evidence files a, b, c re-read in full. Ten key numbers re-opened in the source PDFs (copies deleted from D:/research_scratch/C06.03 afterwards). Claims are in claims.jsonl (K01 to K21; K22 to K24 were never written, see the recovery note in 00_audit). 

## Numbers re-checked

Confirmed exactly:
- Katebi et al. 2011 ablation (a13, b01, c04): full 9068, no learning 4837, no VSIDS 6932, no 2WL 8409, no restarts 8653, of 10,000, 1000 s limit. Per-family sverif (592 vs 420 of 500), plan (327 vs 1006 of 1200), atpg (965 vs 1000 of 1000) also match.
- Bayardo and Schrag 1997 hanoi4 (a03, c01): fail rates 100% naive, 94% sizesat(3), 92% sizesat(4), 79% relsat(3), 13% relsat(4). Table 6 ssa2670-141 (a02): sizesat(3) 23%, sizesat(4) 0%, relsat(3) 4%, relsat(4) 0%.
- Glucose (a16, b09): 176, PicoSat 153, RSat 139, MiniSat 132 of 234 solved; fastest on 68.
- Pipatsrisawat and Darwiche (a22): UNSAT solved 402 / 433 / 438; 647 vs 740 when the empowerment check is skipped; 34% less time.
- Rintanen 2010 (b17): column order is VSIDS, new heuristic, LAMA, Precosat, RSAT = 701, 757, 775, 610, 653 of 968. The column mapping that b17 flagged as uncertain is now confirmed.
- Biere and Frohlich (b14, b15): interval totals 122 to 168, EMA 178 and 181. Confirmed.
- Reflexion (b18, b19): 91% vs 80% HumanEval, 22% / 20% / 11% headline, Rust 52% (no tests) vs 60% baseline vs 68% full, MBPP 0.80 vs 0.77, false-positive rate 16.3% vs 1.4%, self-reflection +8% over episodic-memory only. Confirmed.
- Sentry (b21, c21): 0.335 to 0.391, 0.562 to 0.643, 0.364 to 0.296, 0.651 to 0.599, 0.468 WebShop full, 81.7% of 939, 37% average and up to 77% over the best runtime baseline. Confirmed. The 0.264 "Wink" baseline value was not located in the text. 0.468/0.264 = 1.77 matches the "up to 77%" claim, but the label stays unverified.

Corrections made:
1. b20 (Huang et al.), oracle numbers were mis-mapped. Table 2 reads: GPT-3.5 GSM8K 75.9 to 84.3 with oracle, CommonsenseQA 75.8 to 89.7, HotpotQA 26.0 to 29.0. GPT-4 GSM8K 95.5 to 97.5, CSQA 82.0 to 85.5, HotpotQA 49.0 to 59.0. b20 said GPT-3.5 GSM8K 95.5 and GPT-3.5 HotpotQA 49.0 with oracle; those are GPT-4 baseline values. c19 had the right mapping. The no-oracle numbers in b20 are correct (GPT-3.5 CSQA 75.8 to 38.1 (3 calls) to 41.8 (5 calls); GSM8K 75.9 to 74.7; GPT-4 GSM8K 95.5 to 91.5 to 89.0).
2. a02: "cbjsat 23" is a garbled table read. In Table 6 the cbjsat row cells are blank in the text extraction; the 23% belongs to sizesat(3). So the claim "plain CBJ still failed in some runs" on ssa2670-141 is not supported by the extracted numbers (the text says the cbjsat time is high; fail rate not readable). Do not cite a cbjsat fail rate.
3. a14: "crypto: no learning 472 vs full CDCL 237" cannot be right as a solved count, because the family has 300 versions. The extracted rows are interleaved and appear to mix two families (crypto and another). Treat as unreliable. The sverif, plan and atpg rows are clean and are used instead (claim K06).
4. b23 attributes "w/o soft repair WebShop 0.136 (-70.9%)". In the Sentry intro, appendix and arithmetic (70.9 and 38.5 average to the stated 54.7), the 0.136 / -70.9% row is the "w/o intervention-need check" ablation. The main table text extraction shifted row labels. c22 has both attributions. Use: removing the need check gives 0.136 on WebShop (-70.9%). Soft-repair removal figure is not reliably readable.
5. c01: "best variant fails 1%" in hanoi4. The last row of Table 7 has no label in the extraction (183 s, 0.89 M assignments, 1%). Probably a further relsat variant, not shown in a03. Not used in claims.
6. a22 vs summary: "+36" is Rsat++ over Rsat (438 vs 402). Rsat+ alone is +31.
7. a15 says negative slope on 167 of 199; b10 says 92% (about 183 of 199). These disagree; the first is the paper's count in the extraction, b10's 92% is probably a different cut or a rounding of another statistic. Use 167/199 and flag.

## Contradictions and tensions between sources

- Learning matters most (Katebi) vs. learning loses in some families (Katebi's own per-family rows, Bayardo's 3bit and random 3SAT). Resolved by family type: it wins on structured instances with short derived no-goods.
- Chaff authors credit engineering, not learning; Katebi ranks learning first. Not contradictory: learning is necessary, engineering made it affordable.
- Restarts: Elffers says frequent restarts add real power on some families and Glucose adaptive restarts can fail badly; Biere finds EMA-adaptive best on a competition set. Different benchmark classes (crafted vs competition). Open.
- LRB over VSIDS did not replicate on crafted unsat families (Elffers, b13) though it was tuned on industrial ones.
- Free-text lessons: Reflexion gains vs Huang losses are consistent once the oracle is considered, but Reflexion's ALFWorld retry trigger is a hand-written heuristic, and Sentry says lessons in permanent context can hurt. Reflexion keeps only the last 1 to 3 reflections, which partly acts as relevance bounding.
- Core feedback: Sarkar shows no accuracy gain over generic errors (p=1.0) yet a big drop in fabrication; Salla shows a modest consistency gain. Marked contested.

## Weak spots

- All LLM-agent evidence on failure memory is from 2023 to 2026 preprints, mostly the authors' own benchmarks. Sentry, CausalFlow, Sarkar, Salla, TIDE are single groups with small samples (14 infeasible items in Sarkar; 50+50 tasks in Sentry held-out).
- No source measures an LLM agent with formal no-goods (a conflict set of variable assignments, subsumption, backjumping). Reflexion-type memories are free text and not implied by the failure the way a learned clause is implied by the formula.
- Katebi counts are instance-level, one solver (MiniSat), one benchmark mix, with only 71% of averages within 25% at 90% confidence. Duplicates a13, b01, c04 are one source.
- Bayardo and Schrag explanation (synergy of look-ahead with learning) is a conjecture, untested.
- Theory results (K10) are about idealised solvers and do not give agent-level predictions.

## Seen only in snippets or partially (not to be cited as read)

- c08 (Elffers, title page only; a24 and b11 did read the paper), c25 and b25 AgentDebug (abstract page only; numbers +24%, +17%, 26% relative are unverified), c26 (SciAgentGym, LLM-WikiRace, Robotouille: snippets), c27 (Drescher and Walsh, Dechter: titles only), a25 (Reflexion early pass; b18, b19 read the full text).
- b26 is a search record, not a source.
- Not opened this session: Pipatsrisawat and Darwiche 2011 (restarts equal general resolution), Dechter dead-end learning, Frost and Dechter 1994, ASP lazy nogood generation, planning nogoods (GraphPlan memoization).

## GAPS

1. Does a formal no-good store (short conflict sets, checked in code, with subsumption) cut repeated failed attempts of an LLM agent at equal tokens, relative to free-text reflection and to no memory? No source tests this (K24).
2. What counts as a "conflict" for a language task, and can code derive the minimal responsible subset of choices (the analogue of the first-UIP clause) from a failed trace? CausalFlow gives only a first step (42.7% repair, worse than Self-Refine on MBPP).
3. How many no-goods should an agent keep, and with which relevance rule? Evidence is from SAT (relevance-bounded, LBD); nothing tells us the right list size for prompts, where long lists hurt (Sentry k=3 / k=10 cost 4.5% / 6.2% vs k=5).
4. When does a stored lesson harm? Sentry says always-in-context lessons lower scores; the trigger-matched retrieval needed for a no-good store has not been replicated outside one group and one small model. Does this hold for a frontier model?
5. What is the restart analogue (cutoff length, share of lessons carried over) for LLM attempts, and does the heavy-tail argument of Gomes et al. hold for LLM run lengths and success? No measurement found.
6. Is non-chronological backjumping (revisiting the earlier choice that caused the failure rather than the latest one) worth its overhead for an LLM agent, or does simple retry with a lesson capture most of the gain?
7. How reliable must the failure signal be? Reflexion collapses on MBPP with 16.3% false-positive tests; what false-positive rate makes a no-good store harmful, since a wrong no-good prunes the true answer (SAT clauses are sound, lessons are not)?
8. Is there a published planning or CSP result (GraphPlan memoization, nogoods in ASP) with numbers comparable to Bayardo's, that can fix the size of the effect outside SAT? Not opened this session.
9. Which task families have "short, easily derived no-goods" (Bayardo's boundary condition) among our benchmarks (ARC, puzzles)? A gate for G12 depends on a cheap test for this.
10. Do LLM-reported conflicts and branches track real difficulty? Zhang et al. found self-reported counts did not track CDCL hardness, so any difficulty signal must come from code.


## Gap search results (2026-10-26)

Tools note: WebSearch quota was used up; the arXiv, Semantic Scholar and OpenAlex APIs returned 429. Direct PDF downloads from arxiv.org/pdf, jair.org and cornell.edu worked. Evidence is in evidence_d.jsonl (d01 to d15, all opened). Claims K25 to K35 are in claims.jsonl. The 24 claims K01 to K24 were not on disk, so the file holds only the new ones (see the NOTE row). The ASP/clasp (IJCAI-07) and Katsirelos-Bacchus sources were not reached.

Closed or mostly closed:
- Gap 8 (numbers outside SAT): closed. Kambhampati 2000 gives 1.6x to 120x for EBL/DDB in Graphplan, up to 1000x in the abstract (d01, d02, K25).
- Gap 9 (which families have short no-goods): mostly closed as a test. Speedup tracks how much explanation shortens the memo; blocks world (goals interact) gave 1.6x, rocket, gripper and logistics far more. Cheap test: ratio of derived reason size to state size (K25). Not yet tried on ARC or puzzles.
- Gap 4 (harm from lessons on stronger models): mostly closed. DeepSeek-V3.2-Exp lost 9 to 29 points with two memory baselines; GPT-4.1 fell 2.9 points with top-3 retrieval; a gated store kept the baseline (d11, d13, K29). Reported by few groups, no confidence intervals.
- Gap 7 (how reliable must the signal be): partly closed. Simulated mistake finders show a break-even near 60 to 70% accuracy (d09, K28). No direct measure for a no-good store.

Partly answered:
- Gap 5 (restart analogue): fresh restarts gain log-linearly with a verifier (d06), and Gomes shows the heavy-tail condition plus a counter-instance (d04, d05). Nobody has measured heavy tails or lesson carry-over for LLM attempts. Open.
- Gap 6 (backjumping): Tyen shows the culprit step doubles the fix rate over a random cut, but LLMs cannot find it, and there is no test against plain retry at equal tokens (d08, K27). Open in the form asked.
- Gap 2 (conflict derivation): Olausson shows diagnosis quality is the bottleneck (GPT-4 feedback 33.30% repair success vs human 52.60%) (d07). No code-derived minimal conflict set for language tasks found. Open.
- Gap 3 (list size and relevance rule): match quality beats fixed k (d13); batching and merging shrink stores (d12). No number for list size. Open.

Still open:
- Gap 1: no source tests a formal no-good store against free-text lessons and against resampling at equal tokens (K35). Indirect evidence says free-text reflection barely beats resampling (K26).
- Gap 10: not searched further this pass; the earlier Zhang et al. finding stands.
