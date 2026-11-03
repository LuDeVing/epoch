# Critique: A11.06 Logic and philosophy of analogical arguments

## Checks made (sources re-opened this session)

1. Lewis and Mitchell (arXiv 2402.08955, Table 2). The table text is shifted by one row. Read with the labels aligned: humans 0.753, GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 (136 humans, 1,876 human samples). a17 CONFIRMED. The extended paper (2411.14215) uses 263 humans for letter strings and 301 for digit matrices: b12/b13 CONFIRMED. Note a17 (136) and b12 (263) are two different samples, not a conflict.
2. Lewis and Mitchell Table 4/5 (answer order, paraphrase). Row labels are shifted too. Correct reading: GPT-4 from Webb's data 0.89 (16/18) first, 0.61 (11/18) second, 0.75 total; GPT-4 in their own run 1.0 first, 0.72 second, 0.86 (31/36) total; humans 0.78 in both orders (no order bias). Paraphrase: GPT-4 0.86 to 0.72, humans 0.78 to 0.70. b14 CONFIRMED. a18 only gives the Webb-data pair and is consistent. CORRECTION: the paraphrase effect is based on 18 stories; the authors say it is not clearly significant.
3. Webb, Holyoak and Lu 2023: digit matrices OR=1.88 (p=0.005, CI 1.21-2.91); multiple choice OR=6.27 (p=2.3e-8, CI 3.28-11.99); story analogies t(53)=21.3 overall, far t(53)=16.7, GPT-3 far p=0.065, OR=0.37 p=0.0003 CI 0.21-0.63, 15/54. All CONFIRMED. Small correction: the near-analogy human statistic is t(53)=21.5.
4. Stevenson et al. 2025 (arXiv 2411.02348): adults N=62 0.88/0.91/0.89; children N=41 0.62/0.66/0.67; GPT-4o 0.85/0.63/0.48; Llama-3.1 405B 0.79/0.74/0.27; Claude-3.5 0.68/0.62/0.46 (N=54 each). CONFIRMED. Note c12 had the Claude-3.5 final value cut off; it is 0.46.
5. AnaloBench (EMNLP 2024) T1: Claude 68.2/30.2/25.9; GPT-3.5 65.3/46.4/30.8; GPT-4 89.1/66.5/60.7; human 96.0/72.5/73.3 at 1/10/30 sentences. CONFIRMED. Claude at 30 sentences (25.9) is at chance (25).
6. Qin et al. 2025 (arXiv 2404.12728). CORRECTION to c10: the "failed replication" label is too strong. Relevant self-generated examples DO help on BBH (+1.3% over no-example, average 63.2 vs 61.9 for random-same); they fail on GSM8K and MATH, where every random type beats relevant and no-example is best on average. The "+2.5%" is an average over GSM8K and MATH for random biological over relevant; the abstract's 4% is the GSM8K figure. Treated as a partial replication failure.
7. Hodel and West: 121 UW undergraduates, 50 GPT-3 instances; synthetic alphabet accuracy under 0.1 for four problem types; only "remove redundant letter" and "sort" stay near the original. a16 CONFIRMED and now has the human N.
8. Yasunaga et al.: +4% average gain confirmed from the introduction (arXiv 2310.01714). Per-cell Table 4 values were not rechecked.
9. Calvo Figueras and Agerri (arXiv 2505.11341): paper opened; the "no model above 57% Useful" figure was not re-located in this pass.
10. Webb reply (c05): GPT-4 plus code execution vs humans P=0.496, 46% (23/50) of GPT-4 errors used a valid alternate rule: not re-opened.

## Contradictions between sources

- Webb 2023 says GPT-3 has emergent analogy ability; Hodel and West, Lewis and Mitchell and Stevenson show it fails on surface-changed versions. Webb's reply (c05) says GPT-4 with code gets there. Resolution so far: pattern matching on familiar surface forms plus a weak ability to infer rules; code execution may remove the gap.
- Yasunaga (relevant self-generated analogues help) vs Qin (random ones help as much on math). The unresolved question is whether relevance matters or whether the gain comes from extra reasoning text and example accuracy.
- Qin find irrelevant examples harmless on math, while Shi et al. (c15) find irrelevant sentences in the problem hurt. Different manipulations (example vs problem text), so not strictly contradictory, but it weakens a simple "filter irrelevance" check.
- ARN numbers are inconsistent between lines in the evidence files: b16 gives overall humans 96.0 and models 57.3, c07 gives humans 94.1 on far analogies and models 39.6. These are probably different columns (overall vs far, average vs a single model), but this was not verified. b17 gives GPT-4 zero-shot mean 68.1 while b16 says GPT-4 is below chance on far analogies: these can both hold only if 68.1 is a mean over near and far. Treat the ARN far-analogy numbers as unverified.

## Weak spots

- The philosophy side rests almost entirely on one secondary source (the SEP article by Bartha) plus Norton's draft chapter. Hesse 1966 and Bartha 2010 were never opened (c19, c20 opened:false). Claims K04 to K07 are therefore not independent.
- The central question for the guardrail (can a model or code apply the Hesse/Bartha criteria?) has zero direct studies (K18). Everything LLM-related is indirect: it tests analogy solving, not analogy-strength judgement.
- No test of a causal-link checklist at equal tokens exists anywhere in the evidence.
- Several numbers come from abstracts only (b22, b23, c04, c23, c26 not opened).
- SEP was read through a summariser for part of the text (c18); the V1/V2/H1/H2 labels were not seen.
- All human samples are Western students or Prolific workers; the children data (K09) is one lab.

