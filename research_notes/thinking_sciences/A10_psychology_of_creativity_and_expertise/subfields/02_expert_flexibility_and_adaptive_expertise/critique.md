# Critique: A10.02 Expert flexibility and adaptive expertise

Cross-check of evidence_a, evidence_b, evidence_c. Claims are in claims.jsonl (K01-K27).

## Numbers re-opened this session (checked against the source text)

Confirmed:
- Sheridan & Reingold 2013 (PLOS ONE, full text): 17 experts (mean CFC 2223, range 1876-2580) and 17 novices; 8 of 17 in both groups chose the Einstellung move; move quality t(32)=6.04 and 4.93; first fixation 407 ms vs 719 ms; expert linear trend F(1,66)=13.12, novices F(1,66)=2.25 p=.138; 2 experts and 4 novices did not rule out mate. All match a12-a14, b01-b06.
- Kim et al. 2025 (arXiv 2502.04381 v1): physicians 66%, SE 5.3; Gemini-1.5-Pro 50%, o1 48%; most models under 50%; several under 20%.
- Shidara et al. 2026 (arXiv 2601.11866): Claude 4.1 Opus 0.751 (CI 0.738-0.763), physicians 0.66 (CI 0.55-0.75), four models not significantly different; human-miss set 55.0% / 25.0% / 20.0%.
- MedEinst (arXiv 2601.06636): 5,383 pairs, 49 diseases, 96.1% validity, Gemini-2.5-pro trap 60.90, GPT-5 error split 35% / 43% / 22%, MDAgent robust 3.20 trap 40.34, DyLAN 1.19 and 41.69, ECR-Agent ablation 40.25 to 55.49 to 69.49 and trap 33.75, robust 24.21.
- Naeini et al. 2023 (arXiv 2306.11167): humans 285/494 walls and 1405/1976 groups; GPT-4 5-shot 7 walls and 269 groups; OCW-Randomized 68 walls and 655 groups.

Corrections made or needed:
1. Kim et al. 2025: the v1 text names only Gemini-1.5-Pro (50%) and o1 (48%) as best. The figures "DeepSeek-R1 52%, DeepSeek-V3 50%" (a26, b18) are not in v1; they may come from a later version that I could not open (v3 URL failed). Treat the DeepSeek numbers as unconfirmed and say "best 48-52%" until checked. Also the paper's name for the set is M-ARC (v1), mARC-QA (a26/b18). Same dataset.
2. Naeini OCW-WordNet (b23): the line "298 to 471 walls, 1926 groups at 0-shot" is wrong in pairing. In the table, 0-shot gives 415 walls and 1759 groups; 1926 groups goes with the 10-shot row (471 walls). The correct range for GPT-4 on WordNet is about 279-471 walls (c03 is right). Also GPT-4 on the original set gives 2-7 walls, not 0-shot=7.
3. MedEinst (c13, c15): the table text is garbled in extraction. Row labels and values are misaligned in places (Qwen3-32B appears to have base accuracy 44.12 in one row and 40.25 in the ablation). The ablation numbers (40.25 / 43.46 trap) are consistent with each other; the main-table base accuracy for Qwen3-32B should be re-read from the PDF image before quoting.
4. a03 and b10: "three standard deviations" and the 3.67 odds factor come from the Bilalic 2008 Cognitive Psychology text, which this check could not re-open (paywall; Semantic Scholar rate-limited). Keep as reported, flagged as secondhand to this check.
5. Haq et al. 2025 and Li et al. 2025 (WCST) could not be found by arXiv title search in this session. Their numbers (b22, c06-c08) stay unverified here.

## Contradictions between sources
- Expertise and fixation: Bilalic 2008 shows large expert fixation (GM 100% vs CM 0% under the trap), while Sheridan & Reingold 2013 show equal rates of fixation in experts and novices (8/17 each) when the familiar move is good but suboptimal. These are compatible only if "fixation" is defined relative to skill-matched controls (Bilalic) rather than absolute choice rates.
- Bilalic 2008 treats set as not seeing alternatives (gaze). Pope-Caldwell & Washburn 2022 treat much of it as not trying, since people look at the shortcut. Telling people (the video) helps most but not all.
- Knowledge hurts (Wiley 1998, Bilalic) versus knowledge helps (b13: no cost when semantic accessibility is high). The 2026 study is N=30 and a single lab.
- LLM WCST: Li et al. 2025 report LLMs beat humans on correct matches; Hao et al. 2025 report near-chance set shifting without chain of thought; Reflection-Bench gives rule-dependent accuracy (shape 80%, number 26%). Differences in task format, number of trials and prompt explain much of this.
- Medical LLMs: Kim 2025 (models below physicians) versus Shidara 2026 (reasoning models equal or above physicians) versus MedEinst 2026 (frontier models still highly trapped). Different benchmarks; "closed gap" on mARC does not imply robustness on MedEinst, where stronger baselines had higher trap rates.

## Weak spots
- Almost all human data are chess; the n per skill cell in Bilalic 2008 is small (Exp 1 tier percentages come from groups of about 10 or less; Exp 3 had 12 players). Effect sizes in the eye-tracking study rest on 5 per group in places.
- No replication of the Bilalic chess result by an independent lab beyond Sheridan & Reingold (which changed the design and found boundary conditions). No failed replication was found; this is absence of evidence, not confirmation.
- The Luchins numbers are second-hand from Bilalic's text; the original was not opened.
- Athlete reflection and heuristic toolboxes: only one athlete paper (Siebert 2025, fast-and-frugal trees, 90% / 75% accuracy) and a theory paper (Fenwick 2026). No direct test of Gigerenzer's toolbox as an LLM operator-choice mechanism with measured results.
- LLM Einstellung studies mostly evaluate answer accuracy, not the process (no gaze analogue). Trace-level fixation measures are absent.
- Haq 2025 uses 6 problems per condition: too small to interpret.
- Meta-Reasoner (c20) and HybridMind (c27) are strategy-switching studies, not Einstellung tests; the link is by analogy. c27 and c26 were seen only in snippets.
- Binz & Schulz (b30), Blech et al. 2020 (b31), Hatano & Inagaki 1986 (b32), Luchins 1942 (a01, b29), Kennedy & Nowak 2024 (c25) were not opened.

