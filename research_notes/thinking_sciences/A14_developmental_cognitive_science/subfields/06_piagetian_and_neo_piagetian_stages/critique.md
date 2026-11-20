# A14.06 Piagetian and neo-Piagetian stages: critique

## Corrections made (numbers re-opened this session in the paper HTML)
1. CogLM (arXiv 2408.09150v3): confirmed GPT-4 84.7 (age 20.0), GPT-3.5 64.0 (16.1), Llama-2-70B 54.6 (14.1), human 93.7 (21.5); planning 59.4 vs 95.6; propositional 61.0 vs 82.0; 207 questionnaires, 141 valid; Spearman 0.7169, Pearson 0.7362; held-out Spearman 0.9354 (c02 wrote 0.935, fine); Chain-of-Cognition 31.0 to 38.1. All correct.
2. ConservationBench (2603.07109): confirmed 82/112 (73.2%) under 10% strict; human 98.35%; empty-image conserve 85.7%; CoT effect F(3,333)=18.28. CORRECTION: b08 and a23 state scale explains R2=0.239. In the paper R2=0.019 is for conservation accuracy; 0.239 is only for non-conserving control items. Claim K09 carries the fix.
3. Also in that paper: the 85.7% is the rate of "Conserve" answers on blank images for conserving tasks, and for non-conserving tasks models switched to "Conserve" (71.5% on "More"). It is a response bias figure, not a skill figure.
4. CoreCognition (2410.10855v4): confirmed 230 models, 11 prompts, 2,530 data points, human mean 86.98, GPT-o1 74.91, GPT-4o 69.25, GPT-4o permanence 52.86, "10 of 12 abilities no significant difference".
5. Gong n-back (2305.03731v4): confirmed GPT-3.5 H=58.54 p=1.94e-13, GPT-4 H=52.51, 50 blocks per n.
6. Strong Memory, Weak Control (2504.02789v2): confirmed r=0.82 params vs span (a25 truncated this), flanker Llama-8B 0.471 to 0.910 and Qwen2-32B 0.638 to 0.985, forward span 0.99-1.00, backward span d=15 0.21 for Gemma-9B.
7. REL (2604.12176v2): confirmed 45%, 93%, 65.7/38.1/26.0. Weak point: C1 and C2 have the same RC=2 but 65.7 vs 38.1, so the "39.7% drop" in b24 mixes relational complexity with other task features (the authors call it OC). Do not cite it as a clean RC effect.
8. Not re-opened (no free access or paper not retrievable): Baillargeon 1987 numbers, Bogartz 2000, Clearfield 2009, Schapiro and McClelland 2009 (taken from earlier agents who opened them), Samuel and Bryant 1984.

## Contradictions and duplicates
- The same paper is logged three times under three author names: CogLM appears as Zhu (a20), Wang (b01) and Zhao (c01) 2024/2025. Luo conservation papers appear as Su (a22), Luo (b05, c05); CoreCognition as Li in a18, b09, c08. These are the same studies, so they count as ONE independent source each. Author names could not be checked (Semantic Scholar rate-limited); use the arXiv ids.
- Gong n-back (a24, c18), Strong Memory Weak Control (a25, c17), REL (b24, c19, c20) and the WM paper (a26, c16) also repeat across files.
- Source count for LLM claims is therefore low: most are single-source. Only K10, K13, K14, K16 reach two by combining different papers.
- ConservationBench abstract says "near chance", yet top models average 60-69 on the 3-choice score; strict scoring is what makes it look near zero.
- a18 says Claude-3.5-Sonnet permanence 32.43; this number was not re-checked.
- CoreCognition and CogDevelop2K disagree on which stages models find hard (CogDevelop2K reports a reversed order); stage labels are the authors' own mapping in both.
- Model counts differ across passes (46 vs 48 in CogDevelop2K; 240 vs 1,200 in ChildSafe).

