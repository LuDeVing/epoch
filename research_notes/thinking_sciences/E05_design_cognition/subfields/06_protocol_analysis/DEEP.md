# Protocol analysis: deep document

Subfield E05.06. Coding think-aloud of designers. Key works: Cross, Gero, Eastman. Why it matters: it is the method for coding LLM traces (see E06). Evidence ids (a01..d18) refer to evidence_a-d.jsonl in this folder. Claim ids (E05.06-K01..K28) refer to claims.jsonl. Numbers were checked against opened text in critique.md.

A warning about the base. Most human-side foundations (Ericsson and Simon, Nisbett and Wilson, Dorst and Cross, Kuusela and Paul, Waterman and Newell) were NOT opened this session. No numbers from them are claimed. Independent human design-protocol evidence is thin (one review, Hay 2017). The LLM side is richer, but it mostly tests reasoning traces in general, not design talk.

## 1. What it is

Protocol analysis is a method. A person works on a task and speaks their thoughts out loud (concurrent think-aloud), or explains afterwards (retrospective report). The speech is recorded, cut into segments, and each segment gets a code from a fixed scheme. The coded sequence is then counted and modelled. It is not a theory of design. It is a way to turn talk into data.

In design research the method has three parts.
- Collection: a designer (often an architect, or an engineering or product design student) solves a design brief. Video and sketches are kept. In Hay et al. (2017), 32 of 47 studies were concurrent (68.1%), 11 retrospective (23.4%), 4 combined (8.5%). Protocols ran 15 to 600 minutes (b08).
- Coding: a scheme turns segments into labels. The best known scheme is the Function-Behaviour-Structure (FBS) ontology of Gero. It has 6 issues (Requirement R, Function F, Expected behaviour Be, Behaviour from structure Bs, Structure S, Description D) and 8 processes (formulation, synthesis, analysis, evaluation, documentation, and three reformulations). One code per segment (a01, a02).
- Analysis: code shares, transition matrices (Markov models, 6x6 first order, 8x6 second order), and linkographs (a graph linking each move to earlier moves it builds on, from Goldschmidt). Entropy of link patterns is a proposed summary (a03).

For our agent the method matters in two ways. First, it is a way to code LLM reasoning traces so that traces can be compared across tasks, models and scaffolds. Second, it carries a warning: verbal reports are a partial record, and the LLM literature on faithfulness (Turpin, Lanham, Chen) is the same debate as Nisbett and Wilson versus Ericsson and Simon, now with measured numbers.

## 2. History and theories in depth

Newell and Simon (1972) built problem-solving theory on human protocols. Waterman and Newell (1971) built a program (PAS-II) to code protocols automatically. We know both only through citations (c29, b20). So the idea of machine-coded protocols is 50 years old. What is new is that LLMs can do the coding for free text.

Nisbett and Wilson (1977) argued that people often cannot report the true causes of their behaviour. A classic example, recalled and not verified here, is the position effect on choosing items, where participants denied any position effect (a17, b25, not opened). Ericsson and Simon (1980, 1984/1993) answered that concurrent think-aloud, which reports the contents of short-term memory without explaining, is a valid data source, while retrospective or explanatory reports are riskier (a16, b24, not opened).

The meta-analysis of Fox, Ericsson and Best (2011) is the best test of that view that we opened (b01, b02, c04). 94 studies, nearly 3,500 participants. Plain think-aloud had r = -.03, indistinguishable from zero. It stayed null after controlling for task type. Conditions where people were asked to explain or describe did differ from silent controls (they helped). All verbal conditions took longer. Schooler (2011) replied that null reactivity on accuracy does not show the reports are complete or valid, for example for inchoate or non-verbal insight (b03). Ericsson and Fox (2011) replied that think-aloud is a qualitatively different thing from introspection (b04). The dispute is open (K03, contested).

Design cognition grew from this base. Cross and colleagues studied designers by protocol. Dorst and Cross (2001) proposed co-evolution of problem space and solution space (not opened, a15, d15). Gero, Kan and Pourmohamadi (2011) saw that design protocol studies could not be compared because each group used its own ad hoc codes even on the same data. They proposed one fixed ontology, FBS, and a seven-step method: coding development, video, transcription, segmentation and coding, analysis of the coded protocol, linkograph generation, linkograph analysis. Demo: one industry team, over 1 hour, 1,280 coded segments (a01). They report the FBS papers had over 900 Google Scholar citations in 2011 (a04). Eastman's early design-protocol work is on the key-works list but was not opened here.

Syntactic versus semantic linkographs (a02). A syntactic linkograph treats only adjacent segments as linked, which is a weak model. A semantic linkograph links by meaning (S linked back to Be counts as synthesis). Kan and Gero proposed entropy of link patterns as a measure of design process quality (2007). The opened original shows the low-scoring sessions had higher entropy, not lower (d01, section 5).

The field review. Hay et al. (2017) screened 6,796 articles (4,996 after de-duplication) and included 47 studies from 1979 to 2015. 24 of 47 (53.2%) were from the last decade (a05). About 350 participants in all. Per study 1 to 36, mean 7, median 6, SD 6.30. 64% of the 33 in-depth studies used 5 or fewer participants. 33% used 2 or fewer (b07). 45 design tasks: 20 architecture (44.4%), 19 product design engineering (42.2%), 6 engineering (13.3%) (a06). 35 cognitive processes were found. Of the 24 reported, 10 were search (41.7%) and 14 were exploration (58.3%). Half of the 24 processes rest on a mean of 5 or fewer participants. No meta-analysis was possible. No inter-rater reliability was reported for primary coding. They also proposed a shared ontology of 6 categories (a07).

