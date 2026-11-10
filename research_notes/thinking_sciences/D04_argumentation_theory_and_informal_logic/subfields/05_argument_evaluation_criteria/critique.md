# Critique: Argument evaluation criteria (ARS), cross-check

Checked by re-opening the PDFs (all deleted afterwards): Stab and Gurevych 2017, Wachsmuth et al. 2017 (E17-1017), CASA (2401.05249), ConQRet (2412.05206), Henselmans et al. (2609.05088), LOGICOM (2308.09853), Romberg et al. (2502.14501), Ocampo et al. (2605.28313), Svedholm-Hakkinen et al. (Argumentation 2024), Debatable Intelligence (2506.05062).

## Numbers re-checked

Confirmed exactly: Stab and Gurevych 91.07%, alpha .7672/.7673, kappa .435 and .259 (a06); Wachsmuth 2017 score distributions 172/119/13, 25/155/124, 231/72/1 (a09); CASA alpha .77 overall and .14 on the 32% flagged cases, and the CASA F1 and human-check table (b04, b05, b06, c14); ConQRet Table 5 for GPT-4o listwise+SC and crowd (-.17 global sufficiency), GPT-3.5 pointwise -.40 to .64 (a22, c03); Henselmans 89.6%, 3,389 pairs, 352 disagreements, 18.2%, 67.8%, 51.1%, 46.9%, <0.5% relevance (c09, c10); LOGICOM 17/10 and 56/37, 16.13% and 20.25% (c23); Romberg 103 datasets, 24 non-aggregated (c20); Ocampo kappa .493, 7.75%, 13,952 pairs (a24, b15, c06); Svedholm-Hakkinen 1.30 vs 1.61, 90%, 63%, r=.62 (b18).

## Corrections and cautions

1. b14 says "about 100 papers and 24 datasets". The source reviews 98 papers that introduce 103 datasets; 24 of the 103 keep non-aggregated labels. Use 98 papers / 103 datasets / 24.
2. c20 says annotator information is reported for "only 8 datasets (text excerpt)". Not found in the text during this check. Treat as unverified.
3. c23 (LOGICOM): "41% and 69% more likely" is quoted from the paper, but it does not follow from the paper's own raw numbers (17 vs 10 is +70%; 56 vs 37 is +51%; 37 vs 29 is +28%; 67 vs 37 is +81%). The raw percentages are right; the relative figures are internally inconsistent in the source. The paper also uses two analyses (A1: 37/29 and 67/37; A2: 17/10 and 56/37), and a23-style summaries mix them. Quote the raw numbers with the analysis name.
4. c22 (Qwen size curve) was read off a figure and is approximate. Do not cite the per-size values; cite only "near random below about 7B".
5. c14 removal-of-intervention figure: the paper shows two versions (73.5 / 65.8 in one table, 74.5 / 62.5 in another, TULU vs Llama-2). Macro-F1 65.8 is for Llama-2; the claim is fine but the pair "73.4 to 65.8" is F1 to F1.
6. a22 vs b10: not a contradiction. Table 5 gives pooled GPT-4o listwise+SC (local sufficiency .57); Table 14 gives single runs (.37 to .55). Both are right for different conditions.

## Contradictions and weak spots

- Local sufficiency looks easy in one place and hard in another. Stab and Gurevych (essays, 2 labels) get alpha .77 and 91% agreement; Wachsmuth 2017 (debates, 3 levels) gets expert alpha around .27 and crowd .18. Difference is domain, scale and label granularity; CASA's .14 on contested items shows the first number is inflated by easy items.
- LLM self-consistency (.6 to .98) versus agreement with humans (.2 to .57) is a validity gap, not a contradiction.
- Chain-of-thought hurts in Ocampo (2026) and in Mirzakhmedova (PaLM 2 .97 to .63 with reasoning). This conflicts with the usual assumption that more reasoning helps verification. Two sources, same direction.
- Henselmans (2026, single study, two judges that are themselves LLMs): the failure pattern (sufficiency, not relevance) fits the human-corpus pattern in Wachsmuth 2017, but judge and subject models overlap (Claude judges Claude); self-preference is possible.
- Most "LLM as ARS judge" work scores agreement with humans on argument corpora. None measures whether the checklist improves the answer. This is the central hole (b27).
- Founding works (Johnson and Blair 1977/2006, Govier 2010) were never opened; ARS definitions come from SEP and from the NLP papers' citations. The informal-logic literature on ARS limits (conductive arguments, defeasibility, "sufficiency is not formalisable") is only in the SEP summary (a02, a03).
- Hoffmann and Catrambone (2023), Boudry et al. (2015), Wachsmuth 2024 position paper details: snippets or second-hand only (b22, a27, b24).
- Bayesian rival (Hahn and Oaksford) was seen only partially (a25, a26 opened; b23 not retrieved); no data on whether graded strength beats a checklist for LLMs.
- Only snippet or abstract: c26, b22, b24, b27 (gap statement), a04, a27, c27.

