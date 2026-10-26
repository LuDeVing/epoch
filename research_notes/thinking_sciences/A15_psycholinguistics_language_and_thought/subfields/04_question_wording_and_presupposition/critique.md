# A15.04 Question wording and presupposition: cross-check critique

## Numbers re-opened against the source text (this session)

Confirmed exactly (source text or PDF read): Loftus & Palmer Exp 1 verb means and F'(5,55)=4.65; Exp 2 glass table (16/7/6 of 50) and chi2 7.76; QA2 Table 4; Sharma et al. "up to 27%"; Chan et al. 2024 group means; Cancer-Myth 585/150/43%/80%/41%; CREPE 8,466 / 26.0% / F1 66.3 and 67.1; Zhou 2026 (87.93 vs 54.16 km/h, 29 smashed and 31 hit); Hickman 2017 (39.63 vs 47.75, t=-1.21, df 18); McCloskey & Zaragoza original 37% vs 72% and modified 72% vs 75%; Weinberg et al. cell proportions and F(1,327)=25.42; Lindsay & Johnson 5.52 vs 2.67 and 2.56 vs 2.41; Turpin -36.3%; Sclar 76 points, median 6.4 for GPT-3.5, 7.5 across tasks.

Not independently re-checked (taken from earlier agents): Murphy & Greene effect sizes, Michael & Garry, O'Donnell meta-analysis, the two 2025 Sci Rep warning studies, Cheng ELEPHANT, Echterhoff, Webson & Pavlick, Mizrahi.

## Corrections and clarifications

1. b10 vs c04 (QA2): not a contradiction. b10 gives zero-shot figures (text-davinci-003 0.40 questionable, 0.56 valid, 0.48 overall); c04 gives in-context figures (0.50, 0.62, 0.56 overall). Claims must name the setting. Do not quote "56%" without "with demonstrations".
2. b11 vs c05 (QA2 decomposition): b11 quotes the questionable-assumption column (0.50 to 0.36); c05 quotes the overall column (0.56 to 0.45). Both correct. The questionable-only drop is the one that matters for S1.
3. Sharma "27%" is two different results: suggesting a wrong answer drops accuracy by up to 27% in LLaMA 2; "are you sure" drops it by up to 27% in Claude 1.3. Keep them separate (b14 and b15 do; c08 is ambiguous).
4. Sclar spread: b20 says median 7.5 points, c14 says about 10 on average. These are different statistics (median per task vs mean). Use the median, and say "up to 76" only as a maximum.
5. a20 Zhou: the 69.0% false-glass rate has no control group and uses a different clip; do not compare it to Loftus 32%. Absolute rates differ by about 2x, only the direction replicates.
6. a21: the FORRT "2017 failed replication (sport)" was never opened. The only 2017 replication located is Hickman (a19), a psychology writing sample, N=20, not sport. Treat a21 as unresolved.
7. Loftus & Palmer Exp 2 had a 4-second accident clip and Exp 1 used student estimates after 7 films; the often-cited "50 per group" applies to Exp 2 only. a01 N=45 is Exp 1.

## Contradictions between sources

- McCloskey & Zaragoza (no memory change under a modified test) against Loftus, Schooler & Wagenaar (more sensitive test shows a small effect; snippet only, not opened). Unresolved, see K05/K06.
- Weinberg et al. found a residual deficit on a test they designed to exclude guessing; M&Z argue that test still permits guessing. Unresolved.
- Source-monitoring accounts (Lindsay & Johnson) vs trace-alteration accounts (Loftus): L&J data favour coexistence of both traces, with the error in attribution.
- Warnings: reduce but do not remove the effect, less so when tested by recall (Wikipedia summary of Blank & Launay 2014; not read in the original).
- Reasoning: Fan et al. find reasoning models burn tokens on missing premises; Sathyanathan et al. find reasoning improves detection only by 2-11 points. Compatible, both say reasoning does not fix the premise problem.
- Wei et al. and Sharma agree sycophancy rises with scale, but Wei's fine-tuning fix is a training result and cannot be used by a scaffold-only agent.

## Weak spots

- Almost all human evidence is on students with short films, and several of the replications are tiny (N=20, N=28, N=60).
- No LLM study runs the Loftus-Palmer manipulation itself. The LLM evidence is about false premises, sycophancy and prompt formatting. These are adjacent, not the same mechanism: whether a verb alters a model's recalled fact is untested.
- Most false-premise LLM numbers are 2022-2023 models (text-davinci-003, PaLM). Modern frontier models appear only in Cancer-Myth and Sathyanathan, and both use LLM or expert-labelled judges.
- Fixed-accuracy measures often ignore the false-flag cost; only Cancer-Myth reports it.
- The Zwaan 2025 note that there is no large preregistered replication means the human anchor effect size is itself uncertain.
- Mediation (K04) and ordered-question effects (K24) are single-lab.

## Seen only in snippets or second-hand

