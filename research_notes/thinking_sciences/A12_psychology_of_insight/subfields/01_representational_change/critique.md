# Critique: A12.01 Representational change (cross-check)

Checked 2026-10-26. Evidence files: evidence_a.jsonl (28 lines), evidence_b.jsonl (30), evidence_c.jsonl (28). All parse as JSON. Claims: claims.jsonl (K01-K24).

## 1. Sources re-opened and numbers checked (10)

Full text was fetched and searched this session for each item below.

| # | Evidence | Source | Result |
|---|---|---|---|
| 1 | a04 | Knoblich et al. 1999, Exp 1A | Confirmed: F(3,57)=7.11 p<.001; block F(1,19)=14.41 p<.01; order C<B<A and A<D; T=12, T=10. CORRECTION below. |
| 2 | a05 | Knoblich 1999, Exp 1B | Confirmed: 38 paid participants, F(4,144)=10.03 p<.001, T=107, T=96. |
| 3 | a06 | Knoblich 1999, Exp 2 | Confirmed: N=78, F(4,222)=46.45, block F(1,74)=177.97, B vs A T=151, p<.001 in times. The p=.89 for Type A transfer is in the paper. |
| 4 | a07 | Knoblich 1999, Exp 3 | Confirmed: 61% vs 100%, chi2=12.59, 61% to 100% chi2=13.85, D 61% vs 69% p=.64. CORRECTION below. |
| 5 | b07/b08 | Wu et al. 2017 | Confirmed: D-process 98.40% / 1,797 ms vs 90.00% / 3,070 ms; R-process 49.8% / 4,730 ms vs 49.2% / 4,245 ms; O-process 6,405 vs 5,602 ms. |
| 6 | b14 | Luft et al. 2017 | Confirmed: Type C post-test 32% vs 5% vs 5%, chi2=7.02, p=.030. |
| 7 | a18/b09 | Spiridonov et al. | Confirmed with explanation of the N mismatch (below). Movements A 0.56, B 1.70, C 1.91, D 8.26 confirmed. |
| 8 | c01/c02/c03 | Mizumoto et al. 2025 | Confirmed: 7.6% vs 17.6% vs human 52.9%; full set 9.42% vs 19.25%, odds ratio 2.29; verification failures 5.23% to 39.34%; Grok-4 29.5% (33/112) vs 48.8% (40/82), p=0.0071. |
| 9 | c04/c05 | d'Aliberti and Ribeiro 2026 | Mostly confirmed; one number NOT found (below). |
| 10 | c06, c20 | Kang et al. 2025; Zheng et al. 2024 | Confirmed: 3,427 rollouts, 94% of 426 candidates, 24.5% tokens, 2.9% drop (best-case row; the abstract says "within a 2.9% drop"); step-back 73.2 / 81.8 / 84.5 / 85.6 and 20.5% fixed vs 11.9% introduced. |

Not re-opened: Knoblich, Ohlsson and Raney 2001 (a09 to a12, b01 to b05). The numbers agree across evidence lines a09 and b01 to b04, but both are written by agents reading the same paper, so that is one source, not two.

## 2. Corrections

