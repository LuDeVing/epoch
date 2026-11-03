# Critique and cross-check, C07.07 Novelty search, open-endedness

## Re-opened sources (this session, text extracted from PDFs)
Confirmed against full text: Lehman and Stanley 2011 (18,274 / 56,334 evals, 21/40 random, 39/40 and 35,109, 66.74 connections); Tao et al. 2020 (Table 1); QDAIF (human QD 0.772, agreement 0.833 vs 0.800, Fixed-Few-Shot quality 4.133); NoveltyBench (1.76, 2.88, 5.66, 6.74, "fewer than 3"); Voyager (15.3x, 2.3x, 93% drop); Darwin Godel Machine (20.0 to 50.0, 14.2 to 30.7); OMNI Crafter (82 tasks, 14 interesting, 0.78, 0.52); Go-Explore arXiv (43,763; 666,474; 59,494; 107,363).

## Corrections
1. Tao Table 1: the line "BDQN 525" in b11 is wrong. The extracted table shifts labels by one row; 524.6 (SE 73.24) is the Novelty multi-step maze value, matching the ablation line "Full 524.60". a19 is right (Acrobot novelty 576.0, maze 524.6). c10 is also wrong where it names 576.0 as BDQN. Real finding: novelty is NOT significantly different from RND on Acrobot (592.5, p=0.85). The table is still partly garbled in text, so confidence is moderate. Only 5 trials.
2. Go-Explore scores differ by version: a16 (Nature, robustified mean 1.73 million) vs b13 (arXiv, 43,763 without and 666,474 with domain knowledge). Both are real. Do not mix them.
3. Voyager diamond: a25 says 3/3 trials reached the diamond pickaxe in 19 +/- 3 iterations. This conflicts with b20, b24 and c15 (diamond in 1 of 3 runs, 102 iterations). I did not re-find the 19 figure. Use 1/3 and treat a25's diamond number as unreliable.
4. QDAIF: "higher QD score in all domains" is the automatic QD score. In human ratings the margin over Fixed-Few-Shot is 0.005 (0.772 vs 0.767), and its human quality is lower (3.900 vs 4.133). Claim marked contested.
5. a02 and a03 mix two maps: 18,274 vs 56,334 is the medium map; 39/40 vs 3/40 is the hard map. Do not combine them.

## Contradictions
- Pure novelty wins in the original maze, but Gomes 2015 finds blends and NSGA beat pure novelty on success ratio. PMCNS gave no clear gain. The boundary depends on maze type.
- Taiga 2020: bonus methods barely beat epsilon-greedy in standard Atari, against the strong Go-Explore and Conti results. Setup differences (hard-exploration vs training set, deterministic restarts) are a likely cause.
- NoveltyBench: the smallest models are the most diverse. So diversity may track weaker tuning, not better exploration.

## Weak spots
- Nearly all numbers come from the originating labs (Stanley, Clune). Independent replications: Kistemaker, Gomes, Taiga only.
- No source measures a novelty signal improving LLM reasoning accuracy. LLM studies measure diversity, coverage or open-ended growth, not correctness at equal tokens.
- Small n: Tao 5 trials; Voyager 3 trials; Conti 5-10 runs.
- LLM judges of interestingness agree with humans only 73-83%; errors feed straight into the archive.
- Seen only in abstract, snippet or thinly: a13, a29/c29, c23, c27, c28, c30, c31 (FunSearch numbers not read). AlphaEvolve numbers (c20) come from the lab's own report.

## GAPS
1. Does a "differ from your earlier attempts" operator raise correctness (not just diversity) of an LLM reasoner at equal tokens, and on which task types (deceptive vs non-deceptive)?
2. What is the best behaviour descriptor for an LLM answer (embedding distance, approach label, final-answer class), given how strongly descriptors drive results?
3. Does blending a goal score with a difference score beat pure novelty for LLM search, and which adaptive weight rule (as in NSRA-ES) works?
4. How large must the archive of past attempts be, and is it better shown in context or used to filter silently?
5. How reliable is an LLM judging its own novelty and learnability compared with external judges, and how do errors propagate through the archive?
6. Does diversity from temperature or small models equal useful exploration, or only noise (NoveltyBench small-model result)?
7. Does Go-Explore-style return to a stored partial solution beat restarting, for multi-step reasoning, at equal tokens?
8. Independent replications of Voyager, OMNI and DGM headline results by groups outside the originating labs.
9. When does novelty hurt: tasks where novelty is uncorrelated with progress (unenclosed maze 5/100 vs 2/100) and noisy-TV style traps in text.

## Gap search results (gap searcher, 2026-11-03)
Evidence in evidence_d.jsonl (d01-d17), all opened as full text (pdftotext). Search tools were limited (WebSearch budget exhausted, arXiv API rate-limited), so papers were chosen from known IDs; some relevant work may be missed.

1. Correctness vs diversity (PARTLY CLOSED). PlanSearch (d01, d02) raises correctness at equal attempts on code (LiveCodeBench pass@200 60.6 to 73.0 GPT-4o; 55.6 to 77.0 Claude 3.5 Sonnet), but pass@1 often drops, the gain vanishes for o1-mini, and it is not shown at equal tokens. Answer-novelty bonuses in math RL help slightly (d05, d06). Deceptive vs non-deceptive task types were not compared. Claim K20 revised.
2. Descriptor (PARTLY CLOSED). Idea-level LLM-judged similarity predicts search gain; entropy insufficient (d02); answer class works in math (d05); embeddings stay above 0.8 even at temperature 2.0 (d12). No head-to-head of descriptors found. New claim K22.
3. Blend vs pure novelty (PARTLY CLOSED). Goal-only RL narrows coverage (d07); novelty with a goal term and a baseline helps, naive novelty does not (d05, d06); clade-level value beats own score for choosing what to expand (d03). No adaptive-weight rule tested for LLMs. K23.
4. Archive size (STAYS OPEN). Only indirect: unverified selection plateaus at several hundred samples (d08). Context-shown vs silent filter not found. K24.
5. Self-judging (PARTLY CLOSED). Self-preference tracks self-recognition, GPT-4 73.5% (d14); pairwise judging 61-71% vs human agreement 56.1% (d15); judges weakest on similar-quality items (d13); judged novelty drops after execution (d16). Error propagation through an archive not measured. K13 updated.
6. Temperature/small models (CLOSED enough). Temperature only weakly raises novelty and raises incoherence (d11); min-p at temperature 2.0 still gives similarity above 0.8, models are alike across vendors (d12, d13). Treat as noise, not exploration. The NoveltyBench small-model result remains unexplained but is consistent with weak tuning. K16 updated.
7. Go-Explore-style return (PARTLY CLOSED). Tree of Thoughts: 74% vs 49% for CoT best of 100 on Game of 24, but costs $0.74 vs $0.47 and uses LLM value check, not novelty (d09, d10). K25.
8. Independent replications (STAYS OPEN). Only HGM re-ran DGM as a baseline (d04): direction holds, numbers not comparable, rival lab. None found for Voyager or OMNI. K27.
9. When novelty hurts (PARTLY CLOSED). Noisy-TV slowdown confirmed qualitatively (d17); pre-execution novelty overstates value (d16). No text-task noisy-TV test found. K26.

Caveats: d05 and d06 table rows were partly misaligned in extraction; numbers marked approximate. Hivemind PDF header shows v2 dated Oct 2026.
