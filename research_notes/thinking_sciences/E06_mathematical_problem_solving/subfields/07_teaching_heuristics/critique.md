# Critique: E06.07 Teaching heuristics (cross-check)

## Numbers re-opened (source PDFs read this session)
Confirmed: Schoenfeld 1982 course scores 21->73 vs 14->24 and F(1,17)=47.5/130.6/48.2 (a07); Huang et al. tables (b25, c18); Plan-and-Solve Table 6 (b13, c01, c02); Least-to-most 99.7/16.2, 62.39/60.87, step table (a27, c06); Step-back 73.2/81.8/84.5/68.7, 20.5%/11.9%, GSM8K 84.3 vs 84.5 (a29, a30, b15); Self-Discover 87.5% correct structures, 74.7% computation failures, MATH 50.5 (a31, b18); Analogical prompting GSM8K 75.0/75.8/76.7/77.8, MATH 33.0 to 37.3 (b20, c09); Buffer of Thoughts Game of 24 82.4 vs ToT 74.0 vs CoT 11.0 (c14); Sprague 14.2/12.3/6.9 and 56.9 vs 45.5 (a37); RRV 2026 pass@1 9.25->11.50, STaR 13.02, pass@64 46.30/46.32/48.17, post-RL 44.21/45.69/48.09/47.62 (a34); Gandhi 60% vs 30%, MATH 38->50%, backtracking 0.15->0.59 (a32, c16); Eisenmann 13->58, 18->74 (a20).

## Corrections
1. b13 says PS+ missing-step errors are 10%. Table 6 gives 7% for PS+ (10% is zero-shot PS). c02 was right. Also PS+ semantic is 27%, same as CoT (c02 said "about equal"; b13 said 26%, which is PS).
2. a07 labels the 21->73 / 14->24 scores as part of the card-sort experiment. The text calls them "mean scores on the mathematics test" (problem-solving performance); the scale is not given. Treat as test points, not percent.
3. b25 and c18 are both right but are different rows: GPT-4 GSM8K 95.5 -> 91.5 (round 1) -> 89.0 (round 2); GPT-4-Turbo 91.5 -> 88.0 -> 90.0. Do not merge them. The paper's own "# calls" column is garbled in text extraction.
4. b19/a39: "+79.4% on Game of 24 over GPT-4" is percentage points (82.4 - 3.0), not a relative gain.
5. a01 says the 1979 study is only "significant difference"; N=7 comes from an abstract. The 1979 paper (a02, b28) was never opened (b28 unopened; a02 abstract only).
6. a16/a14/a15 are Liljedahl et al. summaries of Perkins, Mason, Schoenfeld; not primary.

## Contradictions and tensions
- Human record vs LLM record: Schoenfeld (a05) and Sweller (b04) say heuristic teaching alone has weak evidence; LLM prompting studies show large gains from one generic heuristic (b10) but only small gains from richer ones on strong models (GSM8K PS +2.9; L2M +1.5; Step-back none).
- Step-back works on physics/knowledge QA but not on GSM8K (b15); least-to-most hurts on 2-step items (c06). Heuristics are conditional, not general.
- Self-correction (b25) is the Polya "look back" step and it hurts without an outside signal; Gandhi (a32) lists verification as a helpful behaviour. Resolution probably: verification helps in RL-trained traces with a reward, not as a one-shot prompt.
- Training data: wrong-answer traces still help in Gandhi (a33), but wrong Polya-style approaches hurt in RRV (a35). Different tasks (Countdown vs GSM8K) and different setups.
- Meta-analyses (a24, a25) show large effects, but pooled over schema, strategy and many other methods.

## Weak spots
- Almost every LLM claim is single-paper and mostly 2022-2024 models (PaLM-2, GPT-3.5, text-davinci). No 2025-2026 reasoning-model test of Polya-style prompting beyond DeepSeek-R1 note (c22) and RRV (training, 3B model).
- Mason et al. (Thinking Mathematically) has no experimental data in this folder (a14).
- Equal-token comparisons are rare. Plan-and-solve and step-back use extra tokens; only Self-Discover and BoT report cost.
- Human effect sizes: Schoenfeld N tiny (7; 11 vs 8), Koichu effect size value missing, Hembree effect sizes missing.
- Small N classroom studies (Kuzle 14, Kaitera 25) have no control group.

## Seen only in snippets/abstracts
a02, a09-a12, a17-a19, a22-a26, b28, b29 (abstracts or ERIC records); c23-c25 not opened. Do not quote effect sizes from these.

