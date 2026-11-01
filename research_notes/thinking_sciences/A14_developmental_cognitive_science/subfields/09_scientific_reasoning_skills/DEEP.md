# Scientific reasoning skills: deep document

*Subfield A14.09. Controlling variables, coordinating theory and evidence. Key works: Kuhn, Klahr. Built from evidence_a-d.jsonl (a01-a28, b01-b25, c01-c31, d01-d20), claims.jsonl (K01-K29) and critique.md in this folder. Evidence ids are cited in brackets. Schema parts refer to `research_notes/single_agent/SCHEMA.md` v0.2. The founding studies could be read only at abstract level, so this document says plainly where numbers are missing.*

## 1. What it is

Scientific reasoning, in the developmental tradition, is the set of skills used to find out how a system works by testing it. Two skills dominate this subfield.

1. **Control of variables strategy (CVS).** To learn whether variable X matters, build a test where X differs and everything else is held the same. Chen and Klahr (1999) define a comparison as confounded when the variable of interest and at least one other vary together, so no single effect can be separated [b12]. CVS has two halves: vary the focal variable, and hold the others constant [K25].
2. **Coordinating theory and evidence** (Kuhn). A reasoner holds a theory, collects evidence, and must decide what the evidence says about the theory. It includes keeping or dropping a hypothesis, avoiding changing several variables at once, and not reading confirmation into ambiguous data [a20, d09].

Related pieces: knowing that evidence can be indeterminate, spotting confounds, choosing the next test, and drawing a valid inference from the result. These are separate skills that can come apart [K07].

**Why it matters for our agent.** Schema state S4 (TEST) runs checks. The research question is whether a rule such as "change one thing per test" belongs in S4, and when it hurts. The short answer from this folder: it is a good default when many causes are plausible or interactions are possible, and a bad rule when few causes are expected, because grouped tests then win [K02]. The strongest LLM-specific finding is different and more useful: models pick confirming tests and do not seek falsifying ones [K10, K12].

**Scope notes.** Parallel subfields cover counterexample finding, hypothesis testing in other settings, and LLM forecasting. This document only links to them. Its new content is the CVS literature, the Bramley sparsity result, the instruction debate, and the 2022-2026 LLM studies that test experiment choice.

## 2. History and theories in depth

**Piaget and Inhelder (1958).** Isolating variables was treated as a hallmark of formal operations, appearing in adolescence. Cited only second-hand here [a21].

**Tschirgi (1980).** Whether a test is judged good depends on whether its outcome is wanted. People accept a confounded test more readily when the result suits them. Second-hand only [a21, b16].

**Klahr and Dunbar (1988): dual space search.** Scientific discovery is search in two spaces, hypotheses and experiments, plus evidence evaluation. Adults on a toy robot (BigTrak) split into theorists, who changed hypotheses often, and experimenters, who changed experiments [a16]. This is the ancestor of the agent loop "propose, test, update". Not opened; no figures recorded. Klahr, Fay and Dunbar (1993) found children had more trouble than adults designing tests of a hypothesis and generating alternative hypotheses [a17, not opened].

**Kuhn, Garcia-Mila, Zohar and Andersen (1995): microgenetic study.** Multi-week study of multivariable causal systems. 17 community-college students (ages 22-47) and 15 fourth graders. Strategies were mixed within a person and over time. People kept theory-driven, confirming strategies and changed several variables at once; improvement was slow. A published commentary argued that the stage story was partly produced by the experimenter's questions [d09, a20]. No percentages were read from any abstract [K28].

**Chen and Klahr (1999): the canonical CVS study.** N=87 children, ages 7-10. Explicit training inside a domain plus probe questions taught CVS. Probe questions alone, with no instruction, did not help. Age improved transfer to remote tasks [d01]. Per-condition percentages were not read.

**Klahr and Nigam (2004): direct instruction vs discovery.** N=112 third and fourth graders. Many more learned CVS under direct instruction than under discovery. The few discovery learners who did learn did as well later on a broader task (judging science-fair posters) as the many direct-instruction learners. This is the "equivalence of learning paths" claim [d02]. The widely quoted 77% vs 23% mastery is NOT verified. No open copy was found; the figure stays "from memory" [a19, critique row 9].

**Klahr and Chen (2003).** Four- and five-year-olds treat one positive instance as proof even when another source is unexplored (the "positive-capture" strategy). A few training sessions replaced it with the correct strategy [d10]. Sample size not read.

**Kuhn and Dean (2005).** Low-achieving urban sixth graders, told only to focus on one factor, used controlled comparison significantly more [d08]. The one-line instruction is the mechanical form of S4 [K24].

**Dean and Kuhn (2007).** An independent lab, same age, longer follow-up. Three groups of 15 fourth graders. Group 1: 12 sessions over 10 weeks. Group 2: one direct-instruction session plus the 12 sessions. Group 3: the single session only. Direct instruction was neither necessary nor sufficient for robust lasting skill; skill built up gradually over practice [d04].

**Bramley, Jones, Gureckis and Ruggeri (2022), built on Coenen et al. (2019).** The modern reinterpretation. Children's failure to control variables may be adaptive: the best test depends on how many causes are expected. Section 3 gives the numbers [a01-a03, a15, d11].

**Two competing readings.**
- *Deficit view (Piaget, Kuhn, Klahr):* children and many adults lack CVS and must be taught it.
- *Adaptive view (Bramley):* children choose tests to fit the causal structure and can run controlled tests when they suit the situation. Failures on classic tasks may be a mismatch between task and the strategy that is best in typical life.

The evidence supports a blend. Children do change several variables at once in knowledge-lean tasks and CVS is teachable (g=0.61), but the sparse/dense result shows that "grouped" is sometimes rational.

