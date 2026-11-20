# Critique: E16.10 Deliberate practice (cross-check)

## Numbers re-opened and confirmed this session
1. Ericsson 1993 violin means (7410 / 5301 / 3420 h): confirmed via the full text of Macnamara & Maitra 2019 (a01 said "about 7,400", consistent; c01 exact).
2. Macnamara & Maitra 2019: best M=8224 (CI 6400-10048), good M=9844 (CI 6937-12751), t(24)=-0.93, p=.364, d=-0.38; good vs less (M=4558) t=3.26, p=.005, d=1.33; eta2=.26; teacher-designed eta2=.23, best 6251 h. Confirmed in full text. Weekly practice: best 22.69 h vs good 30.65 h; note the direction is the OPPOSITE of the original (good practised more), which b02 reports as d=-1.03 but a reader may miss.
3. Macnamara 2014 abstract percentages (26/21/18/4/<1): confirmed in abstract.
4. Gobet & Campitelli 2007: abstract says N=104 and the 8-fold hours gap; a05 said N=90 (that is the Hambrick 2020 figure, probably the sub-sample with usable practice data). Correction: use N=104 enrolled, about 90 analysed; r=.42 was not re-checked in the primary.
5. Ruoss 2024 (full text): 270M tournament Elo 2299, Lichess blitz vs humans 2895, puzzles 95.4%; 136M 2259 / 94.5%; 9M 2025 / 88.9%; GPT-3.5-turbo-instruct 1755 vs bots, 66.5%; AlphaZero policy-only 56.1% (puzzle table row appeared as 56.1; AlphaZero value net 82.0, 400-MCTS 95.6); 1.33% overlap. Correction: only the 270M model has a vs-bots Elo equal to its tournament Elo (2299); 9M and 136M vs-bots are 2054 and 2156, so "2299 vs bots" in a15 holds only for the 270M model. Also the paper itself says the bots/humans Elo gap may reflect miscalibration (Lichess blitz is not comparable to tournament Elo).
6. ChessLLM (Zhang 2025, full text): Elo 1788, 61% / 56% / 30% at Stockfish skill 0 / 1 / 2, +350 Elo from long-round data, over 20B tokens. Confirmed. a20 and b16 are the same paper, so they are not independent.
7. Schut 2023/2025 grandmaster table: the arXiv table is garbled in text but the 0 to 42 and 33 to 58 rows match the PNAS 0/12 to 5/12 (41.7%). a18 and c22 agree. Gain did not track rating (confirmed in text). Mean gain 0.85 puzzles (a18) is a different unit from percentage points (c22); both fine.
8. Southwick 2026 (Psychological Science, OpenAlex abstract): N=44,213, over 90% of time on games, 3.61x learning-efficiency advantage, ps<.001, not all DP activities equal. Confirmed at abstract level only. a14, b12, c06 are one paper counted three times.
9. Macnamara 2014 variance by Games: the Games N in the table could not be recovered (garbled); only k=11 and r=.51 stand.
10. Not re-opened: Platz rc=.61, Hambrick 2014 34%, Miller 2019. These rest on secondary reading in Hambrick 2020 (opened).

## Contradictions between sources
- Hambrick et al. (2014) say chess DP explains about 34% of reliable variance; Macnamara 2014 says 26% (uncorrected, Games); Gobet & Campitelli 18%; Burgoyne 2019 says over 50% for broader practice-history variables. The spread is due to the correction, the measure (log, questionnaire, interview) and which variables count as DP. It is not a real disagreement about data.
- Ericsson & Harwell 2019 (k=8, r=.56) vs Macnamara 2014 (r=.38) vs Miller 2019 (r=.40): driven by inclusion criteria (the DP definition problem), not by new data.
- Charness 2005: Ericsson rejected it for missing teacher records in one paper and cited it in another (Hambrick 2020).
- Sample sizes of Charness 2005 differ across entries (N=136 earlier chapter, 239 and 169 in the later paper): different studies, not a conflict.
- Elite performers: 1% (sports, Macnamara 2016) is contested by Ericsson on range restriction. Burgoyne 2019 vs a12: practice dominates over cognitive ability in chess at the top.

