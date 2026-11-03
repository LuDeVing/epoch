# Critique: A07.03 Working memory guidance and biased competition

## Corrections made (sources re-opened this session)
Re-opened and checked against the paper text: Shi et al. 2023 (arXiv 2302.00093), Liu et al. 2023 (2307.03172), Niu et al. 2025 (2505.09338), Adaptive Distraction (2502.01609).
- Shi et al.: table values confirmed (COT micro 72.4, macro 6.0; COT+INST micro 77.8, macro 15.0; COT+SC micro 88.1, macro 30.0; LTM+SC micro 93.4, macro 45.0). The text gives two different statements: "no more than 18%" of baseline-solved base problems stay solved for all distractor types, and "fewer than 30%" of base problems consistently solved. These are different denominators. Evidence a31 and b17 mix them; read 18% as share of baseline-solved problems and 30% as share of all base problems for the best settings.
- Liu et al.: 56.1/88.3 (GPT-3.5) and 48.3/76.1 (Claude-1.3) confirmed; 1.5% gain from extra documents confirmed; ">20% drop in the worst case" confirmed.
- Niu et al.: logit shifts +4.08 (related), +4.92 (irrelevant), correct-token +0.75/-1.23 confirmed. Head range: text says 3.2% to 10.7%; table minimum is 2.9% (country-language). a33 and b20 differ only because of this. Country-capital 36 heads (3.5%) and gap 7.69 to 13.20 confirmed.
- Adaptive Distraction: 0.843 to 0.323 (52.0% drop), Claude-3.5-Sonnet 0.879 to 0.495 (38.4 points absolute), static GSM-IC 1.8% confirmed. The abstract's "over 45%" is a different rounding, not an error. Note "38.4% drop" is absolute points, not relative.
- Not re-verifiable here: Woodman and Luck 2007, Soto and Humphreys 2008, Hollingworth and Beck 2016, Sawaki and Luck 2011 (paywalled; OpenAlex gave no open PDF). Their numbers rest on the earlier agents' reading. Treat as single-read.
- Status adjustment: Shi et al. claims are marked single-source (a31, b17, c01 are all the same paper, not independent).

## New items seen only in arXiv listing (not read)
A 2026 listing shows "Sentence-Level Contextual Entrainment in LLMs" (2606.24077), "From Relation-Specific Heads to Shared Interventions" (2610.18674) and ENTRAP-VL (2607.20092). They extend entrainment and are not in the evidence files.

## Contradictions between sources
1. Load: Woodman and Luck (3 items, benefit of 67 ms) vs Soto and Humphreys (1-2 items, cost) vs Hollingworth and Beck (load 2 with one match, no reliable capture). The best reconciliation (number of matching items, template state) is supported but the "load" variable is confounded with item count and memory accuracy (84.6% vs 68.4%).
2. Presence vs match: Match-0 vs No-Color was not reliable in the gap task (p=.20, .29) but was in the singleton task, so task type moderates it.
3. Kukreja 2026: related distractors hurt less with scale while random ones hurt more; this conflicts with a simple "bigger is more robust" story.
4. Contextual entrainment is largest for irrelevant tokens (+4.92) in Llama-3.1-8B, which is not a similarity effect; this differs from the human feature-match account and from Wu/Yoran (related hurts more).

## Weak spots
- Human sample sizes are small (N=10-24); one key contrast is p=.077.
- No LLM study tests load theory vs biased competition directly (c27). All LLM links are analogy by a similarity or position effect.
- Opened:false lines (Desimone and Duncan 1995, Chelazzi 1993/1998, Downing 2000, Olivers 2006, the 2026 capture papers a27-a30, model papers a24-a26) carry no numbers; founding-study numbers are missing.
- Cross-lab claims about the 2026 capture papers come only from abstracts.
- c15 (ICE) has a floor effect (0% in clean controls), so it says nothing about load.

## Only seen in snippets
a01-a05, a14-a16, a19, a22-a30, b09-b16, c20-c26.