## 3. Core findings with exact numbers

Status key: established = two or more independent sources; single = one source; contested = sources disagree; unverified = not read.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| First test in a switch box: share of single-switch tests | 7-9 sparse 15/24 (62.5%); 7-9 dense 23/29 (79.3%); 10-13 sparse 11/28 (39.3%); 10-13 dense 14/23 (60.9%). Age OR 2.24 (CI 1.05-4.9, BF 3.44); condition OR 0.47 (BF 2.34); interaction BF 0.57. N=104 | Bramley 2022 [a02] | established (K01) |
| Same data, multi-switch first test | 37.5% younger sparse; 20.7% younger dense; 60.7% older sparse; 39.1% older dense | Bramley 2022 [d11] | established |
| Best play depends on sparsity | Expected return about 1.90 for split-half in the sparse case vs about 1.25 for one-at-a-time in the dense case. Adults differ between conditions by 66 points; children were powered for 40 | Bramley 2022, Coenen 2019 [a01, a15, d20] | established (K02) |
| Only older children turn multi-switch tests into correct answers | Over trials with 4+ switches live: correct guess among multi-test users older 17/19 (89%) vs younger 3/7 (43%), Fisher p=.003. N=92 with full records | Bramley 2022 [a03] | established (K07) |
| Early precursors predict later CVS | Indeterminacy of evidence and confounding together explain 39% of later CVS. N=170, ages 9 and two years on | Peteranderl and Edelsbrunner 2020 [a04] | established (K06) |
| Choice of controlled test in preschool | 3-6 yrs, N=57: controlled choice 66% (2 variables), 43% (3 variables). Said "cannot know" on 39% of confounded trials; justified robustly on 22%. Recognition and choice unrelated | Moeller, Sodian, Sobel 2022 [a07, d12] | established |
| Fourth to sixth grade justification | More than 50% of fourth graders, about 80% of fifth, almost all sixth justified choices by control of variables | Bullock and Ziegler (1999) via Peteranderl [a05] | single, second-hand |
| CVS is teachable | 72 intervention studies, mean g=0.61 | Schwichow et al. 2016 via Peteranderl [a06] | established (second-hand, K03) |
| Explain plus design beats either alone | Binary-choice test: instruction plus ramps design 72%, instruction only 65%, ramps only 57%. High vs low schools 82% vs 63% in the best condition. About 3000 fourth graders, 96 classrooms | Freer et al. 2011 [a10] | single |
| Confounded examples beat clean-only | High-achieving schools 84% vs 73%; low-achieving 69% vs 56% (immediate). 4 variables 63% vs 2 variables 53% | Freer et al. 2011 [a11] | single (K04) |
| Far-transfer scaffold | Ramps mastery 88% vs 83% (N=33). Delayed pretest-posttest correlation r=+.22 (added questions) vs +.67 and +.79 (baselines) | Siler et al. 2011 [a12] | single (K20) |
| Physical = virtual materials | Grades 4-5 N=92: about 20% pretest to about 60% posttest, no physical/virtual difference | Triona and Klahr 2007 [a13] | established |
| Direct instruction vs discovery | N=112 (Klahr and Nigam); N=72, grades 3-5, with transfer at 1 week, 3 months, 3 years (Strand-Cary and Klahr); n=797 to 848 in 36 to 39 classrooms: lecture plus experiments > lecture > experiments, held at 5 months (Lorch 2010) | [d02, d03, d05] | contested (K05); 77% vs 23% unverified |
| Instruction not necessary or sufficient long run | Three groups of 15 fourth graders, 12 sessions over 10 weeks | Dean and Kuhn 2007 [d04] | single |
| Self-generation no better than reading | Reading M=4.06 (SD 1.31) vs generation M=3.41 (SD 1.62), t(125.58)=2.58, p=.011, d=0.44 at first test; condition F(1,107)=4.32, p=.040; gap gone within a week | Kaiser et al. 2018 [b06] | single |
| Two halves of CVS trained differently | Lecture improves holding variables constant; hands-on improves varying the focal variable. 800+ children. Planning and spotting confounds respond to training; identifying and interpreting controlled tests develop without it (N=618) | Lorch 2010; ERIC EJ1039461 [d05, d07] | established (K25) |
| Invalid-design examples help far transfer | n=1,069 in 60 classrooms (Lorch 2014); high guidance beat low guidance, N=57 (Matlen and Klahr 2013); invent-then-tell tied tell-then-practice, N=101 | [d06] | single (K26) |
| Segmenting the task equals instruction | Direct instruction n=22, task structuring n=23, control n=22; structuring equal to instruction, both beat unguided | EJ1039461 [d07] | single (K24) |
| Inquiry gain is uneven | N=138 fifth graders, 5 weeks. CVS gained; hypothesis-evidence coordination and conclusions did not significantly. Progress between lessons 1 and 3, not 3 and 5. Reading and maths predicted CVS gain (0.253, 0.202, both p<.001) | Schlatter et al. 2020 [b07, a09] | single (K08) |
| Theory of mind predicts later reasoning | Waves at 4, 5.5, 7.5 years; holds with executive function and language controlled | Sobel et al. 2026 [a08, b09] | single (one paper, counted once) |
| Vary-one-thing users solve best | MicroDYN, n=4,371, grades 3-12: conscious VOTAT > non-conscious VOTAT > non-VOTAT | Molnar and Csapo 2018 [b15] | single (K09) |
| Correlation read as causation | 66% found a correlational study convincing; 63% endorsed a decision on it; 97 of 240 completed | Seifert et al. 2022 [b13] | single (K21) |
| LLM confirmation bias in rule discovery | 12 LLMs, 100 games, 20 turns. Success: GPT-5.2-Chat 75%, GPT-OSS-120B 68%, DeepSeek-V3.1 41%, most others 33-35%, Qwen3.5-9B 21%, GPT-5-Nano 12%. Positive-test share 24-39% for reasoning models vs 66-82% for instruction-tuned. rho with success -0.779 (p=0.003); rho(bias, falsification) -0.937 | Bertolazzi et al. 2026 [c01-c03] | established (K10, K12) |
| Opposites prompt | 11 LLMs, 45 turns, success 6% to 78%. Mean 42% to 56% with Think-in-Opposites | Jhaveri et al. 2026 [a22] | single (K11) |
| Prompt effect by model type | Non-thinking, baseline / opposites / dual-goal: Qwen3-8B 0.06/0.06/0.08; 14B 0.23/0.29/0.13; 32B 0.33/0.36/0.10; Llama-3.3-70B 0.21/0.38/0.20. Thinking: Qwen3-32B 0.41 to 0.60, 14B 0.34 to 0.58, at about 40% more tokens per turn | Jhaveri et al. [a23, d15] | single (K11, K29) |
| Disjunctive bias in LLM Blicket play | One object per step: OR rules solved, AND rules failed, worse at 8 objects than 4; information-gain oracle 1.0 on both; sampling 16 to 96 hypotheses removed the gap | GX-Chen et al. 2025 [d13] | single (K22) |
| Active choice beats proposing blind | 306 adults. Conjunctive object identification: active 0.69, passive observer 0.45, passive proposer 0.12. Rule choice 0.82, 0.69, 0.57. Tests: 9.6 conjunctive vs 6.4 disjunctive | Samiei et al. 2026 [a24, d14] | single (K13, K23) |
| LLM experiment choice | Zendo-style game out of 8: ReAct agent 4.60, humans 5.26, fuzzy-rule model 5.35, information-gain scaffold 6.55 | Piriyakulkij et al. 2024 [d17] | single (K27) |
| Hypothesis step in an agent | DiscoveryWorld easy knowledge 0.34 (Hypothesizer) vs 0.25 (ReAct) vs 0.11 (Plan+Execute); challenge completion 0.08 vs 0.18 | Jansen et al. 2024 [c10] | single (K15) |
| End-to-end discovery is weak | DiscoveryWorld completion 0.38 easy to 0.08-0.18 challenge vs humans 0.66; ScienceWorld best 0.17; MLAgentBench 37.5%; ScienceAgentBench 32.4% (34.3% with expert knowledge; o1 variants up to 42.2%) | [b17, b18, b23, b24, c07] | established (K14) |
| More variables break agents | Proteomics: ReAct 0.00 on 2 and 5 variables; Plan+Execute 0.00 on 5 (5 seeds) | Jansen 2024 [b20] | single (K16) |
| Requirement-analysis step | Precision 94% vs 65% without; recall 64% vs 69%; expert correctness 4.1 vs 3.4 without and under 3.0 for LLM-only. One pharma simulator | Xia et al. 2026 [c11-c14] | single (K18) |
| No LLM study on developmental CVS items | Searches of ERIC, Europe PMC, PubMed, citation lists: zero for LLM plus CVS, zero for LLM plus MicroDYN | [a28, d19] | established as absence (K19), search partly rate-limited |

