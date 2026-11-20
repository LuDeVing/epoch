# A10.04 Deliberate practice: cross-check critique

Checked 2026-11-19. Sources re-opened this session: Ericsson, Krampe, Tesch-Romer 1993 (full PDF text), Macnamara and Maitra 2019 (PMC full text), Huang et al. 2024 (arXiv PDF), DAPO, Voyager, Absolute Zero (arXiv PDFs), Macnamara 2014 abstract (Europe PMC).

## Corrections made (10 numbers re-checked)
1. a03 CONFIRMED: 7,410 h vs 5,301 h, F(1,27)=4.59, p<.05; best+good vs teachers 3,420 h, F(1,27)=11.86, p<.01. Middle-aged pros 7,336 h confirmed.
2. a04 CONFIRMED: practice alone 24.3 h (two best groups) vs 9.3 h teachers, F(1,27)=44.05. Note 24.3 is the pooled best+good mean, not "best". Total music time 50.6 h; mean practice alone across all groups 19.3 h; sleep mean 58.2 h.
3. a02 CONFIRMED: 10 of 14 nominated; N=30 plus mid-aged group.
4. a22 CORRECTED: replication groups were n=13 / 13 / 13 (N=39), not "less accomplished n=25"; the 25 was a comparison df. Best 8,224 h [6400, 10048]; good 9,844 [6937, 12751]; less 4,558 [3264, 5851]; chi2(2)=13.90, eta2=.26; 82% power for eta2=.23. All other figures confirmed. Note the good group had MORE hours than the best group (nonsignificant). b01 (n=13 each) is the right one.
5. a23 CONFIRMED: 6,251 vs 6,821 h, t(24)=-0.37, p=.717, eta2=.23.
6. c13 CORRECTED (real error): Huang et al. Table 2 oracle results are GPT-3.5 GSM8K 75.9 to 84.3, CommonsenseQA 75.8 to 89.7, HotpotQA 26.0 to 29.0; GPT-4 GSM8K 95.5 to 97.5, CSQA 82.0 to 85.5, HotpotQA 49.0 to 59.0. The evidence line wrongly gave "GPT-3.5 75.9 to 95.5" and "26.0 to 49.0"; 95.5 and 49.0 are GPT-4 standard-prompting scores. Claim K17 uses the corrected values. Intrinsic numbers (38.1, 41.8, 91.5, 89.0) confirmed; c25 numbers confirmed.
7. c04 CONFIRMED: DAPO 50 on AIME 2024 vs 47, 50% of steps, naive GRPO 30.
8. c08 and c22 CONFIRMED: random curriculum -93% items, no self-verification -73%.
9. c01 PARTLY CONFIRMED: AZR beats prior models by 1.8 average points; math gains +10.9 (Base-7B) and +15.2 (Coder-7B); +10.2 and +13.2 for larger sizes. The 0.3-on-coding and +5.7 (3B) were not separately located.
10. a20 CORRECTED: the line says "about 61% of variance" after attenuation correction. Corrected r=.61 is 36-37% of variance (b10 is right: 36%). The 61% is the correlation, not variance.