The LLM turn, 2023 to 2026, has three strands.
1. Faithfulness: is the written reasoning the real reason? (Turpin 2023, Lanham 2023, Chen 2025, 2026 follow-ups.)
2. LLM as coder: can a model apply a protocol scheme to human think-aloud? (Wurgaft 2025, Sakib 2026, Dunivin 2024, others.)
3. Coded LLM traces: do human taxonomies expose useful structure in model reasoning? (Li 2025, Gandhi 2025, Thoughtology, Thought Anchors.) One paper, Zhang 2025, applies FBS coding to LLM design runs directly.

## 3. Core findings with exact numbers

Status key: est = established (3 or more independent sources or a meta-analysis), single = single source, contested = sources disagree or evidence is weak.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Plain think-aloud does not change accuracy. Explain or describe instructions do (they help). All verbal reporting is slower | 94 studies, nearly 3,500 participants, think-aloud r = -.03 | Fox, Ericsson, Best 2011 (b01, b02, c04) | est (K01) |
| Large replication on Game of 24: no accuracy cost, a time cost | Solved 53% control vs 49% think-aloud (p = 0.067). Time 125.1 vs 117.7 s (p = 0.008). 640 think-aloud + 60 control. 4,947 usable trials. Item difficulty ordering kept, r = 0.83 | Wurgaft et al. 2025 (c01, c03) | est with K01 (K02) |
| Reports can be valid on accuracy but still incomplete | no numbers; argument only | Schooler 2011; Ericsson and Fox 2011 (b03, b04) | contested (K03) |
| Design protocol codes lack comparability. FBS is the proposed fixed scheme | 6 issues, 8 processes. Demo 1,280 segments, one team | Gero et al. 2011 (a01, a02) | single (K04) |
| Evidence base for design protocols is small | 47 studies, about 350 participants, median 6 per study, 64% of in-depth studies at 5 or fewer, no reliability reported | Hay et al. 2017 (a05, b07) | est (K05) |
| LLM coder, coarse design-question codes | GPT-4.1 80.2% vs human-human 85.7% at 3 categories. 52.5% vs 74.7% at 21 subcategories. Per code 93% (low-level) to 53% (generative); subcategories 20.8% (Ideation) to 89.1% (Disjunctive). 1,942 test questions in d1, 175 in d2. The abstract says "up to 85.7%" for GPT-4.1, but 85.7% is the HUMAN figure. Exp. 2 tops at 85.1% | Sakib et al. 2026 (b14, d04, d05) | single (K06) |
| LLM coding of STEM think-aloud varies by task and code | Accuracy .49 to .90. Math M = .78, above biology. Few-shot not reliably better (OR 0.90, ns) and hurt sub-goal setting (81.6 vs 71.2). Human kappa 0.65 (math), 0.66 (biology) | J Learn Analytics 2026 (c17, c18) | single (K07) |
| Asking for a rationale before a code raises agreement | GPT-4 per-code kappa 0.676 with rationale vs 0.592 without (232 passages, 9 codes). Hard code 0.304 vs 0.092. In another study GPT-4 vs humans Fleiss kappa 0.44 to 0.50, humans 0.73, GPT-4 runs vs each other 0.87 | Dunivin 2024; QualiGPT 2024; Kirsten 2024 (c13-c16) | est (K08) |
| Behaviour-by-behaviour coding of reasoning traces | GPT-4o-mini vs two humans ICC3: verification 0.66 and 0.65, backtracking 0.67, subgoal 0.70 and 0.77, backward chaining 0.55 and 0.40. LLM-LLM agreement higher than LLM-human | Gandhi et al. 2025 (c22) | single (K09) |
| Automated coding is cheap but not clean | Claude coded 4,947 trials in under 2 h for $74 vs about 816 human hours (8 h 15 min per 50 trials). All LLMs agreed less with humans than humans did (p < 0.002). Errors survive five rounds of auto-correction. Subgoals in only 9.0% of trials (445) | Wurgaft 2025 (c01, c02) | single (K10) |
| Written CoT can omit the real driver | Biases cut accuracy up to 36% (Suggested Answer -36.3% GPT-3.5, few-shot -24.1%). 1 of 426 explanations mentioned the bias. 0 of 234 generations | Turpin et al. 2023 (a19, b21, c25) | single (K11) |
| Reasoning models also under-report hints | Faithfulness 25% (Claude 3.7 Sonnet), 39% (R1). Misaligned hints 20% and 29%. RL plateau 28% MMLU, 20% GPQA. Reward hacks used on over 99% of prompts, verbalised under 2% (5 of 6 environments). Harder tasks less faithful (44% and 32% relative drop on GPQA vs MMLU) | Chen et al. 2025 (a21, b23, c24) | single, 3 follow-ups agree in direction (K12) |
| 2026 follow-ups show wide spread | 12 open models: 39.7% (Seed-1.6-Flash) to 89.9% (DeepSeek-V3.2-Speciale), overall 69.7% (7,161 of 10,276 influenced cases). Judge choice shifts by about 12.9 points. By hint type 35.5% (consistency) to 79.4% (unethical). Claude 4.5 Haiku honesty at most 34.5%. Reliance judge kappa only 0.26 (presence 0.80) | Young 2026; Walden 2026 (d06, d07) | single (K12) |
| CoT dependence is task-dependent | Truncating CoT changes the answer under 10% on ARC and OpenbookQA, over 60% on AQuA. CoT gain +15.32 (AQuA), -4.69 (HellaSwag). Early-answering area over curve LogiQA 0.44, HellaSwag 0.26, OpenBookQA 0.12, ARC Easy 0.12, lowest 0.02 to 0.07 | Lanham et al. 2023 (a20, b22) | single (K13) |
| Human-derived taxonomy on LLM traces | 28 elements. 192K model traces vs 1,346 human traces (240 recruited, 236 kept, 30 problems). Models use 26% fewer elements on ill-structured problems. Guided by successful structures: +9.7 (+/-1.8) points on ill-structured for strongest models, +18.8 (+/-3.7) on dilemmas. All models +4.4 (+/-1.2) vs +1.6 on well-structured | Li et al. 2025 (b18, b19) | single (K14) |
| Behaviours explain RL outcomes | Countdown: Qwen-2.5-3B about 60% after RL vs Llama-3.2-3B about 30%. Priming Llama with the behaviours matched Qwen. Empty-CoT priming 30-35%. Incorrect solutions with right behaviours matched correct ones | Gandhi et al. 2025 (c21) | est with c19, c23 (K15) |
| Plan and uncertainty sentences matter most | Counterfactual importance highest for plan generation and uncertainty management among 8 sentence categories | Bogdan et al. 2025 (c23) | est (K15) |
| Rumination and length sweet spot in R1 | N-gram repetition rises with difficulty. Accuracy rises, peaks, falls with length on AIME-24. Multiplication always right to 6x6 digits, almost always wrong above 12x12 | Marjanovic et al. 2026 (c19, c20) | single (K16) |
| GPT-4o prompted as problem-driven vs solution-driven reproduces static FBS shares, not crossings | R 9.7 vs 4.3, F 18.9 vs 9.2, S 10.6 vs 29.3, Formulation 31.7 vs 16.3, PP 30.7 vs 15.3, SS 9.9 vs 29.4, PS 6.7 vs 10.5 (p = 0.001). 10 runs per cell. Inter-coder 79.5% raw. Expert r 77.02%. Correction: Be 10.5 vs 13.6 (p = 0.042) also differs | Zhang et al. 2025 (a08-a10, b11-b13) | single (K17) |
| Simulated think-aloud is unlike human | Cosine to human 0.16 and 0.19. Coherence difference -0.22 and -0.44. Success prediction AUC .528 and .572. 630 utterances, N = 10 students | Borchers et al. 2026 (b17) | single (K18) |
| LLM concept extraction and fuzzy linkography unvalidated | 17 designers, 2-second segments. Degree-connectivity correlation across problems 0.721 and 0.710. 6,424 traces, no human validation | Kelly and Gero 2025; Smith 2025 (b16, c09, d03) | contested (K19) |
| Two-coder disagreement is informative | Agree-pair cosine 0.957 vs disagree 0.904 (d = 1.16, 9,746 pairs) | Tajik et al. 2026 (c11, c12) | single (K20) |
| Entropy of linkographs did not track quality in the original | 12 sessions, 6 architects. High group 0.499, 0.338, 0.299 vs low group 0.529, 0.481, 0.422. Only change of entropy over time is claimed | Kan and Gero 2007 (d01, d02) | contested (K21) |
| Trace content, not length, carries answer signal | Injecting own trace: +18.1 to +33.1%. Length-matched random -3.9 to +4.2%. Swapped -18.4 to +3.0%. Shuffled +0.3 to +10.8% (5 open models, GPQA Diamond and MMLU-Pro) | Ballon et al. 2026 (d09) | single (K23) |
| Trace validity and accuracy can diverge | Corrupted-trace training matches correct-trace training (small transformers, formal tasks) | Valmeekam et al. 2025 (d11) | contested (K24) |
| Judge models favour themselves | Over 50% more likely to wrongly pass own failing output. Ensembling helps, does not remove | Pombal et al. 2026 (d16) | single (K26) |
| Human-AI co-design protocol study | 20 novices, 686 segments. Creativity +0.51 to +0.75. Abduction up to +27.2. Midjourney effect flips to -0.833 when abduction is controlled | Guo et al. 2024 (d13) | single, fragile (K27) |
| Expertise effects | Expert 6 vs student 30 simultaneous cognitive actions. 3 architects blindfolded vs sighted n.s. | Hay et al. 2017 (b09) | single (K22) |

