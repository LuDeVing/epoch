# Critique: A07.06 Attentional control theory and executive functions

Cross-check run 2026-11-03. Evidence files a (26 lines), b (25), c (28) read in full. Claims written to claims.jsonl (25 claims, K01-K25).

## Re-opened numbers (confirmed or corrected)

1. Laban et al. 2025 (arXiv 2505.06120, PDF text read). Abstract: average drop 39% across six tasks, 200,000+ simulations: CONFIRMED. CORRECTION: the sources disagree inside the paper. Fig 1 caption says -35%; intro text says 90% single-turn to 65% multi-turn, which is 25 points (28% relative); aptitude is "-15%" in the figure and "16%" in section 6. Use "25 points (90 to 65)" for the plain figure and call 39% the abstract's own summary. Unreliability +112% confirmed. Two-turn drop confirmed. SNOWBALL recovers 15-20% confirmed. Reasoning models 33% longer replies confirmed. The paper warns its simulations are benign, so the drop is probably an underestimate.
2. Shi et al. 2023 distraction (PDF text read). CONFIRMED: no more than 18% of solved base problems stay solved across all distractor types; macro accuracy under 30%; SC +11 micro points, +35.5 for 0-CoT; 99.7% / 96.5% recall in 20 samples; best macro 45%; role overlap drives text-davinci-003 macro to 0 on more-than-2-step problems. Note: "18%" and "under 30%" are two different measures (b16 and c01 mix them in one sentence; c01 is correct).
3. Patel, Wang & Fan (PNAS Nexus 2026, full text via Europe PMC PMC13227603). CONFIRMED: GPT-4o 91/57/22/15% at 5/10/20/40 words; Claude 3.5 Sonnet 76% at 20, 24% at 40. CORRECTION to b18: authors are now known (Patel, Wang, Fan; DOI 10.1093/pnasnexus/pgag149). Primary n=30 per model; GPT-5, Opus 4.1, Gemini 2.5 Pro were n=5 only (5-day test, Sept 2025), so those results are weak.
4. Shi, Sharpe & Abbott 2019 (Europe PMC abstract). CONFIRMED: 58 studies, N=8292, g=-0.58; deficit in efficiency not effectiveness, inhibition and switching but not updating, larger under high load. a09 was marked opened:false but b04 opened the abstract; only the abstract was seen, no moderator tables.
5. Moran 2016 (abstract). CONFIRMED: 177 samples, N=22,061, g=-.334; complex -.342 (k=30), simple -.318 (k=127), dynamic -.437 (k=20). CONTRADICTION found inside the evidence: a11 lists dynamic at -.29 as a "task type" moderator. Different coding scheme in the supplement; not resolved here. Prefer the abstract numbers.
6. Hedge, Powell & Sumner 2018 (abstract). CONFIRMED only the range "0 to .82" and the low-between-subject-variance explanation. The individual ICCs (flanker .40/.57, Stroop .60/.66, etc.) rest on the earlier full-text reading in a13/b06 and were not re-opened by me.
7. Wang & Sun 2025 (arXiv 2506.08184, abstract). CONFIRMED: log-linear decline toward zero, errors are retrieved old values, ignore-earlier-input prompts give limited success. The 3-400 updates, 46 keys, 637B figures were not re-opened.
8. Coda-Forno 2023 and Ben-Zion 2025: only the Ben-Zion abstract (traumatic narratives raise anxiety, mindfulness reduces it but not to baseline) re-seen. STAI numbers 30.8 / 67.8 / 44.4 NOT re-verified. Coda-Forno arXiv page returned a truncated abstract only; betas and t values NOT re-verified.
9. Not re-opened (rate limits on Semantic Scholar, arXiv API intermittently empty): Stroop 1935 numbers, Friedman & Miyake heritability, Moran supplement, Xu/Verguts/Braem, Bukowski 2026, Liu et al. CoT, Gong et al. n-back.

Net: seven of the ten headline numbers confirmed, one correction (Laban 39% vs 35% vs 25 points), one internal contradiction (Moran dynamic span), one missing attribution fixed (PNAS Nexus). Three items remain unverified by me (Ben-Zion/Coda-Forno numbers, Hedge ICC table).

## Contradictions between sources

- c23 says no Stroop/flanker/task-switching test on modern LLMs was found; b18 is exactly such a study (PNAS Nexus 2026). c23 is outdated; K17 uses b18. Still missing: a flanker, WCST or cued task-switching study on LLMs.
- Updating and anxiety: Shi 2019 says no updating deficit; Moran says dynamic (n-back) span is hit hardest (K08, contested).
- a07 (ACT original) was abstract-only in file a but b03 read it; both agree it is a theory paper with no single effect size.
- Emotional text: Coda-Forno finds anxious wording harms, EmotionPrompt/NegativePrompt find both positive and negative wording help. They test different outcomes (bias vs benchmark scores), so they do not strictly conflict, but together they say "tone matters in either direction" (K19/K21).
- a04 gives Common EF 25% shared variance with g and r .51 with IQ; these are consistent but a04 and b02 come from the same review (one independent source for the heritability numbers).

## Weak spots

- Most LLM evidence is a single paper per claim (Laban, Shi, Wang & Sun, Patel). Status "single-source" is honest. Shi 2023 used code-davinci-002 and text-davinci-003, models now retired; not shown on current models.
- ACT itself: no large preregistered replication found; the recent small studies (N=40-74) are null or task-dependent. The agent mapping from "anxiety" to "pressure wording" is an analogy, not shown.
- Hedge 2018 shows conflict-task difference scores have low reliability, which also limits any LLM "inhibition score" built the same way.
- No paper tests inhibition/shifting/updating latent structure in LLMs. Nothing shows LLM Common EF exists.
- Stroop list-length collapse (b18) may reflect long-context counting/format limits, not "executive control"; no control for this was read.
- The claim that fresh context beats "ignore it" rests on Wang & Sun (limited success of instructions) and Laban (CONCAT near FULL); no direct equal-token test of fresh rebuild vs history carry-on inside a scaffold exists.

