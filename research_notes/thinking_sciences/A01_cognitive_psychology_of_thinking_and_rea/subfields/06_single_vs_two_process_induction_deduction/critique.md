# Cross-check: single vs two-process accounts of induction and deduction

Checker pass over evidence_a, evidence_b, evidence_c (83 lines).

## Numbers re-opened and checked

Confirmed (source text read this session):
1. Heit and Rotello (2005) Exp 1: N=40 per cell, Warwick undergraduates. Deduction .89 correct, .22 incorrect; induction .93 / .55. d' 1.68 vs 0.93, t(78)=3.11; interaction F(1,78)=9.67; zROC slopes .84 vs .60. Confirmed.
2. Exp 2: correct .92 vs .88, incorrect .24 vs .57; d' 1.69 vs 0.78, t(94)=4.39; F(1,94)=19.22; slopes .82 vs .71. Confirmed. New detail: incorrect-typical .60 vs incorrect-atypical .53 under induction. Rips (2001) reported about 20% "valid" for incorrect arguments under deduction, a similar value.
3. Stephens, Matzke, Hayes (2019): nine papers, 16 datasets, 6 of 16 (37.5%) significant at assumed SD .10, none at .20 or .30. Confirmed.
4. Bertolazzi et al. (2026), Table 1: Qwen2.5-32B accuracy 81.62 (zero-shot) and 94.60 (CoT), CE 0.348 and 0.096; Qwen3-14B 86.54 and 96.70, CE 0.213 and 0.014. Confirmed.
5. Steering fix: scale 1.5, layers 43 and 26; accuracy 81.62 to 82.21 and CE 0.348 to 0.072; accuracy 86.54 to 96.70 and CE 0.213 to 0.043. Confirmed.
6. Regression beta .557 (p=.017), prompt-style beta .188 (p<.001), 57 data points. Confirmed.
7. Alignment does not differ by prompt style, Mann-Whitney p=.625. Confirmed.
8. Cosine range: text says 0.48 to 0.64; the Figure 2 caption says 0.53 to 0.64. CORRECTION: the paper contradicts itself; quote "0.48 to 0.64 (text) / 0.53 to 0.64 (caption)". Controls 0.10 to 0.13 and -0.12 to -0.17 confirmed.
9. Cheng et al. (2024): the values 0.697, 0.551, 0.462, 0.095, 0.710, 0.185 and Table 13 GPT-3.5 values 0.398, 0.196, 0.934 appear in the text. Row and column alignment is garbled in the extraction, so the mapping to base and condition is not verified. Partly confirmed.
10. Lassiter and Goodman: the sources behind the 10,185 judgments, d' 1.15 vs 0.63, and R2 figures could not be fetched (eScholarship PDF blocked). NOT re-verified. They still rest on one agent's read.

Other note: the Bertolazzi arXiv number (2510.06700) was right; the title in the agent notes shows 2026 (v3 dated 20 Apr 2026), and a29/c01 are the same paper counted twice. Do not count them as two sources.

## Contradictions between sources

- Trippas, Thompson, Handley (2017): a25 gives Exp 1 power for "45 participants" and Exp 2 conflict costs .68 vs .83; b19 gives N=43 and N=82 and different Exp 2 numbers (.21 vs .09). The text labels were noted as possibly swapped in b19. Treat N and cost figures as unverified.
- Rips crossover: b24 and a01 describe a crossover; a02 and b03 say it is closer to a single dissociation. Rips was never opened.
- a19 and b10 describe the same Stephens et al. (2018) abstract; the two agents did not open it. Counted once.
- Chain of thought: Bertolazzi finds CoT cuts content effect strongly; Poddar finds no paired change in zero-shot CoT across 14 models (McNemar p=.612). Different measures and models.
- Prompt helpfulness: Lampinen found few-shot gains small on syllogisms; Ranaldi found a two-stage prompt cuts CE but only to near 50.
- Alignment: Bertolazzi reads alignment as one shared signal; the same paper also finds steering can separate the two (a task-difference vector removes most content effect). One signal that can be partly subtracted is not a clean single process.

## Weak spots

- Human evidence leans on small samples and one item type: Heit and Rotello used 8 and 16 arguments; Hayes et al. used only causal conditionals.
- Equal-variance Gaussian assumptions drive the "two dimensions" result; the state-trace "one dimension" result rests on a null with unproven power for other two-process structures.
- Lassiter and Goodman's model has a free exponent per word, so its flexibility is not a strong test.
- LLM studies measure accuracy gaps, not ROC or d'. Poddar's own method ignores token probabilities as confidence ratings.
- Steering results: best layer and scale were picked on the same data; no held-out test seen.
- Most LLM work is open-weight and on small syllogism sets; the agent is not.

## Seen only in snippets or abstracts

Rips (2001); Heit and Rotello (2010); Rotello and Heit (2009); Stephens, Dunn, Hayes (2018, Psych Review); Singmann and Klauer (2011); Stephens et al. (2020); Dube et al. (2010); Howarth et al. (2016); Valentino et al. (2026); Cao et al. (2026, abstract and introduction only). Lassiter and Goodman: not verifiable here. Hayes et al. (2018) numbers were read by earlier agents; not re-opened (journal full text not freely available).

## GAPS