## 4. Mechanisms and models

Each is written so an engineer can implement it.

### 4.1 Confound detector (the CVS check)

Input: a pair of test setups A and B, each a dict of variable to value. Output: the set of variables that differ.
- Let D = set of variables with different values.
- If |D| = 1: the pair is controlled for that variable. Any outcome difference can be credited to it.
- If |D| >= 2: the pair is confounded. The outcome difference cannot be assigned to one variable. Log "inconclusive for each variable in D".
- If |D| = 0: nothing was varied. No information.

This is Chen and Klahr's definition [b12] turned into code. It is the two halves of CVS [K25]: the focal variable is in D, and D has no other member. The program does it, not the model. This keeps the schema rule that code decides (section 1 of the schema).

### 4.2 Sparsity-aware test chooser (Coenen and Bramley model)

State: a set of candidate causes C, a prior expected number of true causes k (from the task or learned).
- Dense (k large, most candidates matter): test one candidate at a time, vary it, hold the rest. Binary case: leave the others off.
- Sparse (k small, say 1 of n): test about half of the remaining candidates at once. If the outcome is "no effect", the whole half is cleared. If "effect", the cause is in the half; split again. This is binary search.
- Rule of thumb from the model: with one cause and equal priors, split-half is far better. Expected return in the 6-switch task about 1.90 vs 1.25 [a01, a15].
- Note the dual form: in the dense case (one switch broken among many working), one-at-a-time is the only good play [a01].

Implementation: choose the test that maximises expected information gain over the current hypothesis set. For binary single-cause worlds this reduces to split-half. For dense worlds it reduces to one-at-a-time. An EIG scorer therefore covers both cases and removes the need to hard-code the rule [d17, K27].

### 4.3 Expected information gain (EIG) test scoring

For each candidate test t and hypothesis set H with weights w:
1. Predict the outcome of t under each h in H.
2. Group hypotheses by predicted outcome.
3. EIG(t) = entropy(w) - sum over outcomes of P(outcome) * entropy(w within group).
4. Run the t with highest EIG. Update w from the real outcome (code, not the model).

Piriyakulkij et al. used an LLM to propose hypotheses and Monte Carlo belief updating to pick tests. Result: 6.55 of 8 vs 4.60 for a plain ReAct agent and 5.26 for humans [d17]. The LLM does what it is good at (propose and revise hypotheses); code does what it is bad at (choose tests).

### 4.4 Falsification forcing (confirmation-bias counter)

