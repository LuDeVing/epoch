# A02.09 cross-check

## Corrections made (sources re-opened this session: arXiv PDF text and the ERIC PDF)
1. Plan-and-Solve error shares: paper says calculation 7%, missing step 12%, semantic 27%. Record a19 (and a28) said missing step 27%. Wrong; corrected in claim K09. b14 and c05 were right.
2. Step-Back MMLU 73.2 / 81.8, PaLM-2L base 66.4 / 70.9, CoT 65.0 / 75.3, fixes 20.5% / introduces 11.9%: confirmed.
3. Least-to-most SCAN length split 99.7 vs CoT 16.2 vs standard 16.7: confirmed.
4. Huang et al. self-correction (GPT-3.5 GSM8K 75.9, 75.1, 74.7; CommonSenseQA 75.8 to 38.1; GPT-4 to 89.0): confirmed.
5. FOBAR: GPT-3.5 86.6, GPT-4 91.4, davinci 83.5 confirmed. GPT-4 Self-Consistency is 91.1 (CoT prompts) and 91.6 (ComplexCoT, vs FOBAR 91.9). a23's "FOBAR highest on all three" holds only by tiny margins; treat the GPT-4 gain as noise.
6. Rott: 27 of 32 wild-goose-chase processes had no/basic access, 5 advanced; others 16 vs 40; chi-square 25.378. The table says p<0.0001, running text says p<0.001. "Wild goose chase" is Rott's own operational rule (only exploration/execution, no analysis), so the link to success is partly built in. Schoenfeld's 60% to 20% is confirmed only as a quote inside Rott.
7. Self-Discover: 10-40x less compute, 74.7% of MATH failures are computation errors, 25.3% structure: confirmed.
8. GSM-Symbolic: up to 65% (Phi-3-mini), o1-preview -17.5, o1-mini -29.1, GPT-4o-mini -40.0: confirmed (figure labels).
9. Gandhi: b03 says "identical" for incorrect-vs-correct priming; the paper says comparable. Empty CoT: Llama stays 30-35%, Qwen hurt. Countdown only.
10. USAMO 24.4% (Gemini-2.5-Pro), others under 5%; RevThink 13.53 / 6.84 / Mistral 63.23: confirmed.

## Contradictions and oddities
- Step-back: no gain on GSM8K (84.3 vs 84.4) but large gains on physics and TimeQA. Task dependence, not a contradiction.
- Yasunaga (c08): text-davinci-003 14.8 to 61.0 and PaLM2 60.8 to 81.7 on GSM8K look like zero-shot vs method, not comparable to the GPT-3.5 +2.8 over 5-shot CoT. Not re-verified.
- Least-to-most GSM8K: 62.39 vs 60.87 in the table, prose says 60.97. Not resolved.
- Self-Discover MATH gains (PaLM 2-L 45 to 50.5, GPT-4 70.5 to 73) use a 200-problem sample, so are close to sampling noise.

## Weak spots
- Human side is thin: Schoenfeld 1979/1980/1985 quantitative studies, Hembree 1992, Kramarski and Mevarech, Brown and Walter, and Polya were never opened. All Polya content is second-hand.
- No LLM study tests Schoenfeld-style control (episode monitoring, juncture questions) directly. Closest: Gandhi (behaviours), Huang (free self-correction fails), Lightman (process checking).
- Most heuristic-prompting results use text-davinci, PaLM-2, GPT-3.5 era models; effects shrink on stronger models. 2025-2026 reasoning models are barely covered.
- Most claims are single-source (one lab, own prompts).
- Compute is rarely equalised: Self-Discover compares calls, FOBAR uses extra samples.

## Only seen in snippets or not opened
a05, a06, a11, a24-a27, b26-b32, c20-c23 (opened:false). b20 Wei figure values approximate. a20/b18 Yasunaga tables garbled. b25 Lawsen comment had no numbers.

