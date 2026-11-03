# A19.01 Analytic vs holistic thought: cross-check critique

## Numbers re-opened this session (confirmed)
1. Jin et al. 2023 (arXiv 2308.14242 table): AHS GPT-3.5 5.35 (SD .11), GPT-4 5.01 (SD .10) vs norm 4.87 (SD .49, N=702); DSS GPT-4 3.97 vs 4.00, p=.344; TCT 0.87 / 0.85. Confirmed (a24, b15, c01-c03).
2. Atari et al. 2023 PDF: r=-.70 (49 nations), rho=-.72, B=-0.90 (SE .16), GPT queried 1,100 times with 20 triads, closest to Netherlands, Finland, Sweden, Ireland. Confirmed (a26, c05, c06).
3. Na et al. 2010 (PMC): mean r=0.038, median 0.040, first factor 10.69% vs 10%, published mean d=0.62 (cognitive style) and 0.54. Confirmed (b05, b06).
4. Evans et al. 2009: fixations on focal object M=7.16 vs background 1.53 and longer on object (283 vs 232 ms) in both groups. Consistent with b07. Confirmed that the page is a failure to replicate; the 22+22 sample size was not re-seen in the text I extracted, so keep b07's N as likely but unchecked.
5. Roberts 2015 commentary: Mantel r=0.27, p=0.02, 10,000 permutations, 40 varieties, 18 provinces. Confirmed (b12).
6. Talhelm 2014 N: the Frontiers commentary says 1162 undergraduates. This confirms the N in a21 and upgrades b23 (it was marked unverified). Participants were students, not general population.
7. Priming study 2017: n=84 and n=135, larger than 74% and 89% of the 104 experiments in the Oyserman and Lee meta-analysis. Confirmed (b13).