Count tests where the current top hypothesis predicts "yes" and the oracle is asked a case predicted "yes" (positive tests) versus cases the hypothesis predicts "no" (negative tests). If the last m tests (suggest m=3) are all positive, force the next test to be one the hypothesis predicts will fail. Rationale: positive-test share correlates with failure at rho=-0.779, and with conclusive falsification at -0.937 [c02, c03]. FalsifyBench did not test such a forcing rule; Jhaveri tested a prompt instead [c05, a22]. The value of m is our guess.

### 4.5 Sequential loop (choose, run, update)

Each test is chosen after the previous outcome is in the state. Adults who wrote tests without seeing their own outcomes scored 0.12; active choosers 0.69 [a24]. A caution: the proposer group saw other people's outcomes, so this does not prove a pre-written batch fails [K13]. The safe design is sequential.

### 4.6 Disjunctive-bias fix (hypothesis sampling)

For conjunctive (AND) worlds, one-object tests cannot separate "A and B both needed" from "neither". The fix that worked in GX-Chen: sample many hypotheses (16 to 96) up front and eliminate by evidence; accuracy rose with the count, with no OR/AND gap [d13]. Samiei's successful agents also moved from 1-object to 2-object tests [d14].

### 4.7 Candidate-cause listing before testing

Siler et al. added five questions asking which variables could have caused the outcome; far transfer improved and delayed score no longer depended on pretest (88% vs 83%, N=33) [a12]. In code: before the first test, the model lists candidate causes; code builds the grid of variables; the confound detector then runs on every proposed pair.

### 4.8 Segmentation

Open one variable at a time, in order, as in the task-structuring condition (n=23) that matched direct instruction [d07]. In code: a loop over candidate variables; the model fills only the value of the focal variable; code fixes the rest.

## 5. What holds up

### Replicated or well supported
- **CVS can be taught.** Meta-analysis g=0.61 over 72 interventions (second-hand) [a06]. Same-lab replication by Strand-Cary and Klahr (N=72), a large classroom trial by Lorch (797 to 848, randomised, meets What Works Clearinghouse standards without reservations) [d03, d05]. Physical and virtual materials equal [a13].
- **Instruction helps in the short run.** Lecture plus experiments > lecture > experiments in Lorch 2010, with gains held at 5 months [d05]. Freer: explain plus design > either [a10].
- **Sparsity shapes test choice.** One strong human study (N=104) plus the model of Coenen et al. and a second adult line (66-point gap) [a01, a15, d20]. LLM agents show the same boundary on AND vs OR rules [d13, d14].
- **Choosing and inferring are separate.** Bramley (older children 17/19 vs younger 3/7) and Moeller (recognition and choice unrelated) both show it [a03, a07].
- **LLM confirmation bias is real.** Two independent labs, 11 and 12 models, same sign [a22, c02]. Reasoning models test negatively more (24-39% positive tests vs 66-82%) [c02].

### Failures, limits and contested points
- **77% vs 23% is unverified.** The best-known number in the field could not be read in this session [a19, d02].
- **Long-run qualification.** Dean and Kuhn: direct instruction not necessary or sufficient for lasting skill [d04].
- **Self-generation gave no benefit.** Kaiser: reading beat generation at first test (d=0.44) and the gap vanished within a week [b06]. Invent-then-tell tied tell-then-practice (N=101) [d06].
- **Discovery rival.** Vollmeyer and Burns (cited) say undirected exploration yields richer system knowledge; Chinn and Malhotra say once CVS is understood it is adopted almost at once [b05]. Neither was read directly.
- **Uneven gains.** In a 5-week unit, CVS gained but hypothesis-evidence coordination and drawing conclusions did not significantly [b07].
- **Low-achieving schools.** Learn less in the best condition (63% vs 82%), but benefit more from confounded examples; the gap persisted at 2.5 years in low schools only [a10, a11].
- **Strategy variability.** Kuhn 1995: strategies mixed within persons; the stage account may be partly produced by the interview [d09]. No formal failed replication of CVS-teaching effects was found [critique].
- **Opposites prompt.** Only one lab. No independent replication; FalsifyBench tested no prompts [d16, K29]. Non-thinking models gain 0 to +17 points; Dual-Goal lowers some [d15].
- **Reasoning models are not uniformly better.** BoxingGym found instruction-tuned Qwen beat math-and-code reasoning-tuned OpenThinker at experiment design [c16]. The FalsifyBench result is on rule discovery, a different task, and the two are not reconciled [critique, tension 4].
- **More thinking can hurt.** In the Blicket game, more reasoning effort in o-mini models made AND exploration worse [d13].
- **Prior and tool help is unreliable.** A Bayesian modelling tool gave no consistent gain; prior information often did not help [c17, b21].

### Moderators
- Causal sparsity (strongest), age, school achievement, reading and maths skill, theory of mind, executive function [K08].
- Task structure: binary disjunctive switches (Bramley) vs ramps and springs (Klahr).
- For LLMs: thinking mode, model size, whether the rule is conjunctive.

### Interventions that worked and did not
| Worked | Did not (or tied) |
|---|---|
| Explicit training plus probes (Chen and Klahr) [d01] | Probe questions alone [d01] |
| Instruction plus own experiments [a10, d05] | Experiments alone (lowest) [d05] |
| Confounded designs to repair [a11, d06] | Self-generation vs reading [b06] |
| Segmenting the task [d07] | Invent-then-tell vs tell-then-practice (tie) [d06] |
| One-line "focus on one factor" [d08] | Direct instruction alone for long-run robustness [d04] |
| Candidate-cause questions [a12] | Collaboration beyond a temporary help (91 sixth graders) [d09] |
| Short examples against correlation-as-causation [b13] | Feedback on wrong answers, no effect [d09] |

