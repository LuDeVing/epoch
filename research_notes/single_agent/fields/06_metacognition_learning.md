# Metacognition and learning science: what it offers one thinking agent

Marks: [V] source seen this session (often abstract or summary level, so exact numbers still deserve a check in the paper); [M] from memory, re-check. [ours] is our own measurement from `00_PLAN.md`.

## 1. What the field studies

Metacognition is thinking about thinking. Nelson and Narens (1990) split a mind into an object level (doing the task) and a meta level (a model of the object level). Information flows up as monitoring (how am I doing?) and down as control (keep going, switch, stop, ask for help) [M]. Human work covers feeling of knowing before answering, feeling of rightness after a fast answer, judgments of solvability, and the sense of warmth near a solution. Learning science asks a different question: which practice makes knowledge stick and transfer. Its answers decide what an agent should store (worked examples, lessons) and when it should be shown guidance (only when it is a novice at this kind of problem). Both halves fit our plan well, because the plan is a router that must monitor, then control.

## 2. Core findings

**F1. A fast answer comes with a feeling of rightness (FOR), and a weak FOR triggers rethinking.** Thompson, Prowse Turner and Pennycook (2011) [V, via secondary descriptions]: FOR rates how right an intuitive answer feels, is raised by fluency (the answer came easily), and predicts whether people later change it. Weak FOR leads to more analysis, strong FOR ends thinking early. Strength: replicated lab effect, moderate. It is the human version of our "trust the first answer until a check fails", and it says the trigger is a signal, not a schedule.

**F2. Warmth tracks closeness to the solution, but only loosely.** Metcalfe and Wiebe (1987) [V, via secondary]: warmth ratings rise gradually on step-by-step problems and jump on insight problems. Later work (Hedne, Norman and Metcalfe 2016) found no warmth difference between solutions people called insight and non-insight [V, secondary]. Strength: weak to moderate. Lesson: a self-rated "I am getting close" is a noisy signal. Use it as a hint, not a gate.

**F3. Monitoring and control can come apart, in people and in models.** Nelson and Narens' own design separates them [M]. A 2026 benchmark found withdraw decisions and error monitoring correlate only r = .17 across 20 LLMs, with a wide interval [V, abstract]. A model can know it is wrong and still not act.

**F4. Problem solving before instruction beats instruction first (productive failure).** Sinha and Kapur (2021): meta-analysis of 53 studies, 166 comparisons, STEM concepts [V, abstract level via press]. Press reports about two to three times the gain, but I did not see exact effect sizes. Needs enough prior knowledge, tasks hard but not impossible, and a consolidation phase after the struggle. Strength: moderate, mostly school and university samples, some publication-bias risk.

**F5. Retrieval beats restudy (testing effect), more so with feedback.** Rowland (2014) meta-analysis: average g about 0.50 over 159 effect sizes, and larger with feedback (0.73 vs 0.39) [V, secondary; check the paper]. Bjork's "desirable difficulties" frames it: slower, harder practice gives better long-term retention and transfer, while easy practice feels better and works worse [M]. Strength: strong, many replications. Warning: this is about human forgetting. A model does not forget what is in its context.

**F6. Worked examples help novices; the same help hurts experts (expertise reversal).** Sweller, Ayres, Kalyuga and Chandler (2003) [V]: instruction that helps low-knowledge learners loses value or does harm for experienced ones, because it duplicates what they already know and adds load. Fix: fade guidance as skill grows [V, secondary]. A meta-analysis on maths found a worked-example effect of g = 0.48 across 181 effect sizes, with correct examples better than incorrect ones and self-explanation prompts adding nothing extra there (Barbieri et al. 2023) [V, secondary]. Strength: strong for novices, moderate for the reversal.

**F7. Self-explanation helps, mostly when it asks for reasons.** Bisra et al. (2018): g = 0.55 over 69 effects from 64 reports [V]. Prompts that ask learners to conceptualize did best (g about 0.87 in one summary), while generic metacognitive prompts were weak (g about 0.19, not significant) [V, one secondary table, unsure of mapping]. Chi et al. (1989, 1994) is the origin [M]. Strength: strong overall. Note the finding that vague "think about your thinking" prompts do little.

**F8. Experts monitor their own comprehension and sort problems by deep structure.** Chi, Feltovich and Glaser (1981) [V in plan]. Experts also notice when a problem does not fit, which is the entry to an impasse. Strength: strong, small samples.

