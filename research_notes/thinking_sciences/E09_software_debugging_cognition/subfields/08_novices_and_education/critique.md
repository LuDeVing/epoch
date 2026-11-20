# Critique: E09.08 Novices and education (cross-check)

## Corrections made (sources re-opened from arXiv full text this session)
1. Kazemitabaar et al. 2023 (arXiv 2302.07427): confirmed 80.1% vs 44.4% (d=1.67), time 210 s vs 361 s (d=1.56), errors 1.28 vs 2.17 (d=0.74, t(67)=3.03), docs 22.1% vs 54.3% (d=1.33), pre-test 62.7 vs 60 (p=.67), retention 59.1 vs 49.8 (d=0.28, p=.262) and 47.5 vs 34.8 (d=0.41, p=.092). Correction: line a15 attached d=0.68, t(67)=2.8, p=.006 to "training completion"; text confirms the numbers but the other lines (a16) say Codex "not used for 26.5%" which was not re-checked. Line c11 "0.57x time" is a ratio derived from 210/361, fine.
2. Hellas et al. 2023 (arXiv 2306.05715): confirmed 90/57/40% (GPT-3.5, 30 responses per language set), logic 108 requests (72%), 123 of 150, 82 of those naming all issues, 72 false-issue requests. Correction: the 90% and 123/150 (82%) are different samples. Use 82% for the 150-request set. Also "82 of 150" is 55%, not 57%.
3. Leinonen et al. 2022 (arXiv 2210.11630): confirmed 88/84/48/70/33/54% averages; ranges 11-83% and fix 17-56%.
4. Phung et al. 2023 (arXiv 2306.17156): confirmed repair 68/88/100, edits 36.6 vs 19.0, hint overall 18/66/92, grading and task synthesis rows.
5. Prather et al. 2024 (arXiv 2405.17739): confirmed time mean 17.1 (SD 8.1), r=0.693, r=-0.727, r=0.553, r=-0.503.
6. Ma et al. 2024 HypoCompass (arXiv 2310.05292): confirmed p=.033 score, p=.003 time, p=.007 confidence, 90% generation on 145 programs. Detail: "13.6%" time reduction appears in text, and "four times faster than humans" was not re-found in the grep.
7. Liffiton et al. 2023 (arXiv 2308.06921): confirmed 52 enrolled, 49 analysed, 45 survey, 7 of 49 over 100 queries, one over 600, $0.002 per query. Correction: a19 said "49 students" and b23/c16 "52"; both true (enrolled vs analysed).
8. Not re-opened (arXiv ids not found, API rate-limited): Al-Hossami & Bunescu 2026 (a05-a07, b16), Yeltekin & Bauer 2026 (a08, a09, a23), Golrang 2026, McMining, TreeInstruct, CodeAid (wrong id fetched), Padurean. These rest on the first agents' reading.

## Contradictions and inconsistencies
- Reasoning-mode effect: a05 reports Sonnet-4.5 +6.6, Haiku-4.5 +16.3, GPT-5 -0.8; b16 reports 85-91% across 14 configs. Compatible, but no model rankings were checked.
- Codex study: abstract-level "learners did not do worse" vs retention difference favouring Codex only in high-prior-skill learners and more errors on retention authoring (d=0.51, p=.042). Net: no harm shown, no benefit shown after removal.
- Judge agreement: a07 gives only sample counts (30 RTs, 88 turns); b16 gives 96.6%. Same paper, different units.

## Weak spots
- The core topic anchor (Murphy 2008, McCauley/Fitzgerald 2008, Qian & Lehman 2017) has no numbers: a01-a04 and a25 were metadata only (not opened). The folder is mostly 2022-2026 LLM-in-education work, not the founding novice-debugging studies.
- Most LLM evidence uses GPT-3.5, Codex, ChatGPT or GPT-4 (2022-2023). Models are obsolete; only the 2026 papers use current ones.
- Samples are small (HypoCompass n=19, Prather n=21, Michaeli n=13 vs 15, Kurniawan n=10, Kazemitabaar n=69).
- No claim reached two independent replications of the same effect. "Established" claims combine different studies of a similar theme.
- Education outcomes (learning) are rarely measured; most LLM studies measure output quality, not novice learning.
- Mapping to our agent is by analogy: novice-misconception models are about humans, not agent scaffolds.

