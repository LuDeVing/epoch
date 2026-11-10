# Training and tutors: deep document

*Subfield E08.07. Focus: simulators and case libraries (Jonassen; Lesgold). Why it matters: a case library is a candidate memory for our agent. Evidence ids (a01 to d18) are in evidence_a-d.jsonl; claim ids (E08.07-K01 to K38) are in claims.jsonl; the cross-check is critique.md. Where this document and an evidence line disagree, the critique's corrections win.*

## 1. What it is

This subfield is about learning to troubleshoot from practice on simulated faults and from stored past cases. Two traditions meet here.

1. **Coached practice on a simulator (Sherlock, Hydrive).** Lesgold and colleagues built tutors for F-15 avionics test stations. Novices solve a fixed series of simulated faults. A coach gives hints that grow more specific as the trainee struggles. After each problem the trainee replays the work and sees the expert solution. The 1995 field test is the founding study (a01-a04).
2. **Case libraries (Jonassen and Tawfik; case-based reasoning).** A library of stored stories or cases of solved problems is offered to a learner, who retrieves a similar one, reuses it, revises it and retains the new case. The cycle (retrieve, reuse, revise, retain) comes from Schank's Yale group in the early 1980s and was formalised by Aamodt and Plaza (1994) (a11, secondary source only).

The same idea has come back in language-model agents. An agent keeps a bank of past episodes or distilled lessons and retrieves them at test time. No weights change. Memento, ExpeL, Agent Workflow Memory (AWM), ReasoningBank, Reflexion and Dynamic Cheatsheet are the main examples. In operations, RCACopilot and OM-RAG retrieve past incidents to diagnose new ones.

**Why it matters for our agent.** Our schema has a thin memory section (SCHEMA section 5: one-line lessons by problem class, shown after the first attempt; a class record; a planned subgoal library). The question is whether a real case bank should be added, what should be stored, how it should be retrieved, and when it may be shown. This document says: the human evidence is old, small and mostly not replicated; the agent evidence is large in headline size but comes mostly from one lab per method; and the harm side (wrong or misleading cases) is now measured and is serious.

**Scope notes.** Other subfields in this run cover related ground (Cognitive task analysis, Protocol analysis, Cognitive bias and premature closure, Instruction effectiveness, Debiasing, Analogical prompting for LLMs, ACT-R declarative memory, Software/KB debugging, Complexity of expert troubleshooting). We only link to them here.

## 2. History and theories in depth

**1980s: apprenticeship in a box.** Lesgold, Lajoie, Bunzo and Eggan (1988) built Sherlock I as a "coached practice environment" (a05). The motive was a training gap (a06). Routine work is about 95% of a technician's time, a test-station failure happens about once a month, and first-term airmen (under four years) get few chances to repair. A simulator can give the rare, hard cases on demand. The design: 34 problems of about 35 minutes each (about 20 hours total); everyone gets the same ordered series; only the specificity of hints is individualised; an average trainee sees about 45 hints; the expert solution is stored as an abstracted problem space and shown afterwards. In the sample problem the expert needed 7 steps and two trainees took 14 and 20. The 1988 paper itself said comparative experiments were not yet done.

**1989 to 1992: field tests and the student model.** Parker's NASA report (c01) describes tests at two Air Force wings: 16 tutored airmen (mean 28 months on the job), about 20 hours on the tutor, controls on normal duty (mean 37 months), an expert benchmark of about 114 months, and gains that held at a six-month delayed test (snippet-level). Katz and Lesgold (1992) (a07) gave Sherlock II a fuzzy student model: probability distributions over five skill levels, started at an equal 20%, updated from coded performance (Good, OK, Bad). Each goal-tree node was hand-coded with the knowledge it needs.

**1992: other troubleshooting tutors.** Johnson et al. (1992) (b03) tested a troubleshooting tutor in an aviation course: N=34 (16 control, 18 tutor), four faults on an aircraft electrical board. Tutor group solved 72% of problems; controls solved fewer than half. There was no difference in noticing that a fault existed. So the tutor improved fault location, not fault detection. Johnson and Chung (1999) (b04) added thinking-aloud pairs (effect sizes not read). Westerdahl (1991) (b05) found that novices taught expert methods plus a problem-space map solved a generator-set task faster than content-only novices (no numbers read).

**1995: the controlled evaluation.** Gott, Kane and Lesgold (1995) (a01-a04) is the founding quantitative study. See section 3.

**1997: the task-analysis theory.** Katz, Hall and Lesgold (1997) (a08-a10, b06) argue that skill has three layers: procedural (easy, observable), system knowledge (learned by acting on equipment) and strategic knowledge (what to do and when; develops last, after years). Experts and novices were equal in procedural skill and different in strategic skill. A tutor built from the PARI task analysis (Precursor, Action, Result, Interpretation) worked, while a hydraulics tutor built without it showed no learning effect, though the two tutors differ in content too, so this is confounded. Hydrive helped most where novices had to build their own strategy (problem A, no guide) and not where fault-isolation guides were available (problem B).

**1999 to 2006: theory of a learning environment.** Jonassen and Hung (2006) proposed a design for learning to troubleshoot: a layered system model, a simulator that forces hypothesis generation and testing, and a case library with a case-based reasoning cycle (b07). It reports no experiment. It claims that older methods (domain theory, fixed procedures) failed to produce transferable skill.

