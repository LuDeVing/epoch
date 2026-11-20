# Critique: Prospection and mental time travel (A18.05)

Cross-check date 2026-11-19. Sources re-opened this session: Martin 2021 (PMC8651407), Boeckle 2020 (PMC7735258), Redshaw and Suddendorf 2013 (PMC3705196), Amodio 2021 (PMC7804264), Davies 2025 (PMC11880068), and arXiv pages or HTML for TriggerBench (2606.23459), Chopra 2026 (2605.14177), Mittal 2026 (2603.23530), PM-Bench (2607.12385), CheeseBench (2604.10825), Poonsiriwong 2025 (2512.05397).

## Numbers confirmed (10)
1. Amodio 2021 Exp 1 posterior 0.997 (best model), Future Planning 0.0014, Compensatory Caching 0.00001 (a07, b02).
2. Martin 2021 compartment effect F(1,15)=12.18, p<0.001; interaction F(1,15)=3.23, p=0.09 (a09).
3. Boeckle 2020 table: Neptune 9/10, Uranus 7/10, Triton 7/10, Saturn 3/10 p=0.429 (a15, b09).
4. Redshaw and Suddendorf 2013: instant 91.7% vs chance 16.7%, chi2=97.20; condition F(1,22)=12.79, p=0.002 (b11).
5. Davies 2025: W=4, p=0.068, noted as the lowest achievable p for that N (a18).
6. TriggerBench: AIME correct 272 / 47.1% vs wrong 143 / 37.8%; Qwen3-235B-Think 74.86%; GPT-5.2 high 43.94% on negative controls (b24, c08, c10).
7. Chopra 2026: PGR-TOT recall 0.723 vs Mem0 0.256; query-only 0.58; TOT vs COT 0.723 vs 0.718, win 55.67% (c01, c02).
8. Mittal 2026: mean drops DeepSeek 10.2, o4-mini 8.9; 5xGSM8K DeepSeek 72.2 to 100, Llama 70.4 to 98.1 (c04, c06).
9. PM-Bench: heartbeat 65.1% macro Set-F1, todo ledger 62.8%, cross-day hit 50.0%, update 44.4% (b26).
10. Poonsiriwong 2025: 34.2% vs 10.8% (p=0.015); 20.0% vs 2.7% (p=0.019) (b21).

## Corrections and discrepancies
- CheeseBench (c14): the arXiv abstract page (labelled v2) says best open-weight model 52.6% and random 32.1%. The full-text HTML says 68.0% and 38.0%, plus the frontier table (Opus 4.7 86.7%). The evidence lines match the full text. The two differ, so there may be a text-version mismatch. Use the full-text numbers with this warning.
- Amodio 2021 bird counts: a07 says Exp 2 had 6 birds tested of 7; b03 says 7 birds tested. The paper says 7 took part in the test phase and 6 received the test trial (one bird was stopped on welfare grounds). Use 7 entered, 6 tested.
- Amodio calls the Raby birds California scrub-jays; our other lines say western scrub-jays. Same study, naming varies.
- Mittal 2026: DeepSeek model is V3.1 (a/c lines are consistent); abstract says GSM8K accuracy can drop from 93% to 27% for one model, not recorded in the evidence lines.
- Martin 2021: 3 of 6 birds did not cache in the breakfast-choice experiment, which weakens that experiment; added to claim K03.

## Contradictions between sources
- Raby 2007 (positive) vs Amodio 2021 and Martin 2021 (null or reversed). Species differ (western scrub-jay, Eurasian jay, Canada jay), so this is not a clean failed replication of the same species. No one has re-run the exact design in western scrub-jays.
- Cheke and Clayton 2012 (positive, N=4) vs Amodio 2021 (null with a larger design from the same lab).
- Episodic-like memory: Clayton and Dickinson 1998 vs Davies 2025 (4 birds, p=0.068, unclear pattern).
- Spoon test: Boeckle 2020 pass vs Esteve and Santariello 2021 (training could explain results).
- Reasoning effort and PM: TriggerBench shows gain (+13.91) but also false alarms; CheeseBench shows chain-of-thought hurts one model. Tasks differ.

## Weak spots
- Raby 2007 and Correia 2007 primary counts were never read (paywalled); jay effect sizes come second-hand.
- Several evidence lines (a11, a13, a14, b07 as snippet, b08, b13, b14, b19, b20, a25) rest on abstracts or citations only.
- Meta-analyses b19 and b20 were not opened (opened:false); numbers come from abstracts.
- Most LLM results are single-paper, recent (2026) preprints, no independent replication. Several use different PM definitions (formatting constraints, latent triggers, intention ledgers).
- No study tests LLMs on a caching or future-need paradigm. Evidence for "prospection" in LLMs is only analogical.
- Human EFT meta-analyses measure delay discounting, not planning quality.

## Seen only in snippets or abstracts
a11, a13, a14, a21, a22, b07, b08, b13, b14, b19, b20, a25, c12, c21 (abstract-level), c18 (ablation numbers).

