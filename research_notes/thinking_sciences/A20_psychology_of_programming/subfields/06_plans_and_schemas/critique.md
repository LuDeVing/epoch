# Cross-check critique, A20.06 Plans and schemas

## Sources re-opened (full text, this session)
Jiang 2023 (self-planning), Wang 2024 (PlanSearch), Zelikman 2023 (Parsel), Olausson 2024 (self-repair), Le 2024 (CodeChain), Wang 2024 (AWM). Voyager and Fisler 2014 PDFs failed to download (damaged file, wrong URL), so their numbers were NOT re-checked and stay as the finder agents recorded them.

## Confirmed
- Jiang: HumanEval Pass@1 direct 48.1, code CoT 53.9, self-planning 60.3, ground-truth plan 74.4; Pass@10 75.0 / 68.6 / 76.3 / 89.1; MBPP 49.8/54.5/55.7/65.1.
- PlanSearch table: GPT-4o-mini 39.0/53.3/59.4/64.9; GPT-4o 41.3/60.6/70.4/73.0; DeepSeek 41.4/53.2/65.9/70.3; Claude 3.5 Sonnet 40.3/55.6/70.2/77.0.
- Parsel: 14.5 to 25.5 on APPS; ablation 6% vs 25.5% at pass@8x16 on 100 problems, solved set a strict subset; HumanEval 67 to 85 with GPT-4; 91.5 and 93.9 pass@any.
- Olausson: GPT-4 feedback 42.64/19.33/3.67/33.30 vs human 62.21/45.67/14.67/52.60.
- CodeChain: APPS GPT-3.5 22.33 to 30.24, competition 5.42 to 12.38, interview 19.42 to 28.11; centroid sub-modules 35.11; GPT-4 61.50.
- AWM: WebArena 23.5 to 35.5, +12.0 points, +51.1% relative, +7.6% over human workflows.

## Corrections
1. c11 says "Claude 3.5 Sonnet: pass@1 41.4%, repeated sampling pass@200 60.6%". Wrong attribution. In the table Claude 3.5 Sonnet is pass@1 40.3 and pass@200 55.6. The 41.4 is DeepSeek-Coder-V2 (best pass@1 without search) and 60.6 is GPT-4o (best repeated sampling). The 77.0 for Claude with PlanSearch is correct. Use b22's table, not c11's sentence.
2. b24 compares CodeChain+GPT4 61.50 with "Self-repair+GPT4" 52.60 and 33.30. These are Olausson's numbers (human and GPT-4 feedback overall) taken from a different paper and a different problem subset. It is the CodeChain authors' own cross-paper comparison, not a controlled one. Do not cite it as a head-to-head.
3. a03/K01: the 1984 fill-in-the-blank subjects were advanced students, not experts. Detienne's "expert" reading is a later gloss. Beta cell counts are still garbled.

## Contradictions between sources
- Composition as the main bug source (Spohrer/Soloway via Robins and Castro/Fisler) vs Fisler 2014 (3 of 187 composition errors; 5% no plan) and Simon 2013 (36% no pertinent code). Population and teaching differ, and Fisler says comparison is imprecise.
- Plans as first representation (Soloway, Detienne) vs control-flow-first (Pennington 1987, numbers from a snippet).
- Plans as mental structure vs notation artifact (Gilmore and Green 1988: direction unverified, from memory).
- Planning helps (Jiang, SCoT, PlanSearch) but lowers diversity or pass@1 in places (CoT Pass@10 68.6 below direct 75.0; PlanSearch pass@1 often lower), and hurts small models (6.7B).
- Faith and Fate (composition collapses with depth) vs Skills-in-Context (near-perfect after a worked composition): different tasks, old models.

## Weak spots
- Almost all human evidence is 1983-1994, small N, and the founding TSE 1984 paper and Spohrer 1985 were never opened. The 75% PROUST figure is unverified.
- LLM studies use old models (code-davinci-002, Codex, GPT-3.5) and benchmarks, mostly HumanEval-style, where plan = decomposition, not a stored stereotyped plan. Almost nothing tests a library of stereotyped plans on a current model.
- Ground-truth plans (74.4) come from reference code: an oracle bound.
- Token cost is mostly not reported, so equal-token gains are unknown (PlanSearch needs about 200 samples).
- Voyager, Fisler 2014, Fix 1993, Demirtas numbers were not re-checked by me.

## Only seen in snippets or second-hand
Soloway and Ehrlich 1984 TSE, Pennington 1987, Gilmore and Green 1988, Simon 2013, Ebrahimi 1994, Spohrer 1985, Ginat 2013, de Raadt, Rist 1989/1991 (all b28-b35, a05, a22). BoT, ADaPT, Planning-Driven Programming were read at abstract level only.