## 6. Language models

**No LLM study tests CVS on developmental items.** Searches of ERIC, Europe PMC, PubMed and citation lists found none, and none for MicroDYN or VOTAT. arXiv search itself was rate-limited, so recent preprints could be missed [a28, d19, K19]. The nearest tasks are 2-4-6 games, Blicket games, Zendo, ACED, BoxingGym and DiscoveryWorld. Treat everything below as indirect.

**Confirmation bias in rule discovery.**
- FalsifyBench (2026), 12 LLMs, 100 games, 20 turns: success 75% (GPT-5.2-Chat) down to 12% (GPT-5-Nano). Positive-test share 27.3% for GPT-5.2-Chat, 24.2% for GPT-OSS-20B, 39.0% for GPT-5-Mini, 66-82% for instruction-tuned. Conclusive falsification: GPT-OSS-20B 59.2%, GPT-OSS-120B 53.4%, GPT-5.2-Chat 49.5%, Llama-4-Maverick 18.0%. Failed games: partial-overlap hypotheses (27-point gap for GPT-5.2-Chat); surface-level linguistic hypotheses in 97.6% of failed GLM-5 games. Oracle agreement with human annotators: kappa 0.34 to 0.98. No human players; WordNet labels made by GPT-5-Mini [c01-c05]. The bias effect on success is large (odds ratio 0.016 for bias), while oracle error has no credible effect (OR 0.885) [c02].
- Jhaveri et al. (2026), 11 LLMs, 45 turns: success 6% to 78%. The counterexample prompt lifted the mean from 42% to 56%. Distilling the behaviour transferred to a Blicket task [a22].

**What changed it, and by how much.**
- Thinking mode: Qwen3-32B 0.41 to 0.60 with the opposites prompt, Qwen3-14B 0.34 to 0.58, at about 40% more tokens per turn [a23, d15, K11].
- Non-thinking instruct: Qwen3-8B 0.06 to 0.06; 14B 0.23 to 0.29; 32B 0.33 to 0.36; Llama-3.3-70B 0.21 to 0.38. Tokens per turn nearly unchanged (about 7 to 15). The Dual-Goal prompt lowered 14B to 0.13 and 32B to 0.10 [d15].
- Nobody tested a pretrained base model [K11].
- The critique warns that the Wason table also carries a 0.64 / 0.56 pair for another metric; use only the Wason numbers [critique].

**Conjunctive vs disjunctive.** GX-Chen: OR rules solved, AND rules failed with one object per step; oracle Q&A accuracy 1.0 on both; sampling many hypotheses closed the gap [d13]. Samiei: six LLMs (gpt-5, gpt-5-mini, gemini-2.5-flash, deepseek-reasoner, o4-mini, deepseek-chat), 48 trials each, temperature 0, show the same conjunctive-vs-disjunctive gap. Mean tests conjunctive/disjunctive: gpt-5 10.2/7.7, gemini-2.5-flash 13.5/9.7, deepseek-reasoner 8.2/6.8, o4-mini 6.7/4.2. Some match humans on final accuracy but explore less efficiently [a25]. Humans needed 9.6 (conjunctive) vs 6.4 (disjunctive) tests [a24].

**Hypotheses good, experiments poor.** Piriyakulkij: ReAct 4.60/8, human 5.26, information-gain scaffold 6.55 [d17]. BoxingGym: all approaches struggle at experimental design; larger beats smaller; closed beats open; sometimes better with 0 experiments than after some [a27, b21]. ACED-Bench (180 core tasks, 7 contemporary and 2 older LLMs, 3 agent designs, four-turn budget): failures are the wrong intervention, lost evidence, and not stopping. Final accuracy hides this [a26, d18].

**Agent-level results.** DiscoveryWorld: easy completion ReAct 0.38, Plan+Execute 0.18, Hypothesizer 0.28; normal 0.18/0.18/0.23; challenge 0.18/0.15/0.08; humans 0.66. Knowledge scores near zero on harder tasks (challenge 0.10/0.01/0.08 vs human 0.55). Several tasks were never completed by any agent: Reactor Lab, Space Sick, Rocket Science [c07-c09]. The critique notes the unit-test average is 0.60/0.44/0.64, so "60%+" only applies to some agents [critique row 3]. ScienceWorld best 0.17 normalised; MLAgentBench 37.5% over 13 tasks; ScienceAgentBench 32.4% (102 tasks, 44 papers) [b17, b23, b24]. An independent test of the AI Scientist found 42% of experiments failed on coding errors [c26].

**Other relevant LLM facts.** Binz and Schulz: GPT-3 "fails miserably in a causal reasoning task" and shows no directed exploration [c21, abstract only]. Krishnamurthy: only GPT-4 with chain of thought plus an externally summarised history explored reliably [c24, abstract]. Hold these loosely.

**Applied scaffold result.** A requirement-analysis step before simulator calls raised precision from 65% to 94% [c13]. One simulator, one lab.

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | In S4, have **code** detect confounds: when a test pair differs in 2 or more variables, mark it "inconclusive for each of them" and do not credit the result to either. Do not rely on the model to notice. | S4 (code check) | [E] | K06, K25, K07; b12, a04, a07 |
| 2 | Track **test design and inference separately** in logs: did the agent pick a good test, and did it draw the right conclusion from the result. They fail independently. | S4/S5 (logging, schema section 6) | [E] | K07; a03, a07, b11 |
| 3 | **Count positive vs falsifying tests** in code. Confirmation bias predicts failure in two labs. Log the share. (A forcing rule is under "Test first".) | G3/S4 | [E] for the diagnosis | K10, K12; a22, c02, c03 |
| 4 | Make the S4 text state the sparsity boundary: **one change per test when many causes are plausible or interactions are possible; grouped (split-half) tests when few causes are expected.** Do not write "always one change". | S4 | [E] | K02; a01, a03, a15, d13, d14 |
| 5 | **Choose each test after seeing the previous outcome.** Keep S4 sequential, not a pre-written batch. | S4/S5 | [E] direction, [S] on batch evidence | K23, K13; a24, d14 |

