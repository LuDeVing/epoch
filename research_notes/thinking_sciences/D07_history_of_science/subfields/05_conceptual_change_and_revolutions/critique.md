# D07.05 Conceptual change and revolutions: cross-check critique

Checked 2026-11-10. Sources re-opened (full PDF text via pdftotext, or PMC HTML): Huang et al. 2024 (2310.01798), Wilie et al. 2024 Belief-R (2406.19764), Wang et al. 2024 Hypothesis Search (2309.05660), Agarwal et al. 2025 AutoDiscovery (2507.00310), Smith 2026 Little Scientist (2608.16951 v2), Xie et al. 2024 (2305.13300), Jansen et al. 2024 DiscoveryWorld (2406.06769), Qiu et al. 2024 (2310.08559), Shinn et al. 2023 Reflexion abstract (2303.11366), Schroeder and Kucera 2022 (PMC8784251).

## Corrections made

1. b07 (Huang) is wrong on the oracle numbers. It says "GSM8K 75.9 -> 95.5 (GPT-3.5) and 84.3 -> 97.5 (GPT-4)". Table 2 of the paper says: GPT-3.5 GSM8K 75.9 standard, 84.3 with oracle; GPT-4 GSM8K 95.5 standard, 97.5 with oracle. Correct pairs: CommonSenseQA GPT-3.5 75.8 -> 89.7, GPT-4 82.0 -> 85.5; HotpotQA GPT-3.5 26.0 -> 29.0, GPT-4 49.0 -> 59.0.
2. c09 (Huang) says "GPT-4 HotpotQA 29.0 standard to 59.0 oracle". Correct: GPT-4 49.0 -> 59.0 (29.0 is GPT-3.5 with oracle). The no-oracle fall 49.0 -> 43.0 after 5 calls is right.
3. c07 labels columns "rounds 1/3/5 calls". Table 3 uses number of calls: 1 = initial answer, 3 = after self-correct round 1, 5 = after round 2. So CommonSenseQA 75.8 -> 38.1 is after ONE round and 41.8 after two. b07 had this right. Confirmed: GPT-3.5 GSM8K 75.9/75.1/74.7; GPT-4 GSM8K 95.5/91.5/89.0; GPT-4 CSQA 82.0/79.5/80.0.
4. c18 (AutoDiscovery) says Bayesian surprise "correlates 0.67" with human surprisal. Table 2 reports 0.67 as the mean human surprisal rating (vs 0.11 for direct LLM surprisal, 1,620 hypotheses, 3 annotators each). The paper's own text calls it a "correlation (67%)", which is loose wording. Treat 0.67 as an average rating. The separate "67% of surprising discoveries also surprise experts" (500+ hypotheses) is a different statistic; the coincidence of 0.67 and 67% invites mix-ups.
5. b02 I2 is 60.8% in b01; the PMC page shows 60.7% in the visible text (rounding). Immaterial. g=0.41, CI [0.30,0.51], n=3,869, 44 comparisons, trim-and-fill g=0.28 CI [0.16,0.39] confirmed.
6. c11 (Reflexion): HumanEval 91% vs 80% confirmed in the abstract. The "+22% AlfWorld, +20% HotPotQA, +11%" figures are NOT in the abstract text I read; keep them as unverified.

Confirmed unchanged: Belief-R GPT-4-Turbo DP 19.65/82.69/51.17 and Llama-3 70B 10.99/92.09/51.54 (BU/BM/BREU); Hypothesis Search 17% direct, 23% program, 30% LLM summaries, 33% human pick, 33 of 49 (67%) correct programs, SyGuS 94.3%; Xie ChatGPT 3.7 / 99.8 and GPT-4 8.9 / 99.8, 80% memorisation for GPT-4; DiscoveryWorld 38% / 18% / 34% / 8%, humans 66%, 11 of 16 tasks over 60%, knowledge 55%; Qiu ACRE 28.0 IO, 45.0 (T=1,N=1), 59.0 (T=3,N=5), MiniSCAN 0.0 -> 46.0; Smith 2026 B 0.8027, G 0.8612, L 0.8906 (+0.1159), H 0.8463, HG 0.8455, 7 of 10 arms fail, 17 of 64 improved (26.6%), Kuhn agent 63 runs 33.5M tokens of 229.0M, DALE 0.842 vs 0.803 on 132 TFs, wins 89/43.

## Contradictions and tensions

- Hypothesis Search (parallel frames help on ARC) and Smith 2026 (full loop scaffold loses to one-shot sampling) point in different directions. They may agree: sampling several candidate frames and selecting with an external test works; wrapping that in a heavy reasoning loop does not. Selection among draws is what pays.
- Reasoning-model "aha" (c12) is shown as an RL by-product with no controlled test that rethinking causes the gain; the Illusion of Thinking paper (c13) shows overthinking and collapse. So reconsideration is not free.
- Refutation text helps humans (g 0.41 or 0.28) but the LLM transfer is untested. Huang shows that telling an LLM its answer might be wrong does not help. Different mechanism, no bridge.
- Belief-R: models that update well fail at maintaining beliefs; this cuts against any scaffold that simply raises the revision rate.

## Weak spots

- No LLM study isolates a Kuhn-style anomaly-count threshold. Smith 2026 uses "N consecutive non-improving iterations", but the Kuhn agent was never an ablation arm (marginal effect unmeasured), and it is a single independent-author preprint.
- The human-science side relies on encyclopedia and review pages. Primary papers Bruner and Postman 1949, Posner 1982, Chinn and Brewer 1993, Dunbar 1997, Shtulman and Valcarcel 2012, Kulkarni and Simon 1988, Vosniadou and Brewer 1992 were NOT opened (a07, a11, a12, b15, b26, b27, b28, c25, a10 via review). Their numbers are unverified. a07 figures are from memory.
- Kuhn's oxygen case: SEP itself calls it stretched. No replication-style quantitative test of the Kuhn cycle exists.
- Child-science conceptual change studies use different populations (5-year-olds, N=102) and may not transfer to a model.
- Claim counts of "independent sources" are conservative; many LLM items share a single paper.