## Only seen in snippets / metadata
a01, a02, a03, a04, a25, c27 (Crossref listing). a12 numbers (Codex 33%, PyDex 96.5%) are second-hand.

## GAPS
1. What do Murphy 2008 and Fitzgerald 2008 actually report (sample, strategy counts, share of good/bad/quirky)? Needs the full texts.
2. Does an explicit staged debugging process (hypothesis, test, localise) improve LLM bug-fix accuracy at equal tokens versus free-form, on seeded novice-style bugs?
3. Do current models (2025-2026) still show the 40% false-issue rate and the 55% all-issues rate that GPT-3.5 showed on the Hellas help-request set?
4. Does an independent validator (Phung GPT4Hints-GPT3.5Val style) keep its 95% precision with current models and for code-fixing rather than hints?
5. Does a misconception-diagnosis step ("what wrong belief would produce this bug") raise localisation accuracy, per Yeltekin & Bauer and Al-Hossami & Bunescu, and does it hold up when re-measured?
6. Does the learning loss or gain from AI help appear in a long-term, randomised study with current tools (retention beyond the Codex study's weeks)?
7. Is the reasoning-trajectory (concrete counterexample) benefit larger for small models, and does it transfer to non-Socratic bug fixing?
8. Is the scaffold-initiation effect (user-triggered beats automatic, F(3,116)=132.44) replicated by anyone, and does it have an agent analogue (uncertainty-triggered reflection)?
9. What do Qian & Lehman 2017 and McCauley 2008 report as the top novice misconceptions, with counts, to build a seeded misconception test set?

## Gap search results
Search budget: WebSearch was exhausted by other agents, OpenAlex, Semantic Scholar and the arXiv API were rate limited (HTTP 429); arXiv full text, arXiv search pages, Crossref and one open handout worked. New evidence is in evidence_d.jsonl (d01 to d20, 17 opened).

1. Murphy 2008 and Fitzgerald 2008 numbers: STAYED OPEN. ACM and Taylor and Francis returned 403, no open copy found (d01, d02). Needs a library copy.
2. Staged process vs free-form at equal tokens: PARTLY ADDRESSED, not closed. Xu 2025 shows prompt structure matters for GPT-4 but not for o3 or DeepSeekR1 (d06). No hypothesis, test, localise ablation at equal tokens was found. Claim K18 added.
3. Current models on the Hellas set: STAYED OPEN. No replication found. Indirect: GPT-4 still raises false bugs on correct code (d17); current models beat educators on general CS1 questions (d20).
4. Validator precision with current models: STAYED OPEN. Only indirect support: a verifier turned 11 of 53 valid plans into 53 of 53 (d09, K21).
5. Misconception-diagnosis step re-measured: STAYED OPEN. No independent re-measure of Yeltekin and Bauer or Al-Hossami and Bunescu. Related: error-type descriptions raised GPT-3.5 classification 35% to 56% (d19).
6. Long-term randomised study with current tools: PARTLY CLOSED. A randomised N=78 study with a current model shows a large loss after AI removal (23.1% vs 69.2% repair) and a gate recovering it (61.5%) (d10); horizon is one session, so no delayed retention. K05 raised to established (3 sources, short horizon).
7. Reasoning-trajectory benefit larger for small models: CLOSED NEGATIVELY for the Socratic benchmark. Chain of thought helped GPT-4 (F1 42.6 to 45.9) and hurt GPT-3.5 (22.2 to 8.5) (d18). Transfer to non-Socratic bug fixing not tested.
8. Scaffold-initiation replication: STAYED OPEN, with a tension. A forced gate helped repair (d10, d11); K14 set to contested.
9. Qian and Lehman and McCauley counts: STAYED OPEN. Only the abstract taxonomy (syntax, concept, strategy) was obtained (d03, d04).

New contrary evidence: Socratic-first did not improve comprehension and was rated worst in a randomised N=132 trial (d12); fluent LLM error messages gave no objective gain in two studies (d15, d16, K17). Claims file now has 23 claims.