## Unresolved discrepancies
- Macnamara 2014 overall: a11 gives r=.35, 12% (original). b06 (Hambrick 2020 table) gives r=.38, 14.4%. A 2018 Psychological Science corrigendum to the paper exists (Europe PMC 29733772, text paywalled, 403). The corrected figure is probably .38, but this was not read. Domain figures (26/21/18/4/<1%) are the abstract's and may also have moved. Treat "12-14%" as the range.
- Macnamara 2016 sports: a18 r=.43 (18%), b06 r=.45 (20.3%), b15 abstract 18%. Same unexplained gap as above (possibly a later corrigendum or Hambrick's re-computation).
- Ericsson and Harwell 2019 selected effects: a20 r=.54, k not stated; b06 r=.56, k=8; b10 sample-weighted domain r values for k=14 effects (5+3+5+1). Raw .54 vs .56 and k=8 vs 14 are not reconciled.
- Platz 2014: a16 reports 13 studies, b06 reports k=14 effects; likely studies vs effects.

## Contradictions between sources
- Raw r about .35-.43 vs corrected .61: both authors' camps use the same data and differ on definition (b12) and on assumed reliability (b07).
- Elite-level r=.11 (a18) vs E&H range-restriction argument (b11): no test exists.
- Replication (a22) vs the 1993 "complete correspondence" claim: partly fails (best vs good) and partly holds (experts vs less accomplished).

## Weak spots
- Almost all human evidence is correlational and retrospective; reliability of recall is assumed, not measured.
- The people who coded the meta-analyses are the two rival camps; both tables are from the authors with a stake.
- LLM studies do not test deliberate practice. They test training curricula and feedback, which is analogy. a25 has "Deliberate Practice" in its name only.
- No LLM study was found that tests inference-time scaffold "practice" (the agent does not learn between tasks), so schema relevance is low (background).

## Only seen in snippets or abstracts
a28 (paywalled), b05, b14, b15, b16, b17, b20, b21, b22 (abstract only); c18, c19, c20 (from memory or not opened); c05 curriculum effect read as curves only; c23 table partly garbled.

## GAPS (most decision-relevant first)
1. Does any controlled study show that an LLM agent improves at inference time from within-session repeated attempts with graded difficulty and external feedback, at equal tokens, without weight updates?
2. How much of the gain from difficulty-filtered RL (K14) comes from choosing mid-pass-rate items versus simply more rollouts or a verifier, given the ablation shares in DAPO and SPEED-RL are shown only in figures?
3. Is there a published inference-time analogue (self-built curricula in context, skill libraries) with an ablation of ordering, beyond Voyager's Minecraft setting?
4. What is the correct post-corrigendum Macnamara 2014 overall effect and domain split (r=.35 vs .38)?
5. What reliability do retrospective practice estimates really have over long intervals, measured directly (not assumed .6-.9)?
6. Does range restriction explain the elite r=.11, tested with a correction on elite-only samples?
7. Are there further independent replications of the 1993 violin study or of the pianist/other-domain claims beyond Macnamara and Maitra (2019)?
8. When LLM tutors give practice feedback, does the gain survive blinded, non-optimised outcome measures (Fazlollahi's OSATS result was not significant)?
9. Does process-level (step) feedback beat outcome feedback outside math, and at what labelling cost?
10. What do open-ended-task agents show about "predictability" moderating gains from practice-like loops, as Macnamara's predictability split (r .49 vs .21) predicts?

## Gap search results (2026-11-19, evidence_d.jsonl d01-d17)
WebSearch budget ran out after 2 calls; the rest came from PMC, Europe PMC and arXiv PDFs.

1. CLOSED for same-task repeats, OPEN for equal tokens. EvoTest (d13, d14): static agent flat (AUC 0.11), Reflexion 0.32, EvoTest 0.47, no weights updated, 50 episodes. Reflexion (d10): +22 pts AlfWorld in 12 steps. No paper matches tokens against best-of-N. Gains need a real external signal and a strong model (d11, d09).
2. PARTLY CLOSED. SPEED-RL (d06, d07): 2-6x faster to target, screening cost counted, total rollouts per prompt fixed, same rule-based reward, so not a verifier or rollout-count artefact. Still no matched random-subset ablation in text; figures not inspected. DAPO share unchanged.
3. CLOSED, answer negative. Evo-Memory (d16): hard-to-easy beat easy-to-hard (ReMem avg 0.81 vs 0.77; ExpRAG 0.69 vs 0.57). Dynamic Cheatsheet only speculates about easy-first (d09). Voyager claim K17 now "contested". Similarity of tasks matters more (Pearson .717/.563).
4. CLOSED. Post-corrigendum overall r=.38, 14%; domains 24/23/20/5/1 (d01). Corrigendum text itself unread (d05, paywall). The 2016 sports gap (.43 vs .45) remains unexplained.
5. STAYS OPEN. Recall reliability is measured only for recent weeks/years (r .60-.75, de Bruin r(34)=.60; Ward 2007 older years not significant). Nobody has full-career diaries; Ericsson and Harwell adopt 0.6 by guess, Macnamara used 0.8 (d02, d03).
6. STAYS OPEN. No elite-only range-restriction correction exists (d04).
7. STAYS OPEN. No independent replication of the 1993 violin study beyond Macnamara and Maitra 2019 was found; the search budget was too small to say none exists.
8. NOT SEARCHED (no budget). Fazlollahi blinded-outcome question unchanged.
9. NOT SEARCHED. Step vs outcome feedback outside math unchanged (K19 single-source).
10. PARTLY. Predictability moderation has indirect support: gains were strongest where tasks share structure (Dynamic Cheatsheet Game of 24; Evo-Memory similarity r .717) and absent in GPT-4o MMLU-Pro Engineering (53.2 to 51.2). No study tests predictability directly.

Other corrections: Dynamic Cheatsheet's memory gain over its own instructions-only control is much smaller than the headline (Claude AIME 2024 36.7 to 50.0, not 23.3 to 50.0) (K29). Claims K23-K29 added; K01, K02, K04, K15 got evidence ids; K17 status changed to contested.