**2001 to 2020: case-library studies on humans.** Hernandez-Serrano and Jonassen (2003) (b08, d10): undergraduates solved ill-structured food-product-development problems. The experimental group read stories of similar solved problems, a comparison group read summaries, controls read unrelated text. The experimental group won on multiple-choice questions about process; short-answer showed no difference (authors blamed test fatigue). No N or effect size was obtained. Tawfik and colleagues ran a series: failure cases beat success cases (N=36, a13); a retrieve-and-reuse prompt did worse than no prompt (a15); recommendation libraries helped rebuttals (a16); novices struggle most with aligning and reusing cases (a18, N=5). Park et al. (2020) (a17, d12) is the one outside group: N=105, prompts to index cases by explanation or by difference raised self-explanation and rebuttal quality. Hsieh, Smith and Stephanou (2004) (a19) only proposed hint designs for a story library of about 110 stories.

**2011 to 2016: what tutors do on average.** The ITS meta-analyses (b01, b02, a12) show that step-based tutors beat large-group teaching and match, but do not beat, a good human tutor.

**2020 to 2026: the agent-memory wave.** Reflexion (2023), Voyager (2023), ExpeL (2023/24), AWM (2024), Dynamic Cheatsheet (2025), Memento (2025), ReasoningBank (2025/26) and Agent KB (2025) all store experience and reuse it. Independent benchmarks (EvoMemBench, Evo-Memory, the Compliance Trap, Execute-Distill-Verify) then measured the limits (d01-d09). In operations, RCACopilot (2023) and OM-RAG (2026) use past incidents (c05, c09). Cloud-OpsBench (2026) tested case reuse on agentic root-cause analysis (c11-c14, d02).