## 4. Mechanisms and models

This section is written so an engineer can build each piece.

### 4.1 The coding pipeline (what to build for agent traces)

1. Segment the trace. Use one idea per segment. Gero uses utterance units. Kelly and Gero used fixed 2-second slices (a poor fit for text). For LLM text, split by sentence or by paragraph break. Bogdan used sentences (c23). Record the segmentation rule, because it is a free parameter.
2. Define a closed code set with one code per segment. Options: FBS (6 issues, 8 processes), Li's 28 elements, Gandhi's four behaviours (verification, backtracking, subgoal setting, backward chaining), Bogdan's 8 sentence categories. Keep the set small. Sakib shows accuracy falling from about 80% at 3 categories to 52.5% at 21 subcategories.
3. Code with a model coder that writes a short rationale first, then the label (Dunivin: kappa 0.676 vs 0.592). Use temperature 0. Code each category separately if one scheme has many codes (c17: per-code validation).
4. Use two coders from different model families. Treat their disagreement as a flag for a fuzzy code (Tajik: agreeing pairs cosine 0.957, disagreeing 0.904). Do not read LLM-LLM agreement as validity (Gandhi: LLM-LLM above LLM-human. Pombal: self-preference).
5. Validate on a human-coded subset of at least 100 segments or traces. Report chance-corrected agreement (kappa or ICC) per code, never one overall percent. Almost all LLM-coder papers here report raw percent (Zhang 79.5%, Sakib), which hides weak codes.
6. Run executable checks where the coded object is a program or graph (Wurgaft: five rounds of auto-correction still left three error types).

