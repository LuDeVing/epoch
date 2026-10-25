# Critique: Content effects (cross-check)

Note: evidence_c.jsonl does not exist. Only evidence_a (32 lines) and evidence_b (25 lines) were checked.

## Corrections made (sources re-opened this session)
1. Abe et al. 2026 (a28, b18): text says deontic gain is "5.0 to 41.2". Its own Table 2 shows +45 (qwen3-14b zero-shot) (other maxima: +41.2 for gpt-oss-20b few-shot and gemma3-12b few-shot), so the range is +5 to +45. 80 problems per cell confirmed. Zero-shot values in a28 match the table.
2. Cosmides et al. 2010 (a13): Experiment 4 figures were incomplete. Correct: 64 percent with all three factors, 46 with two, 26 with one, and 26 with none (so the third factor removed costs nothing more). Main effects F(1,342)=7.30, 10.22, 4.87 confirmed. a12 numbers (20/25, 13/25, 11/25, 18/25 vs 11/25) confirmed.
3. Cosmides 2010 (a11): "5-30 percent" confirmed. The "65-80 percent" figure was not located in the PMC text in my pass; treat as unconfirmed.
4. Sperber and Girotto 2002 (b03, b04): 68/91/73 confirmed (N 35/35/30); 43 vs 50 percent (want) and 33 vs 66 (conditional, failed replication, "no confident explanation") confirmed. b01 says 67 percent for the same cell: rounding of 20/30.
5. Lampinen et al. 2024 (a20-a24, b12-b14): 625 plus 360 humans, NLI z<1.21, top 15 percent slowest (over 80 s), z=4.44, bonus sample no difference, PaLM-2 L over 75 percent under prior-corrected scoring: all confirmed. Note the Wason human result is weak overall; the effect lives in slow responders.
6. Fiddick 2003 (a03, a04): 61 vs 19 percent (Cheng and Holyoak Exp 2) and 48 vs 25 pooled, h=.83 and .93, permission/obligation n.s. all confirmed against the chapter. Still second hand for 61 vs 19.
7. Bertolazzi et al. 2024 (a25): table values (70.74 to 52.59; 32.22 to 19.26; 54.44 to 57.41; human 44.63/40.97) confirmed. LLaMA-3 8B is a base model.
8. Bertolazzi et al. 2025/26 (a27, b15): CE 0.348 to 0.096 and 0.213 to 0.014 and debias 0.348 to 0.072 confirmed. The paper gives the cosine range as 0.48-0.64 in one place and 0.53-0.64 in another.
9. Ando et al. 2023 (b17): 95/167/102 items and GPT-3.5 61.05/56.89/31.37 confirmed.
10. Klauer et al. 2007 (b10): 16 of 18 data sets, about 75/25 split confirmed.

## Duplicates (not independent)
- a20-a24 and b12-b14 are all Lampinen et al. One source.
- a28 and b18 are the same Abe paper. a27 and b15 are the same Bertolazzi paper (dated 2026 and 2025 in the two files).
- a01-a07 are one chapter (Fiddick 2003), a defender of Social Contract Theory. b05-b07 are Sperber and Girotto summarising their own work.

## Contradictions between sources
- Cheater detection: Cosmides group (80 percent, three added factors, precaution) vs Sperber and Girotto (91 percent with a neutral category; instruction wording flips choices). Both are partly replicated by the other side's data; unresolved.
- Permission schemas: 61 vs 19 percent (1985) vs Fiddick's n.s. abstract permission (20 vs 10) and Cosmides Exp 1-2.
- Fiddick (precaution) vs Cosmides 2010: both say precaution is detected even when accidental; Sperber group attributes this to relevance.
- Oaksford and Chater vs Oberauer on probability effects; Ragni meta-analysis (model theory survives) vs Kellen and Klauer (non-identifiable).
- Prompting: Lampinen finds few-shot leaves effects; Bertolazzi finds CoT nearly removes them in strong models but not in weak LLaMA; Valentino finds ICL cuts accuracy. Model size and scoring method differ.

## Weak spots
- Human cell sizes are small (20 to 35 per group in Fiddick, Cosmides, Sperber). No effect sizes beyond h and phi for most.
- Primary papers never opened by the research agents: Cosmides 1989, Cheng and Holyoak 1985, Sperber et al. 1995, Stanovich and West 1998, Cosmides and Tooby 1992.
- LLM Wason studies (Abe) used exact-match multi-select with temperature 0; results may not transfer to our agent's free-form output.
- Lampinen models are old (Chinchilla, PaLM 2, GPT-3.5); Abe shows reasoning models near ceiling on deontic, so the content effect on current models may be small on classic tasks.
- No source tests an explicit abstraction or "restate the violation" operator on an LLM.

