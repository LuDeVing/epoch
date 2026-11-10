# C04.09 Creative problem solving: cross-check critique

Checker re-opened PDFs (pdftotext) for: Sio & Ormerod 2009, Knoblich et al. 1999, Chein & Weisberg 2014, Henok et al. 2020, d'Aliberti & Horta Ribeiro 2026, Mizumoto et al. 2025, Tian et al. 2024 (MacGyver), Naeini et al. 2023.

## Confirmed
- Sio & Ormerod: 117 effects, weighted mean 0.29, CI 0.21 to 0.39, Q=173.99, variance .0834; subgroup means 0.22 / 0.26 / 0.29 (linguistic / visual / creative); 88 of 117 computed from means. The paper prints the "0.04" as a standard deviation; it is really the standard error of the mean.
- Knoblich 1999: F(3,57)=7.11, F(1,19)=14.41, Type C 61% regular-first, Type D 61% vs 69% chi2=0.22 p=.64.
- Chein & Weisberg: M=24.75 solved (SD 7.6); insight 10.14 s vs analytic 21.74 s; R2 .19 to .39.
- Henok et al.: chi2=12.42, 4.77, 5.03; 61% after switching to hands-on.
- NazoNazo: 52.9 / 7.6 / 17.6; OR 2.29; 9.42% vs 19.25%; verification failure 5.23 / 25.00 / 30.57 / 39.34; Grok 4 language 48.8% vs 29.5% p=.0071.
- MacGyver: 18.9% efficient, 37.5% infeasible, humans 79.3% vs GPT-4 73.3% majority, wrong tool use 42.4%, self-reflect -9.7 vs div-conv -4.3 infeasible, +6.5 vs +2.2 efficient.
- Only Connect: GPT-4 10-shot 6 walls / 239 groups on original; 471 walls / 1,926 groups on WordNet variant; 59 / 595 randomized.

## Corrections
1. c05 says "over 11M traces". The paper says "1M+ annotated reasoning traces" (b23 is right). Use 1M+.
2. c05 "MATH-500: 14.4% vs 32.7%" and "Crosswords exception 20.1% vs 9.6%": 32.70 and 9.65 are the overall pass-1 accuracies (not shifted vs non-shifted) in the appendix table. The shifted vs non-shifted figures were not found in the text. Treat both as unverified; do not cite.
3. d'Aliberti has two inconsistent numbers for the math second-pass gain: main table 0.3221 to 0.4062 (+8.41 pp, N=320,000 pairs) vs appendix 32.70 to 40.43 (+7.74 pp, N=464,000). Quote as "+7.7 to +8.4 pp". The appendix also gives shifted vs non-shifted for Qwen2.5-1.5B all domains as 3.95% vs 20.42% (shift rate 7.65%), unlike the 2.57% vs 16.44% (N=723,200) in the text; probably different labelling (pass-1 labels). Direction is the same.
4. b24 "-7.40 / -22.88 pp" are Math-only strata; c06 wording is fine. Rush Hour "+0.01 pp" and raw values (0.000233 to 0.000363) agree.
5. b02 says creative tasks "gain most"; the table gives creative 0.29 vs visual 0.26 vs linguistic 0.22, and the authors' own moderator test reported only a modest difference. Claim K05 is marked contested.
6. b01 says "Unweighted mean 0.36", not re-checked.
7. a06 table count (13/30 vs 11/29) is already flagged in the evidence file.

## Contradictions between sources
- Pauses help (Sio & Ormerod d=0.29; Segal fresh look) vs unconscious thought advantage fails in a large replication (Nieuwenstein, N=399) and the Cai REM study shows time alone suffices. Resolution: break effect exists; mechanism does not matter for us.
- Gilhooly (favours unconscious work) vs Chein & Weisberg (business as usual) vs Ritter (distraction helps selection, not generation).
- Reasoning-model "aha" (DeepSeek R1) vs d'Aliberti (rare, harmful). The R1 claim was anecdotal.
- Zhang 2025 / Orru 2023 (models match or beat humans on verbal insight) vs NazoNazo / BrainTeaser / Only Connect (models far below humans). Likely explanation: old, public, easy items vs new items; contamination not ruled out.
- Haq 2025: complex-first helped, opposite of human Einstellung.
- Self-reflection helps GPT-4 (MacGyver) but not Claude2 or Llama2; d'Aliberti shows free-running shifts hurt, forced ones help.

