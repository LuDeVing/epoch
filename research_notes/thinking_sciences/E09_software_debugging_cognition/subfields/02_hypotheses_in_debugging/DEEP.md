# Hypotheses in debugging: deep document

*Subfield E09.02. Evidence files in this folder: evidence_a.jsonl (a01-a33), evidence_b.jsonl (b01-b32), evidence_c.jsonl (c01-c25), evidence_d.jsonl (d01-d16), claims.jsonl (E09.02-K01 to K24), critique.md. Written 2026-10-26. Numbers were cross-checked against paper text in critique.md; where a number is a reading of a garbled table, it says so.*

*Overlaps. Chain-of-hypothesis methods and general self-repair belong to the LLM debugging subfield (`09_llm_debugging`). How many hypotheses to hold belongs to Hypothesis limits in troubleshooting. Which test to run next belongs to Probing and measurement selection. Fixation in general belongs to Anomaly handling and fixation. Here we cover what is specific to hypotheses in debugging: where they come from, how good they are, what a supplied one does, and what a wrong one does.*

---

## 1. What it is

A debugging hypothesis is a guess about why a program fails. Example: "the list is sorted in place, so the second call sees changed data." It names a cause. It can be tested. It is different from a location ("look at line 40") and different from a fix ("add a copy").

The subfield asks five things.

1. Where do hypotheses come from, and how often are they right?
2. Does having a correct hypothesis (or being handed one) change whether the bug gets fixed?
3. What does a wrong early hypothesis do? Does it lock the debugger in?
4. Do people actually debug by stating and testing hypotheses, or is that a textbook story?
5. Do language models do the same things, and does a hypothesis-driven scaffold help them?

Why this matters for our agent. In our schema, S3 GENERATE makes attempts and S4 TEST checks them. For a debugging-type item (a failing program, a failing check, a rule that must explain observations), the attempt is a cause plus a fix. The quality of the first causes sets the ceiling. This document says how strong that evidence is. The honest answer: the human evidence is thin (one lab study with 20 people), the LLM evidence is indirect (nobody has replayed the human experiment on a model), and several famous claims rest on abstracts we never read in full.

Scope note. Most sources here are about code. Our bench has ARC and BrainTeaser-style items. The transfer is argued in section 9.

---

## 2. History and theories in depth

### 2.1 Founding studies (1975 to 1991)

These are the studies everyone cites. We did not read them in full. Only abstract pages or secondary summaries were opened (a24, a25, a26, a27, a28, b16, b17, b18). Treat what follows as "reported", not "verified".

- **Gould (1975).** 10 experienced programmers debugged the same 12 FORTRAN listings, each with one non-syntactic error. Median debug time about 7 minutes. About 11% of listings had the bug not found. Fewer than 1 incorrect assertion about the bug location per listing. Assignment-statement bugs were about 3 times harder to find than array or interaction bugs. Debugging was about 3 times as efficient on a program the person had debugged before with a different bug. The paper sets out "a gross theory of debugging": form hypotheses about the bug, then verify. It replicates Gould and Drongowski (1974). Programmers rarely used the interactive debugging tools offered. (a24, b17; abstract page only.)
- **Vessey (1985).** 16 programmers (8 expert, 8 novice) thought aloud on a COBOL program. Expertise was defined by ability to chunk the program, not by years. The abstract proposes that experts go breadth-first with a system view and smooth progress, and novices go depth-first and erratically. A search summary says novices were "constrained by preconceived ideas or early hypotheses about the error source" while experts "respond to the data in the task". This is the origin of the claim that novices fixate on early hypotheses. The PDF is a scan with no text layer. We did not read the results. The strategy statements may be propositions for later testing, not findings. (a25, a26, b16.)
- **Katz and Anderson (1987).** Students debugging Lisp. Secondary summary: three bug-location strategies (heuristic mapping from symptom to origin, hand simulation, causal reasoning). Goal-driven reasoning dominated when debugging one's own code. Data-driven hand simulation dominated for other people's code. N=77 per the table in Alaboudi 2021 (a09). Sources disagree on whether subjects were novices. Not opened. (a27, b18.)
- **Gilmore (1991).** Secondary summary only. Understanding does not finish before debugging starts. It keeps developing during the loop. Deeper bugs were found more easily, which he read as bugs being detected during ongoing comprehension. Locating errors involves repeated cycles of hypothesis formation and test. This disagrees with Katz and Anderson, who assume full understanding first. Not opened. (a28.)
- **Shapiro (1983), algorithmic program debugging.** An early AI debugger. It asks an oracle about subcomputations and narrows to the faulty clause by divide and conquer. Recalled, not opened. (c21.)
- **Zeller (2002, 2009), scientific debugging.** The explicit loop: hypothesis, prediction, experiment, observation, conclusion. Delta debugging is automated hypothesis testing. This is the template AutoSD copies. Recalled, not opened. (c20.)

How thin the founding base is. Alaboudi and LaToza's 2021 Table 1 lists the hypothesis-era studies: Gould 10 participants, Vessey 16, Katz and Anderson 77 (mostly students), Gugerty and Olson 44, Bohme 12, Layman 15. Only five studies watched professionals in the field. (a09.)

### 2.2 Program comprehension theory

Hypothesis-driven debugging sits inside comprehension theory. Brooks: understanding code is hypothesis-driven, top-down. Letovsky: conjectures are answers to questions the reader asks. Robin: novice versus expert differences. Alaboudi and LaToza (2020) use this lineage to say the hypothesis is the unit of debugging, and that professionals mostly use an "intuitive method" of forming and testing hypotheses. We only saw this in their related-work paragraph, not in the originals. (a08.)

### 2.3 Two competing descriptions of what developers do

**Hypothesis-driven view.** Developers guess causes from experience and output clues, then test by editing code or inspecting state. Both forward reasoning (follow the failing run) and backward reasoning (work back from wrong output) are used. (a10.) Interviews and personal accounts say "scientific method". (a15.)

**Observational view.** When you watch what people do, the formal hypothesis is rare. Examples:
- Li and Coblenz (2026): 7 professionals on 11 tasks (7.8 hours) plus 5 streamers on 6 tasks (3.1 hours). None articulated a formal hypothesis. They voiced "casual thoughts about the system". Time: 12% reproducing, 57% updating the mental model, 13% fixing, 18% validating. (a13.)
- Cited in the same paper: a VR performance-bug study with 12 participants found 79 fifteen-second instances of stating and testing a hypothesis against 832 of source inspection. Second-hand, one bug. (a15, b10.)
- Bohme et al. (DbgBench): 12 engineers fixed 27 real bugs. Forward reasoning and code comprehension used most. Abstract only. (a15, a32.)
- A review of 74 papers found 12 strategies. (a15.)
- Information foraging theory predicts that developers follow "scent", not hypotheses. A live-stream study found debugging is 41% editing and 29% testing. (a16.)

**Can both be true?** Yes. Speculation can be informal, held in the background, and still matter. And outside hypotheses can help even if people do not generate them in formal form. The comparison "formal hypotheses help versus hurt" has never been run on natural practice. Li and Coblenz gives no outcome contrast. (b09.)

One observation that cuts against fixation fears: developers sometimes avoid committing on purpose. One listed several speculations and did not check them, "just to try to not to jump to conclusions". Forward tracing dominated in high-familiarity code, backward tracing in low-familiarity and longer tasks (forward used by 7 of 8 participants). (a14.)

### 2.4 The Alaboudi and LaToza line (2020 to 2021)

This is the core of the subfield.

