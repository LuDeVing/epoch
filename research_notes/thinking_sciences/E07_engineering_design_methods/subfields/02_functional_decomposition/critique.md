# E07.02 Functional decomposition: cross-check critique

Cross-checker pass over evidence_a (30 lines), evidence_b (27), evidence_c (25). Claims are in claims.jsonl (K01 to K24).

## 1. Numbers re-opened (full text read this session)

| # | Source | Number checked | Result |
|---|---|---|---|
| 1 | Booth 2015 (IDETC) | Study 1 ANOVA p values (0.037, 0.027, 0.003, 0.001), n=25 | Confirmed |
| 2 | Booth 2015 | Means 19.7 / 16.3 / 15.1 functions; 8.8 / 7.4 / 5.0 features; unmapped 1.3 / 0.2 / 0.0 | Confirmed. Correction to the context: the Tukey table gives group sizes 11, 13, 16 for functions (sum 40, not 25) and 4, 12, 9 for features (sum 25). The energy-flow feature cell is 4 teams. The paper does not explain the 40. |
| 3 | Booth 2015 | Study 2: n=78, 51% used decomposition, r=0.075, p=0.515; matrix r=0.233 p=0.040, r=0.293 p=0.009 | Confirmed |
| 4 | Booth 2013 (IDETC) | 26 students, n=78 trees, no method effect, device effect F=3.63 p=0.0352, prior device F=3.90 p=0.055, class levels 3.5 / 4.17 / 4.84 | Confirmed. The paper states no effect size is reported because n<100. |
| 5 | Simon 1962 | Tempus/Hora ratio about 4,000; 111 times as many assemblies | Confirmed (the paper writes the working as 1/111 x 20 x 20,000, about 4,000). |
| 6 | Hirtz et al. 2002 | 46 of 53 function terms in the NIST taxonomy | Confirmed (line read in NIST TN 1447). The 47 figure for the original basis was not re-read. |
| 7 | ADaPT | 71.6 / 43.3 / 43.3 / 57.5 ALFWorld; WebShop 44.0; TextCraft 52.0; depth 2 26.9 to 78.2; depth 3 1.8 to 38.7 | Confirmed. Correction by addition: the same paper has a second ALFWorld table on the Yao executor and test split: ReAct 56.7, Plan-and-Execute 63.4, Try-Again-with-ReAct 56.7, Reflexion 67.2, ADaPT 79.8. The gain over plan-and-execute is 28.3 points in one table and 16.4 in the other. Evidence lines b23 and c10 quote only the larger. |
| 8 | Least-to-most | SCAN 99.7 / 16.2 / 16.7; GSM8K 62.39 vs 60.87; 2-step 74.53 vs 76.68; 5+ step 45.23 vs 39.07; DROP 82.45 vs 74.77 | Confirmed |
| 9 | Scaling agent systems | Finance +80.8% (0.631 vs 0.349); PlanCraft -39.1 / -50.3 / -70.0 vs 0.568; SWE-bench -2.1 to -14.9 vs 0.522; aggregate -0.3% CI -58.7 to +77.2; amplification 17.2 / 7.8 / 5.1 / 4.4; R2 cv 0.373 | Confirmed. Caveat: the paper's own regression shows the error-amplification term not significant (p=0.658). The -0.236 (p=0.004) term is message density in the regression table, labelled a baseline paradox, and the text ties the 0.45 threshold to the baseline term. Evidence line c17 calls it a capability-ceiling term; the wording is loose, not the number. |
| 10 | Massoudi and Fuge 2025 | Coverage peak 20%; JSON 100%; embodiment tagging 100%; MAS about 650 s | Confirmed in the text. 38.6 s and 94.7% are quoted from the HTML in c01 and not re-read here. |
| 11 | Self-planning code generation | 48.1 / 53.9 / 60.3 / 74.4 pass@1 | Confirmed (HTML). New finding: pass@10 is 76.3 for self-planning vs 75.0 direct and 68.6 code-CoT, so the plan gain nearly vanishes with sampling. Not in evidence lines. Added to K13. |
| 12 | Parsel | 85.1% HumanEval; 91.5% with 8 implementations; 84.1 to 93.9 at 128 | Confirmed (HTML). |
| 13 | Elhambakhsh | 681 samples, test 0.89 at 10% and 0.63 at 90%; train 0.93 to 0.64 | Confirmed. b18 and c04 differ only in whether they quote train or test columns. |