1. a04: the line says "Transfer was large for B, C, D". In the paper, transfer in solution frequency for Type D (75% to 90%) was NOT significant (p=.13). Significant frequency transfer was B (p<.05) and C (p<.001). Transfer in solution time was significant for D (p<.05), as the line also says. Treat D transfer as "time only".
2. a07: "Type D and Type A were unaffected" is true for initial difficulty and for solution frequency (D 61% vs 69%, p=.64). For solution time, the paper reports that prior exposure to tautological problems helped Type D as well as Type C (U=65, Z=2.71, p<.01), but not Type A. The paper's own wording is that the tautological form does not affect initial difficulty or transfer in frequency. Also the Type A and Type C-after-tautology results are partly at ceiling (all 100% in some cells), so the Block 2 test could not be made in the regular-first group.
3. a18 versus b09 (same Spiridonov paper, different Ns: 108/90/74 vs 105/88/73). The paper text says 90 took part in Exp 2 and two were not allowed to take part, so 88 is the analysed N; the same pattern likely holds for Exp 1 and 3. Use the b09 values (105/88/73, pooled about 266) for analysis. The b10 pooled N of 266 equals 105+88+73. a18 has the same paper dated 2026, b09 dated 2025 (preprint then journal).
4. a18 baseline accuracy: Exp 1 baseline is "about 91%" for Type A on one model and "about 86%" is the intercept of the pooled model, and b10's intercept 1.81 log-odds corresponds to about 86%. Both are in the paper; they come from different models, not a contradiction.
5. c04: the line gives pooled "accuracy without vs with shift 0.290 vs 0.066". I could not find 0.290 or 0.066 in the paper text. The paper reports pooled correctness of 16.44% (no shift) vs 2.57% (shift), N=723,200, and per-model rows (for example Qwen 1.5B math 0.327 vs 0.144, Qwen 7B math 0.661 vs 0.282, crosswords 0.096 vs 0.201). Replace 0.290/0.066 by 16.44%/2.57%. The 6.31% shift rate, Math 1.5B and Crossword 1.5B rows are confirmed.
6. c05: Math 32.21% to 40.62% (+8.41) and crosswords +0.45 are confirmed from the paper's headline. The paper also has a second aggregation (Math 32.70 to 40.43, +7.74; crosswords 9.65 to 10.15, +0.49, with high-entropy math 19.70 to 35.09, +15.38). Both are valid; the number depends on which table. Cite the range.
7. a17 and a16 and c23: the name is spelled "Oellinger" in some lines and "Ollinger" in others. The author is Oellinger (earlier Ollinger). Normalise on citation.
8. a16: the solution rates are marked "approximate, from a table" and are not exact. Quote them only as bands (about 90, 75, 60, 25 percent).
9. a09/b01: the type labels differ between papers (in the 2001 paper, A is loose-chunk value change, B operator change, C tight-chunk value change). In the 1999 paper, C is operator+tautology and D is tight chunk. Do not merge the two type systems when comparing rates.

## 3. Contradictions between sources

- Interactivity (K11): Weller et al. 2011 reported that real sticks erase the A-versus-B gap (second-hand only, a19). Spiridonov et al. found no robust effect, and one exception: interactive sticks helped Type D and VR sticks helped in Exp 3, while movements interfered with relaxation of higher-level constraints. Macchi et al. found no gain from pencils but a gain from a photo of real sticks. The field is mixed; the safe reading is "unstable".
- Hill-climbing vs constraint relaxation (K09): Oellinger et al. 2006 favour relaxation. MacGregor et al. 2001 progress monitoring predicts 64% of solvers use lookahead 1 or 2; Jones 2003 observed roughly even splits, and he found that non-solvers did move the taxi, which fits neither theory alone. Neither side has a clean win.
- Mental set (K10): Oellinger 2008 found that repeating non-insight problems did not hurt later insight problems, yet the nine-dot motor-priming study (b19) found strong harm from the wrong pattern. The difference may be that motor training primes the very move that must be dropped.
- LLM "aha" (K18): Mizumoto et al. find Aha language very common (Claude Opus 4 over 100 "Oh!" in logs) and mostly wrong; d'Aliberti and Ribeiro find spontaneous shifts rare (6.3%) in small tuned models. These are different model classes, so rare vs common is not a contradiction, but it means the "shift rate" is model dependent.
- Human reflection claims: Kang et al. say reflection mostly confirms; d'Aliberti and Ribeiro show an external cue can still add 8 points on math. Consistent: unprompted reflection is weak, forced reconsideration works where the first pass was high entropy.
- Language of thought (c03): Grok-4 is worse in Japanese (p=.0071), Claude Opus 4 and Gemini are not significantly different (p=.356, .369). Do not generalise.