- **2020, "Using Hypotheses as a Debugging Aid".** The one controlled test of whether supplying hypotheses helps. Details in section 3 and 5.
- **2021, "An Exploratory Study of Debugging Episodes".** Live-streamed work by 11 developers in the coded sample (dataset over 100 hours, 33 professionals). Debugging was 48% of session time (range 13 to 95%). The 23 long episodes (about 32 minutes) made 80% of debugging time. The 23 short ones made 1%. Self-inserted defects took 6 minutes versus 51 for reported defects. Debugging happens about once every 8 minutes of programming. Episodes range from seconds to over 100 minutes. (a11, b31.)
- **2021, "Edit-Run Behavior".** 28 hours, 11 professionals, 581 debugging and 207 programming edit-run cycles. About 7 cycles before a fix. Mean debugging cycle about 1 minute versus 3 for programming. Only 23% of run steps used logs or the debugger. 18% used automated tests. 94% of debugging cycles had no gaps. 70% edited one file. Text-editor users did 69% more cycles than IDE users. The authors read cycles as tests of hypotheses by trying a change. Hypotheses were not coded one by one. (a12, b32.)

### 2.5 Tools that attack hypothesis generation

- **Whyline (Ko and Myers).** Instead of guessing where to look, the user asks "why did" and "why didn't" questions about the output, and the tool answers from a recording. In Alice, about 8 times less debugging time and 40% more tasks completed (2004). Java Whyline on two real open-source bug reports: about 3 times the success and 2 times the speed against breakpoints (2009). Abstract only. Same group, small, not independent. (a29, a30.)
- **Automated fault localisation.** Parnin and Orso (2011) found suspiciousness lists help little (section 5). (a31, b12-b15.)
- **Prior to LLMs, "hypotheses" meant human guesses.** Section 6 covers what changed.

---

## 3. Core findings with exact numbers

