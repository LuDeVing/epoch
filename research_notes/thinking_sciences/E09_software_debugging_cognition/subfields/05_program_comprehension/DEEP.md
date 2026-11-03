# Program comprehension: deep document

*Subfield E09.05, reading strategies. Key works: Brooks (1983), Letovsky (1987), ICSE 2025. Built from evidence_a-d.jsonl (a01-a27, b01-b25, c01-c25, d01-d19), claims.jsonl (K01-K22) and critique.md in this folder. Many rows repeat one paper: Paltenghi (b17, c03, c21), Li (a18, b18, c01), Kou (b19, c02, c19, c20), Peitek 2021 (b08-b10), Peitek 2018 (a14, a15, b05-b07), Copilot study (c16, c22), RepoNavigator (c10, c24), CodeSense (b23, c09, c23), Orvalho (d01-d03). Count papers, not rows.*

*Main cautions. The classic theories (Brooks, Soloway, Pennington, Letovsky) were read only through the 1995 von Mayrhauser and Vans review and the 2023 Wyrich review. No primary numbers for Soloway and Ehrlich (1984) or Pennington (1987) were verified. Do not cite figures for them. No study was found that tests hypothesis-first reading against bottom-up reading for an LLM agent at equal tokens.*

## 1. What it is

Program comprehension is how a person (or a model) builds an internal picture of what code does and why. The goal is not to memorise the text. The goal is a model good enough to act: fix a bug, add a feature, review a change, answer a question.

Three things matter for us.

1. Reading strategy. Does the reader start from a guess about the purpose (top-down), build up from lines and chunks (bottom-up), or switch as needed (opportunistic)? [a01, a03, a09]
2. Cues. Names, comments, signatures and standard code shapes ("beacons") let a reader jump from a guess to a check. [a08, a15]
3. Episodes. Think-aloud studies break reading into labelled steps: read, ask why, conjecture, simulate, verify. Letovsky's why/how/what questions and "dangling purposes" are the clearest scheme. [a06] Those labels are what we want for logging agent traces.

Link to earlier work: Gilmore's point that comprehension is part of the debug loop, not a step before it [a23]. Overlaps with the schema's localise and hypothesise states, guardrails G2/G3 (revise only from real output; pass on something not fitted to) and G10 (reasoning text is not evidence). Parallel subfields (program comprehension models, distributed cognition, chain-of-thought, worked examples, confidence and metacognition) are only linked here, not covered.

Scope fact: most human studies use short snippets (median pool of 9) and students (53.7% students only). The 1995 review notes that few studies use code above 900 lines, and that models assume "understand everything", while debugging needs partial understanding. [b01, a09]

## 2. History and theories in depth

### 2.1 Early cognitive models (1978-1987)

- Shneiderman and Mayer (1979), bottom-up model. Programmers recode statements into chunks, then chunks of chunks, into a language-free semantic structure. Long-term memory splits into syntactic (language-bound) and semantic knowledge. [a03] This is the origin of chunking as the core mechanism.
- Brooks (1978, 1983), top-down model. Understanding is a rebuild of the map from problem domain to code across intermediate domains. His example chain has four domains: inventory, accounting, mathematics, programming language. A vague primary hypothesis is refined into subsidiary hypotheses until each can be matched to code. Hypotheses are "the only drivers of cognition". Beacons confirm or reject them. Understanding is complete when the hierarchy is full. [a01, a02] The 1983 paper named beacons for the first time. Long dwell on one snippet is read as trouble finding a hypothesis. [a02] Weakness (1995 review): knowledge structures are left undefined.
- Soloway and Ehrlich (1984). Experts hold programming plans and rules of discourse (conventions). Experts beat novices on plan-like code, and unconventional code hurts even experts. [a04] Exact numbers not verified (d17).
- Wiedenbeck (1986). Two experiments: beacons help experienced programmers mainly. [a08, b14] Sample sizes not recovered.
- Littman, Pinto, Letovsky and Soloway (1986/87). A systematic strategy (symbolic execution of data-flow paths between routines) gave strong mental models and better modification. An as-needed strategy gave weak models. [a07] Later, Koenemann and Robertson (1991) found as-needed reading is common and goal-driven, with bottom-up used when hypotheses fail. [a07]
- Letovsky (1987). Knowledge-based understander: a knowledge base, a mental model with three layers (specification, implementation, annotation) and an assimilation process. Conjectures are why, how and what questions with graded certainty. A dangling purpose is a goal-to-code link left unresolved. Data: think-aloud video of 6 professionals adding a feature. [a06] Journal date 1987, often cited as 1986.
- Pennington (1987). Two representations. The program model (control flow, elementary operations) forms first, bottom-up from beacons. The situation model (data flow, function, goal hierarchy) forms later. Experts' memory for new code rested on procedural units, not functional ones. [a05] Numbers unverified (d18).

### 2.2 Integration (1995)

von Mayrhauser and Vans compared six models and merged them: top-down (Soloway), program and situation models (Pennington), plus a knowledge base. Programmers switch between all three. Chunking and cross-referencing are the two mechanisms. Comprehension is opportunistic. [a09] Their experiment census showed mostly observational studies on programs under 900 lines. Gilmore (1991) argued comprehension sits inside a debugging loop. [a23]

