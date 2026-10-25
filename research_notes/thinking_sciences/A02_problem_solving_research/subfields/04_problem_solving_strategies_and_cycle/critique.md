# Critique: A02.04 Problem-solving strategies and the problem-solving cycle

Cross-check of evidence_a, evidence_b, evidence_c (90 lines). Claims are in claims.jsonl (A02.04-K01 to K28).

## 1. Numbers re-opened this session (from the PDF or HTML text)

Confirmed:
- Self-Discover (arXiv 2402.03620): Table 1 BBH/T4D/MATH for PaLM 2-L (56/30/45; CoT 60/40/42; PS 61/42/49; SD 67/69/50.5) and GPT-4 direct 58/51/70.5. Error analysis 87.5% (175 of 200) correct structures, 74.7% of errors from computation. (a23, b06, b27, c09, c10)
- Tree of Thoughts (2305.10601): IO 7.3, CoT 4.0, CoT-SC k=100 9.0, ToT b=1 45, b=5 74, best-of-100 CoT 49; about 60% of CoT samples fail after step one; GPT-3.5 both roles 19, GPT-4 gen + GPT-3.5 eval 64, reverse 31. (c04, c05)
- Step-back (2310.06117): Physics 66.4 / CoT 65 / step-back 73.2; Chemistry 70.9 / 75.3 / 81.8; TimeQA 41.5 to 66; GSM8K 75.8 / 84.4 / 84.3; fixes 20.5% of errors, adds 11.9%. (a27, c14, c15)
- Meta-Reasoner (2502.19918): Game of 24 GPT-4o-mini CoT 4, ToT b=5 65, MACM 80, Meta-Reasoner 89; without progress report 85; without MAB 82 (TheoremQA 84.13 falls to 39.46 without MAB). (a29)
- Adaptive-Solver (2310.01446): 46-85% cost cut versus GPT-4; GSM8K 92.49 vs best equal-cost baseline 87.93; SVAMP 90.75 vs 88.75; GPT-4 vs GPT-3.5 gap 6-16 points at 7-13 times cost. (a28, b05, b29, c06)
- Stadler et al. (2015) meta-analysis: 47 studies, 60 samples, N=13,740, mean g=.433, from the abstract (via Semantic Scholar). (a17, b10)
- Wu and Molnar (2022): 84.3% proficient, 6.2% rapid learners; F(3,1339)=187.28. The profile means (61.37 etc.) were not re-found in the text. (b14)
- Schunn, Lovett and Reder (2001): N=56; aware .44 vs unaware .17 shift; F(1,53)=12.7; chi2(3)=13.0. (a03)
- Zhang et al. (2507.11423): oracle 82.9 / 90.1 (TruthQuest) and 37.7 / 36.4 (ZebraLogic); merge table values 54.9, 57.3, 55.8, 46.9 (Phi-4), 74.1 (R1 verifier). (b02, b03)

## 2. Corrections

1. a25 (analogical prompting) has the row labels shifted. In the paper the GSM8K column for GPT-3.5-turbo reads 75.0 (0-shot), 75.8 (0-shot CoT), 76.7 (5-shot CoT), 77.8 (analogical). MATH: 33.0, 33.9, 34.9, 37.3. c13 is right, a25 is wrong where it says "5-shot CoT 75.0". Correct gain over 5-shot CoT: +1.1 (GSM8K) and +2.4 (MATH), not +2.8 and +4.3. Used in claim K08.
2. b04 (strategy by problem size) mislabels the models. In Table 4/5 of the paper the row "Single strategy 74.2/69.5/61.0/49.0 (avg 63.4)" belongs to R1-Distill (the no-strategy baseline), not Phi-4. Phi-4 no-strategy by 3/4/5/6 persons is 65.7/49.7/40.5/33.5 (avg 47.2). The extracted table is also shifted by one row, so the per-strategy winners at 3 persons (77.7, 79.3) are R1-Distill values with uncertain strategy names. The safe reading is: no strategy wins at every size. b04 also says hard ZebraLogic is "about 8%"; the paper shows 9.4-15.1% (Phi-4 no strategy 15.1%). Treat b04 numbers as unreliable.
3. a28 states model adaptation "saved 35.8% to 53.6% cost". These two figures do not appear in the paper text. The paper's headline is 46-85%. Treat 35.8 and 53.6 as unverified. (GSM8K 93.5 vs 93.0 also not re-found.)
4. a08 (Gick and Holyoak 1980) was marked opened but the source is a SlideShare deck, a secondary source. The numbers (76%, 49%, 8%) agree in direction with b19 and a09 but were not seen in the original.
5. b10 was marked opened:false; the g=.433 figure is now confirmed from the abstract.