**Competing explanations for why a case library works.**
- *Strategy transfer.* The case shows what to test next. Support: Sherlock tutored novices ordered self-tests like masters (a04); strategic knowledge is the gap (a09, a10).
- *Surface matching.* The agent copies the nearest case. Support: agents copy retrieved cases when the new task looks like the old one (d01); gain rises with similarity, r = 0.56 to 0.72 (d07); exact-match success overstates transfer by about 50 points (d05).
- *Extra computation.* Memory methods often use more tokens (up to 3.6 times) and a stronger memory-free model often beats them (d08).
- *Practice in the Sherlock sense.* Not just retrieval: 20 hours of coached practice with fading hints, which no prompt-time library reproduces.

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources), **S** single source, **C** contested, **Su** supported (several sources of mixed independence).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Sherlock 2 lifted novices to master level on trained equipment | VTT3 59 control / 95 tutored / 85 masters; VTT4 58 / 91 / 86; NIT 75 / 87 / 86; N 23 / 18 / 13; t = -4.04, -3.72, -2.77 | Gott, Kane, Lesgold 1995 (a01); Parker 1990 (c01) | E (two reports of the same program; quasi-experimental) |
| Transfer to an unseen station, smaller than on trained gear | Frankenstation VTT 55 / 82 / 91 (n 21 / 17 / 12), t = -2.93, p = .006; NIT 72 / 80 / 88; fault solved in time 63.6 / 70.6 / 83.3% | a03 | S |
| Reported effect sizes are inflated by control spread | Reported 1.27, 1.17, .96 SD. Recomputed from means and SDs: about 0.97, 0.89, 0.87. Control SD 37 vs tutored SD 5 | a02; critique correction 2 | S (use "about 1 SD") |
| Tutor changed strategy, not just recall | Inefficient self-test use: controls 11 of 16, tutored 2 of 14, masters 4 of 12 | a04 | S |
| Hint-free strategy is where training matters | Hydrive: big effect on problem A (no guide), none on problem B (guide). Experts equal novices in procedural skill | a09, a10 | S |
| Task-analysis-built tutor worked, the other did not | Hydrive pre-post t[19] = 4.14, p < .001; F-15 Pneudraulics tutor (different input) showed no effect | a08 | S (confounded) |
| Tutor improves fault location, not detection | N = 34 (16/18); tutor group 72% solved vs controls under half; no detection difference | Johnson 1992 (b03) | S |
| ITS beat conventional teaching on average | Median +0.66 SD over 50 evaluations; g = 0.42 vs large group, 0.57 vs other computer teaching, 0.35 vs textbooks (107 effect sizes, 14,321 participants) | Kulik and Fletcher 2016 (b01); Ma et al. 2014 (b02) | E |
| ITS do not beat a human tutor | g = -0.11 (n.s.) vs individual tutoring; 0.05 vs small group (n.s.) | b02 | S (Ma); VanLehn 2011 via a secondary summary |
| Human case library: failure cases beat success cases | N = 36; better counterarguments and holistic argument, also in a no-library transfer case a week later | Tawfik and Jonassen 2013 (a13) | S |
| Human case library: forced retrieve/reuse prompts hurt | No-prompt and retain prompt beat retrieve/reuse on counterclaims and holistic score | Tawfik 2017 (a15) | C (abstract only) |
| Human case library: indexing prompts help | N = 105; explanation and difference prompts beat control on rebuttals | Park et al. 2020 (a17, d12) | S (outside group, section-level assignment) |
| Human case library: reading stories helps process knowledge | Multiple-choice win; no short-answer difference; no N | Hernandez-Serrano and Jonassen 2003 (d10) | S (abstract only) |
| Case memory helps an LLM research agent | DeepResearcher F1/PM: offline executor 48.8/62.8; no case memory 59.9/72.2; full 66.6/80.4. GAIA val 87.88 Pass@3, test 79.40 | Memento (a20, b19) | S |
| Out-of-distribution gain | F1 +5.0 (MuSiQue), +8.7 (Bamboogle), +6.1 (PopQA); PM +9.5, +9.6, +8.6. Quoted 4.7 low end not found; say about +5 to +10 | Memento (critique correction 3) | S |
| Retrieval depth saturates | K = 0 59.9/72.2; K=1 63.6/77.9; K=2 63.7/78.1; K=4 64.5/78.5; K=8 64.1/78.2; K=16 63.9/78.1; K=32 63.9/78.1 | Memento (b20) | S |
| Distilled lessons beat raw traces | WebArena (684 tasks), Gemini-2.5-flash: none 40.5, Synapse 42.1, AWM 44.1, ReasoningBank 48.8, with MaTTS 51.8. Pro: 46.7 / 53.9 / 56.3. Claude-3.7: 41.7 / 46.3 / 48.8 | ReasoningBank (a23) | S (the "AWM" figure is a re-implementation) |
| Failures help only if distilled | Shopping subset: no memory 39.0; RB success-only 46.5, with failures 49.7 (+3.2); AWM 44.4 to 42.2 (-2.2); Synapse 40.6 to 41.7 (+1.1) | a24, d17 | S |
| Memory and test-time scaling multiply | RB parallel k=1 49.7 to k=5 55.1; sequential 49.7 to 54.5. No memory: 39.0 to 42.2 and 37.4 to 40.6 (flat) | a25 | S |
| Workflow induction from experience | WebArena 35.5 vs 23.5 (+12.0 points, +51.1% relative), about 2.0 fewer steps; beats human-written SteP 32.0; Mind2Web +24.6% relative step success; out-of-distribution +8.9 to 14.0 points | AWM (a28, b18) | E (AWM plus ReasoningBank as baseline, direction only) |
| Insights plus retrieval beat either alone | ALFWorld ExpeL 59.0 vs ReAct 40.0; HotpotQA 39.0 vs 28.0. Insights-only / retrieval-only: HotpotQA 36/31, ALFWorld 50/55, WebShop 37/38 | ExpeL (a26, b15) | S |
| Case selection matters | ALFWorld: task-similarity 59.0, reasoning-similarity 48.5, random 42.5, none 40.0 (corrects c18) | ExpeL (b16) | S |
| Insights transfer across tasks | HotpotQA to FEVER: ReAct 58, transferred 63 to 70 (labels garbled) | a27 | S |
| Written reflection adds to episodic memory | Reflexion: ALFWorld +22, HotpotQA +20, HumanEval +11 (91% vs 80%); reflection adds 8 over episodic memory alone | Reflexion (a29, b23) | E (Reflexion, ExpeL, Dynamic Cheatsheet agree in direction) |
| Light text memory can give large gains | Claude 3.5 Sonnet AIME 2024 23 to 50%; GPT-4o Game of 24 10 to 99% (strong-prompt baseline 19%) | Dynamic Cheatsheet (b22) | S |
| Verified skill library | 3.3x unique items, 2.3x distance, up to 15.3x faster milestones; removing self-verification cuts items 73% | Voyager (b24, c21) | S |
| Structured past-incident retrieval | OM-RAG diagnosis accuracy 0.931 vs chunk retrieval 0.325 vs none 0.238 (1,172 issues, LLM-judged, 123 hand-checked) | Guan et al. 2026 (c09) | S |
| Chunk retrieval: grounded but wrong | Chunk groundedness 0.865 with accuracy 0.325 | c10 | S |
| Past-incident retrieval for cloud RCA | RCACopilot micro-F1 0.766 vs 0.026 for GPT-4 prompt only; 163 of 653 incidents (about 25%) had unseen causes | Chen et al. 2023 (c05, c06) | E (RCACopilot plus the fine-tuned incident work, c07) |
| Case reuse is not always helpful for agentic diagnosis | Cloud-OpsBench trajectory ICL: OnlineBoutique JRA 0.70 to 0.79, ECR 0.62 to 0.75; TrainTicket JRA 0.58 to 0.56, ECR 0.40 to 0.46; DeepSeek-V4-Flash TT 0.63 to 0.55; runbook SOP 0.71 / 0.60 | Cloud-OpsBench (c13, c14, d02) | Su |
| Premature stopping is the main LLM diagnosis failure | 73% of incomplete investigations stopped at the symptom log; GPT-5 correct but evidence-incomplete in 33.1% (OB) and 29.4% (TT) | c11, c12 | S |
| Wrong stored memory is followed and costs a lot | Step-1 compliance 63 to 72% across 5 models; Qwen3.5-27B 49.0 to 23.5, Gemini-3-Flash 46.3 to 27.8, Gemma-4-26B 38.1 to 30.9, Qwen3.5-9B 26.4 to 17.0; damage 9.5 to 26.0 points | Compliance Trap (d03) | S |
| Wrong lessons cost task success | Lesson kept 40 / removed 55 / corrected 65 (60 runs per cell); wrong-but-consistent lessons: self-reflection 22%, ReasoningBank 16%, EDV 5% (Retail) | EDV paper (d06) | Su |
| Add-all memory is worse than small fixed memory | CIC-IoT (network-traffic diagnosis) fixed 71.50, add-all 59.90, strict admission 85.40; history deletion 85.40 to 89.60 with 904 to 788 records; combined 904 to 188 records at 85.50 | Xiong et al. 2025 (d01, b21) | S (diagnosis only in CIC-IoT) |
| Gate before reuse removes most harmful reuse | Reuse-all authorises 8 of 8 harmful; gate 2 of 8 (25%) while keeping 9 of 10 beneficial; abstains about 41.7% | Knowing When Not to Reuse (d04) | S (fine-tuning updates, not prompts) |
| Independent runs show smaller gains | tau2-bench: no memory 76.4, ReasoningBank 79.0 (+2.6). EvoMemBench: DeepSeek 16K no memory 28.5, ReasoningBank 43.0, but memory-free Gemini-3-Flash 50.5; tokens 202,966 (BM25 memory) vs 55,787 plain | d06, d08 | Su |
| Gain tracks task similarity | r = 0.71 reported (Evo-Memory; 0.72 Gemini, 0.56 Claude); embodied navigation: episodic 100.0 at original start vs 51.7 to 66.0 at new start; summaries flat at about 44 | d07, d05 | Su |
| Abstract insights transfer; raw traces can harm | ALFWorld A to B forward transfer raw -9.5, insight +6.5; BabyAI raw -7.5, insight +9.0; one item served 88.5% of queries | d13 | S |
| Consult memory after a first failure | +10.4 on WebArena vs +1.3 for always-on helpful memory; closes 96 to 101% of gap to an oracle schedule | d03 | S |
| Planner and memory super-additive | SWE-bench Verified: baseline 28.5, planner 29.7, memory 30.1, both 33.5; interaction p = 0.011 | PMCoder (d16) | S |
| Agent structure is not reliably additive | HA@3 dataset A: Straight-Shot / ReAct / Plan-and-Execute: Qwen3-32B 0.36/0.35/0.30; Qwen3-4B 0.34/0.29/0.03 | d15 | S |
| Fault retrieval by signal shape is weak | NDCG@10: random 0.189, DTW 0.480, best combined 0.687, supervised 0.776 | READ-Bench (d14) | S |
| Auto-built experience nearly matches hand-written | GAIA 75.15 vs 76.97; SWE-bench Lite 51.0 vs 55.7; harm -7.7 in one cell | Agent KB (d09) | S |
| AI tutoring without guardrails harms learning | GPT Base practice +48%, exam -17% (p<0.05); GPT Tutor practice +127%, exam n.s. (nearly 1,000 students) | Bastani et al. 2025 (b10) | C |
| A guarded AI tutor can beat active learning | N = 194, effect about 0.63 | Kestin et al. 2025 (b11) | C |
| LLM access did not help physician diagnosis | 76% vs 74%, CI -4 to 8; LLM alone 92%; N = 50 | Goh et al. 2024 (b13) | S |
| LLM suggestions to tutors help weaker tutors most | +4 points mastery (62% to 66%, p<.01); +9 for lower-rated tutors; about $20 per tutor | Tutor CoPilot (b12, c23) | S |
| AI-supported STEM instruction | g about 0.67 random-effects, I2 = 83% (35 studies) | Dogan 2026 (b14) | S (heterogeneous) |