Status key: established = two or more independent sources agree (as in claims.jsonl); single-source = one study; contested = sources conflict or are author-run only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Supplied hypotheses (one right, one wrong, each with test steps) raised fix success. Headline "six times" is an odds ratio. | Ordinal logistic model, 60 sessions: OR 6.24, SE 0.88, p=0.03 (text p=0.0388). Approx 95% CI 1.1 to 35 (our calculation). Raw: 16/20 (80%) hypotheses vs 11/20 (55%) control vs 13/20 (65%) fault locations. Raw risk ratio about 1.45. Fisher exact 16/20 vs 11/20: p about 0.18 (our calculation). | Alaboudi and LaToza 2020 (a04, b01, d13) | single-source (K01) |
| Supplied fault locations did not help. | OR 1.4 (SE 0.77, p=0.64). Correct hypothesis share, locations vs control: stage 2 45% vs 45% (p=0.4125); stage 3 60% vs 75% (p=0.1320). Fix rate p=0.6710. | Alaboudi 2020 (a05, b05); Parnin and Orso 2011 (b12-b14) | established (K02) |
| Unaided developers hold few hypotheses and most are wrong early. | Control, 20 sessions. Stage 1 (symptom only): 27 hypotheses, 3 correct (11%). Stage 2 (code and docs): 35, 9 correct (25%). Stage 3 (can run and edit): 38, 15 correct (39%). Median 1 hypothesis per defect at stages 1 and 2, 2 at stage 3, max 4. Participant level: control had a correct hypothesis in 45% at stage 2, 75% at stage 3. | Alaboudi 2020 (a02, b03; critique correction 4) | single-source (K03) |
| A correct hypothesis at stage 2 predicts a fix, but is not enough. | About 5x higher odds, p=0.01 (60 sessions, with controls). 20 of 60 sessions failed; 6 of those 20 held the correct stage-2 hypothesis. | Alaboudi 2020 (a03, b04) | single-source (K04) |
| Supplied hypotheses bought accuracy, not speed. | Median time to success f=0.51, p=0.61. Documentation share among successes: 5% control, 17% locations, 6% hypotheses (f=1.7, p=0.19). | Alaboudi 2020 (a06, b06) | single-source |
| Experience also predicted success. | Experience OR 1.14 per year, p=0.04. Technology knowledge OR 2.19, p=0.07. Median experience 2 years. (An earlier note said experience was not significant. Table IV says it was.) | Alaboudi 2020 (a04, d13; critique correction 3) | single-source |
| Task difficulty varied a lot. | Tasks 1 and 2 about 55% success overall; task 3 about 90%. | Alaboudi 2020 (b01) | single-source |
| Locating the bug is harder than fixing it. Successful runs observed first. | 30 of 32 post-bug forms (93.75%) rated locating at least as hard as fixing. Successful attempts ran the unmodified program first in 16 of 18 (88.9%); 6 of 8 (75%) who edited before the first run failed. Mean transitions between activities 43.1 (fail) vs 26.97 (success). N=14 students. | Arafa et al. 2017 (a22) | established (K15, with b29, b12) |
| Single-cause thinking misses two-line fixes. | Bug 3: 11 examined, 10 located, 3 fixed (many inserted one line). | Arafa 2017 (a23) | single-source |
| Debugging time is heavy-tailed. | 23 long episodes (about 32 min) = 80% of debugging time; 23 short = 1%. Debugging 48% of session time. | Alaboudi 2021 (a11, b31) | single-source (K06) |
| Developers mostly test a guess by edit and run. | 581 cycles; median about 1 min; about 7 cycles per fix; 23% used logs/debugger; 18% automated tests. | Alaboudi 2021 (a12, b32) | single-source |
| Formal hypotheses are rare in observed practice. | 0 of 12 developers stated one (Li and Coblenz). 79 vs 832 instances (VR study, second-hand). | Li and Coblenz 2026 (a13, a15, b09, b10) | established as description (K05); no outcome link |
| Ranked suspect lists help little. | 34 participants, then 10 more. Tetris 12:42 (tool) vs 14:14 (none), n.s. NanoXML 20:16 vs 22:30, n.s. High performers on Tetris 8:51 vs 14:28 (p<0.05). Fault at rank 7 vs 35: same time ratio 0.79 (N=10). 37% of list visits skipped more than one position. | Parnin and Orso 2011 (b12, b13) | established (K17) |
| Seeing the faulty line does not mean knowing it is faulty. | Of 10 who clicked the faulty line, 1 stopped using the tool. Others spent 61% of time (about 10 more minutes) still inspecting. | Parnin and Orso 2011 (b14) | single-source |
| Why/why-not questions over a trace helped strongly (author-run). | Alice: about 8x less time, 40% more tasks. Java: about 3x success, 2x speed. | Ko and Myers 2004, 2009 (a29, a30) | contested (K16) |
| Real execution output must feed the loop. | AutoSD plausible patches 73% (real debugger) vs 63% (model-imagined). DONE token: +12.4 points plausible with real output, -11 with imagined. With DONE and plausible: 89% correct vs 82% without. | Kang et al. 2023 (a19, b25, c02) | established (K09, with LDB a21, XYEval d02) |
| LDB: real variable values per basic block beat imagined traces. | HumanEval GPT-3.5 seed 73.8: Self-Debug +7.3, LDB +9.1 (82.9). GPT-4 seed 87.2: +1.2 vs +2.4. Reflexion seed 91.5: +0.6 vs +3.6 (95.1). 20 rounds: 84.1% (GPT-3.5). | Zhong et al. 2024 (a21) | single-source |
| Print debugging beats rubber-duck explanation. | GPT-4 Leetcode. +1.5 points (easy), +17.9 (medium), nothing on hard (about 5%). | Hu et al. 2024 (c07) | single-source |
| AutoSD loop matches plain prompting on repairs, at about 5x the time. | ARHE: LLM-Base 179 plausible / 177 correct; AutoSD 189 / 187. Defects4J 1.2: 87 plain vs 76 AutoSD. Defects4J 2.0: 110 vs 113. | Kang et al. 2023 (a18, c01, d10) | single-source (K08) |
| Hypothesis traces can mislead readers. | 20 people (8 undergraduates, 6 graduates, 6 professionals), 12 review items. Better with explanation in 7, worse in 2 (ARHE105: accepted wrong reasoning; BIP003: grew cautious). 70% wanted explanations. | Kang et al. 2023 (a20, c03, d10) | single-source |
| Model self-diagnosis is the repair bottleneck. | GPT-4 own explanation 33.3% vs human 52.6% repair success (1.58x). Intro 42.6 to 62.2; interview 19.3 to 45.7; competition 3.7 to 14.7. Obviously wrong feedback: 32/80 (GPT-4) vs 7/80 (human). Doubt expressed: 7/80 human vs 0/80 GPT-4. 16 participants, 40 programs. | Olausson et al. 2024 (b20, b21, d09) | single-source (K10, K22) |
| At matched budget, repair barely beats resampling (older models). | GPT-4 APPS: 10 samples + 1 repair each = 1.05x pass@20; 2 samples + 10 repairs = 0.97x pass@22. Better (stronger-model) feedback beat both. | Olausson 2024 (b19, d08) | single-source (K21) |
| Intrinsic self-correction without outside signal does not help. | GPT-3.5 GSM8K 75.9 to 75.1 to 74.7. CommonSenseQA 75.8 to 38.1 to 41.8. GPT-4 GSM8K 95.5 to 91.5 to 89.0. With oracle label: 84.3 (GPT-3.5), 97.5 (GPT-4). Columns are calls 1, 3, 5. | Huang et al. 2024 (b22) | established (K11) |
| A wrong supplied cause lowers coding-agent pass rate. | SWE-bench Verified pass@1: 77.2 to 68.8, 78.0 to 70.8, 79.8 to 71.4 (three Gemini models; about 9 to 11% relative). Terminal tasks up to 46.7% relative. One SWE-bench Pro cell rose 2.4%. | Wu et al. 2026, XYEval (d01) | single-source (K19) |
| Running tests rescues much of that harm. | Even told to obey the wrong advice: 50.2 to 60.6 pass@1. Turn counts almost the same as control. | XYEval (d02) | single-source |
| A generic warning only partly protects. | SWE-bench Verified drop: none / warning / oracle-named: 3.1 Pro -10.9 / -11.1 / +1.3; 3.5 Flash -9.2 / -6.7 / -0.8; 3.7 Flash -10.5 / -9.3 / -7.9. Terminal-Bench: warning cut -46.7% to -18.3% (3.1 Pro). Human parallel: warnings did not stop over-reliance (Serafini, N=76, second-hand). | XYEval (d03); Biolo 2026 related work (d16) | single-source (K20) |
| For small models, re-showing the failed attempt hurts. | MBPP+ pass@1 at k=8 (resample / placebo / feedback / reflect): 1.5B .749 / .688 / .688 / .688; 3B .778 / .709 / .735 / .743; 7B .820 / .802 / .810 / .828. Placebo minus resample: -0.061 (p=0.006) at 1.5B, -0.069 (p<0.001) at 3B. Near-identical retries 33 to 68% vs 2 to 14%. Reflection costs 2.5 to 5.5x tokens. | Verma 2026 (d04, d05) | single-source (K14) |
| Contradicting small-model result on feedback content. | 3 models of 0.5B to 1.5B, 290 dead task cells. Blind resampling beat bare-code retry by +18 net unlocks (25/7, Holm p=0.0021). Code plus executed facts beat bare code by +18 (21/3, p=0.00042) and a generic placebo by +15 (p=0.0041). | Can 2026 (d06) | single-source |
| Debugging decays with attempts; fresh start helps. | Most models lose 60 to 80% of debugging capability within 2 to 3 attempts. Fresh start: llama3.1:8b 72.56 to 82.82; deepseek-coder-v2:16b 84.1 to 92.1; Mistral 54.3 to 62.8 and 57.3. | Debugging Decay Index 2025 (c13) | single-source (K14) |
| Handing over the debugger after failed rewrites works best. | SWE-bench-Lite, Claude 3.7 Sonnet: rewrite-only 37.2, debugger from start 48.4, debugger after 5th rewrite 52.1. Llama-3.3-70B: 2.4 / 4.0 / 4.8. (Column mapping by position.) | debug-gym, Yuan et al. 2025 (c11, c12) | established (K13) |
| A follow-up turn lifts debugging chat agents. | Python: plain "why" 57%, targeted query 67%, with follow-up 85%. C/C++: root cause fixed 36%, proximate cause only another 55%. Follow-up text was identical. | ChatDBG 2025 (b28, c10) | single-source |
| Failed agent runs find the file but fail at fine reasoning. | Failures took about 20 more steps (OpenHands, SWE-agent) and 49 more (Prometheus) on Lite; 44, 22, 74 more on Verified. | Majgaonkar et al. 2025 (b29) | single-source |
| Confirmation bias in hypothesis testing; disconfirming tests go with success. | Wason game, 11 LLMs: mean rule discovery 42% to 56% with prompts. Think-in-Opposites helped in all settings, Dual-Goal in 8 of 11. FalsifyBench, 12 LLMs, 1,200 games: instruction-tuned best 41%; reasoning GPT-5.2-Chat 75%, GPT-OSS-120B 68%; GPT-5-Nano 12%, Qwen3.5-9B 21%. Positive-test share: reasoning 24 to 39%, instruction-tuned 66 to 82%. Confirmation bias OR 0.016; oracle error no credible effect. | Jhaveri 2026 (c14); Bertolazzi 2026 (c16, d15) | established as pattern (K12); transfer to code untested |
| Negative tests are required only when the guess is narrower than the truth. | Restated Klayman and Ha condition. No code task in the paper. | FalsifyBench (d15) | single-source (K24) |
| Models favour narrow hypotheses; evaluating beats generating. | Number game, 8 non-thinking models. Models pick more correct hypotheses when evaluating a list than when generating. Thinking mode reduces narrow bias. | Xiong 2026 (b30, c06) | single-source |
| Hypothesis step helps localisation in one agent system. | 591 bug reports. MAP full 0.407 (doc) / 0.226 (method). No hypothesis module: 0.379 / 0.195. No investigation: 0.360 / 0.183. No filtering: 0.364 / 0.189. | CogniGent, Samir and Rahman 2026 (c05, d11) | single-source (K23) |
| Diagnosis stage pays in a SWE-bench agent at about 1.9x cost. | Pro ablation (50 issues, GPT-5.4-mini): full 56.0, no diagnosis 48.0, mini-SWE-agent 44.0, live-SWE-agent 40.0. Five-run mean 54.0 (SD 2.0) vs 42.4 and 45.2. Cost per issue Verified $0.43 vs $0.23 and $0.22. | SWE-Doctor 2026 (d12) | single-source |
| Hypothesis format costs more tokens at equal outcome (test generation). | Branch coverage about 80% for iterative and both scientific arms vs 55% single-shot. Cost: baseline $5.09, iterative $37.1, scientific 0-shot $52.4, 1-shot $58.6 (about 41% more than iterative). | Straubinger et al. 2025 (c04) | single-source |
| LLM access did not raise verified bug fixes; hallucination loops. | 24 recordings, 9 Eiffel tasks, GPT-4o mini. All chart indications lower for LLM group, no test. Copy-paster style 38%. | Huang et al. 2025 (d14) | single-source |

Three things to keep in mind when reading this table.

1. The only direct test that supplying hypotheses helps is one lab study. Everything else is indirect.
2. "Six times" is an odds ratio. Raw success was 80% versus 55%. The data are also compatible with no effect (Fisher p about 0.18, our calculation).
3. No finding in the table shows what a wrong-only supplied hypothesis does to a human. Both supplied lists always held the right item.

---

## 4. Mechanisms and models

Each mechanism below is written so an engineer can build it. The program decides; the model fills a slot.

### 4.1 The two-gate model of debugging success

From Alaboudi and LaToza (b04, a03). Success needs two things in order.

