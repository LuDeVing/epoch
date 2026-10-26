# B04.09 Gist extraction by overlapping replay: cross-check and critique

Checked by re-opening sources this session (PubMed abstracts via NCBI, PMC full texts, arXiv text, bioRxiv PDF). Claims are in claims.jsonl (K01 to K26).

## Corrections and confirmations (the 10+ key numbers)

Confirmed unchanged:
1. Wagner 2004: "more than twice as many subjects gained insight after sleep" (abstract read). Exact percentages still not read.
2. Ellenbogen 2007 (full text read): B>E 93% sleep vs 69% (text) or 70% (results) wake, t(29)=2.21, p=.03; sleep-by-degree F(1,27)=7.3, p=.01; groups n=14 and n=17. Confirmed.
3. Newbury and Monaghan 2019: lures g=.129, SE .210, CI [-0.282, 0.539], p=.540; Q(12)=63.227; Egger p=.365; recall g=.606, SE .299, CI [0.020, 1.192], p=.043. Confirmed.
4. Lutz 2017: t(12)=2.27, p=.043, eta2=.30; one-year t(16)=6.25, p<.001, eta2=.71; REM r=.61, p=.027; gaze r=.57, p=.025. Confirmed.
5. Matorina and Poppenk (preprint PDF read): REM vs statistical learning b=-0.626, t(58)=-2.662, p=.010; category gist -22%, instance -15%, detail -6%; F(2,182)=38.721; SWS vs summary gist trend b=1.625, p=.053; the "overlap is an insufficient condition" sentence is verbatim.
6. Hennies 2016: F(5,13)=5.63, p=.006, 56.2% of variance (adjusted R2, r=.83); three-way F(17)=22.12. Confirmed.
7. DreamCoder: 3.7% to 79.6%, 235 s to 40 s, CVC4 82.4%, DreamCoder 84.3%. Confirmed.
8. LILO: +33.14, +20.42, +2.26, +32.20, 19.01% (998/5250). Confirmed. See correction A below.
9. AWM: WebArena 23.5 to 35.5 (+12.0, +51.1% relative); Mind2Web cross-task step SR 36.2 to 45.1 offline and 43.6 online; cross-domain 18.6 to 32.6 / 35.5. Confirmed.
10. ReasoningBank WebArena overall: Gemini-2.5-flash 40.5/42.1/44.1/48.8/51.8; Gemini-2.5-pro 46.7/47.7/47.6/53.9/56.3; Claude-3.7 41.7/42.6/40.8/46.3/48.8. Confirmed.
11. Sleep-time compute: 5x, +13%, +18%, 2.5x (abstract read). Confirmed.
12. Tadros 2022: CUB 5%/95% to 63.2%/45.4%; CIFAR-10 44% vs 19%. Confirmed.
13. Lerner and Gluck: 14 of 30 explicit; 31/45 temporal vs 15/22 stationary (read).
14. Lewis and Durrant 2011, Durrant 2011: abstracts now read (a01, a05 were "opened:false" but the quoted abstract text is accurate).

Corrections:
- A. LILO tables (b16, c12, a22): the "max mean std" columns are over 3 seeds. The 93.20 (REGEX), 73.87 (LOGO), 45.60 (DreamCoder) figures are best-seed values, not means. b16 calls them "final test tasks solved (max)" and c12 calls 93.20 "Max train". Do not compare LILO 93.2 with LLM solver 90.0 as a gain: means are 77.07 vs 76.13 (std 1.50 vs 12.04). Use means (the +33.14 etc. are mean differences and check out).
- B. a07 says inference pairs BD, CE and BE were all better after sleep. The full text shows the sleep gain only on the far pair (B>E); one-degree pairs identical (t(29)=0.18); averaged effect null. Use b05, not a07.
- C. b06 presents "temporal 31/45 vs stationary 15/22" as support for the temporal-rule story. The review says that difference disappears once implicit and explicit effects are counted together; the temporal advantage holds only for explicit detection. Claim K04 states this.
- D. a20 caveat "far below parallel training" is not verified. What the table does show: in at least one column rehearsal with 0.75% stored data (79.91) beats SRC (48.47). Wording in K10 changed.
- E. a23, b20, c20 are the same paper (sleep-time compute) counted three times. a19 and c25 (van de Ven) are two versions of one paper. a21, b14, c11 are all DreamCoder. Independent-source counts in claims.jsonl collapse these.
- F. c03 and c04 are arXiv 2025 ids; dated 2026 in the evidence. Left as given.
- G. b13 (Nagel 2026) has a placeholder URL and rests on a snippet. It is used only as supporting, never as the sole basis of a claim.