## 4. Mechanisms and models

Each item is written so an engineer can build it.

**4.1 Coached practice with fading hints (Sherlock).**
- Inputs: an ordered problem set (34 problems), an expert solution stored as a problem space (nodes: investigate unit under test, test point, test station), a student model.
- Loop: present a problem; student acts; if stuck, coach gives a hint; hint specificity rises with each request; after the problem, show the replay and the expert path.
- Student model: for each skill node keep a probability vector over five levels, initialised uniform at 0.2; update from a coded outcome (Good, OK, Bad) (a07).
- For an agent: treat the stored set as a practice set. Offline, run the agent on a graded fault set, record solved paths, and distil each into the form in 4.3. This is a training-time process that fills a bank. It is not something the agent does live.

**4.2 Case-based reasoning cycle.** Retrieve (nearest cases), reuse (adapt the old solution), revise (test and fix), retain (store the new case) (a11).
- Retrieve: embedding similarity over the problem description. Memento adds a learned case-selection policy (a Q-function), and K=4 was best (b20).
- Reuse: put the full retrieved case (problem plus solution) in the prompt. CBR-RAG found that the full case beat a no-retrieval baseline by 0.9141 vs 0.8967 cosine (N=32, Mistral-7B) (c04). Tiny sample.
- Revise: DS-Agent's revise step, which adapts the retrieved case with execution feedback, beat plain RAG (a30): deployment one-pass 99% with GPT-4 vs best baseline 60%.
- Retain: admit only a verified case (4.5).

**4.3 What a case record should contain.** Evidence points to storing an abstract, verified lesson, not a raw trace:
- ReasoningBank stores title, description and content of a strategy, distilled from both success and failure (a23).
- ExpeL stores trajectories and separately extracted rules (a26).
- Insight-level records transferred better than raw ones to harder targets (d13).
- OM-RAG indexes symptom, root cause, resolution triples (c09).
- Park et al.: add a "why it matches" and "how it differs" line (d12).

Proposed record: {fault family, symptom set, tests run in order with results, confirmed cause, rejected hypotheses and why, one-line strategy, difference note, provenance, verifier status, use count, success-after-use count}.

**4.4 Index choice.** Options: by symptom, by cause, by device family, by strategy. No head-to-head test exists. Indirect: symptom-to-cause triples beat text chunks by 0.931 vs 0.325 (c09); signal-shape similarity is a weak proxy (d14); a sparse index can send 88.5% of queries to one item (d13). Index by structured fields, and measure retrieval spread.

**4.5 Admission gate and pruning.**
- Verify each lesson before storing: a verifier step cut wrong-but-consistent lessons from 16% to 5% (d06).
- Strict ground-truth admission beat add-all on every benchmark in d01.
- Prune by use history: records 904 to 188 at no loss on CIC-IoT (d01).
- Cap the bank. Memento's bank saturated after about 3k items (a20).

**4.6 Reuse gate.** Compliance with advice at step 1 is 63 to 72% even when the advice is wrong (d03). Two designs:
- Timing: show cases only after the first hypothesis fails (+10.4 vs +1.3 on WebArena, d03). This agrees with our SCHEMA rule of showing lessons after the first attempt.
- Match gate: abstain when similarity or a structured match check is poor. Evidence is thin: a gate worked for fine-tuning updates (harmful reuse 100% to 25%, d04), but relevance gating gave no consistent gain in the Compliance Trap (d03). A "verify first" warning cut damage and also cut the benefit of correct memory.

