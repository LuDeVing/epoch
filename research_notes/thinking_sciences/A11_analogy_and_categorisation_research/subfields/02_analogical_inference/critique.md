# A11.02 Analogical inference: cross-check and critique

Cross-checker pass over evidence_a, evidence_b, evidence_c (78 lines). Sources re-opened this session as full text: Lewis and Mitchell 2024 (2402.08955), Stevenson et al. 2025 (2411.02348), ARN (2310.00996), Yasunaga et al. (2310.01714), StoryAnalogy (2310.12874), Webb et al. 2023 (2212.09196), Clement and Gentner 1991 (PDF), Markman 1997 (HTML). Claims are in claims.jsonl (A11.02-K01 to K23).

## Numbers re-checked (confirmed unless stated)

1. Lewis and Mitchell Table 2: humans .753, GPT-3 .488, GPT-3.5 .350, GPT-4 .452; 1,876 human and 6,840 per-model samples. Confirmed. The text extraction interleaves labels, but the row order matches.
2. Lewis and Mitchell Table 4 (rows GPT-3, GPT-4, Human): alternative valid rule 5.81 / 22.00 / 38.59; incorrect rule 30.97 / 32.67 / 14.67; completely wrong 7.74 / 2.67 / 12.50. **CORRECTION to c03:** c03 labelled 38.59% as GPT-3.5 and 5.81% as GPT-3. The table caption says GPT-3, GPT-4, Human, so 38.59% is HUMANS. GPT-3 5.81%, GPT-4 22%. Note that a19 (46% GPT-4 vs 39% human valid alternative rule, from Webb) is consistent with 38.59% for humans. The c03 line should not be used.
3. Stevenson et al. Table 2: adults .88/.91/.89 (n=62), children .62/.66/.67 (n=41), GPT-4o .85/.63/.48, Claude-3.5 .68/.62/.46, Llama-3.1 405B .79/.74/.27, Gemma-2 27B .60/.39/.14, 54 runs each. Confirmed.
4. ARN: near humans 97.9 vs models 75.0; far humans 94.1 vs models 39.6; GPT-4 mean 68.1; SBERT 42.3; human partitions 98.6/97.2/96.8/91.4, mean 96.0. Confirmed.
5. StoryAnalogy: random 25%, humans 85.7%, best LLM 37.7 points below humans; Fleiss kappa 47% entity, 42% relation. Confirmed. **Qualification:** "ChatGPT about 30%" is right for ChatGPT, but other LLM cells reach 44.2 (GPT-3.5), and the best model is about 48%. "LLMs near 30%" overstates the gap for the best model.
6. Yasunaga Table 2 (Codeforces, Acc@1/Acc@10): GPT-3.5 8/24, 9/27, 11/27, 13/25, 15/29; GPT-4 16/30, 16/29, 17/31, 17/32, 19/37. Confirmed (b24 correct). **Qualification:** the headline "GPT-3.5 15% vs GPT-4 16%" compares the best prompt variant (exemplars plus knowledge) of GPT-3.5 against plain GPT-4 0-shot, and not at equal tokens.
7. Webb et al.: digit matrices generative OR 1.88 (p=.005, CI 1.21-2.91), multiple choice OR 6.27 (CI 3.28-11.99), letter strings OR 1.76 (p=6.3e-5; zero-generalisation OR 1.76, p=.0007), stories OR 0.37 (p=.0003, CI .21-.63), 15/54 perfect. Confirmed. a15 gives the letter-string N=57 correctly.
8. Clement and Gentner Exp 1: ratings 6.28 vs 4.89 (analogy), 5.22 vs 5.31 (control), F'(1,44)=13.99; choice 3.17 vs 2.0, F(1,44)=18.43. Exp 2: shared-minus-different 1.63 vs 0, F(1,28)=20.05; free prediction .53 / .12 / .27 vs control .12 / .12 / .74 (Table 5); choice 2.9 vs 1.8. Exp 3: .92 vs .13, F(1,44)=5.15; choice 1.875 vs 1.0, F(1,44)=13.15. Confirmed. Note that a08 and b02 report different statistics for the same experiment (proportion vs per-subject difference); both are right.
9. Markman Exp 1 (.52 vs .22, t(31)=3.97), Exp 2 (1.26 vs .30, t(59)=7.32, F(2,116)=30.49), Exp 3 (1.45 vs .39, t(46)=6.23), Exp 3a (1.41 vs .36, t(77)=7.20; 66/78=85% vs 9/78=12%). Confirmed.
10. Not re-opened: SME paper numbers (6.99, 3.94, 2.44; O(N^2)), Colhoun and Gentner, Musker et al. coefficients, Thought Propagation, Hu et al., Memento. These stay as reported but unchecked.

