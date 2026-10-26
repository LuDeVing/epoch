# Critique and cross-check: E05.03 Problem-solution co-evolution

Cross-checker pass. 27 claims in claims.jsonl (K01-K27). Ids K28 onward are for the gap searcher.

## 1. Numbers re-opened (full text this session)

Confirmed unchanged:
- Ralph Wiggum paper (b15, arXiv 2603.24768): Table 1 means 72.07 / 106.08 / 141.17 Ah, SD 20.52 / 45.60 / 48.45; F(2,86)=21.606, partial eta2 0.334; d=0.956 and 1.846. All match.
- Rephrase and Respond (b18): 64.95 average vs 89.77 (RaR1) match the table; last-letter 21.36 to 86.82 match.
- Step-back (b20): physics 66.4 to 73.2, chemistry 70.9 to 81.8, "up to 40%" fixed and "max 12%" new errors match.
- Martinec 2020 (b03/b04): 49/32/19% transitions, 37/63% problem/solution space, rS=-0.649 and 0.672 match.
- Chen 2026 (b10): problem framing 2.94 vs 4.64, t(31)=14.03, dz=2.48 match (Holm adjusted).
- ClarifyGPT (c20): 70.96 to 80.80, relative +13.87, 2.85 questions per problem match.
- R-Zero (c15-c17): 49.18 to 54.69, labels 79.0% to 63.0%, 47.0%, 0.6B decline at 70.6% match.
- QuestBench (c18): abstract says 40-50% on Logic-Q and Planning-Q; "above 80%" on GSM-Q/GSME-Q match.
- Shin 2025 (c03, c04): times 23.25/21.82/28.35/20.78 min and CSI 64.28/64.85/61.01 match.

Corrections:
1. Shin et al. (c02, c06): "N=280 analysed (456 recruited)" is wrong in kind. The paper says 456 problem frames were collected and 280 FRAMES were rated by 15 experts. Treat 280 as frames, not people. The 93 who reported trouble were of 218 in the LLM arms (confirmed). Fixed in K10 wording ("280 frames").
2. Frontiers 2026 (b11): reported F=43.28 is inconsistent with the table. Recomputing from the table means (20.90, 18.65, 16.13), SDs (7.64, 7.41, 6.85), n=40 each gives F about 4.27, not 43.28. Looks like a decimal slip (4.328). The ANCOVA F=803.16 is also implausible. Treat the ordering of means as the only usable result, and the paper as low reliability. Reflected in K19.
3. Xu et al. (b15): the finding says "at the same number of steps". True only as a cap of 30 design steps per run. The co-regulation arm adds monitor-agent calls, so it is NOT equal-token. Also the paper's discussion text (line about 600) swaps the labels (says RWL 106.08, SRL 72.07) against its own Table 1; the table is right. One task (battery pack), one model (Gemini 3.1 Pro). Reflected in K20.
4. b15 and a24 are single-task, single-source; do not generalise.

Not re-opened (second-hand or abstract only): the Dorst and Cross numbers (no inferential statistics in the source as far as known), Guo 2024/2025 (b08 p-values), Storm 2019 84% figure (a11, via Wiltschnig 2013), Wang NexusAI, IDEAFix percentages.

## 2. Contradictions between sources
- Shin (null, expert-rated, 280 frames) vs Sood (N=7, 29 vs 17 of 189 interesting, favours Dorst chain). Different outcome (rated quality vs felt interest), different sample size, and both are problem-first chains. Not a true contradiction (c26).
- Frame-first prompts help on checkable tasks (RaR, step-back, Self-Discover, ClarifyGPT) but were null on open-ended design frames (Shin, IDEAFix HMW). Candidate boundary: whether the answer can be checked.
- Chen 2026: AI raised framing and breadth but lowered innovation (4.66 vs 3.40). Guo 2025: AI raised novelty. Different tasks and raters.
- Problem-first vs muddling through: Kokotovich (2008, 2015) vs Halstrom and Galle, Cross 2024 (solution may be structured first). No study compares orders at equal conditions.
- Martinec: textbook analysis-synthesis-evaluation mapping to problem/solution space fails, yet the co-evolution model itself is built on that mapping in many papers.

## 3. Weak spots
- The founding result (Dorst and Cross 2001) rests on 9 designers, one task, no inferential test. Cited about 1,570 times; no replication with numbers was found.
- Kruger and Cross 2006, Suwa 2000, Atman 2007, Christiaans 1992, Kokotovich 2008 (the basis of the "map the problem first" critique) were never opened. Claim K07 is therefore only "contested", not measured.
- Almost all human evidence is qualitative with 4-12 participants.
- LLM evidence on the actual loop (revise the frame after a solution try) is almost absent (K26).
- Most LLM studies test one prompt step on one model, not equal tokens. RaR, step-back and ClarifyGPT cost extra calls that were not matched against best-of-N.
- Guo and Chen human-AI studies use novices, so agent relevance is indirect.

## 4. Seen only in snippets or abstracts
a09, a11, a12, a13, a19, a20, a23, a26, a27, b23-b28 (not opened); a01, a02, a03-a06, a14, a18, a21, a22, b09, c11, c24 (abstract only).