## 3. Mechanisms an agent can run

**M1. Pre-solve feeling of knowing (FOK) plus a cheap probe.**
- Trigger: start of every problem, before any expensive work.
- Action: ask for a one-line FOK ("can I solve this: yes, maybe, no, and why?"). Then run the 4 to 5 plain probe attempts from the plan. Compute two numbers: agreement among attempts (a machine FOR) and the stated FOK.
- Check: at equal tokens, does routing on agreement plus FOK beat routing on agreement alone? Report AUROC of each signal against final correctness, per suite.
- Evidence: Kadavath et al. 2022, models predict P(IK) well but calibrate poorly out of domain [V]; Xiong et al. 2023, stated confidence is overconfident, consistency among samples helps, black-box methods are close to white-box (AUROC 0.52 vs 0.61) [V]; the 2026 metacognitive harness, FOK/JOL signals lifted pooled accuracy 48.3 to 56.9 on Sonnet-4.6 [V, abstract, authors' claim].
- Risk: the FOK adds a call. If it only restates agreement, drop it. On easy items, stated confidence is high and wrong in the cases that matter.

**M2. Feeling of rightness gate on the first answer (agreement as FOR).**
- Trigger: after the probe.
- Action: if attempts agree and any available check passes, stop (CONVERGE). If they agree but no check exists, ship without added doubt. Doubt runs only on disagreement or a failed check. Log the FOR bucket.
- Check: error rate in the high-agreement bucket vs the low bucket. A gate is worth keeping only if the high bucket is right at least as often as plain. Test BrainTeaser: the gate must not lose more than 1 point to plain.
- Evidence: Thompson 2011 [V]; our BrainTeaser result, forced doubt cost accuracy [ours]; semantic entropy flags confabulation via meaning-level disagreement (Farquhar et al., Nature 2024) [V].
- Risk: consistent wrong answers pass the gate. The Nature authors say a consistent mistake is not caught [V]. Pair with a real check wherever one exists.

**M3. Impasse detector with explicit stop and switch rules.**
- Trigger: any of these after a round: no attempt passes the check; the last two rounds changed nothing in the answer set; the same error repeats; spend passes a set fraction of the budget.
- Action: write a one-line state ("tried A, B; failing because C"), then move one rung up the plan's ladder (re-check, resample, re-read, helper problem, diverge). Never retry the same move twice. Also run a stop test: if two independent passing attempts agree, stop.
- Check: log ladder step reached and tokens. Compare solved-per-token against a plain loop with the same budget. Also count "wasted rounds" (rounds that repeat a prior move).
- Evidence: Ohlsson impasse theory [M]; Callaway et al. 2024 formalise metamemory as a meta-level decision process with cost-benefit stopping [V, via a 2025 workshop paper citation]; overthinking and underthinking in reasoning models, models spend too much on easy items and too little on hard ones (arXiv 2505.00127, ThoughtTerminator 2504.13367) [V, snippet].
- Risk: a switch rule that fires too early replays our heavy-scaffold failure. Keep the detector rule-based, not a model opinion, and cap setup tokens.

**M4. Judgment of solvability, with abstain as a real output.**
- Trigger: when the budget share used crosses a threshold with no passing candidate, or when FOK is "no" and attempts disagree.
- Action: choose among: continue, escalate one rung, return best candidate with a flag, or abstain. Abstention must cost something in the scoring or the agent will over-abstain (our ARC scaffold abstained on 4 and our BrainTeaser scaffold abstained everywhere [ours]).
- Check: accuracy at coverage. Plot accuracy against fraction answered and compare with plain best-of-N.
- Evidence: Kadavath 2022 [V]; Metacognitive Monitoring Battery, selective-sensitivity models exist but are not the most accurate ones, so accuracy does not predict self-monitoring [V, abstract].
- Risk: highest of all mechanisms. Abstain only when an answer is not required by the harness.

**M5. Explain-to-yourself on failure, not on success (self-explanation, targeted).**
- Trigger: a failed check or a disagreement between candidates.
- Action: write why the failing candidate failed in terms of the rule, using the real check output ("I predicted X, got Y, so my rule misses Z"). Feed that, and only that, into the revision call.
- Check: pass rate after one revision with the explanation vs revision from raw output alone, at equal tokens.
- Evidence: self-explanation g = 0.55 [V]; conceptual prompts stronger than generic metacognitive ones [V, secondary]; Reflexion, 91% pass@1 on HumanEval vs 80% for GPT-4 [V, abstract, with environment feedback]; Greenblatt's one revision round on ARC [V in plan].
- Risk: Huang et al. 2023 show that without an outside signal, self-correction does not help and can hurt [V]. Run it only when a real output exists. In a pure-opinion setting, skip.

**M6. Expertise-adaptive scaffolding (the reversal rule for prompts).**
- Trigger: before building the prompt for a problem, using the router class and the memory hit rate.
- Action: if the memory holds supported lessons or worked solutions for this class, show one or two correct worked examples and a short rule list (novice mode). If the agent has solved many of this class with plain attempts (high pass rate), show nothing extra and run bare (expert mode). Fade as the class pass rate rises.
- Check: three arms at equal tokens, per class: bare, fixed scaffold, adaptive. The adaptive arm must match bare where bare is strong.
- Evidence: expertise reversal [V]; worked examples g = 0.48 [V, secondary]; correct examples beat incorrect ones [V, secondary]. This explains our data: the schema hurt where the model was already "expert" (word puzzles at 92%).
- Risk: the model's "expertise" is per task type and is measured, not assumed. Misjudging it reproduces our losses.

**M7. Store lessons after solving; retrieve with a test, not by rereading (look-back memory with retrieval practice).**
- Trigger: end of a problem (write), start of a new problem of the same class (read).
- Action: write one-line lesson, trap, helper problem. On a new problem, do not paste the lesson. Ask the agent to predict what the trap will be, then reveal the lesson and compare. Mark a lesson "supported" only after it helped twice on different problems.
- Check: held-out problems, memory on vs off, equal tokens. Also memory with raw reread vs memory with predict-then-reveal.
- Evidence: the testing effect and desirable difficulties are human forgetting findings [V, secondary]. Evidence for a model-side benefit is weak [M]. Treat the predict-first step as a design guess.
- Risk: lessons add noise and tokens. Cap at a handful. Failed-lesson contamination is a real risk (see M8).

**M8. Productive failure as a stored contrast, not as a training schedule.**
- Trigger: when a problem was solved after at least two failed attempts.
- Action: store the failed attempt, why it was plausible, and the fix, as a contrast pair. Show it on the next same-class problem only after the new problem's first attempt has failed.
- Check: lesson shown before the first attempt vs after a failure, at equal tokens, on held-out items.
- Evidence: Sinha and Kapur 2021, struggle first then consolidation [V, press level]. The ordering effect for a model is untested [M].
- Risk: showing a wrong approach first can anchor the model on it. Barbieri et al. found correct examples beat incorrect ones for novices [V, secondary].

## 4. Evidence on LLMs and AI agents (2022 to 2026)

- **Models know a fair amount about what they know.** Kadavath et al. 2022: P(True) and P(IK) are informative, with better self-evaluation after seeing many own samples [V, abstract]. Strength: strong for large models on factual and multiple-choice items.
- **Stated confidence is overconfident.** Xiong et al. (ICLR 2024): verbalized confidence overconfident; sample consistency and aggregation help; hard professional-knowledge tasks stay hard [V]. Strength: strong, five models, five dataset types.
- **Meaning-level disagreement detects confabulation.** Farquhar et al., Nature 2024: semantic entropy beat earlier methods on six models; misses consistent errors [V]. Strength: strong, with the limit noted.
- **Self-correction without outside signal fails.** Huang et al., ICLR 2024 [V]. Strength: strong, replicated by many follow-ups [M].
- **Self-evaluation is biased toward the model's own text.** Panickssery et al., NeurIPS 2024 oral: models recognise and favour their own output, and recognition strength tracks bias, shown causally by fine-tuning [V]. This is a direct reason for the plan's anchored tie-break (derive the expected output before seeing candidates) and for judging with a different call or a real check.
- **Metacognitive prompting.** Wang and Zhao, NAACL 2024: a five-stage introspective prompt (understand, judge, evaluate, decide, confidence) beat standard and chain-of-thought prompts on ten language-understanding datasets with Llama2, PaLM2, GPT-3.5 and GPT-4 [V, abstract]. Strength: weak to moderate. Tasks are classification; gains are small by my memory [M]; no equal-token control seen. Treat as a prompt style, not as evidence for our router.
- **Monitor-control harnesses.** A 2026 harness on Sonnet-4.6 (FOK before solving, JOL after each attempt, control policy for trust, retry or aggregate) reports pooled accuracy 48.3 to 56.9 on HLE-Verified, LiveCodeBench v6 and R-Bench-V [V, abstract, authors' claim, token cost not checked] (arXiv 2605.14186). Closest match to our plan. MetaCrit (2507.15015) uses four roles built on Nelson and Narens and reports better truthfulness [V, abstract], but it is a multi-agent scheme with no equal-token control seen. A theory paper (2511.04341) argues pipelines lack a pre-generation monitoring phase [V, snippet]. An ICML 2026 poster applies Nelson and Narens to an LLM agent [V, title only].
- **Monitoring and control dissociate.** Metacognitive Monitoring Battery (2604.15702), 20 LLMs, 10,480 evaluations: three profiles (blanket confidence, blanket withdrawal, selective), accuracy rank a poor guide to monitoring quality, r = .17 between monitoring and regulation [V, abstract].
- **Effort is misallocated.** Reasoning models overthink easy items and underthink hard ones (2504.13367, 2505.00127) [V, snippet]. This supports a router that sets effort from outside the model's own length habits.
- **Humans versus LLMs.** Steyvers and Peters, preprint 2504.14045: mixed alignment, many differences remain [V, abstract]. Steyvers et al., Nature Machine Intelligence 2025: gap between what models know and what users think they know [V, bibliographic only].
- **Learning-science methods on LLMs.** I found no controlled study applying productive failure, expertise reversal, or desirable difficulties to prompting an LLM at equal tokens. Searching was shallow; treat this as a gap, not a proof of absence.

## 5. What does not transfer, and where it could hurt

- **Does not transfer:** forgetting curves and spacing (the context window does not decay; spacing helps only for fine-tuning or memory retrieval), motivation and effort feelings, embodied "gut" sensations, fatigue, and the social part of productive failure (small-group work was a condition in the human studies).
- **Partly transfers:** FOR and FOK. A model has no felt fluency, but agreement across samples and token-level confidence play the same role. Stated confidence is a weaker proxy than agreement.
- **Hurts, given our data:**
  - Any rule that adds doubt on a schedule. BrainTeaser forced doubt cost the most [ours]. The FOR gate (M2) exists to prevent this.
  - Abstain and "I am stuck" signals from the model itself. The ARC scaffold abstained on 4 of 12 and BrainTeaser's full scaffold abstained everywhere [ours]. Use rule-based impasse detection first.
  - Added setup calls (FOK, explanation, memory reveal). A 0% score came from setup eating the budget [ours]. Each must pay for itself.
  - Self-judgment without a check. Self-preference and the Huang result both say a model judging its own answers is unreliable [V].
  - Worked examples shown to a strong model. Expertise reversal predicts a loss where plain is already ~92% [V, ours].
  - Showing failed attempts early. Can anchor the model on a bad approach.

## 6. Open questions

1. Does FOK add anything over sample agreement for our small model? Test with AUROC on each suite.
2. Where is the line between novice and expert for a model? Per-class plain pass rate is the natural measure; needs calibration on at least ~20 problems per class.
3. Does predict-then-reveal for stored lessons beat plain reread, for a model? Untested.
4. Can the impasse detector be fully rule-based and still catch the useful switches?
5. Does the 2026 harness gain survive an equal-token comparison with best-of-N? The abstract does not say.
6. Are lessons from failed attempts helpful or anchoring for a small model?

## 7. References

1. Nelson TO, Narens L (1990). Metamemory: a theoretical framework and new findings. Psychology of Learning and Motivation 26. [M]
2. Thompson VA, Prowse Turner JA, Pennycook G (2011). Intuition, reason, and metacognition. Cognitive Psychology 63. Seen only through citing papers, e.g. https://hrcak.srce.hr/en/219803 [V, secondary]. Journal name from memory [M].
3. Metcalfe J, Wiebe D (1987). Intuition in insight and noninsight problem solving. Memory and Cognition. Discussed in https://pmc.ncbi.nlm.nih.gov/articles/PMC5005374/ [V, secondary].
4. Hedne MR, Norman E, Metcalfe J (2016). Intuitive feelings of warmth and confidence in insight and noninsight problem solving of magic tricks. Frontiers in Psychology. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5005374/ [V]
5. Sinha T, Kapur M (2021). When problem solving followed by instruction works: evidence for productive failure. Review of Educational Research. DOI 10.3102/00346543211019105 [V, press coverage only: https://www.weforum.org/stories/2021/09/students-who-productively-fail-learn-more/]
6. Rowland CA (2014). The effect of testing versus restudy on retention. Psychological Bulletin 140(6). https://doi.org/10.1037/a0037559 [V, bibliographic; effect sizes secondary]
7. Bjork RA (1994) and Bjork and Bjork (2011) on desirable difficulties. [M], no URL checked.
8. Sweller J, Ayres P, Kalyuga S, Chandler P (2003). The expertise reversal effect. Educational Psychologist 38(1), 23-31. https://ro.uow.edu.au/edupapers/136 [V]
9. Kalyuga S (2007). Expertise reversal effect and its implications for learner-tailored instruction. Educational Psychology Review. https://doi.org/10.1007/S10648-007-9054-3 [V, bibliographic]
10. Barbieri CA et al. (2023). Meta-analysis of the worked examples effect on mathematics performance. Educational Psychology Review [V, secondary via https://scholarhub.vn/publication/:slug/f43c618f-344f-4e53-a1ef-60fe03ac85f4; check]
11. Bisra K, Liu Q, Nesbit JC, Salimi F, Winne PH (2018). Inducing self-explanation: a meta-analysis. Educational Psychology Review. https://www.Gwern.net/doc/psychology/spaced-repetition/2018-bisra.pdf [V]. Author list from memory [M].
12. Chi MTH, Feltovich PJ, Glaser R (1981). Categorization and representation of physics problems by experts and novices. Cognitive Science. [V in plan]
13. Kadavath S et al. (2022). Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 [V]
14. Xiong M et al. (2024). Can LLMs express their uncertainty? ICLR 2024. https://arxiv.org/abs/2306.13063 [V]
15. Farquhar S, Kossen J, Kuhn L, Gal Y (2024). Detecting hallucinations in large language models using semantic entropy. Nature 630. https://pmc.ncbi.nlm.nih.gov/articles/PMC11186750 [V]
16. Huang J et al. (2024). Large language models cannot self-correct reasoning yet. ICLR 2024. https://arxiv.org/abs/2310.01798 [V]
17. Panickssery A, Bowman SR, Feng S (2024). LLM evaluators recognize and favor their own generations. NeurIPS 2024. https://arxiv.org/abs/2404.13076 [V]
18. Wang Y, Zhao Y (2024). Metacognitive prompting improves understanding in large language models. NAACL 2024. https://arxiv.org/abs/2308.05342 [V]
19. Shinn N et al. (2023). Reflexion. NeurIPS 2023. https://arxiv.org/abs/2303.11366 [V]
20. LLMs know when they know, but do not act on it: a metacognitive harness for test-time scaling (2026). https://arxiv.org/abs/2605.14186 [V]
21. The Metacognitive Monitoring Battery (2026). https://arxiv.org/abs/2604.15702 [V]
22. MetaCrit: a critical thinking framework for self-regulated LLM reasoning (2025). https://arxiv.org/abs/2507.15015 [V, abstract]
23. Toward metacognitive monitoring before generation, theory paper, NeurIPS 2025 FoRLM workshop. https://arxiv.org/abs/2511.04341 [V, snippet]
24. ThoughtTerminator: benchmarking, calibrating and mitigating overthinking in reasoning models (2025). https://arxiv.org/abs/2504.13367 [V, snippet]
25. Length and correctness in reasoning models, overthink easy and underthink hard (2025). https://arxiv.org/abs/2505.00127 [V, snippet]
26. Steyvers M, Peters MAK (2025). Metacognition and uncertainty communication in humans and LLMs. https://arxiv.org/abs/2504.14045 [V, abstract]
27. Steyvers M et al. (2025). What large language models know and what people think they know. Nature Machine Intelligence 7, 221-231. [V, bibliographic]
28. Callaway F et al. (2024) metamemory as a meta-level MDP, cited in ref 23; not opened. [V, as cited]
29. Ohlsson S (1992). Information-processing explanations of insight. [M]
30. Kapur M (2008, 2016) productive failure studies. [M]
