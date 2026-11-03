# D04.03 Fallacy theory: cross-check critique

Files checked: evidence_a.jsonl (30 lines), evidence_b.jsonl (27), evidence_c.jsonl (26). Claims: claims.jsonl (23 claims, K01-K23).

## 1. Numbers re-opened this session (full PDF text via pdftotext)

| Source | Numbers checked | Result |
|---|---|---|
| Jin et al. 2022 (arXiv 2202.13758) | 2,449 LOGIC items, 1,079 LOGICCLIMATE, 8.62-53.31 range, Electra 53.31, StructAware 58.77, random 12.02, GPT-2 13.67, RoBERTa-MNLI 12.22, exact match 47.67% (+12.01) | Confirmed |
| Jin et al. 2022, GPT-3 row | a14/b01 say 12.20 F1; c01 says 12.00 | CORRECTION: table shows F1 12.20 with precision and recall 12.00. Use 12.20 F1. c01 misread the column. |
| Payandeh et al. 2023 (arXiv 2308.09853) | 41% and 69% more likely; 37% vs 29% (GPT-3.5); 67% vs 37% (GPT-4); 56% vs 37% across all three runs; helper ablation 17.66/10.5 and 28/0.83; 20.25% GPT-4 | Confirmed |
| Helwe et al. 2024 MAFALDA (arXiv 2311.09761) | 9,545 texts, 200 annotated, 260 instances, 28% multi-label, GPT-3.5 0.627/0.201/0.138, random 0.435/0.061/0.010, humans 0.749/0.352/0.186 | Confirmed |
| Habernal et al. 2018 (arXiv 1802.06613) | 0.2% ad hominem in CMV, 19.5% news, 3,866 args, 3,396 threads, 48.6%, kappa 0.79, upper bound 0.878, controversy 0.804, CNN-LDA 0.569 | Confirmed |
| Pan et al. 2024 (arXiv 2410.15050) | GPT-4 78.94 (Argotario) and 79.10 (Reddit); T5-3B 83.20; T5-large 80.42; MAFALDA 48.38 / 49.78; 83.7%; failure rates 12.27 (warm-up) vs 15.09 (zero-shot CoT) | Confirmed. Note: the 12.27/15.09 are failure rates for the warm-up and CoT schemes, not for "with vs without definitions". |

About 45 individual figures checked in 5 papers. One correction. Not re-opened (rate limits on Semantic Scholar and OpenAlex blocked lookups): Li et al. 2024 LFUD, Lei and Huang 2024, Jeong et al. 2025, Bayindir et al. 2005, ISSA 2002 report, Nahar 2026, Chen 2026, Shen 2026 LoFa, Big-Big-SycoBench, Talk2AI. These rest on the earlier agents' reading.

## 2. Contradictions and near-contradictions between sources

- Li et al. LFUD: a19 reports Reclor +4.78% (Vicuna-13B 54.40 to 57.00), b22 reports Reclor +6.36% (LLaMA2-13B, 47.20 to 50.20, matches c14). Different models, not a conflict. Keep the model name with each figure.
- Prompt aids disagree across studies and models: definitions or rules hurt GPT-3.5 and GPT-4o in Bytyqi and Hautli-Janisz (b11) but CoT lifted GPT-4o from 0.13 to 0.86; Jeong et al. show big gains for gpt-3.5 and loss for gpt-4 on Covid-19. Pan et al. say few-shot helps only GPT-4. No stable recipe (K11 contested).
- Theory-based taxonomies (pragma-dialectics, periodic table) do not beat the base prompt (c17), while Bytyqi shows pragma-dialectic rules can matter in some models. Contested (K18).
- GPT-4 vs fine-tuned T5: close on Argotario and Reddit (Pan) but far lower on MAFALDA and LOGIC. Not a contradiction, a dataset effect.
- Macro-F1 on the same MAFALDA data differs by paper (Helwe span-F1 0.138 level 2 for GPT-3.5; Pan 31.27 macro-F1 for GPT-3.5). Metrics are not comparable; avoid mixing them.

## 3. Weak spots

- Theory side (a01-a05) is read through the Stanford Encyclopedia of Philosophy, not through Hamblin 1970, Walton 1995 or van Eemeren and Grootendorst. No primary book was opened.
- No pre-2020 human study except the ISSA 2002 report and Bayindir 2005. Classic experiments (Harris, Hsu and Madsen 2012; Hahn and Oaksford 2007; the 2021 "Do informal reasoning fallacies shape decisions" paper) are listed in b25-b27 with opened:false and "Not verified". They support no claim here.
- Many 2026 LLM studies are single-source and often single-group. Several include closed-model results from API tests in 2025, which cannot be reproduced exactly. They sit as single-source in claims.
- Dataset label quality is a major caveat (K07). A "low F1" can mean the labels are ambiguous, not that the model is bad.
- Almost every LLM study measures classification of a text given to the model. Few measure what we need: does flagging an authority claim or guess in a marked block (S1) change the final answer quality at equal tokens? Nothing in the evidence tests that directly.
- Payandeh's debater setup is a single design with 200 claims; effect sizes have no confidence intervals.
- Training-based results (LFUD, LOGIC data) are outside our no-training scope.
- Independent-source counts: where one lab produced several of the cited papers (Oaksford and Hahn; Pan et al.; Jin and Sourati sharing LOGIC), I counted them as one source.

