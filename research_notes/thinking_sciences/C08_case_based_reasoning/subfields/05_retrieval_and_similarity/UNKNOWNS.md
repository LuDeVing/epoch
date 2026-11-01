# Retrieval and similarity: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C08.05-U1 | Does k=1 nearest solved case beat a random solved case and no case for a frontier model on multi-step items? | A "show one nearest verified case after attempt 1" rule | memory, S3 | K03, K04, K13; direction older models only; no random arm in agent papers (critique gap 1) | none / random-1 / nearest-1 BM25; ARC and BrainTeaser items with a verified bank; pass rate, 5 seeds | nearest-1 beats random-1 by 3+ points and beats none by 2+, interval excludes 0 | High |
| C08.05-U2 | Does the agent copy a wrong stored solution from a near-duplicate? | Rule: retrieved solution must be re-checked by code before reuse; or drop retrieval for unverified cases | G2, G10, memory | K11 contested (Min vs Yoo), K12 and K25 (copying, agents); no frontier corrupted-label test | nearest-1 clean / nearest-1 with 30% corrupted solutions / none; same items; pass rate | corrupted arm falls 3+ points below none: add the re-check rule and verified-only storage as hard requirements | High |
| C08.05-U3 | Does an outcome (success-count) bonus on similarity beat plain similarity? | Success-weighted ranking from the class record | memory, S9 | K07, K17; trained retrievers only (EPR, UDR); light version untested; pruning needs 5 retrievals per case (K28) | similarity rank vs similarity + success bonus; bank of 50+ cases, 5+ retrievals each; pass rate | +1.5 points or more over similarity at equal tokens on 2 item types | High |
| C08.05-U4 | Which key finds the best case: raw text, LLM structure abstract, plan, outcome? | Index cases by a short LLM-written structure abstract | memory, S1, S9 | K19, K27; single source (Skill-KNN 78.3 vs 74.6, 2023 models); no plan or outcome key tested | four keys, k=1, same bank; count abstract-writing tokens; pass rate | best key beats raw text by 2+ points after counting its cost | High |
| C08.05-U5 | Is there a similarity threshold below which showing a case hurts? | A retrieval gate in S0: below tau, show no case | S0, memory | K09 (0-C collapse), K26 (QA gates only); no case-reuse gate measured | always retrieve vs retrieve if top score >= tau, sweep 5 values; accuracy against retrieval rate | some tau beats always-retrieve by 1+ point or cuts tokens 20% at equal accuracy | High |
| C08.05-U6 | Does a diverse or covering set beat top-k when no case is close? | MMR or cover set when top score is low | memory, S3 | K09, K10; established on compositional tasks, mixed on easy; old models | top-3 / MMR-3 / top-1, split by top-score level and difficulty; pass rate | MMR beats top-3 by 2+ points on the low-similarity half and loses by under 1 on the rest | Med |
| C08.05-U7 | Does ranking by estimated adaptation cost beat similarity with an LLM adapter? | Re-rank top-5 by LLM-judged edit effort | memory, O7 | K21, K24; classic symbolic test only (100% vs 70%, 12%) | similarity / adaptation-cost rank on top-5; count judge tokens; pass rate | beats similarity by 3+ points after judge tokens | Med |
| C08.05-U8 | What is the best k for our agent (1 or 4)? | A fixed k in the schema | memory | K13: Memento best 4, ReasoningBank best 1; case type differs; no variance reported | k in {0,1,2,4,8} at equal total tokens; pass rate | pick the smallest k within 1 point of the best | Med |
| C08.05-U9 | Does case order or position matter for 1-4 short cases in new models? | A fixed order rule (best case last) | memory | K29; old models only (50-85% swing); no 2025-26 test | same 4 cases, similarity order vs reverse; pass rate | gap over 2 points: add the order rule; under 1 point: ignore position | Low |
| C08.05-U10 | Does a self-generated analogue match a stored case? | Skip the bank for strong models; use a self-generated analogue (O7 source) | O7, memory | K30; davinci and GPT-3.5 era; K=1 was worst | stored-case-1 / self-generated-1 / self-generated-3 / none; tokens counted | self-generated within 1 point of stored at equal tokens | Med |
| C08.05-U11 | Does verified-only storage with pruning beat add-all as the bank grows to hundreds? | Verified-only plus prune-after-5-retrievals rule | memory, S9 | K02, K25, K28; Xiong (4 agents, single study); no tiny-bank curve | add-all / verified-only / verified+prune at bank size 10, 30, 100, 300; pass rate | verified-only beats add-all by 5+ points at 100+ cases | Med |
| C08.05-U12 | Do Weber and Richter style weighted-attribute scores beat one embedding? | Typed case fields with weights (task type, size, operator used) | memory | K21; classic works unread; CBR-RAG +1.94% unablated, 32 cases | one embedding vs weighted 3-field score with 3 weight sets; pass rate | weighted beats embedding by 2+ points on 2 item types | Low |
| C08.05-U13 | Is LLM-chosen retrieval better than embedding retrieval? | LLM picks among top-5 | memory | K22; the 20-28% agreement figure is unverified | embedding top-1 vs LLM picks from top-5; pass rate, judge tokens counted | LLM pick wins by 3+ points after tokens | Low |
| C08.05-U14 | Do random-looking extra cases help (Power of Noise)? | Nothing planned; only a warning if harm shows | memory | K18; contested; RAG only | none / 1 relevant / 1 relevant + 2 random; pass rate | do not add; if random cases help by 2+ points, investigate | Low |

## Open questions we cannot test on our bench yet

- **Weber, Richter and Bergmann local-global similarity.** The classic works are unread. Unblock: open Richter and Weber (2013) and find any paper with a per-attribute weight ablation measured on correctness.
- **Wilkerson and Leake 20-28 percent agreement.** Source not found in two searches. Unblock: locate the paper (ICCBR workshop likely) and read the table.
- **Learned retriever on our own data.** EPR-style training needs thousands of labelled items and many LM calls. Unblock: a larger logged bank from many bench runs.
- **Case-base growth curve over hundreds of cases with forgetting.** We have no long-running bank. Unblock: a multi-week run with logging of every shown case and outcome. Links to the Case-base maintenance and Retention policy subfields.
- **Position effects with long agent contexts.** Our cases are short. Unblock: a long-trajectory task where many cases accumulate.
- **Frontier-model replication of KATE and EPR numbers.** Most published numbers are from 2021-23 models. Unblock: budget to rerun a few public sets with our model.
- **Why the best k differs across papers** (Memento 4, ReasoningBank 1). Unblock: both papers' variance and case type, or our own T5 sweep.
- **Three items not opened:** the Huawei CBR paper (a28), Dr.ICL figures (a21), full Yoo et al. per-model values (d18).

## Order to run

1. **C08.05-U1 (random vs nearest vs none at k=1).** It is the main missing control, cheap (three arms, existing bench items), and every other retrieval test depends on its answer.
2. **C08.05-U2 (corrupted stored solutions).** It tells us whether retrieval is dangerous without verification, and it reuses the same bank and arms as U1.
3. **C08.05-U5 (similarity-threshold gate).** It runs on the U1 data (score every retrieval, then sweep tau) at almost no extra cost, and it decides when to skip retrieval.