## Seen only in snippets or abstracts

a07 (Eysenck 2007), a16 (Rey-Mermet), a17 (Berggren & Derakshan), a18 (Kiesel 2010), c18 (Gema inverse scaling), c19 (Levy), c20 (Liu lost in the middle), c21 (Yoran), c22 (Huang self-correction); c24-c28 are background knowledge, not opened. Statuses built on them carry that caveat.

## GAPS

1. Does a fresh, rebuilt context beat carrying history plus an "ignore the above" note at equal tokens on our own agent? (No direct equal-token test exists; decides S6.)
2. Does the Stroop list-length collapse (Patel et al.) appear on current models, and does chunking the list in code remove it? (Tests G11 and context length rules.)
3. Is there any published flanker, WCST or cued task-switching test with measured switch cost on modern LLMs? Search was blocked by rate limits in the earlier run and only partly retried here.
4. How steep is each model's proactive-interference slope (Wang & Sun style), and can that slope set the number of steps before a forced reset?
5. Do near-miss distractors (same entities, same numbers) still cut accuracy on 2025-2026 models, and what does a code filter recover? (Shi 2023 used retired models.)
6. Does worry-like or urgent wording in a scaffold lower accuracy or raise token use on our model, versus matched neutral text? (Human worry vs arousal result is only suggestive.)
7. Is the Moran/Shi disagreement on updating under anxiety real (task coding) or a meta-analytic artifact? Needs the Shi moderator tables.
8. What is the true effect of ACT in a large preregistered replication? None found; matters for deciding how much of the theory to import.
9. Why does Claude hold up longer than GPT-4o on incongruent Stroop lists (76% vs 22% at 20 words)? Is it model size, training, or format? Untested.
10. Does a high expected switch rate in the scaffold (frequent S6 resets) reduce carry-over cost as in Xu, Verguts & Braem, or does it only matter in recurrent networks?

## Gap search results

Run 2026-11-03. Evidence in evidence_d.jsonl (d01-d21, 21 lines; 18 opened, d14 and d15 title-only). WebSearch budget was already used up by other agents, arXiv API, OpenAlex and Semantic Scholar were rate limited, so I used Crossref, Europe PMC, ACL Anthology pages and direct PDFs. Claims K26-K31 added; K08, K09, K11, K13, K14, K17, K19, K23 updated (K11 and K19 moved to established).

1. Fresh rebuilt context vs history plus "ignore" note: PARTLY CLOSED. Shnaidman 2026 (7 open models, 2 benchmarks) finds history-keeping repairs recover 2-3 of 14 pairs and deleting the history 14 of 14. Wang & Sun find a spoken reset cue ineffective and a fake closed turn helpful. No equal-token test on an agent scaffold exists; still needs our own run.
2. Stroop list-length collapse on current models / chunking: STAYS OPEN, with a correction. The Patel stimuli were PNG images, so it is a vision result. Newer models (GPT-5, Opus 4.1, Gemini 2.5 Pro, n=5) still show a deficit; chunking was never tested.
3. Flanker/WCST/cued switching on modern LLMs: PARTLY OPEN. Leads found: Gupta 2024 (task-switch in history, real but old models), AGEA preprint (WCST at human range, abstract only), Hao 2025 and Goto 2025 WCST papers (titles only). No measured switch cost on 2025-2026 models.
4. Interference slope per model: CLOSED as to method, open for our model. Wang & Sun: 35 models, IES, size predicts it, context window does not; CoT does not help. Run their recipe on our model to set the reset step count.
5. Near-miss distractors on newer models, code filter: MOSTLY CLOSED. GSM-Symbolic up to 65% drop; Ghost Context 38.3% temporal-contradiction misattribution and 95.5% of detected errors fixed by masking the top distractor. Both abstract-only; no matched equal-token comparison on our model.
6. Worry-like wording on our model: STAYS OPEN. No direct source found (search budget exhausted). Human side adds a cautionary null (Gillan 2021) and an efficiency-before-accuracy pattern (Cocks 2016) suggesting token use should be logged alongside accuracy.
7. Moran vs Shi on updating: STAYS OPEN. Both abstracts re-read (Shi g -0.58, no updating deficit; Moran dynamic span -.437, k=20, N=1,318). Shi's moderator tables are paywalled. Probable cause is task coding (capacity vs efficiency), not proven.
8. Large preregistered ACT replication: STAYS OPEN. None found. Eysenck et al. 2023 is a theory update; Shi 2019 is a preregistered meta-analysis, not a replication; Gillan 2021 is a related null.
9. Why Claude holds longer than GPT-4o: STAYS OPEN. The authors only speculate (tokenization, no conflict circuit). Descriptive only.
10. Switch frequency and carry-over cost: PARTLY CLOSED for design. Humans needed 4 days of exposure (N=51) for environment-specific flexibility, 1 day (N=52) failed; the network has a fast transient and a slow weight component. A scaffold has only the transient part, which resets with the context.

Corrections to earlier files: c23's "no LLM Stroop test" and K17's attributions stand corrected only in that the Stroop was image-based. d12 (Heliyon 2024) is not a shifting or inhibition study.