### 2.3 Replications and revisions (1997-2024)

- Burkhardt, Detienne and Wiedenbeck (1997) tested Pennington on object-oriented code. The situation model was better than the program model, and stronger for experts. This contradicts program-model-first for OO code. [a13]
- Busjahn et al. (2015) eye tracking: novices read less linearly than prose, experts less than novices. [a10] Peitek, Siegmund and Apel (2020) replicated non-exactly and found code linearity mattered more than reader experience. [a11]
- Siegmund (2014) first fMRI study of bottom-up reading (cited, not opened [b16]). Siegmund/Peitek (2017-2018) replicated it and added cue-based reading. [a14, b05]
- Wyrich, Bogner and Wagner mapped 95 experiments from 1979-2019 and found little shared design. [b01-b04]
- Schroeder and Koschke (2024): in recorded IDE behaviour, the patterns predicted by top-down and bottom-up models were not observed. They use abstracted action patterns (file visits, edits) instead. [a26]

### 2.4 Now: AI-era comprehension (2020-2026)

Four new lines. (1) Do LLMs "read" like people (attention alignment)? [a18, b17, b19] (2) Can LLMs predict execution and semantics (CRUXEval, CodeSense, EquiBench)? [c07, b22, b23] (3) How do people comprehend and judge AI-written code? [c14, c15, c16] (4) For agents: repository navigation and localisation. [c10, c11, d11, d14] ICSE 2025 items: a27 (student attention in code summarisation, n=27) was seen as a snippet only; a16 (code review comprehension, 10 reviewers) was read.

## 3. Core findings with exact numbers

