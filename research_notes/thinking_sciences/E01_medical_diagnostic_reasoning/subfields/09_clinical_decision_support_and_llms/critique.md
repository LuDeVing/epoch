# Critique: Clinical decision support and LLMs (E01.09)

Cross-check of evidence_a, evidence_b, evidence_c (83 lines). Sources re-opened this session as text from D:/research_scratch/E01.09 (PDF/PMC text): Goh 2024, Nori 2025, Bean 2025, Brodeur 2024, McDuff 2023/2025 (arXiv and Nature), Hager 2024, Takita 2025, Rao 2023, Bond 2012. Downloaded PDFs deleted.

## Numbers re-checked (all confirmed unless noted)
1. Goh 2024: 76% (IQR 66-87) vs 74% (63-84), adjusted diff 2 (CI -4 to 8, P=.60), 519 s -- confirmed.
2. Nori: physicians 19.9% at $2,963; o3 78.6% at $7,850; MAI-DxO 81.9% at $4,735; ensemble 85.5% at $7,184; GPT-4o 49.3% -- confirmed.
3. Nori budget variant: the paper gives $2,396 in Section 4 but $2,397 in the introduction. Correction: record as about $2,396-2,397 (internal inconsistency in the paper).
4. Bean: 1,298 participants; 94.9% / 56.3% alone; under 34.5% / 44.2% with users; control 47.0% conditions; odds 1.76 (1.45-2.13); 2.21 conditions per chat, 34.0% correct; users 1.33, 38.7% -- confirmed. Note: evidence b11 says control disposition 43.0%; the text read shows 47.0% for conditions. Treat 43.0% as unverified.
5. Brodeur: 78.3% (70.7-84.8); 88.6% vs 72.9%; R-IDEA 78/80 vs 47/80 vs 28/80; correct test 87.5%; ER 65.8/69.6/79.7; landmark +20.2 (CI -0.4 to 40.9, P=.055); management +41.6 (22.9-60.4), +42.5 (25.2-59.8), +49.0 (31.7-66.3) -- confirmed.
6. McDuff: 59.1% vs 33.6% (P=.04); assisted 51.7% vs unassisted 36.1% (McNemar 45.7) vs search 44.4% (4.75, P=.03); table 51.8/44.5 -- confirmed. The abstract and table differ by 0.1 point (rounding between figures).
7. Hager: 87.5% German residents; 45.5% vs 58.8% for Llama 2 Chat; low-lab accuracy 26.5/70.2/45.8 -- confirmed. The "gap 16-25 points" was not re-found in text this pass.
8. Takita: 52.1% (47.0-57.1); physicians +9.9 (P=.10); experts +15.8 (4.4-27.1, P=.007) -- confirmed. Non-expert +0.6 not re-found.
9. Bond 2012: Isabel 3.45, DxPlain 3.45, DiagnosisPro 2.65, PEPID 1.70 -- confirmed.
10. Rao 2023: beta -15.8% (P<.001) and -7.4% (P=.02) -- confirmed. Note the folder's PMC10481210 file is Rao, not Savage.

## Not re-opened this session
Goh 2025 (Nat Med, 92 physicians, +6.5) -- three evidence lines agree but the text was not on disk; attending/resident split conflicts (a22 says 46/46 arms; b04 says 67 attendings, 25 residents; these are different things, but not checked). Savage 2024 prompt-comparison numbers (three agreeing lines, same upstream). Kanjee 2023 (file empty). Tu AMIE exact top-k values (figure only). Automation bias paper (b24), Bedi review (b25), Semigran 2015 (c27, from memory), a27, a28.

## Contradictions and weak spots
- Goh 2024 vs McDuff vs Goh 2025: LLM access helped little, much, and moderately. Explanations (not tested): different tasks (6 vignettes vs 302 CPCs vs management), tool interface, physicians not trained to prompt, short time limit. Nobody ran these factors in one design.
- "LLM alone beats physicians" rests on LLM runs scored by graders who know the format; Goh 2024 LLM-alone arm was 3 runs by the authors, not a blinded arm.
- Landmark o1 vs physicians (P=.055) and 6 vignettes: underpowered. Superhuman claim is real for CPC and R-IDEA, not for landmark.
- All strong results use written cases. Bean is the only study with lay humans; Hager is the only one on real hospital records (MIMIC), with open models, so it does not speak to current frontier models.
- Comparators differ: Nori generalists were barred from outside resources; McDuff clinicians read cases in isolation. Physician baselines are probably lower than in practice.
- Cost and token counts are not matched across arms in most studies. Only Nori reports cost; none reports tokens per case, so "equal tokens" claims cannot be taken from the literature.
- Contamination: o1 pre/post cutoff difference is non-significant (P=.59), but CPC cases may still be memorized in part; absence of a drop is weak evidence.
- Takita pooled accuracy mixes many task types; heterogeneity is high.
- Failed or null replications: Goh 2024 null; Bean null for users; Savage prompt styles null for GPT-4. No direct replication of any headline result was found.

