# C11.08 critique (cross-check)

## Corrections and confirmations (sources re-opened this session as PDF text)
Re-opened: MADIL (arXiv 2505.01081), CompressARC (2512.06104), Product of Experts (2505.07859). Three other downloads (BARC, TTT, hypothesis search) were truncated and unreadable, so their numbers were NOT re-checked.
Confirmed against the PDF text:
1. MADIL: 69 of 400 eval tasks fit, 57 correct, 82% generalisation (a04). Confirmed.
2. MADIL: 54 of 69 on first greedy rollout; best-model rank 1.3 (solved) and 1.6 (all); mean visited 177 vs 45; depth 17 vs 11 (Table 8). Confirmed. Note: 53 of 57 first-attempt (a04) is a different count from 54 of 69 (a07). Not a conflict.
3. MADIL: model size 3 to 46, mean 15.2 (a06). Confirmed.
4. MADIL: Icecuber 117 vs MADIL 59, overlap 43, MADIL-only 16 (a09). Confirmed.
5. MADIL: Np=1 loses 19, Se=1 loses 27, 80% in first 20 s (a08, b04). Confirmed.
6. MADIL Table 6: the PDF extraction is scrambled (columns shifted). Values 32.1 / 15.1 / 7.0 for MADIL and 44.7 / 30.8 / 20.6 for Icecuber are readable but cell alignment is inferred. 57 to 59 of 400 is 14.25 to 14.75%, so 15.1% as micro-accuracy is plausible. Keep "inferred".
7. CompressARC: 20% eval, 34.75% train, 76K parameters, 2000 steps, 20 min (a18). Confirmed.
8. CompressARC: U-Net 0.75% vs 20% (Table 1; row labels garbled in text but the order is consistent). Confirmed, with the caveat that it is the authors' own baseline.
9. CompressARC Tables 4 and 5: train pass@1/2/5/10/100/1000 at 2000 steps = 30.25/34.75/38.25/41.50/48.50/52.75; eval pass@1 18.5, pass@2 20.0, pass@1000 33.75. Confirmed. The eval step list in a20 and c09 agrees at 100 (1.25), 300 (10.75).
10. Product of Experts: NeMo-Minitron-8B 18.3 / 44.5 / 62.5 / 67.6 / 71.6; Llama-3.2-3B 14.9 / 40.9 / 52.9 / 59.5 / 61.4 (c16). Confirmed. Note the 71.6% is on the public eval set with a compute-heavy DFS sampler; it is not a private-set score.
No numeric error found in the ten. No correction needed. One wording fix: the table in CompressARC text lists "pass@2 after 2000 steps" for eval 20.0% while the peak is 21.5% at 1500 steps; claims.jsonl K11 states both.

## Contradictions between sources
- Human baseline: 83.8% (Johnson 2021, 40 tasks, c21) vs 64.2% eval / 76.2% train (H-ARC, c22) vs 60.2% "average human" used by BARC (a24) vs 75% by ARC-AGI-2 paper (b20, different benchmark). Different samples and attempt counts, so not directly comparable.
- "Brute-force program search about 40% on private eval" (CompressARC Table 1, b18 alijs) vs Icecuber 20.6% (MADIL) vs 17% (semi-private, b20). Different submissions (best single Kaggle vs Icecuber) and different splits.
- Which approach does best: MADIL calls MDL search narrow and deep and 82% accurate when it fits; BARC shows 9% false positives for LLM programs. Not a conflict: these are different generators.

## Weak spots
- Everything on MADIL is one author, one paper family, no independent re-run (b24). The claim that MDL is a good selector rests on MADIL (82%), BARC (9%) and one U-Net control.
- No source measures MDL selection inside an LLM loop at matched tokens. That is the decision-relevant test and nobody has run it.
- Description length in MADIL is hand-built with hand-set priors. No ablation swaps the prior for a flat one.
- The ablation (71 tasks, one parameter at a time) is selected on tasks solved by some version, which biases toward tasks the final system solves.
- CompressARC's U-Net control is the authors' own; no third party ran it.
- ARC-AGI-2 numbers (a29, b20, c23) are for 2025 models; later model scores were not collected.
- c24 (TRM 45% ARC-AGI-1) and c25 (Cole and Osman) only seen at abstract/summary level.

## Seen only in snippets or not opened
b21 (re-arc, only opening read), b23 (DreamCoder, not extracted), a34, c25 (abstract-level). BARC, TTT and hypothesis-search numbers were taken from earlier agents and not re-opened here.

