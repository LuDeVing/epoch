# Critique, C05.08 Hierarchical task networks (cross-check)

## Sources re-opened (this session, full text)
ADaPT (2311.05772), Least-to-Most (2205.10625), Meneguzzi 2026 (2605.07707), Puerta-Merino 2025 (2501.08068), HyperTree Planning (2505.02322), Aghzal 2026 (2603.14248), TDAG (2402.10178), Decomposed Prompting (2210.02406), SHOP2 (JAIR 2003).

## Confirmed
- ADaPT ALFWorld ReAct 43.3, P&E 43.3, ADaPT 71.6; Pick2 11.8 vs 52.9; WebShop P&E 17.0 vs ReAct 32.0; TextCraft depth 2 26.9 to 78.2; weak executor 3.3 to 41.7 (a20-a22, b13-b14, c10-c12).
- Least-to-Most SCAN 16.7/16.2/99.7; last-letter L=12 74.0; GSM8K 60.97 to 62.39; 5+ steps 39.07 to 45.23 (a14-a16).
- Meneguzzi: 780 candidates, 419 passed, 347 viable, 72 broke, 60 of 72 (83%) wrong state type; coverage 131/139 vs 134/118/117/113; LLM wins nodes on 104 of 125 (b25, b26, c06, c07).
- HTP: Gemini TravelPlanner 36.1 vs EvoAgent 8.9; GPT-4o 20.0 vs CoT 4.4; Blocksworld 54.7 vs 35.5; Mystery 8.7 vs 0.0; Trip 36.9 vs 15.6; GPT-3.5 HTP 1.7 (a30, c15).
- Aghzal: 60.6 vs 67.7 perfect match; unmatched 29.4 vs 15.4; 38.5 plan completion, 36.4 final success; 29.2 and 17.3 for other executors (b27, c24).
- TDAG: TextCraft 73.5, WebShop 64.5/45.0, cascading failure 32.61 / 19.57 / 4.35 (c13, c14).
- Decomposed Prompting: MultiArith 78 to 95, GSM8K 36 to 50.6 (a18).
- SHOP2: 899 of 904, TLPlan 894, TALPlanner 610 (a09).

## Corrections and discrepancies
1. GSM8K chain-of-thought baseline: Least-to-Most text says 60.97, its own table says 60.87 (c17 used 60.87, a16/b18 used 60.97). Source is internally inconsistent; use "about 61". Gain 1.4 to 1.5 points either way.
2. Puerta-Merino correct plans: abstract says 3%, body says 4% (13% of feasible). b24 reports 3%, c08 reports 4%. Both quote the paper. Use "3-4%". Correct decompositions: zero. c08's "3% feasible decompositions correct" is garbled; the paper's text says "3% correct" in the feasible-decomposition sentence, so treat as unclear.
3. Aghzal c24 lists "NL steps over-decomposed 29.5%" and "unmatched 29.4%" as two figures; the paper's table has Decomposed 29.5 and Unmatched 29.4 as separate rows, so they are not a double count but they sum with perfect match (60.6) to over 100 (119.5%) unless the categories overlap. Treat the breakdown as non-exclusive. The "36.4% final success" is one executor (gpt-5-nano) with human plans, not an average.
4. Meneguzzi "27 times" spread is derived (Opus 4 median 1,878 vs about 51,200), not stated in a sentence I found. Treat as a calculation by the extractor.
5. HTP baselines: the best Gemini baseline is 8.9 (EvoAgent); "3.6 times o1-preview" is an abstract claim not re-checked.
6. a25 says "Mystery Blocksworld results sit in single digits to 14%" while b21 gives 4.3% and 2% for GPT-4; a26 gives 52.8% for o1-preview. Different models; not a conflict, but a25 range is loose.
7. Dating: ADaPT is 2023 on arXiv, NAACL Findings 2024; both years appear and are the same paper. TDAG year 2025 (journal) vs arXiv 2024.

