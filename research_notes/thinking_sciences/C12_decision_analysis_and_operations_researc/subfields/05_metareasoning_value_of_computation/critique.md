# Critique and cross-check: C12.05 Metareasoning, value of computation

Cross-checker pass. Ten sources were re-opened as full PDF text (pdftotext) and the headline numbers compared with the evidence lines.

## Numbers re-checked

Confirmed exactly: Arora and Zanette (16/37/65% tokens, -3.3/-2.2/-1.7 points; 50% under 5%); Sprague (110 papers, 1,218 comparisons, +14.2/+12.3/+6.9, 56.9 vs 45.5, up to 95% on "=" questions); Huang (all GPT-3.5 and GPT-4 table 3 values); Chen (1,953% more tokens, 13 solutions, 39 of 901 tokens = 4.3%, 48.6%, SimPO 22.3%); Callaway 2018 BMPS (90.8-100% variance, 5.19%, 20.3%, 0.6535 vs 0.6596, 0.392, -1.740); Hay 2012 (Theorem 5 and Theorem 10 bounds; 64% win at 10000 samples per ply, c = 1e-6); Snell (about 4x less compute; 14x larger model comparison); AdaptThink (1.5B: +2.4 points, -53.0% length; 7B: +2.3, -40.1%); RaM table 1 (8B: 63.5% / 146.2 vs STaR 61.9 / 215.1, CoT few-shot 56.4 / 253.6, direct 45.8).

## Corrections

1. a16/c25 (Adaptive-Consistency): the GPT-3.5-Turbo figure is 4.4x fewer samples with a 0.2% drop, not "under 0.1%". The 0.1% figure is for the category average (3.3x, 0.04% in the Figure 1 caption). Vicuna-13B 1.9x confirmed.
2. a11 vs b02 (RaM hard/easy): the table labels are ambiguous in text extraction. The 50.3% reduction (145 vs 72) is on the 3B model per the paper's prose; the 8B RaM row is 139 vs 89 (36.0%), equal to STaR (35.9%). So RaM adds nothing over STaR on adaptivity at 8B. Claim K07 is stated that way.
3. a15/b08 (Snell): the FLOPs-matched result is conditional on the ratio of pretraining to inference workload. The intro says test-time compute is often preferable even on hard questions "depending on the specific conditions". "On the hardest questions pretraining wins" is true only for some settings, not all.
4. a04 (Hay Go): the 64% is the highest value reported, for 10000 samples per ply at c = 1e-6, against UCT; board sizes in the text are 9x9 only, engine claim "Pachi" not re-checked. No confidence interval.
5. RaM input tokens: few-shot CoT uses 1,080 input tokens against 73 for RaM; savings in total cost are larger than output tokens alone suggest. Not noted in b01.
6. The "accuracy" in RaM is rescaled accuracy, not raw (already flagged in b01).

## Contradictions and tensions

- Snell (adaptive, difficulty-binned) and Damani (learned predictor): both need a difficulty estimate that itself costs compute; neither nets this out in a deployed loop.
- Ma et al. (NoThinking wins at 700 tokens) vs Muennighoff/s1 (extending thinking helps AIME 50 to 57%) vs Ghosal and Gema (extending hurts): direction depends on budget, model and task. Not a conflict in theory (VOC varies) but nobody gives a predictor.
- RaM claims adaptivity; its own Table 2 shows no gain over STaR at 8B.
- Self-correction (Huang) negative vs gains from verifier-based revision (Snell) : consistent only if the external check is the difference.
- Plan-frequency result (c19) and SwiftSage/Meta-Reasoner come from different benchmarks, so status is contested, not established.

## Weak spots

- The founding source (Russell and Wefald 1991) was never opened by any agent (a01, b19, c01 all second-hand). Everything about its original experiments is unverified.
- Most LLM evidence is token-cost reduction in maths, with accuracy held, and not an actual VOC computed from value of information. Only RaM, Qu et al. (MRT) and Meta-Reasoner use anything like a per-step value signal.
- Callaway 2018 lines a05-a07 and c04 are one paper counted four times; independent_sources set to 1.
- Human-data evidence (b15-b17) rests on a conference paper with 51 participants; the 2022 Nature Human Behaviour version (b18) was not opened.
- No test of metareasoning in an agent with tools at equal tokens, other than c19 (two environments).

## Seen only in snippets or abstracts

b18 (abstract-level), b21 (skim), c29 (memory), a01/b19/b20/c01 (unopened), a18/c17 Thinkless (abstract numbers only), c12 MRT (abstract), c18 Meta-Reasoner (abstract claims), c30, c31 (abstract only), a19 participant counts. c15 (Ma et al. 51.3 vs 28.9) and c11 (s1) were not re-opened in this pass.