Status: E = established (two or more independent papers agree), S = single source, C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Top-down hypothesis refinement with beacons is the classic model; experts switch among top-down, program and situation models | 4-domain chain in Brooks' example; metamodel from 6 models | a01, a09 (via review) | S |
| Situation-model questions beat program-model questions (OO code); experts higher | 4.36 vs 3.55 of 6, F(1,43)=110.94; experts 4.56 vs novices 4.10; about 46 subjects | a13 Burkhardt 1997 | E (against Pennington order) |
| Novices read more linearly than experts | about 80% linear on text, 70% on code (novices), about 60% (experts); saccade 1.86 vs 3.12 deg; 14 novices, 6 experts | a10 Busjahn 2015 | C |
| Reading-order replication | 12 novices, 19 intermediates; correctness 86% vs 91% (p=0.072); code linearity affected nearly every measure; story-order difference not reproduced | a11 Peitek 2020 | C |
| Beacons help experts | behavioural, sizes unknown | a08 Wiedenbeck 1986 | S |
| Beacons and layout do not change brain activation | no difference among 4 conditions, N=11 | a15, b06 | C (low power) |
| Cue-based reading is cheaper than bottom-up | lower activation in all tested areas, N=11, FDR p<0.01 | a14, b05 | S (primed by training) |
| Classic complexity metrics predict comprehension weakly | McCabe about 0; LOC, Halstead, DepDegree small on time, medium on correctness (tau 0.1-0.5); N=19, 16 snippets, 72% solved | b08-b10 | S |
| Subjective complexity rating matches solved vs unsolved | beats metrics; given after solving | b10 | S |
| Displayed complexity anchors ratings, not accuracy | d=-1.29, p=.000132, N=43; no effect on correctness or time | b11 | S |
| Atoms of confusion raise errors | 2.7 to 56 times for 7 of 14 Java atoms; pooled OR 3.82 (CI 2.69-5.42); N=132; 10 of 14 judged more confusing | b12 | E (partial replication of a C study) |
| Experiment designs are not comparable | 95 studies; N 5-277, median 34; 53.7% students only; 67 of 95 test "X influences comprehension"; 23 factorial | b01-b04, a22 | E |
| Code review begins with context building | 23 of 25 reviews, 10 reviewers | a16 | S |
| People over-trust generated assertions | correct judged correct 73.9%, wrong judged wrong 49.0%, OR 2.94, N=86; similar confidence | c15 | S |
| Reading strategy when judging LLM output | think-aloud, 50 responses: 31 top-down, 7 bottom-up, 10 as-needed, 2 unclear; intuition 12/50, 7 of those wrong | c15, c25 | S |
| Students think they understand but do not | 19.3% believed they did, answered at most 1 question right | a21 | S |
| Beginners check LLM code poorly | 32 students, 160 tasks, 32.5% success | c14 | S |
| Copilot cuts time, not comprehension | 632 vs 1281 s (-50.7%); comprehension 7.86 vs 7.27 of 15, p=0.59; N=15 | c16 | S |
| Write-then-view predicts comprehension | 10.8 vs 2.3 transitions (4.7x, p=0.001); viewing Copilot output 8.2% vs 24.0% of time; n=8 vs 7 | c22 | S |
| LLM attention does not match human attention | at most 22% of methods significant; rho -0.128, p=0.386 vs summary quality; 27 programmers, 671 trials, 68 methods | a18, b18, c01 | E |
| Same, on task descriptions | Krippendorff alpha under 0.3 all models, GPT-4 lowest (F1 30.0, alpha 0.04); 57/211 wrong programs (27%) explained by patterns (CodeGen 31%, GPT-4 8%) | b19, c02, c20 | E |
| Open models answer sensemaking questions poorly | developers about 70%; CodeGen 39.3%, InCoder 37.7%, GPT-J 36.3%; model-human rho +0.22/+0.20/+0.04 vs human-human +0.56 | b17, c03, c21 | E |
| Human attention injected into training gives small gains | EyeLayer BLEU-4 +1 to +2 (13.36 to 15.12); EyeMulator all 36 cells positive; up to +7.16 CodeBLEU, one seed | a17, b20, c18 | S |
| GazeCopilot: live gaze-informed prompts help human readers of refactored code | gain 1.44 vs 0.56 standard (p=.0122); N=25 | b21 | S |
| LLM perplexity tracks human confusion on atoms | r=0.45; rho=0.47 on confusing code, 0.05 on clean; 24 EEG participants | c04 | S |
| Misleading names hurt LLMs | Pass@1 down 16.97-34.18% relative (LLaMA3-70B 62.20 to 40.94); GPT-3.5 document selection 92.84% to 52.39% | a19 | E (with a20) |
| Reasoning-tuned small models track human difficulty under obfuscation | rho 0.30-0.47 vs 0.02-0.10 for coder models; DS-R1-Qwen-7B 64% vs coder models 9-13% on output prediction | a20 | S |
| Chain-of-thought lifts code execution reasoning | CRUXEval GPT-4 output 63 to 81.9, input 67 to 74.8 | c07 | E |
| Reflective hypothesis loop (RHDA) | GPT-4o CRUXEval/LiveCodeBench: standard 68.75/41.18; CoT 89.12/83.14; RHDA 90.62/84.16; without amend 86.62/71.29 | c06 | E with c07; gain over CoT small |
| Models fragile to meaning-preserving edits | single mutation up to 7-8 points (open models); frontier loop unrolling -68.1 (GPT-5.2), -70.4 (Gemini-3) | c08, d02 | E |
| Right answer, flawed reasoning | open models 42-61% (Llama3.2 55.1-60.9%); GPT-5.2 and Gemini-3 0.2% | c08, d01 | E for open models |
| Equivalence checking is hard | EquiBench best 82.3% overall, 63.8% hardest; chance 50%; CoT barely helps | b22 | S |
| Real-code statement semantics weak | C single statements under 30%; input prediction about 12%; 3-shot lifts R1-Distill-14B 0.316 to 0.784 | b23, c09, c23 | S |
| Runtime reasoning self-inconsistent | REval accuracy 44.4%, incremental consistency 10.3 | d15 | S |
| Reasoning ability does not predict repair | no correlation in 10 LLMs, 4 benchmarks | d16 | S |
| Coarse-to-fine navigation helps | tree scaffold Function Acc@5 32.61 to 52.13; file-to-function gap 26.9 to 21.7; Agentless file-level 81.7% combined | c11, d11 | E |
| Fewer navigation tools better (7B, RL) | IoU 24.28 (jump only) vs 13.71 (four tools); RL 15.46 to 26.43 | c10, c24 | S |
| Localisation tracks resolve rate | 448 vs 342 files hit; rank by F1 matches rank by resolve rate | d14 | S |
| Hypothesis-first scientific debugging did not raise repair rate | Defects4J v1.2: 76 vs 87; v2.0: 113 vs 110; real debugger 73% vs 63% plausible when predicted | d09 | S (2023 models) |
| Explaining code line by line helps a little | +2-3% Spider, +9% hardest, up to +12% with tests; matches 10x sampling | d10 | S |
| Models miss errors in their own output | 64.5% blind spot (14 open models), Sonnet 4 41.4%; 4.3-10.8% of natural errors caught if external; "Wait" cuts 89.3% | d04, d05 | E with d06, d07, d08 |
| Separate verifier misses wrong answers | blind-spot 0.12 to 0.55 as student grows | d06 | S |
| Self-repair gain vanishes at equal budget | normalised pass rate about 0.92-1.06; human feedback 52.60% vs GPT-4 feedback 33.30% | d07 | E (with d08) |

## 4. Mechanisms and models

Written so an engineer can turn each into a step, a log field or a test.

### 4.1 Hypothesis-driven reading (Brooks)
State: a tree of hypotheses. Root: "this code does X for purpose P". Children: sub-purposes. Loop: pick an open hypothesis, predict what code shape would confirm it (the beacon), search the code for that shape, mark confirmed, refined or rejected. Done when every leaf links to code. Episode log: `{hyp_id, parent, claim, expected_beacon, found_line, verdict}`. Risk: the model invents a hypothesis and then reads to confirm it. Counter: require the beacon to be stated before the lookup, and a refutation attempt (G3). Evidence that this beats other orders: none for LLMs (d19). AutoSD, the nearest test, tied direct patching [d09].

### 4.2 Bottom-up chunking (Shneiderman-Mayer, Pennington)
Read statements, group them into a named chunk ("validates input"), group chunks into a larger one. Output: a summary tree with a one-line label per chunk. Program model comes from control flow; situation model from data flow and goals. Implementation: a chunk table `{lines, label, inputs, outputs}`. fMRI shows bottom-up costs more than cue-based reading but engages a semantic integration area (BA 39) [a14, b07]. Reverse inference from brain areas is weak.