## Weak spots
- Most founding-study evidence comes from Wikipedia summaries (a01-a05, a15-a17, b15, b16), with no N. Piaget's own books and the original 1956 mountains study were not opened.
- The core neo-Piagetian age tables (Pascual-Leone, Case, Halford, Demetriou) are second-hand.
- Human baselines in LLM papers are small: 6 adults (ConservationBench), 141 aged 6-20 (CogLM), human norms from other studies (executive functioning paper).
- No study runs an LLM and children on the same conservation or seriation task.
- No LLM study tests whether a stage-ordered scaffold beats an equal-token plain one. Chain-of-Cognition is the closest (single small model).
- This subfield is "background only" for the schema; evidence for real G/S/O changes is indirect.

## Only seen in snippets or not opened
b17 (Samuel and Bryant 252 children), b18, b21, c22, c25, a26 (WM paper opened only in c16), a27 (403).

## GAPS
1. Does an explicit stage-ordered scaffold (prerequisite sub-answers fed first, as in Chain-of-Cognition) beat plain CoT at equal tokens on a strong model? Only one small-model result (31.0 to 38.1) exists.
2. Is the VLM conservation failure a response bias to "Conserve" (blank image 85.7%) or a real perceptual deficit, and does it appear in text-only reasoning agents?
3. Which controlled step fixes flanker-like interference failures (reasoning lifted Llama-8B 0.471 to 0.910) but not WCST rule switching, and what does that cost in tokens?
4. Does relational complexity predict LLM errors once other task features are held fixed (REL-C1 vs C2 shows RC alone is not enough)?
5. Do Piaget-inspired agent memories (PISA, CAM) gain from the schema-revision mechanism itself? No ablation exists.
6. What are the actual original numbers for the mountains task, Samuel and Bryant 1984 and Pascual-Leone's M-power tables, from primary papers?
7. Do looking-time findings on infant object permanence survive large multi-lab replication (the Bogartz alternative vs knowledge account)?
8. How does LLM accuracy on false belief and perspective taking change with prompt framing in newer reasoning models, given perspective taking worsens with scale and with reasoning (P=0.0037)?

## Gap search results
Evidence in evidence_d.jsonl (d01-d18; 13 opened, 5 snippet-only). Claims K22-K28 added; K02 raised to established; K03, K07, K08, K17, K19 gained evidence ids.
1. Stage-ordered scaffold vs plain CoT at equal tokens: STILL OPEN. Closest is least-to-most (d09): SCAN length 99.7 vs CoT 16.2, GSM8K only 62.39 vs 60.87, 2022 model, not token-matched.
2. VLM conservation bias vs perception: MOSTLY CLOSED (d10). Blank image 85.7% and text-only 73.7% Conserve, so it is largely a response prior and also appears without images. Pure perception is not separated.
3. Flanker vs WCST: CLOSED in direction (d13). Reasoning fixes interference (0.471 to 0.910) not rule switching (0.29-0.53). Token cost only described as thousands.
4. Relational complexity controlled: PARTLY CLOSED (d11, d12). Biology task RC explains 24-44% of variance with other factors fixed; chemistry shows operand complexity also matters.
5. Schema-revision ablation: PARTLY CLOSED (d01, d03, d04). SCG-Mem without assimilation loses 20-35% F1 (3B model). PISA and CAM ablate other parts. Accommodation alone untested.
6. Original numbers (mountains, Samuel and Bryant means, Pascual-Leone tables): STILL OPEN. Only the Samuel and Bryant abstract was opened (d14); Borke's 79/93 is a secondary snippet (d15); no M-power tables obtained.
7. Object permanence multi-lab replication: STILL OPEN. None found. Bogartz 2000 opened (d08); false-belief VoE replications failed (d06, d07).
8. False belief with newer reasoning models: STILL OPEN. d05 only tests older open chat models and excludes RL reasoning models; clean +22.4 CoT gain, perturbed +3.9.
Note: WebSearch budget was exceeded by one call (9 used); arXiv API was rate-limited.
