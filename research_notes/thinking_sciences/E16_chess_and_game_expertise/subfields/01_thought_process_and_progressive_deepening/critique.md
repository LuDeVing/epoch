# E16.01 Cross-check and critique

Cross-checker pass, 2026-10-26. Sources re-opened this session (PDF text): Gobet (1998) full paper; Bilalic et al. (2008) both papers (Cognitive Psychology and Cognition); Huang et al. (2024); Wang et al. (2025) underthinking; Muennighoff et al. (2025) s1; Yao et al. (2023) ToT; Ruoss et al. (2024); Schultz et al. (2025); Gandhi et al. (2024) SoS. PDFs were deleted after extraction.

## Confirmed (number matches the source)
- Gobet 1998: nodes 58.0/58.3/56.8/33.9 (F=1.11 ns); mean depth 5.0/4.6/3.7/2.9 (F(3,44)=2.9, p<.05, only Master vs Class B); regression -2.638 + 0.003 x Elo; base moves 3.2 vs 6.5 (F=2.94); first phase F=4.22; IR max F=5.91; NIR max F=3.71; 35.1%, 29.2%, 17.6%, 72.3%; swiss vs de Groot IR 3.2 vs 2.4, NIR 1.6 vs 1.2. All match a10-a12, b01-b06.
- Bilalic 2008: B=.013, p=.004, odds factor 3.67 per 100 Elo, model probabilities .64/.32/.12/.01; expert guesses 86/74/59%; actual 50/18/0%; eye tracking F(5,20)=0.6 vs 11.9, partial eta2 .75; times 37 s, 79 s, 148 s; t(8)=1.67 p=.13 d=1.2. The paper's own words: skill cut to that of players 3 SD lower.
- Huang 2024: GPT-3.5 GSM8K 75.9/75.1/74.7, CSQA 75.8/38.1/41.8; GPT-4 GSM8K 95.5/91.5/89.0; Llama-2 43.5 and 36.5; 74.7% answer kept. (Check of the table: the columns are labelled by number of calls, 1/3/5.)
- Wang 2025 underthinking: 225% more tokens, 418% more switches; over 70% of wrong answers hold a correct thought; R1 switch tokens 13.8 to 5.7; interval 580.1 to 941.6.
- s1: AIME24 50.0 (none), 53.3 (2x or 1x Wait), 56.7 (4x Wait); 2x no string 50.0/90.2/55.1; 2x Alternatively 50.0/92.2/59.6; GPQA 57.6 to 59.6.
- ToT: IO 7.3, CoT 4.0, CoT-SC 9.0, ToT b=1 45, b=5 74.
- SoS: 51.27 vs 25.73; 36% of previously unsolved; 57.1% correct trajectories.
- Schultz: searchless MAV external 2923; 100 sims is +68 internal Elo (1435 vs 1367); 99.6% well-shaped trees.

## Corrections
1. c03 (Ruoss 2024) had several wrong numbers. In the current arXiv table: 270M puzzle accuracy is 95.4% (not 93.5%); 9M/136M/270M tournament Elo 2025/2259/2299 (a "99M 2007 Elo, 85.5%" row is not in this version); AlphaZero policy-only 1777 (not 1620); AlphaZero 400 sims 2470 (not 2502); Stockfish 16 (50 ms) 2711 (not 2706). Held: 2895 vs humans, 2299 vs bots, GPT-3.5-turbo-instruct 1755 and 66.5%. The paper may have versions; use the table above.
2. c07 (ToT) omitted the equal-cost accuracy comparison. Cost table: IO best-of-100 33% ($0.13), CoT best-of-100 49% ($0.47), ToT 74% ($0.74); ToT 5.5k completion tokens vs 6.7k for 100 CoT trials. This is the one comparison close to equal tokens and it should replace the headline "74 vs 4". The table is garbled in text extraction; row pairing was inferred from the paper's text.
3. b18 and c17 s1: the abstract's "50 to 57%" needs 4 forced Waits; 2 Waits give 53.3 (one problem of 30). Taken together with b17 these are fine-tuned or decode-level effects.
4. a06 (de Groot Table 11/12 rate): moves per minute 3.5 vs 2.5 vs the Gobet 1998 republication showing about 3.6 and 2.4 in the same cells. Probably rounding or different columns; de Groot's own tables were not re-opened this pass. Treat as plus or minus 0.1.
5. Bilalic 2008 Table 2 is garbled in text; the in-text report (IM 50%, Master 18% with two Masters, CM 0%) is the source used. a25 matches.
6. c21: the "24.2% headline gain is relative" note is from the Wang chess paper; not re-verified.