### 4.3 Opportunistic switching (von Mayrhauser and Vans)
Three models (top-down, program, situation) and a knowledge base. Observed human switch rule: use top-down when the code is familiar; fall back to bottom-up when a hypothesis fails [a07, a09]. Implementation: start with cheap cues (signatures, docstring); on a failed prediction, log it and move to chunk-level reading of the failing region. This matches the schema rule "doubt only on a signal" (G1).

### 4.4 Letovsky episode labels
Labels: READ, ASK-WHY / ASK-HOW / ASK-WHAT (question), CONJECTURE (answer with a certainty grade), SIMULATE (run the code mentally), VERIFY (check against code or output). A dangling purpose is an open ASK-WHY with no answer. Logging: tag each agent turn with one label and keep a list of open dangling purposes. Close an item only by a VERIFY tied to real output (G2). No study has validated these labels on agent traces (K22; d19). Practical proxy: file-level and function-level localisation correctness, which tracks resolve rate across six SWE-bench agents [d14].

### 4.5 Situation model before fix
Burkhardt: the situation model (function, goals, data flow) is the stronger representation and improves after a real task [a13]. Mechanism: write "what is this function for, and what must be true of its inputs and outputs" before editing. Not tested for LLM fix accuracy.

### 4.6 Beacons and names
Names are cues. Humans: help experts [a08]; no beacon or layout effect at neural level (N=11) [a15]. LLMs: names carry weight both ways. Misleading names cut Pass@1 17-34% relative [a19]. Renaming helped weak models (+14 points) and hurt Gemini-3 (100 to 68.1) [d03]. Scaffold idea: derive behaviour from the body, compare with the behaviour implied by the name, flag a mismatch. Untested as a recovery method.

### 4.7 Navigation as coarse-to-fine search
Level 1 repository tree, 2 file, 3 class/function, 4 lines. Agentless fixes this order and beats skipping levels [d11]. RepoNav names the failure: agents reach the right file but pick the wrong function in 44-58% of function-level misses, anchoring on a salient symbol. A compact sibling-symbol tree reduces it [c11]. Fewer tools helped a 7B RL-trained agent [c10, c24]; no evidence this holds for frontier prompt-only agents.

### 4.8 Execution prediction and its checks
Trace-then-answer (CoT), hypothesise-test-amend (RHDA) and line-by-line explanation (rubber duck) all improve code reasoning for 2023-2025 models [c06, c07, d10]. Real execution beats predicted execution: 73% vs 63% plausible runs [d09]. Few-shot worked traces gave the biggest jump on CodeSense (0.316 to 0.784) [c23]. Implementation: where a sandbox exists, run; otherwise write a trace table `{line, variable values}` and compare with the claim.

### 4.9 Rewrite-consistency check
Ask the same question on the original and 1-2 meaning-preserving rewrites. Disagreement flags a fragile answer. Only a union upper bound was measured [d03]; no voting-verifier study. Frontier models lose up to 70 points under loop rewrites, so the rewrites may themselves be hard [d02]. Treat it as a test, not a design.

### 4.10 Verification of own claims
Models miss errors in their own output but catch the same error when it is attributed to someone else [d04]. Mechanism: strip authorship before review (matches G5). Humans show a similar pattern: 73.9% vs 49.0% [c15].

## 5. What holds up

### 5.1 Replications and failures
- Busjahn's novice/expert reading-order gap: partly reproduced in direction by Peitek (2020), but code linearity dominates and the story-order difference was not reproduced; Peachock found no experience effect [a10, a11]. Contested.
- Pennington's program-first order: not reproduced for OO code [a13].
- fMRI bottom-up study (Siegmund 2014): reproduced in the same brain areas (N=11) [a14, b05]. Beacon and layout effect: null [a15, b06]. The authors blame the design (too little demand after training).
- Atoms of confusion: partial replication in Java; 7 of 14 atoms raised errors; infix precedence and indentation did not [b12]. The abstract says 2.7-56 and the conclusion says 4.6-56 (paper inconsistency).
- Human-model attention alignment: Li found none that predicts quality; Paltenghi found weak positive agreement (CodeGen +0.22) with a special method. The gap is likely method (SHAP vs attention weights) [a18, c03].
- Attention-injection training: small gains in several papers, mostly single-seed [a17, b20, c18]. Yet alignment itself does not predict quality [a18], so alignment is probably not the mechanism.
- Hypothesis-first debugging: AutoSD tied direct patching [d09].
- Self-repair: gains vanish at equal budget [d07]; "Wait" fixes blind spots for non-reasoning models but reasoning models already have it [d05].

### 5.2 Meta-level
Wyrich's map (95 studies) is a mapping study without pooled effects. Measures (questions, recall, time, correctness) mostly do not correlate [a22, b01]. 71 of 94 experiments test one factor; only 23 of 95 are factorial, so moderators such as expertise are rarely estimated [b04]. Median N=34. No large preregistered replication of any classic result was found [b25]. All human effect sizes here are weak priors.

