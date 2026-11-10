# Critique: A05.06 Productive failure (cross-check)

## Numbers re-opened this session (arXiv full text)
Confirmed as recorded:
1. Puech et al. (arXiv 2410.03781): RSMs 2.34 / 1 / 1.34 / 1.34; PF score 3.67/1.33/4.00/3.67 (Consistency) and 4.00/0.44/4.00/3.11 (Country); state tracing F1 0.77; field p=.046 and p=.05, 2.6 RSMs, N=17. (a21, a22, b16, c01-c03)
2. Rotter et al. (arXiv 2605.15850): N=105, RL vs Always t(71)=2.51, p=.014, d=0.59; RL vs Never t(67)=-0.30, d=-0.07; requests 11.25/2.46/0; metacognitive gain F(2,87)=0.86, p=.425; metacognitive accuracy t(71)=2.32, p=.023, d=0.54. (a23, b19, c04)
3. Reflexion (2303.11366): 130 of 134 ALFWorld tasks; +22%, +20%, +11% headline gains; WebShop no gain over 100 environments. (c13, c26)
4. ExpeL (2308.10144): ALFWorld round table 40.3-54.4 (ReAct+Reflexion), 54.5-60.4 (ExpeL retrieve), 59.0-64.2 (ExpeL+Reflexion) matches c16. The PDF row labels are offset in text extraction, so the mapping rests on the paper's table caption order.
5. Huang et al. (2310.01798): GPT-4-Turbo GSM8K 91.5 to 88.0, CommonSenseQA 84.0 to 81.5; GPT-3.5 GSM8K 74.7% kept first answer; oracle GPT-3.5 GSM8K 75.9 to 84.3, CommonSenseQA 75.8 to 89.7. Confirmed. The GPT-4 HotpotQA oracle figure (49.0 to 59.0 in c17) was not cleanly readable in the extraction; a GPT-4 CommonSenseQA row (95.5/82.0) was seen and is not recorded in c17.

## Corrections
- Rotter: c04 and b19 say nothing about a secondary result. RL participants made fewer mistakes than Never (t(67)=2.05, p=.047, d=0.51) but this vanished after controlling for gender (p=.513). Do not cite as a benefit. Metacognitive accuracy is vs Always only.
- Puech: baseline RSMs in the field study are described as "about 1" or "lower" in different lines. The paper text gives only 2.6 for StratL and p=.05; the baseline mean was not confirmed. Treat "about 1" as simulation-only.
- Evidence a22/b16/c03 and a21/b17/c01-c02 are the same two studies recorded several times. They count as ONE independent source (K11).
- a11, b01, c06 (meta-analysis) are all abstract or secondary text; the 0.87 bias-adjusted figure comes only from the authors' own estimate. Counted as one source.
- c10 attributes the Nachtigall paper to "tenth graders"; b05 says it covers knowledge about science. Population details for Nachtigall are not checked (not re-opened).

## Contradictions between sources
- Original PF studies (Kapur, quasi-experimental) vs independent replications (Nachtigall, Loibl and Leuders, Mazziotti, Glogger-Frey): many null or reversed. Explanations offered (few attempts, no typical errors, domain outside STEM, young children) are post hoc. No study manipulated them.
- Confidence: Kapur 2009 PF students had low confidence (1.22/4), Nachtigall PF students had higher perceived competence after phase 1. Not reconciled.
- Meta-analysis (g=0.36, mostly positive) vs replication sequence (mostly null): consistent only if the meta-analysis includes the original lab's studies heavily. Lab share not counted.
- Vicarious failure vs PF: Kapur 2014 (PF better on effort) vs Braas 2025 (VF-high >= PF, ns). Brand 2024 not read.

## Weak spots
- Almost no PF study is a randomised, delayed-test design at adequate power outside the originator lab.
- No study here tests PF on an LLM agent's reasoning. All LLM evidence is of three kinds: PF-steered tutors (fidelity only), student-AI timing, and agent self-reflection (Reflexion, ExpeL) which is only an analogy.
- Reflexion and ExpeL need a success signal; Huang et al. show that without one the "lessons" step does not help. The schema's lessons memory is only as good as its verifier.
- Several key records were abstract-only: Kapur 2011, Kapur 2014, Schwartz and Martin 2004 (search snippet only), Sinha and Kapur 2021, Bastani 2025, Brand 2024.
- Rotter pilots were n=9 and n=7; the RL policy is trained on a simulated student.

