# Laboratory notebook studies: deep document

*Subfield D07.02. Reconstructing a working scientist's steps. Key works: Holmes on Krebs; Gruber on Darwin. Why it matters for our agent: impasse (S6), look back (S9), and the real order of operators.*

*Honesty note up front. The founding texts (Holmes 1980, 1991, 1993, 2004; Gruber 1974; Grasshoff and May 2003; Dunbar 1997; Tweney 1985) were NOT opened. Paywalls and a quota-limited search stack blocked them. The one founding-era text read in full is Kulkarni and Simon (1988), which paraphrases Holmes with dates. Every founding number below comes from that paraphrase or from Wikipedia. The LLM evidence (DiscoveryWorld, ScienceAgentBench, FIRE-Bench and others) was re-opened and checked against the paper text. No LLM study was found that replays a historical notebook and scores operator order against the record. Evidence ids (a01, d03 ...) refer to evidence_a-d.jsonl; claim ids (K01 ...) to claims.jsonl, both in this folder.*

## 1. What it is

Laboratory notebook studies rebuild how a scientist actually worked, step by step, from records made at the time: lab books, diaries, letters. Some add interviews with the scientist.

The question is not "what did the scientist conclude". It is "what did the scientist do, in what order, and what made the next step follow". This is process tracing. It yields a real sequence of operators: screen, get a surprise, check the method, check the scope, build an explanation, test it, publish.

Two founding families:
- Holmes (historian of biology). Rebuilt Claude Bernard (1840s notebooks, PhD Harvard 1962), Lavoisier, Hans Krebs (biography vol. 1 1991 covering 1900-1933; vol. 2 1993 covering 1933-1937), Meselson and Stahl (2001), Benzer. Method: notebooks plus long interviews with the living scientist. Later book: Investigative Pathways (2004), arguing that investigations run as sequences of linked experiments, each shaped by the prior result. (a01, a03, a17, a18, b03.)
- Gruber (psychologist). Darwin on Man (1974). Treated a creator as a person in a "network of enterprise": several long projects at once, over years. Darwin's notebooks B to E, M and N (1837-39) show parallel streams of thought. (a02, a21, a22, b04.) Only Wikipedia was opened for Gruber, and that page does not mention the notebooks.

Related computational and cognitive work:
- Kulkarni and Simon (1988): KEKADA, a production system that simulates Krebs's urea work with surprise-driven rules. (d01-d04.)
- Grasshoff and May (1995, 2003): the Urea Modeler, a PROLOG then Java simulation of the Krebs and Henseleit 1932 discovery, built from both complete notebooks. Used to study experimental design, instrument set-up, error correction and the origin of hypotheses. The project page gives no quantitative results. (c01, d05.)
- Nickelsen and Grasshoff (2009): error in experimental research, again on the Krebs episode. Not read. (b02, b08, d16.)
- Tweney (1985): cognitive reading of Faraday's diaries; confirming and disconfirming tests, parallel lines. Not opened. (a24, b11.)
- Dunbar (1997) and Dunbar and Fugelsang (2004-05): in vivo study of molecular biology lab meetings. The often-quoted "about half of findings unexpected" is memory only and must not be cited as a number. (a25, b09, d06.)
- Klahr and Dunbar (1988): dual-space search (experiment space and hypothesis space). Not opened. (b10.)
- Langley (1987): BACON, data-driven law finding. Not opened. (a27.)