## Seen only in snippets or not opened

c04 (Hodel and West is now opened by me, so c04 can be upgraded), c19, c20, c21, c23, c26, b22, b23 (abstract only).

## GAPS (most decision-relevant first)

1. Does giving an LLM a Hesse/Bartha checklist (causal link, no essential difference, prior association, potential for generalisation) improve its accuracy on judging classic analogical arguments against philosopher verdicts, at equal tokens? No study found.
2. Does a code-checked typed mapping with a causal-direction field (generative vs preventive) beat model-judged similarity on transfer problems at equal tokens? (McKay-style items.)
3. Is the gain from analogical prompting due to relevance or to accuracy and length of the extra text? Qin et al. versus Yasunaga needs a matched-token test with accurate-but-irrelevant examples.
4. Does GPT-4-class and newer reasoning models' failure on counterfactual letter-string and far-story tasks persist in 2025-2026 reasoning models (o-series, Claude, Gemini thinking)? Most measured models are GPT-3 to GPT-4o.
5. Can code verify determination-rule transfer (Davies-Russell) in practice: how often do real tasks have a known determinant set?
6. Do the answer-order and paraphrase biases (Lewis and Mitchell, 18 stories only) hold on larger story sets, and does order-swap voting in code remove them?
7. What are the actual ARN far-analogy numbers per model (humans 94.1 vs models 39.6 vs 57.3 overall)? Re-open the paper and fix the table.
8. Does the Hesse/Bartha view say anything testable about when analogical prompting hurts (negative analogy in the retrieved exemplar), e.g. does a known essential difference between exemplar and target lower accuracy?
9. Do critical-question checklists (Walton) written by humans raise argument-from-analogy judging above the 57% Useful ceiling seen for model-generated questions?
10. What is Hesse's and Bartha's own evidence for their criteria in historical cases (Norton's successes and failures: Galileo, canals, caloric)? Open the primary books or Norton's full chapter to build a labelled case set.

## Gap search results

Evidence in evidence_d.jsonl (d01 to d18). Search limits: WebSearch budget was spent, and the arXiv API, Semantic Scholar and OpenAlex were rate limited, so I used arXiv search pages, arXiv PDFs and the SEP page. Hesse 1966 and Bartha 2010 books were still not opened.

1. OPEN. No study tests a Hesse or Bartha checklist on LLMs. arXiv search for "argument from analogy" plus language models gave 0 hits (d10). Claim K24.
2. PARTLY. No code-typed causal-direction mapping test exists. Nearest: OpenLock causal transfer with 2026 models (d07): only Gemini-3-Flash transferred significantly; GPT-5.2 favoured common cause over common effect, humans did not. Supports a causal-direction field but does not test it. K22.
3. CLOSED (for math). Qin et al. controlled accuracy: MATH examples correct 62.0% (relevant) vs 72.0% (N/A) vs 86.0% (random); verified fixed examples 56.3 avg vs relevant 52.4 (d03, d04). Accuracy, not relevance, drives the gain. Boundary: GPT-3.5, math; on BBH relevant did help. K12 stays contested for non-math tasks.
4. PARTLY. The Lewis-Mitchell paper has one version and tests GPT models only (d09). Frontier 2026 models still fail far-analogy ARCANA (GPT 5.2 about 48-51% pass@3, Claude Opus 4.5 7-9%, d08) and OpenLock transfer (d07). Standard letter-strings are easy for 2026 models (d11). No counterfactual letter-string run on reasoning models found.
5. PARTLY (in principle only). SEP: determination rules are rarely known; animal drug testing is the example (d17). No frequency data. K06, K23.
6. OPEN at scale. Still only 18 stories (d15). General position bias is documented in 20 LLMs (d14), so order-swap voting is plausible but unproven for analogy. K25.
7. CLOSED. ARN Table 2 re-read (d01): far-analogy mean humans 94.1 vs models 39.6; near 97.9 vs 75.0; overall humans 96.0 vs models 57.3; GPT-4 overall 68.1. The earlier numbers were different columns of the same table, not a conflict. Partition values: 76.9 / 73.2 / 45.3 / 33.9.
8. PARTLY. No direct test with a known essential difference. Indirect: GPT-4 accepts wrong source stories (precision about 0.50, d06). K21.
9. PARTLY. Walton-template reference questions exist, and task-specific systems are about 10 points above the 57% zero-shot ceiling (d05). Not tested on argument from analogy alone. K17.
10. PARTLY. From SEP only (d16): Hesse's cases are heat as fluid flow (failed when heat was not conserved) and Franklin's lightning; Galileo's moon mountains is Norton's case. Canals case not found. A labelled case set needs Norton's chapter or Hesse 1966 directly.

Net: closed 3 (math part) and 7; no gap fully closed for the guardrail question itself (1, 2, 8). New claims K21 to K25.