### 5.3 Moderators
- Code linearity and snippet content outweigh reader experience for eye movements [a11].
- Familiarity: cue-based fMRI gains came after training on near-identical snippets [a14].
- Task type: summarisation, debugging, sensemaking and code review differ; the 1995 review says most models do not cover partial understanding [a09].
- Model type: reasoning-tuned models track human difficulty; coder models do not [a20]. Open models show flawed-correct reasoning; frontier ones almost none (possible contamination) [d01].
- Model strength: the verifier blind spot grows with student strength [d06]; the "Wait" gain vanishes for reasoning models [d05].
- Code size: all LLM localisation studies stay at SWE-bench scale [d11, d12].

### 5.4 Interventions
Worked: CoT and hypothesis loops (large for GPT-4 era) [c06, c07]; few-shot worked traces [c23]; coarse-to-fine navigation and sibling-symbol tree [c11, d11]; real execution [d09]; rubber-duck explanation (small) [d10]; gaze-informed prompts for human readers [b21]; external attribution of errors [d04].
Did not work or weak: hypothesis-first scaffold for repair accuracy [d09]; prompt and fine-tune fixes for name over-reliance (effect persists) [a19]; role prompts for student readers [a21]; CoT on weaker models' input prediction and on equivalence checking [c07, b22]; API definitions in context (Phi-4 -0.036) [c23]; more tools [c24]; self-correction without feedback [d08]; Copilot for comprehension [c16].

## 6. Language models

Reading and attention. Models do not look where humans look [a18, b19]. At most 22% of methods show any significant correlation, and alignment does not predict summary quality. Open models answered sensemaking questions at 36-39% vs developers about 70% [c21]; these are 2022 models.

Names. Misleading names cut completion by 17-34% relative and document selection from 92.84% to 52.39% (GPT-3.5) [a19]. Anonymous names cost less (81.35%). Type inference, recoverable locally, is less affected. Prompt and fine-tune fixes did not remove it. Renaming cut both ways [d03].

Execution reasoning. CRUXEval GPT-4: 63 to 81.9 (output) with CoT [c07]. RHDA with GPT-4o: 41.18 to 84.16 on LiveCodeBench [c06], but plain CoT already gave 83.14, so the loop adds about 1 point on top of CoT and the "up to 3x" claim is mostly CoT. Real-code statements are far harder: CodeSense under 30% on single C statements for Claude 3.5 and GPT-4o-mini; input prediction about 12% [c09]. Few-shot worked traces gave the biggest change (0.316 to 0.784), more than CoT or API docs [c23]. Equivalence: best 82.3%, hardest category 63.8% vs 50% chance; CoT and few-shot barely help [b22]. REval: 44.4% accuracy, consistency 10.3 [d15].

Fragility. Single meaning-preserving edits cost up to 7-8 points for open models [c08]. Frontier models (GPT-5.2, Gemini-3) score 97.5-100% at baseline but fall 28-70 points under loop unrolling, loop conversion or if-else swap [d02]; part may be length or contamination. Flawed-but-correct share: open models 42-61%, frontier 0.2% [d01, c08].

Reasoning vs repair. Code-reasoning ability is not correlated with bug-repair success in 10 LLMs [d16].

Navigation and localisation. Agentless: 32.00% on SWE-bench Lite at $0.70, file-level 81.7%; skipping the hierarchy was worse [d11]. RepoNav: tree scaffold 52.13 vs file-only 32.61 Function Acc@5; the file-to-function gap is the main loss [c11]. LocAgent reports up to 92.7% file accuracy (abstract only) [d12]. RepoNavigator: one jump tool beat four for a 7B RL model; Qwen 32B 25.16 to 32.30 with RL [c10]. Across six agents, localisation tracks resolve rate [d14].

Self-checking. Blind spot on own output: 64.5% average (open models), 41.4% (Sonnet 4) [d04]. A cheap "Wait" cuts it 89.3% for non-reasoning models, so current reasoning models already capture it [d05]. Verifier models miss 12-55% of wrong answers [d06]. Self-repair is no better than resampling at equal budget [d07]. Mostly math and QA, with code in d07.

Human-facing effects. Copilot: time -50.7%, comprehension flat [c16]. Beginners accept LLM code: 32.5% success checking [c14]. Programmers detect wrong LLM assertions at 49.0% [c15]. Tutoring tool explanations are often partly wrong: 90% complete but 67.2% correct in one study [c17].

What changed results, and by how much. Execution feedback is the biggest lever (73% vs 63% [d09]; human feedback 52.60% vs model feedback 33.30% [d07]). Worked traces next (0.316 to 0.784). CoT is large for older models. Scaffolded hierarchies add 10 to 20 points of Acc@5. Model strength removes name and blind-spot effects, except under structural rewrites.

Gaps. LLM studies use at most 8B models, GPT-4-era models, or frontier models only for rewrite tests. No study tests a scaffolded frontier agent with a reading strategy at equal tokens.

## 7. What our agent should take

Format: item | schema part | status | evidence ids. Schema parts: G = guardrail, S = state, O = operator, memory/logs.

### Add now (established)