**4.7 Memory plus sampling.** In ReasoningBank, parallel k=5 with memory went 49.7 to 55.1, while the same scaling without memory stayed flat (39.0 to 42.2) (a25). The mechanism claimed: memory gives contrast between samples. This is a single-lab result.

**4.8 Human-side mechanisms (for hypotheses only).** Think-aloud of novices using case libraries shows five steps: generate an index, prioritise, align with prior knowledge, abstract, reuse; alignment and reuse were hardest (a18). That predicts an agent will fail at the align and reuse steps, which is where wrong-nearest-case harm arises.

## 5. What holds up

**Holds up.**
- ITS beat conventional teaching on average (two meta-analyses, 50 and 107 effect sizes) and match human tutors (b01, b02). Moderator: locally built tests give bigger effects than standardised tests; six studies with nonconventional controls and four with flawed implementations gave small effects (b01).
- Retrieval of past experience helps agents in many settings, in direction: Memento, ExpeL, AWM, ReasoningBank, Reflexion, Evo-Memory and RCACopilot all agree. Independent benchmarks agree on direction but not on size (d06, d07, d08).
- Distilled, verified lessons beat raw traces (ReasoningBank, d13, d01).
- Memory quality matters: add-all fails, strict admission wins (d01, d06).
- Retrieval depth saturates around K = 4 (Memento) (b20).

**Does not hold up, or is weak.**
- Sherlock: one field study, 3 bases, small N, matched not randomised; the test is a scored verbal protocol rated by the study team; the tutor trained on the same station as the test; tutored airmen got about 20 hours of practice and controls did not; effect sizes in the report are not reproducible from its own table (a01, a02, critique). The 1988 paper admitted that comparative work had not been done (a05). No independent replication exists.
- Human case-library effects: almost all from one lab (Tawfik), small N (22 to 91), argumentation tasks, no fault diagnosis. Only abstracts were read. Retrieval/reuse prompts did worse than no prompt (a15). No outside replication of Jonassen's effect (b27, d11).
- Agent memory gains are mostly single-paper and inflated. The independent ReasoningBank run gave +2.6 (d06); EvoMemBench shows a stronger memory-free model beating every memory method in many cells and memory methods costing 2 to 4 times the tokens (d08). No third-party replication of Memento or ExpeL was found.
- Cloud-OpsBench: trajectory reuse hurt on the bigger system (TrainTicket) for two of three models; runbook distillation was mixed (d02). Experience came from a stronger model (GPT-5); one run per cell; 0.03 to 0.08 differences may be noise.

**Moderators.**
- Task similarity: gain rises with similarity (r 0.56 to 0.72, d07). Out-of-family faults get less (Sherlock Frankenstation, a03; embodied navigation loss of about 48 to 49 points at a new start, d05).
- Number of stored episodes: raw episodic retrieval improves with more demos (51.7 to 66.0 from 1 to 4); summaries do not (d05).
- Model strength: small models gain little from a memory of strategies (b22); a stronger base model can beat memory (d08).
- Gain grows with the train-test gap in AWM (c22), but harm grows with it in other results (d13). These do not conflict only if the case is abstract.
- Guardrails and design decide whether a helper hurts or helps humans (b10 vs b11).

**Interventions that did not work.**
- Forcing case retrieval and reuse by prompt (humans, a15).
- Reflections added to rule extraction (ExpeL, hallucinated insights hurt: 29.0 vs 32.0 hand-crafted, b16).
- Success-only workflow memory when failures were added raw (AWM 44.4 to 42.2, a24).
- Raw failed trajectories in a simple retrieval baseline (d07).
- Giving physicians an LLM (b13).

## 6. Language models

**6.1 Agent tasks: how much does a case bank add?** See the table in section 3. Headline sizes: Memento +6.7 F1 (a22); AWM +12.0 points; ReasoningBank +8.3 points over none for Gemini-flash (40.5 to 48.8); ExpeL +19 on ALFWorld (59.0 vs 40.0); Reflexion +22. Independent runs: +2.6 (tau2, d06); Evo-Memory multi-turn 0.27 to 0.46 (ExpRAG) for Gemini-2.5-Flash and 0.24 to 0.63 for Claude 3.7 Sonnet, with single-turn nearly flat (0.59 to 0.60; 0.54 to 0.59) (d07). Treat published gains as upper bounds (K31).

**6.2 Fault diagnosis specifically.**
- RCACopilot: 0.766 micro-F1 vs 0.026 prompt only; fine-tuning alone gave 0.103 (c05). About 25% of incidents had unseen causes (c06), so retrieval must handle novelty.
- OM-RAG: 0.931 vs 0.325 vs 0.238 (c09). LLM-judged. Chunk retrieval was most "grounded" and still wrong (c10).
- Cloud-OpsBench: ICL trajectories +0.09 JRA on OnlineBoutique, -0.02 on TrainTicket (d02). Base JRA per model: DeepSeek-V4-Flash 0.76 / 0.63, Gemini-2.5-Flash 0.65 / 0.53, Qwen3.5-27B 0.70 / 0.58 (OB / TT) (c28). Harness token cost: ReAct 55.13K (OB) and 129.46K (TT); Reflection 76.82K and 230.78K (d02, d18).
- Failure modes of LLM diagnosis: anchoring, stalled progress, arbitrary evidence selection (d15); 73% of incomplete cloud investigations stopped at the first symptom log (c12). These are the problems a case library or scaffold must fix, and they are about premature closure, not missing knowledge.
- AgentRCA, a zero-shot agent with a digital twin and no case library, was competitive with supervised baselines on two industrial facilities (c26, scores not extracted). A case library is not the only route.
- CIC-IoT traffic diagnosis: strict admission 85.40 vs add-all 59.90 (d01).
- Battery failure retrieval: press release claims 19.7% average gain (c27, snippet only; not usable).

