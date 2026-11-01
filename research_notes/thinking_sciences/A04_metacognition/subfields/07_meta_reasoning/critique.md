# A04.07 Meta-reasoning: cross-check critique

## Re-opened this session (full PDF text)
Xiong 2024; Huang 2024; Hagendorff 2023; DeepConf (Fu 2025); Chen overthinking; Wang underthinking; Zhang probe; Tsui self-correction blind spot; Frey 2018; Bago and De Neys 2017 (partial). Nearly all quoted numbers matched.

## Corrections
1. a17: "Oracle: GPT-4 GSM8K 84.3 -> 97.5" is wrong. 84.3 is the GPT-3.5 oracle score. GPT-4 is 95.5 -> 97.5 (Huang Table 2). b22 has it right.
2. a15: "White-box vs black-box AUROC 0.522 vs 0.605" reads backwards. White-box (better) is 0.605, black-box 0.522 (b21 right). Gap is narrow.
3. a15 says "five datasets"; the paper says five task types and eight tasks (b21 right). Five datasets applies to the white-box comparison only.
4. a17/c12: GSM8K "74.7%" appears twice with two meanings: share of cases where GPT-3.5 kept its first answer after two rounds, and the GPT-3.5 GSM8K score after 5 calls. Coincidence; do not merge. The Huang table labels rows "# calls" 1/3/5, not rounds.
5. a13/b23: GPT-4 chain-of-thought share is 85% in one place and 84% in another within Hagendorff; keep "about 85%".
6. c16: Tsui paper is dated 2026 in the evidence file but the arXiv id is 2507; the numbers (64.5%, 76.0%, 89.3%, 5,306 traces) are confirmed.
7. a19/b24: "first round correct in over 92%" confirmed in Chen text; b24 "89-97%" range is per model and dataset, consistent.
8. Wang (a20/b25): TIP pass@1 38.3 -> 44.1 confirmed (table). The Pass@4 43.7 -> 51.4 figure is also in the text; c-file did not use it.
9. Frey (a10): 68.6 vs 79.0, F(1,230)=59.35, 66%, 20.8%, 28.9% confirmed.
10. Bago and De Neys (a11): 74.8% and 87.6% confirmed in text; 12% deadline miss in Exp 2 confirmed. b19 said no percentages found; superseded by a11.

## Contradictions and tensions
- Human conflict detection: Frey (a10) and the 2023 moderate base-rate study (b12) say detection is common; b13 (2025, N=248) says reverse-detection effects vanish when items are scored by chosen response and believability. Status: contested.
- Same-model review: Self-Refine (a26, about 20% gain) vs Huang (a17) and Tyen (a18) show failure. Likely moderator: no ground truth to check vs style tasks. Not tested head to head.
- Early exit (c05, c07) reports accuracy gains while Chen (a19) says first round is nearly always right; both are consistent, but DeepConf-low also loses accuracy in some settings (Qwen3-32B BRUMO25 -0.9%; b26).
- Autism CRT: b08 (no difference) vs b16 (more deliberative in autistic group). Minor for our agent.
- Reasoning models: better verbalised calibration (c08) vs Xiong's weak AUROC for verbalised confidence (older non-reasoning models). Different model generations.

## Weak spots
- Founding human studies not opened: Thompson 2011 (a09, c24), Thompson 2013, Thompson and Johnson 2014. Their effect sizes are known only from the 2017 review.
- No human replication of FOR with a pooled effect size was found. No registered replication of the two-response paradigm.
- No LLM study measures an LLM "feeling of rightness" followed by a decision to rethink at equal tokens. The closest are probe early exit (a21) and DEER (a22).
- Most LLM stop studies use math (AIME, GSM8K, MATH500). Open-ended and agentic tasks are thin.
- Claims backed by one independent source: opt-out trait, probes, AdaptThink, Meta-Reasoner (c15 numbers from abstract-level reading).

## Seen only in snippets or abstract
a09, b17, b18, b19, c18, c21, c23, c24 (not opened or abstract only); a24 slopes not extracted; a25/c22 gains not extracted; c15 table numbers not re-checked; c19 AdaptThink numbers not re-checked; b27 sample sizes not extracted.