1. **Verify through real output, not through own re-read; strip authorship before any review.** The own-output blind spot is large and self-repair gains vanish at equal budget. Schema: G2, G5, verify state. [E] d04, d05, d06, d07, d08, c15.
2. **Coarse-to-fine navigation (tree, file, function, lines), no skipped levels; show sibling symbols at the function step.** Schema: S localise, O3 decompose. [E] c11, d11, d14. Fewer-tools claim is [S] (c10, c24).
3. **Treat names and comments as cues, not facts; check behaviour against the body.** Schema: G5 / G10. [E] a19, a20, d03. The recovery step itself is a test (U1).
4. **CoT or a short trace for execution questions; real execution when a sandbox exists; worked trace examples for statement-level semantics.** Schema: G2, O-trace. [E] c06, c07, c23, d09.
5. **Do not use model attention or human gaze as a design signal; judge steps by outcomes only.** Schema: guard note. [E] a18, b17, b19.
6. **Do not route effort by McCabe-style metrics.** Schema: S0 gate (not-to-add). [S] b08, b10; cheap to follow.
7. **Treat human effect sizes in this field as weak priors; every element must win at equal tokens (G7).** [E] b01-b04, a22.
8. **Log localisation correctness (file, function) per run.** Schema: logs. [S] d14.

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Hypothesis-first reading vs read-first vs bottom-up | localise / hypothesise states, G1 | [C] | a01, a09, a10, a11, d09 |
| Purpose statement (situation model) before fix | memory / frame state | [S] | a13, K02 |
| Write-then-view: predict before reading output | G3, O5 | [S] | c16, c22, d10 |
| Name-blind restatement recovery | G5 / O6 | [S] | a19, d03 |
| Rewrite-consistency check as verifier | verify state | [S] | d02, d03, d15 |
| Context-build step before inspection | frame state | [S] | a16, c15 |
| Atom-aware evaluation-order trace | G6-type check | [E] human error, [S] agent | b12, c04 |
| Episode labels from traces (Letovsky) | logs | [S] | a06, d14 |
| Fewer tools beyond 7B | O3, localise | [S] | c10, c24 |
| Forced refutation attempt on own claim | G3, G4 | [S] | c15, c25, d04 |

## 8. Concrete tests on our bench

All arms get the same total token budget (setup cost counted, G7). Use items with ground truth: SWE-bench Verified subset for localisation, CRUXEval/LiveCodeBench for execution, our own injected-bug localisation items. At least 100 items per arm and 3 seeds. Report paired differences with intervals.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Hypothesis-first vs read-first | Bug localisation, 100 items, medium repos | A: write 3 hypotheses with expected beacons, then read; B: read files, then answer; C: bottom-up chunk summary, then answer | Top-1 and top-3 file/function hit | A within +-3 points of B (AutoSD tie); gain only on large repos |
| T2 Name-blind restatement | Same items, 30% misleading names, 30% neutral | A: plain; B: restate behaviour from body only, then compare with the name | Accuracy on misleading-name items; loss on original-name items | B recovers at least half of the 17-34% relative loss; costs under 3 points on original names |
| T3 Coarse-to-fine vs free search | Repos larger than SWE-bench | A: tree, file, function scaffold; B: free search | Function Acc@5; tokens | A +5 to +15 points (c11); smaller with a frontier model |
| T4 Purpose statement first | Bug-fix items | A: purpose statement before fix; B: none | Fix pass rate | Small positive (+2 to +4) |
| T5 Predict-then-view | Execution or review items | A: write predicted output or behaviour before running or reading; B: run first | Final accuracy | Positive where tools exist; none otherwise |
| T6 Rewrite-consistency | CRUXEval plus rewrites | A: single run; B: original plus 2 rewrites, accept on agreement; C: 3 samples, vote | Precision of accepted answers; false-accept rate; cost | B beats A on precision; B vs C shows whether rewrites add anything beyond sampling (G4) |
| T7 Own vs other attribution | Patches, half wrong | A: self-review; B: same patch labelled as another's; C: no label | False-accept rate on wrong patches | B or C lower than A (d04); smaller gap for reasoning models |
| T8 Atoms trace | Atom-bearing snippet pairs | A: plain; B: explicit evaluation-order trace for flagged atoms | Error rate on atom items | Lower error on atoms; no change on clean |
| T9 Episode labels | 50 hand-labelled agent traces | Two raters, 5 labels | Cohen kappa; correlation of label counts with success | kappa at least 0.6; label counts predict success |
| T10 Context-build step | Review or localisation items | A: description and signatures first; B: inspection first | Hit rate | Small positive for localisation |

Log in every run: label per turn, number of open dangling purposes, localisation hit, tokens, whether each verification used real output.

## 9. What does not transfer, and why

- Eye movements and linearity (Busjahn): LLMs have no gaze or page reading order; token attention is not human attention [a18]. Only the idea (order of cues) transfers.
- fMRI efficiency findings (N=11): no mapping from brain area to model step; reverse inference is weak [b07].
- Working-memory limits behind chunking: a model has a context window, not a human span. Chunking helps only as compression and labelling.
- Student-only samples and short snippets: 53.7% students only; median snippet pool 9 [b01]. Agent tasks are repo-scale.
- Human over-trust of generated code (49% detection): caused by automation bias and reading time. The model analogue (blind spot on own output) is real but a different mechanism, and measured mostly in math [d04].
- Anchoring on shown complexity (d=-1.29): moves ratings, not accuracy [b11]; no analogue for an agent without a rating display.
- Attention-injection training (EyeLayer, EyeMulator): needs training; the schema is a no-training scaffold [a17, c18].
- Brooks' domain knowledge: humans bring years of it; a model's hypotheses can be fluent and wrong. A hypothesis list is cheap and is not evidence (G10).
- Complexity metrics (McCabe): weak even for humans [b08]; the agent's cost driver is length and tool calls.
- Tutoring-tool accuracy (95%): different task, human graders [c17].

