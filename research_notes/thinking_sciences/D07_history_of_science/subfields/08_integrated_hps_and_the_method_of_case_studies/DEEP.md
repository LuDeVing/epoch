# Integrated HPS and the method of case studies: deep document

*Subfield D07.08. Written 2026-11-10 from evidence_a-d.jsonl (104 evidence lines), claims.jsonl (K01-K26) and critique.md in this folder. Evidence ids (a01, b12, d03 ...) point to those files. Status marks: [E] established, [S] single-source, [C] contested.*

**Read this first.** The core of this subfield is philosophical argument, not measurement. No study in the opened sources measures whether the "method of case studies" works, and no study measures whether an LLM treats historical cases as evidence correctly (K20, critique gap 1). What we do have is: (1) a clear conceptual map of how cases may and may not be used as evidence; (2) a handful of real quantitative tests of famous case-based theses, which show how a story can fail when checked on many units; (3) many LLM studies on neighbouring tasks (rediscovery benchmarks, case memory, confirmation bias, hypothesis updating). The link from (1)-(2) to our agent is by analogy. We say so each time.

## 1. What it is

**Integrated history and philosophy of science (integrated HPS)** is the programme of using the history of science as evidence for, and as a source of, theories about how science works (method, rationality, theory change, discovery). The "method of case studies" is its working tool: take a detailed historical episode (the squid giant axon, Brachet's cytology, Millikan's oil drops, Darwin's reception) and draw a methodological or philosophical lesson from it.

The key problem is **Pitt's dilemma** (a01, restated in a02, a07, a17). It has two horns.
- **Top-down horn.** You start from a philosophical claim and pick cases that fit it. The selection is biased and the case is read in the claim's light. The case proves nothing it was not chosen to prove.
- **Bottom-up horn.** You start from a case and generalise. One, two or three cases cannot support a general claim. This is hasty generalisation.

Burian (a02) adds that even a few hundred cases cannot represent the diversity of science. There are no counts behind that claim; it is an argument.

For an LLM agent, the same shape appears whenever the agent backs a claim with examples it picked itself: analogies, precedents, "similar past problems", retrieved cases. The question is how much weight such examples carry, and what the agent must do before it treats them as evidence.

Scope of this document: the philosophy of case use (Pitt, Burian, Scholl, Herfeld, Kinzel, Chang), the attempt to test methodology against many cases (the Virginia Tech VPI project), quantitative tests of famous case theses (Planck's principle, Millikan, Mendel), and the AI studies that either use historical discovery as a test (FIRE-Bench, LLM-SRBench, DiscoveryWorld, MOOSE-Chem) or use "cases" as agent memory (Memento, ExpeL, Empirical-MCTS). Sauer and Scholl (eds. 2016), the key book, was not read (c21).

## 2. History and theories in depth

### 2.1 From Lakatos to Pitt

- **Lakatos (1971, 1972) and Laudan (1977)** (a19, a03, via Burian). Philosophers of science treated history as the test bed for methodologies. Lakatos: expose each methodology to the cases of all its rivals. Drop the trivial claim "all science is rational". Prefer the methodology that rates the most cases as sound. Laudan: use scientists' "touchstone" judgements about which episodes were rational. Burian says both assume the credit and sampling problem away.
- **Giere (1973, 1985), Hull (1992, 1998), Schickore (2011)** (a09, a10, a11; all [M], seen only as references in Scholl 2018). The "confrontation model": HPS is a marriage where philosophical claims are tested against history. Scholl (a07) names it and argues for a better model.
- **Laudan, Donovan, Laudan and colleagues (1986, Synthese 69: 141-223; book 1988)** (a08, b09; [M]). The most direct empirical programme. About 250 hypotheses from Kuhn, Feyerabend, Lakatos and Laudan were collated, and 32 were sent out for testing as "case studies" (d03, via McAllister 2018). Some were true case studies, some were quantitative tests. Example: Perrin tested a thesis on 69 French chemists (age in 1785 versus age at adopting the oxygen theory) and judged it disconfirmed. McAllister lists five design flaws: claims are quantitative so need cross-case statistics; quantitative methods were misread; case studies were not separated from statistics; and others. Its authors describe the project's "limited impact". No pooled effect size and no coder agreement were found (K04 [C]).

### 2.2 Burian (2001): the dilemma "resolved"

Burian (a02-a06, all opened). Three moves.
1. The dilemma is ill-founded because science has local consensus and cases can be chosen with context in mind.
2. The strong designs are **grouped** studies. **Longitudinal**: follow one problem over time. **Comparative**: compare labs, disciplines, places or tools on one problem. Context is limited by showing it was relevant to the work (a04).
3. **Exploratory experimentation and cross-discipline triangulation** as worked examples. Brachet's cytology: work from 1927, RNAse crystallised 1938, differential staining by 1940, scheme in a 1952 book (a05). Jacob and Monod: six named cross-discipline pairs (a06).

### 2.3 Scholl (2018): three operations

Scholl (a07, a12, a13) proposes that cases do three jobs, and only one needs sampling care.
- **Generative**: a case suggests a new claim or concept (gene "expression" redefined from Mendel/Morgan traits to Beadle/Tatum enzymes to Jacob/Monod regulatory proteins).
- **Refinement**: a case sharpens or scopes an existing claim (squid giant axon for neural transmission).
- **Justification**: a case is evidence for a claim. This is where Pitt's dilemma bites.

Kinzel (2015, a18 [M]) lists four functions; Chang (2011, a14 [M]) offers a cyclical mode where history and philosophy feed each other. Scholl's answer to the selection-bias horn (a13): tie each claim to the scope of the cases and count unfavourable cases; but spurious support is still easy if scope counts ignore unfavourable cases, so extra warrant is needed. Conceptual proposal; no data on how well it works.

### 2.4 Herfeld (2025): make selection explicit

Herfeld (a15-a17, opened) uses network analysis to select cases for a study of rational-choice model transfer. Thresholds: at least 3 co-citations, at most 5 years apart, periods 1944-1970 and 1984-2014. The idea is that data, thresholds and selection are explicit and repeatable. Thresholds are justified by intuition, not tuned or validated; co-citation is only a proxy for transfer. No test compares this to free selection (K26, critique gap 9). A press report on historians using computation on 76,000 pages stresses that selection from incomplete data stays a human decision (d17, [M]).

### 2.5 The scale argument: what happens to a case thesis on many units

The sharpest lesson comes not from the philosophers but from the quantitative tests.

- **Planck's principle** ("science advances one funeral at a time"). Hull, Tessner, Diamond (1978) tested it on 67 British scientists born before 1839 and alive in 1869, using acceptance of Darwin's evolution (d04, via McAllister). Mean age in 1859: 39.6 for those who accepted by 1869, 48.1 for those who did not. Significant, but age explained under 10% of variance. Among those who accepted, older ones were as quick as younger ones. Verdict: disconfirmed on balance. Perrin's 69 chemists (oxygen theory): disconfirmed (d03). Gorham (1991) and Levin (1995) also found little support (b02, snippet). Then Azoulay, Graff Zivin and Fons-Rosen (b01, b25, b26) found a different effect: after 452 eminent life scientists died early, non-collaborator output in their 3,076 subfields rose 8.6% against 31,142 control subfields (34,218 in total). Collaborator output fell. Effect sits mostly with earlier deaths; older stars give a small, imprecise effect (critique item 2). It needs low entry barriers. Cheng and Weinberg (2024, d06) find adoption hump-shaped in career age, depending on network distance.
- **Millikan's oil drops.** Published 58 drops and said they were all drops over 60 days (d07). Notebooks hold about 100 drops in 63 days per Goodstein (about 25 aborted, about 75 complete) or about 175 from 11 Nov 1911 to 16 Apr 1912 per accusers. Claimed uncertainty 0.2%. Franklin's re-analysis says using all data would barely change the result: with all data the standard error is within about 2%, value 1.5924(17)e-19 C, about 0.6% from today's value (b05, d07). Goodstein is a defender with an interest.
- **Mendel.** Fisher (1936) found a fit "too good": pooled chi-square p about 0.99993 (about 7 in 100,000) (d08). Franklin et al. (2008) dropped most of Fisher's other points but concede "too good to be true". Pires and Branco (2010) show an unconscious-bias model reproduces the fit without fraud. Not closed.

The moral for method: a famous episode told as a story can be wrong in its details, wrong in its generalisation, or right in direction but wrong in size. A case narrative is itself a claim that can be re-checked against primary data (K07).

### 2.6 Rational reconstruction and discovery

Hanson on Kepler and similar "logic of discovery" reconstructions are often historically inadequate, and published papers are retrospective tidy-ups (b07, b08, SEP; K08 [E]). This warns against feeding an agent a tidy retrospective and calling it the process.

### 2.7 Computation enters HPS

Simons, Zichert and Wuthrich (2025, c16) and Zichert and Simons (2026, c17) review LLMs for the history, philosophy and sociology of science; both are conceptual and report no benchmark numbers. They find no standard for judging LLM analyses of historical cases (c27). Lean et al. (2023, a34 [M]) is digital literature analysis for empirical philosophy.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Pitt's dilemma: picked cases are biased, few cases give hasty generalisation | None. Argument. Burian: "even a few hundred" cases not enough | Pitt 2001 [M]; Burian 2001 (a01, a02) | [E] as position, not measured (K01) |
| Cases play generative, refinement and justification roles; only justification needs sampling care | None | Scholl 2018; Kinzel 2015; Herfeld 2025 (a12, a13, a17, a18) | [E] (K02) |
| Grouped (longitudinal, comparative) designs and scoped, local claims are the accepted way out | None | Burian 2001; Scholl 2018 (a04, a13) | [E] (K03) |
| VPI programme tested methodology theories on cases | About 250 hypotheses, 32 tested, 69 French chemists in one test; no pooled effect or coder agreement | Laudan et al. 1986/88 via McAllister 2018 (d03) | [C] (K04) |
| Planck's principle weak in early tests | 67 British scientists; mean age 39.6 vs 48.1; under 10% of variance | Hull et al. 1978 via McAllister (d04) | [C] (K05) |
| Star deaths raise outsider output | 452 stars, 3,076 subfields vs 31,142 controls, +8.6% | Azoulay et al. 2019 (b01) | [S] (K06) |
| Adoption hump-shaped in career age, depends on network distance | Sample sizes not extracted | Cheng and Weinberg 2024 (d06) | [S] |
| Millikan: data selection charge | 58 published drops; about 100 to 175 in notebooks; re-analysis: little change | Goodstein 2000; Franklin (d07) | [C] (K07) |
| Mendel: too-good fit | p about 0.99993; bias model fits without fraud | Fisher 1936; Pires and Branco 2010 (d08) | [C] (K07) |
| Rational reconstructions of discovery are often historically inadequate | None | SEP entries (b07, b08) | [E] (K08) |
| FIRE-Bench: agents recover under half of recent findings | Best F1 46.7 (Claude Code, Sonnet-4), 41.9 Codex gpt-5-medium, 37.9 and 31.9 OpenHands; 30 core tasks, 3 runs; median CV 0.37 | Wang et al. 2026 (a20, c01) | [S] (K09) |
| FIRE-Bench false positives are mostly wrong conclusions | 76.4 to 95.0% contradictory or unrelated; 4.5 to 10.9% reasonable alternatives | Wang et al. 2026 (a21, c02) | [S] (K10) |
| Date-split contamination checks are noisy | Hard 15.4 to 24.8, 22.6 to 31.0; medium gpt-5 44.5 to 23.1; easy o4-mini 58.9 to 42.1 | Wang et al. 2026 (c03) | [S] (K11) |
| Famous equations partly recited | 239 problems; best 31.5% (Transform), 28.1% (Synth); direct prompting 2.1 to 7.2% vs 10.8 to 31.5% with data-checked LLM-SR | Shojaee et al. 2025 (a24, c04, c24) | [E] (K12) |
| Discovery benchmarks from real work are hard | ScienceAgentBench 32.4% (34.3% with expert hints; o1-preview 42.2%); DiscoveryBench best 25%; DiscoveryWorld 38% easy, 18% challenge vs humans 66% | a29-a31, c06-c08 | [E] (K13) |
| Failure is in composing steps | Unit tests 0.66 to 0.77 vs 0.18 to 0.38 on full tasks | Jansen et al. 2024 (c25) | [S] (K14) |
| Inspiration retrieval from past papers works | Hit ratio 83.7% at top 4% (GPT-4o), 96.7% at top 20%, 60.8% at top 0.8%; Llama-8B 43.5% vs 83.0% for 70B; screening rounds 98.0% to 56.5% (window 10) | Yang et al. 2025 (a23, b14, b23) | [S] (K15) |
| Over-generate and rank hits a diversity wall | 4,000 seeds, about 200 non-duplicate; novelty 4.84 human, 5.64 AI, 5.81 AI reranked; 49 ideas per arm, 79 reviewers, 298 reviews; reviewer agreement 56.1% vs 66.0% (NeurIPS 2021) and 71.9% (ICLR 2024) | Si et al. 2024 (a28, b12, b13) | [S] (K16) |
| Case memory helps, but beats repeat-tries unclear | Memento: +4.7 to 9.6 OOD; K=0 to 4 lifts F1 59.9 to 64.5; K=8/16/32 flat; repeat tries alone 78.65 to 84.47 PM over five rounds. Empirical-MCTS AIME25: repeated sampling 70.0 vs 73.3 (30 problems) | a26, c11, c23, d09 | [C] (K17) |
| Distilled insights vs raw trajectories | ExpeL: HotpotQA 36% (insights) vs 31% (retrieve-only); ALFWorld 50% vs 55%. Sourati: one case best, 2.5 to 6 F1 gain. Decocted Experience: lessons beat raw cases, more K can hurt | a27, c12, c13, d10 | [E] (K18) |
| Speedup from past experience | Up to 56% less compute at highest similarity; 64 of 80 settings; baseline is no memory | Pan and Zhao 2025 (d11) | [S] |
| LLMs confirm first when testing hypotheses | 11 LLMs; success 6% to 78% in 45 turns; debiasing prompts lift average discovery 42% to 56%; Dual-Goal raised success in 8 of 11 models; non-thinking Qwen3-14B 0.23 to 0.13, Qwen3-32B 0.33 to 0.10 | Jhaveri et al. 2026 (d01, d02) | [S] (K21) |
| More examples can lower accuracy and raise confidence | 8 LLMs on the number game; thinking mode lowers confidence, raises accuracy | Xiong 2026 (d14) | [S] (K22) |
| LLMs under-generalise from one example | GPT does not generalise beyond one example; GPT-4o-mini a little | Bazigaran and Sohn 2025 (d13) | [S] |
| LLM judge can match historians on rubrics | r = 0.77 on 50 items (DeepSeek-R1); 400 questions, 10,891 criteria, 18 LLMs; top models near 30/100 | Gao et al. 2026 (d12) | [S] (K23) |
| Time-locked models leak little but know little | Strict leakage 0.0 to 0.1%; TypewriterLM pre-cutoff strict 0.2%; GPT-1900 sft 34.5% strict; CORE 0.1400 (pre-1900) vs 0.2602 (FineWeb-Edu) | Luo et al. 2026; Hla 2026 (c14, c15) | [S] (K19, K24) |
| Models beat experts at spotting real abstracts | 15 LLMs 81.4% vs 63.4% for 171 experts; top 20% experts 66.2% | Luo et al. 2024 BrainBench (b20) | [S] |

## 4. Mechanisms and models

These are mechanisms an engineer could build. Each is marked with how well it is supported.

### 4.1 Case-role tagging (from Scholl 2018; K02)
- **Input.** A claim plus the set of cases the agent cites for it (retrieved, recalled or supplied).
- **Step.** For each case, a short model call assigns one role from {generative, refinement, justification}. Code stores the tag.
- **Rule.** Code flags any claim whose justification set is smaller than a small threshold, or whose cases were chosen by the same model that made the claim. A flagged claim must be output as "hypothesis, scope: these cases", not "general rule".
- **Why.** Only the justification role needs sampling care. Generative uses (give me an idea) need none, so the rule does not slow idea generation.
- **Status.** The role split is [E] as philosophy. The tagging step has never been tested. The threshold N is unknown (K25: no source gives a number; use a flag, not a fixed N).

### 4.2 Scope statement on every case-derived claim (K03)
Code requires a field `scope = {population the cases come from, cases counted for, cases counted against, selection method}`. If the agent cannot fill the "counted against" field, code marks the claim as untested against unfavourable cases. This is Scholl's answer to the selection-bias horn, with the caveat from a13 that spurious support remains easy if the agent just writes "none".

### 4.3 Counter-case search, triggered by code (K21)
Jhaveri et al. (d01, d02) show LLMs test what fits their guess. The fix is a step "name the case or test that would refute this". Constraint from G1: it must not run on a schedule. Trigger it only when a signal fires: the claim is tagged justification and rests on cases the model itself picked. The measured gain was for thinking-mode models; non-thinking small models got worse with Dual-Goal (Qwen3-14B 0.23 to 0.13). So gate by model type.

### 4.4 Re-check the narrative against primary data (K07, K08)
Millikan, Mendel and Kepler show that tidy accounts of a case can be wrong. Mechanism: when a case summary is the sole support, code asks for a primary-data check (a number, a table, a raw log) and marks the case "secondhand" until one is shown. If no primary data is in context, the case counts at reduced weight. This is a plain bookkeeping rule, not a model judgement.

### 4.5 Scale a claim to a sample (K05, K06)
A story-supported claim plus a large-sample statistic that points the other way: update toward the statistic. Mechanism: when the context holds both a case and a quantitative test of the same thesis, code orders them: the larger sample is cited first and the case is demoted to "illustration". The Planck record is the model: stories said age mattered; 67 scientists said under 10% of variance; Azoulay's 452 stars found a different effect (outsiders enter). Both the story and the first test were partly wrong.

### 4.6 Case memory (K17, K18)
Memento-style: a bank of past (problem, plan, outcome) cases; retrieve K similar ones; the planner conditions on them. Measured details: K=4 is the sweet spot (F1 59.9 to 64.5; PM 72.2 to 78.5; K=8/16/32 flat, PM 78.2/78.1/78.1). Distilled lessons beat raw trajectories (d10, ExpeL 36% vs 31% on HotpotQA). One retrieved case is best for small classifiers (Sourati). The open point is the baseline: repeated tries alone moved Memento's PM from 78.65 to 84.47 across five rounds, so a bank must beat repeat-tries at equal tokens before it earns a place (G7).

### 4.7 Inspiration retrieval (K15)
MOOSE-Chem: from a corpus, retrieve the papers that could inspire a hypothesis. Screening in rounds with a window; hit ratio 83.7% at top 4% (corpus 300, GPT-4o). More rounds shrink the hit ratio (98.0% to 56.5% for window 10), so screening should be one round with a wide window (window 60: 71.6% after one round). Smaller models fall hard (Llama-8B 43.5% vs 83.0% for 70B). This is the S3 "grounded in retrieved distant analogues" step in practice.

### 4.8 Contamination control by form change (K11, K12)
Test memory by changing the form, not by splitting on date. LLM-SRBench transforms known equations; the best symbolic accuracy falls to 31.5% on the transformed set. Direct prompting without data gets only 2.1 to 7.2%; data-checked LLM-SR gets 10.8 to 31.5%. The gap between original and transformed problems is the memory share. A date split is the weaker test (FIRE-Bench: gpt-5 medium 44.5 to 23.1 on a few tasks is noise, not memory).

### 4.9 Rubric judge validated against humans (K23)
Gao et al. (d12): six candidate judges were checked on 50 items against historians' 0/1 marks; DeepSeek-R1 reached Pearson 0.77. Mechanism for our own use: before any LLM judge scores case-use answers, have two humans score 50 items, compute agreement, and accept the judge only above a stated bar.

## 5. What holds up

**Holds up.**
- The Pitt dilemma as a statement of the problem. Four sources restate it without dispute (K01). The proposed escapes (grouped designs, scoped claims) are accepted but unmeasured.
- Quantitative checks of famous theses can overturn or reshape them. Planck's principle: early tests found little (under 10% of variance); the later large test found a different effect (+8.6% outsider output on 452 stars).
- Memory of equations is real: the same equations drop to 31.5% best when transformed (LLM-SRBench; K12 [E], two independent sources).
- Discovery from real work is hard for agents: ScienceAgentBench, DiscoveryBench, DiscoveryWorld, FIRE-Bench all report under half, from different groups (K13). They agree in direction, not in measure.
- Distilled insight beats raw trajectories (ExpeL, Decocted Experience; K18 [E]).

**Failed, contested or weak.**
- The VPI programme had limited impact; no pooled effect or coder agreement found (K04). One critic (McAllister) says it was badly designed; his criticism is secondary.
- Planck's principle: the 1978 result is one episode (Darwin in Britain). Physics and social-science replications were not found. The 8.6% effect is mostly from early deaths and is imprecise for older stars.
- Millikan and Mendel are disputed. The Millikan defence (Goodstein) comes from a Caltech physicist. The Mendel bias model fits but is not proof.
- Case memory over repeat-tries: Memento's baseline rises from 78.65 to 84.47 by repetition alone. Empirical-MCTS: repeated sampling 70.0 vs 73.3 with memory plus an evolving prompt, 30 problems, one seed; the gain comes with the prompt, not memory alone (d09). Memento's 79.40% test score uses a case bank built from validation (critique item 9).
- Si et al. (K16): novelty up (4.84 to 5.64), feasibility not; reviewer agreement is low (56.1%), so "better ideas" is not shown.
- Date-split contamination: noisy (K11).

**Moderators.**
- Model type: debiasing prompts help thinking models, can hurt small non-thinking ones (d02).
- Number of cases: Memento K=4 best, Sourati one case best; more retrieved raw cases can hurt (d10).
- Similarity: Pan and Zhao's 56% speedup holds at the highest similarity (near-repeat questions) (d11).
- Entry barriers: Azoulay's effect needs low barriers.
- Network distance: Cheng and Weinberg hump shape.

**Interventions that worked.** Debiasing prompts for thinking-mode models (42% to 56% average rule discovery); distilled lessons over raw cases; retrieval with one wide screening round; form-change controls.

**Interventions that did not.** Dual-Goal on non-thinking small models (0.23 to 0.13); more than about 4 retrieved cases; multiple screening rounds (98.0% to 56.5%); date-split contamination control as a clean test.

## 6. Language models

No study tests case-as-evidence use directly (K20). Nearby results:

- **Confirmation in hypothesis testing** (d01, d02). 11 LLMs on a Wason-style rule task. Task success 6% to 78%. Models mostly choose tests that fit their current guess. Higher incompatible-to-compatible test ratio goes with higher success. Two human debiasing prompts lifted average discovery from 42% to 56%. Thinking-mode example: Qwen3-32B I:C 0.14 baseline, 0.54 Think-in-Opposites, 0.77 Dual-Goal. Non-thinking Qwen3-14B and 32B lost success with Dual-Goal. A toy numeric task, not case picking.
- **Induction from examples** (d13, d14). LLMs do not over-generalise from a few examples; GPT does not generalise beyond a single example. But as examples accumulate, eight open LLMs get less accurate and more confident; thinking mode lowers confidence and raises accuracy. So the failure to guard against is rising overconfidence, not hasty generalisation (critique gap 1 note).
- **Recall versus derivation** (K12). Direct prompting recovers 2.1 to 7.2% of transformed equations; data-checked search 10.8 to 31.5%. Contamination via verbatim recall is detectable at 92 to 100% accuracy for some datasets (a25, c09: GPT-4 contaminated on AG News, WNLI, XSum), but only verbatim, not paraphrased knowledge.
- **Rediscovery of findings** (K09, K10). FIRE-Bench best F1 46.7. False positives are 76.4 to 95.0% contradictory or unrelated conclusions, so the weak link is turning evidence into a conclusion and designing the experiment, not coming up with an alternative. Run-to-run noise is high: median CV 0.37 for the best agent, over 0.6 for weaker ones. The same task can differ by 56 F1 between agents (82.6 vs 26.4). The judge pipeline: precision 0.95, recall 0.86, F1 0.89.
- **Composition** (K14). DiscoveryWorld unit tests 0.66-0.77 completion; full tasks 0.18-0.38. 11 human scientists completed 66% of tasks.
- **Case memory** (K17, K18). See 4.6. Insight memory about equals trajectory memory.
- **Idea generation** (K16). LLM ideas rated more novel; low diversity; low reviewer agreement. Over-generate and rank hits the diversity wall (4,000 seeds, about 200 unique). This agrees with schema G8 (no model as final selector of ideas).
- **LLM as historian** (d12). Top models near 30 of 100 on Chinese history rubrics; judge r = 0.77. Not about method or case use.
- **BrainBench** (b20). 15 LLMs average 81.4% vs 63.4% for 171 experts at picking the real abstract. This is a pattern-prediction result, not a discovery result.
- **Time-locked models** (K19, K24). Clean from leakage (0.0 to 0.1% strict) but weak (TypewriterLM ARC-E/ARC-C/HellaSwag 43.3/27.9/36.1 vs Qwen3-4B 77.4/51.6/65.9). GPT-1900 mostly failed to rediscover; one output echoed Planck's "definite quantities of energy". No scored result.
- **AI Scientist, co-scientist** (b19, b21). One case or under $15 per paper; reviewer AUC 0.65 (same as humans), F1 0.57 vs 0.49. The reviewer is itself an LLM.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status as above.

### Add now (established)

1. **Treat self-picked cases as hypotheses, not proof; require a scope statement on case-derived claims.** G (evidence discipline), O verify, S8. [E] K01, K02, K03; evidence a01, a02, a07, a11, a13, a17, a04. Note: this is rule-by-argument; its effect on accuracy is unmeasured, so it goes in as a cheap guardrail only (cost: one field in the output). Keep it under G7: if it costs tokens without a gain on our bench, drop it.
2. **Memory of a famous fact is not evidence; check against data or a changed form.** G (G10-style), O verify, S4. [E] K12; a24, b15, b16, c04, c24.
3. **Do not trust tidy retrospectives as process.** When input is a polished summary of a case, keep the original wording and mark it secondhand. G, S1 input hygiene. [E] K08; b07, b08.
4. **Case memory stores distilled lessons, not raw trajectories, and retrieves few (about 4).** memory. [E] K18 (two or more sources agree on distilled over raw; the exact K is [S]); a27, c12, c13, d10, c11.
5. **Do not use an LLM self-rating as the selector of ideas.** G8 (already in schema). [E]; supported here by Si et al. (reviewer agreement 56.1%).

### Test first

1. **Tag-and-flag rule (K02, K25).** Tag every case as generative / refinement / justification; flag justification claims on few or self-picked cases. S/O, G. [S] no direct study. Evidence a12, a13, d13, d14. See U1.
2. **Counter-case step for justification claims, code-triggered, thinking models only (K21).** O, G1-compatible. [S] d01, d02. See U2.
3. **Confidence must track case quality, not count (K22).** G. [S] d13, d14. See U3.
4. **Weight a large-sample statistic above a story (K05).** G. [C] b01, d04, d06. See U4.
5. **Case bank versus repeat-tries at equal tokens (K17).** memory. [C] c23, d09, d10. See U5.
6. **Primary-data check on famous cases (K07).** G source check. [C] d07, d08. See U6.
7. **One wide screening round for inspiration retrieval (K15).** O. [S] b23. See U7.
8. **Controls checklist to cut contradictory conclusions (K10).** O. [S] a21, c02. See U8.
9. **Explicit case-selection rule versus free selection (K26).** O. [S] a15, a16. See U9.

Not to add (consistent with section 4b of SCHEMA.md): no schedule-based devil's advocate (G1), no multi-agent argument over cases (G9), no persona voters over case readings (G4). Section 9 lists what does not transfer.

## 8. Concrete tests on our bench

All arms at equal total tokens (setup cost counted, G7). Three seeds minimum. Report the plain model arm beside every scaffold arm.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 60 claims, each backed by 3 supplied cases; half hand-picked to fit, half random draws, with the truth known; the claim is true in half | Plain; role-tag + small-n flag (K02); scope statement (K03) | Accuracy of verdict; calibration (Brier); rate of "hypothesis" label on hand-picked set | Flag arm lowers confidence on hand-picked set; accuracy gain small (a few points) or none |
| T2 | 40 case-picking prompts ("find evidence for X") with known counter-examples in a corpus | Plain; refute step fired by code; refute step on a schedule | Share of picked cases that would refute vs confirm; final accuracy; split by thinking vs non-thinking mode | Gain for thinking mode, loss or zero for small non-thinking (per d02); scheduled arm worse than code-triggered (G1) |
| T3 | Number-game-style and claim-from-cases items, with 1, 3, 6 cases | Plain; confidence-must-track-quality rule | Calibration of stated confidence at each case count | Plain: confidence rises with n; rule: flat when quality is low |
| T4 | 30 planted conflicts: a vivid case story vs a large-sample statistic against it | Plain; scale-first ordering | Share of answers that move to the statistic | Plain under 50%; ordering raises it |
| T5 | 60 problems with repeat structure | No bank; repeat-tries; case bank (raw); case bank (distilled lessons), K in {1, 4} | Accuracy at equal tokens | Distilled > raw; bank beats repeat-tries only if gain > 3 points |
| T6 | 30 famous-case summaries, 10 with a planted wrong number, raw data supplied | Plain; primary-data check step | Share of planted errors caught; false alarms on correct summaries | Check step catches more; cost one tool call |
| T7 | 20 tasks from the MOOSE-Chem style or our own "find distant analogue" items | 1 wide screening round; 4 narrow rounds | Hit ratio; downstream accuracy | One wide round equal or better (per b23) |
| T8 | 10 FIRE-Bench tasks, 3 seeds | Plain; controls checklist | F1; share of contradictory conclusions; CV | Fewer contradictory conclusions; F1 up a few points; CV may stay high |
| T9 | A known case population (for example 100 known cases of a pattern) | Free case picking; Herfeld-style explicit rule | Coverage of the known population; diversity | Rule gives better coverage; unclear gain at equal tokens |
| T10 | 20 FIRE-Bench or LLM-SRBench items, original vs transformed | Plain | Gap original vs transformed = memory share | Diagnostic only; sizes how much of our bench is recall |

## 9. What does not transfer, and why

- **Humanities-style depth.** The philosophical case study is a thick narrative with context. Our agent works on short items with checks. The dilemma's "few cases" worry applies to claims, not to unit tests.
- **Planck's principle as agent behaviour.** An age effect on acceptance concerns human careers. The only part that carries is the method lesson (check the story on many units).
- **The VPI and Lakatos programmes.** They tested theories of method on episodes. We have no theory of method to test on history; we only borrow the sampling caution.
- **Memento, ExpeL, Empirical-MCTS "cases".** These are the agent's own past trajectories, not external historical cases (critique). They tell us about memory design, not about HPS case evidence.
- **Benchmarks as case-use tests.** FIRE-Bench, DiscoveryWorld and ScienceAgentBench test the whole discovery cycle on recent ML papers or simulated worlds, not the use of historical cases (K20). The link is by analogy.
- **Chinese history rubric judge** (d12) is for facts and arguments on exam history, not case-use judgement.
- **Time-locked models** are too weak to rediscover anything (ARC-E 43.3 vs 77.4); not usable now.
- **Rules built for humans' confirmation bias.** The Wason prompts help thinking-mode LLMs and hurt small non-thinking ones, so the human recipe does not carry unchanged.
- **Planned numeric thresholds for N.** No source gives N. A fixed N is a guess; use a flag.

## 10. Open questions

1. Does tagging cases by role and flagging small-n justification change accuracy or calibration at equal tokens? No study (critique gap 1).
2. How often do LLMs pick confirming cases from text, as opposed to confirming tests in a toy rule task (d01)? Not yet measured.
3. What did the VPI programme find, in effect sizes and coder agreement? Needs Laudan et al. 1986 and Donovan, Laudan, Laudan 1988 (not opened; a08, b09).
4. Does a case bank beat equal-attempt repeats with matched tokens? Memento's gap to repeats is unresolved; the Empirical-MCTS result is from 30 problems, one seed.
5. Which contamination control best predicts held-out performance (form change, synthetic, date split, time-locked)? Nothing new found (critique gap 5).
6. Are there Planck replications in physics or social science? None found.
7. Can an LLM rebuild a historical discovery from period text, and how close is it to the historians' account? No scored study (K24).
8. How reliable are LLM judges for case-use analyses? Only the 0.77 correlation on 50 history exam items; no kappa.
9. Does Herfeld's explicit rule beat free case selection? No test (K26).
10. How many cases make a method claim stable? No numbers in any source (K25).
11. The key book (Sauer and Scholl 2016) and Pitt (2001), Hull (1978), Giere, Kinzel, Chang were not read in full; some of the above may be answered there.

## 11. Sources

[V] = opened and read (page or PDF text) in the research session; [M] = snippet, reference, or summary only. Ids point to the evidence files.

**Philosophy of case studies**
- [M] Pitt (2001) The dilemma of case studies (a01). https://vtechworks.lib.vt.edu/items/28f2bd76-2e49-421a-9ded-e58fa0b3018f
- [V] Burian (2001) The dilemma of case studies resolved (a02-a06, b10 is the [M] DOI entry). https://ifz.at/sites/default/files/2022-01/Richard-Burian.pdf ; https://doi.org/10.1162/106361401760375794
- [V] Scholl (2018) Scenes from a marriage: the confrontation model of HPS (a07, a12, a13). https://www.repository.cam.ac.uk/handle/1810/287961
- [M] Laudan, Donovan, Laudan et al. (1986) Scientific change (a08, b09). https://doi.org/10.1007/978-94-009-2855-8_1
- [M] Giere (1973, 1985) (a09); Hull (1992, 1998) (a10); Schickore (2011) (a11): known only via Scholl 2018 references.
- [M] Chang (2011) (a14); Kinzel (2015) Narrative and evidence (a18, b11). https://philarchive.org/rec/KINNAE ; https://doi.org/10.1016/j.shpsa.2014.12.001
- [V] Herfeld (2025) Enhancing the function of case studies, Synthese 205:167 (a15-a17). https://link.springer.com/content/pdf/10.1007/s11229-024-04792-9.pdf
- [M] Lakatos (1971, 1972) (a19), via Burian.
- [V] McAllister (2018) Using history as evidence in philosophy of science (d03, d04, d05). https://scholarlypublications.universiteitleiden.nl/download/1887/7425
- [M] Sauer and Scholl (eds. 2016) The Philosophy of Historical Case Studies (c21). https://link.springer.com/book/10.1007/978-3-319-30229-4
- [M] Langley et al. (1987) Scientific Discovery (c19); Kolodner (1993) (c20).
- [V] Schickore (SEP) Scientific Discovery (b07). https://plato.stanford.edu/entries/scientific-discovery/
- [V] Hepburn and Andersen (SEP) Scientific Method (b08). https://plato.stanford.edu/entries/scientific-method/
- [V] Wikipedia History and philosophy of science (b24). https://en.wikipedia.org/wiki/History_and_philosophy_of_science

**Quantitative tests of case theses**
- [V] Azoulay, Graff Zivin, Fons-Rosen (2019) Does science advance one funeral at a time? NBER w21788 (b01, b02, b25, b26). https://www.nber.org/system/files/working_papers/w21788/w21788.pdf
- [M] Hull, Tessner, Diamond (1978) Planck's principle, Science (b04); read via McAllister (d04). https://doi.org/10.1126/science.202.4369.717
- [V] Wikipedia Planck's principle (b03). https://en.wikipedia.org/wiki/Planck%27s_principle
- [V] Cheng and Weinberg (2024) Old and connected versus young and creative, NBER w33030 (d06). https://www.nber.org/papers/w33030
- [V] Goodstein (2000) In defense of Robert Andrews Millikan (d07). https://calteches.library.caltech.edu/4014/1/Millikan.pdf
- [V] Wikipedia Oil drop experiment (b05); Gregor Mendel (b06). https://en.wikipedia.org/wiki/Oil_drop_experiment ; https://en.wikipedia.org/wiki/Gregor_Mendel
- [V] Pires and Branco (2010) A statistical model to explain the Mendel-Fisher controversy (d08). https://arxiv.org/abs/1104.2975

**LLM and AI studies**
- [V] Wang et al. (2026) FIRE-Bench (a20-a22, c01-c03, c18). https://arxiv.org/abs/2602.02905
- [V] Yang et al. (2025) MOOSE-Chem (a23, b14, b23). https://arxiv.org/abs/2410.07076
- [V] Shojaee et al. (2025) LLM-SRBench (a24, b15, b16, c04, c22, c24). https://arxiv.org/abs/2504.10415
- [V] Shojaee et al. (2024) LLM-SR (c05). https://arxiv.org/abs/2404.18400
- [V] Duan et al. (2024) / Golchin and Surdeanu (2024) Time travel in LLMs (a25, c09). https://arxiv.org/abs/2308.08493
- [V] Zhou et al. (2025) Memento (a26, c11, c23). https://arxiv.org/abs/2508.16153
- [V] Zhao et al. (2024) ExpeL (a27, c12). https://arxiv.org/abs/2308.10144
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? (a28, b12, b13, b22). https://arxiv.org/abs/2409.04109
- [V] Jansen et al. (2024) DiscoveryWorld (a29, b18, c06, c25). https://arxiv.org/abs/2406.06769
- [V] Majumder et al. (2024) DiscoveryBench (a30, c07). https://arxiv.org/abs/2407.01725
- [V] Chen et al. (2025) ScienceAgentBench (a31, b17, c08). https://arxiv.org/abs/2410.05080
- [V] Yang et al. (2024) LLMs for automated open-domain scientific hypotheses discovery (a32, c10). https://arxiv.org/abs/2309.02726
- [V] Gottweis et al. (2025) AI co-scientist (b19). https://arxiv.org/abs/2502.18864
- [V] Luo et al. (2024) BrainBench (b20). https://arxiv.org/abs/2403.03230
- [V] Lu et al. (2024) The AI Scientist (b21). https://arxiv.org/abs/2408.06292
- [V] Sourati et al. (2023) Case-based reasoning with language models (c13). https://arxiv.org/abs/2301.11879
- [V] Hla (2026) Machina Mirabilis / GPT-1900 (c14); [M] summary entry d15. https://michaelhla.com/blog/machina-mirabilis.html
- [V] Luo et al. (2026) TypewriterLM (c15, c26). https://arxiv.org/abs/2606.02991
- [V] Simons, Zichert, Wuthrich (2025) LLMs for HPS (c16, c27). https://arxiv.org/abs/2506.12242
- [V] Zichert and Simons (2026) (c17). https://arxiv.org/abs/2606.04118
- [M] LLMs for history, philosophy and sociology of science (2026) (a33). https://doi.org/10.1016/j.shpsa.2026.102151
- [M] Lean et al. (2023) Digital literature analysis for empirical philosophy (a34). https://doi.org/10.1086/715049
- [V] Jhaveri et al. (2026) Failing to Falsify (d01, d02). https://arxiv.org/abs/2604.02485
- [V] Lu et al. (2026) Empirical-MCTS (d09). https://arxiv.org/abs/2602.04248
- [V] Shen et al. (2026) Decocted Experience (d10). https://arxiv.org/abs/2604.04373
- [V] Pan and Zhao (2025) Can past experience accelerate LLM reasoning? (d11). https://arxiv.org/abs/2505.20643
- [V] Gao et al. (2026) ProHist-Bench (d12). https://arxiv.org/abs/2604.24690
- [V] Bazigaran and Sohn (2025) Concept generalization (d13). https://arxiv.org/abs/2512.20162
- [V] Xiong (2026) Language models lack systematicity (d14). https://arxiv.org/abs/2605.05851
- [M] Underwood, Nelson, Wilkens (2025) Can language models represent the past (d16). https://arxiv.org/abs/2505.00030
- [M] Valleriani et al. via Science News (2026) (d17). https://sciencenews.org/?p=3145474

**Links to other subfields run in parallel** (not covered here): Anomalies and paradigm change; Conceptual change and revolutions; Methodologies of discovery; Scientific discovery systems; Peer review and replication; Reproducibility and methods; Social epistemology; Mathematics history; Epistemic diversity; Cognitive bias and premature closure; Analogy and distant sources; Analogical prompting for LLMs; Calibration and overconfidence; Novelty measurement.