**6.3 Harm.**
- Wrong memory is followed 63 to 72% at step 1 and costs 9.5 to 26 points (d03).
- A wrong stored lesson costs 15 to 25 points (40 vs 55 vs 65, d06).
- Agents copy the nearest case when the task looks similar (d01).
- Unfiltered failures hurt a simple retrieval baseline (d07).
- The AI-tutor RCTs show the same split for humans: no guardrails, harm (-17%); guardrails, no harm (b10).

**6.4 Tokens.** Memory is not free. EvoMemBench: 202,966 vs 55,787 tokens (up to 3.6x) and often a loss to a stronger memory-free model (d08). Only one result separates memory from extra compute: memory-free scaling was flat in ReasoningBank (a25). No study compares a case bank with self-consistency at equal tokens for diagnosis (d18). That is the main gap.

**6.5 Interaction with scaffolds.** Planner x memory was super-additive on SWE-bench Verified (28.5, 29.7, 30.1, 33.5; p = 0.011) but memory there is the agent's own history (d16). Plan-and-Execute was worse than Straight-Shot for small models in RCA (Qwen3-4B 0.34 vs 0.03) (d15). Nothing tests guardrails and states plus a case bank.

**6.6 Auto-built banks.** Auto-built experience nearly matches expert-written (75.15 vs 76.97 GAIA; 51.0 vs 55.7 SWE-bench Lite) with some -7.7 cells (d09). A bank can be built from the agent's own runs if admission is strict.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Show stored lessons after the first attempt, not before. Already in SCHEMA section 5; now backed by a timing result (+10.4 vs +1.3 after a first failure) | S (after S4 fail) / M | [E] for the rule already in the schema (F11, F06); the timing numbers are [S] | d03 (K38) |
| Store verified, one-line, abstract lessons by problem class, and never admit unverified ones | M | [E]: three independent sources agree (admission control, wrong-lesson cost, add-all drift) | d01, d06, b21 (K17, K28, K29) |
| Keep failure lessons only as lessons with a diagnosis line, not as raw failed traces | M | [E] that raw traces and add-all hurt; the benefit of distilled failures is [S] | d17, d07, d13 (K11) |
| Retrieval depth small, about 4 | M | [S] one dataset; low risk because the schema already shows few lessons | b20 (K09) |
| Treat retrieved case text as evidence to check, not as an answer; a revision must still cite a real failing output | G2, G3, G10 | [E] (existing guardrails applied to cases) | d03, d01 (K27) |
| Report gain on repeat faults and novel faults separately | G7 (bench) | [E] practice, backed by two similarity results | d05, d07 (K35) |
| Compare any case bank to the plain model and to extra sampling at equal tokens | G7 | [E] as a rule already in the schema | d08, d18 (K32) |

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Case bank (symptom to cause to test sequence) for fault items, consulted at S6 or after the first failed hypothesis | M, S | [S] | a20, c05, c09, d03 |
| Abstain-on-poor-match rule | M, G | [S] (only a fine-tuning analogue) | d04, d03 |
| Distilled strategy items vs raw trajectories | M | [S] | a23, d13 |
| Cause-and-strategy index vs symptom-only index | M | [S]; no head-to-head exists | c09, d14, d12 |
| Failure-case lessons with a diagnosis line | M | [S] | a24, d17 |
| Memory plus sampling at equal tokens | O, M | [S] | a25 |
| Insight plus retrieval vs retrieval only | M | direction [E] (Reflexion, ExpeL), size [S] | a26, b23 |
| Strategy hint in the prompt (Hydrive) vs case library | G, M | [S] human only | a09, a10 (K05) |
| Evidence-before-verdict step (source tracing before conclusion) | G, S | [S] for the 73% figure | c11, c12 (K21) |
| Verify-before-act step on retrieved cases | G | [S]; the warning cuts both harm and benefit | d03 |
| Auto-built bank vs expert-written bank | M | [S] | d09 |
| Case bank inside the full scaffold vs bare agent | S, M | [S] one hint | d16 |
| Cross-device-family held-out transfer | M | [S] | a03, d05 |
| Case-use audit (answer-copy rate, evidence-complete rate) | G | [S] | b13, b10, c12 |

## 8. Concrete tests on our bench