## Contradictions and tensions

- Webb et al. versus Lewis and Mitchell / Hodel and West: on the standard alphabet Webb found GPT-3 above students, while Lewis and Mitchell found GPT below humans even there (and humans at .753 versus lower in Webb). Protocol differences (human sample, problem set, prompt) are not resolved. The code-execution reply (N=60 per interval, hand scored) is small.
- Lee and Holyoak (causal-model unity) versus Colhoun and Gentner (SME plus later causal step): we hold only the second side's description. The original was not opened (b15 opened:false).
- Systematicity helps in humans (Clement and Gentner, Markman) yet does not guarantee truth (Antarctica to Mars, shared preventer). Not a contradiction, but it means the structural filter lowers noise and does not certify.
- Markman Exp 3 versus 3a: chain valence effect flipped direction; authors could not explain it.

## Weak spots

- The human inference evidence is all from two labs and one theory family. Both used short written passages with undergraduates and few items. Same-lab "replications" are not independent.
- No source found tests an LLM on human-style candidate-inference selection (shared-system vs isolated fact), which is the closest analogue of O7. The LLM studies test analogy identification, rule transfer or prompting, not conjecture validation.
- No LLM study here measures false-conjecture rate before and after a verifier. Yasunaga's audit (28 of 50 failures with a good source) is the nearest.
- Newest models: ARN and StoryAnalogy are 2023-24 models. Stevenson (2025) tops out at GPT-4o, Claude-3.5. No reasoning-model measurement (o1-class, R1) besides one anecdote (c07).
- Equal-token comparisons are absent from Yasunaga and Thought Propagation (more output tokens by design).
- Thought Propagation relies mostly on model self-evaluation and model-rated coherence; ALFWorld table rows were garbled in extraction.

## Only seen in snippets, abstracts or second-hand