## Corrections and inconsistencies in the evidence files (not fixed in place, noted here)
- Fish-scene background gap: a03 says about 70 percent (2001 review), a14 says 65 percent (2003 review). Same study quoted twice with different figures. Use "about 65-70 percent more background statements" and do not treat as exact.
- Hu et al. 2026: the figure 8.10 appears as the Chinese model's landscape object count (c13, d=1.01) and as the US model's categorization relational-minus-categorical score (b19, c15). Possibly two real values coinciding, possibly a copy error. Also a29 gives horizon d=0.34 and c13 repeats it. Needs a check against the paper before use. Not re-opened (paper not reachable).
- Sabir et al. 2025: b18/a27 say Japanese set "up 47 points from COCO", but 73.4 minus 28.6 is 44.8 and 63.9 minus 23.6 is 40.3; a28 says "about 13 points" for the translation shift while the table gives 12.34 to 27.54 (15 points). The 13.21 is a ratio-based figure. Treat the headline numbers as approximate. Also COCO 1K holistic share (22.6/24.6) vs 5K (19.2/23.6) differ by sample.
- Eye tracking: a17 says 25+27 recruited, 21+24 analysed; the t(43)/F(1,43) degrees of freedom match 45 analysed. OK.
- c27 (my predecessor's synthesis) lists Hu as "US model more relational"; that holds for categorization only. On scene description the Chinese model was more background-heavy (d=2.42). The direction depends on the task.

## Contradictions between sources
- Perception: Masuda/Chua (more background) vs Evans (no difference, both look at the focal object). Unresolved; Evans used the same kind of stimuli and ROC analysis.
- LLM direction: Jin (holistic) vs Atari (WEIRD-analytic) vs Hu (US model more relational on triads) vs Sun & Wang (language effect fragile). Same paradigm, different prompts, different verdicts.
- Rice theory: original effect vs imbalance and Galton critiques; re-analysis (b11) says holistic thought stays significant, the individualism measure weakens.
- Priming: Oyserman and Lee meta-analysis reports effects; 2017 and 2023 larger studies find none.

## Weak spots
- The founding paper is a narrative review with student samples and no pooled effect size; almost all numbers come from secondary reports.
- Within-person coherence is near zero (r=0.038), which undermines treating "holistic" as a thinking mode that a scaffold can switch on.
- Every LLM study queries a model once per prompt wording with small n or few items; no study ties holistic style to accuracy on a task.
- Hu et al. is by authors close to the original theory, and effect sizes (d=2.42) are on generated counts with temperature 1; unclear if robust to prompt wording.

## Seen only in snippets or not opened
- b22 (Masuda and Nisbett 2001 numbers), b24 (Oyserman and Lee 2008 effect sizes), b25 (11-country null, press summary), b26 (Czech preregistered study), c23-c26 (unopened cites), a31 (Choi 2007 scale reliability).
- Hu et al. 2026, Sun & Wang 2025, Sabir 2025, Lu et al. 2025: opened by earlier agents; I could not re-open them (arXiv API returned empty responses, Semantic Scholar rate limited), so their numbers are carried over unchecked.

## GAPS
1. Does forcing a second framing (object/category/rule vs field/relation/context) in O6/O8 raise accuracy on a non-cultural reasoning benchmark at equal tokens, versus a second sample of the same framing? No study tests this.
2. Which task types, if any, favour a holistic framing (ambiguous context, covariation, change prediction) versus analytic (rule-based, formal logic)? Human data on task-framing fit with accuracy is thin; the original work compares groups, not accuracy.
3. Do LLM cultural-style scores vary more across prompt wordings than across models? Needs a multi-wording, multi-model, many-item replication of the triad and AHS tasks with pre-set analysis.
4. Does the Hu et al. numerical record hold (8.10 duplicate, d values)? Re-open the paper and verify each task.
5. Is the Evans null on eye movements resolved by later large or preregistered replications? Search for 2010-2024 replications of Chua et al. and Masuda-Nisbett recognition.
6. What do the 11-country (about 1,000 participants) and Czech preregistered studies (b25, b26) actually show; are the measures reliable enough (alpha) to be used as probes for the agent?
7. Do Oyserman and Lee priming effects survive bias correction in the meta-analysis (b24), and does prompt-level "priming" of an LLM behave like human priming?
8. Does the multi-persona debate gain (c21) come from cultural diversity or just from more samples plus aggregation? An equal-token control with same-persona agents is missing.
9. Is the dialectical (Middle Way, accept contradiction) component of holism, which maps to the schema's handling of contradictions, replicated separately from the attention component, given the weak inter-measure correlations?

## Gap search results
Sources: Hu et al. PDF, PubMed abstracts and PMC full texts (OpenAlex, Semantic Scholar, arXiv API and WebSearch were rate limited or out of budget). Evidence in evidence_d.jsonl (d01-d19). Claims K18-K22 added; K03, K04, K08, K11, K16, K17 updated.

1. Forced second framing vs second sample at equal tokens: STAYS OPEN. No study tests it. Closest: step-back abstraction prompting (d19, big gains on physics/chemistry/TimeQA, none on StrategyQA), and multi-agent debate studies (d17, d18) showing sampling (Self-Consistency) beats debate at equal compute. The equal-token test remains the one to run.
2. Task types that favour holistic vs analytic: PARTLY CLOSED for analytic. Abstraction-first helps principle-heavy tasks and not StrategyQA (d19). Human data: goal relevance beat culture in change detection (d09). No test of a holistic framing on any task; still open.
3. LLM style variation across wordings vs models: STAYS OPEN. Not re-run; no multi-wording replication found. Hu et al. (d01-d04) show direction flips by task within one model pair, which supports (not proves) that task and prompt matter more than model origin.
4. Hu et al. numbers: CLOSED. Verified from the PDF. 8.10 is Task 1 Chinese object count (d=1.01), Task 4 US categorization score (d=1.38) and the Task 6 t statistic; all genuine. Horizon d=0.34 is Task 1. Task 2 text description favours the Chinese model (d=2.42). The earlier "possible copy error" is withdrawn.
5. Large or preregistered replications of Chua/Masuda-Nisbett: PARTLY CLOSED. Czech vs Taiwanese eye tracking (d07, 60+69) found small differences in the predicted direction but unrelated tasks; UK vs Malaysia change detection 2025 (d09) found none; the 11-country preregistered perceptual study (d05) did not follow theory. No direct large replication of Masuda-Nisbett recognition found. Evans null is neither confirmed nor overturned.
6. 11-country and Czech studies: CLOSED. Identified as Lacko et al. 2025 (N=993) and Lacko et al. 2023 (N=392). Self-report AHS has unsatisfactory factor structure; Navon and embedded-figure tasks are usable (d05, d06). AHS is not a safe probe for the agent. Exact alpha values not extracted.
7. Oyserman-Lee bias correction and LLM priming: STAYS OPEN. No bias-corrected re-analysis found (d11). Magid 2017 (d10) is a further null for activity priming; Jurkat 2021 (d12) shows verbal primes shift description in children. Prompt priming in LLMs untested here.
8. Multi-persona gain vs more samples: PARTLY CLOSED. Generic debate fails to beat CoT/SC at equal compute; Multi-Persona 0% win rate vs CoT and about 7% worse in a second study (d17, d18). The cultural-persona debate (c21) still lacks its own equal-token control, so its gain is likely sampling plus aggregation, unproven.
9. Dialectical component separate from attention: PARTLY CLOSED. Replicated at country level (k=139, N=23,629) and as separate Midway and Contradiction dimensions (d14, d15, d16); Perception of Change did not fit. No link to reasoning accuracy.