## Weak spots
- Several key LLM claims rest on one paper each (NazoNazo, d'Aliberti), and NazoNazo is counted three times in the files (a20-22, b20-22, c01-04). They are one source.
- d'Aliberti uses small models (Qwen2.5-1.5B) for most numbers; shifts detected by LLM judge and lexical cues.
- Haq 2025: 6 items per cell, no stats.
- Sadeghi 2024 table is a submission log, not an ablation; Fine-tune numbers have an uncertain column mapping.
- MacGyver ablation: 180 problems, no significance tests.
- Human data on interactivity (Henok) and necklace are single-problem studies.
- Verification failure uses literal string match; could be partly accidental mention.

## Seen only in snippets / not opened
- Nieuwenstein 2015: abstract only (k and pooled effect not seen; the JDM PDF did not download).
- Cai 2009: fetched summary, not full text.
- Orru 2023: abstract only. Raz 2024 (c25): second-hand. Jones 2003 (c30), Helie & Sun 2010 (a18), Duncker 1945, Weisberg & Alba 1981, Kaplan & Simon 1990, Danek & Wiley, Dodds et al. 2003: second-hand or from memory.
- Segal 2004, Smith 1995, Strick 2011: second-hand via Gilhooly.
- Sio & Ormerod, creative-moderator regressions: only the key rows re-read.

## GAPS
1. Does an uncertainty-gated forced reconsideration help a strong modern model on genuinely insight-type items (not math), at equal tokens? d'Aliberti shows near-zero gains on crosswords and Rush Hour.
2. How much of the NazoNazo gap is retrievable-by-scaffold: do a candidate ledger plus commit-by-check recover the 5% to 39% verification-failure answers, and what is the false-commit cost?
3. Is there a replication of NazoNazo-type results with fresh items (post-cutoff, other languages) and with 2026 models? Contamination of old insight sets (Orru, Zhang) is unmeasured.
4. Does an explicit "name constraints / split chunks" operator beat generic retry on LLMs (matchstick arithmetic or its text analogues), and does the human result that tautology exposure removes only constraint difficulty transfer?
5. What is the effect size of a context reset (drop failed attempt, fresh sample) on LLMs after impasse, as an analogue of fixation forgetting? No direct LLM test was found.
6. What is k and the pooled effect of the Nieuwenstein meta-analysis, and are there other large failed replications of incubation on insight (not decision) tasks since 2015 (e.g., many-labs-style)?
7. Does reasoning about a physical or concrete object (externalised state, code, tools) raise LLM insight scores the way hands-on interactivity did for humans (Henok)?
8. Which trigger works better for impasse detection: step count, sample disagreement, token entropy, or progress-monitoring (hill-climb stall)? No head-to-head found.
9. Are insight-rating scales for LLM outputs (self-reported "aha") calibrated against correctness, as human false-insight studies imply they are not?
10. Do short targeted hints beat long ones in a controlled ablation on lateral puzzles (Sadeghi data are uncontrolled)?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d16). Claims K24 to K29 were added; K02, K11, K12, K14, K15, K21 got new evidence ids. Note: web search budget was used up and the arXiv API and Semantic Scholar rate-limited (HTTP 429), so coverage is limited to papers I could open directly.

- Gap 1 (gated reconsideration on real insight items, equal tokens): STAYS OPEN. No test on insight items. Related: Huang 2024 shows ungated self-review lowers accuracy (GPT-4 GSM8K 95.5 to 89.0 after two rounds) (d08); CresOWLve shows thinking effort helps (GPT-5.4 9.4% to 17.8%) but not at equal tokens (d02).
- Gap 2 (candidate ledger plus commit-by-check): PARTLY. No direct test. d08 supports gating on an outside check; d13 shows retry after a verified-wrong signal gives gains that plateau. Cost of false commit not measured.
- Gap 3 (fresh items, 2026 models, contamination): PARTLY CLOSED. CresOWLve (2026 models) still under 30% for most; contamination measured for one model: 73% vs 25% chance (d01, d03). Fresh post-cutoff items in other languages still untested for the scaffold.
- Gap 4 (name-and-widen-constraints operator vs generic retry): OPEN. Only a human study found on functional fixedness with LLMs (d14), which is not relevant.
- Gap 5 (context reset effect size): PARTLY. No direct test. Nearest: equal-token fresh samples beat 'Wait' extension, up to 22 pts, and -11.8% vs +10.1% for a 1.5B model on GSM8K (d09, math only).
- Gap 6 (Nieuwenstein numbers; other failed replications): NUMBERS CLOSED, second half OPEN. k=61, g=0.15 [0.03, 0.26]; trim-and-fill g=0.018; replication N=399, BF 7.83 for null (d05, d06). The paper has no insight tasks (d07). No post-2015 large insight-incubation replication found, but the search was blocked, so this is not a negative result.
- Gap 7 (externalised state / tools): OPEN. Nothing found beyond MacGyver (c16 to c18).
- Gap 8 (best impasse trigger): OPEN for head-to-head. Hidden-state probe is calibrated (ROC-AUC above 0.7, ECE below 0.1, 24% fewer tokens) but needs model internals (d10).
- Gap 9 (is aha / confidence calibrated?): PARTLY. Aha text does not go with accuracy (d11); self-review cannot judge its own correctness (d08). No test of verbalised 'aha' after a reframe on insight items.
- Gap 10 (short vs long hints, controlled): OPEN. LatEval varies clue amount (0/50/100%) and strong models gain, weak do not (d12); hint length not varied.

Corrections to earlier notes: none new. The Nieuwenstein result is about decision tasks, so K02 should not be read as a failed replication of insight incubation.

Also: one fetch of a search-engine results page was made by mistake and returned an error; it was not used.