## 4. Seen only in snippets or summaries

SEP summaries for a01-a05 (the entry text was read, but not the cited books). Hahn and Oaksford 2007, Harris et al. 2012, and the 2021 decisions paper (b25-b27) were not opened at all.

## GAPS

1. Does marking an appeal to authority or a stated guess in a separate S1 block change final answer accuracy on reasoning tasks at equal tokens (no direct test exists in the evidence)?
2. What false-positive rate does an LLM fallacy check have on sound arguments that look like fallacies (sound appeal to authority, sound slippery slope), and does a dialogue-type tag lower it?
3. Is the weakness against appeal to authority and fabricated authority cues (LoFa) reproducible on current models (2026 releases), and does CoT hurt there (-1.87%) or not?
4. Do the Hamblin/Walton critical questions for each argumentation scheme, used as a checklist, beat a plain "find the fallacy" prompt at equal tokens? Walton's own scheme-and-question work was not opened.
5. How much of the poor fine-grained labelling (MAFALDA level 2) is label ambiguity vs model weakness? Are there studies measuring model-human agreement vs human-human agreement on the same items?
6. What are the primary human numbers for Hahn and Oaksford 2007 and Harris, Hsu and Madsen 2012 (Bayesian reading of ad ignorantiam, ad populum, slippery slope), and do they replicate?
7. Does neutralising loaded wording before checking (Chen 2026: F1 down 14.5%) recover the lost accuracy, and does it cost more tokens than it saves?
8. Do LLM agents produce fallacious steps in their own chain of thought at a measurable rate, and does a self-audit pass catch them (Talk2AI measured 14.5% of LLM texts in dialogue, not in reasoning chains)?
9. Do multi-round fallacy checks (Pan: +1.27 to +7.54 macro-F1) hold up when token cost is matched against single-round self-consistency?
10. Is there any replication of the Payandeh finding (GPT-4 convinced 67% by fallacious vs 37% by logical arguments) by an independent group or with newer models?


## Gap search results

Search budget: 1 WebSearch used (the shared budget then ran out); arXiv, Semantic Scholar and OpenAlex APIs returned rate-limit errors (HTTP 429). Evidence came from full PDFs opened through arxiv.org/pdf (pdftotext) and two publisher fetches. New evidence: evidence_d.jsonl (d01-d18; 17 opened, 1 not opened). New claims K24-K29; K02, K14, K16, K17, K21 updated.

1. Gap 1 (S1 marking changes accuracy at equal tokens): STILL OPEN. No direct test found. Nearest: the CQoT gate (d01, d02) gives about +5% judge score, about half of it from the added structure, with no token match.
2. Gap 2 (false positives on sound look-alikes; dialogue-type tag): FIRST HALF CLOSED, SECOND HALF OPEN. Singh et al. 2026 (d05-d08): sound scheme-matched arguments flagged 58.9% vs 16.6% native (fine-tuned); zero-shot Sonnet 5, Haiku 4.5 and Qwen3.6-27B also track the scheme, and a binary prompt reduces it. No study tests a dialogue-type tag. K26 and K27 added.
3. Gap 3 (LoFa on 2026 models; CoT -1.87%): PARTLY OPEN. LoFa tested no 2026 model (API calls May-July 2025; GPT-4 authority LFR@3 39.20%). The -1.87% is one GPT-4/NQ1 comparison and means no benefit rather than proven harm (d10, d11). Big-Big-SycoBench (d09) shows 2026 models range from 0.2% to 95% compliance with invalid pressure but does not split out authority.
4. Gap 4 (critical-question checklist vs plain prompt at equal tokens): STILL OPEN, with partial evidence. CQoT uses generic Toulmin questions, not Walton schemes, and is not token-matched (d01, d02). GPT-4 answering Walton critical questions says yes to 53.3% of true-no questions (d03). Walton's own books were not opened.
5. Gap 5 (label ambiguity vs model weakness): PARTLY CLOSED. Agreement is low where it matters (d15: kappa 0.74 overall, 0.50 on the scheme-matched valid class; 12 of 237 CoCoLoFa comments fallacy-like but valid). No same-item model-human vs human-human comparison exists (d14).
6. Gap 6 (Hahn and Oaksford 2007; Harris et al. 2012): STILL OPEN. Both paywalled (d18, opened:false). K04 stays single-source.
7. Gap 7 (neutralising loaded wording): STILL OPEN, and a premise was wrong. The 14.5% drop is for human annotators, not LLMs (d13). K17 corrected. No token-cost data.
8. Gap 8 (fallacious steps in own CoT; self-audit): STILL OPEN. Talk2AI's 14.5% comes from a DistilBERT classifier on chat replies, not reasoning chains (d16), and that classifier type over-flags (d06).
9. Gap 9 (multi-round vs token-matched self-consistency): STILL OPEN. Pan et al. report no token counts or self-consistency baseline (d17).
10. Gap 10 (independent replication of Payandeh 67% vs 37%): STILL OPEN. LoFa is a related design inspired by LOGICOM, with no logical-argument control (d12). K14 stays single-source.

Correction to earlier work: K17 said LLM detection; the study measured human detection.