### 4.2 Measures on coded sequences

- Code shares: count per code as a percentage of segments. Compare across conditions with a test. Zhang used p-values over 10 runs per cell.
- Markov transition matrix: first-order 6x6 for FBS issues, second-order 8x6 for processes. Cell (i, j) is the share of transitions from code i to code j.
- Problem-solution crossings (PS and SP transitions): the Zhang measure of co-evolution. Problem-driven runs had fewer (PS 6.7 vs 10.5).
- Linkograph: one node per move. A link from move j back to an earlier move i if j builds on i. Backlinks go to earlier moves, forelinks go forward. Link density is links per move. Build links by meaning (semantic), not just adjacency.
- Entropy over a sliding window (Kan and Gero): within each window compute the entropy of the link-pattern distribution. The window is a free parameter: 1/10 of the protocol in the 2011 demo, 28 moves in the 2007 study. Whole-session entropy did not track outcome (d01). Only change over time is claimed.
- Fuzzy linkography: link when the embedding cosine of two moves exceeds a threshold (0.35 on all-MiniLM-L6-v2 in d03). Cheap (about 0.4 s per trace) but unvalidated. It can link moves that sound alike but address different problems (c10).

### 4.3 Faithfulness probes (the Nisbett-Wilson test for models)

Recipe from Turpin and Chen. Take a multiple-choice set. Run each item once without a hint and once with a planted hint (suggested answer, reordered options, metadata, a grader hack). Keep only items where the answer changed to the hint. Among those, check whether the written trace mentions the hint. Faithfulness = share that mention it. Judge by a keyword check plus a judge model, and report both, because the judge alone moves the number about 13 points (d07). Reliance (did it use the hint?) is harder to judge than presence (kappa 0.26 vs 0.80, d06).

Truncation probe (Lanham). Cut the trace at k steps, force an answer, and measure how often it changes. Little change means the later reasoning is post hoc on that task. Area over the curve summarises it (LogiQA 0.44 high, ARC Easy 0.12 low).

### 4.4 Intervention probes (tests of whether a coded step matters)

Correlation between a coded step and success is weak evidence, since harder items give longer traces and fewer successes (Ballon). Use interventions: remove the step, swap in a step from another question, shuffle tokens, or length-match with random tokens (d09). Thought Anchors resamples to measure counterfactual importance of each sentence (c23). Gandhi primed models with traces and tested whether the behaviour, not the correctness, caused the gain (c21).

## 5. What holds up

Holds up well:
- Plain think-aloud is non-reactive on accuracy in humans. The 94-study meta-analysis (r = -.03) and the 640-person Game of 24 replication agree (K01, K02). It costs time (about 7 s per trial, about 6%).
- Explanation instructions do change performance, and for the better. This is a directed verbalisation, not a plain report.
- Writing a rationale before an LLM codes raises agreement (K08, 3 sources).
- Coding traces by behaviour or sentence function shows which parts matter (K15, 3 sources).
- Design protocol samples are small (K05).

Holds up, but only in one source:
- Faithfulness numbers (25%, 39%) come from one lab's paper (Chen). 2026 follow-ups give a wider range (39.7% to 89.9%). Treat 25% as a low-end example, not a constant. Baker et al. 2025 reported over 90% detection of coding reward hacks through CoT monitoring (cited in a21, not opened), so the hidden-influence problem depends on the task.
- Li's guidance gain (+9.7 on ill-structured) has not been replicated outside the authors' trace pool (K14, d18 snippet).
- Zhang's FBS-by-prompt result is one model, one task, a prompt that names the issue types (circular), 10 runs per cell.

Failures and contradictions:
- Kan and Gero's entropy: the low-scoring group had higher entropy (0.529, 0.481, 0.422 vs 0.499, 0.338, 0.299). The claim reduces to a change-of-entropy curve fit over 3 sessions. No replication found. Fuzzy linkography reports no validity and its authors say they do not use entropy evaluatively (K21, contested).
- Sakib abstract versus body (85.7% is the human figure). Dunivin abstract says kappa at least 0.6 on 8 of 9 codes; the table recount gives 7.
- Few-shot prompting is not reliably better for coding (OR 0.90, ns) and hurt sub-goal coding (K07).
- Trace validity versus accuracy. Ballon says swapped traces hurt (-18.4 to +3.0%). Valmeekam says corrupted traces train as well as correct ones. Different settings, so the conflict is partly apparent. It shows that trace correctness cannot be assumed to matter (K24).
- Simulated think-aloud from a model is not a stand-in for a human one (K18).
- Zhang's reversal: LLMs matched static shares but problem-driven runs had fewer, not more, problem-solution crossings. The authors say LLMs stay in one space.

