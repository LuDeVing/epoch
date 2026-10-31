# A11.01 Structure mapping: cross-check critique

NOTE: the C: drive was at 0 bytes free during this pass, so claims.jsonl and critique.md could not be written into the subfield folder. They are in D:/research_scratch/A11.01/out/ and must be copied over once space is freed.

## Numbers re-opened this session (arXiv PDFs via pdftotext)
1. Lewis & Mitchell 2024 (arXiv 2402.08955), Table 2: 0.753, 0.488, 0.350, 0.452 with CIs; 1,876 human samples, 6,840 per model. Confirmed. The row labels in the layout text are shifted, so the label order (Humans, GPT-3, GPT-3.5, GPT-4) is inferred, not read. Surprising point: GPT-3 above GPT-4. Keep the caveat.
2. Chen et al. 2024 (arXiv 2404.12728): GSM8K relevant 71.5, none 75.5, random-different 76.3; MATH relevant 33.3, none 36.1, random-different 34.1. Confirmed.
3. Yasunaga et al. 2024 (arXiv 2310.01714): self-generated exemplars 75.8 (GSM8K), 33.9 (MATH). Confirmed. The 5-shot CoT 75.0 figure and Codeforces numbers not re-read.
4. Webb, Holyoak, Lu 2023 (arXiv 2212.09196): digit-matrix OR 1.88, p=0.005, CI 1.21-2.91; near story analogy p=0.0039, t(53)=21.5. Confirmed.

Not re-opened (no network answer or disk full): Clement & Gentner 1991 numbers, SMTB 515x, Forbus 2017 39/45 and 52/56, Alfieri d.

## Corrections and inconsistencies
- Clement & Gentner 1991: evidence a11-a13 and b01-b03 disagree on Exp 2 numbers (a12: free prediction .53 vs .12, N=32; b02: net M=1.63, F(1,28)=20.05; a13 gives .92 vs .13 for Exp 3 with N=48 while b03 says N=46). Sample sizes for Exp 3 (48 vs 46) and the exp numbering conflict. Treat all per-experiment figures as unverified until the 1991 paper is opened in full; only the direction of effect is safe.
- Alfieri et al. meta-analysis: d=.60 (2011 abstract, 57 experiments) vs about .50 (2013 published, snippet only). Use "0.5 to 0.6".
- Webb 2023 humans on letter strings: N=57 in c02, N=57 in b04. Consistent. Digit matrices N=40. Fine.
- Musker et al.: b09 and c09 give p-values and cell sizes consistent; year shown as 2024 and 2025 (preprint vs publication).
- Gentner 1983 (a01): scanned PDF, only the summary pages were readable. The core theory text was never read; the claim rests on later citations.
- StoryAnalogy: b11 says ChatGPT about 30% vs humans over 85%; c13 says 29.2-35.8 vs 85.7. Consistent.

## Contradictions between sources
- Original Webb 2023 says GPT-3 matches humans; Hodel & West and Lewis & Mitchell say not on counterfactual variants; Webb 2024 says yes with code execution. Net: ability is brittle and partly procedural.
- Analogical prompting (Yasunaga) reports gains; Chen finds relevance does not matter. Net contested.

## Weak spots
- Only one lab produces the human systematicity data (Gentner group), mostly 1986-1997, small N. No independent replication of the Clement and Gentner selection effect was found.
- No failed replication of the core systematicity result was found; absence may be search depth.
- Items c15, c18, c19, b19 were snippets only; do not cite for numbers.
- Most LLM studies use GPT-3 to GPT-4 era models, not 2025-2026 reasoning models. Musker is the only one with Claude 3 and Llama-405B.
- Human cells in Musker are 15-18 per condition.

