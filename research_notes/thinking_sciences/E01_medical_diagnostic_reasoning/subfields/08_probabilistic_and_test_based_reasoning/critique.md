# Critique, E01.08 Probabilistic and test-based reasoning

## Re-opened and confirmed (full text this session)
- Manrai 2014 (PMC4955674): 11/60 (18%) vs 14/61 (23%), diff 5% CI -11 to 21, modal answer 95% (27/60 and 27/61), median 66% = 33x. Confirmed (a05, b02).
- Rodman 2023 (PMC10714249): cardiac ischemia after positive test, LLM 69 vs clinicians 70 (MAE 56.5 vs 56.2); hypothetical test, LLM 2 vs humans 95 (human MAE 74.4); "less error ... all 5 cases". Confirmed.
- Brodeur 2024 (arXiv 2412.10849): ischemia after positive 10.9 / 68.7 / 70 (o1 / GPT-4 / clinicians), MAE 5.7 / 56.5 / 56.3; breast 2.8 / 7.8 / 50. Confirmed. Text says five cases.
- Nori 2025 (arXiv 2506.22405): 20% and 19.9% physicians, 49.3%, 78.6% at $7,850, 79.9% at $2,397, 81.9%, 85.5% at $7,184. Confirmed. The "70% cheaper than o3" in a16 is derived (2397/7850), not a stated figure; the abstract states 20% cheaper than physicians.
- Weisenthal (arXiv 2311.12188): 19/20, 10/20, 12/20, 16/20, 17/20. Confirmed.
- Qiu 2025 (arXiv 2503.17523): about 80% agreement after tuning; plateau after round 1. Confirmed in text. Off-the-shelf range reads 36-58% (b15) and 37-58% (c17), taken from a figure; not resolved.
- Morgan 2021 PubMed page returned only page chrome; its numbers are verified only through the Rodman and Brodeur tables (they reproduce the reference ranges and clinician medians).

## Corrections and contradictions
- a08 says 35 articles / 226 estimates; b17 cites a conference snippet of 30 papers / 90 effects. Use 35/226 (PubMed abstract). The 24% vs 4% pooled figures agree.
- Weisenthal is dated 2023 (c-file) and 2024 (a/b): one paper, counted once.
- Morgan, Rodman and Brodeur share one dataset and one clinician sample; not independent confirmations of clinician error.
- Frequency-format effect varies: physicians 10 to 46%; meta-analysis 4 to 24%; Weber replication 20 to 36%; Schulz 21.6 vs 36.2. Direction agrees, size does not; "natural frequencies fix it" is wrong.
- MAI-DxO uses a debate-like panel, which conflicts with G9 (no debate).
- Brodeur table shows four cases in places; the text says five.

## Weak spots
- Eddy 1982, Gigerenzer and Hoffrage 1995, Fagan 1975, Kassirer 1989 were not opened (a22-a25, numbers from memory). Not used in claims.
- Pauker and Kassirer 1975/1980, Sox 1986/1989, Djulbegovic, Gill: abstracts only. No numeric threshold values captured.
- No LLM study found that tests the threshold rule itself with measured results.
- c20-c24 (ALFA, AMIE, Goh, Berner, Heckerman) are abstract-level only.
- Nearly all LLM studies are single-model vignettes; results drift between model versions (Talboy: GPT-3.5 failed on retest).
- MAI-DxO test-chooser benefit is confounded with debate and cost tracking.