## Contradictions and tensions between sources
- Plan-and-execute is much worse than ReAct on WebShop (17 vs 32) but better on TextCraft (27 vs 19). The "static plans hurt" claim is not universal.
- Decomposition gain: huge on synthetic tasks (SCAN, Hanoi-like, last letters), small on natural ones (GSM8K +1.4, open-domain QA smaller than synthetic). The big wins are on tasks built to be decomposable.
- ChatHTN says LLM-made methods break hand-made guarantees; Voyager and Agent Workflow Memory say learned methods help. Difference: ChatHTN verifies effects; AWM does not and reports 18.5% of tasks where the agent ignores new actions.
- Illusion of Thinking (given-algorithm still fails) vs Least-to-Most (given decomposition succeeds): different mechanism (long execution vs short chain); also disputed on output length.

## Weak spots
- Almost all HTN-LLM results are demos: ChatHTN has no success rates; the online-learning paper has 10 problems per domain, bar plots only, neither setting at 100%.
- Most ADaPT, TDAG, HTP gains use the authors' own baselines on older models (GPT-3.5, GPT-4o). No test on current frontier models at equal tokens. ADaPT claims comparable LLM-call counts, not equal tokens.
- No study isolates "method library given" vs "model invents decomposition" at equal compute on natural tasks.
- Planning evidence is dominated by Blocksworld/logistics; little on open-ended reasoning, which is what our agent does.
- Single-group dependence: ChatHTN, Xu and Munoz-Avila, same lab (1 independent source).
- The 1994 expressivity critique (b04) was seen only in a snippet; not opened.
- Valmeekam, Kambhampati position paper reuse each other's numbers: not independent.

## Only seen in snippets or garbled tables
b04 (Wikipedia talk snippet). ChatHTN Table 2 checkmarks garbled (c02). PlanBench replanning rows garbled (c19). LLM+P table mapping garbled (c26). Decomposed Prompting QA numbers read from figures (c18, a19). Alford 2015 read from first page only (c30). Xu and Munoz-Avila results figure-only (b10, b12, c04).

## GAPS
1. Does an explicit method library (given templates) beat model-improvised decomposition at equal tokens on a natural reasoning task set, not Blocksworld or synthetic tasks?
2. What is the cost of per-decomposition verification in tokens, and at what error rate does verification pay for itself?
3. How should the depth and node budget be set; does ADaPT-style gating on a failed check hold with current frontier models, or has the gain vanished as executors improved?
4. How often does a model confabulate a decomposition for an impossible or ill-posed task, and does a no-valid-decomposition exit reduce wrong answers without raising refusals?
5. Does growing a method library from verified decompositions help on a task stream of a few hundred items (ChatHTN learner used 10 problems), and how does the library go stale or conflict (Hogg 2008 interaction effect)?
6. Which part of the gain is decomposition itself and which is answer extraction, format control or verification (Decomposed Prompting +17/+14 on arithmetic)? Needs ablations on current models.
7. Is the Lekavy and Navrat critique of the HTN-over-STRIPS expressivity result sound, and does it matter for choosing tasks over goals as O3 outputs?
8. Where does the planning-versus-execution bottleneck sit for non-web tasks: do leaf errors dominate (Aghzal, DecomP) in math, code and research questions too?
9. Do task-tree scaffolds (HyperTree) still add value over a reasoning model with long thinking at equal tokens (o1-style baselines)?
10. Does ordering of alternative methods (SHOP2 ordered alternatives, LLM-written method heuristics) matter more than the method set itself, and can model-written ordering rules be filtered by execution on training items?


## Gap search results (evidence_d.jsonl, d01-d22; claims K21-K28 added)

Search limits: the WebSearch quota ran out, and the arXiv, Semantic Scholar and OpenAlex APIs returned HTTP 429 for most calls. Sources were found by arXiv listing pages and known IDs, then full text was read with pdftotext. Everything cited below was opened.

### Closed or mostly closed
- **Gap 4 (impossible tasks): mostly closed for planning tasks.** Models rarely say a task has no valid plan: 32 of 360 unsolvable episodes (8.9%), best configuration 4 of 10, while only 1 of 1,440 solvable episodes was falsely declared impossible (d01). Frontier multimodal models refuse missing-information cases 19-65% of the time but contradictions 65-80% (GPT-5 40% vs 80%; Sonnet 4.5 19% vs 72%) (d06). Reasoning models think longer on missing-premise questions and abstain less than non-reasoning ones (d05). So a no-valid-decomposition exit is under-used, and the one study that counted false refusals found almost none. Still open: whether a built-in exit step cuts wrong answers on open-ended reasoning, and the false-refusal rate on ambiguous but solvable items. Claim K26.
- **Gap 6 (what part of the gain is decomposition): partly closed.** A subgoal-sketch step (Plan-and-Solve) did not beat plain CoT on four models after correction (GPT-4o 75.0 vs 77.5 vs direct 57.5; d02). No clean extraction-handler ablation on a current model was found, so the Decomposed Prompting +17/+14 stays unreplicated.

