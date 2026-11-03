# Critique: Working memory and Gf (A13.03)

Cross-check done 2026-11-03. Re-checks used abstracts via OpenAlex/Crossref (Semantic Scholar was rate-limited, arXiv API returned nothing). Full-text re-opening was not possible for most items.

## Corrections made / numbers re-checked
1. Ackerman, Beier, Boyle 2005: confirmed 86 samples, true-score WM-g r = .479 (abstract). The .36 quoted by Colom 2006 is the WM-Gf figure, not WM-g. The CI .44-.52 was not re-verified.
2. Kane, Hambrick, Conway 2005: corrected. Abstract says 14 data sets from 10 published studies, more than 3,100 subjects, MEDIAN r = .72 (about 50% shared variance). Evidence a09 said "r = .72" and b13 said "weighted latent correlation, N about 3,000". Use "median .72, N > 3,100". The "range .41-1.00" in a09 was not re-verified.
3. Kyllonen and Christal 1990: abstract not retrievable. N = 723/412/415/594 and r = .80-.90 rest on a web summary plus Hagemann 2023 (which was opened). Treat as second-hand. b11 (from recall) is NOT independent of a01.
4. IFScale (Jaroslawicz 2025): abstract says the best frontier model reaches only about 68% at 500 instructions. Evidence lists o3 62.8% and grok-3 61.9% as top, so some other model is higher (not identified). Do not call o3 the best.
5. Gong, Wan, Wang: published AAAI 2024 (vol 38 no 9); preprint 2023. Entries a19, b15, b16 and c01-c04 are ONE paper counted many times. It is one source, not many.
6. de Langis et al: published EACL 2026 long papers (preprint 2025); numbers unchanged. a28 vs a20/c06: Hu and Lewis counted twice, one source.
7. Xiong et al 2026 (arXiv 2604.09670): abstract confirms two-layer transformer solves the task perfectly and diverse LLMs show human-like decline and association with capability. Exact r values were not re-verified.
8. Au et al 2014 meta-analysis title confirmed (Psychon Bull Rev). g = 0.24 and the dispute were not re-verified. Melby-Lervag 2016 abstract could not be retrieved; its numbers rest on the opened evidence line b01.

## Contradictions between sources
- Latent WM-Gf: .90 (K&C) vs .59 (Engle 1999) vs .60 (Conway 2002) vs .72 (Kane median) vs .479 (Ackerman, WM-g, with weaker measures). Spread is due to task purity, content overlap, speeding and sample range, not noise alone.
- Colom 2006 found WM-intelligence r = .20 (N = 229, air traffic applicants) in a range-restricted sample; most others found much more.
- LLM n-back: Gong 2024 says ChatGPT limit like humans (n about 3); Hu and Lewis show scale and curriculum push 70B models to 8-10 back. The "human-like limit" is model-dependent, not fixed.
- Parameters predict span in de Langis (r = .82, six models) but not N-back in Xiong (10 models).
- WM training meta-analyses: Au g = .24 vs Melby-Lervag g = .05 (active controls).

## Weak spots
- No source tests whether a prompt-level capacity manipulation raises reasoning at equal tokens. All LLM n-back results measure memory, not a link to reasoning scores inside LLMs. The human claim (capacity limits reasoning) is not shown to carry over.
- The cross-LLM correlation of n-back with benchmarks (Xiong) is on 10 small open models, non-thinking mode.
- Several claims have one independent source (IFScale, de Langis, RULER, 591-LLM study).
- Many "N-back" LLM studies share an author group and prompt format.

## Only seen in snippets / not opened
a01, a10, a11, a12, a14 (blog summary), a25 (Dokic 2025, no figures at all), b11-b14, b24-b27 (Wikipedia or recall). Exact d-prime values are in figures only.

## GAPS
1. Does an external written working state (S-states) raise accuracy on rule-heavy items at equal tokens, and does gain scale with rule count? No LLM study measures this directly.
2. What are the figures in Dokic, Koso-Drljevic, Bilalic 2025 (the named key work)? Not read at all.
3. Does the WM-Gf link appear inside LLMs: do models with better N-back or span also do better on matrix reasoning, controlling for size and thinking mode?
4. Does the I-RAVEN-X collapse follow rule count / attribute range the way Carpenter 1990 predicts for humans?
5. What is the collapse point for frontier thinking models on rule-following (above 500 rules) and does a checklist re-pass move it?
6. Re-open Melby-Lervag 2016 and Au 2014 PDFs to settle the 0.05 vs 0.24 gap by comparing control types.
7. Which model achieved about 68% in IFScale, and how do Claude-class models degrade with density in thinking mode?
8. Does the process overlap account (Kovacs and Conway 2016) make a distinct prediction for LLMs (shared bottleneck vs many limits)? b27 was recall only.
9. Is restraint vs constraint attention control (Kane 2016) mirrored in LLMs: is suppressing distractor rules separable from holding rules?
10. Kyllonen and Christal full text: exact task list and the content-overlap sensitivity analyses.