## Seen only in snippets or second hand
b21 (Stanovich and West), b22, b23, b24 (Kellen and Klauer), b25 (Fiddick and Rutherford), a30-a32, a29 (Wikipedia). Ragni et al. 2018 Table 4 effect sizes (b09) not opened.

## GAPS (most decision-relevant first)
1. Does a "restate the rule as what counts as a violation" step (or an explicit form-extraction step) reduce the content effect in a current LLM at equal tokens, beyond plain chain of thought?
2. How large is the believability effect on syllogisms for current frontier models with and without reasoning budget, and does it shrink with more thinking tokens (the slow-responder result)?
3. Do modern LLMs show the deontic advantage because of content or because of the "must" wording (matching bias)? Needs paired rewrites of the same logical form.
4. What is the effect size for relevance manipulations (Ragni et al. 2018 Table 4), and do they transfer to LLMs?
5. What are the original numbers in Cheng and Holyoak 1985 and Cosmides 1989/Cosmides and Tooby 1992 (N, conditions)?
6. Do abstract-form restatements ("placeholders then map back") cut renaming variance on GSM-style and logic tasks, and at what token cost?
7. Does cognitive ability moderate content effects (Stanovich and West 1998) in a way that maps onto model size or reasoning mode?
8. Is the 65-80 percent social-contract figure stable across independent labs (Gigerenzer and Hug, Platt and Griggs, Fiddick and Rutherford 2006 on cheater detection without losses)?
9. Is there any field evidence (human or model) that sorting rules into descriptive vs prescriptive before reasoning improves outcomes?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01 to d18). Web search quota ran out partway, so some leads (Fiddick and Rutherford 2006, Platt and Griggs, Ragni 2018) could not be reached. Primary papers opened: Cosmides 1989, Gigerenzer and Hug 1992, Kroger et al. 1993, Sperber et al. 1995, Ahn and Graham 1999, Macchi et al. 2019, plus four LLM papers.

| Gap | Status | What was found |
|---|---|---|
| 1. Restate-as-violation step vs plain CoT at equal tokens (LLM) | Open, with partial lead | No direct test. Nearest: BIS Reasoning, GPT-4o errors re-run: plain 5%, "focus strictly on logic / follows necessarily" 76%, CoT 87% (d14). Errors-only, not equal tokens. Human support is good (Ahn and Graham, Macchi, Kroger: d06, d11, d12). |
| 2. Belief effect on frontier models, with and without thinking | Partly closed | Top models near zero (Gemini 2.5 Pro +1.4, Flash +0.9, GPT-OSS-20B +0.8). Mid-size still large (Llama 3.3 70B +31.6, Qwen3-Next Thinking +28.0). GPT-5-nano 69.2 at minimum effort vs 98.8 at medium (d01, d13). No token-budget sweep on a single model exists. Budget helps weaker models; thinking label alone is not enough. |
| 3. Deontic advantage: content or "must" wording | Open | Abe's deontic and descriptive items differ in content, format and modal word (d02). No paired rewrite anywhere. A 2x2 test is specified in A01.03-K22. |
| 4. Relevance effect sizes, transfer to LLMs | Partly closed (humans), open (LLMs) | Primary numbers from Sperber 1995: 78 vs 26, 65 vs 16, 70 vs 25, and 57/38/38/5 by effect x effort (d09, d10). Ragni 2018 Table 4 still not opened. No LLM test. |
| 5. Original N and conditions for Cheng and Holyoak 1985, Cosmides 1989, Cosmides and Tooby 1992 | Mostly closed | Cosmides 1989 fully extracted: n=24 (Exps 1-4), n=40 (Exps 5-9), all cells listed (d03, d04). Cheng and Holyoak 1985 not obtained; 61 vs 19 is reported via Cosmides, N unknown (d05). Cosmides and Tooby 1992 not opened. |
| 6. Abstract-and-map-back on GSM-style and logic tasks, token cost | Partly closed | QuaSAR (prompt only): GPT-4o gains of 2 to 7 points over CoT, smaller variance, hurts small models, no token cost reported (d15). AbstRaL needs RL (d16). No equal-token test. |
| 7. Cognitive ability as moderator, mapping to model size or reasoning mode | Mostly open | Stanovich and West 1998 seen as abstract only (d18). Indirect fit: model belief gaps fall as models get stronger (d01, d13). |
| 8. Is "65 to 80" stable across labs | Partly closed | The figure is Cosmides' own range over Exps 1 to 9 (d04). Gigerenzer and Hug, independent lab (n=93): 94 vs 44 percent, permission and obligation rules +33 to +44 points with a cheater cue, and about 44 to 45 percent without one (d07). Platt and Griggs and Fiddick and Rutherford 2006 not reached. |
| 9. Sort rule as descriptive vs prescriptive first | Open | No direct evidence, human or model. Related: violation framing helps only some rule types (d17), and needs explicit negatives (d06). |