1. Does an LLM agent show a sensitivity gap (d') or only a criterion shift between "necessarily follows" and "plausibly follows" wording, when run on the same items with confidence ratings? No study has done it.
2. Is the state-trace plot for an LLM (accept rate under validity wording vs plausibility wording across belief, validity, length, premises) monotonic? This decides if one shared scale with two cutoffs is a valid design for the agent.
3. At equal tokens, does an explicit "assume premises true, ignore plausibility" step beat a plausibility-first answer on validity items, and what does it cost on plausibility items?
4. Does the criterion shift between wordings track base-rate beliefs (Stephens et al.'s manipulation)? If so, the agent could set its threshold from stated stakes. Not tested on LLMs.
5. Is the Heit-Rotello effect stable beyond causal conditionals and short categories, in longer multi-premise and real-world arguments with natural predicates?
6. When should the agent route a check to a solver or code rather than judge validity itself? Logic-LM lost to CoT on PrOntoQA; where is the crossover?
7. Does CoT reduce content effect on closed API models at equal total tokens (Bertolazzi says yes, Poddar says no)?
8. Is the Lassiter and Goodman one-scale modal-word model right? Could not be re-verified here; need a full-text read and a test on whether "necessary" and "plausible" answers share a rank order in the agent.
9. Does the dual-source mixing weight (form vs knowledge) vary by item type enough to set a per-item rule for when to check form?
10. Do premise-count and odd-premise effects (non-monotonicity failure in GPT-4) damage strength estimates in the agent's induction steps?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d18). Claims K03, K04, K12, K15, K18 and K19 were updated and K21 to K27 added. Web search quota ran out partway through, so searches on gaps 5 and 9 were cut short.

Closed or mostly closed:
- Gap 8 (Lassiter and Goodman): CLOSED as a verification. Full text read (d01, d02). Correction: 485 analysed of 507 recruited, 10,185 judgments. d' 1.15 vs 0.63 and the R2 values hold. Rank order across modal frames: mean Spearman .53, within the .49 to .64 the model plus noise predicts. R2 for necessary (.57) sits below its split-half ceiling (.70), so the model is not complete. The paper itself says it does not rule out a qualitative distinction. Still open: the same rank-order test on the agent.
- Gap 6 (solver versus own judgment): MOSTLY CLOSED for 2023 models (d04 to d08). Model reasoning wins or ties on short, synthetic, forward-chaining problems (PrOntoQA GPT-4 98.79 vs 83.20; FOLIO GPT-4 75.3 vs 72.5, p=.58). The solver wins as proof depth and premise count grow (ProofWriter +7.1 at depth 0 to +39.4 at depth 5; SatLM depth-5 99.7 vs 80.1). Cost is translation: GPT-4 executable-formula rate 79.9% FOLIO, 32.6% AR-LSAT. Not closed: no result for current reasoning models or at equal tokens.

Partly addressed:
- Gap 4 (base rates): human support only. Speeding and a base-rate experiment moved the two criteria in opposite directions (d03, second-hand; the 2018 Psych Review paper was still not opened). No LLM test. Temperature is not a clean criterion lever (d14), so prompt wording or stated stakes would be the lever to test. OPEN for LLMs.
- Gap 10 (premises): two weak-to-moderate sources (d12, d13). Premise count 2, 3, 4 cut LLaMA-3 8B zero-shot CoT from 44.64 to 39.64 to 31.79; GPT-4 fails non-monotonicity. Nothing on the agent's current model. OPEN.
- Gap 7 (CoT on closed models at equal tokens): the conflict is a difference of design (d09: Poddar's cue was 'think step by step' with a one-word answer; Bertolazzi used open Qwen models with a different measure). No equal-token, closed-model study found. OPEN.
- Gap 1 (d' versus criterion in LLMs): no study found (d18). Useful side facts: large model-to-model criterion differences (d09: precision 99.2% recall 42.8% vs precision 61.0% recall 93.1%), global yes-bias that must be removed first (d11), and unequal-variance evidence that breaks equal-variance d' (d14). OPEN, now with method warnings: use d_a or AUC, remove yes-bias, use wording and not temperature as the lever.

Not advanced:
- Gap 2 (state-trace plot for an LLM): no LLM data. d03 supplies the method (monotone points across many conditions, measurement-error model). Needs 12 to 24 conditions (belief x validity x length x premises). OPEN.
- Gap 3 (explicit 'assume premises true' step at equal tokens): no token-matched study. Nearest: two-stage form-first prompt (c10), few-shot with a 'nothing follows' example (d15, GPT-4 'Neither' 44.44% to 94.44%), CoT null (d09). OPEN.
- Gap 5 (Heit-Rotello beyond short arguments): not advanced; search hit the quota. Only the earlier a11 summary (length and similarity move induction more) and d01 (natural predicates raised invalid acceptance to .82 and lowered d' in both wordings) bear on it. OPEN.
- Gap 9 (mixing weight by item type): not advanced. OPEN.

Corrections from this pass:
- K03 N was given as 507; analysed N is 485.
- Critique item 10 (Lassiter and Goodman not re-verified) is now resolved by d01 and d02.
- The Stephens, Dunn & Hayes (2018) paper and Rips (2001) remain unopened; their base-rate and crossover details rest on Hayes et al. (2018).

Suggested minimal experiment on the agent (closes gaps 1, 2, 4 at once): 48 items crossed validity x believability x premise count (1, 2, 4), each judged under 'necessarily follows' and 'plausibly follows' wording, five samples each, plus a 1 to 6 confidence rating. Add a base-rate cue (20% vs 80% valid) as a third arm. Report accept rates by cell, d_a and z-ROC slope per wording, Spearman across wordings with a split-half ceiling, and the state-trace plot with a monotone fit.
