# Critique, C11.03 Statistical MDL (cross-check)

## Corrections made (sources re-opened this session)
1. Blier and Ollivier 2018 (arXiv 1802.07044), Table 1: b04 listed "variational >400 kbits". That cell belongs to the compressed-network row. The variational code is 24.1 kbits (ratio 0.12, 95.5% acc), as a12 and c10 say. Float32 two-part: MNIST >8.6 Mbits (ratio >45); CIFAR10 >428 Mbits (ratio >2500). The "32 Mbits, 200x uniform on CIFAR" in a12 is a worked example for a 1M-parameter model, not a measured cell. Prequential 4.10 kbits / 0.02 / 99.5% and CIFAR 45.3 kbits / 0.27 / 93% confirmed. Catch-up numbers (5,000 and 1,000 samples) confirmed. b04's "22.2 kbits (ratio 0.11)" is a different prequential variant at 98.2%.
2. Deletang et al. 2024 (arXiv 2309.10668), Table 1: b10 said Chinchilla 70B adjusted rate is "1400-1500%". Wrong. The adjusted row is about 14,008% for 70B; about 1,400% belongs to 7B; about 211% to 1B. The text extraction of the table is garbled, so rows were matched by 2 bytes per parameter x parameters / 1 GB. Headline raw numbers (43.4, 58.5, 16.4, 30.3, 8.3, 32.3) confirmed in the abstract and text. Individual table cells for ImageNet/LibriSpeech are unverified.
3. Voita and Titov 2020 (2003.12298) confirmed: online code layer 1 115 vs 717, layer 0 96 vs 515 kbits; variational 85/470 and 103/612; accuracy 93.7 vs 96.3 at layer 0; seed flip 97.48/97.31 vs 97.38/97.48; "wrong for 8 out of 10 settings, MDL is always correct". a16 probe widths not rechecked.
4. Wu et al. (2212.10375) confirmed: 60.16, 58.14, 51.36, 50.43. Random is 42.78 in one table and 43.06 in another; a22 and c11 each quote one. Both exist.
5. Huang et al. (2404.09937): -0.95 per domain, -0.93 overall, RMSE 3.1%, HellaSwag -0.881, TriviaQA -0.951, MMLU -0.890 confirmed.
6. Lotfi et al. (2312.17173): 12.12 / 13.09 / 14.59 / 70.76 / 15.62 bits per dim and 96.41% error confirmed. Hypothesis Search (2309.05660): 17/23/30/33% and 49 hypotheses confirmed; 45% human-written not rechecked.
7. Elmoznino et al. (2410.14086): GPT-4 is "far worse" than small ICL models and the naive baseline, 5 seeds, confirmed. The appendix names gpt-4o at temperature 0; a24 says GPT-4.

## Contradictions and weak spots
- Raw versus adjusted accounting: Deletang's raw rates make LLMs look like great compressors; the adjusted rates reverse it. Any "LLM compresses X%" claim must say which.
- Huang's linear law holds for base models in-domain only; Elmoznino shows GPT-4 does not implement a prequential Occam prior on a novel task. These do not strictly conflict (average benchmark skill vs one novel task) but cap how far a length tie-break can be trusted.
- Wu et al.'s MDL selection reduces to model confidence (c12), so the MDL label adds little beyond a confidence heuristic. Tested only on GPT2-XL.
- Misspecification inconsistency is proven or demonstrated only in constructed settings; no LLM-agent study measures it.
- No evidence line tests a length tie-break inside an LLM agent loop against majority vote or confidence at equal tokens. MIDGARD (b22) is closest; the effect is near zero.
- Most claims are single-source. Established: the theory claims, fake-label incompressibility, the Huang correlation, and dataset-size dependence of MDL.
- Duplicates: a15/b01, a17/b09/c04, a12/b04/c10 describe the same papers; independent_sources counts each paper once.
- Not opened: b26 Rissanen 1978, b27 Schwarz 1978, b28 Hewitt and Liang 2019, c25 (snippet only). CompressARC (c15, c16), MADIL (b21), RIMRULE (b23), Ganeshan (b24), Kolmogorov Test (c13), MIDGARD (b22) numbers were not re-verified here (Semantic Scholar rate-limited, arXiv title search returned nothing).
- Disk note: drive C had under 10 MB free during this run; PDFs were kept on D and deleted.