## GAPS

1. Does a cheap prompt-only gate (no training) reproduce RaM or AdaptThink savings, i.e. cut tokens 30%+ at equal accuracy on easy items? Nobody has tested it on a closed-API model.
2. What does the gate cost? Net savings after difficulty estimation (Snell, Damani) or probe calls are never reported at equal total tokens.
3. Which signal triggers a stop or a switch best for an LLM: answer agreement across samples, verbalised confidence, hidden-state probe, or progress in the chain? No head-to-head exists (Adaptive-Consistency, Dynamic Early Exit, MRT).
4. Does the one-step VOC failure (Hay 2012) show up in LLM agents, and does a two-or-three-step lookahead rule fix it?
5. How to tell overthinking from underthinking before the answer exists: Chen vs Wang both occur in the same models, at different difficulty. Is there a per-item rule?
6. In tool-using agents, what is the best plan or think frequency by task type (c19 has only two environments)? Does plan-on-surprise beat fixed frequency at equal tokens?
7. What did Russell and Wefald 1991 actually measure (game-tree search savings), and do the numbers survive modern replication?
8. Is the correlation of same-model samples (G4) large enough to break statistical stopping rules (Adaptive-Consistency) in practice? Calibration data is absent.
9. Does negative value of computation (Gema, Ghosal) occur in ordinary agent workloads, or only in constructed tasks? Need a base rate.
10. Do the human results (people stop planning early, 28.3% too early) transfer: does the LLM err early or late on the same Mouselab-style task?

## Gap search results

Evidence is in evidence_d.jsonl (d01-d18). claims.jsonl now has 26 claims (K20-K26 new; K01, K05, K12, K13, K16, K17 changed). Web search quota ran out and the arXiv and Semantic Scholar APIs were rate limited, so papers were fetched by arXiv ID from known citations. Gaps 4 and 10 got no direct hit for that reason as well as for lack of studies.

1. Prompt-only gate (CLOSED, for maths). TALE-EP on GPT-4o-mini cut output tokens 68.6% on average and 91% on GSM8K-Zero for 0.8 points of accuracy (d04); Chain of Draft cut 68-92% on GPT-4o and Claude 3.5 Sonnet, equal accuracy on easy sets, minus 4 points on GSM8K (d03). Not shown: reasoning-model APIs, non-maths tasks. NoThinking is model-specific (d17 vs d10).
2. Cost of the gate (PARTLY CLOSED). TALE counts the estimator call: 91% fewer output tokens became 69% lower cost on easy items, about 44% on the hardest (d04). Accuracy at matched total tokens still unreported.
3. Best stop signal (PARTLY CLOSED, no winner). Verbalised confidence is weak (AUROC 62.7%), 5-sample agreement strong (92.7% on GSM8K) (d07). Among open-weight methods agreement, logprob confidence and attention differ by 1-3 points (d10), and DEER's rank flips between papers (d10, d11). Logprob confidence fails when the model is confidently wrong (d08).
4. One-step VOC failure in LLM agents (OPEN). No LLM test found. Historical evidence only: MGSS* failed against depth-6 search because of the single-step assumption (d01).
5. Overthinking vs underthinking per item (OPEN, negative result). Difficulty explains r squared 0.186 of non-convergence; probe AUC 0.608 (d14). Use an in-run cap, not a prediction. One small model.
6. Plan frequency by task type (PARTLY CLOSED). The intermediate peak holds in four settings (d06). A prompted 'plan only when necessary' failed. Plan-on-surprise vs fixed k at equal tokens is untested: open.
7. Russell and Wefald (PARTLY CLOSED). The 1989 IJCAI and UAI versions were read (d01, d02): fewer nodes, more wall-clock time at depths 2-3, failure at depth 6. The 1991 paper returned 403 (d18); win counts and the 60:1 unit were unreadable. No modern replication found.
8. Correlated samples (PARTLY CLOSED). Cross-model errors agree 60% vs 33% by chance (d12); majority voting can lose accuracy with more calls on hard queries (d13, abstract and introduction only). Same-model sample correlation and calibration of Adaptive-Consistency: still open.
9. Base rate of negative VOC (PARTLY CLOSED, no base rate). Found on ordinary easy sets for small models (d05) and on puzzles (d15), where part is a budget artefact (d16). No survey of real agent workloads.
10. Human-to-LLM transfer on Mouselab (OPEN). Nothing found.

Weak spot c15 re-checked and confirmed (d17). Still unchecked: Thinkless, MRT, Meta-Reasoner, b18. New weak points: d10 and d11 tables only partly readable; d13 abstract-level; every stop-signal comparison is by the proposing group.