## 4. Weak spots

- The main human evidence is one task family (Roman numeral matchsticks) and one lab group. The authors themselves state there is no independent evidence that knowledge is stored as constraints and chunks. The hierarchy of constraints was a design hypothesis.
- Chunk categories (tight versus loose) were assigned by the authors with no independent strength measure; only Wu et al. 2017 gives a separate measure (Chinese characters), and its gain is on decomposition time, not on insight problem solving itself.
- Eye tracking (2001): three items, one per type, so item and type are confounded; N=24; one trial per problem. The finding that fixation duration does not separate solvers early has a null interaction (p=.20) with no power analysis.
- The change-point analysis (Graf et al. 2023) is one dataset, N=61, with 34% solving.
- LLM evidence is mostly benchmark gaps. None tests whether a re-representation prompt causes recovery with matched tokens, apart from step-back and the reconsideration cue (c05), which are not insight-specific.
- Triple counting: Mizumoto et al. appears as a26, b25, b26, b27, c01, c02, c03; Graf et al. as a13 and b16; Spiridonov as a18 and b09/b10; Knoblich 2001 as a09-a12 and b01-b05; Naeini et al. as b28 and c13. In claims.jsonl I counted each paper once.
- Chosen "established" labels rest on two or more different papers. K02 (tight chunks) and K03 (separability) are established but thinly: K02 rests on one task family plus a Chinese-character study, K03 on one experiment plus an abstract-only study.

## 5. Only seen in snippets or abstracts

a19 (Weller 2011, second hand), a20, a21, a22 (Ohlsson 1992, 2011 book, Kaplan and Simon 1990: no text read), a23 (MacGregor, from Jones 2003), a27 (Orru, abstract; but c16 read the full text), b06, b20, b21, b22 (abstract only, authors unnamed; this is the key source for "cue both mechanisms at once does not help" and needs a full read), b23, b24, b30, c22, c23, c24, c25 (search snippet). Ohlsson's own 2011 account was not opened at all, so the "redistribution of activation" framing in a21 is unverified.

## GAPS

1. Does a prompt that names the specific constraint to drop (O4) or the specific unit to split (O6) beat a generic "reconsider" cue on LLM insight items at equal tokens? No study compares the two (c05 uses only a generic cue). This decides the router design.
2. Can an impasse be detected from model output alone (repeated candidates, first-attempt element use, entropy), and is the detection accurate enough to gate O4/O6 without the false triggers G1 forbids? Eye-movement markers have no LLM counterpart.
3. What does Knoblich's A to D family look like for LLMs: does failure rise with constraint depth and with chunk tightness (tokenisation may make "tight chunks" model dependent)? MathSticks hints at digit-edit bias but has no per-type data.
4. Does the model fail at generating the re-representation or at endorsing it? Mizumoto et al. show generation without endorsement (5% to 39% of errors). Which fraction of failures on our target sets are verification failures, which would call for G5-style code selection instead of a representation operator?
5. Is separation of constraint relaxation from chunk decomposition real? Exp 3 shows it for solution rates but not for times, and b22 is abstract only. Read b22 in full and test cue-both against cue-one on LLMs.
6. Does the mental-set penalty carry over inside one LLM context (earlier failed frames reduce later success)? If so, is clearing history before re-attempt better than adding a reframe? Human results are mixed (K10).
7. Do reframing operators transfer from insight puzzles to our real target tasks (ARC-type, NoveltyBench)? Step-back is the only strong generic result, and it has a 11.9% break rate. Measure net gain by task class.
8. Was Ohlsson's own 2011 book chapter or the 1992 account saying something we are missing for operational purposes (for example the three-step "activation redistribution" and spreading activation as a retrieval mechanism for an LLM memory)? Not opened.
9. Is the late sudden shift in human data (Graf et al. 2023) replicated elsewhere? One dataset with N=61 should not set how we treat "stuck then sudden" in S6.
10. Does progress monitoring (MacGregor et al.) or representational change better predict LLM failure on search-like insight tasks (car park, matchstick)? Link to the progress monitoring theory subfield, which is researched in parallel.

