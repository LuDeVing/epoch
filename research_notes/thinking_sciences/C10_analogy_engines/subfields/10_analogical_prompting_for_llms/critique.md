# C10.10 Analogical prompting for LLMs: cross-check and critique

## Corrections made (re-opened from arXiv PDFs this session)
Re-checked: Yasunaga Tables 1-5 (2310.01714), Qin et al. Tables 1-5 (2404.12728), Zhang 2026 (2602.09794), Gwak 2026 (2602.15863), Chen Self-ICL (2305.15035), Yu Thought Propagation (2310.03965).
1. b02 (Yasunaga Table 4): davinci-003 fixed and retrieved 5-shot were given as 50 and 54. Correct: 0-shot CoT 50, fixed 5-shot 54, retrieved 57, ours 61. (a05 and c04 were right.) davinci-002: 43/47/48. davinci-001: 10/11/9. curie: 2/3/2.
2. b04 (Yasunaga Table 3): rows were shifted by one. Correct: 0-shot 66.8, 0-shot CoT 67.6, 3-shot CoT 68.4, ours 75.2 (word sorting). The "75.2 row is the knowledge variant" guess is wrong; it is the method itself. a04 and c03 are right.
3. c09 (Gwak 2026): the Llama-3.3-70B "MATH" cells (33.59 / 35.19 / 33.59) are GSM8K values. Correct Llama-3.3-70B: GSM8K 32.67/35.19/33.59, MATH 25.26/28.34/26.69. Also GPT-4.1 GSM8K 48.8 to 57.9 (+9.1).
4. Confirmed unchanged: Table 1 (GSM8K 75.0/75.8/76.7/77.8; MATH 33.0/33.9/34.9/37.3), Table 2 Codeforces, K sweep (K=1 76.1/34.8 to K=5 77.8/37.1; text says best at K=3 or 5), Qin GSM8K/MATH/BBH tables and 62/72/86% example accuracy, Self-ICL 50.81/53.93/55.49 and Temporal Sequences 57.6 to 35.6, TP shortest path 0.33/0.26/0.22/0.65, Zhang 2026 AP 56.0 vs CoT 60.7.
5. Yasunaga Table 1 caption: for text-davinci models the authors used an in-context demonstration of how to generate exemplars; other models got none. So the davinci rows are not the same prompt as the GPT-3.5 row.

## Contradictions between sources
- Yasunaga (GPT-3.5, GSM8K 77.8, MATH 37.3) versus Qin (same model, relevant 71.5 / 33.3, N/A 75.5 / 36.1). Qin's relevant arm is below Yasunaga's 0-shot (75.0). Qin used 500-item subsets, 3 seeds and its own prompt wording, and never re-ran Yasunaga's baselines, so the gap is not isolated. On BBH Qin finds a small win for relevant (63.2 vs 61.9).
- Zhang 2026 finds analogical prompting 4.7 points below CoT on average (MATH -12.9) on three modern backbones, with near-identical deltas. This is third-party, unclear prompt, and the identical deltas look like a shared implementation effect.
- Gwak 2026 finds a gain only when recall and solve are in one prompt, which conflicts with the idea that the recalled examples carry the value; Qin finds example accuracy matters. These can both hold if the gain is a process effect that is hurt by wrong content.