The modern descendant is the LLM discovery agent. These agents keep their own notebooks (notes.txt in the AI Scientist; a status-tagged hypothesis log in DiscoveryWorld's Hypothesizer; a structured experiment notebook in Safdar and Saadeldin). So the method has two uses for us: (1) a template for what a real operator trace looks like, and (2) a way to audit our own agent's logs.

## 2. History and theories in depth

### 2.1 Bernard, Lavoisier, Krebs: Holmes's method (1960s-2004)
Holmes began with Bernard's notebooks and found that daily records show a messier, more gradual path than the published account. For Krebs he had lab books and many interviews, so he could check memory against the contemporaneous record. The same two-source method was used for Meselson and Stahl. (a01, b03.)
His own remark, quoted in Kulkarni and Simon: he once expected to find a gestalt switch in Krebs's work, but the reconstruction shows a gradual path. (d04.) This is the central finding of the field for us: discovery is a sequence of small, local steps, not one flash.

### 2.2 The Krebs 1931-32 sequence (as paraphrased by Kulkarni and Simon from Holmes)
Krebs and his student Kurt Henseleit found the ornithine (urea) cycle in 1932 using liver slices in Warburg manometers. It is called the first metabolic cycle found. It built on Kossel and Dakin 1904 (arginase splits arginine into ornithine and urea). Three papers appeared in 1932 (Klin. Wochenschr. 11:757-759 and 1137-1139; Hoppe-Seyler Z. Physiol. Chem. 210:33-66). (a03, a04, b01.)

Step order (d01, K01), all dates secondhand:
1. 26 July to 15 November 1931. Screen amino acids and known reactions on tissue slices. Mostly negative. About 4 weeks went on known ammonia-to-urea facts first. On 15 Nov an ornithine test gave urea at about double the expected rate. This was the anomaly. It came after about 3.5 months of routine work.
2. 15 Nov to about 14 Jan 1932. Krebs tested derivatives of ornithine. None worked. The effect looked specific to ornithine. This is a scope check.
3. 14 Jan to 13 April. New apparatus. Ammonia shown to be the nitrogen source by 23 Jan. Ornithine judged a catalyst. Krebs thought about the arginase link for two weeks. On 13 April a test gave 24.5 molecules of urea per molecule of ornithine (far above one, so ornithine acts as a catalyst). Citrulline tested 25 April. First paper out about 30 April.

Order of operators in plain words: routine screen, one large surprise, method and scope checks, new instrument, source tracing, catalyst hypothesis, quantitative test, extend to a second compound, publish. Interpreting and testing took about 5 more months after the surprise.

Caveats: no count of individual experiments exists in anything we read. The logs give no reason why ornithine was tested on 15 Nov; it was a departure from the current line. The text says it is not known why Krebs ran that test then, nor why the cycle took so long after catalysis was known. (d01, d03.)

### 2.3 Gruber on Darwin
From a secondary timeline only (Wikipedia, d15): Notebook B opened mid-July 1837, with the first tree sketch on page 36. Notebook C by February 1838. D and M started in summer 1838. E holds an entry of 2 December 1838. M has about 60 pages on moral and social behaviour. Darwin began Malthus in late September 1838 and noted the insight on 28 September 1838. So the selection insight came about 14 months after notebook B opened.
Gruber's claim (memory-level, a21): the Malthus reading did not create selection from nothing. It landed on a mind with several developed streams. His counts of entries per topic and the critical readings (Kohn, Schweber, Ospovat) were not obtained. Treat Darwin as "parallel streams plus an outside trigger". (K27.)

### 2.4 KEKADA (Kulkarni and Simon 1988), opened in full text
KEKADA is a production system. Core idea: expectations are explicit; a violated expectation becomes the focus of attention; the next goals are built around the surprise. (d02.)
- Rule 2: if an outcome violates its expectation, note a surprise and make it the focus.
- Rule 4: if the surprise may lie in a subprocess, study that subprocess.
- Rule 5: if it may be common to a class of substances, study the scope.
- Expectations come from the mean of prior outcomes with a tolerance band, or from a preset prior if there is no prior run.
- Hypotheses carry counters: failure, failed-effort, implied-failure.
- Size: 3 expectation rules, 5 problem-proposer heuristics, 3 sets of choice rules (processes, substances, hypotheses). No hypothesis-modifier rules in this version.

What it reproduced (d03, K21): it rediscovered the cycle in three scenarios that differ in when catalysis is considered (late; early but ranked low; very likely from the start). The authors judge scenario 3 unlikely, because it does not explain Krebs's two weeks of puzzlement. About 10 steps (asterisked) were chosen by the user, not the program, for example citrulline as intermediate and which nitrogen source to test. No match fraction is reported. No independent replication was found. Divergences listed: the alanine surprise, Krebs's doubt about the tissue-slice method, cyanate and pyrimidine ideas, and the slow route to the cyclic path.
The authors' own warning (d04): the early alanine surprise was probably not felt by Krebs, who just kept testing amino acids. Reading surprise into early steps may make the record look tidier than it was.

### 2.5 Rival readings of a reconstruction (b26, K02)
(a) The historian imposes a tidy story. (b) The scientist later recalls a tidier order. (c) The notebook is a true contemporary record. Only (c) is protected by a document made at the time. Holmes combined notebooks with interviews; Grasshoff and May re-derived steps by program; Nickelsen and Grasshoff analysed error. Several readings of one episode exist, but no inter-rater statistic was found. This is our own synthesis, not a measured result.
The one comparison in opened text: Holmes (gradual, interview-informed) versus KEKADA (logical order, with user help) differ on when catalysis was considered. (d16.)

### 2.6 Theories in play
- Surprise-driven focusing (Kulkarni and Simon; Grasshoff 1995 on the methodological function of surprises). Surprise as the trigger that changes the goal.
- Network of enterprise (Gruber). Many streams, long time scales, an image of wide scope.
- Dual-space search (Klahr and Dunbar). Alternate between choosing experiments and choosing hypotheses.
- In vivo lab practice (Dunbar). Unexpected results are met often; first suspicion falls on method, then the model changes. Memory-level only.
- Linked-experiment sequences (Holmes 2004). Each experiment is shaped by the last result.

## 3. Core findings with exact numbers

Status: established = two or more independent opened sources; single = one opened source; unverified = memory or snippet only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Krebs's anomaly came after long routine work | About 3.5 months (26 Jul to 15 Nov 1931) before the ornithine surprise; about 4 weeks on known ammonia work first | d01 (Kulkarni and Simon quoting Holmes) | single (secondhand) |
| Interpretation took longer than finding the anomaly | About 5 more months to the 13 Apr 1932 test; 24.5 urea per ornithine; two weeks on the arginase link; paper about 30 Apr | d01 | single (secondhand) |
| Scope checks followed the surprise | 15 Nov to about 14 Jan: ornithine derivatives all failed | d01 | single |
| Path was gradual, not a gestalt switch | Holmes's own remark | d04 | single |
| KEKADA rediscovers the cycle only with user help | 3 scenarios; about 10 user-chosen steps; no match fraction; no replication | d03 | single |
| KEKADA rule set is small | 3 expectation rules, 5 problem-proposers, 3 choice-rule sets; no hypothesis-modifier rules | d02 | single |
| Darwin: selection about 14 months after notebook B | Notebook B mid-Jul 1837; Malthus noted 28 Sep 1838; M about 60 pages | d15 (Wikipedia) | single (secondary) |
| Dunbar: share of lab-meeting findings unexpected | "About half" | Dunbar 1997, memory | unverified, do not cite |
| Frontier agents fail most full discovery tasks | DiscoveryWorld: best agent 38% easy, 18% challenge; 11 humans 66% completion, 55% knowledge. DiscoveryBench best about 25%. ScienceAgentBench best 32.4% (34.3% with expert hints); o1-preview 42.2%. FIRE-Bench best F1 46.7 (SD 23.4) | a06, a12, b12, b14, c05, c07, c09, c23 | established (K04) |
| Humans also brute-force | Human knowledge 55% below completion 66% | a09, b12 | single |
| Agent knowledge falls with difficulty | ReAct easy/challenge: procedure 0.59/0.63, completion 0.38/0.18, knowledge 0.25/0.10. Hypothesizer: 0.56/0.49, 0.28/0.08, 0.34/0.08 | a07 | single |
| Right moves, no discovery | Procedure score stays 0.49-0.63 while completion collapses | a07 | single |
| Execution feedback roughly doubles code-task success | Claude-3.5-Sonnet: direct 16.7% (20.6% with hints) to self-debug 32.4% (34.3%), 1.94x | c09, b14 | single |
| Plain self-debug beats a heavy agent | 32.4% vs OpenHands CodeAct 21.6%; $0.057 vs $0.958 per task (about 17x cheaper) | b15 | single |
| Self-correction without an external signal does not help | GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1), 41.8 (round 2); GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-4 HotpotQA 49.0 to 49.0 to 43.0 | b21 | established (K08) |
| With oracle labels self-correction "helps" | GPT-3.5 GSM8K 75.9 to 84.3; CommonSenseQA 75.8 to 89.7; GPT-4 HotpotQA 49.0 to 59.0 | b22 | established (it is a leak) |
| Reasoning models have a small or negative self-correction blind spot | Non-reasoning blind spot avg 64.5% (14 open models); Claude 3.5 Haiku 52.5%, Sonnet 4 41.4%; "Wait" cuts blind spot 89.3%; DeepSeek-V3 0.567 to 0.902 (R1-0528 0.908); SFT on 5,306 traces cut it 76.0% | d13 | single |
| LLM research output often wrong | AI Scientist re-run: 5 of 12 experiments (42%) failed from coding errors; 4 of 7 manuscripts (57%) structural errors; 4 of 7 (57%) wrong or hallucinated numbers; 5 of 34 citations from 2020 or later | c11, a11, b18 | established (K10) |
| Model judges overrate | Agent Laboratory automated 6.1/10 vs human 3.8/10; best LLM judge 53.3% vs human inter-reviewer 56.1% balanced accuracy | a14, b20 | established (K11) |
| AI auto-reviewer matches humans on a narrow task | AI Scientist reviewer: 70% accuracy; balanced accuracy 65% vs 66% for humans (500 ICLR 2022 papers) | a10 | single |
| AI ideas look more novel but collapse to repeats | Novelty 4.84 human, 5.64 AI, 5.81 AI plus human rerank; N=49 ideas per condition; 79 reviewers; p<0.05. Of 4000 seed ideas per topic only about 200 non-duplicate (about 5%) | b19, b20 | established (K12) |
| Acting beats watching | GPT-4o own interventions beat observation-only and beat yoked replay of its own intervention data. Gains by complexity -0.6 to +12.7 points | c18, c20 | single (K13) |
| Analyze-then-query helps on programs | Program: plain 43.4, descriptive 47.6, functional 19.2, analyze-then-query 50.8. Formal language: 24.1, 28.6, 22.8, 34.7. Math equation: 34.8, 38.8, 39.9, 38.0 | c21 (column mapping to check) | single |
| Two model-building failure modes | Program: 17 of 20 failures overcomplication. Math equation: 16 of 20 overlooking. Formal language: 8 and 11, 1 n/a. 20 per box, observation-only condition | c19 | single |
| Code tools make strong models stop exploring | Exploration tokens fall, confirm/verify tokens rise with code budget; performance falls from budget 0 to 1 for Gemini-2.5-flash and GPT-5-mini; weak models gain. Noise of 0.0001 cuts symbolic accuracy 12-16% | c15, c16 | single (K15) |
| Long loops anchor greedily | 100 experiments: one early hypothesis gave +21.41 of +26.92 points (79.5%); CIFAR-10 69.67% to 96.59%; acceptance 36-38% early vs 12% in Phase 3; 29 saturated hypotheses; last 18 hypotheses +0.26 points, 2 accepted | c25, c27 | single (one run, no control) |
| Literature access changes the kind of idea | Code-changing hypotheses 5% (2/42) to 76% (16/21); novel mechanisms 2 to 8; confounded with phase | c26 | single |
| Greedy loses efficiency with GPT-4o, not with o4-mini | AutoDiscovery, 500 evaluations: greedy and beam decline with GPT-4o; MCTS equals greedy under o4-mini | d09 | single |
| Surprise as search reward helps at fixed budget | MCTS on Bayesian surprise: 5-29% more surprising discoveries; best on 17 of 21 datasets; 67% of surprises also surprising to experts; Bayesian surprise correlates 67% with human surprisal | d08 | single (K23) |
| Search policy matters less than operators | MLE-bench Lite, 20 seeds: greedy/MCTS/evolutionary and exploration constant 0/0.25/0.75 only marginal; AIRA operators 45.5% vs AIDE 39.8% (14% relative); MCTS with better operators 47%; validation score kept rising while held-out test plateaued or fell | d10 | single (K26) |
| Memory of attempts alone gave no gain | AIDE with vs without memory: nearly identical medal rates | d10, d11 | single (K25) |
| Written explanation after failure carries Reflexion's gain | HumanEval Rust hardest 50, GPT-4: base 0.60, no reflection 0.60, no test generation 0.52, full 0.68. HotPotQA: reflection adds 8 points over episodic memory alone | d12 | single (K24); not equal tokens |
| Failures concentrate in planning and conclusions | FIRE-Bench false positives: 76.4% to 95.0% contradictory or unrelated; only 4.5% to 10.9% plausible alternatives; o4-mini to gpt-5 +6.1 F1 for +21% cost | c23, c24 | single (K17) |
| State tracking breaks before reasoning | Relational graph with 10 houses: Grok-4 and Gemini-2.5-pro 100%; GPT-4o 30%; Qwen2.5 0% | c22 | single (K18) |
| More attempts help | MLE-bench o1-preview bronze 16.9% (1 try) to 34.1% (pass@8) | b24 | single (K19) |
| Written reasoning can hide the real driver | Accuracy down by as much as 36% on 13 BIG-Bench Hard tasks under biased prompts | b25 | single |
| No LLM study replays a historical notebook and scores order | 0 found | b27, c30, d07, d16 | established as a search result, weak (K20) |