## Seen only in snippets or abstracts
a05, a09, a10, a11, a12, a14, a19, a27, a29, b20, c06, c08, c10-c12, c19, c22, c27.

## GAPS
1. What are the study-level effects in Sinha and Kapur (2021) by lab, design fidelity, and domain, and what fraction of the 53 studies come from the originator group?
2. Does attempt-first help an LLM agent on hard reasoning tasks at equal tokens, when the lessons step is a comparison of its own attempts to a correct answer?
3. How much does the lessons step depend on a verifier? Run attempt-first memory with oracle, noisy, and no ground-truth check.
4. Is the number of distinct candidate methods generated in the attempt phase a causal driver (Kapur, Saba, Roll 2023) or only a correlate, and can we force diversity in an agent?
5. Is observing a supplied failed attempt (vicarious failure) as good as the agent's own failed attempt for lessons memory (Kapur 2014; Braas 2025; Brand 2024)?
6. What are the exact numbers in Schwartz and Martin (2004) and Kapur (2012, 2014) that the series is built on? These were never opened.
7. Which published LLM study tests attempt-first versus instruction-first on model accuracy (not tutoring fidelity or student outcomes) in 2024-2026?
8. Do the replication failures (Nachtigall, Loibl and Leuders) share a design feature (few attempts, wrong domain, data presentation) that we can check for in agent traces?
9. Does lessons-memory quality degrade calibration (confidence rising after a failed-then-instructed cycle), as Nachtigall's perceived-competence drop suggests?
10. What is the long-term retention effect of PF (delayed tests beyond a week) in larger samples than Suriyaarachchi's 16?


## Gap search results

Evidence is in `evidence_d.jsonl` (d01-d18). Claims K01, K03-K08, K17 and K19 were updated and K21-K26 added.

**Closed or mostly closed**
- Gap 4 (is method diversity a cause?). Partly closed. Kapur, Saba and Roll (2023) is an association (RSMs F=62.6 and 105.5; d04). Braas et al. (2025, N=152, random assignment) manipulated diversity by supplying five attempts covering all four canonical components versus two: VF-high beat VF-low (d=0.64) and DI (d=0.65) (d05). So diversity is causal when supplied. Own-generation count is still a correlate. Forcing diversity in an agent was not tested anywhere.
- Gap 5 (supplied failure vs own). Partly closed for humans: VF-high matched PF (d=0.29, ns) but only when the attempts covered all components. For LLMs there is only fine-tuning evidence (LeMa, d16). The Learning and Instruction 2025 paper on learner characteristics in PF and VF (10.1016/j.learninstruc.2024.102052, the "Brand" work) returned 403 and was not read.
- Gap 6 (exact numbers). Schwartz and Martin 2004 fully opened (d01-d03): Exp 1 60.8% vs 29.2% with the resource, 30.4% vs 32.0% without. Kapur 2012 and 2014 are NOT opened (paywalled or 403); only an abstract (d18) and secondhand solution counts from Braas (d06).
- Gap 3 (verifier dependence). Mostly closed for prompting-style agents: Reflexion gives reliable +11, noisy -3, none -8 (d14); Huang (earlier) and Kamoi (d15) agree; LEAP uses ground truth (d12). No study ran all three conditions on one task with the same lessons step.
- Gap 8 (shared feature of failures). Answered: none (K24). Nachtigall made about 4 ideas per group, so "few attempts" is not the common cause; K05 was corrected. Checkable in traces via attempts, distinct methods and component coverage.

**Still open**
- Gap 1: the Sinha and Kapur (2021) full text is blocked (Sage 403). Only the abstract was read (d10). Lab share, study-level effects and per-domain values remain unknown. The abstract adds: grades 2-5 and domain-general skills favoured instruction-first; quasi-experimental studies add to the effect.
- Gaps 2 and 7: no study found that compares attempt-first with instruction-first on LLM accuracy at equal tokens (K23). LEAP, Reflexion, ExpeL and multi-attempt RL are analogies. The shared WebSearch budget ran out and the arXiv, Semantic Scholar and OpenAlex APIs were rate limited, so this is absence in a limited search.
- Gap 9: no LLM evidence on calibration after a lessons cycle. Only Nachtigall's student data (d08).
- Gap 10: no new delayed-retention data. Schwartz and Martin's one-year test has no control (d03).

**Corrections to earlier records**
- K05 said replications failed with few attempts. Nachtigall contradicts that (3.93 ideas per group).
