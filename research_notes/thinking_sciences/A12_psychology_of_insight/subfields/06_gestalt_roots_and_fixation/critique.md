# Critique: A12.06 Gestalt roots and fixation (cross-check)

## What was re-opened this session
I re-read the arXiv PDFs behind the most load-bearing LLM numbers, plus Wikipedia wikitext and PMC for two human numbers.

| Number | Source re-opened | Result |
|---|---|---|
| Humans 285/494 walls, 1405/1976 groups | Naeini 2023 PDF | confirmed |
| GPT-4 walls 6,4,5,7,3 (orig), 59,57,62,68,55 (Randomized), 471,304,279,298,378 (WordNet) at 0/1/3/5/10 shot; GPT-4 0-shot 239 groups | Naeini 2023 PDF (raw text order) | confirmed (the -layout text interleaves rows; raw text resolves it) |
| MacGyver 65.1% human, 79.3% vs 73.3% majority | Tian 2023 PDF | confirmed |
| MacGyver error shares 42.4 / 17.7 / 16.9+9.5=26.4 | Tian 2023 PDF | confirmed from paper text |
| Shidara 0.751 (CI 0.738-0.763) vs 0.66 (0.55-0.75); human-miss set 20/100, 36% vs 73%, 55.0% | arXiv 2601.11866 | confirmed |
| CresOWLve 2,061 examples, -6.08% to -17.21% | arXiv 2604.03374 | confirmed |
| Illusion of Insight 6.31%, about 7.6%, +8.41pp (0.3221 to 0.4062) | arXiv 2601.00514 | confirmed |
| Sheridan and Reingold N=34, 17+17, mean rating 2223 | PMC3790829 | confirmed (other numbers not re-checked) |
| Frank and Ramscar 23% baseline | Wikipedia wikitext (Functional fixedness) | 23% confirmed; 55% and 47% not re-read |
| MedEinst 5,383 cases, ECR-Agent 69.49/24.21/33.75, GPT-5 failure split 35/43/22 | arXiv 2601.06636 | confirmed, but see correction 3 |

## Corrections made
1. **MacGyver counts (evidence c04 is wrong).** c04 says "1,306 human-checked (1,073 solvable, 233 unsolvable)". Table 1 of the paper: 1,306 solvable (77.6%), 377 unsolvable (22.4%), total 1,683. Of the 1,306 solvable, 1,073 (82.2%) need unconventional tool use and 233 (17.8%) are conventional. a19 and a20/b23 were right. Claim K15 uses the correct split.
2. **MacGyver error row labels (c06 vs b24 vs paper text).** c06 calls 16.9% "unnecessary steps" and 9.5% "unavailable tools". The paper text says wrong tool usage 42.4%, not achieving the goal 17.7%, and the two hallucination types (unavailable tools 16.9%, unfaithful to constraints 9.5%) sum to 26.4%. Claim K16 follows the paper text. The table rows themselves are garbled in the PDF text.
3. **MedEinst accuracy figures (b29, c07, c08).** The paper text (section 5.2 and appendix) says GPT-5 and Gemini-2.5-Pro reach the highest baseline accuracy "54.30% and 53.58%". Its own Table 1 puts GPT-5 at 40.51 baseline, 11.40 robust, 51.87 trap rate, and puts 54.30 and 53.58 on the small medical models Lingshu-7B and Llama3-Med42-8B. The text also says MDAgent and DyLAN robust accuracy is "~8-10%", while the table shows 3.20 and 1.19. The paper contradicts itself. The trap rates (Gemini 60.90, Claude-Sonnet-4.5 42.98) are consistent in both. Anything quoted from MedEinst should use trap rate, not baseline accuracy, until the authors fix it. Table rows could also be shifted by PDF extraction, so treat the table reading as probable, not certain.
4. **Frank and Ramscar:** a02 says 25% to 50%, a04/b04 say 23% to 55%. The 23% is confirmed in wikitext; the Candle-problem page text did not surface the 25/50 figures in a raw search, so prefer 23/55 until the 2003 paper is opened.
5. **Luchins "483 children" (b13).** The Wikipedia wikitext I searched does not contain 483, and the "3 of 98" speed-test figure was not found either. The 70/58/98/97 percentages are on the page. Treat the 483 and 3/98 figures as unverified. The page does give 140 fifth-graders, 79 college students, 21 adults for the age study.

