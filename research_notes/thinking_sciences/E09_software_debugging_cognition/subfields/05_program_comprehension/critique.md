# Critique: E09.05 Program comprehension (cross-check)

## Corrections made (sources re-opened this session)
Re-checked against the arXiv abstract or full text (pdftotext):
- Wyrich, Bogner, Wagner (2206.11102): 95 studies, 67 of 95 (71%) "X influences comprehension", 53.7% students only, N 5-277 median 34, journals median 61 vs conferences 26, 67 of 95 on screen, 23 factorial: CONFIRMED. Correction: b01/b04 say "of 94 experiments" for factorial; the paper's table shows 23 (24%), i.e. of 95. Minor.
- Langhout & Aniche (2103.05424): 132 students, 2.7 to 56 times, 7 of 14 atoms, 10 of 14 perceived confusing: CONFIRMED. (Pooled OR 3.82 not re-opened.)
- Kou et al. (2306.01220): kappa 0.68 and 0.73, 57 of 211 (27%), GPT-4 F1 30.0% with alpha 0.04 in one table configuration: CONFIRMED. Note: "GPT-4 lowest" holds for that configuration only; the best-method row (45.7 F1, 0.27) was not located in the text.
- Paltenghi et al. (2210.05506): mean +0.22 for CodeGen-type agreement, 39.3/36.3/37.7% answer rates, 42.3% baseline, gap up to 13.3, follow-up Spearman 0.49: CONFIRMED. b17 and c03/c21 are the SAME paper, so they are one source, not three.
- Li et al. (2402.14182): 22% of 68 methods, 85%, rho -0.1279, p 0.3862: CONFIRMED. b18, a18, c01 are the same paper (one source).
- Kaufman et al. (2607.08885): 74% (evidence says 73.9) and 49%, OR 2.94, N=86: CONFIRMED.
- Zhao et al. RHDA (2502.13170): 68.75/41.18 standard, 89.12/83.14 CoT, 90.62/84.16 T=2 N=1: CONFIRMED (GPT-4o rows).
- Copilot brownfield (2511.02922): N=15, p=0.59 confirmed. Correction: the abstract says the category-level rho of +0.50 and -0.57 did not survive multiple-comparison correction; claim kept at single-source.
- Titles/existence of arXiv 2609.26388, 2606.31725, 2602.22368 confirmed; their detailed numbers were NOT re-checked.

Not re-opened: Busjahn percentages, Peitek fMRI figures, CodeSense, RepoNavigator, EquiBench, CRUXEval, Qiao review. They stay at the original agents' confidence.

## Duplicates and independence
- Evidence rows b17/c03/c21 (Paltenghi), b18/c01/a18 (Li), b19/c02/c19/c20 (Kou), b08-b10 (Peitek ICSE21), c16/c22 (Copilot), c10/c24 (RepoNavigator), c09/c23 (CodeSense) repeat papers. Independent-source counts in claims.jsonl count papers, not rows.
- a05, a06, a04, a01 are read through the 1995 von Mayrhauser & Vans review, so classic claims rest on one secondary source.

## Contradictions between sources
- Busjahn (2015) found a strong novice/expert reading-order gap; Peitek (2020) did not reproduce it; Peachock found none. Code linearity matters more.
- Beacons: Wiedenbeck (1986) supports beacons; Siegmund/Peitek fMRI (N=11) found no beacon effect in four conditions. Both are small and different measures.
- LLM-attention alignment: alignment with human attention is low and does not predict quality (Li), yet attention-injection training still gives small gains (EyeLayer, EyeMulator). Alignment may not be the mechanism.
- Copilot study: performance up 50%, comprehension flat; but Qiao review reports high explanation accuracy for tutoring tools. Different tasks.

## Weak spots
- Human studies are small (fMRI N=11, eye tracking N=20, 25 developers) and mostly students; Wyrich shows low comparability across measures.
- Several LLM papers have unconfirmed authors (c04, c05, c08, c10, c16, EyeMulator) and 2026 preprints not peer reviewed.
- Most LLM studies test models of at most 8B parameters or older GPT-4 / Claude 3.5; no study found testing a scaffolded frontier agent with a reading strategy at equal tokens.
- No LLM study found that tests Brooks-style hypothesis-first reading versus bottom-up reading directly.
- Seen only in snippets: a25 (Kevic 32%/58%), a27 (ICSE 2025 n=27), b14-b16 (not opened), c05 (abstract only).

