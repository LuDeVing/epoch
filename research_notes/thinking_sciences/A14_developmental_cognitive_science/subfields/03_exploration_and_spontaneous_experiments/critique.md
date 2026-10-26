# Critique: A14.03 Exploration and spontaneous experiments (cross-check)

Re-opened this session (full text read): Cook, Goodman, Schulz 2011 (PDF); Kosoy et al. 2022 (CLeaR, arXiv); Siegel et al. 2021 (PDF); Samiei et al. 2026 (PDF, partial text); Jhaveri et al. 2026 (PDF). Abstract only (arXiv API): Alderete 2026, GX-Chen 2025, Pan 2025. Downloads of the last three came back damaged, so their tables could not be re-read.

## Corrections made
1. Cook 2011 headline numbers CONFIRMED: Exp 1 informative test All Beads 1/20 (5%), Some Beads B 9/20 (45%), AB 10/20 (50%); chi2(1,N=40)=8.53 and 10.16, p<.005; B vs AB chi2=0.10; 65% of All Beads never pulled the pair apart. Exp 2: 1/20 vs 9/20, chi2=8.53. Breadth 3.83 / 4.06 / 3.95, F(2,60)=1.08 ns. 63% vs 18% for the snapped-apart action.
2. Missing detail added: Cook excluded and replaced 7 children (6 experimental error: 1 All Beads, 1 Some B, 4 Some AB; 1 language barrier). The group means are 53 (All Beads), 55 (B), 54 (AB) months, not 54 for all. Warm-up video data exist for only 17, 16 and 12 children, so the warm-up F tests in b01 rest on partial samples.
3. Cook footnote 3: authors tested each action as a single planned comparison and did not correct for multiple tests. The "one-tailed" wording in b03 was not confirmed in the text I read; treat it as unverified.
4. Kosoy 2022: sample is children aged 4-5 (N=85, 20-23 per cell), not 4-6 as in c03. 71% vs 32%, p=0.002, 14.07 vs 10.58 actions, 178.65 vs 195.38 s all CONFIRMED.
5. Siegel 2021: abstract says N=160; methods say 184 recruited, 16 excluded (168 analysed). The gap is still unexplained. r=0.95 (video) and 0.89 (motion sensor) confirmed in text. a14 and b09 agree on the numbers.
6. Samiei 2026: 306 adults, 102 per condition; conjunctive object identification Active 0.69, Observer 0.45, Proposer 0.12; rule selection 0.82, 0.69, 0.57. CONFIRMED.
7. Jhaveri 2026: 42% to 56% abstract figure CONFIRMED. Correction to c23: Qwen3-32B distilled from Wason-with-TiO traces reached 0.77 on blicket (base 0.57, TiO prompt 0.86), so distillation closed about 70% of the prompt gain, not "less" in a small sense. Qwen3-8B: base 0.32, TiO 0.40, distilled 0.34-0.38.
8. Alderete 2026: abstract confirms 1,085 trials and 94% of accuracy gain from context graphs. Model names, 73.3% to 93.9% and p-values were not re-checked.
9. Pan 2025: abstract says only o1 beats humans. Line c24 says o1 and DeepSeek-R1 beat humans and gives R1 85 elements vs humans 42, with "t=3.40 p<0.027" (a t of 3.40 with p that large is odd). Left as unresolved.

## Contradictions between sources
- Pan abstract (only o1 beats humans) vs c24 (R1 also). Unresolved.
- Reasoning models: Samiei and Jhaveri favour thinking modes; o4-mini (a reasoning model) used the fewest tests but was only modest on AND rules. Claim K16 marked contested.
- Kosoy 2022 says children's play fits neither info gain nor reward; Cook 2011 frames the same behaviour as expected-information-gain driven. The two are about different regimes (simple toy vs larger hypothesis space), not strictly contradictory.
- Binz & Schulz: a19 says GPT-3 does well on reward on the horizon task while c07 says no directed exploration. Both true; reward and directed exploration are different measures.

## Weak spots
- Cook 2011 is two experiments, one lab, N=60 and N=40, and Exp 2 followed a pilot observation. No direct replication was found, but search was rate limited (see GAPS 1).
- About half of the ambiguous group did not run the test; the criterion was strict.
- Confounds in the design: ambiguity, base rate and expected information gain move together. No design keeps ambiguity but removes the gain.
- Three rival readings (expected information gain; cheap trial and error; learning within the session) are not separated by any paper found.
- Siegel is aggregated across condition means, sound-based, one museum, experimenter not blind; N inconsistency.
- Samiei Passive Proposer: proposers saw outcomes that did not match their own proposals, which alone could explain the 0.12 (below passive observers). Not the same as "no agency".
- GX-Chen and Jhaveri correlations (rho 0.76; 0.65 and 0.74) are read from figures, and points are model-prompt combinations, not independent trials.
- Alderete is a preprint from a company selling agents, with one-tailed tests and one model family; the stochastic condition showed no gain.
- Contamination: LaMDA cited the authors' own blicket papers, so any blicket-style test of our agent needs renamed or new machines.
- Prompt claims on small cells (Jhaveri non-thinking models) go both ways.

## Only seen in snippets or secondhand (opened:false or not re-read)
Gweon & Schulz 2008 is opened in b06 but a23 lists it unopened; Schulz & Bonawitz 2007 numbers come from the author manuscript (a08) while b07 is secondhand; Bonawitz 2012 balance study (a15 opened vs b19 not opened, so use a15); Legare 2012, Lucas 2014, Gopnik 2017, Schulz-Gopnik-Glymour 2007, Chen & Klahr 1999 (all unopened); Yiu 2025 empowerment gain (context only); GX-Chen 2025 values (figures only); Pan 2025 and Alderete 2026 tables (not re-read).
Independence note: a12, a13, b08 are all one paper (Bonawitz 2011) and count as one source; a01-a07, b01-b05, b26, c01-c02 are all Cook 2011.