## GAPS

1. Does giving an LLM the ARS checklist (or CASA-style objection prompt, or Walton critical questions) as a verification step improve final answer accuracy or blind-judged quality on open-ended questions, compared with a generic "check your answer" step at equal tokens? No study found.
2. Which ARS move does the work: relevance, acceptability, or sufficiency? Evidence says sufficiency is where answers fail, but is a targeted sufficiency probe better than the full triad at equal cost?
3. Does the counterfactual-objection method (CASA) still help on frontier models, and on answers rather than short fallacy items? Only 7B models were tested.
4. How well does a frontier-model sufficiency judge agree with humans on hard items only (the .14 regime), and does self-consistency over 3 to 5 samples fix it?
5. Can a model judge acceptability of factual premises without retrieval, and does adding retrieval (ConQRet-style RAG metrics lifted alpha .184 to .395-.461) help for closed-book answers too?
6. Does chain-of-thought before the verdict hurt ARS judging on frontier models in 2026 (Ocampo and Mirzakhmedova show losses on older or open models)?
7. Are LLM judges biased toward their own or fluent answers on ARS dimensions (same-family judging, length, hedging)? Henselmans shows hedging marks low grounds; is that a real defect or a judge cue?
8. What do Johnson and Blair and Govier say about limits (sufficiency for conductive arguments, context-relative acceptability) that a checklist prompt would need to encode? Read the books or a faithful secondary source.
9. How does the checklist compare with probability-based strength ratings (Hahn and Oaksford) for calibrated confidence in the final answer?
10. Are models persuaded by fallacious supporting text inside the agent's own retrieved context (LOGICOM-style), and does an ARS check reduce this at equal tokens?

## Gap search results

Evidence in evidence_d.jsonl (d01 to d17); claims K25 to K35 added, K22 and K24 updated. Search was limited: the shared web search budget ran out after one useful query, and OpenAlex, Semantic Scholar and arXiv APIs returned rate-limit errors. "Not found" below means not found in this limited pass.

1. ARS or critical questions vs generic check on answers: STAYS OPEN, partly informed. Nearest: CQoT (d01) +4.6% reasoning and +5.4% math judge score, but Toulmin questions, GPT-4o judge, tokens not matched. STICK (d10) shows a concrete checklist beats free-form self-critique (LiveBench reasoning +7.8, GPT-4o +0.8; Self-Refine lost up to 25 points), but for instruction following. Generic self-check alone does not help or hurts (d03). Need the main experiment.
2. Which ARS move does the work: STAYS OPEN. Indirect: separate targeted probes with the draft hidden beat a joint check (d09, FACTSCORE 63.7 vs 60.8); relevance instruction helps modestly (d08). No ARS ablation found.
3. CASA on frontier models and full answers: OPEN, nothing new (d17).
4. Frontier sufficiency judge on hard items: OPEN. Only side evidence that checklists raise rater agreement modestly (d11, 0.194 to 0.256).
5. Acceptability without retrieval: PARTLY CLOSED for factual claims. Resampling agreement flags unsupported claims closed-book (d13, AUC-PR 93.42 vs 72.96 random, 20 samples); CoVe works closed-book (d09). Detects inconsistency only. Not tested on ARS premises.
6. CoT before verdict: STAYS OPEN, risk strengthened. CoT gains concentrate in math and symbolic tasks (d04); CoT lowered accuracy for frontier models on judgment-like tasks (d05, GPT-4o -23.1, o1-preview -36.3 on a subset). No direct 2026 ARS test.
7. Judge bias: PARTLY CLOSED. Self-preference and cue sensitivity are real (d06, d07). Hedging not tested; keep Henselmans's "hedge equals low grounds" as an unverified judge cue until a paired-rewrite test.
8. Limits of ARS: PARTLY CLOSED via SEP only (d14, d15, d16): audience-relative acceptability, graded undefined relevance and sufficiency, cumulative sufficiency for conductive arguments. Johnson and Blair and Govier books still unread.
9. Checklist vs probability ratings: OPEN. No LLM study; verbalised confidence is overconfident (d12, mostly 80 to 100%).
10. Fallacious context in retrieved text: OPEN beyond LOGICOM. Irrelevant context study (d08) gives the relevance half only; no ARS-check test.

Cautions on new lines: d03 and d10 tables were read from extracted text with scrambled layout, so row order is inferred; use the headline numbers. d02 numbers come from a fetch summary of the HTML. d05 is psychology-paradigm tasks, not argument tasks.