## GAPS
1. Does a hypothesis-first (Brooks top-down) reading prompt beat bottom-up or linear reading for an LLM agent on bug localisation at equal tokens? No direct test found.
2. Is the 1.5x-3x gain from hypothesise-test-amend (RHDA) still present for current frontier and reasoning models, or is it absorbed by built-in reasoning?
3. Can a name-blind restatement step remove the lexical-superstition loss (17-34% relative) without losing the useful information in names? Tested only with prompt/fine-tune interventions, which "persist".
4. Which Letovsky episode labels (read, ask-why, conjecture, simulate, verify) can be logged from agent traces reliably, and do they predict success? (Needed for the "episode labels" purpose.)
5. Does a coarse-to-fine navigation scaffold (tree, file, function) keep its gain on repos larger than SWE-bench and with strong models, and does fewer tools generalize beyond 7B?
6. Does the write-then-view (predict before reading) pattern, which separated high from low comprehension in humans (4.7x), improve LLM agent accuracy at equal tokens?
7. What was the exact percent-correct and N in Soloway & Ehrlich (1984) and Pennington (1987)? Primary papers not opened.
8. Is the human over-trust of wrong generated code (49% detection) mirrored by LLM self-verification false-accept rates on its own code?
9. Do semantics-preserving rewrites expose reasoning flaws (up to 60% flawed-but-correct) in frontier models, and can consistency across rewrites serve as a cheap verifier?
10. What do the ICSE 2025 student-attention papers (n=27) report beyond the snippet, and do they replicate the Busjahn reading pattern for summarisation?


## Gap search results

Searched with arXiv abs/PDF pages (the arXiv API, OpenAlex and Semantic Scholar were rate-limited; WebSearch budget exhausted; arXiv search pages returned nothing). Evidence is in evidence_d.jsonl (d01-d19). Only papers opened this session are used.

- Gap 1 (hypothesis-first vs bottom-up reading at equal tokens): STAYS OPEN. Nearest test is AutoSD (d09): hypothesis loop gave no repair gain over direct patching (76 vs 87, 113 vs 110 on Defects4J), 2023 models. Real execution results mattered (73% vs 63%).
- Gap 2 (RHDA-type gain on frontier reasoning models): PARTLY ANSWERED by analogy. Cheap prompt triggers ('Wait', +89% blind-spot reduction) are absorbed by reasoning models (d05). No direct RHDA retest on frontier models found. Stays open.
- Gap 3 (name-blind restatement): STAYS OPEN. Renaming helps weak models (+14 points) and hurts Gemini-3 (100 to 68.1) (d03), so names carry information in both directions; no restatement test.
- Gap 4 (episode labels from agent traces): STAYS OPEN. Only indirect support: localisation accuracy tracks resolve rate (d14). No validated labelling study found.
- Gap 5 (coarse-to-fine, bigger repos, strong models): PARTLY CLOSED for SWE-bench scale. Agentless hierarchy beats skipping levels (d11); LocAgent still gains in 2025 (d12, abstract only). Larger repos and fewer-tools-beyond-7B untested.
- Gap 6 (write-then-view for LLMs): STAYS OPEN. Rubber-duck explanation gives +2-3% to +12% (d10), a weak analogue.
- Gap 7 (Soloway & Ehrlich, Pennington numbers): STAYS OPEN. Neither paper could be opened (d17, d18). No figures should be cited.
- Gap 8 (LLM false-accept on own output): CLOSED with caveats. Strong convergent evidence of own-output blindness: 64.5% average (Sonnet 4 41.4%) on injected errors, 4.3-10.8% of natural errors catchable externally (d04); verifier blind spot 0.12-0.55 (d06); self-repair gains vanish at equal budget (d07). Mostly math, not code, and not a direct measure of the human 49%.
- Gap 9 (flawed-but-correct, consistency verifier): PARTLY CLOSED. Correction: the 10-50% flawed share is for open code models; GPT-5.2 and Gemini-3 show 0.2% (d01), yet frontier models drop up to 70 points under loop rewrites (d02). Consistency as a verifier is untested (only union coverage, d03). K09 updated.
- Gap 10 (ICSE 2025 student-attention papers): STAYS OPEN. Not located.

Claims changed: K09, K11, K13 extended; K18-K22 added. Confidence note: all new LLM numbers are from preprints and several use abstract-only reads (d08, d12, d13, d15, d16 marked in limits).