## Contradictions between sources
- Frontier models and fixation: M-ARC 2025 (most LLMs under 50%, physicians 66%) vs Shidara 2026 (Claude 4.1 Opus 0.751, level with physicians) vs MedEinst 2026 (trap rates above 50%, no size link). The same word "Einstellung" covers different tasks, so these are not directly comparable. M-ARC became public in 2025, so contamination could explain the 2026 gain.
- Zhang 2025 (rebus: GPT-4o beats humans) vs Naeini 2023 and Tian 2023 (models far below humans). Task type, model generation and human sample all differ.
- Self-reflection: MacGyver GPT-4 -9.7 infeasible, but no help for Claude2 and Llama2-13b; Illusion of Insight says spontaneous reframing does not help but gated prompts do.
- Human Einstellung: speed cost, not accuracy (anagrams, chunk Exp 2) vs accuracy cost (chunk Exp 1, Luchins).

## Weak spots
- **The classic human half is almost all Wikipedia.** Duncker 1945, Luchins 1942, Maier, Glucksberg 1962, Adamson 1952, Birch and Rabinowitz 1951, Frank and Ramscar 2003, Weisberg and Alba 1981, Bilalic 2008, Vul and Pashler 2007, Kohler 1917 were not opened as primary papers. No N for any of them. "Established" for K01, K02 and K07 rests on agreement among secondary summaries and on three modern primary studies (Sheridan, Ellis, Huang) for K07.
- **LLM results are mostly one paper per claim.** Naeini and Tian are the only direct decoy and unconventional-tool studies; no replication seen, no confidence intervals, single runs.
- **Naeini confound:** OCW-WordNet is easier by category type, not only decoy-free. Only the Randomized result (6 to 59 walls) is a clean decoy removal, and it is still small in absolute terms.
- **No study tests a scaffold that names the fixation (S1/O6) against an equal-token plain baseline on a classic fixation task.** All prompting results are generic reflection or divergence.
- Several 2026 papers (CREATE, MedEinst, Shidara) use model names I cannot independently check and some data are LLM-generated and LLM-filtered.
- Evidence files include a28, a29, b32-b34 and c30 flagged as not opened or abstract only; they were not used for numbers.
- The "chimpanzee 2024" and Tran 2021 lines rest on a review text with no N for most studies.

## Only seen in snippets or summaries
Wikipedia (a01-a15, b01-b09, b13, b14, b20, b31); abstract only: a23, a24 (later verified in the PDF), c30; recalled only: a26-a29, b32-b34.

