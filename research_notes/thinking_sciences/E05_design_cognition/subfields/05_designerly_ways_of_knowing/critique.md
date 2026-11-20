# E05.05 Designerly ways of knowing: critique (cross-check)

## Corrections made (sources re-opened from saved text this session)
1. **Xu, Martelaro, McComb 2026 (a16 is wrong, b06 and c11 are right).** a16 listed RWL 106.08 and SRL 72.07. The results table in the paper (and the t-tests: RWL vs SRL d=0.956, RWL vs CRDAL d=1.846) give RWL 72.07 (SD 20.52), SRL 106.08 (45.60), CRDAL 141.17 (48.45). The paper's own prose swaps RWL and SRL once (a typo in the source); the table wins. a16 should be read as corrected. Also 29/30 successful runs for RWL, 30/30 for SRL and CRDAL.
2. **Confirmed unchanged:** Wadinambiarachchi 2024 (N=60, fixation .32, 89% CI [.11,.55], BF 124); Chen 2025 (67.4% vs 78.2% unique terms; keyword counts 208.57 vs 142.71; Red Dot vs Midjourney global feature distance 16.2509 vs 16.0503); Shin 2025 (456 recruited, 280 analysed, 93 of 218 reported problems, experts +12.54%, t=2.70, p=.01); Rosenbaum 2025 (105 recruited, 101 logs, 3.65 vs 2.76, g=.69, p=.003; convergent p=.837); MUTATE (Claude Sonnet 4.6 30/56, GPT-5.4 25/56, humans 44.75/56 = 79.9%); Haase and Hanel 2023 (B=-0.21, p=.218; 32.8 humans beat the best chatbot); Ma 2023 (600 solutions, cosine 0.804 and 0.746); Wen 2026 (N=24, UMUX 81.25 vs 64.24); IDEAFix (TRIZ +35.62%, C-K +40.31% top-5 novelty chart values, three runs, five models).
3. Not re-opened: Guo 2024, Zhang 2025, Egea 2024 dart-range numbers (only the "second of six" claim was spot-checked), Miao DoT p-values, a pdf for Cross 1982 itself.

## Contradictions and tensions
- Fixation: the "AI help raises fixation" result (b03, N=60, BF 124) sits beside "AI help raises originality" (Rosenbaum b07; Wen c14). Reconciliation is task-dependent: a shown example plus an unguided image tool anchors; structured divergent personas or two-mode tools do not. b16 compares BF 124 with a p of 2.2e-6 across different designs; that is a weak comparison and should not be cited as a contrast.
- Method prompts: IDEAFix says every method beats control; the same paper says simple constraints match them. Diamond of Thought shows structure helps; it is confounded with retrieval.
- Shin: LLM does not help reframing in the crowd, yet Zhang 2025 finds process prompts raise novelty. Different tasks, raters and subjects (laypeople vs an LLM acting alone).

## Weak spots
- Founding claim: Cross 1982 has no experiment. a02 (five aspects), a04 (Lawson block puzzle numbers), a08 (Dorst and Cross, N about 9) and a21-a24 were recalled, not opened. No replication or failed replication exists in what we found; this is a searching limit (APIs rate-limited), not proof of absence.
- Almost all LLM studies are small (N=6 to 24) or single-paper; "established" claims rest on same-lab or same-direction small studies. The metacognitive-monitor result is one study with three evidence lines (not three sources).
- Wikipedia lines (a05, a06, a07, a27, a29, b01, b02) are secondary.
- Fixation meta-analysis (Sio, Kotovsky, Cagan 2015) and Micheli 2019 review were seen only as titles; the counterweight (examples can inspire) is unread.
- Guo 2024 is 5 per cell; mediation estimates are fragile.

## GAPS (most decision-relevant first)
1. Does a separate monitor agent beat self-reflection at equal total tokens on verifiable tasks outside battery design (replication of CRDAL)?
2. Does an LLM show solution-first behaviour on Lawson's block puzzle, and does forced problem-exploration first help?
3. Does a one-line "avoid the obvious" constraint match TRIZ/SCAMPER/C-K prompts at equal tokens (IDEAFix gap on full tables)?
4. What does Sio, Kotovsky and Cagan 2015 give for effect size of fixation vs inspiration, and when do examples help?
5. Do divergent-only scaffolds help while convergent ones do not (Rosenbaum null p=.837), and does this hold for agents without a human?
6. Does a reframing operator help an LLM alone (Shin tested laypeople using LLMs)?
7. Primary data from Lawson 1979 (group sizes, scores) and Dorst and Cross 2001 for the true baseline numbers.
8. Do typed idea fragments (what/how/value) as agent memory beat flat notes in a measured agent task?
9. Is there any replication or critique of Cross's five aspects (e.g. 2020s design-research reviews)?

## Gap search results (evidence_d.jsonl, d01 to d19)
Search limits: the shared WebSearch budget was spent; arXiv, OpenAlex and Semantic Scholar APIs returned 429. Sources came from Hugging Face paper search, Crossref, arXiv PDFs and Springer chapter pages. Paywalled: Sio 2015, Lawson 1979, Dorst and Cross 2001 full text.

1. **Monitor vs self-reflection at equal tokens: stays open, sharper.** CRDAL was matched on steps (9.07, 9.10, 9.37; p=0.97), not tokens, and the monitor adds a call per step (d01). Reflection gains elsewhere rest on knowing the first answer failed (Retry alone +0.041, d02). Same-model peers cost 2.1 to 3.4 times the tokens for equal or lower accuracy (d03); at 16 generations parallel sampling beat loops on maths (d04). No replication of CRDAL found. New claim K16.
2. **LLM on Lawson's block puzzle: stays open.** No study found (d19). Nearest: Zhang 2025 sustained single-space focus (c03), Re-Search over-exploit and over-explore (d09).
3. **One-line constraint vs method prompts: mostly closed.** IDEAFix tables show the short "go beyond obvious" family beats control (novelty p=1.16e-34), TRIZ matches it, C-K and SCAMPER do not beat control (p=0.10, 0.28), and method prompts halve list length (d05). Equal-token test still missing. Claims K07, K15.
4. **Sio, Kotovsky and Cagan 2015 effect sizes: stays open.** Paywalled, not opened (d18, opened:false). Analogues: LLMs anchor in 22% to 61% of questions (d12); 800+ person study, many AI examples widened group diversity but not individual creativity (d13); order of AI use changed uptake (d14). Claim K02 updated: effect depends on example type and measure.
5. **Divergent-only scaffolds, agent without human: partly closed.** Rosenbaum's divergent result is a self-rating and control users leaned convergent (d06). A two-stage diverge-then-converge prompt gave about 1.6 times more distinct good tasks with no human (d07), but with no stage ablation. Claim K17.
6. **Reframing operator for an LLM alone: stays open.** No test found. LLMs frame gaps narrowly (bridge 47% to 64% vs 12.1% human, d08) and judge better than they generate (d09, d10). Claims K05, K18.
7. **Primary baselines: partly closed.** Dorst and Cross: N=9, model confirmed, solution space can be structured before problem space (d16). Lawson 1979 group sizes and scores still not obtained.
8. **Typed fragments as agent memory: stays open.** Only analogues: code-side recombination of typed trees (novelty 3.53 vs 3.146, d11), a typed option map (up to +1.25, d10). K13 updated.
9. **Replication or critique of Cross's five aspects: stays open.** Only Cross's own review found (d17). Absence is under rate-limited search. Claim K20.

New or changed claims: K01, K02, K04, K05, K07, K12, K13, K14 updated; K15 to K20 added. Evidence in d is mostly small or single-paper; none was upgraded to established.