### Corrections and cautions added
- The "65 to 80 percent" figure was traced: it is the spread over Cosmides' own switched and standard experiments, so it should not be read as a cross-lab estimate.
- The Cosmides 2010 additive factors (64, 46, 26, 26) remain single-source.
- Qwen3-Next Thinking has a larger belief gap (+28.0) than its Instruct sibling (-7.9) in Poddar; so "thinking" is not a safe proxy for reduced content effect. Poddar uses majority-vote adaptive stopping, so numbers do not map to single-sample runs.
- BIS retest of GPT-4o used only items it had failed (selection effect) and compared prompts of different length.
- OCR errors in the Cosmides 1989 PDF: only clean figures were recorded; some lines (for example the non-social-contract percentages near 0 to 40) are garbled and were left out.

### New claims added (claims.jsonl)
A01.03-K03 rewritten and upgraded to established (two labs). A01.03-K18 rewritten. A01.03-K19 to A01.03-K24 added. A01.03-K19 (explicating the rule's logical relation helps humans) is established; A01.03-K20 (restatement recovers GPT-4o belief errors) and A01.03-K22 to A01.03-K24 are single-source or small; A01.03-K21 is contested.

### Still open, ordered by value
1. Equal-token LLM test of restate-as-violation vs CoT (gap 1). The only run that would change the schema.
2. Paired 2x2 of content x "must" wording (gap 3).
3. Thinking-budget sweep on one mid-size model for belief bias (gap 2).
4. Ragni 2018 Table 4, Cheng and Holyoak 1985, Platt and Griggs, Fiddick and Rutherford 2006, Stanovich and West 1998 full texts.

## Addendum: evidence_c.jsonl (35 lines) now present
Earlier note that evidence_c did not exist is out of date. It was integrated in a later pass.
- Re-opened via arXiv abstracts: Step-Back (c30) confirmed: +7 Physics, +11 Chemistry, +27 TimeQA, +7 MuSiQue for PaLM-2L; the table values 66.4 to 73.2 and 70.9 to 81.8 match. GSM-Symbolic (c31): variance across instantiations and decline with clauses confirmed in the abstract; the "up to 65 percent" NoOp figure is in the body, not re-read here. Saparov et al. (c33) abstract confirmed: four LLMs, weak at longer proofs.
- New claims A01.03-K25 to A01.03-K28 cite c-evidence (previously no claim did).
- c34 and c35 are opened:false (memory and a search note); not used as evidence.
- Weak spot: c07 and c09 tables were garbled in extraction; only patterns are reliable. The Wu et al. FOLIO test is 81 hand-filtered items (selection effect).
- Contradiction: LINC (c27) shows GPT-4 solver loses to CoT on FOLIO while Logic-LM (c25) shows a gain on the same dataset (78.92 vs 70.58). Different pipelines, so not a replication failure.

## Gap search results (second pass: the nine decision-relevant gaps)

New evidence is in `evidence_d.jsonl`, ids d19 to d35 (17 lines, all opened). Claims A01.03-K15, A01.03-K17, A01.03-K18, A01.03-K20 to A01.03-K24, A01.03-K26 to A01.03-K28 were edited; A01.03-K29 to A01.03-K33 were added. Not reached: Cheng and Holyoak 1985 (repository blocked by a bot check), Ragni et al. 2018 (paywalled, no open copy), Stanovich and West 1998 (only a book review and the abstract came back), Platt and Griggs 1993, Fiddick and Rutherford 2006. Web search worked this pass.

| # | Gap | Status | What was found |
|---|---|---|---|
| 1 | Restate-as-violation or form-extraction step vs plain CoT, equal tokens, current LLM | Open | No equal-token LLM test exists in what I could reach. Nearest: SemEval-2026 Task 11 system papers. Extraction pipelines beat weak baselines (set-notation 98.95 vs Gemma3-7B 71.70, d19; Qwen3 4B Thinking 95.83 vs 84.17 direct, d22), but a strong model asked directly gets 98.43 with CE 2.13 (d21). Few-shot CoT raised CE for one model (3.83 to 10.11) while simple CoT had the lowest average CE (d20). Human support for naming the violation in the goal is strong: 16.7 vs 50.0 percent with the same rule (d29). |
| 2 | Belief effect vs thinking budget on one mid-size model | Open | Only two-level contrasts: GPT-5-nano 69.2 (minimum) vs 98.8 (medium); Qwen3-32B 99.58 vs 99.12 without and with thinking (d24). BIS has no congruent items, so no gap. Qwen3-Next Thinking +28.0 stays unexplained. Searches for effort or budget sweeps on belief bias found none. In humans, belief wins mainly on complex items (d33). |
| 3 | Deontic advantage: content or 'must' | Open, design tightened | Abe et al. defines deontic by the modal words and descriptive as arbitrary no-modal rules, so everything changes together (d26). Seals and Shalin is the only matched content-by-rule-type LLM study, on old 7B models, and does not vary the modal (d27). Human data: content effect survives with no rule and no modal (66.7 vs 50.0, d28), and the schema theory treats 'must' as part of its mechanism (d30). The 2x2 in A01.03-K22 now also needs a question-only cell. |
| 4 | Abstract-and-map-back vs plain CoT at matched tokens; premise reordering | Partly closed (negative for strong models), open for equal tokens | Step-Back over CoT: PaLM-2L +8.2 / +6.5, GPT-4 +1.6 / +0.3 on MMLU Physics / Chemistry, and -0.9 on StrategyQA (d31). No token counts. Premise order sensitivity confirmed (20 to over 40 points, d32) but no reorder-step test. |
| 5 | When is a solver worth it; best hybrid on belief-inconsistent items | Partly closed | Best hybrid found: Z3 as tiebreaker on 3-2 splits, +0.9 accuracy, CE 3.39 to 2.85, net +8 of 960 items, inside one sd, about 4,300 tokens and 6 calls per item. Z3 veto 74.1 percent; Z3 alone 97.6 on invalid vs 52.2 on valid (d20). A 4B model gains 11.7 points from a prover (d22). A strong model direct is at 98.43 (d21). Token-matched comparison against a single strong pass with more thinking is still missing. |
| 6 | Relevance manipulations in LLMs; Ragni 2018 Table 4 | Open | No LLM study using relevance-theory predictions found (three searches). Ragni 2018 not obtainable. Human cross-check: question change alone 16.7 to 50.0 (d29). |
| 7 | Stability of social-contract numbers across labs | Partly closed | Still no independent-lab numbers for Cheng and Holyoak 1985 or for Platt and Griggs. Fiddick, Cosmides and Tooby (2000) claim 'scores of replications' without listing numbers (advocate source), and the schema authors dispute Platt and Griggs' reading (d30). Seals and Shalin reproduce the switched-contract drop in 7B models (d27). Treat '65 to 80' as one lab's range plus Gigerenzer and Hug (94 vs 44). |
| 8 | Cognitive ability as moderator | Open | Full text of Stanovich and West 1998 not reached; A01.03-K17 now warns that the abstract wording ('unrelated') conflicts with a later review ('worse predictor, mostly same direction'). Model-side analogue: gap tracks training generation more than size (d23), and complexity matters in humans (d33). |
| 9 | Sort rule as descriptive or prescriptive first | Open | No direct test in humans or models (searched). Related: violation framing works only for some rules and needs explicit negatives (A01.03-K24), and the modal word is part of the schema mechanism (d30). |

### Cautions found this pass
- **Strong-model ceiling.** The big pipeline gains in the shared task are against weak baselines. Proofbusters had no strong-model direct arm; ITLC's own table shows 98.43 direct. Do not read d19 as a gain over a strong model.
- **Duplicate numbers.** ITLC's Table 1 'syllogism notation' row (98.95 / 2.13 / 46.23) is identical to Proofbusters' official row. One may have copied the other, or the two used the same run. Do not count them as two sources for that figure.
- **Garbled tables.** UFAL-CUNI end-to-end row (CE and score), the ITLC multilingual rows, and the confirmation-bias paper's per-cell table were partly garbled in text extraction; only values that reconcile with the score formula were copied.
- **A01.03-K26 correction.** The earlier 'GPT-4 Physics 69.4 to 84.5' is the gain over the plain prompt; over CoT it is +1.6, within about one standard deviation.
- **Instructions cost tokens.** The one human-style debiasing instruction tested in LLMs with token counts (d34) raised success 42 to 56 percent but also raised tokens per turn (about 1,030 to 1,450 for Qwen3-32B thinking). Any equal-token test must control for this.

### Still open, ordered by value
1. Equal-token LLM test: violation-naming restatement vs 'be logical' vs CoT vs form extraction, on congruent and incongruent items, one weak, one mid, one frontier model.
2. Paired 2x2 (content x 'must') with a question-only cell and a switched-contract item.
3. Thinking-budget sweep with congruent items on a mid-size model.
4. Primary texts still unread: Cheng and Holyoak 1985, Ragni et al. 2018, Stanovich and West 1998, Platt and Griggs 1993, Fiddick and Rutherford 2006, Cosmides and Tooby 1992.
