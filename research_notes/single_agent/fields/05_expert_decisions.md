# Expert decision making and reasoning under uncertainty: what it offers one thinking agent

Marks: [V] source checked this session (often only the abstract or a summary page; stated where so). [M] from memory, numbers to re-check. Strength: strong / moderate / weak.

## 1. What the field studies

This field asks how skilled people decide when time is short, data is thin and the answer cannot be computed. Klein's naturalistic decision making studies fire fighters, nurses and officers in the field. De Groot, Gobet and Bilalic study chess masters, where skill is measurable. Johnson-Laird studies how people build small models of what could be true. Evans and Stanovich split thinking into fast, automatic answers and slow, effortful checking. Kahneman and Klein (2009) ask when the fast kind can be trusted. Mercier and Sperber argue that reasoning is built to argue and to judge arguments, not to find truth alone. For us the shared question is: when should an agent accept its first answer, and when should it spend effort to test it?

## 2. Core findings

**F1. Experts recognize first, then simulate one option.** Klein's recognition-primed decision model: experts match the situation to a known pattern, which brings a likely action; they mentally simulate it and only look for another option if the simulation shows a flaw. They do not compare many options side by side. Evidence: field interviews, observational. Strength: moderate for description, weak as a proof that it beats other methods. [M] (Klein 1998, Sources of Power; Klein, Calderwood, Clinton-Cirocco 1986.)

**F2. Experts search no deeper than novices; they search better.** De Groot found masters did not examine more moves or look deeper; they picked better moves to examine. His "progressive deepening" is the habit of returning to the same line several times, each time with a changed view of the position. [V] only via secondary summaries (chessprogramming.org on de Groot; a 1979 Dutch article). Strength: moderate, replicated in later chess work [M].

**F3. Expert memory is chunks and templates.** Masters store tens of thousands of positional chunks (Gobet and Simon estimate about 50,000) and chunks grow into templates with slots. Recall of real positions is much better than random ones; the edge vanishes on random positions. [V] abstract level (Gobet and Simon 1996 papers, Gobet 1998 comparison of memory theories, Brunel repository). Strength: strong in chess, and the lesson is domain-specific: expertise is a large library of patterns, not a general method.

**F4. A good-enough first idea blocks a better one (Einstellung).** Bilalic, McLeod and Gobet: a familiar solution makes players look at features that fit it, and they keep looking even when told to find something better. Eye tracking shows attention stays on the familiar line. Stronger players are hit too, though less. [V] (2008 Cognition paper described in Sheridan and Reingold 2013 PLoS ONE, and Bilalic et al. 2010 review). Strength: strong, replicated with eye tracking. Important detail: when the familiar move is a blunder, nearly all experts avoid it. The trap is the "good but not best" first answer. [V]

**F5. Pre-mortem: assume failure, then explain it.** Mitchell, Russo and Pennington (1989) showed that imagining an outcome as already happened produces more, and more specific, reasons than imagining it as possible. Klein (2007, HBR) turned it into the project pre-mortem. The widely quoted "30% better" figure is disputed: one source says it counts reasons generated, not correctness. I could not read the 1989 paper. [V] for existence and the dispute; the number is not trusted. Strength: weak to moderate. The effect is on quantity of reasons in student studies, not on better final decisions.

**F6. People reason from models of what is true, and miss counterexamples.** Johnson-Laird's mental model theory: people represent only what is true in each case, so they err where the false case matters. Errors drop when people are made to look for a counterexample. [M] (Johnson-Laird 2006, How We Reason; Johnson-Laird and Byrne 1991.) Strength: moderate; the theory is influential but contested against other accounts.

**F7. Fast thinking is trustworthy only in a regular environment with feedback.** Kahneman and Klein (2009): intuition is skilled when (a) the environment has stable cues and (b) the person had many chances to learn them with fast feedback. Felt confidence is not a reliable sign of accuracy. Klein: a gut feeling is one data point that still needs a check. [V] (PubMed record and McKinsey interview). Strength: strong as consensus of two opposed camps; the "failure to disagree" is a review, not an experiment.