## 10. Open questions

1. Does a hypothesis-first prompt beat bottom-up or linear reading for a frontier agent on bug localisation at equal tokens? No test found (d19, K18).
2. Is the RHDA/CoT gain still present for frontier reasoning models, or absorbed by built-in reasoning?
3. Which Letovsky labels can be logged reliably from agent traces, and do they predict success?
4. Can name-blind restatement remove the lexical-superstition loss without removing useful name information?
5. Does consistency across rewrites work as a verifier (precision, cost)?
6. Does write-then-view help models as it separates high from low comprehension in people (4.7x, n=15, associative)?
7. Do coarse-to-fine gains persist on repos larger than SWE-bench and with strong models? Do fewer tools generalise beyond 7B?
8. What are the exact figures in Soloway and Ehrlich (1984) and Pennington (1987)? Primary papers not opened.
9. What do the ICSE 2025 student-attention papers report beyond the snippet (n=27)?
10. Is the 49% human detection of wrong assertions mirrored by LLM false-accept on its own code?
11. Why do frontier models fall 28-70 points under loop rewrites: semantics, length or contamination?
12. Is there any large preregistered replication of Brooks or Pennington? None found.

## 11. Sources

[V] = opened by an earlier agent (page or PDF text); [M] = snippet or citation only.

Classic and review
- [V] von Mayrhauser and Vans (1995), source of a01, a04-a06, a09 (read via this review). https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/von_mayrhauser-1995.pdf
- [V] Wyrich (2023) Source code comprehension: a contemporary definition. https://arxiv.org/pdf/2310.11301
- [M] Brooks (1983) original. https://doi.org/10.1016/S0020-7373(83)80031-5
- [M] Wiedenbeck (1986) original. https://doi.org/10.1016/S0020-7373(86)80083-9
- [M] Soloway and Ehrlich (1984). https://doi.org/10.1109/TSE.1984.5010283
- [M] Pennington (1987). https://doi.org/10.1016/0010-0285(87)90007-2
- [M] Siegmund et al. (2014) fMRI. https://doi.org/10.1145/2568225.2568252
- [V] Maletic slides on mental models (low authority). https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/MentalModels-ProgUnder.pdf

Human studies
- [V] Busjahn et al. (2015). https://huang.isis.vanderbilt.edu/cs8395-f23/paper/linear-order-eye.pdf
- [V] Peitek, Siegmund, Apel (2020). https://www.se.cs.uni-saarland.de/publications/docs/PSA20.pdf
- [V] Burkhardt, Detienne, Wiedenbeck (1997). https://arxiv.org/pdf/cs/0612018
- [V] Siegmund et al. (2017). https://www.se.cs.uni-saarland.de/publications/docs/SPP+17.pdf
- [V] Peitek et al. (2018). https://web.eecs.umich.edu/~weimerw/2018-481/readings/neural-efficiency.pdf
- [V] Peitek et al. (2021) ICSE. https://www.tu-chemnitz.de/informatik/ST/publications/papers/ICSE21.pdf
- [V] Wyrich, Bogner, Wagner (2024). https://arxiv.org/abs/2206.11102
- [V] Wyrich et al. (2021) anchoring. https://arxiv.org/abs/2012.09590
- [V] Langhout and Aniche (2021). https://arxiv.org/abs/2103.05424
- [V] Noone and Mooney (2018). https://mural.maynoothuniversity.ie/id/eprint/12078/1/BeaconsInProgramming.pdf
- [V] Goncalves et al. (2025) code review. https://arxiv.org/pdf/2503.21455
- [V] Schroeder and Koschke (2024), partial read. https://arxiv.org/pdf/2403.08480
- [M] Kevic et al. (2015). https://people.cs.gmu.edu/~tlatoza/teaching/cs691f25/lecture7.pdf
- [M] ICSE 2025 journal-first, A tale of two comprehensions. https://conf.researchr.org/details/icse-2025/icse-2025-journal-first-papers/4/A-Tale-of-Two-Comprehensions-Analyzing-Student-Programmer-Attention-During-Code-Summ

Human-AI
- [V] Zi et al. (2025), abstract. https://arxiv.org/abs/2504.19037
- [V] Kaufman et al. (2026). https://arxiv.org/abs/2607.08885
- [V] Copilot brownfield study (2025). https://arxiv.org/abs/2511.02922
- [V] Qiao et al. (2025) review. https://arxiv.org/abs/2510.17894
- [V] Rong et al. (2026). https://arxiv.org/pdf/2609.26101
- [V] GazeCopilot (2025). https://arxiv.org/abs/2511.08177