## 4. Mechanisms and models

Each mechanism is written so it could be coded.

### 4.1 Surprise-triggered focusing (KEKADA-style)
State: a table of expectations, one per planned measurement. Each expectation = (mean of prior outcomes of the same kind, tolerance band). If no prior run, use a stated prior.
Loop:
1. Before an action, write the expected result and the band.
2. After the result, compute miss = |observed - expected|. If miss > band, mark SURPRISE and set it as the focus. Otherwise continue the plan.
3. On SURPRISE run the proposers in order: (a) check the method (could the measurement be wrong?); (b) check a subprocess (which step could cause the miss?); (c) check scope (does it hold across a class of cases?).
4. Keep per-hypothesis counters: failure (test said no), failed-effort (attempts spent without result), implied-failure (a rival won). Drop a hypothesis when a counter passes a threshold.
5. Return to the routine plan only after an explanation is written for the surprise and one test of it is run.
Design notes from Krebs: the surprise was a single large miss (about double the expected rate) inside a long routine stretch, so fire on the size of the miss, not every deviation (K22). Method doubt came first in Krebs; keep step (a) first. KEKADA lacks hypothesis-modifier rules, so a real agent needs its own "revise the hypothesis" operator.
Risk: the KEKADA authors say that reading surprise into every early step makes the story too tidy. A rule that fires too often turns noise into false leads.