## Contradictions between sources

- Durrant 2011 (SWS predicts statistical learning gain) vs Matorina (SWS predicts nothing; REM negative). Different task details and sample sizes (36 vs 69, preprint). Unresolved.
- Lau 2010 (SWS correlate) vs Alger and Payne 2016 (REM correlate), same paradigm.
- Lutz 2017 (gist needs a long delay) vs Sweegers 2014 (generalisation rises with time, not sleep) vs Matorina (category gist decays over a week).
- Ellenbogen 2007 and Matorina agree that far relational inference is the robust case; Newbury meta-analysis and Lerner and Gluck show weak or null results for simpler gist tasks.
- LILO: unaided LLM compression poor (19% valid) while ExpeL, AWM, ACE use LLM-written insights successfully. Reconciled by task: LILO required executable code to be valid.
- ExpeL: insights beat retrieval on HotpotQA but lose on ALFWorld. No general ranking of abstract vs concrete.

## Weak spots

- No LLM study tests the human core claim (overlap drives merging) against random merging. The whole LLM side is evidence for library learning in general, not for overlap-based selection (K20).
- Lewis and Durrant 2011 is a theory paper; none of its predictions about replay of overlapping sets was tested directly in humans. Its citation count (357) shows influence, not support.
- Matorina is a preprint; no peer-reviewed version found this session.
- Most human studies have N below 60; Lutz one-year result has N=17.
- Library-learning gains come from DSLs (REGEX, LOGO, CLEVR, text editing) where a compressor exists. Transfer to free-text reasoning rules is untested.
- Dynamic Cheatsheet and AWM mix model, benchmark and method; no clean ablation of the merge alone.
- Web-navigation step success gains (AWM) sit beside full-task success of 1 to 5% on Mind2Web.

## Only seen in snippets or secondary text

- Nagel 2026 replication (b13).
- Debarnot 2017, Yordanova, Werchen and Gomez, Lau 2010, Alger and Payne 2016, Song 2007, Hallgato 2013, Wilhelm 2013: known only through Lerner and Gluck's table.
- Sweegers and Talamini 2014, Tse 2007, McClelland 1995, Kumaran 2016, Winocur and Moscovitch 2011, Durrant 2013: abstracts only.
- LATM and EM-LLM, MemoryBank: abstracts or intros only; no numbers.
- A-MEM and LightMem table cells: extraction was messy; quote the prose figures only.

## GAPS

