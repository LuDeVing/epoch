# B05.05 Map versus value replay: critique (cross-check)

## Sources re-opened and checked (this session)
1. Sagiv et al. 2025 (PMC12633763): n = 250 simulated replay sequences (bottleneck figure) and "around ten blocks per goal" confirmed.
2. Gillespie et al. 2021 (PMC8497431): remote replay 35.1/41.1/34.5/47.2% of SWRs; sessions 24/32/23/33; search trials 711/848/725/1065 and repeat trials 1347/1661/1154/1730; about 20% previous-goal share; about two-fold rate; correct/error subsets 848/1308/614/780. All confirmed. The paper also reports a "small increase" for the future (upcoming) category, so planning signal is weak, not absent.
3. Momennejad et al. 2023 (arXiv 2309.15129): GPT-4 0 of 30 runs, at most 10% at higher temperature, confirmed in text.
4. Schaul et al. 2016 (1511.05952): 41 of 49 Atari games confirmed.
5. Andrychowicz et al. 2017 (1707.01495): future strategy with k=4, real Fetch robot transfer without fine-tuning confirmed.
6. Carvalho et al. (2507.05561): 62.39% (CI 53.99-69.53, p=0.0049), 62.80%, 67.1% confirmed. The experiment 2 CI is printed as 59.68-73.91, which is odd around 62.80; probably a paper typo.
7. Ding AgentHER (2603.21357): CORRECTION. The current version says +7.6 to +11.4 pp over SFT-Success, precision 97.1% (WebArena) and 96.0% (ToolBench), noise 5.9% to 2.9%. Evidence b24/b25 ("+7.1 to +11.7", "97.7%", "2.3%") match an earlier version. Filtered-out pairs valid 38.7% confirmed. Use the new numbers; c18 is right.
8. Li et al. HSL (ICLR 2026, OpenReview PDF): SFT 82.14/78.36/70.00/63.81 and SFT+HSL 93.57/97.76/75.12/66.97, column order ALFWorld seen / unseen / PlanCraft / WebShop, confirmed; 55.2 to 83.6 and 92.5 confirmed. A second table shows variance (for example 96.27 +- 2.11), so 97.76 is a single-run figure. Evidence c24 (snippet only) is superseded by this opened PDF.

## Contradictions and weak spots
- Sagiv's fit to Gillespie and Carey is qualitative, with a chosen slow learning rate and decay. Gillespie's authors favour memory maintenance; Chen and van der Meer favour representation protection. Several explanations fit the same data and no experiment separates them.
- Key map predictions (bottleneck replay, goal-switching order with p11) are untested in animals.
- Mallory/Widloski/Foster (goal-trapped replay, barrier-aware rerouting) are things a pure map must also explain.
- All LLM/AI evidence is training-time (HSL, AgentHER, SAC-GLAM) or small tabular. No in-context test of goal-weighted replay exists. AgentHER and HSL gains are self-reported against own baselines (one lab each); the HSL agent is 1B parameters.
- Animal data: N=4 rats per study, one lab each; no independent replication of lagging replay.
- Version drift: AgentHER numbers changed between versions; other preprint numbers may too.

## Only seen in snippets or abstracts
a20, a21, a22, a23, b12, b14, b26, c05, c25, c26, and part of the Carey final version.