## GAPS
1. Does a library of stereotyped plans (role, init, update, guard slots) retrieved by an LLM beat free planning at equal tokens on a current strong model? No direct test exists; ReGAL shows the benefit shrinks with model strength (+1.3 for GPT-3.5).
2. Does an LLM show the plan-like vs unplan-like effect (Soloway fill-in-the-blank) and expectation errors from retrieved plans? Nothing measured; this decides whether plan hints add a bias risk.
3. What is the actual token cost and pass@1 vs pass@k tradeoff of plan search and self-planning on 2025-2026 reasoning models, where thinking may already plan?
4. Is composition (interleaved, merged plans) a real failure source for LLMs, as Rainfall studies ask for humans? No LLM Rainfall study found.
5. What retrieval key works best for solved-subgoal memory: role/goal description, code text, or LLM plan label (Demirtas micro-F1 0.778)? 
6. When does a wrong stored plan hurt (AWM, ReGAL warn)? Rates of harm by verification strength are unmeasured.
7. What do Soloway and Ehrlich 1984 TSE and Spohrer 1985 report exactly (per-group percentages, bug shares)? Needs the full papers.
8. Does explicit plan teaching/prompting help humans or models on transfer (de Raadt; Robins says thin)? 
9. Do plans transfer across paradigms (functional vs imperative vs OOP; Burkhardt, Detienne 1995 N=8 partial fit), i.e. should library entries be paradigm-neutral?
10. Gilmore and Green 1988 and Pennington 1987: what are the real numbers, and do they weaken the role-slot design?


## Gap search results (evidence_d.jsonl, d01 to d16)
Search note: the web search budget ran out and Semantic Scholar and OpenAlex rate-limited, so work went through arXiv PDFs and one Brown PDF. Opened in full text: Wu et al. counterfactual tasks, Dinh 2023, CodeCrash, XYEval, Rivera 2024, Crichton 2021, CodeRAG-Bench, LILO, AWM (harm sections), NoThinking, Danger of Overthinking, Think Anywhere, Denny CACM survey, Fisler and Castro 2017.

Closed or narrowed:
- Gap 6 (wrong plan harm): partly closed in direction, not in rate by verification strength. Wrong hints cost models accuracy and tokens (CodeCrash 23.2% average drop; XYEval up to 46.7% on 2026 models; Dinh 54.9% to 3.1%). A generic warning only partly helps. New claims K24, K29. Still unmeasured: harm rate for a wrong stored plan with versus without a run-and-compare check.
- Gap 5 (retrieval key): narrowed. LILO shows anonymous abstractions lower solve rate and names plus descriptions restore it (K25); Crichton shows tree-edit-distance retrieval works with few examples but confuses plans that differ in filtering placement (d06). No head-to-head of role text versus code versus label exists. Open.
- Gap 3 (token cost, pass@1 versus pass@k): narrowed. NoThinking and overthinking papers say matched-token sampling with a check beats long thought except for code pass@1 (K27); Think Anywhere says up-front planning misses implementation issues (K28). No 2025-2026 test of PlanSearch-style plan stages against reasoning models at matched tokens. Open.
- Gap 1 (library versus free planning on a strong model): narrowed, not closed. CodeRAG-Bench confirms gains shrink for strong or memorizing models (K26). Still no direct test.
- Gap 2 (plan-like versus unplan-like in LLMs): indirect only. Counterfactual HumanEval and buggy-prefix completion show strong pull to the default pattern (K23). The Soloway task itself has not been run. Open.
- Gap 4 (Rainfall for LLMs): one Codex Rainfall study found (350 programs, about 50% average, weak on empty input) with no structure coding. K22 reworded. Open.
- Gap 8 (teaching plans): Fisler and Castro 2017 gives qualitative fixation evidence (K30). de Raadt not opened; no effect sizes. Open.

Stayed open, no new evidence: gap 7 (Soloway and Ehrlich 1984 per-group numbers, Spohrer 1985, the 75% PROUST figure; the queensu link was a different Soloway paper), gap 9 (paradigm transfer), gap 10 (Gilmore and Green 1988, Pennington 1987 numbers). The Fisler 2014 retry also failed (179-byte HTML page), so K06 numbers are still second-hand.

Caveats for the new evidence: Think Anywhere needs training, XYEval's bad advice comes from a user turn, CodeCrash is code reasoning not writing, Rivera 2024 is an experience report, LILO table columns were partly garbled in extraction so only the quoted text deltas are used.
