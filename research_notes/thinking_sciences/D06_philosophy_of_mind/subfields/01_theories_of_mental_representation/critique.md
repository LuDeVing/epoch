# Critique: D06.01 Theories of mental representation

## Corrections and confirmations (sources re-opened via arXiv PDF text, 2026-11-03)
Confirmed exactly: Li et al. 2210.13382 (0.01%, 5.17%, 93.29%; interventions 0.12 vs 2.68 and 0.06 vs 2.59); Nanda et al. 2309.00941 (MINE/YOURS 90.9 to 99.6 peak; null 2.723, linear add 0.10); Hewitt and Liang 1909.03368 (97.3/92.8; linear 97.2/71.2/26.0); Vafa et al. 2406.03689 (shortest paths validity 1.00, probe 0.91, compression 0.10, distinction 0.35; noisy 0.05/0.37; detour 0.99, 0.69, 0.08); Karvonen 2403.15498 (99.8%, 99.6%, 46%, 64%, probe 99.6 vs random 74.7, skill 90.5 vs 69.3, intervention 92.0 vs 40.5); Levinstein and Herrmann 2307.00175 (five of six probes worse than chance; CCS 50-57%); Gurnee and Tegmark 2310.02207 (0.911, 0.864, 0.359 for 70B); Mancoridis et al. 2506.21521 (94.2%, 0.55/0.40/0.40, 0.62); Hao et al. 2305.14992 (RAP 1.00/0.86/0.26 and 1.00/0.88/0.42); Shai et al. 2405.15943 (R2 0.95 vs 0.31). Farquhar et al. 2312.10029: Banana/Shed and Alice setups confirmed; the exact 50% chance figure was seen only in text near the setup, figures not re-read.

Corrections and clarifications:
- a11 says linear MINE/YOURS peak 99.6%; b05/b06 say 99.5% at layer 8. Both are right: 99.6 is the peak (layer 7), 99.5 the last layer. Use "99.5-99.6".
- a18 RSA table is marked garbled; the range 0.16-0.33 is not trustworthy. Use only the baseline figures (fastText 0.23, PMI 0.11-0.17).
- Chess: legal-move rate 99.8% is for free play; 40.5% is legal moves on an edited board without the intervention. Do not compare them.
- Othello always-guess baseline appears as 52.95% (main text) and about 47% (appendix); the source disagrees with itself.
- b13 and b22 were not opened (opened:false); a07 (Fodor and Pylyshyn) not opened.

## Contradictions between sources
- Li et al. (linear probes fail) vs Nanda et al. and Hazineh et al. (linear works with mover-relative coding). Resolved: coding choice.
- Marks and Tegmark (linear truth direction generalises) vs Levinstein and Herrmann (fails on negation) vs Farquhar (unsupervised finds salient features). Partly resolved by scale and data diversity; unsupervised truth discovery refuted for CCS.
- Othello world model: Li et al. say yes; Vafa et al. find the model trained on real games fails compression and distinction. Same model, different criterion (probe vs behavioural coherence).
- Platonic convergence (Huh) vs weak colour alignment numbers (Abdou).

## Weak spots
- Almost all empirical work tests the informational criterion, some the consumer-use criterion, and almost none misrepresentation. The philosophy-to-LLM mapping is our own synthesis (a24), not tested.
- Open-weight models only (Llama-2, small GPTs). No result about frontier prompted models and S2-style restatements except Vafa seating and potemkin.
- Philosophical papers (Bender and Koller, Piantadosi and Hill, Mollo and Milliere) give no numbers; independence among them is low (they cite each other).
- No scaffold-level study: nothing measures whether better stated representations raise accuracy at equal tokens.
- Original primary works (Fodor, Dretske, Millikan, Block) known only through SEP summaries.

## Seen only in snippets or abstracts
Slocum et al. (c24, abstract level), Park et al. linear representation (c17, no numbers), Yildirim and Paul (b22), Levinstein original rebuttal text of Marks (b13).

## GAPS
1. Does an explicit S2 state (typed slots: entities, relations, hidden variables) raise accuracy at equal tokens over free restatement for frontier prompted models? (No direct study found.)
2. Does a use-check (apply the stated concept to a fresh instance) close the potemkin gap, and at what token cost?
3. Do compression and distinction failures (Vafa) occur in prompted frontier models on long multi-step tasks, and does re-stating state each step fix them?
4. Which frame helps the consumer: actor-relative (MINE/YOURS) vs absolute restatement, in text reasoning tasks?
5. Can an LLM detect misrepresentation in its own earlier restatement (criterion c), and how often?
6. Do 2025-2026 interpretability results (causal intervention, steering) replicate Othello/chess world models in frontier models, and do any contradict them?
7. Does self-consistency or internal-agreement signal fail under distractor features in behavioural (non-probe) settings, as Farquhar shows for probes?
8. How much does representation of hidden variables (belief-state style, weighted hypotheses) improve decisions over a single best guess?
9. Primary-source check: Fodor/Dretske/Millikan/Block claims on disjunction and Swampman as used by Mollo and Milliere; is selection-history grounding testable by a fine-tuning vs prompting contrast?