**F8. Dual process: fast default, slow override, and a feeling of rightness.** Evans and Stanovich: type 1 gives a default answer; type 2 may override it. Thompson and colleagues showed a "feeling of rightness" from the fast answer decides whether people check. Low feeling, more checking. [M] (Evans and Stanovich 2013; Thompson et al. 2011, which the plan cites as [V].) Strength: moderate; the strict two-system split is criticized, the check-when-unsure part is better supported.

**F9. Reasoning is better at judging others' arguments than producing our own.** Mercier and Sperber (2011): reasoning evolved to produce arguments for our side and to evaluate others' arguments. So solitary reasoning shows confirmation bias, while evaluating a rival's argument is accurate, and groups with disagreement do better. [V] abstract level (Behavioral and Brain Sciences 34; I could not confirm page numbers). Strength: moderate; BBS commentary was heated and the evolutionary claim is hard to test, but the "people spot flaws in others' arguments more than in their own" pattern is widely replicated [M].

## 3. Mechanisms an agent can run

**M1. Recognize-then-simulate (RPD step).**
- Trigger: probe step done, the probe attempts agree (high agreement means a "feeling of rightness" in machine form) and a pattern from lessons memory matches the problem class.
- Action: write the single best candidate plus "what would have to be true for this to fail". Run one concrete simulation: trace it by hand or in code on one new input. If the trace shows a flaw, only then move to the next candidate. Do not write a list of options first.
- Check: at equal tokens against plain best-of-N, on ARC-1/2 and BrainTeaser. Gate: no loss on BrainTeaser, gain on ARC where a checker exists.
- Evidence: F1, F7, F8. Our data: first natural answers right 56% on ARC and about 92% on word puzzles [ours].
- Risk: low. It is the "trust until a check fails" principle. It fails when the pattern match is wrong and the simulation is too shallow to show it.

**M2. Trust gate from environment, not from confidence.**
- Trigger: router, before choosing converge or doubt.
- Action: answer two written questions. (a) Is there a real check (examples, tests, a run)? (b) Has this problem class been seen before with known outcomes in memory? Yes to either: converge on the fast answer and let the check decide. No to both and probe attempts disagree: escalate. Do not use the model's stated confidence; use agreement across attempts and check results.
- Check: log the route and compare accuracy of "gate says trust" against "gate says doubt". The gate is useful if accuracy on the trust bucket is clearly higher than on the doubt bucket. Then ablate: always-doubt vs gated at equal tokens.
- Evidence: F7 (strong), plus LLM confidence is poorly calibrated [M].
- Risk: moderate. Environment regularity is hard for a model to judge; it may label novel puzzles as regular. Use measured agreement as the real signal.

**M3. Progressive deepening of one candidate (return, do not widen).**
- Trigger: a candidate passes most but not all checks, or the probe splits into two close candidates.
- Action: take the best line and revisit it three times, each time under a different restatement of the problem (objects, then counts, then relations). After each pass write only what changed in the view. Stop at the first pass that fixes the failing case.
- Check: compare with spending the same tokens on fresh independent attempts (best-of-N). Metric: solved per 100k tokens on near-miss items.
- Evidence: F2, moderate, human chess only.
- Risk: moderate. Anchoring on one line is the Einstellung trap (F4). Limit to 3 passes and require a changed representation each pass.

**M4. Einstellung break: demand a better rival only when the first answer is merely "fine".**
- Trigger: the first answer passes the available checks but there is slack (a long program, an unused example detail, answer cost high) AND the problem is open or has a scoring gap (optimization, design, architecture search).
- Action: write the first answer, then a prompt: "assume a solution exists that is clearly better; list which features of this problem my answer ignores". Generate one rival from those ignored features and compare on the one input where they differ.
- Check: on architecture search and NoveltyBench, compare with plain at equal tokens. Do NOT run on single-answer sets; measure the harm there as a control.
- Evidence: F4 (strong in humans). Our data: forced divergence helped open tasks and hurt puzzles [ours].
- Risk: high on puzzles. Bilalic's result is about suboptimal first moves; most puzzle first answers are simply right. Gate it to open problems only.

