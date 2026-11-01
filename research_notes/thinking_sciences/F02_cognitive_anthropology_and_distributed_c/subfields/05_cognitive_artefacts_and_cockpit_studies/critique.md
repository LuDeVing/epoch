# Critique: F02.05 Cognitive artefacts and cockpit studies

## Numbers re-opened this session (all from primary text/PubMed/arXiv)
Confirmed: Hutchins 1995 (more than 100 flights; 2,000 lb card steps; +/-5 kt callout; bug base about 10 kt); Haynes 2009 (3,733/3,955; 1.5% to 0.8%; 11.0% to 7.0%); Urbach 2014 (101 hospitals; 109,341/106,370; 0.71% to 0.65%, OR 0.91; 3.86% to 3.82%, OR 0.97); Pronovost 2006 (108/103 ICUs; 375,757 catheter-days; 2.7 to 0; 7.7 to 1.4; IRR 0.62 and 0.34); Nye 2021 (8.8/20.1 few-shot, 31.8/50.7 fine-tune); TICK (46.4% to 52.2%, +7.8%); SWE-agent (12.47% of 2,294; 10.7 point ACI gain; 18.0/15.0/10.3 editor ablation); MAST (6.20/8.20/9.10%, 41% to 86.7%); Stechly (Game of 24 5%, 3%, 36-38%, sampling 28%/42%).

## Corrections
1. Huang 2024 (b13, c09): the table columns are number of LLM calls (1, 3, 5), not "rounds". GPT-3.5 GSM8K 75.9 to 75.1 (3 calls) to 74.7 (5 calls). b13 "after 1 round/2 rounds" and c09 "round 2/round 3" mislabel this; a26 is right. Numbers themselves are correct.
2. CoVe (a27, b16, c10): "hallucinated entities 2.95 to 0.68" is the paper's own sentence, but its Table 1 shows 2.95 belongs to Llama 2 70B Chat CoT, while the Llama 65B few-shot negatives are 0.98. The 0.68 row is garbled in extraction. Treat the hallucination-count claim as unreliable; list precision 0.17 to 0.36 and FACTSCORE 55.9/60.8/63.7/71.4 are sound.
3. c07 (Urbach) was marked opened:false but the numbers match the abstract just opened. Fine.
4. a21, b06, c07 (Urbach), a20, b05, c05 (Haynes), a19, b11, c06 (Pronovost), a26, b13, c09 (Huang), a27, b16, c10 (CoVe), a23, b17, c16 (TICK) are the same sources repeated. Independent source counts in claims.jsonl count each once.

## Contradictions
- Checklists: big gains (Haynes, Pronovost, Haugen) vs nulls (Urbach, Reames x2, Matching Michigan). The best reading is that gains depend on enforcement and local culture, not on the list. This contradicts any naive "add a checklist" reading of Hutchins.
- LLM checks: TICK, CoVe, Self-Refine report gains from self-generated checks; Huang and Stechly show self-critique without outside signal fails. Likely reconciliation: gains come from structure plus an independent view (separate context, per-item YES/NO) or an external verifier. Not yet tested head to head at equal tokens.
- b19/b20 say more mandatory checking can hurt; TICK/CM2 say checklists help. Different uses (inference gate vs reward/judge).

## Weak spots
- Hutchins 1995 has no statistics, no with-and-without bug test (b23). The "system remembers" claim is interpretive. "Transposition errors are most frequent" is a citation to Norman/Wickens, not data.
- Zhang & Norman: undergraduates, Tower of Hanoi isomorphs, N=18 to 36 per experiment. Transfer to real cockpits or LLMs is argued, not shown.
- Haynes is uncontrolled before-after; Haugen is only 2 hospitals; Bergs meta-analysis pools 7 mostly weak studies.
- No LLM study directly tests Hutchins' mechanism (a chain of media beating one context). SWE-agent, PAL, scratchpad are the closest "tools reshape the task" tests, and they confound tool with prompt.
- Many LLM numbers are on different models and benchmarks; not comparable.

## Seen only in snippets (opened:false)
Norman 1991/1993 (a15, c04); Degani & Wiener 1993 figures "42 crews, 72 flights, 140 hours" (c08) not verified; Hollan/Hutchins/Kirsh full text (c25); Figueiredo 2025 (c19); LeRAAT / Virtual Co-Pilot 90.5% / 86.5% (c23); Auto-Eval Judge 87.9% (c24). Do not cite these numbers.
Also unverified by me: b19, b20, b21, b22 (2026 preprints) and c20, c22 were not re-opened.