### 4.2 Segmented trace and reconstruction (Holmes's method as a procedure)
1. Log every action with a timestamp, the reason given at the time, the expected result, the observed result.
2. Split the log into segments at surprises and at changes of apparatus or goal (Krebs: three segments).
3. Name the operator family of each segment: screen, replicate, scope-check, instrument change, source tracing, hypothesis build, quantitative test, extend, write-up.
4. Count segment lengths and the time from first anomaly to first explanation. These are the numbers a reconstruction yields (Krebs: 3.5 months, then about 5 months).
5. Check the reconstruction two ways: a second independent reconstructor and the raw log. Report rank agreement. No such statistic exists in the literature we read, so this would be new.

### 4.3 Hypothesis-before, outcome-after notebook
Entry template (Hypothesizer, Safdar and Saadeldin and practitioner proposals share it): motivation, literature seen, the change, budget, expected result, outcome, status tag (pending, confirmed, rejected), one-line explanation of any miss.
Hypothesizer limits (c06): cap 40 entries and 2k tokens, update after every action, summarise every 10 actions, 2N calls for N steps. It scored best on knowledge but did not finish more tasks than ReAct. No notebook-only ablation exists, so the template is an untested design.

### 4.4 Impasse rule (operator-family ban)
Safdar and Saadeldin show an agent writing "pivot to a fundamentally different operator family" and then making another small nearby change. The accept/discard rule made the loop greedy hill climbing. A mechanism to fix it:
1. Tag each attempt with an operator family (parameter tweak, new component, different representation, different data view, drop a component, simplify).
2. Track rejections per family in a sliding window.
3. After N rejections in a family (start at 3, tune), ban that family for the next K attempts and require a draw from the least-used family.
4. Show the model the sibling failures of the current node (AIRA scoped memory: siblings for draft and improve; for debug, the full chain of earlier fix attempts to prevent undo-redo loops) and raise the requested change size with the number of children (AIRA complexity cue: minimal under 2 children, moderate 2 to 3, advanced at 5 or more).
Evidence for the pieces: d10, d11 (operators matter more than selection policy). Evidence for the ban itself: none. (K16.)

### 4.5 Look back (S9) with an external check
Reflexion's gain comes from a written reflection after a failed test, and the test result is external (d12). Huang et al. show that without an external signal self-review does nothing or hurts (b21). Mechanism: S9 may revise an answer only when it can cite a new observation (test output, execution result, retrieved fact). Without one it may only confirm or flag uncertainty.

### 4.6 Conclusion-vs-evidence audit
FIRE-Bench errors cluster in planning and conclusions. AI Scientist failures include invented tables. Mechanism: for every number or claim in the final answer, require a pointer to a logged observation; count violations. The AI Scientist fix was to instruct the agent to include only results it observed and to store copies of all executed files (b18).