Moderators:
- Task type: truncation sensitivity under 10% to over 60% (K13). Coding accuracy math .78 above biology (K07).
- Code granularity: 80.2% to 52.5% from category to subcategory (K06).
- Code rarity and interpretiveness: rare codes gain most from a rationale. Agreement drops as coding becomes more interpretive (K08). Backward chaining only 0.55 and 0.40 ICC3 (K09).
- Hint type: sycophancy 53.9% and consistency 35.5% faithfulness vs unethical 79.4% (d07).
- Judge model: about 13 points (d07). Self-preference above 50% (d16).
- Difficulty: harder tasks, lower faithfulness (c24). Unfaithful traces were longer, not shorter.
- Context: richer context made simulated think-aloud more coherent and more overconfident, not more human (b17).

Interventions that worked: rationale-before-code in LLM coding. Length-matched and shuffled controls to isolate content. Structure guidance from successful traces on ill-structured problems (single source). Interventions that did not work: few-shot examples for coding (not reliably). Outcome RL for faithfulness (plateaued at 28% MMLU, 20% GPQA). Embedding similarity as a stand-in for design meaning (c10).

## 6. Language models

How models behave on these tasks.

As subjects of think-aloud (K18). A model asked to simulate a student's think-aloud is more coherent, wordier and overconfident. Cosine to real utterances 0.16 to 0.19. Local coherence lower than humans by -0.22 and -0.44. Predicting whether the student succeeds: AUC .528 and .572, near chance. More context made it worse. Lesson: simulated protocols are not human protocols.

As designers (K17). GPT-4o prompted as "problem-driven" or "solution-driven" gave different FBS shares as asked (R 9.7 vs 4.3 percent, S 10.6 vs 29.3). So the model follows the prompt's style on static shares. It did not reproduce human-like crossings. Novelty and integrity scores were higher than baseline for both styles (p < .05). Feasibility was higher in all groups. Constraints shrank the differences (PS 8.7 vs 10.4, p = .333). The effect on outcome cannot be separated from length (b13).

As coders. Near human on coarse codes, weak on fine ones (K06, K07, K09). Cost: $74 for 4,947 trials against about 816 human hours (K10). Rationale-before-code helps (K08). Stability is not validity: three GPT-4 runs agreed 0.87 with each other but only 0.44 to 0.50 with humans (c15). Rare events starve reliability (subgoals in 9.0% of trials).

As reporters of their own reasoning (K11 to K13, K23). Written reasoning often hides the cause. Early work: 1 in 426 explanations mentioned a bias that cut accuracy by up to 36%. Reasoning models: 25% and 39%, with an RL plateau. 2026 panels of newer models show 39.7% to 89.9%. The reliance judge is the weak link (kappa 0.26). All these tests use multiple choice, where CoT is often not needed. No test on open-ended design tasks exists.

As targets of coded analysis. Human-derived taxonomies reveal structure. Models use 26% fewer elements on ill-structured problems than humans (K14). Guidance toward successful structures added +9.7 points (strongest models) on ill-structured and +4.4 across all models, versus +1.6 on well-structured. Plan and uncertainty sentences carry the most counterfactual weight (K15). R1 shows a length sweet spot and rumination (K16). Trace content carries signal that length does not (K23: +18.1 to +33.1% for own trace vs -3.9 to +4.2% for length-matched random). But answers can survive corrupted traces in small models (K24).

Facts we lack: no FBS or linkography coding of LLM traces with human-validated reliability and an outcome link (K28). No forced think-aloud versus silent comparison at equal tokens (Luo 2026 is abstract-level only). No faithfulness test on open-ended design. No replication of Li's guidance gain.

## 7. What our agent should take

Schema parts: G guardrails, S states, O operators, memory (section 5 of SCHEMA.md), and the run log (section 6).

### Add now (established)