## Only seen in snippets
a01, b29 (Luchins), b30, b31, b32, c25, c26, c27; the first check of Bilalic 2008 Cognitive Psychology numbers.

## GAPS
1. Does a scaffold (explicit "generate a second route, then compare") reduce LLM Einstellung at equal tokens on MedEinst, mARC and Only Connect Walls, relative to plain reasoning and to best-of-N? No study ran this equal-token comparison; ECR-Agent changed both tokens and structure.
2. Do the DeepSeek-R1 52% / DeepSeek-V3 50% numbers on M-ARC exist in a later version of Kim et al., and what is the correct Qwen3-32B base accuracy in the MedEinst main table?
3. What is a process-level measure of fixation in an LLM (the gaze analogue): fraction of reasoning tokens spent on the first-proposed route, number of distinct routes explored before the answer? Has anyone validated one against accuracy?
4. Does a one-line prompt that a shorter or different method may exist (the Pope-Caldwell "informed" condition) lift LLM performance on trap items, and does it hurt on items where the familiar route is right (the cost of over-switching)?
5. Is there an independent replication of the Bilalic 2008 skill gradient (GM 100% down to CM 0%), and of the carry-over cost (d=.65)? Any failed replications in other domains (programming, medicine, music)?
6. Does adaptive-expertise training (explaining why a procedure works, Hatano and Inagaki; invention before instruction, Schwartz) transfer to LLM agents, for example storing rationale with each stored procedure, and does it improve changed-constraint transfer?
7. Can a learned or rule-based operator selector (Meta-Reasoner style, Take The Best style stop rules) beat a fixed O1-O8 order on trap items, and what is the token cost of the monitor?
8. When is the Einstellung choice rational (Binz & Schulz resource-rational account)? What stop rule decides when to stop looking for alternatives in our S6, so the agent does not over-search?
9. Why do stronger LLMs show higher trap rates on MedEinst ("stronger priors, stronger blindness") while reasoning models improve on mARC? Which feature of the benchmark (counterfactual flips versus unusual items) drives the difference?
10. Do WCST perseveration patterns in LLMs (more perseverative than random errors, the reverse of humans) predict failure on trap tasks, i.e. is WCST a valid cheap proxy for fixation?

## Gap search results

Evidence in evidence_d.jsonl (d01-d22). Claims K28-K34 added; K09, K15, K18, K22, K24, K25 changed; K18 now "contested". Web search budget was exhausted and arXiv/OpenAlex/Semantic Scholar APIs were rate-limited, so gaps 1, 4, 6 could only be checked by absence.

1. Scaffold at equal tokens: STAYS OPEN. MedEinst baselines (d04) show generic debate (MDAgent) and dynamic agents (DyLAN) did worse on robust accuracy (3.20, 1.19 vs 11.28) with only small trap-rate changes (40.34, 41.69 vs 43.46); ECR-Agent changed structure and tokens together. No equal-token study found.
2. DeepSeek numbers and Qwen3-32B: CLOSED. Kim arXiv v1 is the only version and lacks DeepSeek 52/50 (d01); K15 now says 48-50 for v1. MedEinst Qwen3-32B base is 44.12, robust 11.28, trap 43.46 (d02).
3. Process-level fixation measure: PARTLY CLOSED. Underthinking (d06, d07) gives route-switch counts and UT score but for the opposite failure and not validated against trap accuracy. A first-route token share has no validation.
4. Informed prompt and cost of over-switching: STAYS OPEN for LLMs. Human data now exist: warning cut Luchins set from 0.83 to 0.57, alternating practice to 0.16 (d12); forget instruction costs when the old routine is needed (d15). LLM prompt controls (d07, d10) gave near-zero change.
5. Independent replications: PARTLY CLOSED. Set effects replicate outside the Bilalic design (d14-d17, d18), Luchins data re-checked (d11). The chess GM-to-CM gradient has no independent replication among 59 citing records (d20). Failed or null: programming interventions (d18, 2 of 39 switched) and reversed experience direction.
6. Adaptive-expertise training for LLM agents: STAYS OPEN. No study found.
7. Learned selector vs fixed order: PARTLY CLOSED. Meta-Reasoner (d08) beat fixed sets (89 vs 65/72) and direct self-selection (89 vs 82) on Game of 24, with 29-33% less time than ToT/Reflexion; HybridMind (d09) and Zhang (d10) show oracle headroom of 10+ points. Nobody tested it on trap items.
8. Rational stop rule: PARTLY CLOSED. Binz and Schulz model (d13) explains Luchins data, no stop rule validated for an agent.
9. Stronger models more trapped: REVISED. The paper's claim is not supported by its own Table 1: r=-0.69 between base accuracy and trap rate over 8 aligned rows, and the cited accuracies 54.30/53.58 belong to other models (d03). K18 downgraded to contested. Which benchmark feature drives the difference (counterfactual flips vs unusual items) remains untested.
10. WCST as proxy: STAYS OPEN. Perseverative-error pattern is real (d21) but no study links it to trap tasks.

Caveat: the MedEinst table was read from garbled text; confirm d03 against the PDF image before quoting r.
