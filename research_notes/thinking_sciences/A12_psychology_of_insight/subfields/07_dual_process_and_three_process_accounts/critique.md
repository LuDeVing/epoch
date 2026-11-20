# Critique: A12.07 Dual-process and three-process accounts

## Numbers re-opened this session (full text, arXiv PDFs)
Confirmed: Hagendorff et al. CRT (humans 38%, ChatGPT-3.5 59%, GPT-4 96%, intuitive 80/15/0%, CoT 5%->28% and 80%->29%); S2A (62.8->80.3, 51.7->61.3); SwiftSage (84.7 vs 33.8/36.4/45.3); BRAINTEASER (ChatGPT 53/63, human 92, random 25); Mizumoto NazoNazo (7.6%, 17.6%, 52.9%, OR 2.29, verification failures 5.23-39.34%, Grok-4 29.5% vs 48.8%, p=.0071); d'Aliberti and Horta Ribeiro (6.31%, 2.57% vs 16.44%, +8.41pp 0.3221->0.4062).

## Corrections
1. a23 names the authors as Yax, Capdeville and Oudeyer. The paper is by Yax, Anllo and Palminteri (c11/c12 are right). Treat a23 and c11 as the same study, not two sources.
2. a23 numbers mix odds ratios and differences; use the paper's tables, not the a23 line.
3. c12 implies example prompts did not help humans. The paper says the example prompt raised human CRT accuracy by 0.14 (at the cost of intuitive answers). Only the reasoning prompt had no effect on humans.
4. c05: N=723,200 belongs to the entropy-versus-shift regression in the paper, not to the shifted vs non-shifted accuracy contrast. Do not cite it as the sample of that contrast.
5. c04: Grok-4 Japanese counts appear as 111 in one column and 112 in another in the paper itself; minor.
6. a20 (Cohen's d 0.946) and c02 (OR 2.29) are different metrics on different item sets (120 vs 201); not a conflict.
7. a/b/c duplicate sources: Hagendorff (b11-b13, c08-c10), Mizumoto (a20, a21, c01-c04), Webb (a04, b01, b02), SwiftSage (b17, c18), S2A (b18, c21). Independent-source counts in claims.jsonl collapse these.

## Contradictions between sources
- Warmth: Metcalfe and Wiebe (classic) vs Hedne et al. 2016 (no warmth difference). Unresolved.
- Insight as special process (Aha, restructuring) vs business as usual (Weisberg, Chuderski): the last two were seen as titles or framing only.
- Hagendorff: GPT-4 shows "hyperrational" behaviour; Yax: models still intuition-prone on fresh items. Memorisation of original CRT items is the likely gap.
- LLM insight parity (Orru, Zhang rebus) vs large deficit (Mizumoto, BRAINTEASER).

## Weak spots
- The founding Davidson and Sternberg 1984 study was never read beyond the abstract. No founding numbers exist in this folder.
- No LLM study tests the three-process account itself. Nearest proxies are S2A (selective encoding) and BRAINTEASER.
- Orru 2023: only 30 items, n=20 humans. Speed 2023: 5 insight items.
- Pupil study: 11 solvers.
- Many LLM papers are 2025-2026 preprints, not peer reviewed.

## Only seen in snippets, titles or abstracts
a01, a08, a13, a15, a16, b19-b26 (all unopened), b14, a25, a26, a28, c22-c25.

## GAPS
1. Does an explicit selective-encoding / combination / comparison prompt step beat plain CoT on BRAINTEASER and NazoNazo at equal tokens? (No one has tested it.)
2. What did Davidson and Sternberg 1984 and Davidson 1995 actually measure (N, effect sizes, training gains)? Needs full text.
3. Are model gains on BRAINTEASER-type items real reframing, or contamination and fine-tuning (SemEval 100% results)? Is there a fresh, uncontaminated set?
4. When does an externally forced reconsideration cue (entropy-gated) help beyond MATH-500, e.g. on lateral and riddle items?
5. Does thought-log verification failure (correct candidate generated and rejected) disappear with a candidate-retention rule?
6. Does forced verbalisation (long CoT) hurt LLMs on insight items as it hurts humans (Macchi 2025 double dissociation)?
7. Is the Aha-marker/accuracy relation in LLM traces (calibration of "wait") different by domain and temperature?
8. What do Chuderski and Jastrzebski 2018, Weisberg 2015 and Gilhooly and Murphy 2005 report in full, to settle special-process vs business-as-usual?
9. Has anyone replicated Macchi 2025 verbalisation and Laukkonen 2022 false-insight results outside the original labs?

## Gap search results (evidence_d.jsonl, d01-d17)
Web search budget ran out after 3 queries and the Semantic Scholar, OpenAlex and arXiv APIs returned rate-limit errors, so work relied on page fetches.

1. Selective-encoding/combination/comparison prompt vs plain CoT: STILL OPEN (no direct test). Nearest proxies: step-structured CoT was worse than direct on GPT-3.5 (62.5 vs 75.0, n=120; d04); explanatory few-shot CoT helped GPT-4 (76.7 to 90.0; d05). Neither is equal-token. New claim K20.
2. Davidson and Sternberg 1984: STILL OPEN. Only the abstract is reachable (d01); no N or effect sizes. Davidson 1995 reports 12-13% of non-insight problems with an insight warmth pattern (via d03).
3. Contamination vs real reframing: PARTLY CLOSED. No uncontaminated lateral set exists; word-puzzle scores jump 53.5 to 84.4 with five examples (format learning; d06); top SemEval 98.3 came from tuned systems (d05, d07); NazoNazo authors argue against memorisation but propose a private rotating set (d08). Claim K21.
4. Forced reconsideration beyond MATH-500: PARTLY CLOSED. Crosswords +0.45 pp, Rush Hour about 0 (d10); riddles and lateral items untested.
5. Candidate-retention rule: STILL OPEN. NazoNazo only suggests it (d08).
6. Forced verbalisation hurting LLMs on insight items: PARTLY CLOSED. CoT hurts on 3 of 6 verbal-overshadowing-style tasks (d11) and long reasoning can lower accuracy (d12), but no insight items. Human evidence is itself conflicting (d13). Claims K05 (now contested), K22.
7. Aha-marker calibration by domain and temperature: CLOSED for the d'Aliberti data (d09): harmful in math at every temperature, not significant in crosswords; no riddles. Claim K23.
8. Chuderski, Weisberg, Gilhooly and Murphy full results: STILL OPEN. Only secondary summaries (d15; d16 unopened, 51.8% and 84.6% unverified).
9. Replications of Macchi 2025 and Grimmer 2022: STILL OPEN as outside replications. Verbalisation literature conflicts (d13); Grimmer has an in-lab Exp2 (d14). Correction: the false-insight paper is Grimmer, Laukkonen, Tangen and von Hippel 2022, not Laukkonen 2022. Claim K24.