### 4.7 Surprise as search reward (AutoDiscovery)
Reward = shift in the model's belief before and after an experiment (Bayesian surprise). MCTS with progressive widening expands high-surprise branches. This directs search to surprising places. It does not force an explanation. (d08.)

## 5. What holds up

### Replications and meta-analyses
- Failure of discovery agents is replicated across four independent benchmarks (DiscoveryWorld, DiscoveryBench, ScienceAgentBench, FIRE-Bench), all re-opened and confirmed. Different tasks, same conclusion: agents finish a minority. (K04.)
- AI Scientist: the authors' failure list (a11, b18) was matched by an independent re-run (c11): 42% of experiments failed, 57% of manuscripts had structural errors. This is the only true replication of an LLM-discovery system in the file. Sample is small: 12 ideas, 7 manuscripts, one domain (recommender systems), one template.
- Huang et al. is a meta-analytic reading of earlier work: earlier positive self-correction results used oracle labels, and gains vanish without them. (b22.)
- Si et al.: one study; reviewer agreement is low (human 56.1% balanced accuracy), so the novelty gap carries noise.

### Failures and non-replications
- KEKADA: no independent replication, no match rate, user-chosen steps. Partial only. (d03, K21.)
- Founding notebook studies have no replication in the sense of independent re-reading with an agreement statistic. Several reconstructions of the Krebs episode exist, but nothing we read compares them. (d16, K28.)
- The Huang et al. protocol has no located exact replication on o-series or R1-class models. (d14.)
- AIDE memory on vs off made no difference. Search policy changes made no difference with fixed operators. (d10.)
- Panchekha's blog test: ChatGPT Pro reasoned 67 minutes on synthetic Kepler-style data (about 15,000 daily observations at 0.001 degree) and did not find ellipses. n=1, no scoring. (d07.)

### Moderators and boundary conditions
- Model strength. Code tools help weak models and hurt strong ones (c15, c16). Wait helps non-reasoning models close to reasoning models (d13). Greedy loses efficiency with GPT-4o but not o4-mini at 500 evaluations (d09). A rule that helps one model class may be neutral or harmful for another.
- External signal. Self-review works only with an oracle or a real test (b21, b22, d12).
- Budget. Greedy's drop-off may appear at larger budgets (d09 footnote 7). Safdar's saturation came after many experiments (c25).
- Task type. Execution feedback nearly doubles success on code workflow (c09) but strong models explore less with code in symbolic law search (c16).
- Noise. 0.0001 noise cuts symbolic accuracy 12-16% (c15).
- Contamination. FIRE-Bench gpt-5 fell from 44.5 to 23.1 on a post-cutoff subset (c23). Rediscovery tasks can be partly recall.
- Domain. DiscoveryBench: biology 0%, engineering 7%, economics 25%, sociology 23% (c07).
- The DiscoveryBench domain-knowledge direction is unsettled (9.9% vs 17.5%, ambiguous sentence). Not used. (c08.)

### Interventions that worked
- Execution feedback and self-debug (c09, b15).
- Agent-chosen interventions over passive observation and over yoked replay (c18, c20).
- Analyze-then-query every fifth query on program boxes: 50.8 vs 43.4 (c21).
- Better operators over better search policy: 45.5% vs 39.8% (d10).
- Written reflection after an external failure (d12).
- Wait cue on non-reasoning models (d13).
- Bayesian surprise as search reward at fixed evaluation budget (d08).
- More attempts: pass@8 doubles the bronze rate (b24).
- Literature access changed hypothesis kind (c26, confounded).

### Interventions that did not work
- Intrinsic self-correction on 2023 models (b21).
- A memory log alone (d10).
- Changing search policy alone (d10).
- ReAct-style prompts and a self-critic on DiscoveryBench did not beat plain CodeGen; Reflexion with oracle feedback did (c07).
- Writing the black box as Python code gave no extra gain (c21).
- Code tools for strong models in law discovery (c16).
- Scaling idea generation (diversity collapse; b20).
- LLM judges as quality gate (b20, a14).
- Backbone upgrade o4-mini to gpt-5: +6.1 F1 for +21% cost, a small gain (c23).

## 6. Language models

How LLMs behave on discovery-like work:

1. They finish few full cycles. Best completions: 38% easy and 18% challenge (DiscoveryWorld), about 25% (DiscoveryBench), 32.4-42.2% (ScienceAgentBench), F1 46.7 (FIRE-Bench). Humans: 66% completion on DiscoveryWorld. (K04.)
2. They make the right moves but do not discover. DiscoveryWorld procedure score stays 0.49-0.63 on challenge tasks while completion is 0.08-0.18. (a07.)
3. Knowledge falls as difficulty rises: ReAct 0.25 to 0.10, Hypothesizer 0.34 to 0.08. (a07.)
4. They anchor. In one 100-experiment run 79.5% of the total gain came from one early hypothesis, acceptance fell from 36-38% to 12%, and the agent announced a pivot and then made another small change. (c25, c27.) Single run, no control arm.
5. They overcomplicate (programs, 17 of 20 failures) or overlook data (math equations, 16 of 20). (c19.)
6. State tracking breaks before reasoning: 10-house relational graph, GPT-4o 30%, Qwen2.5 0%, while Grok-4 and Gemini-2.5-pro reach 100%; failures persist when intervention choice and hypothesis writing are supplied. (c22.)
7. They learn more by doing than by seeing the same data: own interventions beat yoked replay. (c20.)
8. Strong models explore less when given code in law discovery. Exploration tokens ("What if", "Alternatively") fall; "Confirm" and "Verify" rise. (c16.) Only four reasoning models with visible traces could be measured.
9. They invent: whole ablation tables, hardware facts, wrong number comparisons. Independent re-run: 57% of manuscripts had incorrect or hallucinated numbers. (c11, b18.)
10. They over-rate themselves and each other: automated review 6.1 vs human 3.8 (a14); best LLM judge below human agreement (b20).
11. Written reasoning may hide the real driver: accuracy down by up to 36% under biased prompts with no mention of the bias. (b25.) Old models.
12. Intrinsic self-correction: harmful or null on GPT-3.5 and GPT-4 (b21). For reasoning models the blind spot is small or negative (d13). The cheap lever is a "Wait" cue: DeepSeek-V3 0.567 to 0.902, Qwen3-14B 0.117 to 0.868, Qwen3-32B 0.045 to 0.793, phi-4 0.325 to 0.701. The test injects errors, so it is a different question from Huang's no-oracle one, and Wait lengthens output (not equal tokens).
13. Idea generation is high-novelty and low-diversity: novelty 5.64 vs 4.84, but about 200 distinct ideas from 4000. (b19, b20.)
14. What changed results, with size: execution feedback x1.94 (c09); operators +5.7 points (39.8 to 45.5; d10); analyze-then-query +7.4 points on programs (c21); Wait up to +0.73 on a non-reasoning model (d13, Qwen3-14B 0.117 to 0.868 is +0.751); pass@8 x2 on bronze rate (b24); backbone upgrade +6.1 F1 (c23); Bayesian-surprise search +5-29% more surprising findings (d08); reflection +8 points on HotPotQA (d12).
15. Not found: any test where an LLM rebuilds the operator order of a real notebook; any equal-token test of "explain the surprise before moving on"; any ablation of a structured hypothesis notebook alone. (K20, K09, K23.)

## 7. What our agent should take

Each item: schema part, status ([E] established, [S] single-source, [C] contested), evidence ids.

### Add now (established)

1. Do not trust unaided self-review. Revise only on a new external observation (test, execution, retrieval). | G, S9 | [E] | b21, b22, d12, d13 (K08). Caveat: reasoning models differ; the rule costs nothing and prevents the measured harm.
2. No unobserved claims. Every number in the final answer must point to a logged observation; count violations. | G | [E] | a11, b18, c10, c11 (K10).
3. Do not use a model judge as the quality gate for its own output; use external checks. | G | [E] | a14, b20 (K11).
4. Use a diversify step when sampling many hypotheses; measure the unique-hypothesis rate. | O (diversify) | [E] | b19, b20 (K12).
5. Keep a baseline arm on a held-out slice of a public benchmark as the reference for every scaffold claim. | evaluation | [E] | K04.

### Test first

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Surprise rule: write expected value and band; on a miss beyond the band, explain it (method, subprocess, scope) before the next action | S6, O | [S] | d01, d02, d03, d08, K03, K22, K23 |
| Fire the rule on size of miss only, not every deviation | S6 | [S] | d01, d04 |
| Hypothesis-before, outcome-after notebook with status tags | memory | [S] | c06, c25, d12, K09, K24 |
| Impasse rule: ban an operator family after N rejections; show sibling failures | S6 | [S] | c25, c27, d10, d11, K16, K25, K26 |
| Change the operator, not only the node chosen; judge on a held-out check | S6 | [S] | d10 (K26) |
| Report completion and explanatory knowledge separately | evaluation | [S] | a09, b12, a07 (K05, K06) |
| Simplicity vs use-all-data operators matched to failure type | S6 | [S] | c19 (K14) |
| Agent-chosen queries over passive data | O (experiment) | [S] | c18, c20, c21 (K13) |
| Explicit state table | memory | [S] | c22 (K18) |
| Track exploration-token rate against tool budget | S6 | [S] | c15, c16 (K15) |
| Conclusion-vs-evidence audit at S9 | S9 | [S] | c23, c24 (K17) |
| Operator-order self-reconstruction: a second model rebuilds order from the agent's own log; score agreement | S9 | [C] (no reliability statistic for the method) | b26, d16, K01, K02, K28 |
| Wait or continue cue at look back | S9 | [S] | d13 |
| Best-of-N versus one long chain at equal tokens | O (resample) | [S] | b24 (K19) |
| Self-debug loop versus multi-step planner | G, O | [S] | b15 (K07) |

Nothing from the Test first list goes into SCHEMA.md until its test passes.

## 8. Concrete tests on our bench

