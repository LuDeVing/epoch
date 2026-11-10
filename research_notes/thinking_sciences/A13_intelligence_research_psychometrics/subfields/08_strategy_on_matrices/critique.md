# Critique: A13.08 Strategy on matrices (cross-check)

## Numbers re-opened this session (full PDF text from arXiv)
Confirmed as recorded:
- Camposampiero 2025 (arXiv 2503.11207): o3-mini 86.6 to 17.0, R1 80.6 to 23.2, ARLC 98.6 to 88.0; o3-mini medium 5445 tokens, high 9867 tokens, R1 4486 (a25, c04, c05).
- Hersche 2024 (arXiv 2412.05586): GPT-4 discriminative 56.0 / 60.0, predictive 74.8; Llama-3 70B 22.8 / 22.4 discriminative, 79.0 predictive; per-attribute 91.4 (GPT-4), 83.2 (Llama-3); n=7 self-consistency 93.2 / 84.8; arithmetic 27.1 vs 73.6 (GPT-4), 31.0 vs 45.0 (Llama-3); GPT-4 at range 1000 is 8.4 (c01, c02, c03, c05).
- Hu 2021 SRAN (arXiv 2002.06838): ResNet 53.4, CoPINet 91.4, context-blind 71.9 and 94.2; I-RAVEN 40.3, 46.1, 12.2, 14.2; SRAN 60.8 vs 60.7 (a21, b27, c20).
- Webb 2023 (arXiv 2212.09196): generative OR 1.88 (CI 1.21 to 2.91, p=.005); r(30)=.39, p=.027 (a22, b24, c17). MC OR 6.27 was not re-found by grep in the extracted text (the pdf text has odd characters); keep as recorded but unverified here.
- Zhang 2024 (arXiv 2403.04732): GPT-4V Mensa .24, IntelligenceTest .16, RAVEN .12; Gemini Pro .15 / .18 / .11; "2-8 percentile"; humans 84.67% on Raven; Gemini best 18% on IntelligenceTest (a24, c07).
- Gendron 2023 (arXiv 2305.19555): GPT-4 RAVEN-T open .410 / .330, MC .697 / .535; TD3 open .343 / .234.

Corrections:
1. c15: multiple-choice cells for Text-Davinci-3 and GPT-3.5-Turbo were reversed between text and symbolic. Table 4 gives TD3 text .461, symbolic .452; GPT-3.5-Turbo text .276, symbolic .315. (Evidence line c15 should be read with this fix; the GPT-4 values stand.)
2. a28: text says 25 of 36 settings, intro says 27. Left as a source inconsistency, not resolved.
3. a26 and c26 (and a22/b24/c17, a24/c07, a27/b28, a21/b27/c20, a03/b03) are the same papers recorded twice by different agents. They count as one independent source each; claims use this.
4. a12/b14 and a13/b15 are the same two von Gugelberg data sets; a14/b12 are the same Liu et al. data. Not independent.
5. a20 says human 84.4 and c19 says 84.41: same number.

## Contradictions between sources
- Toggle count: Vigneau 2006 reports r=-.27 for number of toggles (N=55); Rivollier 2021 reports r=.02 (n.s., N=130). Toggle rate, latency to first toggle, and time on matrix are the robust ones.
- Drift to elimination later in the test: Gonthier & Roulin 2020 find a clear shift with item difficulty (self-report), but von Gugelberg & Troche 2025 find change tied to item position, with three gaze metrics disagreeing on direction. Self-report and gaze may measure different things.
- Mediation by strategy: three studies, three answers (full, partial, none).
- Direction of option effect in LLMs: GPT-4 gains from options on text RAVEN (.410 to .697) while Claude Sonnet 4 loses (.560 to .385 in the 2026 Raven text set, single run each).
- Hersche predictive-over-discriminative result (GPT-4) conflicts with Camposampiero's reason for moving to discriminative (generation led to irrelevant relations). Different models and prompts; no head-to-head.

## Weak spots
- The founding paper (Bethell-Fox, Lohman & Snow 1984) was never opened by anyone; all numbers are second-hand via Laurence & Macedo 2023. Same for Mitchum & Kelley 2010, Loesche 2015, Becker 2016, Arendasy & Sommer 2013, Gonthier & Thomassin effect sizes beyond b05, and Jastrzebski 2018.
- Human results re-opened this session: none. Gonthier & Thomassin (b05), Vigneau (a03), Rivollier (a04, a05), Gonthier & Roulin (b04) numbers were not re-checked because the papers are paywalled or I did not reach open copies. Treat them as agent-recorded, opened:true.
- Almost all human data are university students on the APM (36 items, small N, often compared across non-independent labs). Strategy labels come from gaze or self-report, both proxies.
- The LLM studies mostly test different things: perception (VLMs), rule induction (text), and choice artefacts. None of them directly manipulates build-first vs eliminate-first inside a reasoning-model scaffold at equal tokens. Closest: Cao et al. elimination loop (+8 points GPT-4o) and Hersche predictive vs discriminative.
- Single runs and small human pilots (N=9 in the 2026 Raven text study) make the format reversals fragile.
- Snippet-only: Hayes 2011 abstract, Gonthier 2015 abstract (a06), Gonthier & Roulin abstract (a07), Mitchum 2010 abstract (a10), Liu 2023 model (b13).

