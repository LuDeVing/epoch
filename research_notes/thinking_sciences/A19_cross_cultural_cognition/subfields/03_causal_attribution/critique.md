# Critique: A19.03 Causal attribution (cross-checker)

## Corrections and confirmations (sources re-opened this session)
1. Bott et al. 2022 (a23): confirmed k=86, N=13,630, dz=0.59 [0.53, 0.66]; independent 0.62, interdependent 0.51; beta -0.09, p=.239. Correction: a23 gave CI [0.54, 0.70] for independent cultures only; the overall CI is [0.53, 0.66].
2. Talhelm 2025 (a20-a22): confirmed. Correction: Study 1 is Hong Kong college students (N=107; 36/35/36 per prime); Study 2 Mainland college N=272; Study 3 is Mainland older adults born before 1978 (N=258), which a22 labelled only "generation". Result: prime effect in the young, none in older adults.
3. Tsui 2026 (b22, c18, c19): confirmed 14 models, 64.5%, 89.3%, 5,306 traces, 76.0%.
4. Rosenblum 2026 (c25): confirmed 4.7% to 22.3%, risk difference 17.5 (16.2-18.8), five models, range 10.4-34.4.
5. Jin 2023 (c12-c14): abstract confirms holistic lean on AHS/TCT and no clear lean on value measures. Detailed numbers not re-verified.
6. Malberg 2025 (c01, a24): 20 models confirmed; the FAE mean 0.10 could NOT be confirmed (abstract has no figure; PDF too large to fetch). Treat as unverified.
7. Not re-opened (arXiv and OpenAlex returned 429 rate limits): Gill 2014, Kirkland 2025, Moore 2021, Edwards 2022, Malle 2006.

## Contradictions
- a24 and c01 are one source (Malberg), not independent. Likewise a25 and c04-c09 are one paper (Raj 2026); no exact d in text.
- Culture moderates spontaneous trait inference in a single study (b06, Na & Kitayama) but not in the meta-analysis (a23). Contested.
- Moore 2021 (b15) is internally inconsistent on N (110 vs df 214).
- Jin 2023: ChatGPT looks holistic on thinking but mixed on values; no consistent "Eastern" profile.
- Malle 2006 meta-analysis says the actor-observer asymmetry is near zero, while textbook accounts treat it as robust.

## Weak spots
- Most classic cultural results (a06-a19) come from review descriptions with no N or effect size. Originals not opened.
- Several preprints (b14-b18) are not peer reviewed.
- No direct LLM replication of Morris & Peng 1994, Choi et al. 1999 or Jones-Harris with numbers (only a blog, c10).
- Wikipedia is the source for a03, a04, b02, b10, b11; the Hindu-children claim is unsupported.

## Seen only in snippets (opened:false)
b01, b03-b09, b25, c27-c29.

## GAPS
1. Does an LLM show a Jones-Harris effect with real numbers (assigned vs chosen essays, graded pressure), and does a "was it chosen?" step cut it at equal tokens?
2. Is Malberg's FAE bias score of 0.10 reproducible, and what does the role-gap measure mean for our agent?
3. Original N and effect sizes for Choi/Nisbett/Norenzayan 1999, Morris & Peng 1994, Miyamoto & Kitayama 2002.
4. Did the East-West difference in correspondence bias replicate in large preregistered samples?
5. Does a culture or language prompt shift LLM attributions as much as priming does in young humans (d about 1.0-1.5)?
6. Does a "Wait"-style self-check change identity-based attribution bias (Raj 2026) or label bias (Rosenblum 2026)?
7. Raj 2026 exact effect sizes per model and identity pair.
8. Can failure attribution in our own scaffold traces beat Who&When step accuracy (14.2%) using intervention checks?
9. Does a tight token budget raise LLM correspondence bias as cognitive load does in humans (Gilbert 1989)?
10. Malle 2006 original effect sizes by moderator, and do LLMs show actor-observer swaps when roles are switched?

## Gap search results (evidence_d.jsonl, d01-d19)
Limits of this pass: Semantic Scholar, OpenAlex and the arXiv API returned HTTP 429 throughout, and the shared WebSearch budget ran out after 2 calls. Work used direct PDF opens and arXiv search pages.

1. **Open.** No LLM Jones-Harris study with numbers found in 6 targeted arXiv queries (d18). Needs our own experiment. Closest analogue: self-attribution bias (Khullar 2026, d10).
2. **Closed.** Malberg FAE mean 0.10 verified in the paper's heatmap (range -0.02 to 0.23, random 0.03); test is an actor/observer role swap on a -1 to 1 scale, so it measures a small role gap (d01, d02). Information bias is 0.54 and in-group bias 0.41.
3. **Partly closed.** Norenzayan, Choi, Nisbett manuscript opened with N, means and F values (d05-d07). Morris & Peng 1994, Miyamoto & Kitayama 2002 and Choi et al. 1999 originals still not obtained; only review descriptions (d08, d09).
4. **Open.** No preregistered large-sample cross-cultural replication found (d18). Castagnetti & Potters 2025 and Thierman 2011 are leads only (d19, opened:false).
5. **Open, partly informed.** Culture prompting shifts LLM survey values (GPT-4o distance 2.42 to 1.57, d16) and ChatGPT looks holistic by default (AHS 5.35 vs human 4.87, d15), but no LLM-vs-human priming comparison on attribution exists.
6. **Open.** Wait cuts the self-correction blind spot by 89.3% (d11) but nobody applied it to identity bias (Raj) or label bias (Rosenblum, d14).
7. **Mostly open.** Raj 2026 gives design and direction in text; per-model effect sizes exist only in figures (d03, d04). Correction: Aya-8B attributes both success and failure to external causes; K14 reworded.
8. **Open.** Baseline from Who&When: hybrid 12.28% step accuracy at 8.7x the tokens of all-at-once (4.39%); reasoning models no better (d12, d13). No equal-token intervention test yet.
9. **Partly informed.** Human load x culture interaction (Knowles 2001, via d08). For LLMs, hidden reasoning budget did not consistently change self-attribution bias (d10). No direct token-budget test on correspondence bias.
10. **Partly closed.** Role-swap gap in LLMs is small (0.10, d02). LLMs are more lenient on actions presented as their own (d10) and miss their own errors but fix user-labelled ones (d11). Malle 2006 original effect sizes still not opened.

New claims K22-K26; K10 value now verified; K14 and K17 rewritten.