All arms at equal total tokens (prompt plus completion across all calls). Report per-arm token counts.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Hidden-structure puzzles with a planted anomaly (a rule that breaks once after a run of routine cases); 60 items | A: baseline loop. B: forced expectation plus band, then forced explanation of a miss before the next action | Solved rate; steps to the correct rule | B beats A by 5-10 points |
| T2 | Same puzzles with no anomaly (20 items) | B vs A | False-alarm rate: share of items where the agent chases a non-existent surprise | B within 2 points of A; worse by more than 3 means the band is too tight |
| T3 | Discovery-style tasks with a checker (DiscoveryWorld unit-test and easy slice, 40 tasks) | A: no notebook. B: structured hypothesis/outcome notebook, same token cap | Completion and knowledge score, separately | B gains 3-6 points of knowledge; completion flat |
| T4 | Long optimisation task (50+ experiments, held-out score) | A: greedy accept/discard. B: operator-family ban after 3 rejections plus sibling failures shown | Held-out gain at end; share of gain from the single best change | B higher by at least 2 points; top-change share below 60% (Safdar: 79.5%) |
| T5 | Black-box reverse engineering (program, formal language, math equation boxes) | A: observation only. B: agent chooses queries. C: yoked replay of B's queries | Descriptive score 0-10 | B > C > A; B minus C at least 2 points |
| T6 | Same boxes, failure typing | A: no hint. B: simplest-rule and use-every-datum operators picked by failure tag | Share of failures that are overcomplication or overlooking | B cuts the dominant failure type by a third |
| T7 | Tasks with a real checker (code with unit tests) | A: self-review only. B: look back with test output. C: look back with a Wait cue only | Accuracy after revision | B beats A by 5 points or more; C about equal to A (record any gain) |
| T8 | Final answers from 30 runs | A: free answer. B: each number cites a log line | Unsupported numbers per answer | B down by half or more with no accuracy loss |
| T9 | 30 logged agent runs | Two different models rebuild operator order from the same hidden-order log | Kendall tau with the true trace and between the two rebuilders | tau above 0.6: usable as a probe; below 0.4: reject |
| T10 | Hypothesis sampling | A: N samples. B: N samples plus diversify operator | Unique-hypothesis rate | B at least 1.5x A |
| T11 | Symbolic law search | A: no code tool. B: code tool; track exploration-token rate | Accuracy and exploration rate by model strength | Gain for weak, loss for strong; sets a rule per model class |
| T12 | Same items as other tests | A: best-of-N. B: one long chain | Accuracy | Best-of-N wins with a checker; ties without one |

## 9. What does not transfer, and why

- Human insight timing. Krebs's 3.5 months before the anomaly and 5 months after are wall-clock time for wet-lab work. Our equivalent is steps. Use the shape (long routine, one big miss, local checks, then explanation), not the durations.
- The Krebs path as a template. One case, chosen after success, with rival readings. Klahr and Simon note that case studies are few, chosen after success and rely on subjective records (a26, via SUBFIELDS.md). The order may be tidier than what happened (d04).
- Gruber's network of enterprise. Darwin ran several streams over years with an outside trigger. Our agent runs one session on a token budget. Parallel streams need memory across sessions that we do not have.
- KEKADA's expectation tables. Krebs's expectations were numeric. Many of our items have no numeric expectation. The band rule needs an expected value the agent can state.
- Bayesian-surprise search. AutoDiscovery surprise is judged by an LLM family on open-ended data analysis. Our items have fixed answers.
- Discovery benchmarks to real science. Simulated text worlds, GPT-4o-era models (DiscoveryWorld), one domain and template (AI Scientist re-run), LLM-behaviour papers (FIRE-Bench). The scores say little about our bench.
- Huang numbers to 2025-26 models. They were GPT-3.5 and GPT-4. Do not quote them as current.
- Wait results. Injected errors, not self-found errors; extra tokens. Not an equal-token result.
- Safdar and Saadeldin phases. One run, human-declared phase changes.
- Dunbar and Tweney. Unread. Nothing from them transfers until opened.

## 10. Open questions

1. How many experiments did Krebs run between 26 Jul 1931 and April 1932, by operator family? Needs Holmes 1980 (Fed Proc 39:216-225), Holmes 1991, Grasshoff and May 2003 (pp. 269-294).
2. What fraction of Krebs's steps did KEKADA match without user help? None is reported. It could be recounted from the paper's scenario traces.
3. Does any 2020-2026 LLM study replay Krebs, Darwin, Faraday or Kepler and score order against the record? Searches were throttled; absence is not proven.
4. Do independent reconstructions of one notebook agree? No inter-rater statistic found (Nickelsen and Grasshoff 2009 unread).
5. Gruber's counts: entries per topic, parallel streams, time from Malthus to the selection write-up; the critical readings (Kohn, Schweber, Ospovat).
6. Dunbar's actual rates of unexpected findings and how labs responded (method check first, then model change).
7. Does an explain-the-surprise rule beat baseline at equal tokens? Only reward-based surprise search was tested, at equal evaluations.
8. Does a structured hypothesis/outcome notebook alone help? No ablation found.
9. Does an operator-family ban beat greedy? Only indirect evidence.
10. Does Huang's no-oracle self-correction result hold for o-series and R1 models under the same protocol?
11. Do Safdar's saturation and anchoring patterns appear across runs and agents?
12. How much of "right moves, no discovery" is state tracking (c22) and how much is poor hypotheses?

## 11. Sources

[V] = opened and read this session. [M] = snippet, landing page or memory only.