## Only seen in snippets or abstract pages

c23 (Thagard 1989, abstract page), c25 (KEKADA, blocked), a27 (refutation meta-analysis, not opened), a28 (ECHO, not read), b14 (secondhand), b04 (secondhand via Schroeder).

## GAPS

1. Does reframing triggered after N consecutive failed external checks beat reframing at the first failure and beat best-of-N one-shot sampling at equal tokens? (No study isolates the trigger count; Smith 2026 did not ablate the Kuhn agent.)
2. What does the Smith 2026 Kuhn agent actually add on top of the loop? Is there a later version or code with a Kuhn on/off arm?
3. Does refutation-style reframing (name old frame, say why it fails, state new one) help LLMs beyond plain "try a different approach"? Any 2023-2026 test in prompting or in-context learning?
4. How do LLMs behave when kept with two rival frames and scored by an explanatory-coherence tally (ECHO-style)? Any LLM test of coherence-based theory choice?
5. What are the exact numbers in Chinn and Brewer 1993 and Dunbar 1997 (how often scientists ignore, reinterpret or change the model, and after how many anomalies)? Needed to set a counted threshold with human data.
6. Are there replications or failures to replicate the persistence of outdated information (Johnson and Seifert, O'Brien, Kendeou KReC) and does the effect appear in LLM context windows (old claim still used after a correction)?
7. Does the Huang et al. result (intrinsic self-correction hurts) still hold for 2025-2026 reasoning models with tools, and when does a model-judged anomaly signal become reliable (calibrated surprise)?
8. Can the Bayesian-surprise signal (AutoDiscovery) be used as a cheap impasse detector for a single-answer task, and what is its cost in samples versus a failed-test signal?
9. Counterfactual-task drops (Wu et al.): do they recover when the agent is told to restate the task under the new frame first? Any measured effect of an explicit frame-restatement step?
10. What is the failure rate of "flip-everything" bias: for a reframe operator, what share of correct first answers get wrongly overturned (Belief-R BM-type loss) at equal tokens?


## Gap search results (2026-11-10, evidence_d.jsonl d01-d20)

Tool limits: WebSearch budget was spent before the first call, and the arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429. Work used arXiv PDFs by known id, Crossref, Europe PMC, PMC, and GitHub raw files. Absences below are "not found", not "proven absent".

Corrections confirmed or added
- Reflexion: the +22% AlfWorld, +20% HotPotQA, +11% HumanEval figures ARE in the paper's own intro and results text (d05). K05 is now established. Its trigger heuristic is counted (same action and response more than 3 cycles, or more than 30 actions; stop after 3 consecutive failures) and was never swept.

Closed
- Gap 2 (Smith 2026 Kuhn agent): closed as "no on/off arm exists". arXiv v2 (3 Nov 2026) is latest, no v3. The repos show the Kuhn trigger is 5 or more consecutive non-crashing rejections and that the violated assumption and imported domain are assigned externally (d08).
- Gap 10 (flip-everything loss): measured, not for our operator. FlipFlop: 46% mean flip, 17% mean drop, GPT-4 flips 10.4% of correct and 30.3% of wrong answers (d03). Snell: about 38% of correct answers overturned by naive revision (d04). Self-Contrast: toxic reflections 52 -> 11 with contrast (d06). Selection or contrast of two frames cuts the loss.
- Gap 7 (Huang vs reasoning models): mostly closed. Self-Correction Bench shows a 64.5% blind spot for non-reasoning models on their own errors, near zero for reasoning models, and 'Wait' gives DeepSeek-V3 0.567 -> 0.902 vs R1 0.908 (d01, d02). Huang's result is conditional on model type. Still open: calibrated anomaly judgment with tools on open-ended tasks.

Partly closed
- Gap 3 (refutation-style reframing): no 2023-2026 test of name-old-frame refutation. Nearest: Reflexion explain-failure beats plain retry (HotPotQA +8%; Rust 0.68 vs 0.60, n=50) and Self-Contrast (d05, d06). Both need an external failure signal.
- Gap 6 (persistence): human side extended. Meta-analysis persistence d=0.75 to 1.06 (52 samples, N=6,878); backfire replication N=1,156 found none; person-impression persistence is inconsistent (1 of 3) (d10-d12). Johnson and Seifert, O'Brien and KReC primary papers still unopened. No LLM context-window test found.
- Gap 9 (frame restatement): Wu's comprehension check is passed by GPT-4 while the counterfactual task still fails (d09). No restate-then-solve arm exists. Open.
- Gap 8 (Bayesian surprise as impasse detector): cost facts only (two belief-sample sets plus the experiment; boolean elicitation biased; 100 experiments about 8 h) (d14). No comparison with a failed-test signal. Open.
- Gap 1 (trigger count N vs first failure vs best-of-N): still no study varies N. Snell gives a difficulty-dependent sequential/parallel split at equal compute (d04); Reflexion and Smith use fixed N (d05, d08). Open.

Still open
- Gap 4 (ECHO-style coherence tally with LLMs): nothing found (d20).
- Gap 5 (Chinn and Brewer, Dunbar counts): publisher pages blocked or no abstract (d15, d16). Not opened; no numbers.

New claims K25-K33 in claims.jsonl. Statuses changed: K05 single-source -> established; K04 independent sources 3 -> 5; K29, K31, K33 added as open.