Item 4 is [E] on the boundary (children plus LLM agents plus a model), but the exact thresholds are not known. Item 5 rests on one study whose "proposer" arm saw other people's outcomes, so it supports the sequential design and does not prove batches fail. Per schema section 8, items marked [E] still need to pass the equal-token rule (G7) on our bench before they stay.

### Test first (single-source or contested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 6 | **Falsification forcing:** if the last 3 tests were all confirming, force a test the current top hypothesis predicts will fail. Compare to a prompt-only version. | S4, S7 | [S] | K10, K11, K29; a22, c02, d15 |
| 7 | **EIG test chooser:** the model proposes hypotheses; code scores candidate tests by how many remaining hypotheses they split and runs the best. | S4, S2 | [S] | K27; d17, d18 |
| 8 | **List candidate causes first,** then build the test grid, then run the confound detector. | S2/S4 | [S] | K20, K22; a12, d13 |
| 9 | **Many-hypothesis sampling for AND worlds** (16 to 96 initial hypotheses, eliminate by evidence). | S2/S3 | [S] | K22; d13 |
| 10 | **One-line focus rule** ("vary only one factor") vs a long CVS rule. | S4 | [S] | K24; d07, d08 |
| 11 | **One worked confounded example** in the S4 text, with repair. | S4 | [S] | K04, K26; a11, d06 |
| 12 | **Opposites prompt** only if the base model uses thinking mode; skip for small non-thinking models. | S4 | [S] | K11; a22, a23, d15 |
| 13 | **Requirement-analysis pre-check** ("what comparison is needed?") before running a check. | S4 | [S] | K18; c11-c14 |
| 14 | **Hypothesis step** on hard tasks: DiscoveryWorld shows it can cost completion. Measure before keeping it. | G7 | [S] | K15; c10 |
| 15 | **Repeating the one-change rule at every test** vs stating it once. | S4 | [C] | K05; d02-d06 |
| 16 | Keep a refuted hypothesis flagged across a multi-session task. | memory | [S] | K28; d09 |

Do not add a generic "be careful" instruction; schema section 4b already excludes it.

## 8. Concrete tests on our bench

All arms at equal total tokens (G7). Setup cost counts. Use at least 3 seeds and report a bootstrap interval.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | **Switch-box set.** Sparse (1 true cause of 6) and dense (1 broken of 6), OR and AND variants, 40 items per cell. | (a) plain; (b) "one change per test" always; (c) sparsity-aware rule (item 4); (d) EIG chooser | Tests to identify the cause; accuracy at a fixed test budget | (b) wins dense, loses sparse; (c) matches the best of both; (d) equal or better. Human anchor: split-half expected return 1.90 vs 1.25 |
| T2 | **AND-rule Blicket items**, 4 and 8 objects. | plain; one-change; list-causes-then-split; 16-96 hypothesis sampling | Accuracy on AND minus accuracy on OR | Sampling closes the gap [d13]; "one change" alone widens it |
| T3 | **Rule discovery (2-4-6 and WordNet category rules).** | plain; opposites prompt; code forcing of falsifying test; both | Success rate; positive-test share | Forcing lifts success at least as much as the prompt on a non-thinking model; the prompt alone near flat on small models [d15] |
| T4 | **CVS items in developmental format** (ramps, springs, balls; 2, 3, 4 variables), scored as in Chen and Klahr: choose the controlled pair from several pairs. | plain; CVS rule once; CVS rule per test; one worked confounded example; code confound detector as a filter | Share of controlled pairs chosen; justification correct | Fills the main gap (K19). Expect near ceiling for strong models; the point is to find where each model type fails |
| T5 | **Choice vs inference split.** Show a result from a confounded pair, ask what can be concluded. | plain; with confound detector message | Share saying "cannot tell" when 2 variables changed | Detector should push this to near 100%; human preschool value 39% |
| T6 | **Sequential vs batch.** Hidden-rule worlds, 3 to 5 tests per rule. | sequential; batch written up front | Accuracy at equal tests | Sequential wins in conjunctive worlds [a24, d14] |
| T7 | **Multi-variable systems (MicroDYN style).** | free test choice; forced VOTAT; sparsity-aware | Knowledge score and control score | VOTAT best with many plausible causes [b15]. Untested on LLMs |
| T8 | **Correlational vs interventional evidence probes** (Seifert items). | plain; one example lesson in S4 | Share accepting a causal claim from correlation | Drop from base rate; humans fell from 66% [b13] |
| T9 | **Hypothesis step on hard items** (DiscoveryWorld-style or our own multi-step tasks). | with vs without explicit hypothesis step | Completion and knowledge | Easy: knowledge up. Hard: completion may fall [c10] |
| T10 | **Multi-session retention.** A task over several sessions in which one early hypothesis is refuted. | memory of refutation vs none | Rate of re-adopting the refuted hypothesis | Fewer re-adoptions with memory; no evidence yet |

## 9. What does not transfer, and why