## GAPS
1. Does a forced juncture-monitoring step (Schoenfeld's three questions) change solve rate or dead-end rate of a current LLM at equal tokens? No direct study found.
2. Can a model pick the right heuristic (specialise, generalise, work backward, analogy, decompose) per item better than chance? Self-Discover hints yes; there is no per-heuristic ablation on one benchmark.
3. Do these prompting gains survive on current long-CoT reasoning models? Step-back and FOBAR already shrink on GPT-4.
4. Has "specialise" (try small cases, then conjecture) been tested in LLMs on olympiad or number-theory problems? Nothing found.
5. How large and replicated is the human effect of heuristic training (Schoenfeld 1979/1985, Hembree 1992, IMPROVE effect sizes)?
6. Does forced strategy switching after failure improve proof tasks (USAMO repeated-wrong-strategy), and at what token cost?
7. Do Gandhi's behaviour results (verification, backtracking, backward chaining) transfer from Countdown RL to maths word problems and proofs, and to pure scaffolding with no training?
8. Is backward verification (FOBAR) better than an extra independent sample at matched tokens on strong models?
9. How much of the maths brittleness (GSM-NoOp, premise order) is fixed by an explicit restate-and-strip step?
10. Do Brown and Walter problem-posing moves ("what if not") help an agent on open tasks? No LLM evidence found.


## Gap search results

Gap searcher pass: evidence in `evidence_d.jsonl` (d01 to d19, 17 opened and 2 not opened), claims K20 to K30 added, K12, K13, K15, K17 and K19 updated. Web search quota ran out mid-pass, and the arXiv, Semantic Scholar and OpenAlex search APIs were rate limited, so papers were reached by known arXiv id or open PDF only. Some relevant work may be missed.

1. Forced juncture monitoring (HALF CLOSED). Think2 (d07) forces plan, monitor, evaluate on every query: Llama-3-8B GSM8K falls 80.71 to 69.55, Qwen-3-8B thinking is flat (91.72 vs 91.65). Seeded-error self-correction 12 of 24 vs 7 of 43, a tiny count. No token-matched or dead-end-rate study. Verdict: do not run the monitor always; make it conditional.
2. Per-item heuristic choice (OPEN). Self-Discover (d18) chooses per task, MATH gain 2 to 5 points. No per-heuristic ablation found. K28.
3. Gains on long-CoT reasoning models (HALF CLOSED). Generic CoT adds +2.9, +3.1 and -3.3 points on o3-mini, o4-mini and Flash 2.5 (d06); R1 recovers about 90% from planted errors without help (d08). Step-back and Polya-style prompts were not themselves re-tested on reasoning models.
4. Specialise on olympiad-type problems (MOSTLY CLOSED). Enumerate-Conjecture-Prove (d05) lifts answer construction 14.54 to 45.06 (gpt-4.1-mini). Not tested on reasoning models, at equal tokens, or on proofs.
5. Human effect size (PARTLY CLOSED). Schoenfeld 1979 opened (d01): N=7, p=1/35. Rott and Gawlick 2014 replication opened (d02): N=28, d=0.79 to 1.44. Hembree 1992 (d03) and IMPROVE (d04) NOT opened; still unknown.
6. Forced strategy switching (HALF CLOSED, negative lean). Underthinking (d09) shows reasoning models already switch too much; wrong answers have 418% more switches; stay-on-one-thought prompt did not help R1. USAMO (d10) shows the opposite failure. No forced-switch intervention study exists.
7. Transfer of Gandhi's behaviours (HALF CLOSED). Appendix H (d11): behaviours transfer to GPQA in count (6.5 vs 0.7 subgoal settings) but not accuracy (about 12% both). No pure-scaffolding or GSM8K/proof transfer test.
8. Backward verification vs extra sample at matched tokens (STAYS OPEN). FOBAR adds backward chains on top of equal forward chains (d16), so it is not matched. Sample-scrutinize-scale (d15) shows verification scales past voting for Gemini 1.5 Pro, a different verifier.
9. Restate-and-strip (MOSTLY CLOSED for older models). S2A regeneration 51.7 to 61.3 on GSM-IC while 'ignore' instruction gave no consistent gain (d12); on Llama-3.1-8B an ignore instruction cut attack success 37.5% to 9.9% (d13); few-shot examples did not fix GSM-NoOp (d14). No restate step on GSM-NoOp with a reasoning model.
10. Brown and Walter problem posing (OPEN). Only indirect training-time evidence (Absolute Zero, d19). K29.

Correction notes carried forward: Gandhi's 'identical' priming result is worded 'comparable' (d11). The 24-error Think2 funnel and the 100-problem S2A test are too small to rank methods. The newly added K20 to K30 are mostly single-source.

Priority experiments left for our own harness: (a) conditional monitor vs always-on vs none at equal tokens; (b) backward check vs extra sample at equal tokens; (c) per-heuristic ablation with oracle best-heuristic baseline; (d) specialise operator on find-the-formula items; (e) restate-and-strip vs plain ignore instruction on distractor variants, per model.