## GAPS
1. Has anyone replicated the Cook bead contrast (any lab, any age, any 2012-2026 sample) or failed to? Search with Google Scholar "cited by" and a Many-Labs or OSF registry check, not only the rate-limited APIs.
2. Does an LLM run the isolating test more often when the evidence is ambiguous than when it is unambiguous (the Cook base-rate contrast)? If not tested anywhere, build the toy task and measure the rate at equal tokens for a plain model, a model with a stated rule list, and the code-computed gate.
3. Is the ambiguity trigger needed, or does always running the splitting test cost less than the trigger saves? Compare gate vs always-split vs never-split on tasks where the rules sometimes tie and sometimes do not.
4. Which reading of Cook is right: prior knowledge of isolation, trial and error, or learning within the session? Look for any study that gives the informative action for free or trains isolation first (Siegel, Legare 2012, Schulz Gopnik Glymour 2007).
5. How large is the real LLM gain from enumerating and eliminating hypotheses in code (GX-Chen 2025 figure values, Piriyakulkij 2024 per condition), and does it hold at modern model scale and equal tokens?
6. Does the Samiei "own outcome" effect hold for LLM agents: interleaved test-then-choose loop vs a batch plan of tests, and was the Passive Proposer drop due to mismatched outcomes?
7. Does a break-the-leading-rule prompt (Think-in-Opposites) help only in thinking mode, as Jhaveri's blicket numbers suggest, and at what token cost? Re-run at equal tokens with a code check on the proposed test.
8. Does a worked example or stated hypothesis in context narrow an LLM's open-mode exploration the way teaching narrowed children (Bonawitz 2011), measured as distinct candidate classes?
9. Resolve the open numbers: Siegel N (160 vs 168), Pan R1 vs humans, Alderete tables, and the GX-Chen figure values by reading the full tables.
10. When should the selector switch from information gain (closed rule set, S7) to entropy or empowerment or novelty distance (open world, S3)? Find a test with both regimes.


## Gap search results (2026-10-27)

Evidence is in `evidence_d.jsonl` (d01-d20; 9 opened in full this session, 11 abstract or snippet only and marked opened:false). Claims K26-K31 were added and K01, K06, K12, K14, K15, K16, K25 were updated. Semantic Scholar and OpenAlex were rate limited again; Europe PMC citations, Crossref, arXiv and web search were used instead. No LLM calls were made.

**Closed**
- Gap 9, numbers. Siegel N is 168 analysed (184 recruited minus 16 excluded, about 7 x 24); the abstract's 160 is the odd one. Pan 2025 contradicts itself on DeepSeek-R1: main text R1 85 vs humans 42 elements (t=3.40), abstract names only o1, appendix says near human-level and below o1. Alderete and GX-Chen were re-read: Alderete Base 87.3%, CG 77.3%, CG+DB 89.1% (raw, 110 per arm). GX-Chen Table 1 is near ceiling for random play at 4 objects (0.968) and very noisy at 8; the Q&A gain from hypothesis sampling has no table value, figure only.
- Gap 3, as a design argument only. A toy model shows the code gate beats always-split iff gate cost < (1 - tie rate) x split cost, and never-split beats a costly gate when ties are rare. This follows from my assumptions and is not an LLM measurement.
- Gap 7, partly. Think-in-Opposites on blicket: large gain only for Qwen3-32B thinking (0.57 to 0.86); other thinking models +0.02 to +0.11; non-thinking mixed (+0.08, -0.05, -0.08, +0.04). Tokens per turn on Wason rose 12-58% in four of five thinking models. No code check on the proposed test and no equal-token rerun.

**Partly answered**
- Gap 1. 112 Europe PMC citing records scanned: no direct replication and no failed replication. Conceptual extensions exist with different tasks: Lapidow and Walker 2020, van Schijndel 2015, Moeller 2022, Koksal 2021, McCormack 2016, Bramley 2022. OSF and Many Labs registries not checked. The contrast is still a single-lab result.
- Gap 4. No study trains isolation first and repeats Cook. Indirect evidence: when the informative action is on a menu, 4-6-year-olds pick it (Lapidow and Walker, abstract only), so the free-play base rate is about generating or wanting the test (reading A, partial). Moeller 2022 shows detecting confounding and choosing a controlled test are unrelated. Ruggeri 2019 and Legare 2012 fit learning within the session (reading C). Cheap trial and error (reading B) was not tested. Verdict: no single reading wins.
- Gap 5. Piriyakulkij: InfoGain 6.55/8 vs LLM-chosen 4.72 vs random 5.84 (GPT-4 Turbo class, calls not tokens). GX-Chen: size unknown. Modern scale and equal tokens still untested.
- Gap 6. Samiei design re-read: the Proposer saw another person's outcomes, so plan mismatch and lack of control are confounded. No LLM batch arm exists.

**Still open (need our own runs with real model calls)**
- Gap 2: no LLM version of the Cook contrast found.
- Gap 8: no LLM analogue of Bonawitz 2011 found; only diversity papers (Lee 2025, Xiong 2026).
- Gap 10: no switching rule from information gain to entropy or empowerment. Working guess, untested: information gain while a countable rule list has more than one live member, diversity then control when the world is open.

**Confidence notes**
- The 11 abstract-only items must not be cited for numbers until opened.
- Jhaveri table values were read from a PDF text dump with misaligned columns; they match the earlier note on the two headline figures.
- Next step for gaps 2, 3, 8: a small toy blicket harness with three arms (plain, rule list, code gate) at equal token budgets.