**M5. Pre-mortem before committing to a costly action.**
- Trigger: before an irreversible or expensive step (running a long experiment, submitting a final answer with no checker, spending a retry round).
- Action: write "It is later and this failed. The three most likely reasons were:" then for each reason, one cheap test that would show it, run the cheapest. Revise only if a test fires. Keep it to one short call.
- Check: rate of avoided bad runs per token (for architecture search, share of runs that crash or regress); compare with no pre-mortem at equal tokens.
- Evidence: F5 (weak to moderate; quantity of reasons, not quality of decisions). Plus PreFlect (section 4).
- Risk: moderate. Forced failure stories are an always-doubt move. Our BrainTeaser result showed forced doubt hurt most. Run it only before costly actions, never on a cheap answer.

**M6. Counterexample hunt before accepting a rule.**
- Trigger: a rule fits all examples and there is no external checker for new inputs (ARC-style, rule induction, logic items).
- Action: write the rule as a small model of cases ("when A, output B"). Ask for the case the rule has not been tested on: an edge case, an empty case, a case that mirrors or rotates. Compute the rule's output there by hand and ask whether it is plausible given the examples. This matches the plan's symmetry consistency selector.
- Check: replay on stored ARC candidates: does the counterexample test separate right programs from wrong ones better than vote or shortest program? The plan's symmetry selector reached 34 of 36 and is the benchmark to beat [ours].
- Evidence: F6 (moderate); our own symmetry result as an implementation.
- Risk: low to moderate. Generating test inputs costs tokens; a wrong "expected output" can reject a correct rule. Derive the expected output from examples before looking at the candidate output (anchored tie-break).

**M7. Critic role: judge the rival's work, not your own.**
- Trigger: selection among candidates, or a revise round with no external signal.
- Action: do not ask "check your answer". Present each candidate to a fresh call as someone else's proposal, with the instruction "find one specific flaw, with an input that shows it". The proposer defends only with a run. Strip authorship labels and shuffle order.
- Check: A/B at equal tokens: self-review call vs other-proposal critic call vs no review. Metric: flip rate from right to wrong and from wrong to right.
- Evidence: F9 for humans. For models the evidence is mixed (section 4).
- Risk: high. Self-correction without outside signal often lowers accuracy [V, Huang et al.]. The critic must be tied to a run or an input where candidates differ, otherwise it only adds doubt.

**M8. Chunk library: pattern recall by class.**
- Trigger: the look-back step after each problem, and the probe step before a new one.
- Action: store lessons as (pattern signature, trick, trap), like chess chunks with slots. At the start of a new problem retrieve at most three by signature match. Promote a chunk only after it helps twice.
- Check: held-out stream of problems; accuracy with memory vs without at equal tokens, including the extra tokens of the memory lines.
- Evidence: F3 (strong in chess, but expertise there came from thousands of hours; a small ledger is a weak analogue).
- Risk: moderate. Wrong chunks cause Einstellung (F4). Keep entries one line, tagged by class, and drop ones that fail twice.

## 4. Evidence on LLMs and AI agents