- **Gate 1, diagnosis:** the debugger holds the correct cause. Predicts a fix with about 5x odds.
- **Gate 2, repair:** the debugger turns the cause into a working edit. 6 of 20 failures passed gate 1 and failed gate 2.

Implementation. Score and log the two gates separately for every debugging-type item.
- Diagnosis score: does any hypothesis in the ledger (4.2) match the true cause? On our bench, use items where the true cause is known (seeded bugs, ARC items with a known rule).
- Repair score: does the final answer pass the held-out check?
- Four cells: right cause and fixed; right cause and not fixed; wrong cause and fixed anyway; wrong cause and not fixed. The second cell tells you where to spend tokens.

Related (b29, a22): in agent traces the right file is usually found. Failure is in fine-grained reasoning. So locating the region is not the bottleneck for agents either. It is explaining.

### 4.2 The hypothesis ledger

A plain data structure kept in code, not in the model's prose.

```
Hypothesis {
  id, text (one sentence: "X causes Y because Z"),
  scope: narrow | broad | unknown        # for test choice, 4.6
  prediction: "if true, running T gives R"
  test: a runnable probe (command, input, print)
  status: open | supported | rejected | undecided
  evidence: [raw outputs from code, never model prose]
  confidence: model-stated, 0..1, logged only
  source: generated | supplied | retrieved
}
```

Rules.
- Predictions are written before the test is run.
- Status changes only from executed output (G2, G10).
- A broken experiment sets status to `undecided`, never `rejected`. AutoSD's main failure was a breakpoint on a line never reached, which left the hypothesis undecided; the scaffold needs that state explicitly (b27, 25 failed cases).
- Rejected hypotheses stay in the ledger as one-line entries. They are used for restarts (4.5).
- The ledger is logged at S3 before any S4 check. That gives the measurement Alaboudi used: hypotheses scored before testing.

### 4.3 The loop (scientific debugging, Zeller; AutoSD)

```
S3: model writes up to K hypotheses, each with prediction + probe   (K tested, see U-rows)
S4: code runs each probe for real; stores raw output
    model writes conclusion per hypothesis: supported / rejected / undecided, citing the output
S5: model writes the fix from supported hypotheses only
    (AutoSD removed rejected hypotheses from the prompt before writing the patch: it improved repair)
```

Facts that shape it:
- Observation must be real (K09). Imagined debugger output dropped plausible patches from 73% to 63% and flipped the DONE signal.
- The format alone is not an accuracy win (K08). AutoSD was at parity and cost about 5x time. Straubinger's version cost about 41% more than plain iteration. So the loop must pass the equal-token test (G7) before it stays.
- The loop's value is explanation and a trace code can inspect.

### 4.4 Where hypotheses come from: four sources and what is known

1. **Generated by the model from the failure.** Models are weak here: GPT-4 explanations were obviously wrong 32/80 times (b21) and never voiced doubt (0/80). Models favour narrow hypotheses (c06).
2. **Evaluated from a supplied list.** Models do better evaluating a list than generating (c06). This is the case that matched the human result: a short list with test steps helped even at 50% precision (b02).
3. **Retrieved from similar past cases.** Experience let one developer skip information gathering (b11, single anecdote). Gould found about 3 times better efficiency on a program debugged before (a24). This maps to the lessons memory, but is untested here.
4. **Asked from the failure by questions.** Why-did and why-didn't questions over a recorded run (Whyline, a29, a30). Backward reasoning from wrong output.

Design consequence. Hypothesis generation is a bottleneck (K03, K10). Generation and evaluation give different answers in models (c06). So: generate several, let code test them, do not ask the generator which is best (G5, G8).

### 4.5 Fixation and how it works in a model

Two mechanisms are seen in LLMs.

- **Anchoring on a supplied wrong cause** (XYEval). Pass@1 dropped about 9 to 11% relative on SWE-bench Verified. Turn counts did not rise, so the harm is "off-track reasoning, not more turns" (d02). A length or turn budget will not detect it. Tracking which hypothesis the agent is testing will.
- **Anchoring on the model's own failed output** (Verma, DDI). For models up to 3B, showing the failed program hurt more than a fresh draw (d04, d05). The cross-task control (other tasks' solutions in the prompt) did nothing, so it is not just length. The mechanism is conditioning on the earlier attempt. DDI reported the same direction on 8B to 16B local models (c13). Frontier models are untested.

Defences, with evidence on each.
- Real runs (strongest; d02: 50.2 to 60.6 even when told to obey wrong advice).
- A generic "distrust the hint" warning: weak (d03: -10.9% to -11.1% for Gemini 3.1 Pro, no change). Do not rely on it.
- Naming the exact wrong item removes the harm (d03), but that is an oracle.
- Restart from the original prompt plus a short rejected-hypotheses list (not tested on strong models). Can's finding that executed facts help (d06) suggests adding observed facts to that list.
- Repeat detector: weak models kept rewriting the same wrong chunk (c12). Code can detect it.

### 4.6 Test design: confirm, disconfirm, scope-matched

Humans and LLMs prefer tests that fit their guess. In rule-discovery games, negative testing predicts success and confirmation bias predicts failure (c14, c16). But Klayman and Ha: a negative test is needed only when the hypothesis is narrower than the truth. A broader hypothesis can be falsified by a positive test (d15).

Implementable rule for code:
- Label each hypothesis `scope`:
  - narrow: names a single input path or case ("fails when list has one element"). The real cause may be broader. Run a probe outside the named case. Falsify by finding the same failure elsewhere.
  - broad: names a general cause ("sort mutates the input"). A single positive probe that should fail and does not will falsify it.
- Count the share of probes aimed at breaking the leading hypothesis. Log it. FalsifyBench found reasoning models use 24 to 39% positive tests and instruction-tuned models 66 to 82%.
- Competing view (c17): when the hypothesis generator is weak, confirming tests keep proposals valid and converge faster on simple rules. Falsifying probes win when the rule is compound or has exceptions. So "always disconfirm" is not safe.

### 4.7 When to change method (gating)

debug-gym (c11): the best arm gave the debugger only after 5 failed rewrites. That is G1 (doubt on a signal) applied to tool use. A parallel finding in the agent traces: failed runs are longer (b29), and in humans heavy-tailed episodes dominate time (b31). So the signal is cheap: count failed patches, count repeats.

Conditions that fit the evidence:
- Run k plain rewrites first (k=5 in debug-gym; the right k for us is untested).
- Then switch to instrumented probing (print, trace, debugger).
- Do not give weak models the debugger unconditionally; they do not know how to use it (c11).

### 4.8 Information scent as a ranker

Information foraging (a16) says developers follow scent. A scent ranker for the ledger: order open hypotheses by how many words in the error text or failing output match the hypothesis. Code does the matching; this is a plain tiebreaker. No evidence it beats other orders. It exists to give code a way to choose the next probe without asking the model.

---

## 5. What holds up

### 5.1 Replications and independent agreement

