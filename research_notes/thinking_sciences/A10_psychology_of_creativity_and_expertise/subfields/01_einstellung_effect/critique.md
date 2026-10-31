# Critique: Einstellung effect (A10.01), cross-check

## Limits of this check
- The C drive was full (0 MB free) and the arXiv export API returned HTTP 429 during this pass. I could NOT re-open the primary sources behind the top 10 numbers. The cross-check below is internal: the three evidence files (a, b, c) were compared line by line, raw counts were recomputed, and conflicts were resolved by arithmetic. Every "confirmed" below means "two or more independent evidence lines agree and the percentages match the counts", not "I re-read the paper".
- Re-opening is the first job for the gap searcher once disk and rate limits are fixed.

## Corrections made
1. b05 (time pressure): lists speedy C3/C4 as 0.99 and plain as 0.55. Wrong. a05 and the raw counts give 94/98 = 96% (speedy) and 100/153 = 65% (plain). Claim K05 uses the corrected values. b05 should be edited.
2. "Telling them Don't be blind made over half switch" (task brief): true only on C3/C4 (63% short method). On C1/C2 only 43% switched (87/153 still used the long method = 57%). Claim K03 states both.
3. "IQ unrelated": a06 says Luchins found no strong IQ/education effect, but Luchins and Luchins (1959) and Ross (1952) found the effect grows with age with IQ controlled. Marked contested (K11).
4. Plain-group N differs between comparisons (155, 153, 121) because Binz and Schulz compare each condition against its own matched plain group. This is not an error, but any pooled use must not mix them.
5. a22/b22/c03 give the same Only Connect numbers; consistent. a23 (Claude-Sonnet-4.5 baseline 42.09%) and c11 (trap rate 42.98%) are two different metrics; not a conflict.

## Numbers checked by recomputation (not by re-reading)
128/155 = 82.6%; 100/155 = 64.5%; 87/153 = 56.9%; 57/153 = 37.3%; 20/124 = 16.1%; 97/121 = 80.2%; 79/108 = 73.1%; 59/108 = 54.6%; 95/98 = 96.9%; 126/153 = 82.4%. All match the stated percentages.

## Contradictions between sources
- Haq et al. (2025) direct LLM order test: complex-first often IMPROVED shortcut accuracy (GPT-4o 0.33 to 0.66). That is the reverse of Einstellung. Six items per cell, so differences of one item are 0.17. This does not refute a set in LLMs; it fails to show one.
- MedEinst says stronger models are more fooled and size does not matter; Shidara et al. say strong reasoning models reach physician level on M-ARC. Different benchmarks, different construction (M-ARC hand-written 100 items; MedEinst generated from DDXPlus). Reasoning effort may be the real variable; no one has tested it on MedEinst.
- Crooks and McNeil (more than one set problem matters) contradicts Luchins' own claim that extra set problems add nothing, though Luchins' thesis tables show a dose effect from 2 to 10 problems. The claim of "no extra effect" probably refers to a narrower range.
- Chess: the effect is strong for the shortest-mate task (Bilalic) but Sheridan and Reingold find experts avoid a familiar move when it is a blunder. Boundary condition, not a contradiction.

## Weak spots
- Luchins (1942) monograph never opened; every Luchins number comes from Binz and Schulz's re-coding of percentages from thesis tables. Single point of failure for K01 to K05.
- Bilalic Exp 3, Saariluoma and the eye-tracking study use very small groups (5 to 12). The 148 vs 79 s result is not significant (p=.13).
- Thomas, Didierjean and Kuhn is a manuscript, not peer reviewed.
- MedEinst, Shidara, Guan, Gu and Shi, Haq are 2025/2026 preprints. MedEinst's mitigation gain comes from the authors' own system with no independent run.
- Binz and Schulz model: beta is hand-tuned per condition, so fit is not a strong test.
- No study found measures Einstellung in an LLM agent with a Luchins-style design at adequate N.

## Only seen in snippets or abstracts
b17 (Ollinger et al. 2008), b18 (DeCaro 2016), b19 (Blech et al. 2020), b28 (programming abstract), b29 (Guan abstract), c26 and a25 (Luchins 1942). Numbers not read.

