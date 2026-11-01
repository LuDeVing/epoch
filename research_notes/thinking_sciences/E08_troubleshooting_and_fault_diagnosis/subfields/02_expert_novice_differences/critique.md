# Critique and cross-check: E08.02 Expert-novice differences

## Re-opened sources (this session, pdftotext of the real PDFs)
Confirmed with no change: Johnson 1987 fuel pump 3/5 and open wire 2/5 novices, 45-minute cutoff, 1 of 5 failures hit the limit (a02); Johnson 1995 systems exam 19.82 (SD 1.94) vs 19.88 (SD 2.13), t(32)=.073 (a06); Gott 1995 Table: VTT3 59 (37) vs 95 (5), 1.27 SD; NIT 75 vs 87, .87; Frankenstation VTT 55 (31) vs 82 (23), .96; NIT 72 vs 80, .76; solve rates 63.6/70.6/83.3 (a12, a13); Katz/Hydrive t(19)=4.14 and Sherlock t[39]=-4.04, -3.72 (a10, a11); SREGym 72.6% to 62.6% and E2E 63.7/60.8/57.8 to 17.9/28.2/15.4 (b06, b08); OpsHarness 59.0/41.4/38.4/36.1 and 5.3 + 17.6 = 22.9 (c02, c03); Lu et al. 79.6, 90.0 (+10.8), 89.5 to 57.1, 11.4 extra rounds, 82.8% resource_probe, DiagGuard +21.1/+35.1 (c06-c10).

## Corrections and caveats
1. a10: the Hydrive t(19)=4.14 is a within-group pre/post test, not Hydrive vs control. "Only Hydrive improved" means the other two groups' pre/post change was not significant; it is not a between-group test.
2. a14: the swap (50/3/8) and self-test (11 of 16, 4 of 12, 2 of 14) counts come from Frankenstation (the transfer station), not the trained stations, and the scan tables are garbled; the figures match but should be read as counts of events, not per person. Violations (21/9/20) were not re-checked.
3. b07: the 3.82 vs 1.88 attempts figure is for the no-noise condition only.
4. Gott effect sizes are in control SD units (SDS = Sherlock, SDf = Frankenstation) with small cells (N 13-23).
5. a02: all samples in Johnson 1987 are 5 vs 5; "experts about 5 times faster" is on one task only.

## Contradictions
- Laban (2025, c24) says multi-turn costs reliability; Bi et al. (c14) found multi-turn adds aptitude. Not read directly. Task types differ.
- Strategy: Johnson 1995 says strategy type does not separate skill; Gott 1995 says logical-sequence violations do. Possible reconciliation: range/flexibility vs sequence quality. Open.
- Experts vs agents: a22 says expert personas do not help, yet c01/c15 say distilled expertise helps. Reconcile: a label does not work, content does.
- Chunking (a26, a27) vs "search" views: not settled.

## Weak spots
- Founding human data are small, 1980s-90s, military avionics and one generator study. No replications found for Johnson 1987.
- Sherlock evidence is by the developers (Gott/Lesgold group); no independent replication. Tutored group also got feedback; training time is not matched to a control.
- No LLM study compares agents against human experts on the same faults; "novice-like" behaviour is inferred from failure modes.
- Many 2026 LLM numbers come from single preprints with no peer review.

## Only seen in snippets or recalled, not opened
a27 Chase & Simon, a28 Chi et al., b19-b25 (Rasmussen & Jensen, Rasmussen 1983 page only partly, Gott 1993, Gugerty & Olson, Chi 1981, Kalyuga, Macnamara), c21-c24. Treat as unverified. a16 (Parker) was an abstract page only. Not re-opened this session: a19, a20, a21, a22, a26, b10-b18, c13-c20 (only first-pass reading).

