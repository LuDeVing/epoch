# Critique: E18.03 Heuristics and biases (cross-check)

## What was re-opened (full text via pdftotext of arXiv PDFs, plus Crossref abstract)
Confirmed against source text:
- Suri et al. 2305.04400: anchoring means 20.83 / 22.50 (low), 105.97 / 80.50 (high), t(58)=8.78 and 5.55; GPT-4 22.0 vs 94.33 (5 trials). OK.
- Jones & Steinhardt 2202.12299: Codex 32.9 -> 2.4 and framing line 91.7 percent for `raise NotImplemented`; CodeGen 25.6 -> 1.5, 79.3 percent. The "81 / 70.7 percent vs 4.5 / 0.0" figures are averages over five framing lines. Both sets are right; they are different aggregates. OK.
- Macmillan-Scott & Musolesi 2402.09193: 69.2, 55.0, 77.5, 21.7, 50.8, 73.3, 41.7 percent all confirmed.
- Hagendorff et al. 2212.05206: CRT 5 / 59 / 96 percent correct, 80 / 15 / 0 intuitive, humans 38 / 55; CoT 5 -> 28 and 80 -> 29. OK.
- Echterhoff et al. 2403.00811: 13,465 prompts, GPT-4 0.375 vs 0.780 (-0.405), 32.1 percent fewer females, self-help 1.4 and 2.7 percent. OK.
- Malberg et al. 2410.15413: 30,000 tests; table rows framing 0.41, anchoring 0.39, availability 0.11. OK.
- Huang et al. 2505.15392: Llama-3.1-8B 34.7 -> 36.8 (question-aware), 50.5 (knowledge enhancement), 33.3 (adversarial finetuning); GPT-4o 27.3, R1 25.0, Qwen3 thinking 22.0. OK.
- Binz & Schulz 2206.14576: Linda fallacy yes, cab roughly correct, hospital "about equal", black-cab "20%". OK.
- Many Labs 2 (Crossref abstract): 28 findings, 125 samples, 15,305 participants, 15 (54%) at p<.05, 14 (50%) at p<.0001, 7 (25%) larger and 21 (75%) smaller than original. OK. Item-level figures (d=0.04, OR 2.06) were not re-opened here.

## Corrections and clarifications
1. b15 says humans chose the Linda-type conjunction in "85%". In Suri et al., 85% is the original Linda figure quoted from the literature. In their own artist-who-likes-to-read prompt, ChatGPT chose the conjunction 18 of 20 and the humans 10 of 20 (a21 is right). Treat 85% as T&K 1983, not as Suri's human sample.
2. Hagendorff: GPT-4 CRT correct is 96% in the main results and 95% in the Study 2 text and discussion (and 95% with CoT, 88% with CoT blocked). Use "95 to 96".
3. a20 says GPT-3 "fell for the small-hospital item". Source says answered "about equal", like people. Consistent, but note this is the human-like wrong answer, not a measured rate.
4. a10 and b21 (Wikipedia) cite Strack and Mussweiler Gandhi anchors 9 vs 140 giving 50 vs 67: secondary only.
5. Evidence lines a22/b10/c10 and a20/b13/c17, a28/b14/c01, a24/b17/c04 are the same papers read three times. Independent source counts in claims.jsonl are counted per paper, not per line. Several claims that looked "established" by line count are single-source by paper (K18 to K22, K24 to K26) and were marked single-source.

## Contradictions between sources
- Shaki et al. (a25/c18): abstract says no anchoring in GPT-3, but two of four experiments had significant gaps (p=.006, p<.001) of 3 to 4 points. "No anchoring" is better read as "very small, task dependent". Suri, Lou & Sun, Huang, Malberg all find clear anchoring in chat models, so the gap is probably task type (code-completion length vs numeric Q&A) and model.
- Frequency format and Linda (a16/b22): Gigerenzer says errors drop to about 20 percent; Tversky and Kahneman say wording changes alone leave 57 percent. Contested, source is Wikipedia only.
- Stronger models: Lou & Sun say stronger GPT versions are more consistently anchored; Huang says reasoning models are least anchored. These may both hold (non-reasoning scale increases, reasoning-time compute decreases) but nobody tested it in one design.
- Instruction tuning (Itzhak) raises bias, yet ChatGPT-class models avoid CRT traps (Hagendorff). Different bias families.
- Prompt-level fixes: Echterhoff and Lyu find self-rewrite works; Lou & Sun and Huang find prompts do not remove numeric anchoring. Difference: removing the anchor from the input (rewrite) vs asking the model to ignore it.

## Weak spots
- Most 1974 detail comes from the paper itself, but several later numbers (Linda 85/57/20, Tom W., cab, availability moderators, Asian disease 72/78) come from Wikipedia only (a10, a15 to a19, b21, b22, b25 to b27). They are not primary reads.
- Most LLM studies use GPT-3, GPT-3.5, Llama-2, early GPT-4. Few test 2025-era reasoning models (only Huang 2026, Malberg 2025). Results may not transfer to our agent's model.
- Many LLM anchoring sets have small N (Suri 30 per cell, GPT-4 5 trials) and no repeated-run variance.
- Training-data contamination of classic items (Linda, CRT) is likely; only Yax et al. built new vignettes.
- Bias scores in Malberg are defined by the authors, not comparable to human d.

## Seen only in snippets or not opened
- b23 (incentive meta-analysis, OSF) and b24 (OSF 2026 reflective-thinking preprint): opened:false.
- Schley and Weingarten 2026 and Rebholz 2026 numbers: not re-checked.
- Many Labs 1 table values (a12) via LessWrong review; Jacowitz and Kahneman 1995 numbers second-hand.
- Item-level Many Labs 2 numbers (d=0.04, OR 2.06) not re-opened, only headline.