## GAPS (most decision-relevant first)
1. Has anyone used code length or likelihood-based MDL scoring as the selector for LLM-written programs on ARC at matched sampling cost, versus majority vote or random choice among fitting programs? (ArcPrize 2025 report, Berman, Greenblatt-style systems.)
2. Is there any independent re-run or extension of MADIL (OCaml repo forks, ArcPrize 2025 entries), and what did it score?
3. What is the false-positive rate (fits all examples, wrong on test) as a function of number of examples and rule length in LLM programs, and does a length penalty cut it?
4. Does a flat or learned prior replace MADIL's hand-set code lengths with similar accuracy? (tests whether the MDL idea or the hand DSL carries the result)
5. What did ArcPrize 2025 and ARC-AGI-2 winners (reported late 2025 / 2026) use, and do any use compression or length scores in selection?
6. Does CompressARC-style test-time compression transfer to a prompt-only LLM agent (e.g. ask for the shortest rule that explains all grids, then check)? Any measured result?
7. Do large reasoning models (o3, Claude, Gemini 2.5/3) on ARC-AGI-2 show a preference for shorter solutions, and does shorter reasoning trace correlate with correctness?
8. How do human rule-description length and model description length correlate across ARC tasks (extension of Johnson 2021 b=? with H-ARC data)?
9. What are the tasks needing non-compressive intermediate steps (21 in MADIL), and can an LLM agent propose such detours when greedy shortest search stalls?

## Gap search results (evidence_d.jsonl, d01 to d18; claims K18 to K24 added)
Method note: WebSearch quota was exhausted, so search ran through arXiv search pages (WebFetch), the Semantic Scholar and arXiv APIs (rate-limited, HTTP 429) and OpenAlex (budget used up). The MADIL citer list could not be pulled. Full text was read for: ARC Prize 2025 report, SOAR, Moghe and Chin 2026, Land 2026, Zhu 2026, Barber et al. 2025, the ARC survey (MADIL parts only), MADIL (priors and future work), H-ARC (discussion).

1. Length or MDL as selector for LLM programs at matched cost: STILL OPEN. No study found. Related, now recorded: SOAR selects by train accuracy plus vote (9.5 points below oracle, d04); Moghe and Chin find train-accuracy selection already recovers 95% of the 5-candidate ceiling (d06); Land finds a trace-reading judge beats majority vote by 7 instances (d08); Barber et al. give a 3-task length-weighted comparison with mixed result (d10). Lesson: the selection step is not the main loss, so a length selector has limited headroom (K18, K19, K22).
2. Independent re-run of MADIL: STILL OPEN, weakly negative. Survey of 82 approaches shows none (d13); CompressARC has four citers, none a re-run (d14). MADIL's own citer list was not retrieved.
3. False-positive rate versus examples and rule length: PARTLY CLOSED. No curve found. Qualitative evidence of the failure in LLM programs on ARC-AGI-1 and 2 (d05, d09, d12) and three guards in use (K24). No rate as a function of example count.
4. Flat or learned prior for MADIL: STILL OPEN. Re-read shows hand-set uniform and colour-split distributions and no ablation (d15). CompressARC paper has no prior ablation either.
5. ARC Prize 2025 and ARC-AGI-2 winners: CLOSED for the Kaggle top five and the paper track. Top private score 24.03% (NVARC); no winner described as using MDL selection; CompressARC 4% on ARC-AGI-2 (d01, d02). Later non-competition results (Land 72.9% semi-private, Zhu 87.8% pass@2 in competition mode, Poetiq 54%) used refinement and judging, not length (d03, d08, d11). Team write-ups were not opened.
6. Prompt-only CompressARC analogue: PARTLY CLOSED. Hourglass reasoning compresses examples to a schema and rule in isolated contexts and gains +8 to +14 points on ARC-AGI-2 (d11, d12). It is not a measured shortest-description test, and single-author.
7. Reasoning-trace length versus correctness on ARC-AGI-2: STILL OPEN. Only the report's one-task example of 96 versus 138,000 tokens (d03); no correlation study found.
8. Human versus model description length: STILL OPEN. H-ARC collected descriptions but did not analyse length (d16); Johnson 2021 (b = -0.17, 40 tasks) is still the only measure.
9. Detours when greedy shortest search stalls: PARTLY CLOSED. Moghe and Chin's orchestrator, which spawns fresh exploration when the current rule fails, gains 9.75 points over the pipeline (CI +6.50 to +13.25) (d06); execution-guided building composes novel solutions better than fine-tuning (d17). Neither is tested on MADIL's 21 detour tasks.

New caution: the 2026 sources are single-author or small-team preprints, not peer-reviewed, and tuned on public eval sets. Hourglass and Land numbers may be optimistic.