## GAPS
1. Do heuristic prompts (plan, decompose, step-back, analogy) still beat plain reasoning-model output at equal token budget on 2025-2026 reasoning models (o-series, R1, Claude thinking)? No measured study found.
2. Does a control layer (monitor, assess, curtail) add effect beyond heuristics in LLMs? Schoenfeld confounded them in humans; no LLM ablation separates them.
3. Which heuristics transfer to unrelated problem families for an LLM (Schoenfeld's "acid test")? Need cross-family transfer tests, not same-benchmark gains.
4. Can an agent select the right heuristic per task (selection accuracy), and what does a wrong selection cost? Self-Discover reports gains but not selection accuracy.
5. Hembree (1992) and Schoenfeld (1979) primary numbers: what are the actual effect sizes for heuristic teaching vs other problem-solving instruction?
6. Is the benefit of heuristics larger for weaker or lower-ability solvers (Koichu) and does that match small/weak LLMs vs frontier LLMs (Kramer ceiling effect)?
7. When does self-verification help? Under which external signals (tests, tools, second model) does the Polya "look back" step pay at equal tokens?
8. Does heuristic diversity at inference (sampling under different heuristics) beat same-heuristic sampling (RRV result is training-time)?
9. Do taught-heuristic gains persist or decay (human delayed tests: Hohn and Frey; LLM equivalent: long-context drift of instructions)?
10. How should "heuristic use" be measured in agent traces given coding-manual disagreement (Rott 2015)?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d17; d17 is snippet-only, opened:false). Claims updated (K02, K03, K07, K09, K11, K18, K23, K24) and K25-K32 added.

1. Gap 1 (heuristic prompts vs plain reasoning-model output at equal tokens): PARTLY CLOSED. Meincke 2025 (d01): on GPQA Diamond, step-by-step prompting changes o3-mini by +0.029, o4-mini +0.031, Gemini Flash 2.5 -0.033, and richer decompose/weigh-paths prompts do no better. Plan and Budget (d12): decomposition plus budgets on R1-distills, QwQ and o4-mini cut tokens with comparable MATH-500 accuracy. Token Economies (d08): at equal budget, CoT-SC matches or beats Plan-and-Solve and Least-to-Most (GPT-3.5, plots only). Still missing: a Polya-style prompt tested on a reasoning model at matched tokens on maths.
2. Gap 2 (control layer beyond heuristics): PARTLY CLOSED. Meta-Reasoner (d04) ablation: controller 89 vs LLM self-selected strategy 82 vs plain CoT 4 (Game of 24, GPT-4o-mini). Metacognitive Consolidation (d05): monitor+control 79.20 vs updates alone 80.47 vs bare reasoner 72.67, table garbled. Both author-run, older non-reasoning models. No clean heuristics-only vs control-only 2x2 exists. Schoenfeld 1979 (d13) itself mixed a stop-and-review prompt into both arms.
3. Gap 3 (cross-family transfer): OPEN. Only training-time transfer found (d16, d17 snippet). No prompt-level cross-family test.
4. Gap 4 (selection accuracy and cost of wrong selection): PARTLY CLOSED. MRP (d02, d03): choosing a method helps GPT-4 (0.772 vs best fixed ToT 0.725) but hurts GPT-3.5 (GSM8K 83.1 to 78.1; macro 0.433 below SPP 0.469). Selection accuracy itself still not reported anywhere found.
5. Gap 5 (Hembree and Schoenfeld 1979 numbers): Schoenfeld 1979 CLOSED (d13, full text: N=7, 4 vs 3, all trained beat all controls, p<.05 by 1/35 rank probability, no effect size). Hembree OPEN on numbers: abstract only (d14; 487 reports; heuristics mild at grades 6-8, distinct in high school); effect sizes not found.
6. Gap 6 (weak vs strong solvers): PARTLY CLOSED for LLMs. Gains from selection and from meta-roles are larger or only present on weaker models (d03, d05; Gemini-2.0-flash 94.93 to 96.73 near ceiling; d01 shows prompt gains mostly on non-reasoning models). Koichu human effect size by ability still not found.
7. Gap 7 (when self-verification helps): CLOSED to the level of current evidence. Sound external verifier needed (d06: 5% to 3% self-critique vs 36% verifier vs 42% re-sampling k=25 on Game of 24); survey (d07) agrees. Not tested on reasoning models.
8. Gap 8 (heuristic diversity at inference): PARTLY CLOSED. DIV-SE (d09) beats same-prompt SC on GPT-4 (graph colouring 97 vs 23; Blocksworld 3 94 vs 73) but not on GPT-3.5 hard planning; no equal-token test on reasoning models; model-diversity debate (d10) is weak evidence.
9. Gap 9 (persistence of heuristic gains): OPEN for humans (Hohn and Frey not opened). LLM analogue only: instruction drift within 8 rounds (d11).
10. Gap 10 (measuring heuristic use): CLOSED for the human side. Rott 2015 (d15): three coding manuals on the same 32 actions code 29, 23 and 16 as heuristic. Recommendation: fixed written rule, separate metacognitive category, report agreement. No LLM-trace study of this found.

Caveats: several tables (d02, d05, d09 Table 2, d12) were garbled by text extraction, so only cells that could be read unambiguously are quoted. Corrections to earlier files: Koichu et al. 37 eighth graders in Rott's summary versus the N=92 used in K07 (probably the whole sample incl. control; not resolved).