## 3. Contradictions between sources

- Analogy baselines. Gick and Holyoak report control solution rates of about 8-10% for the radiation problem; Seiter and Krabbe (b21) report 51% of controls giving the splitting solution. Different populations and coding. Also a09 reports 20% (no hint, Exp IV) while b19 says about 30%: different experiments, not a true conflict.
- Does strategy matter in CPS? Strategy use (VOTAT) predicts MicroDYN success (b13, b14, b23) but is neither necessary nor sufficient (b15), and the transfer paper (b12) finds VOTAT does not mediate transfer (r=.28 with performance). These fit together as "weak, confounded".
- b14 says inductive reasoning predicts CPS in all four profiles (beta .309-.432); b26 says it predicts knowledge acquisition only in proficient (.363) and rapid learners (.327). Different outcome measures; not checked against the paper tables.
- CPS as general ability: g=.433 (a17) against near-zero correlations among different complex problems after control (a18, snippet only) and about 5% incremental variance (a15).
- Structured plans: Self-Discover (a23, b06) says task-level JSON structures help; Gunasekara and Ratnayake (b07, b28) say free-text per-instance plans beat JSON on MATH. Their own Self-Discover baseline on BBH (86.59/82.04) is far above the original 67/81, so the two setups are not comparable (different models and prompts).
- Error source. Self-Discover and Step-back say reasoning execution is the main error source; Plan-and-Solve (a26) found misunderstanding (27%) larger than calculation (7%) for zero-shot CoT with GPT-3. Different methods, different models.

## 4. Weak spots

- Almost all human evidence on strategy choice is from arithmetic, Building Sticks and MicroDYN. Nothing was found that tests strategy choice in open-ended reasoning with real stakes.
- Most LLM strategy results come from one or two papers per method and from models of 2023-2025 (PaLM 2, GPT-3.5, GPT-4, Phi-4). No result was tested on recent reasoning models other than Zhang et al. (R1-Distill, Qwen3) and Route to Reason.
- Meta-Reasoner (a29) and SMART (c08) are single-source; Meta-Reasoner's own ablation shows a huge TheoremQA effect (84.13 vs 39.46) that looks like an implementation failure of the no-MAB arm rather than a clean contribution.
- Many "established" claims are established only at the level of "two papers agree on direction".
- Token cost is rarely reported at equal budget. Self-Discover reports fewer calls than self-consistency but not an equal-token comparison on every task.
- The Alderete et al. (c21) result is a 2026 paper with one-tailed testing and 110 trials per arm.

## 5. Seen only in snippets or secondary text (not opened)

a11 (Duncker 1945), a12 (Simon 1973), a18 (Suess 1999), a20 (Shrager and Siegler 1998, abstract only), a22 (Luchins 1942, garbled OCR, the 77% is unverified), a30 (analyst synthesis), a31 (Dorner et al. 1983, 403 error), a32 (Kotovsky, Hayes and Simon 1985), b09 (Meta-Prompting), b18 (Lemaire and Siegler 1995), b22 (Sinha and Kapur 2021 meta-analysis, pooled effect not obtained), c26 (Reverse Thinking), c27, c28. Claims that rely on them (K24 working backwards, none on Luchins) are marked single-source.

## GAPS

1. At equal tokens, does a routed strategy (cheap-first, escalate on disagreement) beat the best single fixed strategy on our own task mix, and how large is the oracle gap there? (Zhang et al. shows oracle +33 points on TruthQuest but selectors recover under a third.)
2. Which signal decides a strategy switch best at inference time: answer disagreement across samples, a progress report, a verifier, or explicit failure of a sub-goal? No paper compares these four under one budget.
3. Does a persistent per-task-type record of strategy success (the ACT-R and SSL idea) help an LLM agent across items, or does the model ignore it? No LLM test of the Lovett and Anderson mechanism was found.
4. Do current reasoning models (o-series, R1, Qwen3 thinking) still gain from prompted strategies such as decomposition, abstraction or analogy, or do they already do them? Most strategy-prompt results are from 2023-2024 models.
5. Is failure to notice that a strategy has stopped working (Schunn et al.) the same in LLM agents, and does an explicit "has success changed" check fix it?
6. How should the agent classify an item as well-structured or ill-structured before choosing a strategy? Simon (1973) and Dorner's criteria were not opened; no operational test exists in the collected evidence.
7. Do Dorner-style failures (hasty action, stereotyped repetition, loss of goals in long dynamic tasks) occur in LLM agents in simulated environments like Lohhausen or Tailorshop, and which monitor catches them?
8. Is the Einstellung effect (Luchins) real in LLMs when a previous method works but a shorter one exists? Only red-herring work (c01) was found, not the classic set-up.
9. Does productive failure (try before instruction; Sinha and Kapur meta-analysis, 53 studies) have an agent analogue: attempting first, then retrieving a method? The pooled effect size was never read.
10. What is the right unit of "strategy" for the schema (named prompt template, operator in O1-O8, or a plan structure)? Gunasekara and Ratnayake vs Self-Discover suggest the format matters as much as the choice.