- **Dual process in models.** Hagendorff, Fabi and Kosinski (Nature Computational Science 2023) gave models cognitive reflection tests and semantic illusions. GPT-3 era models made human-like intuitive errors; the ChatGPT models mostly avoided them, partly through chain of thought, but stayed accurate even with it blocked. [V] via PubMed Central summary. Strength: moderate; shows intuition and deliberation are entangled in models, so "fast vs slow" is not a clean switch.
- **Self-correction.** Huang et al. (ICLR 2024): LLMs cannot reliably correct their own reasoning without external feedback; accuracy sometimes drops. A summary says multi-agent debate did not beat self-consistency at the same number of responses. [V] abstract, with the debate remark from a secondary summary. Strength: strong. This directly limits M7.
- **Debate.** Du et al. (ICML 2024): multiple model instances propose and critique over rounds; gains on math, strategy and factuality (a secondary summary says up to 8 points factual and 26 points reasoning; not checked against the paper). [V] abstract level. Strength: moderate; the Huang comparison shows the gain may be mostly sampling.
- **Self-preference.** Panickssery, Bowman and Feng (NeurIPS 2024): models recognize their own text above chance and score it higher; the stronger the self-recognition, the stronger the bias. [V] abstract level; the numbers (73.5% for GPT-4) are from summaries. Strength: moderate. This is the machine side of F9: a model is a weaker judge of its own output than of someone else's, so strip authorship in M7.
- **Einstellung in models.** MedEinst (arXiv 2601.06636, 2026) reports that frontier models keep a first diagnosis against counterfactual cues; stronger models showed a higher bias trap rate (a 60.9% figure for one model). [V] summary only; I did not read the paper. Strength: weak to moderate, one benchmark. A separate Only Connect dataset with red herrings exists; I did not check it. [V] listing only.
- **Mental models.** An arXiv study fitted PaLM 2 to mReasoner, a mental model theory implementation with parameters for counterexample search and its effect on syllogisms (arXiv 2311.00445). The summary did not show results. [V] existence only. RULEBREAKERS (arXiv 2410.16502) tests whether models avoid formally valid but implausible conclusions as humans do. [V] existence only. I found no direct test that adding a counterexample-search step improves model accuracy. That is an open gap.
- **Pre-mortem for agents.** PreFlect (arXiv 2602.07187, Feb 2026) critiques and refines a plan before execution, using errors drawn from past trajectories, and reports better utility than reflection-after-failure baselines. [V] listing; effect sizes not read. Community "premortem" skills exist but are untested. Strength: weak.
- **Chess-style search for LLMs.** I did not find a checked study of progressive deepening or chunk-template memory as an LLM prompting method. The nearest, adaptive sampling and early stopping, is already in the plan.

## 5. What does not transfer, and where it could hurt

- **Does not transfer:** years of feedback that build a chunk library (a model has no such trained-in-run library, only its weights and our small ledger); eye gaze and attention capture; the felt sense of rightness (we use agreement and check results instead); motivation to win an argument; groups with real stakes. The argumentative theory says humans defend their side because of social stakes; a model has no side to defend, though self-preference shows a related bias.
- **Where it makes the agent worse, given our data:**
  - M4 and M5 are forced-doubt moves. Forced doubt hurt most on BrainTeaser, and forced divergence cut ARC per-attempt accuracy from 56% to 12-31% [ours]. They need strict triggers.
  - M7 as self-review is known to lower accuracy without a run or a shared difference input.
  - M3 can anchor on one line. M8 can import a wrong lesson.
  - Every mechanism adds calls. The 0% heavy scaffold shows setup can eat the whole budget.
  - Kahneman and Klein's rule suggests the opposite risk: in low-validity settings (forecasting, open design) the first answer should not be trusted. Our open tasks are that case; our puzzle tasks are the regular case. The router must tell them apart.

## 6. Open questions

1. Does agreement across probe attempts predict correctness well enough to serve as the "environment regularity" signal? (Plan item: untested router.)
2. Does a counterexample step beat the symmetry selector or only equal it?
3. Is a critic on another's proposal (M7) better than a plain re-sample at equal tokens, once authorship is hidden?
4. Does a pre-mortem reduce wasted architecture runs, or only add text? Needs a count of crashed or regressed runs.
5. Does the lesson ledger behave like chess chunks (helps on similar problems) or like Einstellung (locks in)? Needs a held-out stream.
6. Do these effects survive across model sizes? Most LLM evidence here is from larger models than Haiku.