## GAPS
1. Does choosing among N LLM-proposed hypotheses by shortest-description-that-fits beat first-fit, majority vote and model confidence at equal tokens on ARC-like or rule-induction tasks? (Decides whether S7 uses length at all.)
2. How should description length be computed for a natural-language or program hypothesis in an agent (token count, LM log-prob under a fixed prior, prequential on the examples), and which version predicts correctness best?
3. Does the complexity penalty help or hurt with few examples (catch-up effect) and when the true rule is outside the proposal set (misspecification)? Is a damped weight (eta below 1) better?
4. What do 2024-2026 MDL-based selection results look like on current LLMs: does Wu et al. (GPT2-XL, +3.5% over TopK) replicate, and beyond confidence?
5. Are the Deletang and Huang numbers stable across tokenizers and model families (Yuan et al. 2025 reports linguistic bias)? Is bits-per-character a usable cheap proxy inside one agent run?
6. Verify the unchecked ARC numbers: CompressARC (20% eval, 76K params) and MADIL (57 of 400). What is the cost per puzzle at equal compute, and can compression rank LLM candidate programs?
7. Why did GPT-4 fail prequential Occam on Mastermind (prompt format, scale, lack of meta-training)? Does a scaffold that forces sequential prediction of each example recover it?
8. Does MDL consolidation of stored lessons (RIMRULE) beat pruning by recency or usage on unseen tasks?
9. Source gap: Rissanen 1978 and Hewitt and Liang 2019 were not read directly; check the founding derivation and control-task numbers.

## Gap search results (evidence_d.jsonl, d01-d17)
Tool note: WebSearch quota was used up; arXiv API, OpenAlex and Semantic Scholar were rate-limited. Only papers with known ids could be opened. "Not found" below means not found with these tools.

- Gap 1 (length vs first-fit, vote, confidence at equal tokens): OPEN. No study tests it. Bounding evidence: about 9% of train-fitting ARC programs are false positives and majority vote removes about half of those problems (d04); Hypothesis Search says fitting programs almost always generalise (d05); sampling plus vote does not reliably help rule induction (d06). Room for a length tie-break is small. New claim K25.
- Gap 2 (how to compute length): OPEN. Nothing compares token count, LM log-prob and prequential code on LLM hypotheses. MADIL's authors say their expression lengths are poorly designed in places (d03). Direct LLM shortest-program writing is unreliable (d13).
- Gap 3 (few examples, misspecification, eta): PARTLY CLOSED. Theory side confirmed (d08, d09). ARC side: MADIL spurious fits rise with fewer examples (d02, d03). No test of a damped weight on LLM hypotheses. K26.
- Gap 4 (Wu et al. replication): OPEN. No replication found. Paper's own limits: gains need closed label sets and a good retrieval set (d10).
- Gap 5 (stability across tokenizers, families): PARTLY CLOSED. Huang normalises per character across 31 base models (d11); Deletang shows tokenizer effects reversing with model size (d12). Yuan et al. 2025 not found. K28.
- Gap 6 (CompressARC, MADIL): CLOSED for the numbers. CompressARC 20.0% pass@2, 18.5% pass@1, 76K params, 138 h for 400 puzzles (about 20.7 min each) (d01). MADIL 69 fit, 57 correct, 180 s budget; 59 correct vs Icecuber 117 under the stricter count (d02). Compression as a ranker of LLM candidate programs: OPEN, no test found. K16 now established.
- Gap 7 (GPT-4 on Mastermind): PARTLY ANSWERED. The run already predicted one example at a time with growing context (d15), so forced sequencing is not the fix. Prompt format, meta-training and task difficulty were not separated. Scale is unlikely (gpt-4o is large).
- Gap 8 (RIMRULE vs recency or usage): OPEN. Only compared with LLM prompt-merging; unseen gains of +1.0 and +0.9 are below the SD (d14).
- Gap 9 (sources): PARTLY CLOSED. Hewitt and Liang read (d07): linear probe 97.2 / 71.2 control / 26.0 selectivity vs MLP-1 97.3 / 92.8 / 4.5. Rissanen 1978 still unread; Gruenwald and Roos give the secondary account (d08).

Net for S7: no evidence yet that description length beats verify-then-vote at equal tokens. Keep length as a last tie-break only, after held-out fit and vote, and test it in our own harness (K25 test).