- **Stage claims and ages.** Piagetian onset of formal operations, the Kuhn 1995 strategy stages, the "critical period 9-11" are statements about children's development. An LLM has no development curve; use them only as item-difficulty hints.
- **Individual-difference predictors** (theory of mind, executive function, reading, maths) [K08] have no counterpart in a scaffold.
- **Classroom teaching effects** (lecture, hands-on, collaboration). They assume a learner who keeps what it was taught. Our agent starts every run fresh; the nearest analogue is the text in S4, and the one-line focus instruction [d08] is the only intervention that maps directly. Instruction-then-practice results do not carry over to a model in the same run.
- **Long-run retention at 5 months or 3 years** [d03, d05] has no meaning for a stateless call. Only the memory lessons (schema section 5) persist.
- **Self-generation and discovery learning debates** [b06, d02] are about what the learner retains. For an agent, the question is only which scaffold wins at equal tokens.
- **Switch-box cost model.** Children paid in tokens per test; our agent pays in text tokens. The EIG argument still holds but the cost ratios differ.
- **"One variable at a time" in knowledge-lean tasks.** Moeller's preschoolers saw artificial tasks. LLMs have world knowledge, which can substitute for testing and bias it. In SciGame, familiar priors hurt once the rule changed [d18].
- **Human fatigue and motivation effects** are absent.
- **Reasoning-model results** apply to models with a thinking mode; they do not transfer to a pretrained base model, which nobody tested.

## 10. Open questions

