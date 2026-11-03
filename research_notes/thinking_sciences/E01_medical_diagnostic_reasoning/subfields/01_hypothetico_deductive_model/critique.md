# E01.01 Hypothetico-deductive model: cross-check critique

## 1. Numbers re-opened this session (10 checked)

Re-opened with arXiv PDFs (pdftotext), arXiv abstract API and PubMed abstracts.

| # | Number | Source reopened | Result |
|---|---|---|---|
| 1 | MAI-DxO ~80% accuracy, 20% generalists, -20% cost vs physicians, -70% vs o3, 85.5% max (b01, c19) | Nori 2025 arXiv 2506.22405 abstract | Confirmed. Budgeted 79.9% at $2,396 vs physicians $2,963 gives -19%; vs o3 $7,850 gives -69%. Evidence says $2,396 (b01) and $2,397 (c19): rounding, not an error. |
| 2 | GPT-3.5: CoT 46, intuitive 48, analytic 40, DDx 38 (-8, P<0.001), Bayesian 42 | Savage arXiv 2308.06834 text | Confirmed (DDx 38%, CI -13 to -4.5). |
| 3 | GPT-4: CoT 76, DDx 78 (+2.2, CI -1.4 to +5.8, P=0.24), Bayesian 72 (-3.4, P=0.07) | same | Confirmed. |
| 4 | McDuff: LLM top-10 59.1 vs clinicians 33.6 (p=0.04); assisted 51.7 vs 36.1 (McNemar 45.7) vs search 44.4 (p=0.03) | McDuff arXiv 2312.00164 text | Confirmed. Correction: the paper's own table shows 51.8% for the full set while the text says 51.7%; keep both. |
| 5 | Brodeur o1-preview: 78.3% in differential (CI 70.7-84.8), first 52%, 88.6 vs 72.9 (p=.015), test 87.5%, R-IDEA 78/80 | Brodeur arXiv 2412.10849 text | Confirmed. |
| 6 | Goh RCT: 76% vs 74%, adj diff 2 (CI -4 to 8, P=.60), 50 physicians, LLM alone +16 | PubMed abstract PMC11519755 | Confirmed. Correction: time difference P=.20 in the abstract; c07 gives ".15 to .20", use .20. |
| 7 | Norman 2014: 44.5 vs 45.0%, 69 vs 89 s, +17 s on wrong cases, n=96 and 108 | PubMed 24362377 | Confirmed (b14 was marked opened:false; now verified). |
| 8 | Monteiro 2015: 47 residents, 12/19, 9/11, 8/17, 8% revised, 1.20 to 1.22 (t=2.15, p=0.03) | PubMed 26173528 | Confirmed. |
| 9 | Kanjee 2023: 45/70 (64%) in list, 27/70 (39%) first | PubMed record is a research letter without numbers | NOT re-verified this session. Keep as single read of c04. |
| 10 | Bass 2013: nephrologists 31.1 to 65.6% | OpenAlex and PubMed searches returned wrong papers | NOT re-verified. b10 stays opened:true from the original agent; treat with caution. |

Not re-opened (secondhand or abstract only): Elstein 1978 book, Sprafka 1973, Joseph and Patel 1990, Coderre 2003, Ark 2007, Kulatunga-Moruzi 2001, Sibbald 2013, Hager 2024 tables, LA-CDM/LDTL tables, INTERNIST-I counts.

## 2. Contradictions between sources

- **Do experts generate more hypotheses?** The review line (Elstein and Schwarz, a03; task note) says no. Arocha and Patel (a10) report 1.5, 3, 3.4 and 5 early hypotheses by training level. The studies count different things (cases, groups of 4 students, one resident) and a10 does not measure quality. Left as contested (K04).
- **Hypothetico-deductive vs pattern recognition.** Coderre 2003 (b11) says the pure form does worse; Bass 2013 (b10) says forcing analysis of the initial impression helps even experts. Strategy coding in b11 is post hoc.
- **Prompting vs orchestration.** Savage (b05, b06) finds no gain from a differential-diagnosis prompt; Nori (b01) finds gains from a multi-role orchestrator. They differ in task (MedQA single turn vs sequential), model, and tokens/cost, so they do not contradict directly, but no study isolates the role structure.
- **Hypothesis-driven vs random tests.** LA-CDM (81.3) beats prompted ReAct (74.9) in c13, yet a random planner (84.8) beats both in c14. Same benchmark, different authors; c14 uses a Llama-3-8B backbone, c13 trained models. Hypothesis-driven structure alone is not a clear win.
- **LLM alone vs LLM-aided physicians.** McDuff (b07) shows physician lists improve with LLM help; Goh (b09) shows no gain in reasoning scores (CI -4 to 8). Different metric (top-10 list vs graded reasoning score), different tool access.
- **Brodeur c06 contamination check:** 79.8 vs 73.5 (p=0.59) before vs after cutoff is non-significant, so it neither proves nor rules out leakage.

## 3. Weak spots