## Gap search results
Gap search done 2026-11-03. New evidence is in evidence_d.jsonl (d01-d17). Search tools: arXiv API, Semantic Scholar and OpenAlex were all rate-limited, so work used direct PDF downloads (arXiv, ACL Anthology, PMC), Crossref and PubMed. No WebSearch call succeeded (budget used up).

1. External written state at equal tokens, scaling with rule count: STAYS OPEN. Indirect support only. MAKER (d07) solved 1,048,575 Hanoi steps with zero errors by passing next_state each step plus voting; Zhang 2024 (d08) got +35.4 points on state tracking from a chunked status list. Neither holds tokens equal nor varies rule count. Illusion of Thinking (d06) shows the single-run collapse that explicit state avoids.
2. Dokic, Koso-Drljevic, Bilalic 2025: STAYS OPEN. DOI 10.1016/j.intell.2024.101874 found in Crossref (no abstract), ScienceDirect returns 403, Europe PMC has no copy. No figures read. Do not cite numbers from it.
3. WM-Gf link inside LLMs: PARTLY ANSWERED. Xiong 2026 (d09, re-read): N-back vs MMLU-Pro r .78, GPQA Diamond .88, IFEval .69 (autoregressive), 10 models, non-thinking, size not a predictor. No matrix-reasoning test, no thinking-mode control, no partial correlation. Still open for Gf-type items.
4. I-RAVEN-X vs Carpenter rule-count: CLOSED, answer is no. I-RAVEN-X varies grid width (3x10) and value range (50-1000), not rule count (d04). Old LLMs drop on arithmetic rules with range (GPT-4 arithmetic 73.6 to 8.4). For reasoning models the large drop comes from perceptual noise, not range (d05): o3-mini 86.6 to 81.0 on clean range 1000, to 17.0 only with max noise. Claim K19 and evidence c24 corrected.
5. Collapse point above 500 rules and checklist effect: PARTLY ANSWERED. IFScale stops at 500 (d01, d02); no source goes beyond. Checklist re-pass: STICK +3.8 for Command-R+, +0.8 for GPT-4o on LiveBench, Self-Refine hurts (d03). Not tested on dense-rule prompts or Claude. Open: collapse beyond 500 rules.
6. Melby-Lervag vs Au: CLOSED as to cause. Control type (Q(1)=6.09, p=.01), baseline adjustment, n-back-only scope, age range 18-50 (d10, d11, d12). N-back with treated controls g=0.15 comes from five small single-test studies with control drops. Au's own g=0.24 and active-control split were not retrieved (paywalled).
7. Which model gave about 68% in IFScale: MOSTLY CLOSED. Text lists o3 62.8% and grok-3 61.9%; the garbled appendix table shows 68.9% in a row beside gemini-2.5-pro; gemini-2.5-pro and o3 are named the top two. Treat gemini-2.5-pro as likely, not certain. Claude models at 500: 3.7-sonnet 52.7%, opus-4 44.6%, sonnet-4 42.9%, linear decay; thinking mode gives moderate gains (figure only).
8. Process overlap vs shared bottleneck in LLMs: STAYS OPEN. Kovacs and Conway 2016 itself was not opened (paywalled); only a connectome study of N=297 (d16). No LLM test exists. The LLM prediction written in d16 is inference.
9. Restraint vs constraint in LLMs: STAYS OPEN. No LLM study. Human side: Lee and Engle 2026 preprint (d14, abstract only) says avoiding rejected hypotheses depends on Gf and disengagement, not WMC. The Kane 2016 citation could not be tied to the restraint/constraint wording (d15 unopened).
10. Kyllonen and Christal full text: STAYS OPEN. Not retrievable in this session.

Claims changed: K05 (note), K09 (rewritten), K10, K14 (rewritten with numbers), K16 (rewritten, now 2 sources), K17, K19 (corrected). New claims K22-K28.