## GAPS
1. Does forcing a build-first step (answer written before options shown) raise accuracy of a reasoning-model agent at equal tokens, on a leak-free matrix set such as I-RAVEN and on non-matrix multiple-choice tasks? No study has run it.
2. For LLMs, is explicit response elimination (prune options one by one) better, worse, or equal to build-then-match, and does the answer depend on whether the model can perceive the items (text vs image)?
3. What did Bethell-Fox, Lohman & Snow (1984) actually measure: N, effect sizes, the item difficulty boundary at which high-ability people switch? Get the original.
4. Is the hybrid "isolate one rule, eliminate, repeat" better than either pure strategy in humans (accuracy by strategy in Jarosz 2019) and is it testable as a fixed procedure in an agent?
5. Which agent-side trace metric corresponds to proportional time on matrix and toggle rate (for example tokens before first option mention, number of option re-reads) and does it predict accuracy the way the gaze metrics do?
6. Does an adaptive switch (build first, fall back to elimination after a stall) beat always-build, as the Rivollier reversal at long latencies suggests?
7. How much of reasoning-model gain on multiple-choice reasoning benchmarks is choices-only leakage (Balepur 2024, 2025) versus true reasoning, measured on our own benchmark set?
8. Why did Claude Sonnet 4 lose and GPT-5 gain when options were removed on Raven-like text (2026), and does this replicate with more than one run and a larger human sample?
9. Does build-first lower or raise calibration error in LLMs (human result from Mitchum & Kelley 2010 is unread)?
10. Do the hard-rule failures (arithmetic rules, noisy value ranges) need an exact tool in S5, or can a scaffold with decomposition alone (per-attribute queries) close the gap at equal tokens?

## Gap search results (2026-11-10)
Search was throttled: Semantic Scholar, arXiv API and OpenAlex mostly returned 429, so work relied on direct arXiv PDFs, 4 WebSearch calls, and open PDFs. New evidence is in evidence_d.jsonl (d01 to d16).

- Gap 1 (build-first at equal tokens on I-RAVEN): stays OPEN for matrices. Nearest test is Raman 2025 (d01, d02): on knowledge/math MCQA, reasoning only before options keeps MCQA a fair proxy; reasoning after options adds 30 to 40 points for models above about 50B. Not at equal tokens, not matrices. New claim K25.
- Gap 2 (elimination vs build-then-match in LLMs): PARTLY CLOSED. Forced elimination was worse than direct answering in older models on 2-choice items (Balepur 2024, d05); a soft eliminate-then-choose scorer helped a 3B model on 5 of 8 tasks (Ma and Du 2023, d06). No reasoning-model or text-vs-image comparison. New claim K26 (contested).
- Gap 3 (Bethell-Fox 1984 original): stays OPEN. Paper paywalled, no open copy. Only extra detail: N=28, geometric analogies, fixation counts and sequences (via Laurence 2018, d09, d10). Do not cite effect sizes.
- Gap 4 (hybrid isolate-and-eliminate): PARTLY CLOSED on definition (d08), OPEN on accuracy. Over 50% constructive, 3% pure elimination, hybrid exists; no accuracy by strategy found. K27.
- Gap 5 (agent trace metric): stays OPEN. No study found (d16). Human anchors: toggle rate r=-0.68 N=34 (d09); constructive-item count r=.31 N=192 (d11). K28.
- Gap 6 (adaptive switch): stays OPEN. Only human indirect support (strategy shifts with difficulty, d11). K28.
- Gap 7 (choices-only leakage vs true reasoning on our set): literature part CLOSED, own-benchmark part OPEN. Choices-only beats majority in 11/12 cases up to +0.33 (d03); NOTA cuts reasoning-model advantage from 12.63 to 5.29 points (d02). Needs our own choices-only and NOTA baselines.
- Gap 8 (Sonnet 4 loses, GPT-5 gains without options): LOCATED, NOT REPLICATED. Source is NeuroCognition (d12): single runs, N=9 humans, Sonnet 4 with reasoning off. Reasoning-off helped text MC (p=.021) not Gen (d13). Treat as fragile.
- Gap 9 (calibration under build-first): stays OPEN. Mitchum and Kelley 2010 not opened; no LLM study found.
- Gap 10 (exact tool vs decomposition): no new evidence; earlier Hersche and Camposampiero numbers stand. Pattern hints gave no gain on text RAPM (d13), which weakly suggests the bottleneck is the abstract step, not rule choice.

Weak spots added: d10, d14, d15 are opened:false. Exact MC alignment figure in Chandak 2025 (d07) not extracted.