Founding and historiography
- [V] Wikipedia, Frederic L. Holmes. https://en.wikipedia.org/wiki/Frederic_L._Holmes (a01, b03, b26)
- [V] Wikipedia, Howard Gruber. https://en.wikipedia.org/wiki/Howard_Gruber (a02, b04)
- [V] Wikipedia, Hans Adolf Krebs. https://en.wikipedia.org/wiki/Hans_Adolf_Krebs (a03, b01, b02, b07, b08)
- [V] Wikipedia, Urea cycle. https://en.wikipedia.org/wiki/Urea_cycle (a04)
- [V] Wikipedia, Inception of Darwin's theory. https://en.wikipedia.org/wiki/Inception_of_Darwin%27s_theory (d15)
- [V] Kulkarni and Simon (1988) KEKADA, CMU full-text copy. https://ndownloader.figshare.com/files/12102893 (d01-d04)
- [M] Kulkarni and Simon (1988) Cognitive Science 12:139-175. https://doi.org/10.1207/s15516709cog1202_4 (a19, b05, c02)
- [M] Kulkarni and Simon (1990) Experimentation in machine discovery. https://doi.org/10.1016/B978-1-55860-131-8.50007-X (a20, b06)
- [V] MPIWG project page, Urea Modeler. https://www.mpiwg-berlin.mpg.de/project/urea-cycle (c01)
- [M] Grasshoff and May (2003) Reworking the Bench, pp. 269-294. https://link.springer.com/chapter/10.1007/0-306-48152-9_13 (a23, d05; landing page and references only)
- [M] Nickelsen and Grasshoff (2009) Concepts from the Bench. https://doi.org/10.1007/978-1-4020-8893-3_7 (b08, d16)
- [M] Holmes (1980) Fed Proc 39:216-225; Holmes (1991, 1993) Hans Krebs vols 1 and 2; Holmes (2004) Investigative Pathways (a16, a17, a18, c03; no URL)
- [M] Gruber (1974) Darwin on Man; Gruber (1989) (a21, a22; no URL)
- [M] Tweney (1985) Faraday's discovery of induction. https://doi.org/10.1007/978-1-349-07477-0 (a24, b11)
- [M] Dunbar (1997) How scientists think. https://doi.org/10.1037/10227-017 (a25, b09, d06); Dunbar and Fugelsang (2005) Neuropsychologia 43
- [M] Klahr and Dunbar (1988) Dual space search. https://doi.org/10.1207/s15516709cog1201_1 (b10)
- [M] Klahr and Simon (2001) Current Directions in Psychological Science (a26, quoted from SUBFIELDS.md)
- [M] Langley (1987) Scientific Discovery: BACON (a27)

LLM and AI studies
- [V] Jansen et al. (2024) DiscoveryWorld. https://arxiv.org/abs/2406.06769 (a06-a09, b12, b13, c05, c06)
- [V] Majumder et al. (2024) DiscoveryBench. https://arxiv.org/abs/2407.01725 (c07, c08)
- [V] Chen et al. (2025) ScienceAgentBench. https://arxiv.org/abs/2410.05080 (a12, b14, b15, c09)
- [V] Yang et al. (2024) MOOSE-Chem. https://arxiv.org/abs/2410.07076 (a13)
- [V] Lu et al. (2024) The AI Scientist. https://arxiv.org/abs/2408.06292 (a10, a11, b17, b18, c10)
- [V] Beel, Kan and Baumgart (2025) Evaluating Sakana's AI Scientist. https://arxiv.org/abs/2502.14297 (c11)
- [V] Yamada et al. (2025) AI Scientist-v2. https://arxiv.org/abs/2504.08066 (c12)
- [V] Agent Laboratory (2025). https://arxiv.org/abs/2501.04227 (a14, a15; introduction only)
- [V] Laurent et al. (2024) LAB-Bench. https://arxiv.org/abs/2407.10362 (b16)
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas. https://arxiv.org/abs/2409.04109 (b19, b20)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b21, b22)
- [V] Gandhi et al. (2025) BoxingGym. https://arxiv.org/abs/2501.01540 (b23; abstract and setup only)
- [V] Chan et al. (2024) MLE-bench. https://arxiv.org/abs/2410.07095 (b24)
- [V] Turpin et al. (2023) Unfaithful explanations in chain-of-thought. https://arxiv.org/abs/2305.04388 (b25)
- [V] Shojaee et al. (2025) LLM-SR. https://arxiv.org/abs/2404.18400 (c13)
- [V] Shojaee et al. (2025) LLM-SRBench. https://arxiv.org/abs/2504.10415 (c14)
- [V] Zheng et al. (2026) NewtonBench. https://arxiv.org/abs/2510.07172 (c15-c17)
- [V] Geng, Chen, Arumugam, Griffiths (2025) Are LLMs reliable AI scientists. https://arxiv.org/abs/2505.17968 (c18-c21)
- [V] Chen et al. (2026) Auto-Discovery-Bench. https://arxiv.org/abs/2502.15224 (c22)
- [V] Wang et al. (2026) FIRE-Bench. https://arxiv.org/abs/2602.02905 (c23, c24)
- [V] Safdar and Saadeldin (2026) Long-horizon autonomous architecture research. https://arxiv.org/abs/2608.01995 (c25-c27)
- [V] Agarwal et al. (2026) AutoDiscovery. https://arxiv.org/abs/2507.00310 (d08, d09)
- [V] Toledo et al. (2025) AI research agents on MLE-bench. https://arxiv.org/abs/2507.02554 (d10, d11)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (d12)
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778 (d13)
- [V] Panchekha, Can an LLM reproduce Kepler from raw data (blog, via summariser). https://pavpanchekha.com/blog/llk.html (c04, d07)
- [M] Agents of Discovery (2025) LHC Olympics. https://arxiv.org/abs/2509.08535 (c29)
- [M] Practitioner notebook essays (osteele; SciLog). https://notes.osteele.com/essays/research-lab-notebook/ (c28)
- [M] arXiv search for LLM notebook reconstruction, zero hits. https://arxiv.org/search/?query=laboratory+notebook+reconstruction+scientific+discovery+language+model&searchtype=all (b27)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 6 established claims: 6 confirmed as written, 0 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