LLM studies
- [V] Li et al. (2024). https://arxiv.org/abs/2402.14182
- [V] Paltenghi et al. (2022/2024). https://arxiv.org/abs/2210.05506
- [V] Kou et al. (2024). https://arxiv.org/abs/2306.01220
- [V] EyeLayer (2026). https://arxiv.org/pdf/2602.22368
- [V] Zhang et al. (2025). https://arxiv.org/abs/2503.14936
- [V] EyeMulator (2026), abstract. https://arxiv.org/abs/2508.16771
- [V] EEG confusion study (2025). https://arxiv.org/abs/2508.18547
- [V] Centaur comprehension (2026), abstract only. https://arxiv.org/abs/2607.11372
- [V] Shen et al. (2026) lexical superstition. https://arxiv.org/pdf/2609.26388
- [V] Le et al. (2026) obfuscation. https://arxiv.org/pdf/2606.31725
- [V] Zhao et al. (2025) RHDA. https://arxiv.org/abs/2502.13170
- [V] Gu et al. (2024) CRUXEval. https://arxiv.org/abs/2401.03065
- [V] Orvalho and Kwiatkowska (2026). https://arxiv.org/abs/2505.10443
- [V] Wei et al. (2025) EquiBench. https://arxiv.org/abs/2502.12466
- [V] Roy et al. (2026) CodeSense. https://arxiv.org/abs/2506.00750
- [V] CodeMMLU (2025). https://arxiv.org/abs/2410.01999
- [V] RepoNavigator (2025). https://arxiv.org/abs/2512.20957
- [V] RepoNav, Chai et al. (2026). https://arxiv.org/abs/2609.08355
- [V] Xia et al. (2024) Agentless (abstract in c12; hierarchy details in d11). https://arxiv.org/abs/2407.01489
- [V] Jimenez et al. (2024) SWE-bench, abstract. https://arxiv.org/abs/2310.06770
- [V] Chen et al. (2025) LocAgent, abstract. https://arxiv.org/abs/2503.09089
- [V] Yang et al. (2024) SWE-agent, abstract. https://arxiv.org/abs/2405.15793
- [V] Ma et al. (2024) bug-fixing agents. https://arxiv.org/abs/2411.10213
- [V] Liu et al. (2024) REval, abstract. https://arxiv.org/abs/2403.16437
- [V] Majumdar et al. (2024) CodeMind, abstract. https://arxiv.org/abs/2402.09664
- [V] Kang et al. (2023) AutoSD. https://arxiv.org/abs/2304.02195
- [V] Chen et al. (2024) Self-Debug. https://arxiv.org/abs/2304.05128
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778
- [V] Rajput et al. (2026) cheap verifiers. https://arxiv.org/abs/2609.01345
- [V] Olausson et al. (2024) self-repair. https://arxiv.org/abs/2306.09896
- [V] Huang et al. (2024) self-correct, abstract. https://arxiv.org/abs/2310.01798

Note: several 2026 LLM papers have unconfirmed authors (c04, c05, c08, c10, c16, c18). Preprints are not peer reviewed. Detailed numbers of a19, a20 and the 2026 preprints d-series were not re-checked by the critique pass.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 9 established claims: 6 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E09.05-K02** (number corrected). Means (situation 4.36 vs program 3.55, experts 4.56 vs novices 4.10) are right, but Burkhardt et al. report 51 subjects (30 experts, 21 novices), not 'about 46' (that was inferred from F degrees of freedom); the Pennington source is a secondary review, so the claim rests on one primary study (an OO-code study). Corrected claim: Experts build richer situation (domain) models than novices (4.56 vs 4.10 of 6); in an object-oriented program-comprehension study of 51 programmers (30 experts, 21 novices), situation-model questions were answered better than program-model questions by everyone (4.36 vs 3.55 of 6).
- **E09.05-K15** (number corrected). Langhout and Aniche numbers check out (7 of 14 atoms, 2.7 to 56 times, 132 students, pooled OR 3.82), but the EEG study's perplexity-to-EEG correlation is Spearman rho = 0.47 for confusing snippets (r=0.45 is a perplexity effect size, and clean snippets showed rho = 0.05); also 'LLM perplexity tracks human confusion' holds for confusing code only. Corrected claim: Atoms of confusion (precedence, side-effect patterns) raised human error 2.7 to 56 times for 7 of 14 Java atoms (N=132 students, pooled OR 3.82); an EEG study found LLM perplexity correlates with human confusion responses on confusing code (Spearman rho = 0.47) but not on clean code (rho = 0.05).
- **E09.05-K19** (reworded: the sources support less). Tsui (64.5%, Sonnet 4 41.4%, Wait -89.3%) and Olausson/Huang are fine, but Rajput et al.'s 0.12-0.55 blind spot is for a fixed cheap verifier (gpt-4o-mini) checking students from 0.5B up to 14-32B, rising with student size, not a verifier 'of similar strength'. Corrected claim: Models are poor at catching errors in their own output: 14 open non-reasoning models show a 64.5% blind spot (Claude Sonnet 4 41.4%) on injected errors; self-repair on code rarely beats resampling at equal budget; a fixed cheap verifier (gpt-4o-mini) waves through 12% to 55% of wrong answers from students of growing size (0.5B up to 14-32B). A cheap 'Wait' trigger removes about 89% of the blind spot for non-reasoning models.
- **E09.05-K10** (now single-source: only one opened source, code check).
- **E09.05-K14** (now single-source: only one opened source, code check).
