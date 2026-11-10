# A19.07 Priming of orientation: cross-check critique

Checked by re-opening the Oyserman and Lee (2008) PDF, Sun and Wang (2025), Tao et al. (2024), Hu et al. (2026) and Luther and Brown (2025) from arXiv or the author site. Magid et al. (2017) PDF could not be fetched (HTML wall), so its numbers rest on the two earlier readers, who agree. Scratch PDFs deleted.

## Corrections made

1. Oyserman and Lee N: line a03 says 5,818 participants; the journal paper says 6,240 (5,408 without 3 anomalous studies). 5,818 is the 2007 chapter count. Use 6,240. 67 studies, 369 effect sizes, weighted d 0.34 (CI 0.29-0.39), unweighted 0.45, 0.42 without anomalies, fail-safe N 3,495, trim-and-fill d 0.17 (24 imputed): all confirmed (c01, c02).
2. Prime-task d values (c02): scrambled sentence is 0.45 (CI 0.30-0.61), not 0.32. Group imagination is 0.32. SDFF 0.49 confirmed. The Sumerian warrior and pronoun-circling cells are garbled in the text extraction; treat warrior about 0.45 as unconfirmed.
3. Outcome d values: relationality 0.61, cognition 0.54, values 0.29, self-concept 0.26 confirmed in the paper text (c03). Well-being is negative in one reading (-0.13), not 0.54 (the table columns scramble). The supplemental-set values in b02 (0.12, 0.30, 0.41, 0.54) are not the headline numbers; do not mix them.
4. Sun and Wang: the change-framing effect is d = -2.095 (neutral minus change-framed), eta-squared 0.5423; a17 and c09 give the same size with opposite signs. Magnitude confirmed. Language d 0.045, Chinese-LLM advantage 0.169, qwen 0.540 confirmed. a18 says "picture task" for ernie; c10 lists ernie, gpt, qwen for experiment 2: the per-task attribution of which model moved is not settled.
5. Tao et al.: 71.0/81.3/77.6/72.6/80.4%, 2.42 to 1.57, Jordan 4.10 to 0.36, Taiwan 2.40 to 3.94, Finland and 0.45 to 2.48 confirmed. The paper's Wilcoxon test (not a t-test) is the test used.
6. Luther and Brown (b15, c17): the percentages are unreliable. The appendix table is column-shifted. Recomputing from the raw totals gives DeepSeek-V3.1 23.6% (text says 30.87%), Opus 4 11.3% (text 12.75%), GPT-4.1 3.6%, GPT-5 14.3%, Llama 3.1 about 38% worse (text 27.33%). The country rows (US 1,027.74 to 892.13 = 13.2%) look like the model-mean row. Quote raw totals only, and read direction (Llama worse, France and Iran worse) not the exact percentages.
7. Hu et al. confirmed: objects 10.71 vs 8.91 (d 0.49), reversed scene description 10.90 vs 10.06 (d 0.36), relational-minus-category 8.10 vs 6.04, collective attribution 3.17 vs 2.81 (model origin). One detail: b19 says collective attribution 3.05 vs 2.93 for language; the paper gives 3.05 (Chinese prompt) vs 2.93 (English), consistent. Individual attribution 4.68 vs 4.74 is a Chinese-prompt-lower reading, p = .021.
8. Jin et al. (b20 vs c04): b20 says value scales read independent, c04 says no clear lean. The numbers are the same (SCS-Independent 6.98 and 5.32 against norm 4.73); both can be true. Dialectical self for GPT-4 was not different (p = .344). Also these t-tests use 10 runs against human norms, so p-values overstate.
9. Authorship: a19 (Magid, Sarkol, Mesoudi) and b09 (Mesoudi, Magid, Sarkol) are the same paper, counted once. a20 (Wu, 2021) and b03 (Lin and Wu) are the same replication, counted once; c25 is the same again from a talk abstract. a21 has no confirmed citation.

## Contradictions between sources

- Lu et al. (language shifts style in GPT-4 and ERNIE) versus Sun and Wang (no robust language effect in 8 models). Not a clean refutation: items differ, original items unreleased, temperature differs.
- Tao and Luther/Brown say persona cues work on values; Kharchenko et al. and Jeripity Venkata say they give stereotypes or deference. Both fit: mean distance falls but profiles are not calibrated.
- Oyserman and Lee call the average moderate; Lin and Wu find a clean null on its most popular prime; trim-and-fill halves the average. Human evidence is therefore weaker than headline.
- Hu et al. found English prompts sometimes give more holistic-style output than Chinese ones; this reverses Lu et al. on scene description.

## Weak spots

- Only 2-3 primary human studies were read in full beyond the meta-analysis; original founding papers (Trafimow 1991, Gardner 1999, Kuhnen 2002, Hong 2000) were not opened; only described second-hand.
- Established claims rest on LLM value-survey studies, which measure values, not reasoning style.
- Eren et al. (2026) is a replication of Tao but by an overlapping method family; independence is moderate.
- K03 counts one replication; no second direct test of pronoun circling in a Western sample was found.