## GAPS
1. Does computing the posterior in code from separately elicited prior and LRs beat one-shot LLM posteriors at equal tokens on 2025-2026 models? No direct head-to-head found.
2. How much does spectrum bias inflate published LRs (Sox 1986 warning), and does keeping LR ranges change decisions? Numbers not captured.
3. What error does the independence assumption cause when LRs of sequential tests are chained (Pathfinder-style dependencies), in LLM or human studies?
4. Do LLMs obey a test or treatment threshold when told costs, and how often do they order tests that cannot change the action? No measured rates found.
5. What does EIG test selection (UoT, BED-LLM, ACTMED) gain over simple heuristics (most discriminating feature) at equal tokens, given uncalibrated LLM-simulated outcomes?
6. How well calibrated are stated pretest probabilities of current models (GPT-5, Claude 4+, Gemini 2.5+) on the Morgan vignettes after Rodman 2023?
7. Does a counts format in the prompt help LLMs as it helps people? No LLM-specific frequency-format test found.
8. Does odds/LR form beat counts for chained tests in LLMs, as in Schulz 2025 for students?
9. Which stopping criterion (posterior margin vs EIG floor) is best, and what does stopping early cost in sequential diagnosis?
10. Original numbers from Eddy 1982, Gigerenzer and Hoffrage 1995 and Fagan 1975 need verifying from the text.

## Gap search results (evidence_d.jsonl, d01-d26)
Search note: WebSearch quota ran out, arXiv/Semantic Scholar/OpenAlex APIs were rate-limited. Discovery used Europe PMC and direct arXiv/PMC/Nature opens. Several gaps may be open only because search was limited.

- Gap 1 (code posterior vs one-shot, equal tokens): STILL OPEN. Nearest: BIRD (d07; non-medical, older models, tokens not equal) favours elicit-then-compute. Sci Rep 2026 (d06) measures LLM-elicited LRs (GPT-5 limits 0.26x-3.70x) and says it did not compare an LR workflow with an end-to-end answer.
- Gap 2 (spectrum bias): CLOSED enough to use. Case-control design DOR 3.0x (d08); sens/spec shift 0-40 points across prevalence, significant in 8/23 reviews (d09); single pooled value overstates yield 10.8-19.1% (d11); LLM benchmarks also enriched (d12). Not found: effect of ranges on decisions in a controlled test (only the TB yield example).
- Gap 3 (independence when chaining): PARTLY. Theory and estimation work found (d13, d14); a toy calculation (d15, our own) shows 0.90 vs 0.50-0.70. No LLM or human study of chained-LR error. Stays open empirically.
- Gap 4 (threshold obedience, needless tests): PARTLY. Over-ordering measured without costs (d16: specificity 0.13-0.37, prompt restraint barely helps; d17: precision 23-42%). Threshold formulas re-derived (d18). No study gives LLMs costs and tests the rule. Open.
- Gap 5 (EIG vs simple heuristics): MOSTLY CLOSED. Medical: halving heuristic nearly matches UoT at equal tokens (85.1 vs 88.4; 86.7 vs 92.5; d02). 20Q: BED-LLM beats Split by about 2-28 points (d03). K14 changed to contested. Outcome simulation remains uncalibrated.
- Gap 6 (current models on Morgan vignettes): STILL OPEN. Only indirect: confidence of GPT-5 / Gemini 2.5 Pro (d22), Brodeur Science 2026 abstract (d26), second human overestimate source (d20).
- Gap 7 (counts format for LLMs): STILL OPEN. Indirect only (d01 qualitative, 3 models; d23 LLMs far above human norms on textbook problems).
- Gap 8 (odds/LR vs counts, chained, in LLMs): STILL OPEN. Nothing found.
- Gap 9 (stop rule): STILL OPEN. MAI-DxO uses a certainty threshold, untuned (d04); confidence-gated asking beats always-ask (d25); free turns add 2-5 points and loops (d17); stopping is confounded by protocol (d24). No margin-vs-info-gain comparison.
- Gap 10 (Eddy, G&H 1995, Fagan, Kassirer originals): STILL OPEN at source. Only secondary numbers via Hoffrage 2015 (d21): students 7% vs 45% mean; physicians 1/24 vs 16/24 quoted from 1998. Kassirer 1989 abstract empty; Pauker-Kassirer 1980 abstract has no numbers.

Claims changed: K02 -> established (2 independent sources, d20); K14 rewritten, contested; K15 numbers and Science 2026 added ($2,396 not $2,397); K03, K04, K05, K09, K16 evidence extended. New: K19-K26. Corrections: MAI-DxO no-budget 81.9% at $4,735; physician accuracy 19.9% in preprint vs 36.1/46.8% in Science version.