## GAPS
1. Does any LLM-agent study weight stored routes or experiences by the probability of future goals (not only hindsight relabeling) and measure it at equal tokens?
2. Does in-context (no fine-tuning) hindsight relabeling, tagging stored trajectories with all achieved goals, help a prompted agent, and how much label noise breaks it?
3. Which task statistics (goal recurrence, switching rate p11, number of goals) flip the advantage between map memory and current-goal memory for an LLM agent?
4. Can an LLM reliably estimate P(future goal) from its own task history, and does a slow versus fast goal estimate (as in the Sagiv model) matter?
5. What is the token cost of precomputing routes for unpursued goals (preplay) versus retrieving at test time, at equal total tokens?
6. Do the bottleneck/hub prediction and the goal-switching order prediction hold in new rodent or human data?
7. Which of the rival accounts (map prioritisation, memory maintenance, representation protection) is right, and what experiment would separate them?
8. Does the cognitive-map chain-of-thought gain (76.5% vs 19.0% optimal planning) survive without fine-tuning on frontier 2026 models?
9. Are HSL and AgentHER gains independently replicated, and do they hold for large agent models?
10. How should an LLM agent choose which routes to evict from a bounded memory (gain times need) when goals drift?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d18). Web search budget was used up after 6 calls; Semantic Scholar and OpenAlex were rate limited most of the time, so forward-citation lists could not be pulled. All absence claims below are weak.

1. Goal-probability-weighted routes in an LLM agent: STAYED OPEN. No study found. Nearest: sleep-time compute (gain rises with query predictability, d01), TraceRetain and AMV-L (value-scored eviction, d08-d10). New claim K10 reworded.
2. In-context hindsight relabeling: PARTLY CLOSED. ECHO (d03) is prompt-only and beats ReAct by 80% and the next baseline by 42% on XMiniGrid-Stateful; 34 of 40 imputed workflows (85%) reached their goal. No noise-injection sweep exists, so the breaking point is unknown (d04). New claim K20.
3. Task statistics that flip the advantage: STAYED OPEN. ECHO fixes recurrence (16 queries over 4 goals per environment) and never varies it (d05). Sleep-time compute gives the only graded evidence: 1-2 queries per context unfavourable, 5-10 favourable (d02).
4. LLM estimating P(future goal), slow vs fast: STAYED OPEN. No calibration study found (d17). Log-probability of the real query tracked payoff in sleep-time compute, which is indirect.
5. Token cost of preplay vs test-time retrieval: PARTLY CLOSED. Sleep-time compute: about 5x less test-time compute at equal accuracy, 2.5x cost cut per query when shared (with a 10x price on test-time tokens); at high test-time budgets test-time-only wins (d01, d02). Memory write costs: reflection about 3.5M policy plus 0.2M supervisor tokens vs 2.2M with no memory on WikiSQL (d07). No clean equal-total-token test. New claim K19.
6. Bottleneck and goal-switching-order predictions in new data: STAYED OPEN. Newest rat dataset (Mallory 2026, d14) keeps the goal fixed in a session and has no bottleneck analysis.
7. Which rival account is right: STAYED OPEN. Mallory 2026 adds a third family (adaptation-based trapping at the current goal). The separating experiment (switch the rewarded arm at a known rate and read replay order) is written in d18. New claim K23.
8. Cognitive-map CoT without fine-tuning: CLOSED NEGATIVE for 2024 models, OPEN for 2026. Kim 2024 re-opened: cognitive-map prompts gave 0-1% few-shot on Llama-3 and GPT-4o; only GPT-o1 plain prompting rose to 38% at 4 shots (d11). 2026 frontier models (d12): adjacency input 80-86% vs visual grid 16-34%, no map built across questions. MAP (d13) shows a prompt-only modular planner helps on graphs. K12 moved to contested.
9. Independent replication of HSL and AgentHER: STAYED OPEN (d15). Only ECHO agrees in direction, with a different method. Reported HSL figures differ across sources.
10. Eviction by gain times need under goal drift: STAYED OPEN. TraceRetain shows no difference among bounded policies on a clean stream and a large one under 75% noise; AMV-L is latency-only; nobody tested goal drift (d08-d10). New claim K22.

Added side finding: stacked memory types conflict (fact plus reflection: skip rate 77% to 20%, pass@5 58.8% to 52.9%, d06). New claim K21.

Not opened: d12 (abstract page only), d15-d18 (search-note lines, opened:false). The Kim 2024 few-shot table text came out of the PDF with scrambled rows, so one 10% cell is not assigned to a model.