## Gap search results (2026-11-03)
Method note: WebSearch budget was exhausted and the arXiv, Semantic Scholar and OpenAlex search APIs returned rate-limit errors, so papers were found from prior knowledge and opened as arXiv PDF text (and SEP pages). No search-based discovery was possible; coverage is therefore narrower than a full literature search. Evidence is in evidence_d.jsonl (d01-d18); claims K21-K28 added, K19 and K20 updated.

- Gap 1 (typed S2 slots vs free restatement at equal tokens, frontier models): STAYED OPEN. Nearest evidence: Chain-of-Symbol (d10) shows a compact symbolic state gives +60.8 points on GPT-3.5 Brick World but only +2.3 (GPT-3.5) and +2.8 (GPT-4) on natural SPARTUN; entity tracking (d11) needs code-trained models. No frontier ablation found. Claim K25.
- Gap 2 (use-check closing the potemkin gap): STAYED OPEN. The potemkin paper (already in claims) names mitigation as future work; no study of an apply-to-fresh-instance check with token cost found. Related: self-verify prompting does not fix self-conditioning (d02), and same-model review is weak (d04, d05), so the check should use an independent instance.
- Gap 3 (compression/distinction failures in prompted frontier models on long tasks; restate each step): PARTLY CLOSED. Long-horizon failure and self-conditioning are measured (d01, d03); a sliding window or thinking mode mitigates it (d01, d02). Compression and distinction metrics themselves were not applied to frontier models, and no run tests a state restatement as the fix. Claim K21.
- Gap 4 (actor-relative vs absolute frame in text tasks): STAYED OPEN. Only the Othello probe-coding result (already in claims) exists; no text-reasoning comparison found.
- Gap 5 (can an LLM detect misrepresentation in its own earlier restatement): PARTLY CLOSED. Evidence says poorly without an outside signal: intrinsic self-correction hurts (d04), mistake finding 39.8-52.9% for GPT-4 on others' CoT (d05), explanations can rationalise biased answers (d07); P(True) calibration is better for answers (d06). All are 2022-2023 models; no test on restatements and no 2025 frontier figure. Claims K22, K23.
- Gap 6 (2025-2026 interpretability replications in frontier models): PARTLY CLOSED. Extensions found (d12 lookback belief tracking up to Llama-3.1-405B; d13 belief intervention in Mistral-7B; d14 seven-model Othello alignment up to 99%). None contradict the earlier results, none cover closed frontier models. Claim K28.
- Gap 7 (self-consistency/internal agreement failing under distractors, behaviourally): PARTLY CLOSED. Behaviourally, self-consistency helps but does not fully fix distractor failure (d08: LTM+SC micro 93.4%, macro 45%); biasing features corrupt CoT (d07). Probe-style failure (Farquhar) does not carry over directly. Claim K24. Models are 2022-2023.
- Gap 8 (hidden-variable belief state vs single guess): PARTLY CLOSED. Prompted LLMs plateau near single-guess behaviour (36-58% vs Bayesian 81%) and CoT does not help; fine-tuning on Bayesian outputs does (d09). No prompt-only scaffold test of weighted hypotheses. Claim K26.
- Gap 9 (primary-source check; fine-tuning vs prompting contrast): PARTLY CLOSED. SEP pages confirm Fodor 1984 disjunction problem, Dretske 1981/1988, Davidson 1987 Swampman, and that selection may include learning (d16, d17). Mollo and Millière (d18) use selection history but never use the words Swampman or disjunction in the text searched, so the earlier note that they use these terms should be read as the SEP-level concepts. Original books by Fodor, Dretske, Millikan, Block still unopened. Slocum et al. (d15) is the nearest prompt-vs-training contrast but is not a test of the theory. Claim K27.

Items still unverified in this pass: Kadavath numbers (abstract-level only, d06), Prakash IIA values (figures), Zhu et al. table values (extraction garbled), Qiu per-model accuracies (figure text garbled).

Net: no gap fully closed. Strongest new result for the schema is K21 (restatements copied forward from a wrong step propagate the error) and K22 (same-model self-review is weak, so give locating hints or an independent check).