## 7. References

1. Kahneman D, Klein G. Conditions for intuitive expertise: a failure to disagree. American Psychologist 64(6):515-526, 2009. https://pubmed.ncbi.nlm.nih.gov/19739881/ [V abstract]. McKinsey interview: https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/strategic-decisions-when-can-you-trust-your-gut [V]
2. Mercier H, Sperber D. Why do humans reason? Arguments for an argumentative theory. Behavioral and Brain Sciences 34, 2011. https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/why-do-humans-reason-arguments-for-an-argumentative-theory/53E3F3180014E80E8BE9FB7A2DD44049 [V abstract]
3. Bilalic M, McLeod P, Gobet F. Why good thoughts block better ones: the mechanism of the pernicious Einstellung (set) effect. Cognition 108(3), 2008. [V citation]. Related: Sheridan H, Reingold E. PLoS ONE 2013, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3790829/ [V]; Bilalic et al. 2010 review, https://cognition.aau.at/download/Publikationen/Bilalic/Bilalic_etal_2010b.pdf [V listing]
4. Mitchell DJ, Russo JE, Pennington N. Back to the future: temporal perspective in the explanation of events. Journal of Behavioral Decision Making 2, 1989. [V citation only; original unread]. Klein G. Performing a project premortem. Harvard Business Review 85(9), 2007. [V citation via Wikipedia and summaries]
5. Gobet F, Simon HA. Templates in chess memory: a mechanism for recalling several boards. Cognitive Psychology 31, 1996; Gobet F. Memory for the meaningless: how chunks help. 1998 and related Brunel repository items: https://bura.brunel.ac.uk/handle/2438/1339 [V abstract level; exact titles not confirmed]
6. de Groot AD. Thought and Choice in Chess. 1946/1965. [M]. Summary of the work: https://chessprogramming.org/Adriaan_de_Groot [V]
7. Klein G. Sources of Power. MIT Press, 1998; Klein, Calderwood, Clinton-Cirocco 1986. [M]
8. Johnson-Laird PN. How We Reason. Oxford University Press, 2006. [M]
9. Evans JStBT, Stanovich KE. Dual-process theories of higher cognition. Perspectives on Psychological Science 8, 2013. [M]. Thompson VA, Prowse Turner JA, Pennycook G. Intuition, reason and metacognition. Cognitive Psychology 63, 2011. [M]
10. Hagendorff T, Fabi S, Kosinski M. Human-like intuitive behavior and reasoning biases emerged in large language models but disappeared in ChatGPT. Nature Computational Science 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10766525 [V summary]
11. Huang J, Chen X, et al. Large language models cannot self-correct reasoning yet. ICLR 2024. https://arxiv.org/abs/2310.01798 [V abstract]
12. Du Y, Li S, Torralba A, Tenenbaum J, Mordatch I. Improving factuality and reasoning in language models through multiagent debate. ICML 2024. https://arxiv.org/abs/2305.14325 [V abstract; author list from memory]
13. Panickssery A, Bowman SR, Feng S. LLM evaluators recognize and favor their own generations. NeurIPS 2024. https://arxiv.org/abs/2404.13076 [V abstract]
14. MedEinst: benchmarking the Einstellung effect in medical LLMs. arXiv 2601.06636, 2026. https://arxiv.org/pdf/2601.06636 [V summary only]
15. PreFlect (pre-execution plan reflection for agents). arXiv 2602.07187, 2026. https://arxiv.org/abs/2602.07187 [V listing; authors not checked]
16. A systematic comparison of syllogistic reasoning in humans and language models. arXiv 2311.00445. https://arxiv.org/pdf/2311.00445 [V listing]. RULEBREAKERS, arXiv 2410.16502. https://arxiv.org/pdf/2410.16502 [V listing]