## GAPS
1. Does an S3-to-S2 return (revise the problem frame after a failed solution attempt) beat frame-once-then-solve for an LLM agent at equal total tokens, and on which task types (checkable vs open-ended)?
2. Does problem-first mapping, solution-first, or interleaving give higher novelty AND correctness in humans when compared directly (Kruger and Cross 2006, Kokotovich 2008 full numbers)?
3. What are the real numbers behind Dorst and Cross 2001 and any replication (session length, ratings, number of bridges per protocol)?
4. Why do frame/restate steps help on checkable tasks but not on open-ended design frames (Shin)? Is it checkability, model strength, or judging method?
5. How many reframe rounds help before the loop drifts (R-Zero label decay, Microsoft loop contraction)? Is there a measured optimum for a scaffolded LLM?
6. Which solution-side signals best trigger a reframe in an agent (failed check, contradiction, stall) and does trigger type matter (Xu et al., Parsons and Shukla)?
7. Do LLM design traces show human-like problem-solution transitions when coded with the FBS or Martinec scheme, and does transition complexity predict quality (Zhang et al. abstract only)?
8. Does the Xu et al. co-regulation gain survive at equal tokens, on other tasks and models?
9. Do clarifying-question and missing-information steps (QuestBench, ClarifyGPT) transfer to open-ended design where no single missing fact exists?
10. Do model strength and expertise of the steering person moderate frame gains (RaR weak-model losses; Shin expert-novice gap), and so should the schema skip the frame step for weak models?

## Gap search results (evidence_d.jsonl, d01-d20; claims K28-K35 added, K04, K07, K12, K14, K18, K20, K23, K24, K25 updated)

Limits of this pass: the web-search quota ran out early, arXiv and Semantic Scholar rate-limited, and the Dorst and Cross, Kruger and Cross, Kokotovich 2008 and Lu 2015 full texts were not reachable (closed access or bot check). Gaps that depend on those stay open.

1. S3-to-S2 return vs frame once, at equal tokens: STILL OPEN. No study found that tests it. Closest: d02 (symptom-triggered intervention 20.15% vs unguided rerun 6.90%, self-reflection 4.29%, at equal attempts, on web agents) and d09 (self-judged correction loses; oracle-triggered gains). Both say the trigger must be an external check and a resample arm is the baseline. Checkable vs open-ended split is untested.
2. Order of work in humans: STILL OPEN on numbers. Kruger and Cross 2006 (abstract only, N=9) says solution-driven = more creative, less correct; problem-driven = best balance (d13). Kokotovich 2008 is correlational, closed (d11, d12). No interleaved arm anywhere. K07 stays contested.
3. Dorst and Cross 2001 numbers and replication: STILL OPEN. Abstract only (d14). Partial support from Cash, Goncalves and Dorst 2023 (d03): 31 novices, 1617 segments, uncertainty level tied to transition type (chi2(6)=180.1), but pseudo R2 about 1%.
4. Why frame steps help on checkable but not open-ended tasks: PARTLY ADDRESSED. Cause is not separated. New data: model tier matters (d05), clarification is fragile even on checkable tasks (d08), and Zhang (d01) found a process-style prompt did raise novelty on an open task over a bare prompt, so open-ended framing is not always null. Judge strictness (Shin expert raters) remains a live confound.
5. How many reframe rounds: PARTLY CLOSED. Evidence points to 1-3 rounds: Self-Refine gains mostly in rounds 1-3, max 4 (d10); self-judged loops lose with each round (d09); rerun can break a passing run (d17). No measured optimum for a reframe loop specifically. Suggested default cap: 2-3 with a stop when a check passes.
6. Trigger type: PARTLY CLOSED. Concrete symptom beats generic reflection (d02); external check beats self-judgment (d09); uncertainty hedging is a weak but real human signal (d03, pseudo R2 about 1%). No head-to-head of failed check vs contradiction vs stall on frame revision.
7. LLM traces coded with FBS: CLOSED for the one source. Zhang full text read (d01): static shares match humans, cross-space switches are fewer for the problem-driven persona. Whether transition complexity predicts quality was not tested; still open.
8. Xu et al. at equal tokens: STILL OPEN. Correction to the critique: steps were genuinely equal (9.07 / 9.10 / 9.37, F=0.031, p=.97), not just capped (d04). Monitor tokens are unmeasured. One task, one model.
9. Clarifying questions on open-ended design: STILL OPEN, with a warning. Even on a checkable Lean task the gain ranged -4.2 to +6.3 pp and k=10 did not beat k=3 (d08). Probe-gated clarification did not beat plain generation (d19, snippet). No open-ended design test.
10. Model strength and steering expertise: PARTLY CLOSED. Self-rephrase helps strong models, can hurt weak ones; a stronger framer helps a weak model on 6 of 6 tasks (d05). Expert users got 12.54% more novel frames (p=.01) (d06). Recommendation: gate the self-frame step by model tier, or use a stronger framer. Not tested on design-frame tasks.

Net status changes: K23 now rests on full text (single-source); K20 claim rewritten (equal steps, unmeasured tokens); K25 narrowed; K07 stays contested with added Kokotovich/Kruger detail; K29 (self-correction decay) is established on two benchmarks and two model families.