## Weak spots
- Almost all human DP numbers are retrospective self-report (interview, questionnaire). Diary data (de Bruin 2008) correlates 0.6-0.8 but is small.
- The only large objective-log study (Southwick 2026) was seen as an abstract; authors are DP-aligned; the 3.61x is efficiency, not a randomised effect. Players choose their own practice.
- No LLM study tests "deliberate practice" as defined by Ericsson. The LLM evidence (c14-c21) is about self-improvement, curricula and test-time compute, which is analogy, not test. Most of it trains weights; our agent cannot.
- Chess LLM results (Ruoss, ChessLLM) are specialist supervised training on engine labels; they show amortised search, not practice.
- Medical-AI evidence (c23-c25) is small, uncontrolled and human-facing.
- Evidence entries a01, a10, a12, a13, b08-b11, b13, b14, b17, c13 were not opened; their numbers come from abstracts or secondary text. b17 and c13 gave no scores.
- b18 methods say n=600 but tables n=300 for mate-in-N: unresolved.
- Entries a21-a25, b20-b25, c01 are second-hand through Hambrick 2020 or Macnamara & Maitra.

## Only seen in snippets
Burgoyne 2016/2019, Charness 2005, de Bruin 2008, Vaci 2019, Li 2023 meta-analysis, Clark 2022, Macnamara 2016, Southwick 2026 (abstract).

## GAPS
1. Is there any LLM study that compares targeted weakness practice against unguided self-play at equal tokens (the Southwick 3.61x contrast, on a model)? None found.
2. Does a prompt-only scaffold (no weight updates) show a "practice effect" over repeated episodes with a note memory (Reflexion-style), and does the gain saturate?
3. What are the Games k, N and moderator effects in Macnamara 2014 (including the 2018 corrigendum) and the chess-only Burgoyne 2016 effect size by skill band?
4. Do the Southwick 2026 results hold after controlling for motivation or prior rating (selection into drill use)? Needs the full paper and supplement.
5. Does adding engine-derived concept examples (Schut-style) help LLM agents at equal tokens, with a random-example control and an unaided-practice control for the humans?
6. Do external verifiers (LLM-Modulo) help or hurt on reasoning tasks beyond legal-move checks (b19 shows puzzle accuracy can fall)?
7. How large are curriculum effects for inference-only agents (task ordering by estimated weakness vs random)? Voyager and PLR train or act with memory; no clean prompt-only test.
8. Is the ceiling effect (practice explains little among elites) mirrored in agents: does scaffold benefit shrink as the base model gets stronger?
9. Which operational definition of "deliberate" for an agent (goal, feedback, weakness targeting) predicts gain best? Needs an ablation across the three components.

## Gap search results
Evidence file: evidence_d.jsonl (d01-d16). Web search budget was exhausted, so Gaps 3 and 4 relied on Europe PMC and PMC full text only.

1. CLOSED (negative, partial). No LLM study compares targeted weakness practice with unguided self-play at equal tokens. Nearest: SEC (d09, trains weights): adaptive curriculum beats random and ordered at equal steps (3B Countdown OOD 0.48 to 0.54). Prompt-only version untested.
2. CLOSED. Yes, prompt-only note memory gives a practice effect (Reflexion 130/134 ALFWorld in 12 trials, ExpeL 59% ALFWorld, AWM +24.6% / +51.1%) (d04, d13, d14). It saturates fast: baseline plateaus at trials 6-7, iterative gap goes to 0 in a few rounds (d04, d12). It needs a reliable success signal.
3. PARTLY OPEN. Burgoyne 2016 skill band: ability r=.32 lower skill vs .14 higher skill, age-confounded (d03). Both Macnamara 2014 and Burgoyne 2016 have 2018 corrigenda (d01), but their content, and Games k and N, were not retrieved.
4. OPEN. Southwick 2026 full text and supplement not reachable (d16). 3.61x stays unadjusted and observational.
5. PARTLY CLOSED. No Schut-style concept-example study for LLM agents found. ExpeL (d13) has a random-example control: random retrieval loses to similar-task retrieval, and insights from given few-shot examples add nothing.
6. CLOSED. External sound verifier: Blocksworld 40 to 88 of 100, LLM verifier 55 (d06); Blocks World 82%, Logistics 70%, Mystery BW about 10% (d07). Intrinsic self-correction without oracle lowers accuracy (d05). Verifier helps only when candidates are plausible.
7. OPEN. Voyager random curriculum -93% (d08) but its curriculum is state-adaptive, so no clean prompt-only ordered-vs-random test.
8. PARTLY CLOSED. Ceiling effects appear in models: SEC gain shrinks from 3B to 7B (d10), Self-Refine +0.2 where base is 93 (d11), CoT helps mostly math or symbolic (d15). No direct same-scaffold test across model strengths.
9. PARTLY CLOSED. Human data: deliberate r=.56 vs purposeful r=.51, p=.64 (d02), so teacher guidance adds little beyond goal plus feedback. No agent three-component ablation exists.

Claims changed: K20 to contested (self-correction caveat); K02, K21, K25 got new evidence ids; K27-K34 added.
