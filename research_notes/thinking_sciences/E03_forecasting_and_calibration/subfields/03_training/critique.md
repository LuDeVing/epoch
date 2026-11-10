# E03.03 Training: critique (cross-check)

## Re-opened this session (text read)
- Schoenegger et al. 2025 prompt engineering (arXiv 2506.01578): confirmed mixed-model table (Frequency-Based -0.014, Base Rate First -0.011, CoT -0.011, Step-Back -0.011, all adj p=.774; Propose-Evaluate-Select +0.033) and t-test table (Bayesian +0.025, adj p .036; Propose-Evaluate-Select +0.028, adj p .010); the 17.2 to 19.9 point spread.
- Turtel et al. 2025 (arXiv 2505.17989): confirmed 1,265 questions, ReMax ensemble 0.190 [0.178, 0.203], ECE 0.062, Modified-GRPO 0.192/0.054, o1 0.202/0.093, $52 vs $39, differences -0.025, -0.011, +0.039.
- Halawi et al. 2024 (arXiv 2402.18563): confirmed random 0.250, crowd 0.149, system 0.179, accuracy 71.5% vs 77.0%, GPT-4-1106 0.208, crowd-weighted average 0.146.
- Karger et al. 2025 (arXiv 2409.19839): confirmed 0.096 / 0.121 / 0.122; combination 0.076 vs 0.096.
- Lu 2025 (arXiv 2507.04562): confirmed o3 0.1352, o3-pro 0.1386 (main) and 0.1307 (hold-out), experts 0.023 vs o3 0.135.

## NOT re-verified
- Chang et al. 2016: the journal URL returned an HTML page, not a PDF (also on a mirror). All Chang numbers (6 to 12% gains, t values, n) rest on three agents' separate reads that agree on every figure, but I did not re-read the text. Agreed by three, not re-checked by me.
- Moore et al. 2017 (4.3 to 2.0; 2.8 to 0.7): one agent only (a07, a08).
- Not re-opened: Savage 2021, Doussau 2023, Superforecasting reality check 2020, Damani 2025, Chandak 2025, Qiu 2025.
- Abstract/snippet only: Tian 2023, Lin 2022, Kadavath 2022, Zou 2022, Pratt 2024. Never opened (second-hand): Lichtenstein & Fischhoff 1980, Stone & Opel 2000, Fong 1986, Larrick 1990, Lehman & Nisbett 1990, Sedlmeier & Gigerenzer 2001 (a16-a21).

## Corrections and reconciliations
1. Schoenegger numbers differ by analysis, not by error: a22/a23 use one-sample t-tests, b18/c08/c09 use mixed models. Both are in the paper. Name the analysis when quoting. The helpful prompts are significant only in the t-tests; the harmful ones are robust in both.
2. Chang mediation: a04 says Y2 significant and Y4 not (p=.20); b06 says Y2 not significant. Unresolved.
3. Chang Y4: a01 notes the text swaps n and mean labels versus Table 4; Table 4 shows trained as better.
4. Lu: expert Brier 0.023 is on a small subset, not comparable with 0.135 on the full set.
5. Karger: the best LLM score used crowd freeze values on market questions, so it is not a pure model score.
6. "Lasted at least a year" is from AI Impacts (b14): secondary, a lower bound. The primary data are four yearly cohorts; no delayed retest of the same people was seen.

## Contradictions between sources
- Human training helped (Chang, Moore); prompting LLMs with the same ideas barely helped and some prompts hurt (Schoenegger). This is a transfer failure, not a data conflict.
- Feedback training failed for cancer-trial experts (Doussau) but worked for geopolitical forecasters (Chang): domain or feedback quality.
- Ensembling helps the agent but not base GPT-4o (Hsieh).

## Weak spots
- No independent human replication of the CHAMPS KNOW effect was found; the four years are one team.
- The principle-level result (only comparison classes helped) is correlational, from self-classified explanations (69%).
- Self-selected volunteers; forecast counts differ between arms in Y1 (73 to 87).
- Brier is not comparable across question sets; LLM papers differ in leak control.
- Moore's gain is mostly lower confidence; hit rate rose about 0.8 points.