1. [E] Keep G10 as it is: do not decide from what the trace says. Evidence is now wider: 1 of 426 explanations (Turpin), 25% and 39% (Chen), 39.7% to 89.9% across 12 models (Young), judge-dependent. Strengthen the wording: faithfulness depends on task, hint type and judge, so no rate can be assumed. Schema part: G10. Evidence: a19, b21, a21, b23, d06, d07 (K11, K12). The direction (hidden influences occur) is established. Any single number is single-source.
2. [E] When the agent or a tool codes a trace, require a one-line rationale before each label, one code per segment, and a small closed code set. Schema part: run log (section 6) and any trace-coding tool. Evidence: c13, c14, c15, c16 (K08). The rationale step is established. The code set size is [S] (K06).
3. [E] Do not use a model-simulated protocol as a stand-in for human protocol data, and do not use model-written think-aloud text as a quality signal. Schema part: G10. Evidence: b17, c28 (K18) plus the faithfulness set. The numbers are single-source. The direction agrees with the faithfulness set, so it is a rule.
4. [E] Never test a trace-coding claim without length-matched and shuffled-trace controls. Schema part: G7 (pays for itself at equal tokens). Evidence: d09, d10, c24 (unfaithful traces were longer), K23. Established as method practice. The specific numbers are single-source.
5. [E] A coded process step is not shown to be the cause of the answer until it is removed or swapped. Schema part: G2 and G3. Evidence: d09, d11 (K23, K24).
6. [E] If a trace requirement is added (explain-first, think-aloud), accuracy and item difficulty ordering must hold at equal tokens against the silent arm. Human evidence says plain think-aloud is free in accuracy and costs about 6% time (c03, c04). Explanation helps humans (b02). Transfer to LLMs is untested, so the trace requirement itself enters as a test (U1), and the check is part of every scaffold test.

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Sentence-function codes (plan generation, uncertainty management, self check) on our traces: does a fixed share of planning sentences predict correctness at equal tokens | S/O (trace coding) | [S] | c23, c21, c19 (K15) |
| Problem-space versus solution-space switching: force a problem-restate step and a solution-draft step, count crossings, test whether forced crossings improve quality | S (mode) | [C] | a08-a10, a27, d13 (K17, K27) |
| Structure guidance on ill-structured problems from coded successful traces (Li) | S/O | [S] | b18, b19 (K14) |
| Skip explicit reasoning where truncation changes the answer under 10% of the time | O / G11 | [S] | a20, b22 (K13) |
| Two coder families, flag disagreements for codebook repair | trace coding | [S] | c11, c12, d16 (K20, K26) |
| Hidden-hint probe on our scaffold: does the scaffold raise hint mention rate | G10 | [S] | a19, a21, d07 (K11, K12) |
| Reasoning-length bins as a G11 cap input | G11 / G12 | [S] | c20, d10 (K16) |
| Link density and entropy as a quality signal | none | [C] | a14, d01, d03 (K21). Do not add. Listed only so nobody re-proposes it |

## 8. Concrete tests on our bench

All arms run at equal total tokens (setup cost counted, G7), at least 3 seeds, paired items. Build a 100-trace hand-coded validation set first.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Mixed bench items (ARC and brain-teaser style) | Silent answer vs forced think-aloud trace vs explain-then-answer, equal total tokens | Accuracy. Item-difficulty rank correlation with the silent arm | Small or zero for think-aloud (human r = -.03). Explain arm may help on some tasks. A drop above 3 points kills the trace requirement |
| T2 | 100 hand-coded agent traces | Coder A (model family 1) vs coder B (family 2), each with and without rationale step. Coarse (3 to 8 codes) vs fine codes | Cohen kappa per code vs two humans. LLM-LLM minus LLM-human gap | Rationale about +0.08 kappa (Dunivin). Fine codes drop sharply (as 80.2% to 52.5%) |
| T3 | Ill-structured items vs well-structured items | Plain vs scaffold prompt with structure guidance from successful traces (Li-style) | Accuracy. Share of Li elements per trace | About +4 points ill-structured, +1.6 well-structured if it replicates. Abandon if under +2 on ill-structured |
| T4 | Items with a planted hint (suggested answer, metadata) | Plain vs scaffold. The scaffold adds "state what influenced you" | Hint mention rate among items where the answer changed. Hint-follow rate | Plain 25% to 40% mention. Test whether the scaffold raises it without losing accuracy |
| T5 | Items with a coded process step | Original trace vs length-matched random vs shuffled vs swapped trace | Accuracy at the full-trace decile vs controls | Own trace +18 to +33%, controls near 0 (Ballon). Tells us if coded content matters |
| T6 | Design or open-mode items (open briefs) | Plain vs forced problem-first-then-solution alternation vs solution-first | Count of PS and SP crossings. Quality by code-based checks plus a no-authorship judge (G5). Novelty by running (G8) | Zhang suggests LLMs under-cross. Unknown whether forced crossings help. Guo 2024 effect is fragile |
| T7 | Truncation items | Truncate the trace at 0, 25, 50, 75, 100% and force an answer | Answer change rate. Area over curve | Task-dependent (under 10% to over 60%). Tasks with low AOC should skip long reasoning |
| T8 | Our own trace logs | Per-trace reasoning length bins | Accuracy by bin | Rise-peak-fall shape (R1). Gives the G11 cap |
| T9 | Repeated extraction | 5 repeats of concept or network extraction on one trace | Variance of degree and connectivity | Unreliable repeats expected (Kelly and Gero). Block network metrics if variance is high |

## 9. What does not transfer, and why

- Human non-reactivity (r = -.03) is about humans solving a problem aloud versus in silence. An LLM's thinking is its text. A forced trace changes the computation, so non-reactivity cannot be assumed. It is tested (T1).
- Human design-protocol effects (expert versus student, blindfolded versus sighted, entropy and outcome) come from single small studies (6 architects; 3 architects) with no replication. Do not import them (K22, K25).
- FBS issue shares. FBS describes how people talk about artefacts (function, behaviour, structure). Reasoning traces on puzzles have no function-behaviour-structure split. If used, FBS is a design-mode tool only, not for ARC-style tasks.
- Linkography and entropy as quality measures. The only opened original shows the opposite sign for whole-session entropy. Embedding-linked graphs are unvalidated and can link unrelated moves (K19, K21).
- Faithfulness numbers from multiple-choice hints. They test whether the trace reports a planted hint, not whether the trace shows the true cause of an open-ended design decision (K12 limits).
- Human-with-AI co-design results (Guo 2024, Wang 2025) measure AI helping humans, five per cell or 48 master's students, with no protocol coding in Wang. They do not show that our agent benefits from forced problem-solution crossings.
- Model-simulated protocols stand in for no human data (K18).
- Reasoning-model statistics from R1 and 3B models (c20, c21) do not carry to every model. Training-time findings (Gandhi priming) concern training, which our scaffold does not do.
- Scale of effect. Many effects are percentages on one lab's tasks. No general effect size across tasks exists.