1. Does merging by overlap beat merging random groups, at equal tokens, in an LLM agent? (No published test; this decides whether the "overlap" in the design is doing anything.)
2. Which overlap finder gives the best merges: shared entities, embedding similarity, or symbolic fragment compression (Stitch-style) applied to rules written as structured code? Any head-to-head?
3. Does a merged-rule library pay for itself on free-text reasoning tasks, not only DSL program synthesis? Any LLM study with a measured token-matched gain on math or logic word problems?
4. How long must a library be observed before a gist-type benefit shows? (Lutz needed a year; is there a task-count analogue, and does an early merge hurt before it helps?)
5. Does merge order matter (within family first, then across families) as Lewis, Knoblich and Poe predict, and is easy-to-hard order (ReGAL -18.7% for random) general?
6. What guards stop a bad merge (breaks an old case)? Compare: replay check on stored cases, held-out inference check, vote-and-remove, human review. Which has measured rates of bad-rule admission?
7. Does a stronger model's library transfer to a weaker solver, and what library size or form helps weak models (Dynamic Cheatsheet and AWM show reversals)?
8. Is there a peer-reviewed large-sample replication of SWS-gist (Durrant 2011) and of Matorina's REM result, and is there an LLM analogue of the DRM false-memory finding (merged rules causing confident unsupported generation)?
9. Do rule stores and raw-case stores need to be separate and routed by task type (ExpeL ALFWorld vs HotpotQA split)? Which routing signal works?
10. Can offline consolidation be triggered by a count or predictability signal rather than a fixed schedule, and what is the break-even number of later related tasks (sleep-time compute reports 2.5x per query)?

## Gap search results (evidence_d.jsonl, d01 to d21; claims K27 to K35 added)

Closed or mostly closed
- Gap 6 (what stops a bad merge): partly closed. GRASP (d11) is the only measured guard: a replay probe of stored pass and fail cases with a regression budget took gpt-oss-120b from 40.1 (no gate) to 88.8. Review by an LLM reader is a weak guard (Huang 2026, d13: judge 46.4%, 15.8% on the biggest gaps). Add-all admission hurts (Xiong 2025, d14). Still missing: a measured count of bad rules admitted, and any test on merged rules specifically.
- Gap 10 (trigger and break-even): partly closed. RecMem (d03) shows a count trigger (count 5 best, 6 worse, 87% fewer tokens). Auto-Dreamer (d04) shows an interior optimum for cadence. Sleep-time compute (d02) has about 10 questions per context and a 2.5x cost drop at t=10, but states no break-even count.
- Gap 3 (free text): answered in the negative for two math systems (d09, d10): reuse near zero, gains vanish under matched sampling or compute. No positive token-matched math result found.

Stayed open
- Gap 1 (overlap vs random merge groups at equal tokens): still untested. Nearest are LILO random vs cosine-similarity example choice (d07, mixed) and ReGAL (d08), which has no random-grouping arm. ExpeL (d15) shows random example choice is worse than task similarity, which is retrieval, not merging.
- Gap 2 (best overlap finder): the only head-to-head is LILO's appendix (d06): Stitch 1.5x to 3.5x compression, GPT-4 about 1.0x with 19.01% valid. Code DSLs only. No entity vs embedding vs symbolic comparison exists. Cosine similarity was fooled by shared surface words.
- Gap 4 (time to benefit): no controlled sweep. AWM gains within tens of examples (d16, figure note only); LILO shows an unreadable merge hurts (d05). Not closed.
- Gap 5 (merge order): ReGAL order result confirmed (d08: LOGO -18.7, Date -20.4, TextCraft -5.3) but still one paper and no within-family-first test.
- Gap 7 (strong to weak transfer): contested. GRASP says a stronger writer helps weaker executors and the reverse hurts; Dynamic Cheatsheet (d01) and Huang (d13) show weak or negative gains. Snippet-only leads (d21) were not opened.
- Gap 8 (replication): partly. Nagel 2026 (d18, N=398, peer-reviewed) is a null DRM replication; no peer-reviewed replication of Durrant 2011 or Matorina REM was found. LLM DRM analogue (d19) is small (0.114 vs 0.053 lure vs unrelated). No test of merged rules causing unsupported output.
- Gap 9 (routing): no learned router found. ExpeL's split (d15) is by the authors' task-type call.

Corrections to earlier work found in this pass
- LILO text deltas mix bases: REGEX -30.60 is a difference of maxima; the mean difference is -22.93 (d05). Claim K12 annotated.
- Nagel 2026 is now confirmed from the PubMed abstract (d18), no longer search-snippet only.