- The founding source (Elstein, Shulman, Sprafka 1978) was never opened. All founding numbers are secondhand. No exact counts for "average 5 hypotheses within 5 minutes" style claims were verified.
- Human sample sizes are tiny (N=13, N=15, N=15 nephrology, N=30 via snippet). Several analyses are uncorrected exploratory tests.
- Key LLM claim (Nori) is one company paper, with no role ablation and a gatekeeper LLM that can leak cues; physicians were restricted from outside resources.
- a25, b05, c08 are one study entered three times; a29-a32, b01-b04, c19-c20 are one paper. Independent source counts in claims.jsonl count papers, not evidence lines.
- Several newer (2026) LLM studies (c13-c15, b22) were only read from text with garbled table alignment per the evidence notes.
- Almost no study tests the specific Elstein claim (few early hypotheses guide search) with an LLM at equal tokens.

## 4. Seen only in snippets or abstracts

Sprafka 1973 (a23, search snippet); Coderre 2003, Ark 2007, Kulatunga-Moruzi 2001, Norman 2017 and 2005 (abstracts); Joseph and Patel 1990 (abstract and secondhand through a14); Sibbald 2013 (abstract); Kanjee 2023 and Bass 2013 (not re-verified).

## GAPS

1. Does forcing an LLM to name 3-5 hypotheses before asking for data beat plain chain of thought at equal tokens on sequential diagnosis (no study isolates this; Nori confounds it with roles and cost steering)?
2. Which MAI-DxO role (hypothesis tracker, challenger, cost steward, checklist) carries the gain? Needs an ablation at matched cost.
3. Optimal number of early hypotheses for an LLM: is accuracy flat, peaked, or rising in the number requested (Sprafka 1973 found no effect; needs the primary source and an LLM replication)?
4. Is the human finding that experts gain from analysing the initial impression (Bass 2013) real? Needs the primary paper opened and a control without the priming step.
5. Why does a random test planner beat hypothesis-driven LLM agents on MIMIC-CDM? Does it hold on harder, more diseases and on current reasoning models?
6. What are the exact numbers in Elstein, Shulman, Sprafka 1978 (hypothesis count, timing, accuracy by group) and what did Barrows 1978 and Neufeld 1981 replicate or fail to replicate?
7. Does content knowledge (retrieval of disease scripts) explain more LLM accuracy than loop structure? Test by crossing scaffold on/off with knowledge retrieval on/off.
8. Is anchoring in LLMs reduced by an explicit disconfirmation step at equal tokens, on unpublished bias prompts (b22 shows contamination risk)?
9. When should the loop be skipped (easy cases, pattern recognition) and can an LLM reliably detect that case difficulty from its own confidence?
10. Does verification of the final answer against the hypothesis list (Bass, Sibbald, Monteiro) yield a net gain for LLMs, or do second looks mostly flip correct answers (Monteiro: 8% revised, tiny gain)?

## Gap search results

Evidence in evidence_d.jsonl (d01-d16). arXiv, Semantic Scholar and OpenAlex APIs were rate-limited (429) during this run; PubMed, Europe PMC and arXiv search pages worked. Only 3 WebSearch calls were used before the shared budget ran out.

| Gap | Status | What was found |
|---|---|---|
| 1 Hypothesis list vs CoT at equal tokens | OPEN | No study found that isolates it. VivaBench (d15) shows the loss is in the gather-and-revise loop but has no scaffold arm. |
| 2 Which MAI-DxO role | OPEN (confirmed untested) | Nori full text: variants change budget, ensembling and question-only mode, not roles. Only ablation is single vs batched (83.9% both). ClinicalAgents (d12) ablates memory vs backtracking orchestrator, not Nori's roles. |
| 3 Optimal number of hypotheses | PARTLY CLOSED for LLMs, OPEN for humans | MedKGI (d11): accuracy peaks at 5 candidates in one 8B pipeline. Sprafka 1973 primary text blocked by MSU repository (d08). |
| 4 Bass 2013 | CLOSED (as a weak result) | Abstract opened (d01): N=15, final 65.6% vs initial 31.1%, but no control that saw the extra data without the priming step; abstract p=0.07 vs a CI excluding 1. Treat as unproven. |
| 5 Random planner beats hypothesis-driven agents | OPEN, now with a counterexample | MedKGI (d11): random question selection 31.1% vs information gain 69.8%. So the c14 result depends on setup. No test on current reasoning models found. |
| 6 Elstein 1978 numbers; Barrows, Neufeld | PARTLY CLOSED | Replications found: Neufeld 1981 (d02, process constant across training, only hypothesis content tracks level), Barrows 1982 (d03, 37 physicians, 62 encounters, early multiple hypotheses, promptness and accuracy tied to outcome). Exact 1978 counts still not seen (d05 abstract only). |
| 7 Knowledge vs loop structure | PARTLY CLOSED | Both matter: MedKGI KG removal -25.5 points; ClinicalAgents memory and orchestrator each add a few points. No clean 2x2. New claim K20. |
| 8 Disconfirmation step vs anchoring | OPEN | Ke 2024 (d13): 0/80 to 71.3% but cases selected for initial failure, no equal-token control. |
| 9 When to skip the loop | PARTLY CLOSED | Handler 2026 (d14): models commit prematurely about 70% when information is missing, more on routine-looking cases (81%) than urgent (19%). Self-detection of difficulty is unreliable. |
| 10 Final verification net gain | OPEN | No LLM study found that tests it directly. VeriDx (d16) is an audit tool, not a gain measurement. Human data still Monteiro (8% revised). |

New claims: K20-K24. Statuses changed: none downgraded; K01, K02, K06, K09, K13, K17 gained evidence ids; K17 stays single-source (secondhand).
