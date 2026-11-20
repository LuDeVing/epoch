# Critique: LLM help in hardware debugging (E08.09)

## Corrections made (sources re-opened this session)
Re-checked against the arXiv abstract or full text: Hu and Ash 2608.02955 (99% confident quote, 4m 33s, "Almost all factual errors", pins 1,2,3 vs 5,6,7; images in 2/5 Spring and 5/12 Fall logs = 7/17); HWE-Bench 2604.14709 (417 tasks, 70.7%, precision 0.928 / 0.619, 77.7 tool calls, 714K vs 4.2M tokens, 45/417 = 10.8% unsolved); Sun et al. 2505.02151 (humans 66% / 70%, 81% when 100% sure, 10% confidence drop ~ 25% accuracy drop); METR 2507.09089 (+19%, -24%, -20%, 39%/38%); Kim et al. 2405.00623 (N=404, first-person effect); Bo et al. 2505.08063 (n=8).
Corrections:
1. b15: accuracy gain is 5.6 (answer) and 7.1 (answer+confidence) points in the SI regression, not "7.0". Use 5.6-7.1. The accuracy gap between the two arms is not significant (p=.213); the bias gap is (p=.011).
2. a13/b07: the "above 90% on smaller cores" holds for the best model (GPT-5.4: 97.1, 91.4, 93.8). The paper text also says "over 80%" for proprietary models in general. Quote both when used.
3. a01 images: "7 of 17" is a sum of 2/5 and 5/12, and the paper notes some images show only the assignment, not the circuit. Treat 41% as an upper bound for circuit photos.
4. a14 vs c05: Opus tool calls are 20.0 and Sonnet 18.6; a14 quoted Sonnet only. Not a conflict.
5. b11: the VeriPilot figure is 77.1% in the body and 85.71% in the abstract. Unresolved; do not cite either as final.
6. Not re-opened (snippets only or not read): a08, a09, a10, a21 (Katz and Anderson, Alaboudi and LaToza, Jonassen and Hung, Schaafstal: only via Hu and Ash), c10, c11, c12, c20, c27. MEIC 48x speedup and 93%/78% fix rates are unverified.

## Contradictions and tensions
- Chatbots give "sensible" debugging advice (Hu and Ash theme 2) yet make false image claims; both hold, but they are about different input types.
- Engineers prefer LLM answers (58.3%) even though 65.7% bury the core answer (b04). Preference does not track quality.
- Hedging helps (Kim et al.) but displaying LLM confidence raised bias more (Sun et al.): numeric confidence and first-person verbal hedges act differently. Not tested head to head.
- Waveform context helped 8 models and hurt 13 (ChipBench): no clear rule.
- Benchmark rates conflict by orders of magnitude (HWE-Bench 70.7%, EDA Bench ~2%, board-level design ~8%) because task type and grader differ. No cross-benchmark comparison is valid.
- Verbosity vs METR slowdown: unclear how much of any slowdown is verification overhead.

## Weak spots
- The key paper (Hu and Ash 2026) is n=17 self-selected logs, qualitative, no accuracy rate, no control; the WIP companion is n=1. "Overconfidence" in hardware chat rests on 2-3 anecdotes.
- No study measures the effect of LLM help on real hardware repair success or time with a control group.
- Most quantitative work is on HDL/RTL code, which is software-like and verifiable by simulation; it does not transfer to breadboard or PCB faults.
- Calibration papers (Xiong, Kadavath, Sun, Ghosh) use QA, not diagnosis.
- The over 40% troubleshooting-time claim comes from trade articles.
- All 2026 items are recent preprints, not yet replicated. Several model versions (GPT-5.4, Opus 4.6) cannot be reproduced by us.
- Few replications or failed replications exist in this subfield.

## GAPS
1. Does a forced "request a measurement before accepting a physical-state claim" step reduce wrong actions from image-derived claims at equal tokens? (No study; test on our agent.)
2. What is the actual rate of false claims per image input, with a control set, across current multimodal models (Hu and Ash give only anecdotes)?
3. Does LLM help change time-to-repair and success in a controlled hardware debugging study (the authors list it as future work)?
4. Does first-person hedging transfer from medical QA (Kim et al.) to diagnostic advice, and does it beat numeric confidence?
5. Does hypothesis ordering by cheapest discriminating test beat the model's own ranking?
6. Does a symptom-to-root-cause trace step reduce the symptom-fix failure in HWE-Bench-style tasks?
7. Which verifiers (reference model, waveform summary, compiler feedback) give the largest gain per token in RTL debugging, and are the gains additive?
8. Does the human-as-sensor loop (test, report, repeat) degrade over many turns because of context handling, and does a running state summary help?
9. Are there replications of the Hu and Ash findings with other courses or models, or any non-student (technician) population?
10. Do verbal overconfidence results hold for reasoning models in 2026 (Ghosh and Panday show wide spread: ECE 0.122 to 0.726)?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d17); claims K22-K28 were added and K02, K03, K09-K11, K17-K19, K21 were extended. No claim status was raised, because every new line is a single source or a different task type.

1. Measurement-before-physical-claim step (open). No study found. Related: a verifier is under-used more than over-trusted (d12, 15.2% flipped vs 47.5% of corrections missed), so the step must force acting on the result. OmniSch shows a locate-then-verify aid lifts symbol F1 (d06).
2. False-claim rate per image (open, partly informed). OmniSch (best net F1 27.44%) and AMSbench (count accuracy 0.88 to 0.45 as circuits grow) give perception error rates, but neither reports a hallucination rate or a control set; both use drawn schematics, not bench photos (d06, d07).
3. Controlled time-to-repair (open). Closest controlled design is software: 106 students, GPT-4 error explanations faster in 1 of 6 tasks (d03). The vocational electronics quasi-experiment saw no clear assembly-error drop, but the page gave HTTP 403 and was not read (d04, opened:false).
4. First-person hedging transfer (open). Nothing new on hedging vs numeric confidence in diagnosis; consumer repair work shows completeness does not imply safety (d05).
5. Ordering by cheapest discriminating test (partly closed). Information-gain question choice (UoT) beat direct prompting on a troubleshooting set, GPT-4 67.3% vs 43.7%, simulated, closed fault set (d10). Cost-weighted bench tests untested; no head-to-head with the model's own ranking on hardware.
6. Symptom-to-root-cause trace (open). No new source; HWE-Bench items from earlier files remain the only evidence.
7. Verifier gain per token (partly closed). AutoVeriFix+ gives stage gains on GPT-4: testbench I/O +22.2 (RTLLM v2.0), syntax +24.6 (VerilogEval-Human), trace +0.9 to +4.4; largest verifier depends on benchmark. Additivity only in a fixed order; no token data (d15). A small-model loop paper gave +2.8 points and has internal number conflicts (d14).
8. Multi-turn degradation (closed as general evidence, open for hardware). Laban et al.: 39% average drop, unreliability +112%, reasoning models no better, recap helps only partly, temperature does not fix it (d01, d02). No test of a model-written running summary.
9. Replication of Hu and Ash (open). Citation lists of the paper and its WIP companion were empty; no technician population found (d16).
10. Verbal overconfidence in 2026 reasoning models (open, mixed). Reasoning models better calibrated in 33 of 36 QA settings (d08), but RL on verifiable rewards may bring overconfidence back (d09, snippet only). No diagnostic-task test.

Caveats: OpenAlex and arXiv search endpoints were rate limited and Semantic Scholar search returned empty, so coverage depends on 7 web searches. d04 and d09 were not opened; do not cite their numbers.