## GAPS
1. Does an S1 input-rewrite step (strip numbers, reframe gain/loss, reorder options) beat CoT and "ignore the anchor" at equal tokens on our agent's model? No study compares these head to head on a 2025-26 reasoning model.
2. Are reasoning-mode models (R1, thinking modes) robust to anchoring and framing because of extra tokens, or because of training? Need a token-matched test of same model with and without thinking.
3. How large are anchoring and framing effects for the current frontier models on fresh (uncontaminated) items, with variance across at least 10 repeats?
4. Does a self-generated estimate before reading the hint (generate-then-compare) cut anchoring, as it does for humans with self-generated anchors? Not tested in LLMs.
5. What is the effect of multi-turn contexts (earlier irrelevant numbers, long-context noise) on bias, beyond the code-model study of Jones and Steinhardt?
6. Does debate or critique (O-steps) copy the biased frame (Lyu: debate 0.50 vs 0.38)? Which critique designs avoid echoing?
7. Availability and representativeness: only Malberg gives LLM availability (0.11, weak). Are base-rate and sample-size errors present in current models when items are rewritten?
8. Primary reads for Linda format effects, Tom W., and Asian disease numbers (Tversky and Kahneman 1981/1983, Gigerenzer 1991) to replace the Wikipedia-only evidence.
9. Do human-style moderators (relevance, distance of anchor, low knowledge) predict LLM anchoring strength? Schley's moderator design could be run on LLMs directly.
10. Is the LLM-judge bias (order, bandwagon) present when our agent verifies its own outputs, and does randomised order remove it at equal tokens?

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d19). WebSearch was out of budget; the arXiv, Semantic Scholar and OpenAlex APIs were rate-limited, so sources came from arXiv PDFs, Crossref, Europe PMC and the ACL Anthology. Primary T&K 1981/1983 and Gigerenzer 1991 PDFs could not be fetched.

1. Input rewrite vs CoT vs "ignore the anchor" at equal tokens: STAYS OPEN. Pieces only. Restating the anchor lowered anchoring on 5 of 5 items but p=.057 (d04). "Ignore metadata" defences left attack success at 83 to 88 percent on four open models (d06). No head-to-head study found.
2. Reasoning mode vs training: PARTLY CLOSED. Kraishan (d01, d02) toggled thinking at matched weights for Claude and GPT-5.1: no reliable gain (+0.031, p=.157), no negative slope over realised tokens. Yao (d05, abstract only) found thinking amplified an authority-tagged anchor in 6 of 7 models. Contradicts the "reasoning models least anchored" reading of Huang (K11 now contested). Cause (tokens vs training) still not separated for DeepSeek and Qwen.
3. Frontier models on fresh items with 10+ repeats: PARTLY CLOSED. Kraishan used 10 samples per cell on 7 current models, but the items are from the public Malberg benchmark (not fresh) and only 5 per bias. Anchoring +0.163 (d=1.89) was the only human-direction bias (d03). Fresh-item test still missing. Scoring choice matters (d19).
4. Generate-then-compare (own estimate before the hint): STAYS OPEN. No LLM study found.
5. Multi-turn and long-context: PARTLY CLOSED. RealICU (d08) shows early frames and stored insights persist (Hit@5 0.526 with insight memory vs 0.601 without). Self-anchoring drift (d09) is model-specific, N=15 per cell. Neither varies irrelevant numbers in earlier turns directly.
6. Debate or critique copying the frame: PARTLY CLOSED. Hantel (d10, abstract only): cloned agents turn a mild anchor into a market collapse (96 to 15 percent efficiency), reversed by a one-line debiasing instruction. Which critique design avoids echo is still untested.
7. Availability, base rate and sample size in current models on rewritten items: STAYS OPEN. Availability was absent in seven 2025 models on 5 items (d03). Two representativeness papers (d18) could not be opened.
8. Primary reads of Linda, Tom W., Asian disease: PARTLY CLOSED. ML2 PDF read: its framing item is T&K 1981 Study 10 (d 1.08 to 0.40), not the Asian disease problem (d14), which corrects K04. Stegmueller 2024 review (d15) shows the frequency-format effect on Linda is mixed (Fiedler yes, Wedell and Moro no). Original Linda 85/57/20 percent, Tom W. and Asian disease 72/78 numbers are still second-hand.
9. Human moderators predicting LLM anchoring: PARTLY CLOSED. Humans: expertise lowers, extremity raises, relevance no effect (d16). LLMs: stronger models more consistently anchored, time-period answers resist (6 of 11 exceptions from 17 percent of questions; d17). No LLM moderator sweep exists.
10. Judge bias in self-verification: MOSTLY CLOSED. Order swaps changed verdicts in 5 to 82.5 percent of comparisons (d11); position consistency 23.8 to 65.0 percent (d12); robustness below 0.5 with 3 to 4 candidates (d13). Swapping or averaging orders helps but doubles calls (not equal-token); randomising order is the no-token option. Self-preference evidence is weak (Zheng: too few data) and no study tests a model judging its own output with order randomised at equal tokens.

Corrections to earlier lines: the ML2 framing d=1.08 to 0.40 belongs to Study 10, not the Asian disease problem. Claims K11, K24 changed status; K27 to K34 added. Not opened: d18 (two papers by title only); d05, d10, d16, d19 are abstract-only.