## Gap search results

Evidence is in `evidence_d.jsonl` (d01 to d23; 19 opened, 4 not opened). Claims K29 to K37 were added. K10 moved to established, K26 moved to contested. Status per gap:

1. Routed vs best single strategy at equal tokens: partly closed. Select-then-Solve (d02) gives a router at 53.1% vs best fixed 50.3% (+2.8) and recovers 26% of an oracle gap of +17.1, at about half the tokens of always-ReAct. Disagreement routing (d03) beats majority vote by 6.9 points on Qwen3-8B at an equal cap of six samplings. Still open: no paper fixes tokens, the oracle is inflated by single runs, and nobody tested our task mix. Do a pilot with repeated runs.
2. Which switch signal is best: partly closed, not compared head to head. Answer disagreement works (d03; false agreement is the stated blind spot). Self-chosen routing fails below the frontier (d18). A tool-failure rule works for strong models only (d05). Progress report, verifier and sub-goal failure were not compared under one budget in any new source.
3. Persistent record of strategy success: partly closed. Outside bandits that learn from per-task success work (d15, d16; modest gains, tens of tasks to learn). In-context use of raw history is poor without a summary (d17, abstract only). No test of an LLM reading its own success table. Open for that case.
4. Prompted strategies on reasoning models: partly closed for CoT only. Gains are marginal or negative (d13, d19). Decomposition, abstraction and analogy on RL reasoning models were not found (d14 uses instruct models). Open.
5. Failing to notice a strategy stopped working: closed in direction. LLM agents do fail to notice (d05), and an explicit reuse-last-success, switch-on-failure rule fixes it only for the two strongest of four models. The WCST study (d23) is a snippet lead only.
6. Well- vs ill-structured classification: stays open. Simon (1973) was not obtained. Jonassen and Funke were seen only as search summaries (d21, d22). The only usable operational proxy found is sample disagreement (d20), which is an outcome signal, not a structure test.
7. Dorner-style failures in LLM simulations: partly closed. Derailments, loops and idle-drift are documented (d11, d12) and are not context-limit failures. A strong no-reasoning model beat human trajectories in Tailorshop (d10). No study maps failures to Dorner's taxonomy or tests a monitor; the no-op counter and belief check are untested ideas.
8. Einstellung in LLMs: partly closed, contested. The classic-style test is tiny (d06: six items per cell) and its three-step result may be instruction following. Cue-based fixation was strong in 2024-25 models (d07) and gone for strong reasoning models in 2026 (d08, same 100 public items). No Luchins water-jug replication exists.
9. Productive failure: the human side is closed (d01: g 0.36, CI 0.20 to 0.51, 53 studies; 0.37 to 0.58 with high fidelity; younger pupils favour instruction first). The agent analogue is open; no LLM test found.
10. Unit of strategy: partly closed. Operators offered as callable tools beat a fixed-order script (d14: Llama3.3-70B 52.8, 66.0, 80.0), which favours operators in O1-O8 over named templates. Single source, instruct models, math only.

### Cautions

- Disk was full during this pass and several downloads were truncated. Full text was read for Select-then-Solve, Route-to-Reason, Haq et al., Kim et al., Shidara et al., Welsch, CoffeeBench, LIMBO, MemCon and Meincke et al.; the disagreement-routing paper, set-shifting paper and Vending-Bench came as arXiv HTML; Krishnamurthy et al. and the Sinha and Kapur meta-analysis were abstract only.
- Not verified: Lovett and Anderson (1996) abstract (search failed), Funke full text (download was not a PDF), EDRM 2605.22873 (PDF damaged), and a "15.2 points" MemCon figure from a search summary (not in the text; not used).
- All 2026 papers are preprints; none has an outside replication.
