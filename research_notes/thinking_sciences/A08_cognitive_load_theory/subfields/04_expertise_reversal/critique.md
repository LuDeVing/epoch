# Critique: expertise reversal (A08.04), cross-check

Cross-checker pass, 2026-11-01. Claims are in claims.jsonl (A08.04-K01 to K19).

## Corrections and re-checks made this session
1. SkillsBench (c08-c12). Re-opened arXiv 2602.12670. The current version is v4 (14 June 2026): 87 tasks, 8 domains, 33.9% to 50.5% (+16.6 pp), configurations +4.1 to +25.7 pp. Matches c08. Confirmed from the v4 HTML: self-generated skills -8.1 (Opus 4.7, 43.0 to about 34.9), -11.3, -11.5 pp; 13 of 87 tasks negative, largest -7.4 pp; skills count 1/2-3/4+ = +18.0/+19.0/+10.1; Gemini 3.5 Flash 41.1% baseline, +7.1 pp. Correction: the self-generated "34.9" and other post-values are derived by subtraction, not printed. Version drift: v1 reported 86 tasks and a self-generated effect of about -1.3 pp overall; a NeurIPS page says 84 tasks, +16.4 pp. Always cite the version. The +24.8 pp Gemini 3.1 Pro case has a 36.0% baseline, so the "strong baseline gets small lift" story is only weakly supported (K09 marked contested).
2. Tetzlaff et al. 2025 meta-analysis (b01). Confirmed the 60 studies / 176 effect sizes / d=0.505 / d=-0.428 against the blog summary again, but could not reach the paper (Elsevier redirect, no abstract in search). Still single-source; the blog also says the effect grows with age (strongest in higher education) and is somewhat smaller in language and humanities. No CI, no heterogeneity.
3. Liu et al. 2025 (b23). Abstract confirms: up to 36.3 pp lower for o1-preview than GPT-4o, six tasks, three significant drops, three mixed. The task is not named in the abstract.
4. Sprague et al. 2025 (b22). The abstract confirms "over 100 papers", 20 datasets, 14 models, and the equals-sign point, but gives no numbers. The 14.2/12.3/6.9 and 95% figures were NOT re-confirmed (they come from the full text read earlier). Treat as unverified this session.
5. Wu et al. 2026 (a28 note). a28 says "signs for the positives inferred from the text"; that is a weak spot, not a confirmed result.

Not re-opened (budget): Kalyuga 2007 table values (b03-b12), Hou et al., Macina et al., Gorbunova et al. The OpenAlex, Semantic Scholar and arXiv APIs were rate limited (HTTP 429) today.

## Contradictions between sources
- Wikipedia and secondary pages describe the effect as "support hurts experts". The founding data show many partial reversals (expert d near 0 in 2001b Exp 2, Reisslein -0.26 to -0.37). Harm is smaller than the benefit for novices in most rows (+0.5 vs -0.43 in the meta-analysis; 0.33 vs -0.37 in Reisslein).
- Kalyuga 2007 reads effect sizes as about 0.86 per side; the meta-analysis gives 0.505 and -0.428. The first is a convenience review by the effect's proponent; the second is a pooled estimate. The meta-analysis is smaller. Prefer it.
- Fading is the proposed fix, yet Reisslein 2006 found faded examples worse than example-problem pairs for experts, and Salden 2010 found adaptive selection beat fixed fading.
- Agents: curated help helps on average, but self-written help hurts (-8 to -11.5 pp), and lift does not track baseline cleanly.

## Weak spots
- Most human numbers come from one network (Kalyuga, Sweller, Chandler, colleagues) and a 2007 self-review with effect sizes recomputed by the author.
- Many cells have N of 15 to 63. Expert and novice groups are made from pre-tests (selection).
- Most a-file items are abstracts only (opened:false).
- The key meta-analysis was seen only in a blog.
- LLM evidence is weak for the actual effect: no study splits LLM agents by expertise at fixed help with a randomised design. SkillsBench mixes harness and model. SLATE, Hou, Macina and Gure test related dials. A weak model hurt by help is a capacity limit, not a reversal.
- Median-split, underpowered nulls (Gorbunova N=136; Gure N=63) cannot refute the effect.
- Simulated-learner studies (He-Yueya, Macina) score with an LLM judge and may reward the judge.

## Seen only in snippets or abstracts
a02, a06-a16, a18-a24 (abstracts via ERIC), a32 (snippet), b13-b16 (unopened), c21-c23 (cited second-hand), c07 (no outcome data).

