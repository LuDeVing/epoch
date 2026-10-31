# Critique: A03.04 Framing (cross-check)

Confirmed from full text (D:/research_scratch/A03.04): T&K 1981 (N=152 72%; N=155 78%), Pinon (151 ES, d .437/.260/.444), Kuhberger (d .31/.52/.56/.60, h .612), Echterhoff (GPT-4 .375 vs .780; selfhelp .270 vs .280), Jones-Steinhardt (45.4/74.1), Payne (87.2/41.6; 85.6/88.8; math control no effect), FRAGILE (39.9/36.3/47.2 vs 18.0/21.4/21.5), Suri (5.2 vs 4.6), Wang-Zhang (4.3%/68.8% of 1,640 incl. non-compliant), Data Colada (Mandel ~38/cell; replication ~98/cell p<.001), CogBias 35.6 to 41.4, Malberg 0.41, Elkins SVI 0.52.

CORRECTIONS
- c21 origin means wrong: paper gives US open-source 0.81, SOTA US 0.36, SOTA China 0.36 (0.41, 0.39 are single models). Records 39,975, mean 0.52 (not 43,680, 0.53).
- b18/c21 temperature check is 3 models, p=0.875, not significant; "fragility rises at T=0" unsupported.
- h=0.612 attribution to Im and Chen / COVIDiSTRESS unconfirmed in Kuhberger text.
- Payne 2,550 (table) vs 2,150 (c12) unresolved.

CONTRADICTIONS
- Goal framing: Pinon d=.444 vs Kuhberger "no effect".
- Mandel 2014 ('exactly' removes effect) vs Data Colada and Mandel-Kapler 2018 (does not).
- Self-rewrite fixes GPT-4, overshoots GPT-3.5.
- Reasoning helps some families (Grok .48 to .23), hurts other slices.

WEAK SPOTS
- Several LLM framing tests change more than valence (Wang-Zhang rules, Payne story text, FRAGILE narration).
- Fixes scored for consistency, not accuracy. No equal-token cost test.
- Frontier-model evidence thin (Elkins, Payne, Malberg, one blog post).

SNIPPET-ONLY: a12, a18, a19, b14 (Many Labs 1 d .60 via Kuhberger/FORRT), b23, b25, b26, b28, c22, c27, c28, c29 (own synthesis). Single-source claims: K06, K14, K17, K18, K20, K22.

GAPS
1. Does S1 restatement keep accuracy, not just consistency, where the framed answer is correct?
2. How much LLM flip is pure valence vs information difference (matched structured-form design)?
3. Paraphrase-only flip rate for current frontier models on forced choice?
4. Does code-side neutral rendering beat a model-run rewrite at equal tokens?
5. Does original/neutral/opposite reconciliation in code work on gain/loss choice items?
6. Is Many Labs 1 (d .60 vs original 1.13) confirmed in the primary paper?
7. Do option order and negation cause more drift than valence in frontier models?
8. Does choice-vs-price reversal occur in reasoning models, and does a code check remove it?
9. When does the frame carry real information so that stripping it hurts?
10. Do debias prompts hold on held-out domains?


## Gap search results

Search budget and the C drive were both limited, so some gaps got only partial answers. New evidence is in evidence_d.jsonl (d01 to d18). Claims K02, K07, K11, K14, K15 to K20 were updated and K24 to K29 added.

Closed
- Gap 6: Many Labs 1 is confirmed in the primary paper (OSF manuscript and supplement). Pooled d=0.60 (95% CI .53 to .67) against original 1.13; 62.2% vs 33.5% choose the sure option (original 72% vs 22%); 86% of 36 samples significant in the same direction, 14% ns, 0% opposite; heterogeneity Q(35)=37.01, p=.69, I-squared 0. The vignette dropped "Asian" and used the local country. (d05, d06)

Partly answered
- Gap 2 (valence vs information): Ge et al. 2026 is close to a matched design (same prospect, polarity swap, 20 LLMs, 3 prospects): reasoning models are invariant, conversational models are not. Chun and Elkins show affect with length-matched controls adds no drift on rule-bound items (h=0.003). Robinson and Burden show story content changes behaviour a lot, which is an information effect. Still missing: one structured form, Asian-disease wording, frontier models. (d01, d10, d17)
- Gap 3 (paraphrase floor): frontier surface paraphrase is small on logic items (94% to 99.7% consistent, CRTBench). FRAGILE paraphrase ceiling is about 0.20 for small open models. The medical-QA baseline disagreement is about 24%. No frontier floor on framed forced-choice items exists. (d04, d11, d13)
- Gap 7 (order, negation, valence): cue words pull answers even with objective answers (MathComp); negation and contrapositive rewrites cost more than passive voice (CRTBench); reasoning models are order-invariant (Ge). No head-to-head of valence, order and negation in one frontier study, and no single normalisation tested. (d01, d03, d04)
- Gap 8 (choice vs price): reversal occurs in four frontier models at the top reasoning setting (48.4% to 30.7%), but the only source is still a preregistered blog post with separate-call design. No code-side check tested. (d02)
- Gap 9 (frame carries information): rule-fixed decisions show the frame is noise (d10). No LLM test where the frame signals a speaker reference point; the human evidence (Leong 2017) stands alone.
- Gap 10 (debias on held-out domains): CogBias shows sign flips across bias types in the same benchmark, FRAGILE shows CoT, instruction and steering raising flips in 7B to 8B models. This leans "no transfer", but held-out domains of the same bias were not tested. (d12, d14, d16)

Still open
- Gap 1 (accuracy kept?): no study measures consistency and accuracy together on items where the framed answer is right. MathComp and the rule-bound set have gold answers but test no restatement fix. CRTBench family consistency mixes the two.
- Gap 4 (code-side rendering vs model rewrite at equal tokens): nothing found.
- Gap 5 (reconcile original, neutral, opposite in code on gain/loss items): DeFrame is model-run, small models (3B to 14B), fairness and yes/no decision sets only; the opposite-frame step adds stability but most of the gain comes from self-revision and guidelines. (d07, d08)

Corrections to the claim set from this pass
- K14 had read DeFrame as a compare-in-code design. It is a model-run chain. Claim rewritten.
- K11 changed from established to contested: reasoning removes risky-choice framing in Ge et al. but not choice-price reversal, logical negation, or CoT-driven flips in small models.
- The earlier note "Payne 2,550 vs 2,150" and the Kuhberger h=0.612 attribution were not re-checked in this pass and stay unresolved.

Limits of this pass
- Several new papers are preprints dated 2026 and not yet peer reviewed. d15, d16 and d18 were read only in part (abstract, introduction and the relevant section).
- Table text from the PDFs was partly garbled for d05 (effect-size column headers), d08 and d14; those lines say so.