All tests use the same model, the same held-out fault items and the same total token budget in both arms. The case-bank arm pays for retrieval and the bank text in its budget. Report each result by item type (repeat, same-family novel, out-of-family) and by model.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Held-out diagnosis items with a known fault; bank built from a disjoint set of solved items | A: plain scaffold, budget B; B: scaffold with 4 retrieved cases after the first failed hypothesis (bank cost deducted from B); C: scaffold with self-consistency using the same extra tokens | Final-answer accuracy; evidence-complete rate; tokens | Small gain on repeat faults, about 0 on novel; bank beats C only if the effect is more than sampling |
| T2 | Items with a planted plausible-but-wrong nearest case (30% of items) | A: no abstain rule; B: abstain when a structured match check fails; C: no bank | Accuracy on planted items; harm = C minus A | A loses 10 to 25 points vs C (d03, d06); B recovers most of it |
| T3 | Mixed repeat and novel faults | A: raw successful traces; B: distilled lesson with difference note; C: distilled plus failure lessons | Accuracy by novelty bucket | B above A on novel items by about +5 (d13); C adds about +3 (d17) |
| T4 | Same items | Index by symptom vs by cause/strategy vs by device family | Accuracy; share of queries served by the top-1 item | Structured index wins by a clear margin; watch for one-item dominance (d13) |
| T5 | Items with a fixed strategy hint available | A: hint only; B: hint plus bank; C: bank only | Accuracy | Bank adds little once the hint is given (K05); if it adds more than 3 points, keep both |
| T6 | Repeated sessions of 200 items | Add-all vs strict admission vs strict plus pruning | Accuracy over episodes; bank size | Add-all drifts down; strict wins by 10 or more points (d01) |
| T7 | Whole held-out device family | Bank with the family vs bank without | Gain gap in-family vs out-of-family | Gain drops by about half or more (a03, d05) |
| T8 | Short vs long budget | k samples without bank vs fewer samples with bank at the same tokens | Accuracy | Bank gains more when k is larger (a25) |
| T9 | Audit on T1 output | Log whether the cited cause appears in the retrieved case but not in tool output | Answer-copy rate; accuracy when copy-only | Copy-only answers less accurate than evidence-backed ones |

## 9. What does not transfer, and why

- **Twenty hours of coached practice.** The Sherlock effect came from a human spending 20 hours with graded hints. A prompt-time bank has no such practice. The offline analogue is building the bank by running the agent over a graded set (the retain step), which is not the same thing.
- **Student modelling.** Sherlock's fuzzy student model tracks the learner's skill. Our agent has no persistent learner; the class record in SCHEMA section 5 is the nearest thing.
- **Human case-library results.** They come from argumentation tasks with students and show forced retrieval prompts hurting. The mechanism (novice cannot align and reuse) may differ for a model, which can read case text at low cost. We use them only as hypotheses (K24).
- **Tutor RCT results (Kestin, Bastani, Tutor CoPilot).** They teach humans. They say little about an agent using memory. One lesson carries: a helper that gives answers can reduce the user's own derivation, so a case helper must not replace the agent's checked derivation (b10).
- **Web and QA agent gains.** WebArena, GAIA, ALFWorld and HotpotQA have repeated task templates, so similarity is high. Fault diagnosis had about 25% unseen causes in the Microsoft data (c06). The gain from similarity will not carry over.
- **Press-release and proprietary results** (BattFailScholar, c27; industrial CBR test-script work, a31) are not usable as evidence.
- **Domain size.** Sherlock covered one avionics system. Cloud RCA covers 57 fault types; physical device troubleshooting differs again.
- **Knowledge as the key gap.** In LLM diagnosis the failure is stopping early (c12), not missing knowledge, so a library of facts addresses the wrong problem unless it carries strategy.

## 10. Open questions

1. At equal tokens, does a case bank beat self-consistency or longer reasoning for fault diagnosis? No study exists (d18).
2. What is the harm rate when the nearest case is wrong, on diagnosis items, and does abstention remove it? Only analogues (d03, d04, d06).
3. Is there any third-party replication of Memento, ExpeL or AWM on a diagnosis benchmark? None found.
4. Which index works best: symptom, cause, family or strategy? No head-to-head.
5. Do failure cases with a diagnosis line help more than success cases in troubleshooting? ReasoningBank says yes for web; unknown for diagnosis.
6. How large is the Hydrive-style strategy-hint effect on a language model, and does a bank add anything once the strategy is stated?
7. How many cases and what mix of novel and familiar faults are needed before gains appear? Sherlock used 34 problems; Memento saturates near 3k items.
8. How does a bank interact with a fixed scaffold (guardrails and states): additive, redundant or conflicting? One hint of super-additivity (d16).
9. What did Hernandez-Serrano and Jonassen report in numbers (N, effect size)? Only abstracts were read.
10. Do the Sherlock gains last? Parker mentions a six-month check, read at snippet level (c01).
11. Does the effect depend on model strength? Small models gain little from strategy memory (b22), and a stronger memory-free model often wins (d08).
12. Why did Cloud-OpsBench trajectory reuse help on one system and hurt on another? Retrieval quality, system complexity or noise (one run per cell).

Links to parallel subfields in this run: Cognitive task analysis, Protocol analysis, Cognitive bias and premature closure, Instruction effectiveness, Debiasing and cognitive forcing, Analogical prompting for LLMs, Readings in model-based diagnosis, Complexity of expert troubleshooting, Software, spreadsheet, KB debugging, ACT-R declarative memory, Scaffolding and guided discovery, Productive failure, Transactive memory and reasoning.

## 11. Sources

[V] means the page was opened by a research agent. Several [V] human case-library entries were read at abstract or ERIC-record level only; the line says so. [M] means snippet or secondary only. The d-series pages were read through a summarising fetch of the first 100k characters, so their numbers are one level less certain than a direct read (critique).