- **No replication of Alaboudi 2020 was found** (K01, d13). One lab, 20 analysed participants (25 recruited, 5 piloted), three tasks. The word "replication" appears nowhere for this effect.
- **Fault locations not helping** is supported by two independent human studies: Alaboudi 2020 (a05) and Parnin and Orso 2011 (b12 to b14). Established (K02, K17).
- **Real execution beats imagined execution** is supported by AutoSD (73% vs 63%), LDB, Hu et al. (print debugging beats rubber duck), Chen et al. (gains largest with unit-test feedback, up to +12%; explanation alone +2 to 3%) and XYEval (running tests rescued 50.2 to 60.6). Established (K09).
- **No self-correction without an outside signal** is supported by Huang et al. and Olausson. Established (K11).
- **Debugger access helps strong models and hurts weak ones** is supported by debug-gym and ChatDBG (and Levin's authors note longer prompts can degrade the model). Established (K13).
- **Confirmation bias in LLM hypothesis testing** is supported by Jhaveri, FalsifyBench and Banatt (second-hand, best model 26%, N=50). Established as a pattern (K12), with the code transfer unproven.

### 5.2 Failures, nulls and conflicts

- **AutoSD parity.** Plausible and correct counts are level or mixed in sign across datasets (Defects4J 1.2: 87 vs 76, AutoSD worse by 11; 2.0: 110 vs 113). The paper's aim was explanation.
- **Olausson: repair is level with resampling at small budgets.** Verma, on small models, found blind resampling beats repair.
- **Verma versus Can** disagree on whether feedback content matters. Verma: executed feedback added nothing over a content-free "wrong" notice. Can: code plus executed facts beat the same code plus a generic placebo by +15 net unlocks. Both are single-author preprints on 0.5B to 3B models. Possible reconciliation: Can tested "dead" tasks where no best-of-8 sample passed (a selected hard subset). Not tested.
- **Arimbur** found self-repair gains of +4.9 to +17.1 points (HumanEval) and +16.0 to +30.0 (MBPP Sanitized) for seven models, but had no equal-token resampling control. It cannot separate feedback from extra draws (d07).
- **ChatDBG's jump from 67% to 85% on an identical follow-up text** may be a second-sample effect, not new reasoning (c10).
- **Li and Coblenz versus the hypothesis-driven view.** Observed developers did not state formal hypotheses. This does not say whether formal ones would help.
- **Time did not improve** with supplied hypotheses (p=0.61), and AutoSD costs 5x time. Gain is accuracy at a cost, not speed.
- **Fault-location tool gains in Parnin and Orso were unstable:** a first run showed a tool effect on Tetris that did not appear in the final run (b12).

### 5.3 Moderators

- **Task difficulty.** Alaboudi tasks 1 and 2 about 55% success, task 3 about 90%. Olausson: human feedback gain grew with difficulty (competition 3.7 to 14.7; interview 19.3 to 45.7). Hu: print debugging gains vanished on hard problems.
- **Model strength.** Debugger helps Claude 3.7 and hurts weaker models (c11). The XYEval harm differs by model; Claude Opus 4.8 was most resistant (d01). Verma: the penalty tracks baseline quality (r=0.96 across six configurations), confounded with size.
- **Bug type.** Gould: assignment bugs about 3x harder.
- **Own versus others' code.** Katz and Anderson (secondary): goal-driven for own code, data-driven for others.
- **Familiarity.** Forward tracing in familiar code, backward in unfamiliar (a14).
- **Interactive versus static tasks.** XYEval harm is much larger on terminal tasks (up to 46.7%) than SWE-bench (9 to 11%) because test runs recover part of the loss.
- **Experience.** OR 1.14 per year (Alaboudi), median 2 years. Expertise effects untested properly.

### 5.4 Interventions that worked

- Supplied hypotheses with test steps (humans; OR 6.24; weak evidence).
- Real debugger or print output instead of imagined (several studies).
- Gating the debugger after repeated failures (debug-gym, +3.7 points over always-on for Claude 3.7).
- Fresh start at a decay point (DDI, +8 to +10 points on 8B and 16B models).
- Stronger or human diagnosis fed to a weaker repair step (Olausson, 1.58x).
- Prompts to seek disconfirming tests, in reasoning models (Jhaveri; 42% to 56%).
- Why-not questions on a trace (Whyline; author-run).
- Print/probe over rubber-duck (Hu; medium problems +17.9).

### 5.5 Interventions that did not work

- Supplied fault locations or ranked suspect lists (humans).
- Rank position of the true fault (7 vs 35: no change in time ratio, N=10).
- A generic "be wary of misleading advice" warning (XYEval; also second-hand human data).
- Self-review without outside signal (Huang).
- Reflection to weaken anchoring: partial, at 2.5 to 5.5x tokens, not significant at 7B (+0.8) (d05).
- Prompting with execution traces alone, without training (Ni et al.: average drop of 7.8% for some models vs vanilla prompting; c18).
- Scientific-debugging format as an accuracy booster (parity at best, costlier).

---

## 6. Language models

### 6.1 What models do on these tasks

1. **They generate weak diagnoses.** GPT-4 explanations of failing code: obviously wrong 32 of 80 times against 7 of 80 for humans. Zero of 80 expressed doubt (humans 7 of 80). (b21, d09.)
2. **Diagnosis quality is the lever.** Human explanation instead of GPT-4's own raised repair from 33.3% to 52.6%. The lift grew with difficulty (competition 3.7 to 14.7). Stronger-model feedback also lifted weaker models. This is the nearest LLM analogue of the six-fold human result (b20, c09).
3. **They are bad at self-checking without outside signal.** Huang: GSM8K 75.9 to 74.7; CSQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 89.0. Correct answers get changed. (b22.)
4. **They anchor.** Wrong supplied cause: 9 to 11% relative drop on SWE-bench Verified. Own failed program: worse than a fresh draw up to 3B (pass@1 .688 vs .749 at 1.5B; .709 vs .778 at 3B). By 7B the arms tie.
5. **They favour confirming tests.** Instruction-tuned models used 66 to 82% positive tests; reasoning models 24 to 39%. Reasoning models won (75% vs 41%).
6. **They prefer narrow hypotheses** in a toy domain, and generalise poorly beyond the examples (c06).
7. **They benefit from real execution, not imagined.** 73% vs 63% (AutoSD); LDB per-block values (+9.1 vs +7.3 on GPT-3.5).
8. **A fluent wrong explanation persuades humans.** AutoSD ARHE105: reviewers accepted wrong reasoning. Also the hallucination loops in Huang 2025.

### 6.2 What changed behaviour, and by how much

| Change | Effect | Model(s) | Source |
|---|---|---|---|
| Debugger after 5 failed rewrites (vs rewrite-only) | 37.2 to 52.1 (SWE-bench-Lite) | Claude 3.7 Sonnet | c11 |
| Debugger from start (vs rewrite-only) | 37.2 to 48.4 | Claude 3.7 Sonnet | c11 |
| Debugger on weak model | 2.4 / 4.0 / 4.8 (rewrite / start / after 5) | Llama-3.3-70B; some models harmed when always-on | c11 |
| Real vs imagined debugger output | 73% vs 63% plausible | ChatGPT-era model | a19 |
| Human instead of model diagnosis | 33.3 to 52.6 repair | GPT-4 | b20 |
| Wrong supplied cause | -8.4 / -7.2 / -8.4 points pass@1 | Gemini 3.1 Pro, 3.5 Flash, 3.7 Flash | d01 |
| Wrong cause on terminal tasks | up to -46.7% relative | five models | d01 |
| Told to obey the wrong cause | 50.2 to 60.6 pass@1 | Gemini 3.1 Pro, 3.5 Flash | d02 |
| Fresh start at decay point | +10.3 (72.56 to 82.82), +8.0 (84.1 to 92.1) | llama3.1:8b, deepseek-coder-v2:16b | c13 |
| Blind resample vs show failed code | +6.1 to +6.9 points | Qwen2.5-Coder 1.5B and 3B | d04 |
| Disconfirm prompts (rule discovery) | 42% to 56% mean | 11 LLMs | c14 |
| Diagnosis stage in agent | 48.0 to 56.0 (50 Pro issues) | GPT-5.4-mini | d12 |
| Hypothesis module in localiser | MAP 0.379 to 0.407 | Devstral | d11 |
| Follow-up turn (same text) | 67% to 85% | ChatDBG model | c10 |

### 6.3 What is not known for LLMs

- Whether supplying a correct, a wrong, or no hypothesis changes repair at equal tokens. XYEval ran only the wrong arm. The correct-hint and no-hint arms at matched tokens are missing (K18).
- Whether the hypothesis loop beats best-of-N at equal tokens on current models. The nearest data are Olausson (older models), Verma (small models) and cost-unmatched agent papers (AutoSD about 5x, SWE-Doctor 1.9x) (K21).
- Whether generate-many-then-select closes the human gap (K22).
- How many hypotheses to hold (K23).
- Whether the small-model restart finding holds on frontier models (K14).
- Whether disconfirm prompts help in code (K12, K24).

### 6.4 Caution on the LLM literature

- Several 2026 preprints (Verma, Can, Arimbur, XYEval, SWE-Doctor, CogniGent, FalsifyBench, Jhaveri, Xiong) are single-team or single-author. Treat each as a lead.
- XYEval wrong hints came from a user, not from the agent's own hypothesis.
- FalsifyBench and Jhaveri use rule-discovery games, not code.
- ChatDBG and debug-gym have no equal-token control.
- Contamination risk: Defects4J, HumanEval, Leetcode (flagged in a18, c13, c07).

---

## 7. What our agent should take

Format. Each item: what to do, schema part (G, S, O, or memory), status ([E] established, [S] single-source, [C] contested), evidence ids. "Add now" items are established. "Test first" items need the tests in section 8 and UNKNOWNS.md.

### Add now (established)

1. **Observations come from code, never from the model.** A hypothesis test counts only if its output was produced by a real run. Imagined debugger output is worse than none (73% vs 63%; DONE signal reverses). Schema part: G2 and G10 (already present); add to S4 and S5 explicitly that a hypothesis status is set from executed output only. **[E]**. Evidence: a19, b25, c02 (K09); a21; c07; c08; d02.
2. **Do not revise a hypothesis from the model's opinion alone.** Re-examination without an outside signal flips correct answers to wrong ones. Schema part: G2 (already present). **[E]**. Evidence: b22, b23, b19 (K11). No change to the schema, but cite K11 in G2.
3. **A location is not a diagnosis. Require a cause statement and a test.** If the agent is given or finds a line or region, S3 still writes a cause with a prediction. Ranked lists and locations did not help humans. Schema part: S3 (add as a one-line note); S4. **[E]**. Evidence: a05, b05, b12, b13, b14, a31 (K02, K17).
4. **Never accept a ranked or supplied suspect list on agreement; test it.** Developers scanned lists for items that fit their own guess, and they did not recognise the true cause when they saw it (10 clicked the faulty line; 1 stopped; others spent 61% more time). Schema part: S4. **[E]**. Evidence: b13, b14 (K17).
5. **Log diagnosis and repair as separate outcomes.** Right cause and no fix is a distinct failure (6 of 20). Locating is harder than fixing; failed agent runs reach the right file and fail at fine reasoning. Schema part: section 6 logging. **[E]**. Evidence: a03, b04, a22, b29 (K04 single-source for the 6 of 20; K15 established for the locate-fix claim). Add the log fields now; the split itself is measurement, not behaviour.
6. **Switch to instrumented probing only after repeated plain failures.** Gate by count of failed patches or repeated edits to the same region; not at the start for weak models, and not never for strong models. The threshold k is not known for us. Schema part: S6 operator (new operator "probe": print/trace/debugger), gated by the impasse detector. **[E]**, as direction. Evidence: c11, c12, b28, b29, c18 (K13). The value of k goes to UNKNOWNS.
7. **Put at least one probe in the plan that could refute the leading hypothesis before accepting it.** Reasoning models that test negatively succeed more. This agrees with S7's counterexample search (already **[E]**). Schema part: S4/S7, one line added to S4: "for the leading hypothesis, one probe must be able to refute it". **[E]** as a pattern in rule-discovery tasks; code transfer is unproven (see Test first #8). Evidence: c14, c16, b30, c06, d15 (K12). Hold the S4 text change until U10 passes, because transfer to code is the weak step. (This keeps to the rule that nothing unproven enters SCHEMA.md.)
8. **Do not use a hypothesis log's fluency as a correctness signal.** Wrong but fluent reasoning persuaded reviewers (ARHE105). Schema part: G10, G5 (judges see no explanation). **[E]** for G10; this case is single-source. Evidence: a20, c03, d10, d14.
9. **Do not add a generic "distrust the hint" instruction as a guardrail.** Warnings cut XYEval harm little (-10.9% to -11.1% for the best case) and did not stop human over-reliance. Schema part: section 4b "not to add" (candidate line). **[E]**: XYEval (d03) plus second-hand human data (d16). Strictly this is two sources, one of them second-hand. Mark as [E] in 4b only after Biolo's primary source (Serafini) is opened; for now it is [S].

Items 8 and 9: item 8 is anchored on G10 (already [E]); item 9 stays [S] until the primary human source is read.

### Test first (single-source or contested)

10. **Supply 1 to 2 candidate causes with test steps (S3 operator "hypothesis supply").** The human result is the headline. An LLM replay (correct, wrong, none; equal tokens) does not exist. **[S]**. Evidence: a04, b01, b02, d13, c25 (K01, K18). Test: U1.
11. **Test-the-hint step for any supplied cause (input hygiene in S1 + S4).** A forced "run a probe that would fail if this cause is wrong" before editing, versus a distrust prompt. **[S]**. Evidence: d01, d02, d03 (K19, K20). Test: U2.
12. **Hypothesis loop (hypothesis, prediction, experiment, observation, conclusion) versus best-of-N at equal tokens.** **[S]**. Evidence: a17, a18, d08, d10, d12, d04 (K08, K21). Test: U3.
13. **Generate many causes, test cheaply, pick by run.** Closes the diagnosis gap? **[S]**. Evidence: b20, b21, d09, c06 (K10, K22). Test: U4.
14. **Number of live hypotheses (1, 2, 4).** **[S]**. Evidence: a02, d11 (K03, K23). Test: U5.
15. **Restart with rejected-hypothesis list only, versus keeping full history.** **[S]**, small models only. Evidence: d04, d05, d06, c13 (K14). Memory/S6. Test: U6.
16. **Force a second hypothesis before the first test.** Anti-fixation for two-cause bugs. **[S]**. Evidence: a23, a07, a26, d01 (K07). Test: U7.
17. **Forced hypothesis-and-prediction template versus free-form reasoning.** Human practice is informal; the LLM may differ. **[C]**. Evidence: a13, b09, a15, a17 (K05). Test: U8.
18. **Scope-matched test choice (narrow vs broad) versus always-disconfirm.** **[S]**. Evidence: d15, c17 (K24). Test: U9, U10.
19. **Explicit `undecided` status when an experiment fails to run.** Design hygiene, **[D]/[S]**: AutoSD's main failure case. Evidence: b27. Test: U11 (cheap).
20. **Ask for a confidence per hypothesis, log only.** GPT-4 expressed doubt 0/80. **[S]**. Evidence: d09. Test: U12.
21. **Trace-query operator (why / why-not over a recorded run).** **[C]**: author-run only. Evidence: a29, a30, c22 (K16). Test: U13.
22. **Long-tail trigger: change strategy after N failed tests.** **[S]**. Evidence: a11, b31, b29 (K06). Test: U14.
23. **Retrieved similar-case hypotheses (memory).** **[S]**, single anecdote plus Gould's 3x on repeat programs. Evidence: b11, a24. Test: U15.

---

## 8. Concrete tests on our bench

General rule for every test below. Both arms get the same total tokens, setup and ledger overhead included (G7). Report pass rate and tokens per item. Use at least two seeds. Stratify by item difficulty (G12), because gains are bigger on hard items and vanish when the plain pass rate is near 100% or near 0.

| # | Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| T1 | Supplied-hypothesis replay (Alaboudi on a model) | Seeded-bug items with a known cause: small programs with one planted fault; ARC items with a known true rule (rule description as the "cause") | A: no hint. B: one wrong hint. C: two hints (1 right, 1 wrong) with test steps. D: one right hint. All with the same token cap; hint arms spend less on generation, so give A the saved tokens as extra samples | Pass rate on held-out check (G3); share of runs whose final answer matches the supplied wrong hint | D above A by a large margin (an oracle bound). C above A modestly (the human OR 6.24 translates to about +25 points raw; expect less). B below A by 5 to 10% relative (XYEval gives 9 to 11% on SWE-bench) |
| T2 | Test-the-hint versus warning | Same items as T1, wrong-hint arm | A: wrong hint, no instruction. B: wrong hint plus "be wary" warning. C: wrong hint, code forces one probe that would fail if the hint is wrong, before any edit | Pass rate; share of runs ending on the wrong hint; tokens | C recovers most of the loss (to within 2 points of no-hint); B recovers little (matches XYEval: -11.1% vs -10.9%) |
| T3 | Hypothesis loop versus best-of-N | Debugging-type items with a runnable check (code fixes, ARC program synthesis) | A: best-of-N fresh attempts (G3 check, code selects). B: ledger loop (K hypotheses, probes, fix from supported). Same total output tokens | Pass rate at the cap; tokens to first pass | Parity is the prior (AutoSD, Olausson). B wins only on hard items (plain pass rate 20 to 60%). Keep B only if it wins there |
| T4 | Generate many, test, pick by run versus single diagnosis | Items where the plain model's diagnosis is often wrong (Olausson-style, interview and competition level) | A: one diagnosis then repair, plus extra repair samples for equal tokens. B: M diagnoses, one cheap probe each, repair from best supported | Pass rate; diagnosis match to known cause | B closes part of the 33.3 to 52.6 human gap; if it closes under a third of the gap, drop |
| T5 | Dose of hypotheses | Same as T3 | A: K=1. B: K=2. C: K=4. Equal tokens | Pass rate; switch rate; wrong-fix rate; tokens per hypothesis | Inverted U. K=1 fixates, K=4 splits budget. Median human was 1 to 2 |
| T6 | Restart policy after failure | Items where the first 2 attempts failed | A: keep full history (failed patch and output). B: fresh prompt plus one-line rejected hypotheses. C: fresh prompt plus rejected hypotheses plus observed facts (Can-style). D: blind redraw | Pass rate of attempt 3; similarity of attempt 3 to attempt 2 | B and C above A if anchoring holds for our model. D is the control. At frontier size expect ties; at small size expect D to match B |
| T7 | Second hypothesis before first test | Items with two causes needed (like the two-line fix) or a decoy cause | A: test the first hypothesis at once. B: S3 must write 2 distinct hypotheses before any test | Rate of partial fixes (passes some checks, fails held-out); pass rate | B reduces single-cause misses; costs tokens on one-cause items. Keep only if net gain on mixed set |
| T8 | Forced template versus free-form | Mixed easy and hard items | A: free-form reasoning. B: ledger template with prediction before the test. Equal tokens | Pass rate by difficulty; tokens | Template hurts on easy items (G11, G1), neutral or helpful on hard. Gate by S0 class |
| T9 | Scope-matched test | Items where the hypothesis is narrow (single path) or broad | A: always-disconfirm. B: scope-matched. C: no rule | Probes needed to reject a wrong hypothesis; pass rate | B uses fewer probes than A at the same accuracy; both beat C if bias holds |
| T10 | Refutation probe required | Same as T9 | A: no rule. B: one refuting probe required for the leading hypothesis | Share of wrong accepted hypotheses; pass rate | B lowers wrong acceptance. Transfer from rule games to code is the unknown |
| T11 | Undecided state | Items with a flaky or unreachable probe (breakpoint on uncovered line) | A: failed probe treated as rejected. B: failed probe sets undecided and re-probes once | True hypotheses wrongly discarded | B keeps more true hypotheses. Cheap; almost no token cost |
| T12 | Confidence per hypothesis | Same ledger runs | Log only | Calibration: does stated confidence predict supported status? | Probably poor (0/80 doubt in GPT-4); if useless, never use it |
| T13 | Trace query versus breakpoints | Items with an execution trace | A: print/trace only. B: queryable trace with why-not queries | Pass rate; probes | Author-run human result suggests large gain; expect smaller; test needs a trace tool |
| T14 | Long-tail trigger | Long-horizon items | A: no trigger. B: after N failed tests or repeated edits to one region, force a new operator | Share of runs in the tail; pass rate | B shortens tail without hurting easy items. N unknown; try 3 and 5 |
| T15 | Similar-case hypothesis retrieval | Items from the same class as past solved ones | A: no memory. B: one lesson line shown after the first attempt (schema rule). C: lesson before the first attempt | Pass rate; fixation on lesson | B ≥ A; C may fixate (schema says lessons come after the first attempt) |

Baselines to include once. Gold-diagnosis ceiling: inject the true cause after S3 and measure repair. This sets the maximum any hypothesis method can reach. If the ceiling is near the plain pass rate, hypothesis work is not where the loss is.

---

## 9. What does not transfer, and why

- **The six-fold human number.** It comes from 20 graduate students on 3 small Stack Overflow web bugs, 36 to 45 lines, no internet, median 2 years experience. The supplied list always contained the accepted answer. A real generator does not. Do not plan around OR 6.24.
- **Human time and fatigue.** Humans pay for reading; hypotheses did not speed them. The agent's cost is tokens. The relevant output is pass rate at equal tokens.
- **Founding claims about novices.** Vessey's expert/novice contrast is about chunking ability among 16 COBOL programmers. A model has no novice/expert axis of the same kind. Not read in full.
- **"Developers rarely state hypotheses."** True of humans in familiar codebases. A model can be forced to state and test them, and the cost-benefit differs. This is a design choice, not a copy of human practice (K05).
- **Whyline gains.** Alice and two Java reports, authors' own tests. Strong for people who had no tool for asking why. Models have no such handicap if given traces.
- **Rule-discovery games (Wason, FalsifyBench, number game).** Hypotheses there are about a hidden rule, not a fault in a program. The test-design principle may transfer; the numbers do not.
- **Small-model anchoring (Verma, DDI).** Sizes 0.5B to 16B on function-level tasks. Ties by 7B for the main contrast. Frontier models may not show it.
- **XYEval hints.** The wrong cause came from a user. The agent's own wrong hypothesis may behave differently (it may be more or less sticky).
- **Fault-localisation lists.** Humans skip around lists and confirm. A model may read a list in order and trust it more. Untested.
- **Multi-year, multi-file, social debugging** (asking colleagues, reading logs of a live system). Out of scope on our bench.
- **ARC and BrainTeaser items.** They have no runtime to probe. Probing is only possible if the agent can run candidate programs on the given examples. For puzzle items without a runnable check, the ledger is still useful for logging, but "real execution" collapses to "check the candidate against the examples". G3 warns that fitting the examples is not proof.
- **Training results** (NExT, distillation in Jhaveri). Outside the no-training rule.

---

## 10. Open questions

1. Does the Alaboudi effect replicate with professionals, real bugs and larger N? Is the OR stable? (CI about 1.1 to 35.)
2. What does a wrong-only supplied hypothesis do to a human? Never run.
3. Does supplying correct, wrong or no hypothesis change LLM repair at equal tokens? (K18.)
4. Does the loop beat best-of-N at equal tokens on current models and SWE-bench-style tasks? (K21.)
5. Can generate-many-then-select close the human diagnosis gap? (K22.)
6. How many hypotheses should be held, and when to switch? (K23; links to Hypothesis limits in troubleshooting.)
7. Does the small-model restart result hold for frontier models, and does a rejected-only restart beat full history? (K14.)
8. Do Gould, Vessey, Katz and Anderson, Gilmore say what the summaries say about early-hypothesis fixation? Full text not reached; Vessey's PDF has no text layer.
9. When is a forced written hypothesis harmful (premature commitment avoided on purpose in Li and Coblenz)? Does it hurt on easy bugs?
10. Do disconfirm-test prompts transfer from rule games to debugging? Does the scope condition (Klayman and Ha) help?
11. Why do Verma and Can disagree on feedback content? Selected hard subset, model size, or design?
12. Does a hypothesis the agent wrote itself anchor more or less than one supplied by a user?
13. Can the agent recognise a true cause when it sees it? (Humans clicked the faulty line and did not stop.)
14. Do the Whyline gains replicate outside the authors' lab and for models?
15. How much of ChatDBG's 67% to 85% jump is a second sample?

---

## 11. Sources

[V] = opened and read this session (full text or the page described). [M] = snippet, abstract, or second-hand only. Where a source is [V] but only part was read, the note says so.

**Human studies**

- [V] Alaboudi and LaToza (2020). Using Hypotheses as a Debugging Aid. https://arxiv.org/abs/2005.13652 (PDF https://arxiv.org/pdf/2005.13652). Re-read twice (a01 to a08, b01 to b08, d13). Table III cell layout is ambiguous in text extraction; the per-task split used here (hypotheses 5/6, 5/8, 6/6; control 4/8, 2/6, 5/6; locations 2/6, 4/6, 7/8) is the only one whose sums match the 20 failures (critique correction 2).
- [V] Alaboudi and LaToza (2021). An Exploratory Study of Debugging Episodes. https://arxiv.org/abs/2105.02162 (PDF https://arxiv.org/pdf/2105.02162).
- [V] Alaboudi and LaToza (2021). Edit-Run Behavior in Programming and Debugging. https://arxiv.org/abs/2109.02682.
- [V] Li and Coblenz (2026). A Grounded Theory of Debugging in Professional Software Engineering Practice. https://arxiv.org/abs/2602.11435. (Marked opened by earlier agents; not re-opened in the cross-check.)
- [V] Arafa, Solomon, Navabpour, Fischmeister (2017). Debugging Behaviour of Embedded-Software Developers. https://arxiv.org/pdf/1704.03397.
- [V] Parnin and Orso (2011). Are automated debugging techniques actually helping programmers? PDF https://web.eecs.umich.edu/~weimerw/2018-481/readings/debugging-helping.pdf; DOI https://doi.org/10.1145/2001420.2001445. (Marked opened by earlier agents; not re-opened in the cross-check.)
- [V] Huang, Mustafin, Piccioni, Schena, Weber, Meyer (2025). Do AI models help produce verified bug fixes? https://arxiv.org/abs/2507.15822.
- [M] Gould (1975). Some psychological evidence on how people debug computer programs. https://research.ibm.com/publications/some-psychological-evidence-on-how-people-debug-computer-programs (abstract page only).
- [M] Vessey (1985). Expertise in debugging computer programs. https://archive.nyu.edu/handle/2451/14532 and https://aisel.aisnet.org/icis1985/18 (abstract page; PDF is a scan with no text; the "early hypotheses" line is from a search paraphrase).
- [M] Katz and Anderson (1987). Debugging: an analysis of bug-location strategies. https://www.ets.org/research/policy_research_reports/publications/article/1987/icwz.html ; https://www.academia.edu/18305405/Debugging (snippet).
- [M] Gilmore (1991). Models of debugging. https://www.sciencedirect.com/journal/acta-psychologica (search description only; citation not checked).
- [M] Bohme et al. (2017). How developers debug software: the DbgBench dataset. https://doi.org/10.1109/icse-c.2017.94 (abstract).
- [M] Ko and Myers (2004). Designing the Whyline. https://doi.org/10.1145/985692.985712 (abstract).
- [M] Ko and Myers (2009). Finding causes of program output with the Java Whyline. https://doi.org/10.1145/1518701.1518942 (abstract).
- [M] Serafini et al., via Biolo et al. (2026) related work. https://arxiv.org/abs/2606.25973 (second-hand).
- [M] Brooks, Letovsky, Robin, Gugerty and Olson, Layman, Perscheid: cited via Alaboudi 2020 and 2021 only.
- [M] Shapiro (1983). Algorithmic Program Debugging (recalled, no URL).
- [M] Zeller (2002, 2009). Isolating cause-effect chains / Why Programs Fail (recalled, no URL).

**LLM studies**

- [V] Kang, Chen, Yoo, Lou (2023). Explainable Automated Debugging via LLM-driven Scientific Debugging (AutoSD). https://arxiv.org/abs/2304.02195 (PDF https://arxiv.org/pdf/2304.02195).
- [V] Olausson et al. (2024). Is Self-Repair a Silver Bullet for Code Generation? https://arxiv.org/abs/2306.09896.
- [V] Huang et al. (2024). Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798.
- [V] Zhong et al. (2024). Debug like a Human: LDB. https://aclanthology.org/2024.findings-acl.49.pdf.
- [V] Chen, Lin, Scharli, Zhou (2023). Teaching LLMs to Self-Debug. https://arxiv.org/abs/2304.05128.
- [V] Hu, Kuang, Sun, Yang, Wu (2024). Leveraging Print Debugging to Improve Code Generation in LLMs. https://arxiv.org/abs/2401.05319.
- [V] Levin, van Kempen, Berger, Freund (2025). ChatDBG. https://arxiv.org/abs/2403.16354.
- [V] Yuan et al. (2025). debug-gym. https://arxiv.org/abs/2503.21557.
- [V] The Debugging Decay Index paper (2025). https://arxiv.org/abs/2506.18403.
- [V] Majgaonkar et al. (2025). Understanding Code Agent Behaviour. https://arxiv.org/abs/2511.00197.
- [V] Straubinger, Kreis, Lukasczyk, Fraser (2025). Mutation Testing via Iterative LLM-Driven Scientific Debugging. https://arxiv.org/abs/2503.08182.
- [V] Samir and Rahman (2026). CogniGent. https://arxiv.org/abs/2601.12522.
- [V] Ni et al. (2024). NExT. https://arxiv.org/abs/2404.14662.
- [V] Xiong (2026). Hypothesis generation and updating in large language models. https://arxiv.org/abs/2605.05851.
- [V] Jhaveri, GX-Chen, Sucholutsky, Choi (2026). Failing to Falsify. https://arxiv.org/abs/2604.02485.
- [V] Bertolazzi, Tentori, Bernardi (2026). FalsifyBench. https://arxiv.org/abs/2606.04751.
- [V] Chari and Pattanaik (2026). Wild Guesses and Mild Guesses in Active Concept Learning. https://arxiv.org/abs/2602.06818.
- [V] Wu, Li, Tafjord, Kim (2026). XYEval: Agents say yes to bad advice. https://arxiv.org/abs/2609.23939.
- [V] Verma (2026). Try Again, Don't Look Back. https://arxiv.org/abs/2607.26117.
- [V] Can (2026). Falsification, Not Exposure. https://arxiv.org/abs/2606.31511.
- [V] Arimbur (2026). How Many Tries Does It Take? https://arxiv.org/abs/2604.10508 (abstract and opening only).
- [V] Anonymous authors (2026). SWE-Doctor. https://arxiv.org/abs/2607.00990.
- [V] Biolo, Tezza, Gong, Massacci (2026). Helpful or Harmful? https://arxiv.org/abs/2606.25973 (protocol; related work read).
- [M] Follow-ups to AutoSD: DoVer https://arxiv.org/abs/2512.06749, DebugHarness (2026), mutation-testing paper (abstracts via arXiv API only; DoVer: flips 18 to 28% of failed trials; DebugHarness: about 90% of SEC-bench bugs).
- [M] Banatt et al. (2024), Wason 2-4-6 as an LLM benchmark (via Jhaveri et al.; best model 26%, N=50).
- [M] Shapiro-descendant LLM paper arXiv 2603.20334 (title listing only).
