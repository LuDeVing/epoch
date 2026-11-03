# Critique: A11.05 Connectionist and hybrid mapping models

## Corrections made (sources re-opened this session)
Re-opened: Webb, Holyoak and Lu 2023 (arXiv 2212.09196), Lewis and Mitchell 2024 (2402.08955), Stevenson et al. 2024 (2411.02348), Yasunaga et al. 2024 (2310.01714).
1. Webb 2023 digit matrices confirmed: generative OR 1.88, p=.005, CI [1.21, 2.91]; multiple choice OR 6.27, p=2.3e-8, CI [3.28, 11.99] (N=40). Evidence line a20 had this right; b10 omitted the p value.
2. Webb 2023 letter strings: overall OR 1.76, p=6.3e-5, CI [1.34, 2.31] (N=57). The zero-generalisation subset ALSO has OR 1.76 but p=.0007, CI [1.27, 2.46]. Lines that quote "OR 1.76, driven by zero-generalisation" are right, but the two ORs are separate numbers that happen to match. Claims cite the overall figure.
3. Story analogies: OR 0.37, p=.0003 confirmed.
4. Lewis and Mitchell 2024 Table 2: the PDF text puts the numbers 0.753, 0.488, 0.350, 0.452 one row off from the labels (Humans, GPT-3, GPT-3.5, GPT-4). The order humans .753, GPT-3 .488, GPT-3.5 .350, GPT-4 .452 is the only reading consistent with "humans stable, GPT below humans", but it is an inference. The N (1,876 human, 6,840 per model) is confirmed. Notable: GPT-4 is below GPT-3 pooled, which should be checked in the figure.
5. Stevenson et al. 2024 table confirmed exactly: adults .88/.91/.89 (N=62), GPT-4o .85/.63/.48, Llama-3.1 405B .79/.74/.27, Gemma-2 27B .60/.39/.14. Children (.62/.66/.67, N=41) were not separately re-read.
6. Yasunaga 2024: K=5 for GSM8K, K=3 for MATH/BIG-Bench/Codeforces confirmed; Codeforces GPT-3.5 13% to 15% and Acc@10 37% for best method visible. Gains on Codeforces are only 1 to 3 points, so "beats baselines" is small. Evidence line c20 says "best K 3 to 5"; paper just states the K values used, not a K sweep result I verified.
7. Evidence lines a04/a05 (Holyoak and Thagard 1989 tables) were flagged by their authors as garbled; cell labels are NOT reliable. Do not quote the 69/33/13 or 3/4/38/3 cycles by condition without checking the original print.
8. Not re-opened (time): Hummel and Holyoak 1997 Ross numbers (b06: LISA mapping 1.98 vs human .19), Musker coefficients, Thought Propagation tables, ConceptARC per-group numbers.

## Contradictions between sources
- a/b/c disagree on how many problem types survive counterfactuals in Hodel and West: "only remove-redundant and sort" (2 of 6) is consistent across them; fine.
- Hodel and West / Lewis and Mitchell (failed generalisation) versus Webb et al. 2025 reply (code execution fixes it): no consensus whether failure is missing abstraction or missing letter-index skill. Contested.
- Hummel and Holyoak 1997 claim ACME is too powerful; a06 shows ACME-style mapping is reachable by 5 of 8 humans, and 6 of 8 in the secondhand citation (b03/b05). The same experiment is reported as 5 all-six-correct + 2 four-of-six (a06) vs "6 of 8 correct within 3 min" (b03/b05). Unresolved; likely different counting of partial credit.
- Webb 2023 says GPT-3 far-analogy is n.s. (p=.065) for story analogies, while GPT-4 is near-perfect. The 2025 paraphrase test shows GPT-4 drops 86% to 72% when overlap is removed, so GPT-4 strength is partly surface overlap.

## Weak spots
- Almost all human data for ACME/LISA come from the authors' own simulations on hand-built propositions (tens of units). No test on open-domain text. The 1997 LISA runs were on a 486 PC; scale-up not shown.
- LISA reproduces SIGNS of human effects, not sizes (access index -1.3 vs human -.22; mapping 1.98 vs .19). So "LISA explains" claims are qualitative.
- Copycat evidence is entirely qualitative (no human data).
- Most LLM studies are on one task family (letter strings) and one model generation (GPT-3 to GPT-4o). Nothing found for 2025-2026 reasoning models (o-series, Claude 4+) on counterfactual letter strings in these evidence files.
- Analogical prompting and Thought Propagation are not mapping models; they only borrow the word "analogy". Link to ACME/LISA is thin.
- Wide claim "attention implements ACME/LISA mapping" is an argument, no ablation.