## GAPS
1. Does a code-scored typed mapping (O7) beat free-text mapping at equal tokens on permuted-relation tasks with a current model? (Webb 2024 hints yes; no direct test.)
2. Has the Clement and Gentner (1991) systematicity-selection effect been replicated independently, with exact numbers, and in what N?
3. What do 2025-2026 reasoning models score on counterfactual letter-string and permuted-pair tasks (Lewis & Mitchell, Musker designs)?
4. How well does LLM-extracted relational structure (the representation step) agree with human-built structure? YARN suggests abstraction is the bottleneck; measured parse accuracy is missing.
5. Does relevance of recalled analogs matter for strong models on non-math tasks? Chen says no on GSM8K; test elsewhere.
6. Does mapping-based retrieval (structure-first) beat embedding retrieval for choosing past cases at equal tokens (links to subfield 03, case representation)?
7. What does the SME corpus show on failure modes when representation is flat or noisy (SMTB says higher-order bias fails)? Need a noise-robustness figure.
8. Gentner 1983 core experiments (flowing waters, tables) were never read; open a text-readable copy.

## Gap search results (2026-10-31)

Search note: WebSearch quota was used up; OpenAlex and Semantic Scholar rate-limited; arXiv API throttled. Papers were found through arxiv.org/search and opened as PDFs (pdftotext). Evidence is in evidence_d.jsonl (d01-d19). No email address was sent anywhere.

Number checks now closed:
- Clement & Gentner 1991 re-read in full. Exp 1 N=48, Exp 2 N=32 (16/16), Exp 3 N=48 (24/24, not 46). Key F values and proportions are in d01-d03. The a12/b02 conflict is resolved: .53 vs .12 is the free-prediction proportion, M=1.63 is the shared-minus-different count.
- SMTB speedup is 5-15x. "515x" was a lost en-dash. Claim K15 corrected.
- Forbus 2017: 52/56 (93%) and 39/45 confirmed.
- Alfieri: d=.60 at experiment level (57 experiments, CI .47-.72), .50 at test level.
- Lewis & Mitchell Table 2 labels read from raw text: humans .753, GPT-3 .488, GPT-3.5 .350, GPT-4 .452. Caveat removed.

Gaps:
1. Code-scored vs free-text mapping at equal tokens: STAYS OPEN. Nearest evidence: Webb 2024 (code only for counting, P=0.496 vs humans) and PRISM (code score 82.5% vs zero-shot 88.5%, different errors, McNemar p=.0227). Net: code scoring is a complement, not shown to be better. New claim K20.
2. Independent replication of Clement & Gentner: STAYS OPEN (not found). Exact numbers now fixed; effect in all three experiments but Passage 2 of Exp 3 failed. New claim K19.
3. 2025-2026 reasoning models on counterfactual letter strings: PARTLY CLOSED. Hellwig et al. 2026 tests GPT 5.2, Claude Sonnet 4, GPT-OSS 120B and others but gives bars only; ARCANA gives numbers for far analogy (GPT 5.2 48-51%, humans 58-69%). No o1/o3/R1 score on the Lewis and Mitchell design found. Claim K21.
4. Parse accuracy of LLM-extracted structure: STAYS OPEN. Indirect evidence only (YARN 0.17 to 0.46; PRISM role ablation to 24%). Claim K22.
5. Relevance of recalled analogs for strong models: PARTLY CLOSED for weak models (Chen: relevant below none on CSQA, MBPP, GPQA); strong models untested. Claim K23.
6. Structure-first vs embedding retrieval at equal tokens: STAYS OPEN. AnaloBench shows LLM retrieval from 200 stories near random for long stories; no structure-first arm. Claim K23.
7. SME robustness to flat or noisy representation: STAYS OPEN. SMTB has no noise experiment (checked, d19); only argued failure cases and kernel-violation rates (0.14-9.16%).
8. Gentner 1983 core experiments: STAYS OPEN. The scan still yields only discussion and references (d05). Gentner & Gentner 1983 (flowing waters) is readable and gives Exp 1 F(1,13)=4.53 on 15 of 36 subjects (d04). Claim K24.

Disk note: C: had about 570 KB free; writes to the subfield folder were kept small.
