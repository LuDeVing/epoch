# Adaptation: deep document

*Subfield C08.06 of case-based reasoning: edit a retrieved solution so it fits the new problem. Schema parts: S5 (revise), O7 (map an analogue). Built from evidence_a-d.jsonl (a01-a32, b01-b31, c01-c30, d01-d22), claims.jsonl (K01-K26) and critique.md in this folder. The critique re-opened the DS-Agent, Memento, Huang and Olausson numbers and confirmed them. Numbers from TextBFGS, CBR-to-SQL, AWM, DomAgent and Ye et al. were read by one or two extractors only.*

## 1. What it is

Case-based reasoning (CBR) has four steps: retrieve a past case, reuse it, revise it, retain the result. Adaptation is the reuse and revise part. It takes a retrieved solution that almost fits and changes it so that it fits the new problem.

Three classic kinds of adaptation (Kolodner 1993, named in a29):
- Substitution: swap a part of the old solution for a part that fits (chicken for beef).
- Transformation: add, delete or reorder parts (add a step the new item needs).
- Generative re-derivation: replay the reasoning that made the old solution, with the new inputs.

Three modes proposed for LLM agents in a 2025 review (a17, b30, c28; conceptual, no data): transformational (substitute, delete, insert), compositional (merge parts of several cases), generative (write new, guided by a case).

Why it matters: retrieval alone returns something close, not something correct. Badra et al. call adaptation "the Achilles heel" of CBR, because the knowledge for editing is domain specific and hard to get (b06, c20). For our agent, adaptation is what S5 (revise from a failing output) and O7 (map an analogue) actually do.

The question for our schema: when the agent has a stored solution or lesson, does editing it, with a check, beat a fresh attempt at equal tokens? No study answers this directly (K19). The nearest evidence is in sections 3, 5 and 6.

## 2. History and theories in depth

**CHEF (Hammond 1986) [a01-a03, V].** The founding adaptation-by-edit system. Domain: Szechwan stir-fry recipes. Six processes: anticipate problems, retrieve a plan, modify it, repair it, assign credit, store it.
- Modify: a stored beef-and-broccoli plan becomes chicken-and-snow-peas by two substitutions. Each ingredient has a critic that adds or removes steps (chicken must be boned before chopping).
- Anticipate: failures are stored and indexed by the goal features that interacted (beef plus a crisp vegetable gives soggy broccoli). On a new problem with the same interacting goals, CHEF predicts the failure before planning and retrieves a plan that already avoids it.
- Repair: when a plan fails in simulation, CHEF explains the failure first, then repairs.
- Evidence level: worked examples only, hand-built critics, no benchmark. A plan has about 17 steps over a dozen ingredients.