## GAPS (most decision-relevant first)
1. Does the pooled expertise-reversal effect hold with moderators (element interactivity, scaffold type, domain) in the Tetzlaff 2025 meta-analysis? Need paper text: CIs, heterogeneity, publication bias.
2. In LLM agents, is there a crossover when scaffold strength is varied with model strength and the harness held fixed, at equal tokens? No clean study found.
3. What signal should trigger fading in an agent: running pass rate, per-item confidence, or verifier outcomes? Which adaptive rule (Kalyuga's rapid-assessment test, Salden's performance-based selection) transfers to LLM loops?
4. Are the SkillsBench negative-delta tasks the high-baseline tasks? Per-task baseline versus delta data is needed.
5. Why do self-written scaffolds hurt (-8 to -11.5 pp): contamination, length, wrong content? Which guardrails in our schema are the "self-written" kind?
6. Is element interactivity measurable for agent tasks (number of dependent steps), and does it predict the scaffold benefit better than baseline pass rate?
7. Was the early-version SkillsBench self-generated effect (-1.3 pp) the same method? Why did it move to -8 to -11.5 pp across versions?
8. Failed replications: are there registered or independent replications of Kalyuga 1998/2000 outside the Sweller network? None found, and the Nievelstein and Darabi nulls were seen only as abstracts.
9. Does LLM few-shot reversal (R1-style "few-shot hurts") have an ablation with numbers across model strengths?
10. How should "equal tokens" be defined when fading shortens prompts? Need a cost-matched protocol.

## Gap search results (evidence_d.jsonl d01-d32; claims K01 changed, K07-K10 and K19 extended, K20-K24 new)

Closed:
- Gap 1 (mostly). The Tetzlaff 2025 meta-analysis is open access; the full text was read from a CC-BY copy (d01, d19-d21). CIs: novices 0.505 [0.260, 0.750]; experts -0.428 [-0.647, -0.209]; difference 0.971 [0.631, 1.312]. Heterogeneity I2 90.9% and 87.6%. Egger tests null (p=.57, .77). Moderators: educational status, content area, prior-knowledge assessment. Element interactivity and assistance type were not coded. K01 is now established. Weak points: two databases, dichotomised groups, few studies per moderator cell.
- Gap 7. The early SkillsBench self-generated result (-1.3 pp) used a different method (same-session writing, 84 tasks, other models) than v4 (separate creator and solver sessions, -8.1 to -11.5 pp). Not the same measurement (d22, d24).
- Gap 5 (mostly). Self-written help hurts mainly because packs go unused (10 of 12 audited), authoring displaces solving, and used packs lock in confident wrong content (d23). Length was not the cause shown. Mapping to our guardrails: the agent-written, early-assumption kind is the risky one. Audit sample is small.

Narrowed but open:
- Gap 4. SkillsBench text gives no per-task baseline-versus-delta table, only heat maps. Negative tasks are explained by skill design, and with three trials a 5.6 pp change is one trial in 18 (d25). The high-baseline hypothesis stays untested.
- Gap 2. No clean crossover study. Closest: pre-registered GAIA scaffold study (d26; stronger Anthropic model gained most at Level 2; family matters) and observational coding-agent data (d27; scaffold gap 19.4 to 3.8 to 0.9 pp over three Claude generations). Neither varies amount of help at matched tokens. Marked contested (K21).
- Gap 3. The human template exists (Kalyuga and Sweller 2004, 2005, abstract level only, d31) and Tetzlaff advises repeated assessment (d21). No LLM-loop rule is tested. Few-task pass rates cannot locate a threshold (d14).
- Gap 6. Element interactivity can be counted in synthetic tasks (CogniLoad, d29) but no study links it to scaffold benefit. The 2017 Chen paper stayed paywalled (d02).
- Gap 8. Meta-analysis shows no publication-bias signal; partial or null studies outside the network exist as snippets (d32). Still no registered replication.

Still open:
- Gap 9. No ablation table with numbers for "few-shot hurts reasoning models" (d30).
- Gap 10. No cost-matched protocol found. Proposal (our own, not from a source): fix total tokens per item including help text and any creator step, and report accuracy per token as well as accuracy. SkillsBench's self-generated arm and Rodionov's gains both carry extra tokens (d22, d28).

Cautions: Table 6 post-values in SkillsBench v4 are printed, correcting the earlier note that 34.9 was derived. Tetzlaff table coefficients for non-reference levels are differences from a reference level, not raw effects.