## GAPS
1. At equal tokens, does a hard gate that blocks (enforced checklist item) beat the same item shown as advice in the prompt? (Decides whether guardrails G1-G12 need enforcement code.)
2. Which checks have an outside signal on our tasks (tests, tools, retrieval), and do the others (pure self-review) cost accuracy as Huang found, on our benchmarks?
3. Does a factored check in a fresh context beat an in-context check at equal tokens, and how much of it is just best-of-N?
4. What is the optimal number of checklist items before over-verification costs more than it saves (b20: 67 of 307 failures)?
5. Does a written ledger of computed constants (the speed-card analogue) improve long multi-step tasks versus recomputation, and at what task length?
6. Does changing only the tool or artefact interface (output format, error messages, linting) move accuracy for a fixed model, outside code tasks?
7. Is there a direct, controlled LLM test of Hutchins' redundancy claim: two independent checkers with different views vs one checker run twice?
8. Do the checklist-null results (Urbach, Reames) map onto LLM agents as "compliance without understanding"? Is there LLM data on agents ticking items without doing them?
9. Verify Degani & Wiener 1993 and Norman 1991/1993 from full text, including any empirical error rates for checklist skipping.

## Gap search results (evidence_d.jsonl d01-d17, claims K20-K27)

Search note: WebSearch quota ran out partway; arXiv/Semantic Scholar/OpenAlex APIs were rate limited. Sources were opened by direct URL (PDF text via pdftotext, or HTML). Several (Kamoi, Tam, He, Kim) were abstract-level only, marked in limits.

1. Hard gate vs advice (CLOSED for one task family, d01-d03). Zhang et al. 2026 (Qwen3-235B, 128 episodes per cell): shown checklist 0.55/0.59, self-written ledger 0.70/0.79, directive gate 0.84/0.87, enforcement gate 0.98/0.98. Gate used 0.79 to 0.92 times the raw-transcript tokens. Limits: gate helps only when failures are code-decidable and frequent; at 35B on tau2-bench airline no gain, on PM-Bench a judgement-bound gate fell below the raw transcript (0.55 vs 0.63); with thinking on, the gap shrinks. One preprint, one task family. Verdict: enforce code-decidable guardrails; keep judgement items as advice.
2. Outside signal vs self-review (MOSTLY CLOSED in general, OPEN on our benchmarks, d06-d07). CRITIC without tools equals CoT (HotpotQA F1 46.1 vs 50.5 with tools); GSM8K PoT -1.8 without the interpreter. Kamoi 2024 survey agrees. Mapping our G1-G12 to tool-backed or not is still to do on our own tasks.
3. Factored check vs in-context at equal tokens (OPEN, d05, d08). CoVe re-opened: factored beats joint (FACTSCORE 63.7 vs 60.8; F1 0.48 vs 0.46) but no equal-call or best-of-N control. Budget-aware work shows sampling baselines absorb much of such gains. Nobody found with the exact test.
4. Optimal checklist length (OPEN, d15). Only the b20 count (67 of 307) plus Degani & Wiener's argument that long lists invite non-use. No dose-response curve found.
5. Ledger vs recomputation (OPEN, d12; indirect). Sinha 2025 shows self-conditioning and decay over turns (Qwen3-32B under 50% within 15 turns) but does not test a ledger. Zhang 2026 shows an agent-written ledger beats a shown checklist (0.70 vs 0.55, 0.79 vs 0.59) but is not a ledger-vs-recompute test.
6. Interface-only change outside code (PARTLY CLOSED, d13-d14). Format restrictions lower reasoning accuracy (Tam 2024); template shifts up to 40% (He 2024, a code translation task). Both abstract-level; no result for error-message or tool-output design outside code.
7. Two independent checkers vs one run twice (OPEN, d09-d11). No direct controlled test. Nearest: MoA with different models +2.7 over self-consistency (within noise at n=1000); debate adds almost nothing over voting; error agreement 60% when two models are both wrong, so same-family checkers are not independent.
8. Ticking without doing (CLOSED for the existence of the effect, d03-d04). Zhang 2026: 24 of 26 and 20 of 20 on-turn re-executions were of steps already marked done in the agent's ledger. SOPBench scores skipped check calls as failures even with a right final state; only 5 of 18 models pass above 60%. Prevalence on our agent is unmeasured.
9. Degani & Wiener (PARTLY CLOSED, d15-d16). Opened the 1991 NASA CR-177549 full text (the 1993 Human Factors paper not opened). It has no empirical skip rates (ASRS narratives not analysed statistically). Norman 1991/1993 still unverified from full text.

Net: gap 1 and 8 give usable guidance now (gate code-decidable items; log whether checks actually ran). Gaps 3, 4, 5, 7 need our own experiments; the claims' agent_test fields carry the designs. Treat the GitAuto blog (d17) as an anecdote only.