1. What are the real numbers in Chen and Klahr (1999) and Klahr and Nigam (2004): mastery percentages, transfer, sample per cell? Is 77% vs 23% correct?
2. Does a "vary one thing" rule in S4 help an LLM at equal tokens on dense tasks and hurt on sparse tasks? No equal-token study exists.
3. Do LLMs confound variables on developmental CVS items, and how does reasoning budget change it? No study found.
4. Does the opposites prompt replicate on a pretrained base model and outside rule discovery? No independent replication.
5. Do LLMs keep a refuted hypothesis across sessions (Kuhn's multi-week design)? Piriyakulkij and ACED give partial hints only.
6. Does handing the agent its own earlier test outcomes matter for batched plans? The human result is not a clean test of batching.
7. Do MicroDYN or VOTAT results hold for LLMs?
8. Why does reasoning effort worsen conjunctive exploration in o-mini models [d13] while reasoning models falsify more [c02]? Different tasks, not reconciled.
9. Is the Schwichow g=0.61 reproducible from the paper itself? It is second-hand.
10. Is the sparsity effect in children robust to ramps and springs? Bramley's boxes are binary and disjunctive.
11. Hypothesis-evidence coordination did not improve in a 5-week unit [b07]. What trains it?
12. Which of the 2026 LLM preprints (Jhaveri, FalsifyBench, Samiei, ACED) survive replication?

## 11. Sources

[V] = opened and text read this session. [M] = snippet, citation only, or abstract-level where noted.

**Developmental**
- Bramley, Jones, Gureckis, Ruggeri (2022) Children's failure to control variables may reflect adaptive decision-making. https://pmc.ncbi.nlm.nih.gov/articles/PMC9722808/ [V]
- Coenen, Ruggeri, Bramley, Gureckis (2019) Testing one or multiple. Read through Bramley's text. https://pmc.ncbi.nlm.nih.gov/articles/PMC9722808/ [M]
- Peteranderl and Edelsbrunner (2020) Predictive value of children's understanding of indeterminacy and confounding for CVS. https://pmc.ncbi.nlm.nih.gov/articles/PMC7736087/ [V]
- Schwichow, Croker, Zimmerman, Hoffler, Hartig (2016) Teaching the control-of-variables strategy: a meta-analysis. Read only as a citation in the above. https://pmc.ncbi.nlm.nih.gov/articles/PMC7736087/ [M]
- Bullock and Ziegler (1999), Tschirgi (1980), Inhelder and Piaget (1958), Kuhn (2007): cited in Peteranderl. https://pmc.ncbi.nlm.nih.gov/articles/PMC7736087/ [M]
- Moeller, Sodian, Sobel (2022) Developmental trajectories in diagnostic reasoning. https://pmc.ncbi.nlm.nih.gov/articles/PMC8886032/ [V]
- Sobel, Koksal, Osterhaus, Bachhuber and colleagues (2026) Longitudinal theory of mind and scientific reasoning. https://pmc.ncbi.nlm.nih.gov/articles/PMC13505288/ [V] (one paper; the last author differs between a08 and b09)
- Osterhaus and Koerber (2023); Koerber and Osterhaus (2020): cited in the above. https://pmc.ncbi.nlm.nih.gov/articles/PMC13505288/ [M]
- Schlatter, Molenaar, Lazonder (2020) Individual differences in children's development of scientific reasoning through inquiry learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC7241249/ [V]
- Freer, Lorch, Lorch, Calderhead (2011) Deconstructing the interaction in teaching CVS. https://files.eric.ed.gov/fulltext/ED528958.pdf [V]
- Siler, Klahr, Willows, Magaro (2011) Scaffolded case-based questions and CVS transfer. https://files.eric.ed.gov/fulltext/ED528963.pdf [V]
- Triona and Klahr (2007) Hands-on science. https://files.eric.ed.gov/fulltext/EJ1050925.pdf [V]
- Morris, Croker, Zimmerman, Gill, Romig (2013) Gaming science. https://pmc.ncbi.nlm.nih.gov/articles/PMC3766824/ [V]
- Kuhn and Franklin (2006): cited in Morris. https://pmc.ncbi.nlm.nih.gov/articles/PMC3766824/ [M]
- Montes, van Dijk, Puche, van Geert (2017) Trajectories of scientific reasoning in 5-year-olds. https://pmc.ncbi.nlm.nih.gov/articles/PMC7869623/ [V]
- Kaiser, Mayer, Malai (2018) Self-generation in inquiry-based learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC6315139/ [V] (critique: spot-checked only)
- Seifert, Harrington, Michal, Shah (2022) Causal theory error in college students. https://pmc.ncbi.nlm.nih.gov/articles/PMC8755867/ [V]
- Mueller and Coon (2013), Sumner et al. (2014), Xiong et al.: cited in Seifert. https://pmc.ncbi.nlm.nih.gov/articles/PMC8755867/ [M]
- Molnar and Csapo (2018) Students' problem-solving strategies in MicroDYN. https://pmc.ncbi.nlm.nih.gov/articles/PMC5855089/ [V]
- Funke (2014), Schoppek and Fischer (2017): cited in Molnar. https://pmc.ncbi.nlm.nih.gov/articles/PMC5855089/ [M]

**Founding studies (abstract level only, via PubMed or ERIC; no cell-level numbers)**
- Chen and Klahr (1999) All other things being equal. https://doi.org/10.1111/1467-8624.00081 [M, abstract] (PMID 10546337, ERIC EJ597753)
- Klahr and Nigam (2004) The equivalence of learning paths in early science instruction. https://doi.org/10.1111/j.0956-7976.2004.00737.x [M, abstract] (PMID 15447636)
- Klahr and Dunbar (1988) Dual space search. https://doi.org/10.1207/s15516709cog1201_1 [M]
- Klahr, Fay, Dunbar (1993) Heuristics for scientific experimentation. https://doi.org/10.1006/cogp.1993.1003 [M]
- Kuhn, Garcia-Mila, Zohar, Andersen (1995) Strategies of knowledge acquisition. https://doi.org/10.2307/1166059 [M]; abstract at https://eric.ed.gov/?id=EJ518577 [M, abstract]
- Strand-Cary and Klahr (2008). https://doi.org/10.1016/j.cogdev.2008.09.005 [M, abstract] (ERIC EJ819444)
- Dean and Kuhn (2007). https://eric.ed.gov/?id=EJ760016 [M, abstract]
- Lorch et al. (2010). https://eric.ed.gov/?id=EJ876300 [M, abstract]; What Works Clearinghouse review ED535812 [M, abstract]
- Lorch et al. (2014) and Matlen and Klahr (2013). https://eric.ed.gov/?id=EJ1054467 and https://eric.ed.gov/?id=EJ999871 [M, abstract]
- Task segmentation study. https://eric.ed.gov/?id=EJ1039461 [M, abstract]
- Kuhn and Dean (2005). https://doi.org/10.1111/j.1467-9280.2005.01628.x [M, abstract] (PMID 16262771)
- Klahr and Chen (2003) Overcoming the positive-capture strategy. https://doi.org/10.1111/1467-8624.00607 [M, abstract] (PMID 14552398)

**LLM and AI**
- Jhaveri, GX-Chen, Sucholutsky, Choi (2026) Failing to falsify. https://arxiv.org/abs/2604.02485 [V]
- Bertolazzi, Tentori, Bernardi (2026) FalsifyBench. https://arxiv.org/html/2606.04751 [V]
- Samiei et al. (2026) Human adults and LLMs as scientists. https://arxiv.org/abs/2606.06464 [V]
- GX-Chen, Lin, Samiei, Precup, Richards, Fergus, Marino (2025) Blicket game with LLMs. https://arxiv.org/abs/2505.09614 [V]
- Piriyakulkij, Langenfeld, Le, Ellis (2024) Doing experiments and revising rules. https://arxiv.org/abs/2402.06025 [V]
- Chen et al. (2026) ACED-Bench. https://arxiv.org/abs/2610.14381 [V]; Witness, SciGame, DiG-bench as summarised there [M]
- Gandhi et al. (2025) BoxingGym. https://arxiv.org/abs/2501.01540 and https://arxiv.org/pdf/2501.01540v2 [V]
- Jansen et al. (2024) DiscoveryWorld. https://arxiv.org/abs/2406.06769 and https://arxiv.org/html/2406.06769v1 [V]
- Wang, Jansen, Cote, Ammanabrolu (2022) ScienceWorld. https://arxiv.org/abs/2203.07540 [V]
- Huang, Vora, Liang, Leskovec (2024) MLAgentBench. https://arxiv.org/abs/2310.03302 [V]
- Chen et al. (2025) ScienceAgentBench. https://arxiv.org/abs/2410.05080 [V]
- Xia et al. (2026) LLM agents perform controlled experiments. https://arxiv.org/pdf/2608.23622 [V]
- Rueda et al. (2025) Understanding LLM scientific reasoning through prompts. https://arxiv.org/pdf/2505.01482 [V]
- Binz and Schulz (2022) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 [M, abstract]
- Kosoy et al. (2022) Learning causal overhypotheses. https://arxiv.org/abs/2206.08353 [M, abstract]
- Dasgupta et al. (2022) Language models show human-like content effects. https://arxiv.org/abs/2207.07051 [M, abstract]
- Krishnamurthy et al. (2024) Can LLMs explore in-context? https://arxiv.org/abs/2403.15371 [M, abstract]
- Wang et al. (2023) Hypothesis search. https://arxiv.org/abs/2309.05660 [M, abstract]
- Beel, Kan, Baumgart (2025) Evaluating Sakana's AI Scientist. https://arxiv.org/abs/2502.14297 [V]
- Lu et al. (2025) AI Scientist-v2. https://arxiv.org/abs/2504.08066 [V]; Lu et al. (2024) AI Scientist. https://arxiv.org/abs/2408.06292 [V]
- Gui and Toubia (2023). https://arxiv.org/abs/2312.15524 [M]; EAIRA (2025). https://arxiv.org/pdf/2502.20309 [M]
- Absence searches. https://api.ies.ed.gov/eric/ [M]