### Partly answered
- **Gap 1 (given library vs improvised):** SkillsBench is the closest test. Curated skills 50.5% vs 33.9% none (+16.6, 87 tasks, 18 configurations); self-written skills were 8.1-11.5 points below none (d12, d13). Skills are agent packages, tokens were not equalised, and the tasks are terminal tasks, not pure reasoning. Equal-token test on natural reasoning items is still missing (K21, K22).
- **Gap 2 (verification cost):** an LLM critic cost 1.8x ReAct's tokens with no gain and raised timeouts to 15.0% from 0.6% (d04); Tree of Thoughts cost about 22x direct with no corrected gain (d02). Execution-based checks did pay: ASI verified induction 36.4-40.1 vs 32.6 unverified, with 84% of induction attempts rejected (d15). A break-even error rate was not computed by any source; with the numbers above a mechanical check pays when it costs a fraction of one extra model call. A weak check (no exception means verified) let broken skills in (d17) (K24, K25).
- **Gap 3 (budget and gating):** ADaPT on TextCraft with newer backends: GPT-4o 0.58, Mistral Small 3 0.58, GPT-3.5 0.52, GPT-4o mini 0.43, R1-distill-32B 0.13, Claude-3 Haiku 0.00 (d08). ReAcTree reverses for a 7B model without examples (2% vs 7%, d10). So the gain does not vanish for GPT-4o-class models but depends on the executor, and no source tests Claude 4 or GPT-5 class models against a plain agent. Depth and node budget settings were not studied. Open. (K27)
- **Gap 5 (growing a library):** ASI and SkillWeaver show gains over a stream of about 160 practice iterations (+31.8% relative on WebArena, d16) and ReAcTree shows +13 to +30 points from retrieved successful subgoal examples (d22). Nothing measured staleness or conflicts over hundreds of items. SkillsBench points to conflict risk: 4 or more skills per task gain +10.1 vs +19.0 for 2-3 (d14). Hogg 2008 interaction effect still comes only from the ChatHTN authors' note. Open.
- **Gap 8 (leaf vs planning errors outside web):** illegal steps (precondition violations) make up 89% of failed plans in toy planning (d03), and whole-plan critique helps far more than step-wise reflection (d07). That supports the leaf-error view for planning. Math, code and research questions were not found. Open for those.
- **Gap 9 (task tree vs long thinking):** HTP on GPT-4o beat o1-preview on TravelPlanner (20.0 vs 10.0) and Trip planning (36.9 vs 31.1) at 8.7-13% of the cost, but lost Blocksworld (54.8 vs 97.8) (d18). No current reasoning model and no equal-token test. Open at frontier level. (K28)
- **Gap 10 (ordering vs set):** ReAcTree shows that having a fallback path is worth 10-22 GSR points (sequence-only 36 vs 58 for LLaMA 70B; d11). Alford 2009 shows partial methods with the planner choosing the order still speed search by orders of magnitude (d19). SkillsBench shows set size matters (d14). No study varies order inside a fixed set, and nothing filters model-written ordering rules by execution on training items beyond Meneguzzi (c06). Open. (K23)

### Not closed
- **Gap 7 (Lekavy and Navrat critique):** the paper text was not found. The current Wikipedia HTN article does not mention it (d20). Alford, Kuter, Nau 2009 shows restricted HTNs compile to PDDL (d19), which weakens the practical weight of the expressivity claim for a bounded scaffold. Whether the critique is sound is unresolved. K02 stays contested.

### Cautions on the new evidence
- Much of it uses open-weight or 2024 models (ReAcTree, SCOPE, HTP) or terminal agent skill packages (SkillsBench), not method libraries in the HTN sense.
- APB and Miro-Lopez use LLM judges or small benchmarks (50 tasks, one run each).
- The Missing-Premise table was garbled by text extraction, so per-model abstain figures are ranges.
- The Lawsen comment gives no exact table (d21).