Lee and Holyoak 2008, Lassaline 1996, Spellman and Holyoak 1996 (b09 numbers are Markman's summary), Brown et al. 2020 and Wu et al. 2023 via citations, Day and Gentner 2007 (title only; scanned PDF), Sultan and Shahaf (abstract and intro), ANALOGICAL benchmark (abstract and skim), ACME paper (host refused). Table cells garbled in extraction: Yasunaga Table 4 and BIG-Bench rows, TP Table 2 and ALFWorld rows, Lewis and Mitchell per-condition accuracies.

## GAPS (most decision-relevant first)

1. Does adding a separate verification step (code check, test run, or counterexample search) to LLM-transferred conjectures lower the rate of wrong conjectures kept, at equal tokens? No study measures this directly.
2. Do current reasoning models (2025-26) still fail far-domain, near-decoy analogy (ARN-type) and mutated letter-string transfer, or has the gap closed? No measured result after GPT-4o and Claude-3.5.
3. Does analogical prompting (Yasunaga) or Thought Propagation still beat plain CoT or best-of-N at equal total tokens, and for strong 2025 models?
4. Can an LLM reproduce the human systematicity preference when choosing which source fact to project (Clement and Gentner design run on LLMs), and does a mapped-causal-chain rule improve accuracy of kept inferences?
5. What is the false-conjecture rate when a model copies from a surface-similar but structurally wrong source, and does an explicit structure check (relations, not entities) remove it? Quantify with decoy items.
6. What do Lee and Holyoak 2008 and Day and Gentner 2007 actually report (preventers, nonintentional inference)? Do unrequested analogical inferences arise in LLM reading and should O7 run when no analogy was asked for?
7. Is the letter-string failure counting (fixable by code) or structure transfer? A larger, independent test of GPT-4-class and reasoning models with and without code, on multiple mutated task families beyond letter strings.
8. Do verified retrieved sources (AnalogyKB-style banks, case memory as in Memento) beat self-generated sources for strong models, and what is the effect of source quality on transfer?
9. Do independent labs (not Gentner or Markman) replicate the systematicity-in-inference result with larger samples, other domains, or non-student participants?
10. Does keeping the source verbatim in context (versus summarised) change conjecture accuracy in LLMs, as the Exp 3 memory result suggests for humans?

## Gap search results

Evidence file: `evidence_d.jsonl` (d01 to d21). New claims K24 to K29; K13 changed to contested; K03, K06, K07, K09, K10, K11, K14, K20 got added evidence. Limits of this pass: WebSearch quota was exhausted, so sources were found through the arXiv site search, the Hugging Face papers API, Crossref and Europe PMC, then opened as PDFs. Lee and Holyoak 2008, Day and Gentner 2007, Holyoak, Lee and Lu 2010 and Lassaline 1996 are paywalled or scanned; only abstracts were read (opened:false).

1. Verification step at equal tokens: STAYED OPEN for conjectures, partly answered for neighbours. No study tests a verifier on transferred analogical conjectures. Neighbouring results (d06 to d09, K24): LLM counterexample search is weak (under 9 percent, o3-mini high), model-judged verification loses to extra samples at equal compute until about 8x budget, and verification can flip right answers to wrong (harmful flips 2.2 to 1.0 percent with a gate). Code execution against a validator removed validation errors. Direction: use executable checks, not model judgement.
2. Reasoning models and far/near analogy: PARTLY CLOSED. Not closed on related tasks (d02 to d04, K25): o3-mini and R1 collapse to 17 and 23 percent on noisy Raven, top models 39.8 vs humans 68.5 on A2RBench, Claude Opus 4.5 and Gemini 3 Pro at chance on high relational complexity. ARN and mutated letter strings were not re-run on 2025-26 models (d01 has figures only). Still open for those exact items.
3. Analogical prompting vs CoT or best-of-N at equal tokens: STAYED OPEN, with a negative lead. Qin et al. (d10) show random correct examples do as well as relevant ones on GPT-3.5 and GPT-4o-mini, so K13 is now contested. Shen et al. (d11) show a gain on novelty at equal call count for 2026 models, not correctness. No equal-token comparison against best-of-N was found.
4. LLM systematicity preference (Clement and Gentner on LLMs): NOT FOUND. No study found. Lassaline 1996 (d20, abstract only) is human evidence of the same rule.
5. Decoy false-conjecture rate and relation check: PARTLY ANSWERED, mechanism only. d14 shows failures align with the lexically similar distractor in 7 to 14B models; d16 shows irrelevant-context decay and recovery by voting or an ignore-instruction. No false-conjecture rate for a relation-level check was found.
6. Lee and Holyoak, Day and Gentner, unrequested inference: CLOSED AT ABSTRACT LEVEL. Lee and Holyoak: removing a shared preventer lowers similarity and raises inductive strength (3 experiments). Day and Gentner: readers used a similar earlier passage without awareness; mapping was structural. For LLMs, d15 shows unrequested transfer of a procedure from a metaphorical source (23 to 35 percent of samples vs 3 to 10 for literal text; adversarially searched). Recommendation: run O7 whenever a source schema is in context. Cell values still unread.
7. Letter-string failure: counting or structure: STAYED OPEN. Webb et al. reply (d21) says the dispute stands. REL tool test (d05) suggests structure binding is not cured by a toolkit, but it is not a paired test and not a letter-string task. No larger paired with/without-code test found.
8. Verified retrieved sources vs self-generated: PARTLY ANSWERED. d12 (flipped labels cut F1 in 5 of 6 models) and d13 (similarity-only retrieval plateaus; utility re-ranking +3.8) show source correctness and outcome record matter. d10 shows the accuracy of self-generated examples is the factor. No same-model, equal-token test of self-generated vs verified retrieved sources for strong models.
9. Independent labs replicating systematicity: STAYED OPEN. Only Lassaline 1996 and Holyoak, Lee and Lu 2010 abstracts were found as related but not direct replications; affiliation of Lassaline not checked. No larger or non-student replication found.
10. Verbatim source vs summary in LLM context: NOT FOUND. Only indirect hint: Hellwig et al. (d01) find copy tasks make the small model learn letter-string analogies (25 percent vs 100 percent of runs developed matching heads in their appendix), which is a training result.

Corrections still standing from the cross-checker: c03 not to be used; StoryAnalogy best model about 48 percent; Yasunaga headline not equal-token.

Checks made this pass: d12 table had one unlabelled row (80.65 ... 88.48) in extraction and was excluded; d03 and d06 tables were misaligned, so only headline text figures are cited; d09 was read in part (abstract and introduction).