Not re-opened (could not): Linsey 2005 (b10, b11; the ASEE page returned a bot check, so the 19.0 / 19.7 and 5 vs 2 numbers rest on the first agent's read), Kurfman 2001/2003 (a21, a22), Atilola 2016 (b12), Press, Dziri, Radhakrishnan, Plan-and-Solve, Decomposed Prompting figures.

## 2. Corrections made

- ALFWorld gain for ADaPT depends on the executor and split (K10). The headline 28-point gain over plan-and-execute shrinks to about 16 in the second table.
- Booth 2015 cell sizes (K06): do not sum to 25 for the function metric.
- Self-planning gain depends on sampling budget (K13). This matters for G7, because the schema compares at equal tokens.
- c17 wording on the capability-ceiling coefficient is imprecise.
- b01 was already flagged by its author for unclear n; confirmed unclear.

## 3. Contradictions between sources

- Fixation. Linsey 2005 (b11): function group produced fewer highly novel concepts. Atilola 2016 (b12, unopened, secondary summary): function tree caused no more fixation than control. A 20-novice abstract (b14): function terms raised novelty. These use different manipulations (a given function list, a function tree as example, function words as stimuli). So K07 is marked contested, not refuted either way.
- Planner versus executor. ADaPT says a weak executor gains most; self-planning says a small model loses when it plans for itself. Reconciled in K12 by who writes the plan (a strong separate planner helps, a weak self-planner does not). This is an interpretation, not a tested result.
- Decomposition helps (ADaPT, Parsel, least-to-most on SCAN) versus helps little (GSM8K +1.5, Plan-and-Solve +0.6 to 3.1, self-planning at pass@10). The split follows task structure: synthetic or cleanly separable tasks show large gains.
- Multi-agent splitting (K15): ADaPT and Parsel report gains, while Scaling Agents and Massoudi report losses and crashes. The tasks differ in independence; no single paper tests both.

## 4. Weak spots

- No LLM study replicates a human function-decomposition study, and none scores LLM function structures against expert Stone-and-Wood structures with a baseline. The only repeated-run design paper (Massoudi) uses 5 seeds, small local models, and its own coverage metric.
- The human evidence is small and mostly one lab (Purdue). Linsey 2005 is a preliminary one-session analysis with cells of 5 to 13.
- Most LLM decomposition studies use 2022 to 2023 models (davinci, GPT-3.5). Behaviour on current reasoning models is unmeasured here. Reasoning models may already decompose internally; the Massoudi R1 two-agent run collapsed to one node.
- LLM studies rarely match tokens. ADaPT, Parsel and Scaling Agents all spend more calls than their baselines. Only Parsel matches sample counts at 128.
- "Established" claims K01, K11, K14 rest on analysis and synthetic or QA tasks, not on engineering design.
- Evidence a21, a22, a23, a24, a25, a30, b13, b14, c05, c15, c22 are abstract-page reads only. Their findings are carried as single-source or used only to support a limits statement.
- Evidence b12 (opened:false) and b27 (opened:false) were seen in search summaries only.

## 5. What was seen only in snippets

Atilola 2016; the Haddad and Seibel MCTS-FD numbers; MAST per-mode percentages; Kurfman participant counts; the Erden 17-criteria count; Clemson dissertation numbers; the 2018 CIE functional-terms study details.

## GAPS

1. Does a current strong model (2025 to 2026 reasoning model) get any gain from an explicit O3 decomposition step at equal tokens, on tasks with a code check, once the model already reasons at length? Every LLM number we hold is from weaker models and unmatched budgets.
2. How well do LLMs reproduce expert Stone-and-Wood function structures (sub-function recall, flow connectivity) on 10 or more products, and does a verb-object vocabulary change quality? The Haddad and Seibel MCTS-FD numbers (ICED 2025) are the one unread lead.
3. What are the participant counts and agreement percentages in Kurfman et al. 2001 and 2003? Without them the only founding test of the method cannot be weighed.
4. Does showing a decomposition before generation narrow the final answers (fixation) in LLMs, and does decomposing after a free first attempt avoid it? The human evidence conflicts (Linsey 2005 vs Atilola 2016 vs the 2018 stimuli study); Atilola needs to be opened.
5. Is the gain from decomposition mostly better plans or more tokens? A plan-quality score (against a held-out solution) correlated with final success, and a matched-token comparison against plain sampling, are missing outside Parsel.
6. Where is the break-even depth or step count for decomposition in LLM agents (GSM8K shows a loss at 2 steps, a gain at 5 or more)? A routing rule for the S0 gate needs a measured threshold on current models.
7. Does the Booth null for human decomposition come from poor use (51% very low quality diagrams) or a weak method? A study where experts or a checker enforce diagram quality, then compare design outcomes, has not been run.
8. Do separate-context sub-question answers (factored decomposition) keep their faithfulness gain and lose less accuracy on current models, and can code recombination close the compositionality gap (about 23% on GPT-4)?
9. How should sub-problems be sized so each is solvable (Vermaas)? Is there a measurable stopping rule, such as ADaPT's executor-failure trigger, that also works without an environment reward (ADaPT's self-judgement overstated success by over 30 points on WebShop)?
10. Do the morphological-matrix and combine steps (Booth 2015, r=0.233 to 0.293) add value that decomposition alone does not? Only one observational sample exists.