1. [V] Gott, Kane, Lesgold (1995) Tutoring for transfer of technical competence (Sherlock 2 evaluation). https://files.eric.ed.gov/fulltext/ED382817.pdf (a01-a04; table figures confirmed in the critique)
2. [V] Lesgold, Lajoie, Bunzo, Eggan (1988) Sherlock: a coached practice environment for an electronics troubleshooting job (a05, a06)
3. [V] Katz and Lesgold (1992) Use of fuzzy modeling techniques in a coached practice environment (a07)
4. [V] Katz, Hall, Lesgold (1997) Cognitive task analysis and intelligent computer-based training systems (a08-a10); Katz and Hall (1997) https://eric.ed.gov/?id=ED411309 (b06)
5. [M] Wikipedia: Case-based reasoning (a11); Wikipedia: Intelligent tutoring system (a12)
6. [V, abstract only] Tawfik and Jonassen (2013); Tawfik, Kim, Hogan, Msilu (2019); Tawfik (2017); Tawfik, Kim, Kim (2020); Tawfik et al. (2019) novices and case libraries (a13-a16, a18, d11), via ERIC https://api.ies.ed.gov/eric/
7. [V, abstract only] Park, Park, Jung, Kim (2020) Promoting case indexing in case library learning (a17, d12), via ERIC
8. [V, abstract only] Hsieh, Smith, Stephanou (2004) explicit hints in storytelling (a19)
9. [V] Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153 (a20-a22, b19, b20, c15, c16; re-opened by the critique)
10. [V] Ouyang et al. (2025/26) ReasoningBank. https://arxiv.org/html/2509.25140 (a23-a25, d17; re-opened by the critique)
11. [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144 (a26, a27, b15-b17, c17-c19; re-opened by the critique)
12. [V] Wang, Mao, Fried, Neubig (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (a28, b18, c22; re-opened by the critique)
13. [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (a29, b23, c20)
14. [V] Guo et al. (2024) DS-Agent (a30); Guo et al. (2025) CBR for functional test script generation (a31)
15. [V] Kulik and Fletcher (2016). https://eric.ed.gov/?id=EJ1090502 (b01); Ma, Adesope, Nesbit, Liu (2014). https://eric.ed.gov/?id=EJ1049508 (b02; abstract-level)
16. [V, abstract only] Johnson et al. (1992). https://eric.ed.gov/?id=ED351602 (b03); Johnson and Chung (1999). https://eric.ed.gov/?id=EJ596672 (b04); Westerdahl (1991). https://eric.ed.gov/?id=ED339360 (b05)
17. [V, abstract only] Jonassen and Hung (2006). https://eric.ed.gov/?id=EJ747007 (b07); Hernandez-Serrano and Jonassen (2003). https://doi.org/10.1046/j.0266-4909.2002.00010.x (b08, d10); Lajoie and Lesgold (1989). https://eric.ed.gov/?id=EJ410569 (b09)
18. [V] Bastani et al. (2025) Generative AI without guardrails can harm learning. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12232635/ (b10; not re-opened by the critique)
19. [V] Kestin et al. (2025) AI tutoring outperforms in-class active learning. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12179260/ (b11; not re-opened)
20. [V] Wang et al. (2024) Tutor CoPilot. https://arxiv.org/abs/2410.03017 (b12, c23, c24; re-opened)
21. [V] Goh et al. (2024) LLM influence on diagnostic reasoning. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11519755/ (b13; not re-opened)
22. [V] Dogan et al. (2026) AI-supported instruction in STEM, meta-analysis. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13302280/ (b14)
23. [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/html/2505.16067 (b21, d01)
24. [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (b22)
25. [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291 (b24, c21)
26. [V] Das et al. (2021) Case-based reasoning for natural language queries over knowledge bases. https://arxiv.org/abs/2104.08762 (b25)
27. [V] Wiratunga et al. (2024) CBR-RAG. https://arxiv.org/abs/2404.04302 (b26, c04; re-opened)
28. [M] Gap note on replication (b27). https://eric.ed.gov/?id=EJ675076
29. [V] Parker (1990) Success in tutoring electronic troubleshooting, NASA. https://ntrs.nasa.gov/citations/19900016252 (c01, c02; snippet-level on the delayed test)
30. [M] Shute (1991) review of ITS evaluations. https://myweb.fsu.edu/vshute/pdf/shute%201991_c.pdf (c03; scanned PDF, not extractable)
31. [V] Chen et al. (2023) RCACopilot. https://arxiv.org/abs/2305.15778 (c05, c06)
32. [V] Ahmed et al. (2023) Recommending root-cause and mitigation steps for cloud incidents. https://arxiv.org/abs/2301.03797 (c07, c08)
33. [V] Guan, Xu, Rogers (2026) OM-RAG. https://arxiv.org/abs/2607.21911 (c09, c10)
34. [V] Wang, Yu et al. (2026) Cloud-OpsBench. https://arxiv.org/abs/2603.00468 and https://arxiv.org/html/2603.00468 (c11-c14, c25, c28, d02; not re-opened by the critique)
35. [M] Wei and Fink (2026) AgentRCA. https://arxiv.org/abs/2607.22385 (c26; scores not extracted)
36. [M] BattFailScholar press release. https://www.eurekalert.org/news-releases/1135775 (c27)
37. [V] Compliance Trap (2026). https://arxiv.org/html/2607.10608 (d03)
38. [V] Knowing When Not to Reuse (2026). https://arxiv.org/html/2608.26730 (d04)
39. [V] MemTransfer (2026). https://arxiv.org/html/2609.32313 (d05)
40. [V] Escaping the Self-Confirmation Trap, Execute-Distill-Verify (2026). https://arxiv.org/html/2606.24428 (d06)
41. [V] Evo-Memory (2025). https://arxiv.org/html/2511.20857 (d07)
42. [V] EvoMemBench (2026). https://arxiv.org/html/2605.18421 (d08, d18)
43. [V] Agent KB (2025). https://arxiv.org/html/2507.06229 (d09)
44. [V] When continual learning moves to memory (2026). https://arxiv.org/html/2604.27003 (d13)
45. [V] READ-Bench (2026). https://arxiv.org/html/2609.32123 (d14)
46. [V] Stalled, Biased, and Confused (2026). https://arxiv.org/html/2601.22208 (d15)
47. [V] PMCoder (2026). https://arxiv.org/html/2608.06811 (d16)