**Case difference heuristic (Hanney and Keane 1996) [a07, c21, M].** Learn adaptation rules from pairs of stored cases. The difference in problems becomes the rule condition. The difference in solutions becomes the action. Rules with alike conditions and effects are merged. Second-hand report (d'Aquin 2007): better than no adaptation on house-price and servo-rise-time regression. Original not opened, no figures.

**DIAL (Leake, Kinley, Wilson 1996) [a10, M] and Jarmulak, Craw, Rowe 2001 [a11, M].** Keep a library of past edits (adaptation cases), not only past solutions. DIAL stores transformations (add, delete, substitute) plus the memory search needed to find the filler. Jarmulak builds one adaptation case per stored case by retrieving its nearest neighbour (leave-one-out) and recording the problem and solution difference. Both second-hand. Cheap to build from the agent's own history.

**Adaptation-guided retrieval (Smyth and Keane 1995, 1998) [a12, a13, b07, d21, M].** Retrieve the case that is cheapest to adapt, not the most similar one. Claim: similarity is a poor stand-in for usefulness. Reported to beat similarity retrieval on accuracy and efficiency in case-based design (Deja Vu). Both papers are paywalled; no number was read. Follow-ups: Jalali and Leake ensemble adaptation-guided retrieval [b08, M] and Craw, Wiratunga, Rowe 2006 [b09, M], snippets only.

**Adaptation knowledge discovery (d'Aquin et al. 2006, 2007; Badra et al. 2009) [a08, a09, a30, a31, b04-b06, c19, c20, V].**
- CABAMAKA looks at all ordered pairs of cases (not only similar ones) and mines frequent closed itemsets from the pair differences. A human reads the itemsets as rules.
- Numbers: breast-cancer treatment, 647 cases, support threshold 10 percent, 2344 frequent closed itemsets in about 2 minutes, 208 kept after requiring a change in both problem and solution. The early paper used about 750 cases and about 5x10^5 pairs. Example rule: tumor under 4 cm in source and over 4 cm in target means swap partial mastectomy for radical mastectomy.
- Opportunistic version (Taaable, 862 recipes): mine at problem-solving time, only when adaptation fails, then show the rule to the user. Feasibility shown on use cases; no accuracy figure.
- Three-step model: (source, target) gives a problem difference; (difference, adaptation knowledge) gives a solution difference; applying it to the source solution gives the target solution. Properties are marked kept (=), lost (-), gained (+).
- The authors call their evaluation anecdotal. The bottleneck is expert filtering, not rule generation.

**Deep-learning CDH (Ye, Zhao, Leake, Wang, Crandall 2021) [a04-a06, b01-b03, c17, c18, V].** The first modern controlled test of learned adaptation. See sections 3 and 5. Related and not read: NN-CDH (Leake et al. 2021) [a15, M], Siamese difference prediction (Wetzel et al. 2020) [a16, M], Leake and Ye 2021 on alternating optimisation of retrieval and adaptation [a14, c29, M].

**LLM era.** Adaptation becomes "put a retrieved case in the prompt and let the model edit it". Key systems: DS-Agent 2024, Agent Workflow Memory 2024, Memento 2025, TextBFGS 2026, CBR-to-SQL 2026, DomAgent 2026. Wilkerson and Leake 2024 (the main CBR group on LLMs as adapters) is closed access and unread [a28, d20, M].

**Parallel line: self-correction and test-time revision.** Not CBR, but it tests the same act (edit an earlier solution): Self-Refine, Self-Debugging, CRITIC, Huang et al., Olausson et al., SCoRe, Snell et al. These supply the controlled evidence on when an edit helps.

## 3. Core findings with exact numbers

Status: E established (two or more independent sources), S single source, C contested.

| Finding | Numbers | Source (ids) | Status |
|---|---|---|---|
| Edit one retrieved case beats zero-shot and random-case prompting (data-science code) | One-pass rate, 18 tasks, 10 runs: GPT-3.5 85%, GPT-4 99% (99.44) vs best baseline 56% and 60%. Mixtral-8x7B 6% to 31% | DS-Agent, Guo 2024 (a18, b10, c01) | S (K01) |
| Editing a stored case is cheap | $0.0045 (GPT-3.5) and $0.135 (GPT-4) per run; 92.5% and 91.5% less than the development stage | DS-Agent (a18, c04) | S |
| Removing the feedback-driven revise step hurts | DS-Agent mean best rank, 12 tasks, GPT-4, 5 trials: full 2.08, without ReviseRank 2.58, without CBR 3.41 (lower is better) | DS-Agent (b12, c02) | E with CBR-to-SQL (K02) |
| Removing the Revision stage hurts a lot | CBR-to-SQL on MIMICSQL: execution accuracy 0.894 vs 0.786 without Revision (-10.8 points); logical form 0.862 vs 0.776. Replacing the smart retrieval with plain RAG retrieval cost only 0.005 (0.889) | Nguyen 2026 (a25, c09) | E (K02) |
| Two-stage design beats single-step RAG | MIMICSQL AccEX 0.894 vs 0.860; EHRSQL 0.895 vs 0.818; AccLF 0.729 vs 0.676 | CBR-to-SQL (c09) | S |
| Explicit adaptation stage degrades less when top cases are removed | AccEX drop MIMICSQL 0.028 vs 0.074 (RAG); EHRSQL 0.043 vs 0.138. A second table shows 0.065 vs 0.082 and 0.086 vs 0.171; EHRSQL logical form 0.182 vs 0.184 (no difference) | CBR-to-SQL (a26, c10) | S (K15) |
| More retrieved cases do not help | Memento DeepResearcher F1/PM: K=0 59.9/72.2; K=1 63.6/77.9; K=2 63.7/78.1; K=4 64.5/78.5 (peak); K=8 64.1/78.2; K=16 and K=32 63.9/78.1. DS-Agent falls as cases grow (figure only). Fallacy-CBR peaks at k=1 | Memento (a21, b20); DS-Agent (a19, b11, c03); Sourati (a27, c15) | E (K03) |
| Case memory adds on top of planning | Memento CBR gain F1/PM: HLE +4.5/+7.0; SimpleQA +3.7/+5.3; DeepResearcher +6.7/+8.2. GAIA val 87.88 Pass@3, test 79.40. The gap shrinks to about 0.4 by iteration 5 (84.85 vs 84.47) | Memento (a20, a22, b19, c12, c13) | S (K10) |
| Planning matters more than case memory | Adding planning: HLE +11.0/+1.6, SimpleQA +32.5/+4.9, DeepResearcher +29.1/+11.5. Tool use with no planner: DeepResearcher -18.0 F1 | Memento (a22) | S |
| Learned edit helps most when the query is far from memory | Ye et al., train ages 20-50. Under 20: regressor 8.95, Siamese+adapt 8.09, L1+adapt 9.18. 50-70: regressor 15.51, Siamese 14.85 to 12.02, L1+adapt 14.74. Over 70: regressor 32.77, Siamese 33.05 to 28.83, L1 35.84 to 32.11 | Ye 2021 (a05, b02, c17, c18) | S (K04) |
| Familiar queries: a plain regressor wins | Normal setting MAE: constant 12.94, regressor 5.97, L1 9.58 to 8.14 after adapt, Siamese 7.49 to 7.86 after adapt | Ye 2021 (a04, b01) | S (K04) |
| Adaptation can make a good retrieval worse | Siamese+adapt normal setting 7.49 to 7.86. Adaptation lowered error in 7 of 8 cells | Ye 2021 (a06, b03, a32) | S (K05) |
| Error-keyed operator memory transfers across domains; problem-keyed does not | TextBFGS Plus pass. MBPP-Hard (117 tasks): no case base 48.72; problem-keyed in-domain 78.63; cross-domain problem-keyed 58.12 vs error-keyed 74.36. HumanEval-Hard (45 tasks): no case base 82.22; in-domain 97.56 (problem) vs 96.34 (error); cross-domain error-keyed 93.33 | TextBFGS (a24, b16, c06, c07) | S (K06). Extractor warns one 74.36 cell may be mis-mapped |
| Operator memory saves tokens | 21.6k tokens, -50.6% vs Momentum (43.7k); one-pass variant 25.2k vs TextGrad 30.9k (-18.4%) at equal 82.22% pass; iterations down to 13.6 | TextBFGS (b17, c08) | S (K07) |
| Case base lifts a hard subset | MBPP-Hard Plus: TextGrad 48.72, Momentum 58.12, TextBFGS without case base 48.72, with case base 78.63. HumanEval-Hard: 82.22, 86.67, 93.33 | TextBFGS (a23, c06) | S |
| Trained adapter on small LMs, best at k=1 | LOGIC weighted F1, CBR vs baseline: RoBERTa 0.657 vs 0.599; BERT 0.619 vs 0.560; ELECTRA 0.611 vs 0.586. Out of domain 0.270 vs 0.217; 0.245 vs 0.200; 0.200 vs 0.120. Overlap of retrieved and true labels only 27.7% | Sourati 2023 (a27, c15, c16) | E with K03 sources (K12) |
| Retrieval plus LLM adapter in a narrow domain | Truck CAN code pass@1: Qwen2.5-7B 39.62 to 96.64; GPT-4o 71.22 to 98.04. DS-1000 GPT-4o 51.0 to 58.6 (+7.6). KG-selected 30% of cases about equals random 80% | DomAgent (b31, c11) | E with others (K12); proprietary data |
| Legal QA: small gain | Cosine 0.8967 no RAG; 0.9141 best CBR-RAG (+1.94%), significant at 95% | Wiratunga 2024 (c26) | S |
| Abstracted workflows raise web success; task success on hard splits stays small | WebArena 23.5 to 35.5 (+12.0, +51.1% relative). Mind2Web cross-task/website/domain SR: MindAct 2.0/2.0/1.0; AWM-offline 4.8/2.3/0.7; AWM-online 4.0/1.6/1.7. Step SR cross-task 36.2 to 45.1 | AWM (b21, b22, c14) | C (K11) |
| Raw stored items can fall below the no-memory baseline | GPT-4o Game of 24 10 to 6; MMLU-Pro Eng 53.2 to 48.8; AIME 2024 full-history 20.0 to 6.7. AWM WebArena multi-site 3.4 vs 10.3 no memory | Dynamic Cheatsheet, ReasoningBank (d13, d14, d15) | E (K22) |
| Distilled items beat raw ones, but the best unit depends on the task | WebArena: no memory 40.5, Synapse 42.1, AWM 44.1, ReasoningBank 48.8, +MaTTS 51.8; multi-site 10.3 / 3.4 / 13.8 / 17.2 (no memory / AWM / RB / RB+MaTTS). ExpeL insights vs retrieved trajectories: HotpotQA 36 vs 31; ALFWorld 50 vs 55; WebShop 37 vs 38. BoT at about 12% of multi-query cost, Game of 24 82.4 vs 3.0 (GPT-4) | d11, d13, d15, d17 | C (K23) |
| Lessons from failures help when distilled | WebArena-Shopping success-only vs with failures: Synapse 40.6 to 41.7; AWM 44.4 to 42.2; ReasoningBank 46.5 to 49.7 | ReasoningBank (d16) | S (K26) |
| Executable case beats a text insight | Fig. 6a: case variant above insight variant on nearly all deployment tasks; no numbers in text | DS-Agent (b13) | S |
| Self-generated exemplars: strong models only | GSM8K davinci-003: 0-shot CoT 50, 5-shot 54, retrieved 57, self-generated 61. davinci-002 47 retrieved vs 48 self; davinci-001 11 vs 9; curie 3 vs 2. GPT-3.5-turbo GSM8K CoT 75.8, 5-shot 76.7, self 77.8; MATH 33.9 / 34.9 / 37.3 | Yasunaga 2024 (b27, c24) | S (K13) |
| Blind self-edit does not help and often hurts | GPT-3.5 GSM8K 75.9 to 74.7; CSQA 75.8 to 41.8; HotpotQA 26.0 to 25.0; GPT-4 GSM8K 95.5 to 91.5 to 89.0; HotpotQA 49.0 to 43.0. With oracle labels GSM8K 84.3, CSQA 89.7. 74.7% of GSM8K answers unchanged | Huang 2024 (b25, b26, c23) | E (K08) |
| Break rate of blind edits | 38% of correct answers flipped by a naive revision model (MATH, PaLM 2-S*). Gemini 1.5 Flash MATH: turn 1 52.6, turn 2 41.4; correct-to-incorrect 15.8%, incorrect-to-correct 4.6%; Self-Refine 52.8 to 51.8, 4.2% and 3.2%; SCoRe 60.0 to 64.4, 1.4%. Llama-3.1-8B: 58.8% of correct answers overturned, accuracy -20.4 | d02, d09, d10 | E (K21) |
| Repair is bottlenecked by diagnosis | GPT-4 repair success 1.58x with human feedback (33.3% to 52.6%); GPT-4 feedback inaccurate 32/80 vs human 7/80; uncertainty expressed 0/80 vs 7/80. 16 participants, 40 failing programs. (Critique: ignore the c22 table cells 42.64 to 62.21 as headline) | Olausson 2024 (b23, b24, c22) | E (K09) |
| Specific feedback beats generic beats none | Self-Refine Code Opt 27.5 / 26.0 / 24.8; Sentiment 43.2 / 31.2 / 0; Acronym 56.4 / 54.0 / 48.0. Self-Debugging explanation alone +2 to 3 on Spider (81.3 to 84.1); with tests up to +12 (MBPP 61.4 to 70.8, scrambled table) | d03, d07 | E (K25) |
| Edit beats fresh samples when a verifier exists | Self-Debugging Spider: debug of 1 greedy sample matches baseline with 16 samples; debug of 8 beats 32; more turns add under 0.1%. Snell: compute-optimal revision matches best-of-N with up to 4x less compute (64 vs 256 samples) on MATH, with a finetuned reviser and learned verifier | d01, d06 | E (K20) |
| Fresh sampling is a strong bar | Large Language Monkeys: SWE-bench Lite 15.9% at 1 sample, 56% at 250 | d18 | S |
| Edit gain shrinks with base accuracy on reasoning | Self-Refine math: GPT-3.5 64.1 to 64.1; ChatGPT 74.8 to 75.0; GPT-4 92.9 to 93.1; oracle (GPT-3.5) +4.8. But CBR-DDI Naive-CBR to CBR-DDI: 47.88 to 68.52 (8B), 48.09 to 71.36 (70B), 55.20 to 71.05 (DeepSeek-V3): +20.6, +23.3, +15.9 | d04, d19 | C (K24) |
| Analogy and case generalisation is brittle | Letter-string analogies: humans 0.753 (136 participants); GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 on counterfactual alphabets. Fine-tuned transformers collapse inside held-out squares; rule-following fine-tuning gives over 95% at 12 digits | Lewis and Mitchell 2024 (b28); Hu 2024 (b29, c25) | E (K14) |
| Case-pair mining yields many candidate rules and needs an expert | 647 cases, 2344 itemsets, 208 kept | CABAMAKA (a09, b05, c19) | E (K16), no accuracy |
| Cases calibrate reasoning effort (needs RL) | BFCLv2 88.43% (Qwen2.5-7B), +5.85 over SFT, +4.76 over GRPO; reasoning length -26% | CAST, Pang 2026 (b18, c27) | S, not a scaffold |

## 4. Mechanisms and models

Each mechanism is written so an engineer can build it.

**4.1 Classic cycle.** (1) Retrieve top-k cases by similarity or an editability score. (2) Reuse: compute the problem difference (source vs target), pick adaptation knowledge, produce a candidate. (3) Revise: run a check; if it fails, repair from the failing output. (4) Retain: store the verified result, and optionally the edit.

**4.2 Typed edit (keep / drop / add).** From CABAMAKA (a09). Represent a solution as a set of parts. An edit is a diff: parts kept (=), lost (-), gained (+). The agent writes its adaptation as such a diff. Code checks that the edit touches only the parts the problem difference requires. Free-text "improve this" edits cannot be checked this way.

**4.3 Case difference heuristic.** Build pairs (A, B) from stored cases. Store delta_problem = B.problem minus A.problem and delta_solution = B.solution minus A.solution. To adapt: find the nearest stored case C to query Q, compute delta_problem = Q minus C, predict delta_solution with a learned model, apply it to C.solution. Ye et al. used features from a pretrained CNN (VGG-Face, 2622 dims), a Siamese or L1 retriever, and a network mapping problem difference to solution difference. Weak point: training pairs are random and far apart, so the model is poor on the small differences seen at test time (K05).

**4.4 Adaptation case library (leave-one-out).** For each stored case, retrieve its nearest neighbour among the rest and store the problem diff, the solution diff and the search that found the filler (DIAL, Jarmulak). Adaptation is then retrieval over this edit library. For an LLM agent the library holds records of (failing output, operator, fix).

**4.5 Error-keyed operator memory (TextBFGS).** Case = (diagnosis of an error, abstract fix rule). Key = the current failure signal, not the problem text. Loop: run code, get the error, retrieve k=3 operators by error, ask the LLM to apply one to the current code, run again, retain successful (error, operator) pairs. Case bases were small: 39 trajectories (HumanEval), 245 (MBPP).

**4.6 Structure first, then bind (CBR-to-SQL).** Stage 1 (Proposal): retrieve top-5 masked skeletons (entities replaced by slots) and draft. Stage 2 (Revision): look up the real entities in the database and let the LLM fix the draft to match the schema. The facts that make the draft right come from a lookup, not from model memory. The case base was shrunk from 8,000 to 774 skeletons (MIMICSQL) by clustering.

**4.7 Adapter prompt on one case (DS-Agent).** Deployment: retrieve one past solved task; prompt "adapt this solution to the new task with minimal edits"; execute; feed errors back. Development: retrieve k=5, 5 iterations, 5 debug steps, with ReviseRank (re-rank cases by execution feedback). Retain only verified successes; the authors flag an echo-chamber risk if LLM-written cases are stored unfiltered (b14).

**4.8 Workflow induction (AWM).** Abstract past successful trajectories into workflows with variables and insert them as guidance. Offline plus online workflows combined scored between the two, not above (b21). Workflows induced from wrong trajectories degrade results.

**4.9 Distilled memory items (ReasoningBank, Dynamic Cheatsheet, BoT).** The model writes a short strategy item from each success and failure. Retrieval returns items, not trajectories. BoT instantiates a high-level thought template per problem.

**4.10 Case selection by value (Memento).** Cases are (state, action, reward). The non-parametric selector uses similarity; the parametric selector learns a Q-function over cases. Learning curve, DeepResearcher, 5 iterations: no CBR 78.65 to 84.47, non-parametric 79.84 to 84.85, parametric 80.46 to 85.44 (b19).

**4.11 Edit versus resample as a budget choice.** Fresh-sample coverage rises log-linearly with N (d18). Edit wins when one verified feedback round is worth more than one extra sample (Self-Debugging, Snell). Edit loses when the feedback is the model's own opinion (Olausson, Huang).

**4.12 Distance gate (from Ye et al.).** Measure distance between the query and the nearest stored case. Close: reuse or solve directly. Far: retrieve and edit, or use a rule. For text, embedding distance is a placeholder [D].

## 5. What holds up

**Confirmed by two or more independent sources**
- A separate revise step after reuse pays when grounded in an outside check or lookup: DS-Agent (ReviseRank), CBR-to-SQL (entity lookup), Self-Debugging (tests), CRITIC (tools), Snell (verifier) (K02, K08, K20).
- Blind self-edit fails: Huang, Kamoi (survey), Zhang (dark side), Kumar, Snell (K08, K21).
- Few cases, not many: Memento, DS-Agent, Sourati all peak at K=1 to 4 (K03).
- Diagnosis quality sets edit quality: Olausson, Self-Refine, Self-Debugging (K09, K25).
- Raw old material can hurt strong models: Dynamic Cheatsheet and ReasoningBank (K22).
- Reuse is brittle at the edge of stored cases: Lewis and Mitchell, Hu et al. (K14).
- Small models in narrow domains gain a lot from retrieval plus an LLM adapter (K12).

**Single source, not replicated**
- DS-Agent headline numbers (authors' own benchmark, Kaggle case bank from the same distribution).
- All TextBFGS and CBR-to-SQL numbers (2026 preprints).
- Ye et al. distance finding (one dataset, one lab). NN-CDH is reported to show the same pattern, second-hand (a15).
- Memento additive gain (complex agent; contamination flagged on DeepResearcher).
- Error-keyed over problem-keyed retrieval (one dataset pair; the in-domain gap of 1 to 2 points on 45 tasks is about one task).

**Failures and null results**
- Siamese retrieval plus adaptation got worse in-distribution (7.49 to 7.86).
- Self-Refine on math: +0.0 to +0.2 at every base level (d04).
- CBR-RAG legal: +1.94% cosine on a high baseline (c26).
- AWM Mind2Web: whole-task success under 5% in every arm; cross-domain offline 0.7 vs baseline 1.0 (b22).
- Offline plus online workflow memory did not stack (b21).
- Mixtral-based DS-Agent had a worse mean metric than zero-shot on several tasks (a18).
- Dynamic Cheatsheet on GPQA, GPT-4o: 57.1 to 57.1 (d13).
- Self-generated exemplars give nothing for weak models (b27).
- Failure lessons stored raw hurt AWM (44.4 to 42.2) (d16).

**Moderators**
- Distance from memory (Ye): more help when far, none or harm when near.
- Base-model strength: edit gain on reasoning is about 0 near 93% base accuracy (d04); the pipeline gain held from 8B to 671B on a low-base task (d19). Contested.
- A verifier: the largest single factor (K08, K20).
- Narrow, templated domains: biggest gains (DomAgent, DS-Agent, CBR-to-SQL).
- Memory unit: depends on the task (ExpeL, K23).
- Case quality: a random case did not beat zero-shot for GPT-3.5 in DS-Agent; ExpeL random selection gave a significant drop.
- Joint tuning: retrieval and adaptation trained apart drift (K05).

**Interventions that worked**: execute and revise from real errors; one precedent; operator memory keyed on the failure; abstracting cases into items; adding failures to a distilled memory; a grounded entity lookup after structure retrieval.

**Interventions that did not**: asking the model to review its own answer; stuffing more cases; raw trajectory memory on cross-site transfer; mixing offline and online workflows; text insights in place of executable cases.

**Confounds**
- Almost all LLM evidence is 2024 to 2026 preprints from single labs; none replicated.
- DS-Agent ReviseRank gain is 0.5 rank on 12 tasks, 5 trials, no significance test.
- TextBFGS compares to TextGrad, not to plain resampling at equal tokens; its test sets are tasks the base model failed once (selection effect).
- Memento adds a planner and tools; the edit is implicit.
- Dynamic Cheatsheet has no equal-token control; the Game of 24 jump comes from a stored Python solver.
- Publication bias: papers that add an edit step report it helping (a32).

## 6. Language models

**What the LLM adapter does well**
- With one close precedent and an executor it adapts code to a new task: 85% (GPT-3.5) and 99% (GPT-4) one-pass vs 56% and 60% for the best baseline (DS-Agent).
- With a grounded lookup it fixes entities and schema: 0.786 to 0.894 execution accuracy (CBR-to-SQL).
- With a failure-keyed operator it fixes hard code tasks: MBPP-Hard Plus 48.72 to 78.63 (TextBFGS; a failure-selected set).
- In narrow domains it lifts small models: Qwen-7B 39.62 to 96.64 (DomAgent, proprietary).

**What it does badly**
- Finding its own errors. GPT-4 feedback was inaccurate in 32 of 80 cases (human 7 of 80) and expressed uncertainty 0 of 80 times (Olausson).
- Leaving correct answers alone. 38% flipped (Snell, naive revision model); 15.8% of items correct-to-incorrect (Gemini 1.5 Flash, base); 58.8% overturned (Llama-3.1-8B, doubt prompt).
- Mapping onto altered surfaces. GPT-4 0.452 vs humans 0.753 on counterfactual letter strings, with flat human accuracy across alphabets.
- Using many cases. Performance peaks at K=1 to 4 in three systems.

**What changed the result, and by how much**

| Change | Effect |
|---|---|
| Execution feedback in the loop | DS-Agent rank 2.58 to 2.08; Self-Debugging up to +12 with tests |
| Outside check vs none | GSM8K 74.7 to 84.3 and CSQA 41.8 to 89.7 with an oracle (an upper bound, not a deployable check) |
| Specific vs generic feedback | Sentiment 43.2 vs 31.2; Code Opt 27.5 vs 26.0 |
| Human vs model feedback | GPT-4 repair 1.58x |
| One case vs many | Memento +3.7 F1 at K=1; +0.9 more by K=4; nothing after |
| Error-keyed vs problem-keyed retrieval, cross-domain | 74.36 vs 58.12 (MBPP-Hard Plus) |
| Distilled vs raw memory | ReasoningBank 48.8 vs AWM 44.1; GPT-4o Game of 24 raw 6 vs baseline 10 |
| Adding failures to memory | +3.2 (ReasoningBank), -2.2 (AWM) |
| Training for revision (SCoRe, Snell) | SCoRe turn-2 gain +4.4 with 1.4% correct-to-incorrect; Snell matches best-of-N with up to 4x less compute |

**Model trends.** Stronger models show smaller edit gains on reasoning (Self-Refine math about 0 at 93%). Weaker models gain more from a close retrieved example but cannot generate their own (b27). Frontier 2026 models are untested for retrieved-case editing. Most numbers come from GPT-3.5, GPT-4, Qwen3-235B, Gemini-2.5-flash, Claude 3.5 Sonnet and GPT-4o.

**What no study shows.** No head-to-head isolates the adapt step against retrieval alone at equal tokens (K19). Adaptation-guided retrieval has no LLM test. The break rate for editing a retrieved case is not measured. CHEF-style pre-emptive failure prediction is not tested on LLMs.

## 7. What our agent should take

Marks: G guardrail, S state, O operator, M memory. Status: [E] established, [S] single source, [C] contested, [D] design choice.

### Add now (established)

1. **Gate every edit by an external check and keep the original.** The edit replaces the original only if the check passes. Part: G2, S5, S8 (already in the schema; make the keep rule explicit for O7). [E] K08, K21. Evidence: b25, b26, c23, d02, d08, d09, d10.
2. **Edit from the real failing output, with a separate specific diagnosis line.** The model names what is wrong in the actual output before editing. Part: S5, O7. [E] K09, K25. Evidence: b24, c22, d03, d07. The equal-token cost of a separate diagnosis call is untested (see Test first).
3. **Offer one to four cases, default one.** Part: O7, M. [E] K03. Evidence: a19, a21, a27, b11, b20, c03, c12, c15.
4. **Add a grounded revise step after reuse; fetch facts by lookup.** Where entities, schema or tool output can be looked up, fetch them and let the edit use them. Part: S5, O7. [E] K02. Evidence: a25, b12, c02, c09.
5. **Store only verified successes, and filter before showing.** No free-for-all store of raw old attempts. Part: M, G3. [E] K22 plus the DS-Agent echo-chamber note. Evidence: b14, d13, d14, d15.
6. **Probe a stored mapping on surface-altered variants before trusting it.** Part: G, O7. [E] K14. Evidence: b28, b29, c25.
7. **Name the edit types in O7:** substitute / delete / insert, merge, regenerate. Vocabulary only. [D] a17, b30, c28.
8. **Mine edit rules from solved pairs only after a failure, and validate by running.** Part: S9, M. [E] that mining works but needs validation (K16); the failure trigger is [S] (a30, b06, c20).

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Edit one retrieved case vs best-of-N fresh samples at equal tokens, same verifier, on a reasoning set | S5, O7 | [E] for self-edit with verifier (K20); retrieved-case version untested | d01, d06, d18 |
| Edit gain vs distance from memory (route by distance) | O7, S0 | [S] K04 | a05, b02, c17 |
| Editability-based case ranking vs similarity ranking | M, O7 | [S] K18 | a12, a13, b07, d12 |
| Error-keyed operator memory vs problem-keyed vs whole-solution memory | M, O7 | [S] K06, K07 | a23, a24, b16, b17, c07, c08 |
| Distilled lesson vs whole solution vs template, by task type | M | [C] K23 | d11, d13, d15, d17 |
| Pre-emptive failure warning from a failure index | M, G | [S] K17, K26 | a03, d16 |
| Separate diagnosis call vs edit-only at equal tokens | S5 | [E] direction, cost untested (K25) | d03, d07 |
| Case memory on top of a planner | M, S5 | [S] K10 | a20, a22, b19 |
| Edit gain on the strongest model, by base-accuracy bucket | S5, O7 | [C] K24 | d04, d19 |
| Self-recalled exemplars vs retrieved when memory is empty | O7 | [S] K13 | b27, c24 |
| Break rate of edits of a retrieved case | G | [E] for blind edits (K21); retrieved untested | d02, d09, d10 |
| Retrieval and edit tuned jointly (score retrieval by post-edit success) | M | [S] K05 | a06, b03, c18 |

## 8. Concrete tests on our bench

All arms get the same total token budget, counting retrieval, diagnosis and check calls. Report pass rate, tokens, and correct-to-incorrect and incorrect-to-correct counts for every edit arm.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Items with a check (our ARC set, checkable BRAINTEASER items) | (a) best-of-N fresh; (b) edit-one-retrieved-case with check, keep-if-pass; (c) edit own draft with check, no retrieved case | Pass rate at fixed tokens; (b) minus (c) = value of the retrieved example beyond the verifier | (b) and (c) beat (a) when a check exists (K20). (b) over (c) unknown; guess 0 to +5 points |
| T2 | Same items, bucketed by embedding distance to nearest memory case | direct solve vs edit-retrieved, per bucket | Pass rate per bucket; break-even distance | Edit wins in far buckets, ties or loses in near buckets (K04) |
| T3 | Items with a stored case library | Rank cases by similarity vs by estimated edit size (dry-edit diff size) vs random | Pass rate after edit | Editability ranking +2 to +5 over similarity (K18; Smyth-Keane unread) |
| T4 | Mixed items, no check available | blind edit with keep-original default vs verified edit vs no edit | Correct-to-incorrect and incorrect-to-correct rates | Blind edit net negative (K08, K21); verified edit net positive |
| T5 | Items with failed attempts, with a cross-domain split | Memory keyed on problem text vs on failure signature vs whole old solution | Pass rate; tokens; cross-domain gap | Failure-keyed wins cross-domain, ties in-domain (K06); token saving up to 30 to 50% (K07, single source) |
| T6 | K sweep | K = 0, 1, 2, 4, 8 retrieved cases at fixed total tokens | Pass rate by K | Plateau by K<=4; K=8 below K=4 on a strong model (K03) |
| T7 | Items of 3 task types (reasoning, action or planning, code) | memory unit: whole solution vs one-line lesson vs template; no-memory control | Pass rate by type; count of items worse than no-memory | Unit depends on type (K23); raw can fall below no-memory on a strong model (K22) |
| T8 | Edit-stage ablation | full vs without diagnosis line vs without edit | Pass rate at fixed tokens | Diagnosis adds 2 to 5 points; kept if it beats its token cost (K25) |
| T9 | Surface-altered variants of stored cases (renamed symbols, permuted constants) | edit retrieved case on original vs altered | Drop in pass rate | Larger drop than for a fresh solve (K14) |
| T10 | Top-1 removal | remove top-1 retrieved case; edit stage on vs off | Drop in pass rate | Edit-on drops less (K15, single source) |
| T11 | Failure index | warning from a matching stored failure shown before the first attempt vs after vs none | First-attempt and final pass rate | Small gain; the schema shows lessons only after the first attempt, so test both timings (K17, K26) |

## 9. What does not transfer, and why

- **Learned CDH adapters** (Ye, NN-CDH). They need many pairs and numeric features (a CNN on faces). We have no training and use text and code items. Keep only the idea problem diff to solution diff, written as a typed edit.
- **Hand-built critics and failure indexes (CHEF).** Domain-specific, one domain, no benchmark. The principle (explain the failure, store it by what interacted) transfers; the code does not.
- **Expert-filtered rule mining (CABAMAKA).** 208 candidate rules needed an analyst. Our code validator can replace the human only where a check exists.
- **CAST and Memento's parametric selector.** They need RL or training; our agent is a scaffold. Use the non-parametric version.
- **Gains in proprietary narrow domains (DomAgent truck CAN code).** Narrow, templated, internal documents, no public data. Large gains probably do not carry to open reasoning items.
- **DS-Agent one-pass numbers.** Cases and tasks come from the same Kaggle distribution, so neighbours are near. Our held-out items may be farther.
- **Hard-subset gains (TextBFGS).** Test sets were tasks the base model failed once, which inflates the case-base gain.
- **Oracle self-correction numbers.** The oracle gives the right stopping signal; no deployed check is that good (G3).
- **Human-feedback gains (Olausson 1.58x).** Humans are not in our loop.
- **Letter-string and arithmetic interpolation (Lewis, Hu).** Toy or fine-tuned settings; they transfer as a warning about the edge of memory, not as a rate.
- **Self-Refine open-ended gains** (sentiment, acronyms). Style tasks, not checked answers.

## 10. Open questions

1. At equal tokens, does editing one retrieved case beat best-of-N fresh samples on a reasoning (not code) task? No source tests it.
2. Does a retrieved example add value beyond the verifier? DS-Agent has both; Huang and Olausson have neither case.
3. Does adaptation-guided retrieval beat similarity retrieval with LLMs? The 1995 and 1998 numbers were never read.
4. What is the best unit (whole solution, workflow, error-operator rule)? TextBFGS, AWM, DS-Agent and ReasoningBank have never been compared on one benchmark.
5. Where is the break-even distance between query and memory for LLMs?
6. Do edit gains survive on frontier 2026 models, or shrink with base accuracy?
7. How often does editing a retrieved solution break a correct one (negative transfer, copy errors)?
8. Does a CHEF-style pre-emptive failure warning help LLM agents?
9. Does a separate diagnosis call pay for its tokens at equal budget?
10. What do Wilkerson and Leake 2024 and Leake and Ye 2021 report? Both are closed access and unread.
11. Do effects reported on 45 or 117 tasks with no confidence intervals (TextBFGS, DS-Agent rank) hold with more tasks or seeds?
12. Does an adaptation stage reduce reliance on near-exact matches (CBR-to-SQL robustness) beyond clinical SQL?

## 11. Sources

[V] opened and read by the extractors; [M] snippet or second-hand only.

- [V] Hammond (1986) CHEF. https://cdn.aaai.org/AAAI/1986/AAAI86-044.pdf (a01-a03)
- [V] Ye, Zhao, Leake, Wang, Crandall (2021) Case difference heuristic with deep network features. https://arxiv.org/abs/2107.07095 (a04-a06, b01-b03, c17, c18)
- [M] Hanney and Keane (1996) Learning adaptation rules from a case-base. https://doi.org/10.1007/bfb0020610 (a07, c21)
- [V] d'Aquin et al. (2006) Adaptation knowledge discovery from a case base. https://arxiv.org/abs/cs/0610156 (a08, b04)
- [V] d'Aquin et al. (2007) Case base mining for adaptation knowledge acquisition. https://arxiv.org/abs/cs/0703156 (a09, b05, c19)
- [M] Leake, Kinley, Wilson (1996) DIAL; Jarmulak, Craw, Rowe (2001); as described in https://arxiv.org/abs/cs/0703156 (a10, a11)
- [M] Smyth and Keane (1998) Adaptation-guided retrieval. https://doi.org/10.1016/s0004-3702(98)00059-9 (a12, d21)
- [M] Smyth and Keane (1995) Experiments on adaptation-guided retrieval in case-based design. https://doi.org/10.1007/3-540-60598-3_28 (a13)
- [M] Deja Vu experiments summary. https://edepositireland.ie/handle/2262/12782 (b07)
- [M] Jalali and Leake, ensemble adaptation-guided retrieval (b08, no URL)
- [M] Craw, Wiratunga, Rowe (2006) Learning adaptation knowledge to improve CBR. https://doi.org/10.1016/j.artint.2006.09.001 (b09)
- [M] Leake and Ye (2021) Harmonizing case retrieval and adaptation. https://doi.org/10.1007/978-3-030-86957-1_9 (a14, c29)
- [M] NN-CDH (Leake et al. 2021) and Wetzel et al. (2020), as described in https://arxiv.org/abs/2107.07095 (a15, a16)
- [V] Review of case-based reasoning for LLM agents (2025). https://arxiv.org/abs/2504.06943 (a17, b30, c28)
- [V] Guo et al. (2024) DS-Agent. https://arxiv.org/abs/2402.17453 (a18, a19, b10-b14, c01-c04)
- [V] Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153 (a20-a22, b19, b20, c12, c13)
- [V] Zhang et al. (2026) TextBFGS. https://arxiv.org/abs/2602.00059 (a23, a24, b15-b17, c05-c08)
- [V] Nguyen, Moen, Marttinen (2026) CBR-to-SQL. https://arxiv.org/abs/2603.05569 (a25, a26, c09, c10)
- [V] Sourati, Ilievski, Sommerauer (2023) CBR with language models for logical fallacies. https://arxiv.org/abs/2301.11879 (a27, c15, c16)
- [M] Wilkerson and Leake (2024) On implementing CBR with LLMs. https://doi.org/10.1007/978-3-031-63646-2_26 (a28, d20)
- [M] Kolodner (1993) and other textbook pointers. https://doi.org/10.1002/0471644676.ch4 (a29)
- [V] Badra, Cordier, Lieber (2009) Opportunistic adaptation knowledge discovery. https://arxiv.org/abs/0912.0132 (a30, a31, b06, c20)
- [V] Synthesis across opened sources, own tally (a32)
- [V] Pang et al. (2026) CAST. https://arxiv.org/abs/2605.15041 (b18, c27)
- [V] Wang, Mao, Fried, Neubig (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (b21, b22, c14)
- [V] Olausson et al. (2024) Is self-repair a silver bullet for code generation? https://arxiv.org/abs/2306.09896 (b23, b24, c22)
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b25, b26, c23)
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714 (b27, c24)
- [V] Lewis and Mitchell (2024) Counterfactual tasks and analogical reasoning. https://arxiv.org/abs/2402.08955 (b28)
- [V] Hu et al. (2024) Case-based or rule-based: how do transformers do the math? https://arxiv.org/abs/2402.17709 (b29, c25)
- [V] DomAgent (2026) KG and CBR for domain code generation. https://arxiv.org/abs/2603.21430 (b31, c11)
- [V] Wiratunga et al. (2024) CBR-RAG for legal QA. https://arxiv.org/abs/2404.04302 (c26)
- [V] Snell et al. (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314 (d01, d02)
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651 (d03, d04)
- [V] Gou et al. (2023) CRITIC. https://arxiv.org/abs/2305.11738 (d05)
- [V] Chen et al. (2023) Teaching LLMs to self-debug. https://arxiv.org/abs/2304.05128 (d06, d07)
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 (d08)
- [V] Kumar et al. (2024) SCoRe. https://arxiv.org/abs/2409.12917 (d09)
- [V] Zhang et al. (2024) Dark side of intrinsic self-correction. https://arxiv.org/abs/2412.14959 (d10)
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144 (d11, d12)
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (d13, d14)
- [V] Ouyang et al. (2025) ReasoningBank. https://arxiv.org/abs/2509.25140 (d15, d16)
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271 (d17)
- [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787 (d18)
- [V] Zhang et al. (2025) CBR-DDI. https://arxiv.org/abs/2505.23034 (d19)
- [M] Search-status notes (c30, d22): rate limits stopped a systematic 2020-2026 sweep; absence of a source here is not evidence of absence.