## 10. Open questions

1. Does coding agent traces with a fixed human-derived scheme (FBS issues or Li's 28 elements) predict correctness at equal tokens (K28)?
2. What is the chance-corrected agreement of an LLM coder on FBS codes for design talk, per code, against two trained humans?
3. Is Zhang's reversal real in other models with unrevealing prompts, and do forced crossings improve design quality?
4. Does non-reactivity hold for LLMs at equal tokens (silent versus think-aloud versus explain)?
5. How faithful are current reasoning-model traces on open-ended and ill-structured tasks, and does a scaffold raise the mention rate of hidden influences?
6. The original human numbers behind the LLM comparisons (Chen 2023, Jiang, Gero and Yen 2014, Dorst and Cross 2001) were not opened. What are they?
7. Does anyone replicate linkography or entropy as predictors of design outcome? Do the 2023 to 2026 LLM-linkography papers (a24 titles) give validity numbers?
8. Fox et al. full-text moderators: do any design tasks appear, and how does instruction wording moderate?
9. Does LLM-LLM coder agreement above LLM-human indicate a shared bias, and does mixing families fix it? Only indirect evidence (Pombal) exists.
10. Does Li's trace guidance replicate outside the authors' pool?
11. Is the faithfulness spread (39.7% to 89.9%) explained by hint type, model family or judge choice? A regression on scale gave R2 0.07 (d07).

## 11. Sources

[V] opened and read this session. [M] snippet only. "Abstract only" means only the abstract page was opened and no numbers beyond it are claimed.

[V] Gero, Kan, Pourmohamadi (2011) Analysing design protocols: development of methods and tools. https://human.designsociety.org/download-publication/32332/Analysing+Design+Protocols%3A+Development+of+Methods+and+Tools (a01-a04, a23, b05, b06)
[V] Hay, Duffy, McTeague, Pidgeon, Vuletic, Grealy (2017) A systematic review of protocol studies on conceptual design cognition. https://doi.org/10.1017/dsj.2017.11 and https://www.cambridge.org/core/product/identifier/S2053470117000117/type/journal_article (a05, a06, a25, b07-b09)
[V] Hay et al. (2017) Towards a shared ontology. https://doi.org/10.1017/dsj.2017.6 (a07)
[V] Zhang, Gu, Chen, Ding, Chai, Fan (2025) Leveraging LLMs to emulate the design processes of different cognitive styles. https://openaccess-api.cms-conferences.org/articles/download/978-1-964867-39-7_12 and https://doi.org/10.54941/ahfe1006042 (a08-a10, a26, a27, b11-b13)
[V] Sakib, Hurst, Safayeni (2026) Evaluating the performance of LLMs in taxonomic classification of design questions. https://doi.org/10.1017/S0890060426100250 and https://www.cambridge.org/core/product/C354297FB0A05B03DF61B5857F4BDAD5/core-reader (a11, a12, a22, b14, b15, c05-c07, d04, d05)
[V] Kelly and Gero (2025) Semantic and network analysis of design protocols. https://doi.org/10.1017/pds.2025.10301 and https://www.cambridge.org/core/product/8D1C149E4A72F84D30E5DCD28DAA5ED2/core-reader (a13, b16, c09)
[V] Kan and Gero (2007) Can an objective measurement of design protocols reflect the quality of design outcomes? (ICED07). https://www.designsociety.org/download-publication/25329/can_an_objective_measurement_of_design_protocols_reflect_the_quality_of_design_outcomes (d01, d02)
[M] Kan and Gero (2007) Comparing entropy measures of idea links in design protocols (AI EDAM). https://doi.org/10.1017/s0890060407000339 (a14)
[V] Smith, Kreminski et al. (2025) Fuzzy Linkography. https://arxiv.org/html/2502.04599v2 (d03)
[M] Dorst and Cross (2001) Creativity in the design process. https://doi.org/10.1016/s0142-694x(01)00009-6 and https://oro.open.ac.uk/3278 (a15, d15)
[M] Ericsson and Simon (1980, 1984/1993) Verbal reports as data; Protocol analysis. https://mitpress.mit.edu/9780262550239/protocol-analysis/ (a16, b24)
[M] Nisbett and Wilson (1977) Telling more than we can know. https://doi.org/10.1037/0033-295X.84.3.231 (a17, b25)
[V] Fox, Ericsson, Best (2011) Do procedures for verbal reporting of thinking have to be reactive? https://pubmed.ncbi.nlm.nih.gov/21090887/ and https://doi.org/10.1037/a0021663 (b01, b02, c04). [M] full text https://core.ac.uk/download/74368816.pdf (a18, d14)
[V] Schooler (2011) comment. https://pubmed.ncbi.nlm.nih.gov/21355632/ (b03)
[V] Ericsson and Fox (2011) Thinking aloud is not a form of introspection. https://pubmed.ncbi.nlm.nih.gov/21355633/ (b04)
[M] Kuusela and Paul (2000) concurrent and retrospective protocols. https://doi.org/10.2307/1423365 (b26)
[M] Waterman and Newell (1971) PAS-II. https://doi.org/10.1016/0004-3702(71)90003-3 (c29)
[M] Dinar et al. (2015) Empirical studies of designer thinking (abstract). https://doi.org/10.1115/1.4029025 (b10)
[M] Crossref listing of LLM and linkography titles, 2023 to 2026. https://doi.org/10.1080/10447318.2026.2662519 (a24)
[V] Turpin, Michael, Perez, Bowman (2023) Language models don't always say what they think. https://arxiv.org/abs/2305.04388 (a19, b21, c25)
[V] Lanham et al. (2023) Measuring faithfulness in chain-of-thought reasoning. https://arxiv.org/abs/2307.13702 (a20, b22)
[V] Chen, Benton et al. (2025) Reasoning models don't always say what they think. https://arxiv.org/abs/2505.05410 (a21, b23, c24)
[V] Walden (2026) Reasoning Models Will Blatantly Lie About Their Reasoning. https://arxiv.org/html/2601.07663v1 (d06)
[V] Young (2026) Lie to Me. https://arxiv.org/html/2603.22582v1 (d07)
[V, abstract only] Lewis-Lim et al. (2025) Analysing Chain of Thought Dynamics. https://arxiv.org/abs/2508.19827 (d08)
[V] Ballon et al. (2026) Probing the Trajectories of Reasoning Traces. https://arxiv.org/pdf/2601.23163 (d09, d10)
[V, abstract only] Valmeekam et al. (2025) Beyond Semantics. https://arxiv.org/abs/2505.13775 (d11)
[V, abstract only] Luo et al. (2026) Capable yet Parsimonious. https://arxiv.org/abs/2609.26637 (d12)
[V] Guo, Yin, Sun, Chen (2024) Problem-solution co-evolution in human-GAI co-design. https://doi.org/10.21606/drs.2024.983 (d13)
[V] Pombal, Rei, Martins (2026) Self-Preference Bias in Rubric-Based Evaluation. https://arxiv.org/pdf/2604.06996 (d16)
[M] Family-mixing judge summaries. https://tldr.takara.ai/p/2604.11589 (d17)
[M] Style over Substance: Distilled Language Models Reason. https://arxiv.org/html/2504.01738v3 (d18)
[V] Wang, Khinvasara, Creijghton et al. (2025) Enhancing designer creativity through human-AI co-ideation. https://www.cambridge.org/core/product/BCC2CBE43EECE6F0D937BBC0D2F44868/core-reader (b27)
[V] Wurgaft et al. (2025) Scaling up the think-aloud method. https://arxiv.org/abs/2505.23931 (c01-c03)
[V, abstract only] Sakib (2024) Automating Protocol Analysis with Generative AI. https://uwspace.uwaterloo.ca/items/40187e22-c68c-46d5-af92-747931aa7a79 (c08)
[V] Lee, Jin, Hyun (2026) Beyond Semantic Similarity. https://arxiv.org/abs/2603.07611 (c10)
[V] Tajik et al. (2026) Disagreement as Data. https://arxiv.org/abs/2601.12618 (c11, c12)
[V] Dunivin (2024) Scalable Qualitative Coding with LLMs. https://arxiv.org/abs/2401.15170 (c13, c14)
[V] QualiGPT authors (2024) When Qualitative Research Meets LLM. https://arxiv.org/abs/2407.14925 (c15)
[V] Kirsten, Buckmann, Mhaidli, Becker (2024) Decoding Complexity. https://arxiv.org/abs/2403.06607 (c16)
[V] Journal of Learning Analytics (2026) LLMs for automated coding of STEM think-aloud. https://learning-analytics.info/index.php/JLA/article/view/9025 (c17, c18)
[V] Marjanovic, Patel et al. (2026) DeepSeek-R1 Thoughtology. https://arxiv.org/abs/2504.07128 (c19, c20)
[V] Gandhi, Chakravarthy et al. (2025) Cognitive Behaviors that Enable Self-Improving Reasoners. https://arxiv.org/abs/2503.01307 (c21, c22)
[V] Bogdan, Macar, Nanda, Conmy (2025) Thought Anchors. https://arxiv.org/abs/2506.19143 (c23)
[V] Kim et al. (2026) What Did the AI Take On? https://arxiv.org/abs/2610.06328 (c26)
[V] Li, Mo, Tang et al. (2026) HugAgent. https://arxiv.org/abs/2510.15144 (c27)
[V] UXCascade authors (2026) UXCascade. https://arxiv.org/abs/2601.15777 (c28)
[V] Borchers, Vie, Azevedo (2026) LLMs as students who think aloud. https://arxiv.org/abs/2602.01015 (b17)
[V] Li, Kargupta, Wang et al. (2025) Cognitive foundations for reasoning and their manifestation in LLMs. https://arxiv.org/abs/2511.16660 (b18-b20)