## GAPS (most decision-relevant first)
1. Does a naming-style operator (S1 restate plus O6 list each object's alternative roles) beat plain prompting and a generic "reconsider" prompt at equal tokens on classic Duncker candle, nine-dot and water-jar items given to a current model? No source tests this.
2. How large is LLM Einstellung on classic water-jar sequences (Luchins) for 2025-2026 models, and does thinking budget remove it? The primary Luchins numbers (N, group sizes) also still need to be opened.
3. Is the Naeini decoy effect still present in current reasoning models (GPT-5-class, Claude 4.x, Gemini 3) on Only Connect, with chain-of-thought and with decoy-clean walls controlled for category difficulty?
4. Do the MedEinst baseline accuracy numbers in the paper text or the table hold, and does Shidara-style reasoning effort lower the MedEinst trap rate? Needs the authors' released data or a re-run.
5. Do reasoning-trace "reframing" shifts (Illusion of Insight) occur or help in large frontier models, and does uncertainty-gated reconsideration scale beyond small Qwen/Llama?
6. Primary data for the human classics: Duncker 1945 solution rates, Glucksberg 1962 N and means, Adamson 1952, Frank and Ramscar 2003 (23 vs 25, 55 vs 50), and large-sample replications or failed replications of the prior-use and incentive effects.
7. What does Weisberg and Alba 1981 and the progress-monitoring work (MacGregor, Ormerod, Chronicle) say about the nine-dot hint effect, and is there an LLM run of nine-dot or matchstick problems with hints?
8. Does fixation in LLMs track memory strength of the decoy (Beda and Smith's corollary), i.e. can we dose it by varying prompt priming strength?
9. Does multi-agent debate reduce or amplify fixation (MAD +11 points on counter-intuitive arithmetic vs MDAgent/DyLAN collapse on MedEinst)? Matched-token comparison needed.
10. Is the MacGyver gap (35-42% vs 65.1%) due to fixation or to missing physical grounding, and does a current model close it with the scaffold? Newer models were not in the paper.

## Gap search results (2026-11-03)
Search conditions: WebSearch budget was exhausted after one call; the arXiv, Semantic Scholar and OpenAlex APIs all returned rate-limit errors. Work used Wikipedia fetches, Crossref, Europe PMC full text, and arXiv PDFs. Evidence is in evidence_d.jsonl (d01-d16).

| Gap | Status | What was found |
|---|---|---|
| 1 Naming operator vs plain vs generic reconsider at equal tokens | OPEN | No study exists in the index searched (d15, claim K33). Only own pilot can answer. Related lessons: showing the alternative is not enough (d10, K29); format change without representation change does nothing (d13, K31). |
| 2 LLM Einstellung on water-jar sequences | OPEN | No paper found (d15). Luchins 483 children and N=98 speed-test figures now traced to the Wikipedia page (d01); primary 1942 monograph still unopened, no 1942 group sizes. |
| 3 Naeini decoy effect in current reasoning models | OPEN | Nothing newer than Naeini 2023 found. M-ARC peer-reviewed version (d04): best R1 52%, o1 48% vs physicians 66%, so reasoning models do not remove Einstellung-style items. |
| 4 MedEinst accuracy and reasoning effort | PARTLY CLOSED | The paper runs only zero-shot CoT; reasoning effort is never varied, so the effort question cannot be answered from it (d07). The text/table accuracy conflict remains; use trap rates. Structured scaffold cut one model's trap rate 43.46 to 33.75 (d07). |
| 5 Reasoning-trace reframing in large models | PARTLY CLOSED | Illusion of Insight appendix also tested DeepSeek-R1 and GPT-4o: shifts 1-7% of traces, no accuracy benefit (d08). Gated reconsideration at frontier scale still untested. |
| 6 Human classics primary data | MOSTLY OPEN | Duncker, Glucksberg, Adamson, Frank and Ramscar still not opened (paywalled; DTIC 403). Wikipedia confirms 23/55/47 (d03) and 25/50 on the Candle page (d02); the conflict persists. No large replication found. New human boundary evidence: habit tendency did not predict candle success (N=69, d11); 29.4% still failed after seeing the shortcut (d10). |
| 7 Weisberg and Alba, progress monitoring, nine-dot LLM run | PARTLY OPEN | MacGregor et al. 2001 Exp 1 via a secondary report: 80-93% on simplified variants, 0 on nine-dot (d14). Weisberg and Alba not opened. No LLM nine-dot run found. |
| 8 Dose of fixation by memory strength | PARTLY CLOSED (humans only) | Prior reinforcement hurt only when the answer was weakly associated, N=30, interaction significant (d12). No LLM dose test; Beda and Smith 2018 primary not opened. |
| 9 Debate: reduce or amplify | PARTLY CLOSED | Forced-opposition MAD: GPT-3.5 26.0 to 37.0, tokens 2.46x (d05, d06). Consensus prompts (level 0) and consensus-style agents are the failing design (K27 now contested). No token-matched run exists. |
| 10 MacGyver gap: fixation or grounding | PARTLY CLOSED | Authors' error coding says wrong tool usage 42.4% (physical infeasibility); humans slightly worse than GPT-4 on average attempts, possibly due to fixation (d09). Newer models never tested. |

Corrections and status changes: K07 note on 483/3-of-98; K27 changed to contested; K12 now has a human dose source; new claims K29-K33.
Still the largest hole: no equal-token test of an S1/O6 naming scaffold on classic items. Recommend a small pilot (candle, nine-dot with and without hints, a 6-problem water-jar sequence; arms plain, generic reconsider, S1+O6 name-and-try, debate; 3+ runs each).