## GAPS
1. Does a held lesson that matches a distractor raise the agent's error rate more under high task load than low load (the direct load-theory vs biased-competition test), at equal tokens?
2. Is bias driven by the number of lessons that match the distractor rather than the number held (Hollingworth and Beck pattern), in an LLM agent?
3. Do "do not" (negative-template) lessons help or hurt an LLM, given the human nulls?
4. Does restating a lesson every step (active template) increase distractor-following relative to showing it once, and does repetition make the bias shrink as in the human data?
5. What are the exact numbers in Desimone and Duncan 1995, Chelazzi 1993/1998 and Downing 2000 (founding studies were never opened)?
6. Which of the 2026 capture papers (Hautekiet; Kim; Liu; Won and Zhang) report boundary conditions that change the conclusions, and with what effect sizes?
7. Does the 2026 contextual-entrainment work (sentence-level; shared interventions) show a method to suppress entrainment that an agent scaffold can use?
8. Does position of the held lesson (start, middle, end) interact with similarity to the distractor, at equal tokens?
9. Does a late rejection step (analogue of the Pd marker) filter matching distractors without cost to correct use?
10. Are there any LLM studies of recency or lag decay of a held lesson's influence (analogue of Sasin and Nieuwenstein)?


## Gap search results
Search conditions: WebSearch budget was exhausted for this session; the arXiv, Semantic Scholar and OpenAlex APIs returned HTTP 429. Europe PMC and direct arXiv PDF downloads worked. Evidence is in evidence_d.jsonl (d01-d16). Absence of a study below is weak evidence.

- Gap 1 (load x match in an LLM agent): OPEN. No study found (d14). Needs our own test.
- Gap 2 (number of matching lessons vs number held): OPEN (d15). Human pattern stays the only evidence.
- Gap 3 (negative "do not" lessons): PARTLY CLOSED. NeQA (1,428 items) shows larger models fall below random on negated questions and answer the un-negated association (d12). Together with the human nulls (K11) the best reading is that naming the forbidden item primes it. Not tested on lessons. Newer RLHF models were not read.
- Gap 4 (restating every step): OPEN, one indirect hint. Pattern Match Suppression (d13) shows repeated context beats an explicit instruction. No restate-vs-once test.
- Gap 5 (founding studies): PARTLY CLOSED. Chelazzi 1993 and 1998 and Downing 2000 abstracts read (d01-d03): 2-5 choice items, 90-120 ms and 150-200 ms timings. Desimone and Duncan 1995 not opened (d04). Cell counts, N and probe RTs still missing because full texts are paywalled.
- Gap 6 (2026 capture papers): CLOSED at abstract level (d05-d08). Boundary conditions: a task-switch cue does not remove capture (Hautekiet); matching distractors cost time but not accuracy (Kim); cost arises after fixation and higher WMC lowers dwell (Liu, Wang, Liu); feature search raises capture vs singleton mode (Won and Zhang). Effect sizes not obtained. K27 changes the prediction: expect extra steps, not extra errors.
- Gap 7 (suppressing entrainment): CLOSED with a negative for scaffolds. Both 2026 papers (d09-d11) use white-box head masking (2-4% of heads; -2.3 clean accuracy vs -6.8 per-relation; with-context +1.5 to +7.9). Instruction tuning cuts damage 40-70% but leaves 4.5 to 15.3 points. No prompt-level method found.
- Gap 8 (position x similarity): OPEN (d15).
- Gap 9 (late rejection step): OPEN as a direct test; human support is indirect (d06, d07, d16).
- Gap 10 (lag decay in LLMs): OPEN (d15). Laban 2025 (c09) stays the nearest item.

Status changes: K15 and K16 raised to established (three and two independent sources; Liu and Chu, Zheng and Shi confirm Niu and Kukreja). K11 text extended (LLM negation evidence). New claims K25-K29. Note: the three 2026 entrainment papers (Liu and Chu, Zheng and Shi, ENTRAP-VL) overlap in method with Niu et al.; ENTRAP-VL was not read.