## Contradictions between sources
- Do weak players return less (de Groot W2, r=0 for two subjects) or more (Gobet: non-immediate returns fall with skill)? Two weak subjects against 48 players; Gobet's design wins on size, but recording method differed (audio vs notes).
- Selectivity: de Groot's grandmasters mention more moves and more distinct first moves per minute; Gobet's Masters consider fewer base moves; Saariluoma sees an inverted U. Skill ranges and positions differ.
- Depth slope per 200 Elo: 0.5 (Charness), 0.6 (Gobet), 2.4 (Campitelli and Gobet). Resolved only by position difficulty, but N=4 for the large one.
- Time pressure: same data, opposite readings (Gobet vs Chabris and Hearst); van Harreveld and Burns point opposite ways.
- LLM revisit: no-signal self-revision hurts (Huang) vs forced Wait helps slightly (s1) vs fewer switches helps (TIP). All three can hold if the key variable is whether the revisit adds new information, but nobody tested that directly.

## Weak spots
- Almost all the human data are one easy position (de Groot A, 9 plies) and N=4 on the hard positions.
- Chess human literature has no outcome study of revisit policy (disciplined vs free) at equal time. This is the central missing link for operator design.
- The LLM evidence mostly measures accuracy, not equal-token comparisons. Only ToT has an explicit cost table.
- Bilalic's two papers come from the same lab; claim K08 counts as one independent source.
- Chess LLM benchmarks are first-move puzzle scoring; this tells little about revisiting inside a long deliberation.

## Seen only in snippets or abstracts (do not cite numbers)
Connors, Burns and Campitelli 2011 (abstract only, paywalled); Van Harreveld 2007 (abstract); Burns 2004, Charness 1981, Saariluoma 1990, Holding 1985/1992, Newell and Simon 1972, Kotov 1971 (all second-hand through Gobet and Campitelli); Sala and Gobet 2016 (snippet); Sunde et al. 2026 PNAS (news report); Valmeekam 2023, s1 abstract, Deep Self-Evolving Reasoning, LessWrong essay (snippet or search summary); Ciancarini and Pareschi 2026 (abstract only).
Not re-opened in this pass because the source was unreachable (Cloudflare block or rate limit): Campitelli and Gobet (2004) full text, the 2026 four-in-a-row search-tree paper (c13), Chassy et al. 2023, ChessQA, ChessArena, SPIN-Bench, TsuGO, Searchformer. Their numbers keep opened:true from the earlier agents but are NOT cross-checked. K14 rests on three such sources.