## GAPS
1. Does any independent group (not Tetlock/Mellers) replicate the one-hour probability module on human forecasts, and with what effect size?
2. Does the reference-class step alone, as a fixed scaffold step, improve an LLM at equal tokens, given general base-rate prompts gave only -0.011 to -0.019?
3. Why did Bayesian and Propose-Evaluate-Select prompts hurt and push forecasts to extremes, and does a shrink or calibration step reverse it?
4. Did the 2016 training effect persist within the same people after a year (delayed retest), or only across yearly cohorts?
5. Do training-style prompts help current reasoning models if retrieval is frozen? Study 2 says no for o1.
6. Which year's mediation (Y2 or Y4) was non-significant in Chang et al., and what are the exact Table 4 values?
7. Do Moore et al.'s overconfidence figures (4.3 to 2.0; 2.8 to 0.7) hold in the source, with tests?
8. What are the exact calibration numbers, decay and transfer in Lichtenstein & Fischhoff 1980 and Stone & Opel 2000?
9. How much of the fine-tuning/RL gain can be moved into fixed scaffold steps or few-shot memory at equal tokens?
10. Does teaching by worked examples (Bayesian teaching, Qiu 2025) beat abstract instructions for forecasting?

## Gap search results (evidence_d.jsonl, d01-d18)

Search tools were limited: the WebSearch budget was used up, and arXiv and OpenAlex search APIs returned nothing. I used direct PDF opens, Crossref and the OSF file store.

### Closed
- Gap 6 (Chang mediation): CLOSED. Results text: Y1 indirect effect -0.02 (CI -0.04 to -0.01, p=.01) significant; Y2 not significant; Y3 -0.02 (p=.05) borderline significant; Y4 not significant (p=.20). Both Y2 and Y4 fail. Agent a was right on Y4, agent b on Y2. The paper's summary says "three of the four years", which its own Results do not support. Table 4 re-read (d01): trained better in all four years; the Y4 running text swaps n and mean labels versus the table.
- Gap 7 (Moore figures): CLOSED. Table 1 matches (4.3 to 2.0 solo, 2.8 to 0.7 team; hit rate 60.7 to 61.5 and 62.9 to 63.6). N=2,860 forecasters, 344 questions. Significance is by Bonferroni-adjusted CI grouping only. The team-no-training cell (2.8) does not differ from the solo cells.

### Partly closed
- Gap 4 (persistence): Chang Table 9 gives same-people evidence. Veterans stayed in their original condition; trained veterans beat control veterans in Y2 (0.34 vs 0.39) and Y3 (0.33 vs 0.36). Moore finds the overconfidence cut did not decay within a year. Still confounded: attrition selection, revised module, and continuous Brier feedback. No delayed retest without feedback.
- Gap 8 (Lichtenstein & Fischhoff; Stone & Opel): only Moore's description recovered (45 min plus 22 one-hour sessions; 6 two-hour sessions; degraded, limited generalization). Originals still unread. Exact numbers still missing.
- Gap 1 (independent replication): not found. Nearest outside work is different training: Kelly & Mandel 2024 (70 analysts, pre/post, no control; miscalibration .33 to .18; interval bias d=1.17 down, binary bias d=0.37 up; no cross-task transfer) and Stone et al. 2023 (lab feedback, abstract only). Sedlmeier & Gigerenzer 2001, Benson & Onkal 1992 and Karimi Motahhar & Gruca 2025 were located but blocked.
- Gap 2 (reference class alone): no token-matched test exists. Best proxies: Base Rate First -0.011 mixed / -0.016 t-test; Multiple Reference Classes -0.004 / -0.009; none survive the mixed model. A base-rate pipeline lost to a plain prompt in Pratt 2024.
- Gap 3 (why Bayes prompts hurt): they moved forecasts furthest from 50% (distance 0.199 and 0.175 vs 0.134), but CoT also moved far (0.172) and did not hurt, so extremity alone is not the cause. No one tested a shrink step. Pratt 2024 shows the opposite failure (probabilities too low), so prompt effects depend on the set's Yes rate.
- Gap 5 (reasoning models, frozen retrieval): Study 2 covers o1 and o1-mini only; no prompt helped. No 2025-2026 reasoning model test was found.
- Gap 9 (move RL gain into scaffold): Halawi shows about 0.02 from retrieval, 0.007 from fine-tuning, about 0 from prompt content. RL gives 0.025 (Turtel). No equal-token comparison exists.
- Gap 10 (worked examples): Qiu 2025 shows Bayesian-demonstration fine-tuning beats oracle demonstrations and generalizes, prompting did not help. Not tested on forecasting and not in-context.

### Still open
Gaps 1, 2, 3, 5, 9, 10 need our own harness runs. Gap 8 needs the two original papers.