## GAPS
1. Does a scaffold with an explicit challenger step (like MAI-DxO) beat the same base model at equal tokens, not equal cost? No published study controls tokens.
2. How much of MAI-DxO's gain comes from the panel roles versus from simply sampling more and ensembling? Ablations by role are missing.
3. Does LLM accuracy drop when the agent must elicit the case (not receive it), for current frontier models? Hager used open 2023 models; Bean's loss was on the human side. A frontier-model test with a simulated, lossy patient is needed.
4. Which part of the human-plus-LLM failure (Goh 2024, Bean) is due to the output format and prompting rather than the model? Does a structured, short, ranked output reduce it?
5. Is the top-1 vs top-10 gap (29% vs 59% on CPC) closed by a rerank or discrimination stage, and at what token cost?
6. Do reasoning models (o1/o3, R1) lose accuracy on post-cutoff, real-record cases compared with published CPCs? Contamination is not ruled out.
7. How well does a model know when it is wrong on diagnosis (calibration, 1.2% of studies measured it)? Does confidence predict top-1 correctness on CPC cases?
8. Does automation-bias exposure (flawed advice, -14 points) have an agent analogue, where a wrong early hypothesis in context anchors the final answer, and does a challenger step reduce it?
9. Are forced differential or Bayesian prompts harmful only for weaker models (GPT-3.5), or also for current ones? Only GPT-4-era data exist.
10. Has any study replicated Goh 2025's management-reasoning gain with a different physician population or a newer model?

## Gap search results (2026-11-01, evidence_d.jsonl d01-d22)

Search conditions: WebSearch quota ran out after one query. arXiv, Semantic Scholar and OpenAlex returned HTTP 429. Europe PMC and direct page fetches worked. So preprint-only work is under-covered. Abstract-only lines are marked opened:false.

Status key: closed = answered by evidence; partial = some evidence; open = nothing found.

1. Scaffold vs same model at equal tokens: OPEN for diagnosis. Re-reading Nori confirms no token control (inference cost $0.15 per case treated as negligible). Indirect: a token-matched study of 260 configurations (d03) found multi-agent help depends on the task, mean change -0.3%, and big losses on sequential tasks. Debate often fails to beat self-consistency (d04, abstract only). Added K25, K26.
2. Role ablation vs sampling: OPEN. Nori's ensemble (85.5% vs 81.9%) is several independent runs plus an aggregator, so it mixes the two. No per-role ablation exists in the paper or in anything found. K25.
3. Elicitation penalty for current models: PARTIAL, leaning yes. GPT-4o loses 28 points (MC) and 48 points (free response) on 218 text cases when the case becomes a conversation (d07). GPT-4 loses 25 points on iMedQA with initial info only (d06). Bean's simulated patients overestimate human performance and barely predict it (d09). Still missing: o3-class or Claude-class models on CPC cases with a lossy patient. Part of the loss is simulator limits (vignettes not written for dialogue). K22, K23, K24.
4. Is the human-plus-LLM failure due to format or prompting: OPEN. Input style did not predict score (d10). The meta-analysis shows imprecise pooled effects (d11). One simulation (d15, 13 physicians) saw top-3 gain but no top-1 gain with a short ranked output. No study varies output format. K31.
5. Rerank to close top-1 vs top-10: OPEN. Only direct test is a perplexity reranker, AUC 0.666, not reliable (d21; case reports, old generators). No LLM discriminator test on CPCs found. K15 note.
6. Reasoning models on post-cutoff real records: OPEN, slightly more context. Nori's 56 post-cutoff CPC cases scored at least as high as the 304 set (d02), which argues against memorisation inflation, but there is no clean pre/post number, and a 2026 study flags possible contamination in Gemini-2.5-Flash on unpublished prompts (d17). K18 note. Consider K18 "established" fragile: it rests on one o1 test (P=.59) plus indirect signals.
7. Calibration on diagnosis: PARTIAL. On multiple-choice items GPT-4o's confidence separates accuracy (83.2% at 5 vs 16.7% below 3) but most models say 5 always and none say "I don't know" (d19). Accuracy and calibration diverge between two current models (d20). Nothing on CPC top-1. K30.
8. Anchoring in agents and the challenger: PARTIAL. Prompt-planted bias hurts weak models a lot and GPT-4 little (d16, d08). Reasoning mode does not reliably protect, and debiasing prompts help (d17). Anchoring-failure rates on 54 emergency cases run 6.9-26.4% and most dangerous outputs are stochastic (d18). A challenger can also be a channel for a wrong persuasive argument (d05). No study plants a wrong early hypothesis in an agent and tests a challenger. K27, K28, K29.
9. Forced differential or Bayesian prompts on current models: OPEN. Only Savage (GPT-3.5, GPT-4) remains. Debiasing evidence (d17) is a different prompt type. K11 note, K32.
10. Replication of Goh 2025: OPEN. No same-design replication. AMIE management (21 PCPs, 100 scenarios) and a cardiology trial (9 cardiologists) are different designs (d13). Goh 2025 abstract confirms +6.5 (CI 2.7-10.2) and notes an erratum (d12). K04 note.

Corrections found:
- Qazi automation-bias CI: this pass gives -18.9 to -9.1; line b24 gave -19.7 to -8.3. Unresolved (abstract only both times).
- Bean control figure: the page shows 47.0% for conditions; 43.0% is the overall disposition rate, not a control-group condition rate.
- MediQ's +22.3% could not be reproduced from its Table 2.
- Nori ensemble note: cost $7,184 vs single o3 $7,850; budget variant $2,396 (the $2,397 in one section appears to be a rounding slip).

Next searches to retry when quota returns: pre/post-cutoff CPC tests; LLM rerank/verifier on CPC; Goh 2025 replication; forced-differential prompts on o3/Claude-class; a MAI-DxO open reproduction with drop-one-role.