## GAPS
1. Does a Luchins-style order manipulation (N of 50+ items per cell, blocked vs interleaved vs control) produce a measurable set in current LLMs and reasoning models, at equal tokens? Haq et al. is too small to say.
2. Does reasoning effort or thinking budget reduce Einstellung on a fixed trap set (M-ARC, MedEinst) more than model size does, and where is the break point?
3. Which intervention reduces LLM fixation at equal tokens: a warning line, a forced list of alternatives, interleaved examples, context clearing of rejected routes, or a second independent attempt? Human data (K03, K04) suggest interleaving beats warnings.
4. Does the human finding "dose of 1 already hurts" (Crooks and McNeil) hold for in-context examples in LLMs?
5. Does the fixation persist after a route is explicitly rejected in the context (Bilalic Exp 3, magic lure study)? Test whether LLMs repeat variants of a rejected approach.
6. Re-open and verify the Luchins thesis tables (via Binz and Schulz source or Luchins 1942) and the Bilalic 2008 Exp 1 and 2 tables; confirm Elo-odds figures (3.67 and 1.82 per 100 Elo).
7. Is the human age effect (Luchins and Luchins 1959, Ross 1952) real, and does it map to model capability or only to experience with a method?
8. Does multi-agent debate or self-consistency voting reinforce the shared prior (MedEinst) in non-medical Einstellung tasks, and is independent sampling with different framings better?
9. Do LLMs show the expert pattern (high confidence while not exploring) in their traces: can a trace-based detector of "claims to search, does not" be built (Bilalic gaze finding)?
10. Does time or token pressure raise fixation in LLMs as it does in humans (97% vs 82%)?


## Gap search results

How this pass was run: the web-search budget for the session was used up, and the arXiv API, OpenAlex and Semantic Scholar all returned rate-limit errors, so no new literature search was possible after the first two searches. I opened full PDF text of 18 sources (evidence_d.jsonl, d01-d18, opened:true) from arXiv ids and the two Brunel and OSF links already in the evidence files, and read three abstracts (d19-d21, opened:false). New claims K20-K27 were added; K11 and K15 changed status.

### Closed or mostly closed
- Gap 6 (verify the numbers): closed for chess. Odds factors 3.67 (Exp 1) and 1.82 (Exp 2) per 100 Elo re-read in the paper; they are two different problems (d11). Luchins counts re-checked against Binz and Schulz (d14); all hold. A new finding: the typo "0.99 vs 0.55" is printed in the Binz and Schulz paper itself, not only in our b05; the counts (94/98 and 100/153) are right. Still open inside this gap: the 1942 monograph was not opened, so Luchins' numbers are still second-hand.
- Gap 7 (age): mostly closed. Age effect is real in Luchins' own data (N=504, r=0.19, p<.001; d15). It is best read as longer history with one method, not as capability. The IQ half is still second-hand.
- Gap 5 (rejected route keeps its pull): partly closed. Reasoning models stay near the wrong draft even with an explicit error label (d01, d02); small models re-emit a failed call, and a "do not repeat" line does nothing (d05); reflection repeats the failure category in 85% of cases (d04). Open: frontier agents on tool tasks, and the exact Luchins-style design with a rejected method.
- Gap 8 (debate, voting): partly closed. Voting beats debate on average (d09). Errors are correlated across models, about 60% agreement when both are wrong (d10). Correction to K16: in MedEinst the debate agents had lower accuracy but slightly lower trap rates than the base model (d08). Open: voting versus differently framed prompts on Einstellung items.

### Partly answered
- Gap 3 (which intervention at equal tokens): no head-to-head found. Indirect evidence: warnings and explicit error signals are weak (d02); rewriting the draft helps sometimes (d03); describing a failure instead of quoting it removes 76% of the repeat effect in small models (d05). Interleaving is supported only by the human result (K04) and by the fact that example order moves LLM results (d20, abstract only).
- Gap 4 (dose): wrong-draft dose is monotone in LLMs (d01, appendix B.2), but a Luchins-style dose of same-method examples was not found. Many-shot work (d19, abstract only) shows dose changes behaviour in general.
- Gap 9 (trace detector): none built. Models verbalise their reliance rarely (d18), experts misreport their own search (d12), and reasoning traces fixate on early wrong answers at high difficulty (d17, with open critiques). A behavioural detector is a design proposal (K26), not a result.

### Still open
- Gap 1 (properly sized Luchins-style order test on LLMs): nothing new. Haq et al. re-read: exact match not strategy, six items per cell (d16). The experiment must be run by us.
- Gap 2 (reasoning effort versus size): no effort sweep exists in what I found. M-ARC used maximum effort only (d06); MedEinst shows no size gain and a weak positive link (r=0.49 by my calculation, n=15, not significant) between accuracy and trap rate (d07). K15 downgraded to contested: the claim "effort is the lever" is only a hypothesis.
- Gap 10 (token or time pressure): no study found that measures fixation against a token cap. Token-budget work (d21, abstract only) measures cost.

### Cautions from this pass
- Most new LLM evidence is 2026 preprints from single labs (contextual drag, feedback backfires, MedEinst). The small-model result (d05) covers 135M to 1.7B models only.
- MedEinst's text and its Table 1 disagree on the multi-agent trap rates; I used the table. Its trap rate is conditional on a correct control answer, which biases comparisons across weak and strong models.
- The tables in several PDFs extract badly; the numbers recorded in evidence_d were read from clean rows or from the paragraph text, and cases where I could not resolve a column (the HMMT24 fine-tune cell in d03) are flagged.
- No evidence file contained the 1942 monograph, Luchins and Luchins (1959) or Ross (1952).