## Gap search results (2026-10-26, evidence_d.jsonl d01-d19, claims K25-K32)

Method note: the web-search quota ran out early. I used arXiv listing pages, Crossref, Semantic Scholar and direct PDF or HTML reads. Publisher pages (Taylor and Francis, ScienceDirect, Purdue, the Chinese journal) were blocked or refused, so some sources stay abstract-level. Disk space also ran out once; I deleted only my own downloaded PDFs.

| Gap | Status | What changed |
|---|---|---|
| 1 Named vs generic cue | OPEN | No LLM study found (d17). Nearest evidence is human: targeted cues work only on matching items (d03). A Wait-style generic cue is a strong baseline (d10, 89.3% blind-spot cut) and must be an arm in the test (K25, K26). |
| 2 Impasse detection from output | PARTLY ADDRESSED, not closed | Candidate signals exist: thought-switch rate (418% higher in wrong answers, d11), first-pass entropy linked to cue benefit (d15), answer stability (d13), trace confidence (d14). None tested as a fixation detector, and stable-and-wrong cannot be told from stable-and-right. Keep G1: gate on code-visible failure and log the statistic (K27). |
| 3 A-D family for LLMs | OPEN, with a proxy | MathSticks shows sign-changed items are 8 to 14 points harder in text for the three best models (d07). Still no A-D or tightness labels. Tokenisation does change what is tight (d08, K29). |
| 4 Generation vs endorsement | PARTLY ADDRESSED | Over 70% of wrong o1-like responses contain a correct thought (d11); correctness is encoded in hidden states (d12). So verification and selection is likely a large share. The share on our own target sets is not measured (K31). |
| 5 Separability | MOSTLY CLOSED for solution data | The Type D time gain is explained by the tautology set holding a tautological Type D item (d01, my inference from the Method). b22 is Miller, Wiley, Ohlsson 2025; full abstract read, full text paywalled, N unknown (d03). The LLM cue-one vs cue-both test is not done. |
| 6 Carry-over of a failed frame | SUPPORTED INDIRECTLY | Models do not recover from wrong early turns (d09, unreliability +112%) and correct the same error less when it is their own (d10). Clean-context vs reframe comparison on insight items not done (K28). |
| 7 Transfer to ARC and NoveltyBench | PARTLY ADDRESSED | Code-side object re-encoding nearly doubled GPT-4 ARC solves (d16, abstract only). Fixation effects fade with model strength (d18). Nothing on NoveltyBench. Net gain per task class still has to be measured (K30). |
| 8 Ohlsson 1992 and 2011 | OPEN | Only the chapter opening is public (d06). The redistribution mechanism is still unverified (K32). |
| 9 Replication of the late sudden shift | OPEN | No second dataset opened. Candidates found by title only (d19). Danek et al. 2016 abstract says Aha falls as constraints stack (d05). Keep K06 single-source. |
| 10 Progress monitoring vs representational change | OPEN | No LLM study of MacGregor-style progress monitoring on car park or matchstick items found. Left to the progress monitoring subfield. |

Status changes in claims.jsonl: K03, K13, K06, K10, K17 and K23 gained evidence and amended text; no status flipped. K10 stays contested for humans but the LLM evidence now leans one way. New claims K25 to K32, all single-source.

Corrections to earlier text: b22 authors are Miller, Wiley and Ohlsson. The Type D time gain in a07 is probably practice at decomposition, not a leak between mechanisms.

Next tests, in order: (1) a four-arm cue test (generic Wait, named constraint, named unit, neutral resample) at equal tokens; (2) count wrong answers whose log holds the gold answer on our target sets; (3) clean-context vs continued-context re-attempt.