## Gap search results

Search quota ran out after about 4 searches and arXiv search was rate limited, so sources were reached by DOI, repository API and known arXiv ids. 15 evidence lines in evidence_d.jsonl (d01 to d15); claims K25 to K31 added and K07, K13, K17, K18, K20 extended.

Status of the 10 gaps:

1. Explicit O3 step at equal tokens on a strong reasoning model: STAYS OPEN. No direct test found. Indirect only: generic step-by-step prompting adds about nothing on o3-mini, o4-mini and Flash 2.5 (d08), while Atom of Thoughts reports +3.4 AIME and +8.6 LiveCodeBench for o3-mini with unmatched cost and a very regular result pattern (d09). DISC beats best-of-N at equal tokens, including R1 (+33% relative), but splits the solution, not the problem (d06). K25.
2. LLM reproduction of expert function structures: PARTLY CLOSED, negative. Haddad and Seibel was read in full (d01, d02). It measures rule validity on 50 products (plain GPT-4o 16% error-free, 44% connected; with MCTS-FD 42% and 72%), not recall against expert structures, and uses Roth's 21 functions, not the verb-object basis. Raters scored plain GPT-4o above MCTS-FD. Recall, flow accuracy and vocabulary effect remain unmeasured. K26.
3. Kurfman participant counts and agreement: STAYS OPEN. Full text blocked by a bot check; only abstracts read (d04, d15). K30.
4. Does a shown decomposition narrow answers: PARTLY CLOSED for humans, OPEN for LLMs. Atilola was opened through the open thesis (d03): N=61, a function tree of an example caused no fixation and less than a sketch, sketch plus tree was worst, and the tree group had the best quality. But the omnibus tests were mostly not significant (p=0.083, 0.08), the pairwise Z and p values look inconsistent, and it concerns someone else's decomposition. The conflict with Linsey 2005 is partly explained: a decomposition of an example is not the designer's own decomposition. No LLM test. K27.
5. Better plans or more tokens: PARTLY CLOSED. PlanSearch (d07): plan diversity predicts search gain and a correct sketch is sufficient to solve; token-matched, it wins only above about 10,000 tokens per problem and often lowers pass@1. Plan-and-Act (d12): a poor planner hurts. Still missing: plan quality scored against a held-out solution and correlated with success for a scaffold (not trained). K28.
6. Break-even step count on current models: STAYS OPEN. Only AoT's depth and sub-question trend (3 to 4 parts at depth 3 typical, accuracy falls with more; d10) and a second-hand small-model loss (d13, not opened). No threshold measured.
7. Booth null from poor use or weak method: STAYS OPEN for humans. LLM analogue found: partial structure was worse than none in the AoT ablation (d10). K29.
8. Separate-context faithfulness and compositionality gap on current models: STAYS OPEN. Nothing new found.
9. Stopping rule without environment reward: STAYS OPEN. Plan-and-Act shows replanning helps with environment feedback (d12); nothing for reward-free stopping. AoT proposes using graph depth as the cap (d10), untested.
10. Morphological matrix and combine step: STAYS OPEN. Nothing new.

Net: the two decisions the gaps were meant to inform (turn O3 on by default, and size the parts) still lack a measured threshold. The cheap, defensible plan is to default O3 off for strong reasoning models, gate it on an S0 depth estimate, require a quality gate on the decomposition, and run the K25 test before relying on it.