## GAPS
1. Does a revisit policy change outcomes at equal tokens? No study compares "finish each candidate once" (Kotov) against free re-entry (de Groot) on result quality, in humans or LLMs. Needed to set the S4/S5 rule.
2. What makes a revisit useful for an LLM: new information (a verifier, a different representation, a different sampled path) versus an unconditioned "check again"? Huang, s1 and TIP point in different directions; no paper isolates the variable.
3. How should depth budget scale with task difficulty? Easy positions show flat search stats, hard ones a 2.4 ply per 200 Elo slope (N=4). Is there a larger replication, and can an LLM estimate difficulty cheaply to set the budget?
4. How much of expert quality can a retrieval library replace? Elo explains 17.6% of quality after search is partialled out; no LLM study tests memory of solved cases against extra search at equal tokens.
5. Can first-solution anchoring (Einstellung) be broken in an LLM by a forced second pass that excludes the first answer's key elements, and does it work for strong models as for experts (GMs resisted on easy items but not hard ones)?
6. Are LLM trace branches causally used? The 32.0% vs 1.2% result is from one game and a GPT-5 judge; replicate on chess and open problems with ablation of branches in the trace.
7. Candidate width: is the best number of first moves difficulty-dependent for LLMs (the human data conflict: 3.2 vs 6.5 vs de Groot's more moves for GMs)?
8. Full-text numbers for Connors et al. 2011 (22 players, two positions, GM to Class A) and Campitelli and Gobet 2004 are needed; they decide whether the depth-skill link on hard positions replicates beyond N=4.
9. Stopping rule: de Groot reports the played move was not the last one investigated in 15% of protocols (5% in position A). What evidence exists on stopping and on "best so far" versus "last explored" for LLM agents?
10. Time pressure curve for an LLM scaffold: does accuracy drop as flat (retrieval-led) as Kasparov's 100 Elo or as steep as Chabris and Hearst's 36.5%? Needs a token-budget sweep.

## Gap search results

Gap searcher pass, 2026-10-26. Evidence in evidence_d.jsonl (d01 to d18, all opened this session as full PDF text, except d03 which is abstract and record pages only). Web search quota ran out partway; the arXiv search API and OpenAlex and Semantic Scholar then returned empty or rate-limit errors, so late gaps were worked from papers already found. PDFs were saved under D:/research_scratch/E16.01/ and deleted after extraction.

### Closed or mostly closed
- Gap 8 (half): Campitelli and Gobet (2004) full text was found at the Brunel repository and verified (d01, d02). The earlier numbers all match: depth 13.8/10.5/7.4/2.8, 2.4 plies per 200 Elo, N=4. New caveats: three positions per player, two of them with a "find the unique solution" instruction, class B lost one position, IM move quality (4.7) above GM (4.3). K04 text updated. Status stays single-source.
- Gap 2: best current answer is "new information, not a repeat". ThinkRetrieve (d08) varies the content of the revisit at equal budget: nothing, random, relevant. Plain Wait revisits stalled or fell, relevant retrieved examples helped most. Kamoi (d07) agrees. New K18, and K09 raised to established with three lines. Still open inside the answer: verifier vs different path vs different representation have not been compared head to head.
- Gap 3: second half closed. A cheap difficulty signal exists: 4 samples and their disagreement, +2.3% over uniform, 14 of 15 settings (d12). Snell's difficulty-adaptive allocation matched best-of-N at up to 4x less compute (d04, d05), but its estimate used 2048 samples per question. New K21 (established). SelfBudgeter (d13) warns that budget prediction can fail on the hardest items. First half (a larger human replication of the depth slope) stays open, see below.
- Gap 4: partly closed. Reasoning Memory (d09) and ThinkRetrieve (d08) show a case or procedure library beating compute-matched sampling in LLMs. Matching is by sample count, not exact tokens, and both are 2026 preprints. New K23, single-source status kept.
- Gap 9 (LLM half): partly closed. OTBench (d14) shows the final state is on average 9.03 points below the best prefix (task-dependent: MATH 1.83, GPQA 16.98), and DEER (d15) shows a confidence-based stop works without training. Both are from the same lab and the oracle number is biased upward. New K20, single-source.

### Partly answered
- Gap 1: no study compares Kotov-style "finish each candidate" against free re-entry on outcomes, in humans or LLMs. The nearest LLM tests are Snell (sequential revision vs parallel samples at equal generations, d04), Chen's iterative deepening (d10), and Mirtaheri (d11). They say the answer depends on difficulty and task. New K22, contested. Not closed.
- Gap 6: the 32.0% vs 1.2% ablation was not replicated; K13 lowered to single-source. Related evidence (d16 Lanham, d17 Thought Anchors) shows reliance on the trace varies by task and that planning and backtracking sentences have the highest causal weight in math. New K19. No chess or open-problem replication was found.
- Gap 7: Snell (d06) shows more search helps on hard items and hurts on easy ones with a learned verifier. This is difficulty dependence of search effort, not of candidate width in first-move choice. Human conflict (3.2 vs 6.5 vs more for GMs) is unchanged.
- Gap 10: no LLM token-budget sweep on a time-pressure question was found. OTBench shows budget curves flat on MATH but not on GPQA or code, and ThinkRetrieve shows sequential scaling falling after a peak (Qwen3-32B MATH-500 peaked near 15K tokens). So there is no single curve shape; it depends on task. K06 stays contested. Needs our own sweep.

### Still open
- Gap 5 (Einstellung and a forced second pass): only mARC (d18) was found. It shows high-effort reasoning models resist traps (0.751 vs physicians 0.66; 55% vs 36% on physician-miss items), but the miss set was defined from the same physicians, and nothing tests "exclude the first answer's key elements". Needs our own run.
- Gap 8 (Connors et al. 2011): paywalled, no open copy. Only the abstract (22 players, speed result) was read. The hard-position depth slope is therefore still N=4.
- Gap 3 (human half): no larger replication of the 2.4 plies per 200 Elo slope.
- Gap 9 (human half): nothing new on the 15% vs 5% "played move was not the last investigated" rate.

### New cautions
- ThinkRetrieve, Reasoning Memory, UAB and OTBench are 2026 preprints with 30-problem AIME sets in several tables; treat gains of a few points as unproven.
- Snell's revision gains need a fine-tuned revision model; they do not show a prompt-only revisit rule works.
- Chen's iterative deepening Table 2 caption is ambiguous on model size in the text read.
- Not re-opened and still unchecked: the 2026 four-in-a-row paper, Chassy 2023, ChessQA, ChessArena, SPIN-Bench, TsuGO, Searchformer (K14 and K12 numbers unchanged from the earlier pass).