## Weak spots
- The founding paper has no seeds, no intervals, one prompt wording, 2023 models. Gains of 1 to 2 points on GSM8K are inside plausible noise. Codeforces uses 50 problems.
- No study found that matches tokens against CoT with self-consistency (Yasunaga's own self-consistency add-on reached 85.3/46.0 but is a different arm).
- No test on reasoning-trained models (o-series, Claude thinking) with this prompt; Gwak uses strong chat models but low absolute GSM8K (about 50), so its prompt format is probably restrictive.
- Most "support" is from authors' own methods (Thought Propagation, Cognitive Tools bundle, Self-ICL). Cognitive Tools isolates recall only in one ablation (Qwen2.5-32B 79.6 to 84.2; Llama3.3-70B 52.8 to 75.1) inside an agent loop.

## Only seen in snippets or abstracts
a25 (Gick and Holyoak numbers not verified), b24/c21 (Lee et al., abstract/intro), b25/c23 (abstract numbers), b26, b27 (citation lists), c19, c22, c26, c27 (abstract level), b11 CodeSim (garbled table extraction, block-to-model mapping uncertain), b20/c17 (accuracies in figures). Webb et al. (a24, c16), Hu (c18), AnaloBench (c20) were not re-opened this pass.

## GAPS (most decision-relevant first)
1. At equal total tokens, does recall-then-solve beat plain CoT and CoT with self-consistency on a modern (reasoning or strong chat) model? No paper has measured this.
2. Is the gain from relevance of the recalled problems, or only from extra generation? Qin says irrelevant (N/A) is as good or better in math; Yasunaga says diverse relevant beats non-diverse. A clean three-arm test (relevant, unrelated, nothing) with the same wording is missing.
3. Does Gwak's Integrated-vs-Decoupled result replicate, and does it hold on a scaffold where recall is a separate state (S3)? This decides how S3 must be implemented.
4. Does a verification pass on recalled problems (re-solve and compare) recover the accuracy loss Qin links to wrong examples, and at what token cost?
5. Why do Zhang 2026 and CodeSim find analogical prompting below CoT? Need the exact prompts used and a rerun with Yasunaga's published prompt.
6. How does the method behave on counterfactual or novel-rule variants (Lewis and Mitchell style), where recalled analogies from training data may mislead?
7. Does cross-domain recall (distant analogies, 2026 science paper) beat same-type recall on open or creative tasks, with blind judging?
8. What is the loss tail by task type? Self-ICL shows drops up to -22 points on some tasks; which task features predict harm, so the agent can gate the operator?
9. Do the gains hold on newer benchmarks less likely to be contaminated (fresh Codeforces, post-cutoff sets)? Yasunaga used 2023 level-A problems only.

## Gap search results (2026-11-10, evidence_d.jsonl d01-d19)
Tools: 6 web searches, OpenAlex citation scan, direct PDF reads (Qin, Gwak, Zhang, Luo et al. LBS3, Wang et al. 2025 on reasoning-model demos, Wang et al. 2024 budget-aware, Michelman et al., Shen et al., Lewis and Mitchell). arXiv and Semantic Scholar APIs were rate-limited.

1. Equal-token comparison vs CoT and CoT-SC on a modern model: STAYS OPEN. Partial hints only: Qin Table 12 (Llama-3.1-8B GSM8K: relevant recall 74.8, SC5 77.6, fixed correct set 80.2-81.0, not token-matched); Zhang 2026 (CoT-SC above AP by 6 points average); budget-aware paper shows CoT-SC wins at equal 10k tokens over other strategies but does not include AP. On reasoning-trained models, worked demos hurt (AIME'25 -6 to -35 points), so a test there is the priority. (d05, d08, d12, d14)
2. Relevance vs extra generation: MOSTLY CLOSED for math on 2023-24 chat models. Qin runs relevant / N/A / random-same / random-diff / random-bio on 5 models; relevant is worst each time (GSM8K Llama-3.1-8B 74.8 vs 77.3-78.8). Caveat: no zero-shot arm in the same table, and relevance is confounded with example accuracy. Not independent (one lab). (d02, d03, d04)
3. Integrated vs Decoupled: HALF CLOSED. Re-read: holds on 5 models and 1/2/4 shots inside Gwak; no second group; no test with S3 as a separate state. Design implication stays: keep recall and solve in one stream. (d06, d07)
4. Verification of recalled problems: PARTLY CLOSED. An outside check (GPT-4 answers) lifts relevant arm 71.2 to 75.2 (GSM8K) and 37.0 to 44.4 (MATH); Llama-2-70B 56.2 to 60.8. Same-model re-solve check and its token cost: still open. (d01)
5. Why Zhang and CodeSim fall below CoT: STAYS OPEN. Zhang gives no prompt in the paper; identical CoT averages across backbones (60.7 vs 60.4) hint at a shared harness. New independent data (Luo et al.) show AP below ZS-CoT on three open models and above it on GPT-3.5/4-turbo, so a model-strength explanation is plausible. (d08, d09)
6. Counterfactual or novel-rule variants: STAYS OPEN. No paper runs AP on them; Lewis and Mitchell test only zero-shot models. (d17, d18)
7. Distant vs same-type recall on creative tasks: PARTLY CLOSED. Shen et al. 2026: cross-domain analogy search beats domain-constrained search on novelty (50-69% vs 22-38%) and diversity, humans agree 78% (kappa 0.445), same call count as the cross-domain baseline. No same-type arm; correctness not measured. (d16)
8. Loss tail by task type: PARTLY CLOSED. Losses concentrate on short-answer symbolic BBH tasks (raco -28 and -15 points on Qwen-72B and Llama3-70B; ts -8) and on weaker open models; Gemini 1.0 also loses on Tracking Shuffled Objects. May be answer-format failure, not reasoning harm. (d09, d10, d15)
9. Fresh, post-cutoff benchmarks: STAYS OPEN. Nothing found; only snippet-level background on contamination. (d04 GPQA/MBPP are small and noisy; d18, d19)

New claims: K17-K23. Statuses changed: K02 independent_sources 2 to 3 (still contested); K01, K03, K08, K10, K16 got gap-search notes and evidence (status unchanged). K19 (model-dependence of AP) is established across three groups.
Still only abstract or snippet level: d19. Garbled tables not quoted: Michelman cells, Lewis and Mitchell Table 4 row labels.