## Seen only in snippets or abstracts

Wu 2021 talk abstract (c25), Wagner 2025 flower categorisation (c27), Hong et al. 2000 (a10, b24), Kuhnen and Oyserman 2002 (a09, c26), the "digital replication" (a21), Lu et al. 2025 full text (a16, b18; read via PsyPost for c06), Mishra and Bost effect statistics, the EA Forum pilot (blog, charts unread).

## GAPS

1. Does any prefix cue (SDFF-style reflection, pronoun circling, "average person from X") change accuracy on reasoning benchmarks at equal tokens, versus a neutral prefix? No study found does this.
2. Does a task-structure cue (explicit "consider what may change", "what is shared among the parties") beat a culture label on holistic-vs-analytic reasoning items? Sun and Wang suggest yes; demand effects not separated.
3. What does the full Lu, Song and Zhang paper report (effect sizes, items, prompt text), and does the persona cue replicate on current models with many items?
4. What are the real founding numbers (Trafimow 1991, Gardner 1999, Kuhnen and Oyserman 2002, Hong 2000), and did any Western-sample preregistered replication of pronoun circling or SDFF exist (Many Labs type)?
5. Is the human null a weak prime or a fixed trait? Do compliance-filtered analyses (a21 claim) hold, and is there an LLM analogue (check the model followed the cue)?
6. Do orientation cues generalise across models: how do Claude, Gemini and open-weight models respond to the same cue panel, with per-model signs?
7. Can a post-cue measurement step (compare to a reference, revert if worse) recover the 19-29% of targets where the persona cue backfires?
8. Does sycophancy to a claimed identity (Jeripity Venkata) explain persona-cue gains, and can a cue with no identity claim (task-only framing) give the same shift?
9. Does cue effect on reasoning style depend on baseline holistic/analytic default of the model (Jin et al.) in the same way human baseline moderates it (Jiang and Sui)?
10. Are there any computational models of priming or accessibility-times-applicability (Hong et al.) to fix when a cue should help versus hurt?

## Gap search results (evidence_d.jsonl, d01-d17)

Limits of this pass: arXiv, Semantic Scholar and OpenAlex APIs were rate-limited, the WebSearch budget was spent, and the Nature papers were paywalled. Crossref, OSF API and arXiv abstract pages worked. Evidence marked opened:false is abstract only.

**Closed or mostly closed**
- Gap 4 (partly): a pre-registered, close, digital replication of Kuhnen and Oyserman Study 2 in Waterloo students exists (OSF t34kf). The pronoun prime worked among full compliers (N 87, d .47-.52), weakly at partial compliance (N about 157, d .26-.30) and not without a filter (N 193, d .10-.15, p>.25). Close replications pooled: d .35 over three labs. No Many Labs run of pronoun circling or SDFF was found. The Gardner 1999 Chinese null (K03) is now contested, not settled: the prime can work if people follow the task.
- Gap 5: the human null looks like a weak, dose-dependent prime, not a fixed trait, and compliance-filtered analyses do hold, but the cut-off was not pre-registered and filtering breaks randomisation. LLM analogue: log whether the output obeyed the cue and report both numbers (claim K17).
- Gap 7 (analogue only): Jekyll and Hyde chooses between persona and neutral answers with a judge. Gains of about 1-2 points over persona alone (GPT-4 92.28 to 93.15; llama3-8B 82.32 to 84.23) and a recovery where persona hurt (llama3 CSQA 72.29 to 74.97). Item level: persona flips 15.75% of AQuA items up and 13.78% down. Cost is extra calls, and no culture cue was tested (K19).
- Gap 1 (partly): wide persona tests show no mean gain (162 roles, 2,410 questions, 4 families). Role-play can help via chain-of-thought triggering (AQuA 53.5 to 63.8). No orientation-prime prefix at equal tokens was found (K16, K18).
- Gap 6 (partly): per-model signs differ for role personas (GPT-4 up, llama3 flat or down on 7 of 12 sets). No Claude or Gemini result on an orientation cue panel was found. Baseline value profiles differ by vendor (Gemini, ChatGPT, DeepSeek).

**Still open**
- Gap 2: task-structure cue vs culture label with demand effects separated. No new source.
- Gap 3: the full Lu, Song and Zhang paper is paywalled; its prompt text, items and effect sizes were not obtained. Persona-cue replication on current models unknown.
- Gap 8: sycophancy is a plausible mechanism (Sharma; warm-tuned models +10 to +30 points error) but no identity-claim vs identity-free comparison exists (K20).
- Gap 9: baseline-moderation in LLMs untested (K21).
- Gap 10: no computational model of accessibility times applicability for LLM cues was found.

Direct experiments needed for gaps 1, 2, 8 and 9 are listed in the agent_test fields of K16, K20 and K21.