## GAPS
1. Does a trigger-based "rethink only on low certainty" policy beat always-rethink and never-rethink at equal tokens for an API-only LLM agent, using sampling agreement or trial-answer confidence as the signal? (No direct study found.)
2. What are the exact effect sizes and sample sizes in Thompson, Prowse Turner and Pennycook (2011) and Thompson and Johnson (2014), and has the FOR to rethink-time link been replicated independently?
3. Which cheap, black-box signal best predicts an LLM's wrong answer on reasoning tasks (self-consistency, trial-answer confidence, token entropy, verbalised confidence) with AUROC on one common benchmark?
4. Does external-feedback self-correction (tests, tools, retrieval) reliably help while blind review hurts, and what is the crossover? Quantify from CRITIC, Reflexion-style and code-execution studies.
5. How does the blind-spot fix (framing own answer as another's, or appending "Wait") perform on reasoning models and at equal tokens?
6. Where is the optimal stop point: is there a published curve of accuracy vs reasoning tokens by difficulty for current models (2025-2026), and does difficulty estimation before solving (initial judgment of solvability) help allocate budget?
7. Is overthinking driven by model confidence being too low after a correct answer (fixable by a verifier) or by training reward shaping? Any 2026 work with controlled ablations?
8. Do agentic or open-ended tasks show the same underthinking/overthinking pattern as math, and which stop signals transfer?
9. Does the diminishing-criterion pattern (lower bar over time) improve LLM stopping rules versus a fixed threshold? No test found.
10. Individual-difference analogues: do prompts that induce actively open-minded thinking reduce myside bias in LLMs where Stanovich and Toplak found no human effect?

## Gap search results (evidence_d.jsonl d01-d25; claims K25-K34 added)

Web search quota ran out, so the search used arXiv PDFs by known id, Europe PMC abstracts, and Semantic Scholar/OpenAlex (both rate-limited). Papers found by title recall, not by broad search, so coverage of 2026 work is thin.

1. Gate vs always-rethink vs never-rethink at equal tokens: STILL OPEN. No study runs that three-way test. Nearest: stop-on-agreement rules (ESC d07, Adaptive-Consistency d08, answer convergence d23, Certaindex d25) save 34-84% of samples with under 0.1% average accuracy loss, and At equal compute, majority vote beats generative verification until about 8x budget (d09). These show an agreement gate is cheap and safe for stopping; they do not test a gate that triggers a rethink.
2. Founding FOR numbers: PARTLY CLOSED. Thompson 2011 sample sizes found (N=60, 48, 128, 64; d01, abstract only). Effect sizes not obtained (full text blocked, 403). Thompson and Johnson 2014 not retrievable. Later support (d02 N=289, d03) comes from the same tradition; no independent-lab replication found. K01 stays established but with a note.
3. Best cheap signal by AUROC on one benchmark: STILL OPEN as a single table. Partial: within-question discrimination in CISC (d05) ranks P(True) 62.3% > response probability 59.0% > verbalised 0-100 56.1% > verbalised binary 52.2%, and calibration (ECE) did not predict usefulness. Length (d19, d20) and agreement (d07, d08) are free signals. No paper compares all four by AUROC on one set.
4. External feedback vs blind review: MOSTLY CLOSED (K26). Sound verifier 88% vs LLM verifier 55% vs none 40% (Blocksworld, d14); graph colouring 1/100 self-verifier vs about 40% sound (d15); CRITIC shows small tool gain on GSM8K (+2.1 vs -1.8 no tool) and larger on QA (d12). Reflexion fails when test false positives are high, 16.3% (d13). Caveat: much of the external-loop gain is resampling (d15). A numeric crossover threshold was not found; the best statement is "gain tracks the false-positive rate of the accept test".
5. Blind-spot fixes on reasoning models at equal tokens: PARTLY CLOSED (K28, contested). Wait at equal tokens loses to parallel sampling (d17); s1 shows a gain on AIME24 but with more tokens and 30 items (d16); NoWait shows most reflection tokens can go (d18). The "frame answer as someone else's" fix was not found tested at equal tokens.
6. Accuracy-vs-tokens curve by difficulty and solvability judging: PARTLY CLOSED. Non-monotonic length-accuracy curve and under/overthinking by tier shown on small distilled models (d19, d17). Snell (d21) shows difficulty-conditioned allocation helps but its difficulty estimate costs 2048 samples per question, uncharged. A 2025-2026 curve for frontier models by difficulty was not found. Judging solvability before solving as a cheap probe is untested (K31).
7. Cause of overthinking (low confidence vs reward shaping): STILL OPEN. No controlled ablation found. Evidence is only correlational (d19 wrong answers longer, d23 early convergence). AdaptThink (existing) fixes it by RL, which hints at training but does not isolate cause.
8. Agentic and open-ended tasks: PARTLY CLOSED (K32). Overthinking appears in SWE-bench (d22), but the mitigation was post-hoc selection by an LLM-judge score, not a live stop signal. Transfer of stop signals from math to agents is not shown. Out-of-distribution transfer of probe stops drops from 60% to 20% (d24).
9. Diminishing-criterion stopping rule vs fixed threshold: STILL OPEN. No LLM test found.
10. Actively open-minded thinking prompts on LLM myside bias: STILL OPEN. Searches found only human AOT measurement papers (Europe PMC); no LLM study.

Corrections to earlier files: none found. Note for K08: it holds, but d12 shows the no-tool loop is not uniformly bad (TabMWP +20.3 without tool), so "does not help" should read "does not reliably help".

Net: the strongest new finding for the schema is a design rule, not a measured policy: use an external accept test where one exists, use agreement and relative length as the cheap trigger elsewhere, and compare every rethink step against plain k-sample voting at equal tokens.