## GAPS
1. What are the exact cache counts and statistics in Raby et al. 2007 and Correia et al. 2007 (primary text)?
2. Has anyone re-run the Raby breakfast design in western scrub-jays with larger N, and with pre-registration?
3. Does a prospection-style scaffold step (imagine future needs, then plan) beat a plain scratch-note baseline on an agent task at equal tokens?
4. Does a typed intention ledger (PM-Bench style) hold up on other benchmarks, and with Claude models?
5. Are the TriggerBench and Mittal reminder effects the same for strong reasoning models, and what do reminders cost in tokens?
6. Do the two EFT meta-analyses (g=0.44, g=0.52) survive an independent read, and which moderators carry over to LLM "imagery" prompts?
7. Which version of CheeseBench has the correct headline numbers, and does the radial-arm gap hold for frontier models beyond Opus?
8. Is there any LLM study that tests caching-for-future-need or Bischof-Kohler-style choice (current need vs future need) directly?
9. Is the spoon-test result (Boeckle 2020) robust to training-history controls, and has it been run on more crows or other species?
10. Do LLM agents show the "spread caches evenly" pattern (Amodio) when given hunger and location states, i.e. do they track future need or only hedge?


## Gap search results

Date 2026-11-19. Evidence in evidence_d.jsonl (d01-d21). Web search was unavailable (budget used up), and arXiv API, Semantic Scholar and OpenAlex were mostly rate-limited, so work used Europe PMC, PMC pages, arXiv HTML and arXiv listing search.

1. Raby 2007 and Correia 2007 counts: STAYS OPEN. Raby is paywalled (abstract and figure captions only, d01). Correia full text was blocked for automated download (d02). Claims K01 and K05 stay marked as second-hand. A human with a browser can fetch the Correia PDF that Semantic Scholar lists as open access.
2. Re-run of the Raby design in western scrub-jays: CLOSED, NEGATIVE. No large-N or pre-registered re-run was found. Farrar, Boeckle and Clayton (2020) say the Cambridge lab no longer houses scrub-jays and only one other lab publishes on their caching (d05). The only same-design re-run is Martin 2021 in Canada jays, N=6, opposite direction (d04). Amodio 2021 lists design differences (d03). New claim K27.
3. Prospection scaffold step vs plain scratch notes at equal tokens: STAYS OPEN. No such test was found. Nearest items are Pro-Memory token accounting (d10) and a learned thinking policy on synthetic tasks (d21).
4. Typed intention ledger on other benchmarks and with Claude: MOSTLY CLOSED. Pro-Memory (2611.05731) reports Claude Sonnet 4.5 and Haiku 4.5 on PM-Bench and ProactiveBench (d09, d10). ProMemAgent gives CPMBench (d11), PIS adds small models (d12), and a ledger on a synthetic TriggerBench-like set shows recall@5 0.000 to 0.955 (d13). Caveats: all are preprints with the authors' own methods, and on GLM-4.7 the baseline RWM beat Pro-Memory on PM-Bench (0.7218 vs 0.7068). K18 moved to status replicated-preprint (new label; independent_sources 4).
5. Reminder effects for strong reasoning models and token cost: PARTLY CLOSED. TriggerBench shows GPT-5.2 (high) at 75.02 at 40K context but only 39.80 on negative-clean (d15). Mittal Table 3 shows the reminder costs main-task accuracy, o4-mini GSM8K x3 93.3 to 26.7 (d14). Pro-Memory whole-run token totals are in d10. No study measures the token cost of a trailing reminder itself, and no recent frontier model was tested with it. New claims K29, K30.
6. EFT meta-analyses independent read: PARTLY CLOSED. Both abstracts were re-read from Europe PMC and match the earlier lines (d16, d17). Full texts were not read (the OSF PDF had no text layer). Moderators that plausibly carry to an LLM prompt: concreteness and link to the choice. K11 keeps status established at abstract level. New claim K32 (no LLM efficacy test yet).
7. CheeseBench version: CLOSED. v1 (12 Apr 2026) reports 52.6% vs 32.1% random for six open-weight models. v2 (15 May 2026) reports 68.0% vs 38.0% and seven frontier models. The arXiv abstract page labelled v2 still shows the v1 numbers (d07, d08). Radial-arm gap holds for open-weight models and closes for Claude Opus 4.7 (100%) and 4.6 (90%) but not GPT-4.1 (0%); frontier runs have only 10 trials per environment. K21 rewritten.
8. LLM test of caching or Bischof-Kohler choice: STAYS OPEN (no hit). About 10 more arXiv listing queries found nothing (d19). Closest: the delay-of-gratification micro-benchmark (d18, K31), which is persona-driven waiting, not a future-need choice.
9. Spoon-test robustness: STAYS OPEN. No extra crows or second lab. The authors' 2021 reply (d06) argues that past reward cannot explain the result but gives no new data. K07 note updated.
10. LLM agents spreading caches (Amodio pattern): STAYS OPEN (no study found, d19). Would need a new experiment.

Corrections to the earlier critique: the CheeseBench conflict is a version difference, not an error. Status vocabulary now includes replicated-preprint (K18 only).