a13 (Loftus & Zanni 1975 headlight figures), a14 (Loftus, Miller & Burns 1978 cells), a15 (Harris 1973), a21 (FORRT atlas), a23 (Kaur et al. 2024), a27 (earlier false-premise QA citations), b25 (M&Z via the 2024 review), c11 (Perez et al. 2022), c21 (Xie et al. 2024), and the Loftus-Schooler-Wagenaar reply.

## GAPS (most decision-relevant first)

1. Does a leading verb or adverb inside a question change a modern LLM's reported fact (the Loftus-Palmer manipulation run directly, with many items, several verb strengths, and a control)? Nobody has published this.
2. Does a code-side neutral rewrite of the user query (strip the stated belief and presupposition) beat answering the raw query at equal tokens on current frontier models, and what is its false-flag cost on clean questions?
3. Does the effect of loaded wording survive the McCloskey-Zaragoza control in LLMs, that is, is the harm a changed answer or only a pull toward the offered option when unsure?
4. Does a source-tag step (label each claim as from-source or from-prompt-wording) remove loaded-prompt errors in LLMs as it did in Lindsay & Johnson?
5. How large is the Loftus-Palmer effect in a large, preregistered human replication (the Zwaan-proposed N about 2000 study) and in the FORRT-listed 2017 failed replication?
6. Which of presupposition strength, repetition across turns, and user authority drives the dose-response in current reasoning models, and does repeated exposure to a false premise within one session compound the effect (O'Donnell g=0.38 for humans)?
7. Does the premise-check split (extract assumption, then verify) beat one-shot detection on modern models, given that older models were near chance at detection but better at verification?
8. Do warnings placed before the task versus after the answer differ for LLMs as they do for humans (equal in Sci Rep 2025, immediate better in interpolated-test design)?
9. How much of a long-context agent's S1 error comes from a false premise carried in earlier turns of the conversation rather than in the current question?


## Gap search results

Search limits: the shared web-search quota ran out and the OpenAlex, Semantic Scholar and arXiv APIs returned 429, so the gap search used arXiv title search pages and direct paper pages, read through a fetch tool. Evidence is in evidence_d.jsonl (d01-d25). Pages were summarised by a fetch tool; the first 100,000 characters of long pages were read.

1. Verb or adverb in a question changing an LLM's reported fact: STAYS OPEN. No paper runs a graded verb ladder with a control. Closest: FramingQA (d14, 54,756 questions, 9 open models: framed question shifts answers sharply, premise-only framing less) and the medical framing study (d15, 76.2% to 72.0% agreement). Claim K24 widened; K31 added.
2. Neutral rewrite vs raw query, with false-flag cost: PARTLY CLOSED. Rewriting to a question beat an anti-sycophancy instruction (d01, d02) but only for advice prompts, with no clean-question cost. False-flag cost was measured elsewhere: premise identification wrongly challenged 95% of true premises (d10). De-presupposition was inconsistent (d11). K25 and K26 added. A direct equal-token test on factual items with a frontier model is still missing.
3. Harm is a changed answer or only a pull toward the offered option: PARTLY CLOSED. A bare asserted answer moved reasoning models more than fabricated evidence and was seldom disclosed (d20); naming an answer drove large shifts (d22); matched controls are needed because near-boundary items inflate flips (d21). No LLM version of the McCloskey-Zaragoza modified test exists. K28 and K32 added.
4. Source-tag step as in Lindsay and Johnson: STAYS OPEN. Only a trained provenance method (about 90% less drift, d24) and an oracle evidence arm (d07) exist; no prompt-only tag. K30 added.
5. Large preregistered human replication and the 2017 failure: PARTLY CLOSED. The 2017 failure is Goldschmied et al. (d16), a hockey clip, post-event verb test null; sample size not seen. The multi-lab study is funded with 75+ labs, no result and no N published (d17). K02 now marked contested and corrected.
6. Which of strength, repetition and authority drives the dose-response; compounding: PARTLY CLOSED. Authority of the delivery channel gave a steep gradient in two of three newer models (Gemini 0.1% to 94.0%, d04). User job-title authority and social pressure were weak in factual QA (d08). Justification strength is non-monotonic and model-specific (d19). Repetition within a session was NOT varied in anything found. K15 updated.
7. Premise-check split vs one-shot: CLOSED, negative for the split on current models. Detect-then-verify lost to direct QA once true-premise questions were counted (d09, d10). K12 marked contested.
8. Warnings before vs after in LLMs: STAYS OPEN. Nothing found (d25). Related: user retraction restored clean behaviour in only 2 of 14 pairs (d07).
9. Long-context S1 error from earlier-turn false premises: CLOSED in direction, open in size for frontier models. Residue persists after reset in small open models (d06, d07) and adoption persists with relapse in two newer models (d04, d05); GPT-5.4 Mini adopted nothing. K27 added.

Still open after this pass: gaps 1, 4, 8 and the repetition half of 6. These need our own tests.

New correction: the FORRT 2017 entry is Goldschmied et al. (sport, QJEP), not Hickman. Hickman (N=20) is a separate student replication.