## GAPS
1. Does distilled expert strategy text (not raw traces) improve a plain LLM agent on held-out novel faults at equal tokens? (Opsharness suggests yes; needs a direct test.)
2. Which part of Sherlock-style tutoring transfers to an agent: system model, strategy list, or the verify-before-swap rule?
3. Is there an independent replication of Johnson 1987 or Gott 1995 effect sizes, or a modern human expert-novice study with larger N?
4. Do LLM agents show the novice first-symptom anchoring pattern under controlled decoys, and does an enumerate-alternatives step remove it at equal tokens?
5. How should memory be written so it does not overfit? What regression gate size and held-out set are enough (OpsHarness rejected 37%)?
6. Is evidence-closure (grounded causal path) a better training/selection signal than final-answer accuracy?
7. Does the effect of expert persona prompts hold for diagnosis tasks specifically (a22 tested factual questions)?
8. Where does the skill/rule/knowledge (Rasmussen) split map onto agent behaviour: can we detect when an agent should switch from recalled rule to model-based reasoning?
9. Chase and Simon / Chi et al. numbers need opening: how large is the pattern-store advantage for fault cases, and does it vanish on random (novel) cases?
10. Is the repair-after-diagnosis gap (R2Act 91-99% vs 36.8-60.3%) caused by missing domain knowledge or by weak action validation?

## Gap search results (evidence_d.jsonl d01-d21; claims K26-K33 added)
Limits of this pass: the WebSearch quota ran out at the start, and arXiv, OpenAlex and Semantic Scholar APIs returned 429 (shared rate limit). So I could only open papers whose ids I already had. "Not found" below means "not searched for", not "does not exist". Chase and Simon (ScienceDirect 403) and Chi et al. (Wiley Cloudflare block) stayed closed.

1. Distilled strategy text vs raw traces (PARTLY CLOSED). OpsHarness: 59.0 vs ICL 38.4 vs Direct 36.1 at about equal tokens (106k/106k/112k), but time-split on the same systems and the harness also adds tools (d03). Trace2Policy (not diagnosis): unrefined distilled rules lowered strong models 7-9 points vs zero-shot (d06). Still open: a text-only arm and a novel-fault test. Claim K27 is marked contested.
2. Which Sherlock part transfers (OPEN). Hydrive vs the F-15 tutor differ in developer, task analysis and content; the t(19)=4.14 is within-group (d16). No ablation exists. K31.
3. Independent replication (OPEN). Only developer data: n=18/23/13 and 17/21/12 (d17). Nothing independent found, with the search caveat above.
4. Anchoring under decoys (HALF CLOSED). SREGym shows first-anomaly greed under injected noise, diagnosis down about 10 points for every agent (d12). Lu et al. code anchor lock and loudest-anomaly bias, and DiagGuard self-audit gives median +10.5 (d13, d14). Not shown: a controlled decoy, or an enumerate-alternatives step alone at equal tokens.
5. Memory-write gating (MOSTLY CLOSED on design, OPEN on size). Two independent sources support a gate: OpsHarness no-verify 0.33 vs 0.83 with gate (d02), Trace2Policy bypass fell to 66.8/67.5 (d07). Held-out sizes used were 40 and 139 cases (Trace2Policy), and the OpsHarness testbed size was not stated. No study varies gate size. K26.
6. Evidence closure as signal (OPEN). OpenRCA 2.0 shows the gap (61.5 vs 76.0) and model re-ranking (d10, d11) but only as evaluation. K29.
7. Persona on diagnosis (OPEN). Only the factual-QA test (162 personas, 2,410 questions) was opened (d18). K32.
8. Rasmussen levels to agent behaviour (PARTLY INFORMED). Luo et al. give a measurable proxy for rule-to-model switching: overrides beat corrections in every configuration, and raw-metric verification beats competing analysis (d15). No direct skill/rule/knowledge mapping. K30.
9. Chase and Simon, Chi (OPEN). Primary texts blocked; only a Wikipedia summary (d21). Do not cite numbers. K33.
10. Repair gap (CLOSED to a first answer). Mainly operation and plan validity: 67.9% wrong operation, 29.7% invalid structure, 1.3% wrong target; gold RCA with a fixed mapper only 0.599; live replay 48.3% (d08, d09). One benchmark, one group. K28 (K14 updated).

Caveats found: Cho et al. (d19) Study 1 reader was GPT-4o, so it is an agent-reader result, but the task is tutoring. Lu et al. failure-rate table is garbled in text extraction (d13); re-check before citing per-mode rates. Status changes: K16 note added (beats raw traces, not proven vs no text); K17 now 3 independent sources.