## Seen only in snippets or abstracts
Gendron et al. 2023 (b20, abstract only); Webb et al. 2021 ESBN exact numbers (b25 abstract only; c23 read more); Altabaa et al. Abstractors (c24, figures only); relational-bottleneck review (b24); original model papers in line c29 were flagged unopened by angle C but angles A and B opened them.

## GAPS (most decision-relevant first)
1. Do 2025-2026 reasoning models (with long chain of thought and code tools) pass counterfactual and far-transfer letter-string/ConceptARC analogies, and does the pass come from abstraction or from tool use?
2. At equal tokens, does an explicit ACME-style mapping step (candidate correspondences scored on structure, semantics, pragmatics, with one-to-one inhibition) beat free-form chain of thought on cross-mapped and relational-role tasks?
3. Does serial chunked mapping (a LISA-like capacity limit of about 4-6 bindings per step) help or hurt LLMs on many-correspondence problems?
4. Does separating retrieval of analogs from mapping (Ross-type dissociation) improve far-analog use in an LLM with memory, and does surface-cue retrieval cause negative transfer?
5. Is Copycat-style interleaved re-representation (re-describe while mapping) better than mapping from a fixed description on open-domain analogies, and has anyone built an LLM version with measured results?
6. Can an importance-weighted coverage gate (LISA's 70% rule) cut unsupported analogical inferences in an LLM?
7. How big is the surface-overlap shortcut in other analogy benchmarks (answer order, sentence overlap), and what invariance test is cheap enough to include in the scaffold?
8. Are Yasunaga-style self-generated analogs useful in small models if exemplars are retrieved or verified, and at what token cost compared with self-consistency?
9. Does the relational-bottleneck idea (separating relations from object attributes) transfer to prompt design, for example by anonymising object names before mapping?
10. What do the original Holyoak and Thagard 1989 tables (cycles by condition, convergence percentages) actually say, given garbled extraction?

## Gap search results (evidence_d.jsonl, d01-d18; claims K22-K28 added, K02/K05/K14/K16/K17/K21 updated)
Tool limits: WebSearch was used up for the session (3 calls refused), arXiv API, Semantic Scholar and OpenAlex returned rate-limit errors. All work was done with arXiv listing pages (WebFetch) and PDFs read with pdftotext. Searches were therefore title/abstract based and not exhaustive.

1. CLOSED in part. Reasoning models (o3, o4-mini, Claude Sonnet 4, Gemini 2.5) now match or beat humans on text ConceptARC (o3 77.1% vs 73%), but ~27% of correct outputs use unintended rules (humans ~7%); code tools do not raise text accuracy, effort does (d01, d02). Far analogy (ARCANA) is still 10 to 52 points below humans (d05). Raven-type tasks collapse with load (d15). Still open: counterfactual letter-string tests of o-series / Claude 4+ models; I found none.
2. OPEN. No study compares an explicit ACME-style scored mapping step with free chain of thought at equal tokens. Nearest: ARCANA analogy-correctness correlation, which is confounded by modality (d07).
3. OPEN. No LLM chunked-mapping study found. Only indirect support: performance falls with binding load even with long reasoning (d15).
4. PARTLY CLOSED. Puranam et al. show retrieval/application split in GPT-4: recall 1.00, precision ~0.5 with a hint, none without (d08). No memory-agent study with measured negative transfer.
5. PARTLY CLOSED. ConceptSIR (d06) is a Copycat-style LLM loop, 9/17 on a hard subset, no control arm. No matched fixed-vs-interleaved test.
6. OPEN. Nothing found on an importance-weighted coverage gate for analogical inference.
7. CLOSED in part. Answer-order bias (GPT-4 89% vs 61%, d03), embeddings reach 78% alone (d12), identification among many stories ~30% (d16). Cheap tests for the scaffold: swap order, paraphrase, permute symbols.
8. CLOSED. Self-generated analogs help only when the examples are accurate; relevance does not matter on math; verified fixed sets are cheaper and as good (d09, d10). MetaLadder (d11) needs training. No equal-token comparison against self-consistency found.
9. OPEN, with indirect support. Interpretability work (d13, d14) says abstract relations tied to familiar lists do not generalise and application is a separate failure; no prompt-level anonymisation test found.
10. CLOSED in part. Table 15 read cleanly (3/4/38 and 3/4/none cycles); Table 5 column assignment stays uncertain because of the scan (d18).

Corrections to earlier lines: K16 (GPT-4 ConceptARC 25%) is now dated; K17 downgraded to contested because the replication (d09) reverses the relevance claim on math. Limits: several PDF tables were scrambled (d05, d08, d09, d12); numbers marked as uncertain in the evidence lines.
