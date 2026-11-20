# NDM in sport: deep document

*Subfield E04.08. Scope: recognition-primed decision making (RPD) in athletes, with Bossard et al. 2022 as the anchor. Evidence files: evidence_a-d.jsonl; claims K01-K20 in claims.jsonl; cross-check in critique.md. Ids such as a02 or K08 point to those files. Earlier general NDM material (Klein's founding firefighter studies, the RPD model itself) lives in the sibling document "Naturalistic decision making" and is not repeated here.*

## 1. What it is

Naturalistic decision making (NDM) studies how experts decide in real, fast, high-stakes settings. Its main model is recognition-primed decision making (RPD). In RPD an expert does not compare options. The expert sees the situation, recognises it as a typical case, and the case brings a likely action. If the action looks wrong in a quick mental run, the expert adjusts it or takes the next one.

Sport is a good test field. Decisions take under a second to a few seconds. Athletes are real experts. Video and eye tracking exist. Time pressure varies a lot between roles (a goalkeeper facing a shot, a defender far from the ball, a rugby coach at half time).

Bossard et al. 2022 (Frontiers in Psychology, opinion article, opened) is the standard recent summary for sport. It names RPD's three levels and gives usage rates (a01, a02):

| RPD level | What happens | Share of expert decisions (Macquet 2020, quoted in Bossard) |
|---|---|---|
| Level 1, simple match | Situation recognised, typical action comes to mind, done | 60-81% |
| Level 2, diagnosis | Situation unclear, expert looks for more cues, builds a story | 13-28% |
| Level 3, evaluation by mental simulation | Expert runs the action forward in the head to check it | 3-24% |

Important correction (critique.md, K03): Bossard also says experts choose "their preferred first option in 80% of decisions". That sentence has no citation and no sport or sample (d05). It is about option generation, not about the RPD match rate. Several earlier notes (a04, b01, c01) blurred the two. Do not use 80% as a prior.

Why it matters for our agent: the schema already has a fast path (direct mode) and a triggered slow path (S6, G1). Sport gives numbers for how often a fast match is enough in humans, and a list of conditions that push experts to the slow path. It also gives a warning: the human evidence is mostly interview work, so the rates are soft.

Scope limit: there are no tests of RPD in an LLM on athletes' decisions. The only close LLM test is in medicine (Kopka and Feufel 2026). See sections 6 and 9.

## 2. History and theories in depth

**Origin.** Klein and colleagues built RPD from fireground commander interviews in the 1980s. The claim: experienced commanders rarely compared options. They matched the scene to a prototype and acted. That work is covered in the general NDM document, not here.

**Move into sport.** Sport researchers took RPD up because decisions are fast and experts are easy to find. The usual method is retrospective: show the athlete a video of their own play (self-confrontation interview), ask what they saw and thought, then code the speech into RPD levels. Bossard lists about 20 such qualitative studies across a dozen sports: badminton, volleyball, soccer, ice hockey, handball, basketball, judo, karate, rugby coaches, adventure coaches, officials (a01).

**Key studies (sport).**
- Macquet 2009, volleyball, n=7 professional men; Macquet and Kragba, basketball, n=7 elite women (a08, a21). Interview studies that showed recognition within the decision process. Only the sample sizes were read, second-hand.
- Kermarrec and Bossard 2014, soccer defenders, 118 defending situations: simple match 60% (68), simulation 23% (26), diagnosis 16% (18). The three sum to 99. Second-hand via Le Menn (a15, a23).
- Le Menn et al. 2019, handball goalkeepers, 83 accounts: simple match 46% (38), simulation 34% (28), diagnosis 20% (17). The test of the process mix was not significant, chi2(2)=1.044, p=.593 (a13, a14). The "salient features" coded were cues 44%, expectancies 22%, actions 18%, knowledge 10%, goals 4%, consequences 2% (419 units).
- Collins, Collins and Carson 2016, coaches, N=18 (10 adventure sport, 8 rugby union): rugby coaches estimated their own decisions as about 30% intuitive (range 5-40%), one adventure coach said about 90% (a16, b07). Only 2 of 8 rugby coaches reflected regularly (b08).
- A rugby union study (N=16, 2021) found the mix shifts with the time available (d17). No rates in the abstract.

**Option generation line (a rival or companion theory).** Johnson and Raab 2003 proposed Take The First (TTF): experts generate options in order of validity and the first is usually good, so more options hurt. Related work: Raab and Johnson 2007 (same option count across expert, near-expert and non-expert, quality differs, d10), Raab and Laborde 2011 (N=54 handball players; deliberators less successful, b10, d09), Hepler and Feltz 2012 (N=72 students, TTF used on 70% of trials, b09), Musculus et al. 2019 (N=169 soccer, less is more, b06; a separate developmental study N=73 children, b12), Klatt et al. 2019 (more options, higher accuracy in Brazilian players, b13, d08). Del Missier et al. 2014/2015 (N=141, non-sport) found option fluency did not predict choice quality (r from -0.01 to 0.08 across scenarios, b16) but more options raised the best option and lowered the set mean (d07).

**Rival frameworks.** Ashford, Abraham and Poolton 2021 (a07, b04) reviewed 53 studies (2,078 participants: 2,021 players, 57 coaches): 25 information-processing, 18 ecological dynamics, 10 NDM. Most use decontextualised video tasks. So NDM rates cannot be compared cleanly with the other paradigms (K16). Raab and Gigerenzer 2015 (b14) give the fast-and-frugal view: simple heuristics such as the recognition heuristic beat rankings in Wimbledon forecasts (127 matches), with validity learned from feedback. North et al. 2011 give two memory models with opposite-sign predictions (b15, second-hand).

**Open theory points raised by Bossard (a03, a05, b03).** The intuition-analysis continuum is unproven. There is no consistent evidence for how intuition develops. Six research avenues and three emotion hypotheses are proposed, with no data.

**AI-side history.** Computational RPD models exist: Fan et al. 2005 (extended RPD, agent teams), Fan and Yen 2008 (Team-RPD), Nowroozi et al. 2012 (general computational RPD), Hu et al. 2018 (pilot behaviour in midair encounters) (c20-c23). All were seen only as citation records. Bossard names zero AI studies (c02).

## 3. Core findings with exact numbers

Status follows claims.jsonl: established / single-source / contested. "Second-hand" means quoted from another paper.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Most expert sport decisions are simple matches | 60-81% match; 13-28% diagnosis; 3-24% simulation | Macquet 2020 via Bossard 2022 (a02, d06) | established as a range; Macquet chapter unopened |
| Goalkeeper mix differs from the range | 46% match, 20% diagnosis, 34% simulation; 83 accounts | Le Menn 2019 (a13) | established (K01, K02) |
| Defenders: match dominant | 60% / 16% / 23%, 118 situations (sums to 99) | Kermarrec and Bossard 2014 (a15) | second-hand |
| Process mix did not differ across groups | chi2(2)=1.044, p=.593 | Le Menn 2019 (a14) | single study |
| Mix moves with time available | rugby N=16; far from the ball more simulation and diagnosis | Bossard 2022; rugby 2021 (a03, d17) | qualitative |
| "80% first option" is an option-generation claim, source not named | 80% | Bossard 2022 sentence (d05) | single-source (K03) |
| TTF used on most trials | 70% of 13 trials x 2 tasks, N=72 | Hepler and Feltz 2012 (b09) | abstract only |
| More options: best option better, set mean worse | N=141, ill-structured non-sport problems | Del Missier 2014 (d07) | single-source |
| Option fluency does not predict choice quality | r = -0.01 to 0.08 | Del Missier 2015 (b16) | non-sport |
| Fluency stable across problems, best-option quality not | r=0.46 vs r=0.17 | Del Missier 2015 (a18) | non-sport |
| Deliberators less successful than intuitive players | N=54 handball | Raab and Laborde 2011 (b10, d09) | abstract; no effect sizes |
| Less is more | N=169 male soccer players | Musculus 2019 (b06) | not reopened |
| More options, higher accuracy | Brazilian players, N not in abstract | Klatt 2019 (b13, d08) | contested (K04, K20) |
| Self-estimated intuition share is small and unstable | about 30% rugby, range 5-40%; one adventure coach 90%; N=18 | Collins 2016 (a16, b07) | single-source (K06) |
| Creative players: more fixations per second | d=0.91 (locations/s), d=1.32 (fixations/s), fixation duration d=1.24; N=44, groups of 11 | Roca 2018 (a12, b19) | single-source; extreme groups |
| Creative players find threats faster | 2164 vs 3798 ms (d=1.58); time on threatening attacker 19.1% vs 10.7% (d=1.84) | Roca 2018 (a12) | single-source |
| Creativity score gap between extreme groups | t(20)=12.75, d=5.36 | Roca 2018 (a11) | inflated by the extreme-group split; do not cite |
| Experts make fewer fixations in individual sports | SMD -1.52 (95% CI -2.38 to -0.65); duration SMD 0.93; locations SMD -1.27; 26 studies, N=611 | 2026 meta-analysis (d16) | meta-analysis; abstract only |
| Elite handball players choose offensive responses more | OR 2.76-3.00, N=44, left-handed attacks only; no expertise effect on decision time | Hinz 2022 (b18) | single-source |
| Video-feedback and questioning programme | 55.54 to 61.20% vs 58.65 to 54.95%; N=11; F(1,9)=19.318, p=.002 | b23 | single, tiny |
| Video training, quarterbacks | N=4; one player +60 points rate difference accuracy, +80 reaction time | Powless 2020 (b20) | single-case |
| Pitch-recognition test vs batting | r=0.53, p=.052; test-retest r=0.707, p=.117 | b22 | not significant |
| Youth decision-making reviews | 26 articles of 6,215 records; no pooled effect | b21 | review |
| LLM on SportQA, GPT-4 5-shot CoT | L1 85.63; L2 78.82; L3 73.58, 64.08, 34.40, 23.01 (easy single, hard single, easy multi, hard multi). Humans 96.63 and 96.02 on L1 and L2 | Xia 2024 (c03) | established (K09) |
| SPORTU text and video | GPT-4o 71% best text; Qwen2-VL-72B 70.94% video overall, 44.12% hard | Xia 2025 (c06) | opened |
| Reasoning first hurts on hard sport video | Claude-3.5-Sonnet 52.57% direct vs 39.32% rationale-first | SPORTU (c07) | established as a pattern (K10) |
| Models disagree across camera angles | all angles correct: Claude-3.5-Sonnet 52.86%, GPT-4o 47.42%, Gemini 1.5 Pro 43.24%; mixed 28-39% | SPORTU (c08) | single-source (K11) |
| RPD prompt on triage | 63.3% default; 67.6% RPD; 66.7% data-frame; OR 2.26 and 2.05; 10 models x 45 vignettes x 10 repeats | Kopka and Feufel 2026 (b24, d01, d02) | single-source (K08) |
| Where the triage gain is | self-care 13.4% to 29.8% (13 cases); nonemergency about 82% flat (30 cases); emergency 100% to 98% (2 cases); 88% of errors over-triage | d02, d03 | single-source (K17) |
| TacticAI retrieval and tactics | refinements favoured 45 of 50 (90%); receiver top-3 0.782; retrieval recall 0.63 vs 0.33 (feature baseline); real-vs-generated F1 0.60 | Wang 2024 (c12, d15) | single-source (K13) |
| Prompt structure moves game-agent results | GPT-3.5 LV4 win 12.5% vs 84%; LV5 0% vs 50% | Ma 2024 (c16) | single-source (K14) |
| LLM anchoring | low anchor mean 20.83, high 105.97 (humans 22.5 and 80.50) | Suri 2023 (c19) | single-source (K15) |

## 4. Mechanisms and models

The sport literature describes the mechanism in words. Below it is restated so that an engineer could build and log it. These are descriptions of human models, not validated agent designs.

**4.1 The RPD loop as a program.**
1. Read the situation. Pick out salient cues (in handball goalkeepers: cues 44%, expectancies 22%, actions 18% of coded units, a13).
2. Match the cue set to a stored case or prototype. Output: a typicality flag (typical or not), expectancies, a default action, and goals.
3. Branch:
   - Typical and clear: act on the default action (level 1).
   - Typical but unclear or cues missing: seek more cues, build a story or diagnosis, then act (level 2).
   - Action not obviously safe: run it forward mentally, check for a failure, modify or take the next option (level 3).
4. Act. No comparison across options in levels 1 and 2.

**4.2 The branch rule.** The sport data say time and role move the branch. Short time and high pressure: more level 1. Long time (defender far from the ball, a coach between plays): more level 2 and 3 (a03, d17). The goalkeeper's 34% simulation share (a13) shows that even under time pressure a role with predictable threats can simulate. Implementation: the branch should be set by a signal (unfamiliar cue set, failed check, high stakes), not by a timer or by a self-report. Self-reported intuition share is unreliable (K06).

**4.3 Take The First (option generation).** Options come from memory in order of validity. Rule: take the first option that passes a minimal check. Variants differ in what is checked. The empirical debate (K04, K20): option count affects best-of-set, mean-of-set and chosen-option quality differently. Any test must score those separately.

**4.4 Fast-and-frugal heuristics (Raab and Gigerenzer).** Recognition heuristic: if one option is recognised and the other is not, pick the recognised one. Works when recognition correlates with the criterion. In Wimbledon it beat ATP rankings and seedings in two studies on 127 matches (b14). Boundary: validity must be learned through feedback.

**4.5 Visual search as cue extraction.** Roca 2018 links creative decisions to faster threat detection with more, shorter fixations in full 11v11 scenes (a12). The 2026 meta-analysis says experts in individual sports use fewer, longer fixations (d16). Rule of thumb for an agent: the scan strategy depends on the task. In dense multi-threat scenes, scan wide; in compact tasks, go to the key item.

**4.6 Similar-case retrieval (TacticAI).** A graph network embeds corner-kick set-ups. Retrieval finds similar past set-ups. Raters judged retrieval and refinement favourable (c12, c13, d15). This is the closest machine analogue of RPD's match step. It was evaluated by five raters, not by match results.

**4.7 Video decision training.** Present the situation, ask the athlete to say what they see and what they would do, give feedback with questions. This is a case-library-with-outcomes idea, but evidence is tiny (b20, b22, b23).

## 5. What holds up

**Holds up (human).**
- A match-dominant mix is the commonly reported finding across sports and roles. The range 60-81% rests on one paywalled chapter (Macquet 2020), so it is established as a pattern, not as a precise number. Single studies fall inside or just below it (goalkeepers 46%).
- Time and role change the mix (qualitative support in Bossard, rugby N=16).
- Experts do deliberate sometimes. Simulation shares of 3-24% in the range and 34% for goalkeepers show it is a real path.
- People cannot report their mode reliably (rugby 5-40%, one coach 90%, N=18).

**Failures, weak spots and contradictions.**
- No sport study tests causally whether match-first beats analysis on performance (critique, weak spots). All the rates are descriptive.
- Nearly all RPD coding comes from retrospective interviews with soft coding of the level. Different coding schemes produce different shares.
- The Kermarrec and Bossard percentages sum to 99; Ashford 2021's own study counts disagree in places (41 vs 53 studies, 13 vs 7 added; critique).
- Le Menn found no significant difference in the process mix (p=.593), so the three-level split should not be over-interpreted.
- Roca d=5.36 comes from an extreme-group split; effect sizes there are inflated. Fixations: fewer in experts (2026 meta-analysis) vs more in full scenes (Roca). Resolved only as task dependence (K05).
- Option count: Klatt (more options help) vs Musculus N=169 and Raab and Laborde N=54 (less is more) vs Del Missier (fluency does not predict quality). Partly reconciled by what is scored (K20).
- Video decision training has only small positive studies; the youth review gives no pooled effect (K07). The baseball test-retest was not significant.
- The 80% first-option figure has no traceable source (K03).

**Interventions that worked (weakly).** Video feedback with questioning (N=11, p=.002); single-case quarterback video training. **Did not clearly work:** pitch-recognition test as a predictor (p=.052); youth reviews (no pooled effect).

**Moderators named in sources.** Time available, role (distance from the ball), expertise, sport, paradigm (information processing vs ecological dynamics vs NDM), whether coding uses retrospective speech.

## 6. Language models

**What exists.** No study tests RPD directly in an LLM on athletes' decisions (K12). Searches of Crossref, Europe PMC and arXiv returned 0 relevant hits (a25, c26, d19). The 2025 Ivanova et al. item is a book chapter on financial markets and was not opened (d12). A 2026 geopolitical simulation paper surfaced by the same search does not mention RPD (d18).

**RPD prompt in medicine (the one real test).** Kopka and Feufel 2026 (opened in full text): 10 ChatGPT-family models, 3 prompts, 45 vignettes, 10 repeats (b24, d01-d04).
- Overall accuracy: default 63.3% (CI 61.9-64.7), RPD 67.6% (66.3-69), data-frame 66.7% (65.3-68). Odds ratios vs default 2.26 and 2.05.
- Per model, default / RPD / data-frame: GPT-4o 65.3/70.7/66.2; GPT-4.1 64.4/72.7/72.4; GPT-4.1 mini 49.8/60.7/62.4; o3 70.7/75.1/76.2; o4 mini 69.3/70.7/72.9. 8 of 10 models gained; no gain for GPT-5.2.
- By urgency: self-care (13 cases) 13.4% to 29.8% (RPD) and 24.6% (data-frame); nonemergency (30 cases) 82.5 / 82.0 / 82.8%; emergency (2 cases) 100% to 98%.
- 88% of errors were over-triage. The authors say no safety conclusions follow.
- Read: the gain is a shift in threshold toward lower-urgency advice in cases where the default was too cautious, not better discrimination (K17). The data-frame prompt did as well, so the RPD content is not shown to matter (K18). No prompt token counts were reported. The authors suspect extra reasoning explains part.

**Sport knowledge benchmarks (text and video).**
- SportQA (70,592 items; 21,385 / 45,685 / 3,522 by level): GPT-4 5-shot CoT 85.63 / 78.82 / 73.58 / 64.08 / 34.40 / 23.01; humans 96.63 and 96.02 on L1 and L2 (c03). 82.5% of level-3 errors were inadequate multifaceted answer identification (c05).
- Sports Intelligence: hard multi-hop GPT-4 22.78-31.65 (c09).
- SPORTU: GPT-4o 71% best on text; Qwen2-VL-72B 70.94% on video overall and 44.12% on hard (c06).
- SportsMetrics: GPT-4 34.77-yard discrepancy in NFL passing yards in one setting; degradation on long games (c11).

**What changed results.**
- Few-shot and CoT: GPT-4 L1 0-shot CoT 80.60, 5-shot standard 80.24, 5-shot CoT 85.63 (c04). On hard multi-hop, no gain (22.59, 24.69, 23.01). PaLM2 hard single-hop fell from 49.80 to 38.37 with CoT.
- Sports Intelligence: GPT-4o L1 81.70 to 85.35 with CoT, Claude 3 Opus 66.67 to 58.73 (c10). Mixed sign.
- Order on hard video items (SPORTU): direct answer > answer then rationale > rationale first (c07). Claude-3.5-Sonnet 52.57 vs 39.32.
- Outside sport, Mind Your Step (Liu et al.): CoT drops on implicit tasks, GPT-4o 87.5 to 64.4 on statistical learning, 64.0 to 51.2 on face recognition, rounds-to-learn 2.9 to 12.5 on exceptions. Claude 3.5 Sonnet drops were smallest (97.8 vs 94.8 on faces; 65.9 vs 67.7) (c18, d13, d14).
- Game agent: TextStarCraft II GPT-3.5, Prompt 1 vs Prompt 2: LV3 25 vs 100%, LV4 12.5 vs 84%, LV5 0 vs 50%, LV6 0 vs 8.33% (c16). Against humans the LLM agent won 0 of 10 against pro and grandmaster, 5 of 10 middle, 10 of 10 gold (c17).
- Consistency: only 36.89-52.86% of questions correct at all camera angles, depending on model (c08).
- Biases: GPT-3.5 shows anchoring (c19) and exceeded humans on a conjunction error (18 vs 10 of 20). A recognition-first agent may inherit match errors.

**Retrieval-based tactical assistant.** TacticAI was favoured over existing tactics in 90% of 50 cases by five raters; retrieval recall 0.63 vs 0.33 for a feature-cosine baseline (not vs no retrieval) (d15).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested. No item below has been tested on our bench.

### Add now (established)

1. **Treat the fast path as the default and the slow path as triggered.** Part: S0 and G1/G11. [E] K01, K02 (a02, a13, a15). Sport adds a human prior, with the caveat that the range is quoted and soft. This agrees with what the schema already does; nothing new needs adding beyond keeping it. Do not copy the numbers as a prior.
2. **Do not use "80% first option" as a prior.** Part: S0. [E] K03 correction (d05). Measure our own first-option rate.
3. **Do not trust self-reported mode; log mode from the trace.** Part: G10 and run log (schema section 6). Support is one study but agrees with G10 (K06, a16). Implement as a log rule.
4. **Any NDM-style prompt must be compared with a length-matched neutral prompt.** Part: G7. [E] on the method; K10, K18. Reason: Kopka's data-frame prompt matched the RPD prompt.
5. **Report per-class accuracy and error direction when testing prompts.** Part: G7 and bench. [S] K17 (d02, d03), but cheap and safe, so adopt as a reporting rule.
6. **Reasoning-first on perception-like items is risky.** Part: S0 mode choice / O2. [E] K10 (c07, d13, d14). The schema already caps reasoning (G11); the sport data add a specific item class to watch.

### Test first

| Item | Part | Status | Evidence ids |
|---|---|---|---|
| Recognise-then-simulate frame (recall similar cases, then run action forward) vs neutral reasoning of equal length | S2/S3, O1/O3 | [S] | K08, K18; b24, d01, d04 |
| Direct answer first, then a check step, on perception-like items | S2/O2 | [S] | K19; c07, d13, d14 |
| Case retrieval (analogue of RPD match) vs none | memory | [S] | K13, K07; c12, d15, b23 |
| Number of options before choosing (1, 3, 5), scored three ways | S3/O4 | [C] | K04, K20; b06, b10, d07, d08 |
| Paraphrase disagreement as a trigger for diagnosis | S2/S6 | [S] | K11; c08 |
| Anchor check at the first-match step | O4/S1 | [S] | K15; c19 |
| Wide-scan-first vs go-to-obvious-item | S1 | [C] | K05; a12, d16 |
| Task-structure prompt ablation on a sequential game | G/S | [S] | K14; c16 |

## 8. Concrete tests on our bench

Rule for all: both arms at equal tokens (G7). Setup cost counted. Report per-item-class results and error direction.

1. **RPD content vs extra text (K18).** Items: 40 to 60 text vignettes with expert-coded actions, plus our existing bench classes with known answers. Four arms at the same token budget: neutral reasoning, recall-only, simulate-only, recall plus simulate. Metric: accuracy per class, error direction, tokens. Expected effect: Kopka's +4.3 points shrinks to the data-frame level (+3.4) or less; recall-plus-simulate does not beat neutral reasoning by more than 2 points.
2. **Direct then check vs reasoning first (K19).** Items: perception-like (grid or pattern recognition, ambiguous-image captions) and rule-like items, split. Arms: direct only, rationale first, direct then check, at equal tokens. Metric: accuracy and its sign by item type. Expected effect: rationale-first loses 5-15 points on perception-like items, direct-then-check recovers most of it; no sign flip on rule-like items.
3. **Option count (K04, K20).** Items: choice items with expert-scored option quality. Arms: 1, 3, 5 options, equal tokens. Metric: first-option, best-of-set and chosen-option quality, scored separately. Expected effect: best-of-set rises with count, set mean falls, chosen quality flat or slightly up.
4. **Case library with outcome notes vs none (K07, K13).** Items: repeated-class tasks where earlier solved cases exist. Arms: retrieve top-3 similar cases after the first attempt, vs none, equal tokens. Metric: pass rate on later instances of the class. Expected effect: gain only on classes with near matches; none on novel classes.
5. **Mode-coding agreement (K02).** Items: 100 agent traces. Two LLM judges code each into match / diagnose / simulate; report agreement (Cohen kappa). Expected: kappa under 0.6, which would confirm the soft-coding problem.
6. **Paraphrase consistency (K11).** Items: 50 items asked in two paraphrases. Metric: agreement rate; accuracy when agreeing vs disagreeing; arm with a diagnose step on disagreement vs without. Expected: disagreement flags a clearly lower-accuracy subset.
7. **Anchor check (K15).** Items: items with a planted number or guess in context. Arms: with and without an anchor check at first-match, equal tokens. Metric: shift of the answer toward the anchor. Expected: shift reduced by a third or more.
8. **Sequential game scaffold ablation (K14).** Items: a text game with a fixed budget. Arms: two prompt structures at equal tokens. Metric: win rate. Expected: swings of tens of points according to structure.

## 9. What does not transfer, and why

- **Usage rates.** They come from retrospective speech of athletes about plays lasting under a second. Our agent writes explicit traces and has no hidden fast path to measure. The rates are not priors for our task mix.
- **Perceptual expertise.** Anticipation, visual search and cue use are about eyes and bodies. A text agent has no such channel. The visual-search numbers (d=0.91 to 1.32, SMD -1.52) cannot be ported.
- **Time pressure as the driver.** In sport, time forces intuition. Our agent's constraint is a token budget, which is a different thing. G11 and G12 handle it.
- **Experience as the store of cases.** Human matches come from thousands of plays. An LLM's prior sits in weights, not in a case library; "recall similar cases" may retrieve invented cases, not real ones. Only an external library of real solved cases (memory) is comparable.
- **Self-report.** Athletes' and coaches' accounts of their mode are weak evidence; for the agent, reasoning text is not evidence at all (G10).
- **Option generation results.** They come from students and handball players on lab video, with option quality scored by experts. Our bench is scored by code, so the notion of option quality does not map one to one.
- **Medical triage gain.** It looks like a threshold shift (K17). It should not be read as RPD making the model reason better.
- **Benchmark QA vs decisions in play.** SportQA and SPORTU test knowledge and perception of sport, not decisions under pressure.
- **Safety claims.** Two emergency cases cannot support any.

## 10. Open questions

1. What is the primary source and sample of the 80% first-option figure (Johnson and Raab 2003)? Unopened (paywalled).
2. Which studies and Ns sit behind Macquet 2020's 60-81%? Only the chapter reference was recovered (CRC Press, doi 10.1201/9781351060073-12).
3. Does an RPD-structured prompt beat a length-matched neutral prompt, and which half (recall or simulate) does the work? No ablation and no replication exist.
4. Does option count help or hurt when experts score quality? Reconciled only by what is scored.
5. Does direct-then-check recover reasoning-first losses on perception-like tasks? Untested anywhere found.
6. Do similar-case retrieval systems beat no retrieval in a controlled outcome trial? TacticAI has expert opinion only.
7. Do LLMs show expert-novice differences (anticipation, cue use) on text descriptions of the same plays? Nothing found.
8. Is Ivanova et al. 2025 an RPD test of any kind? It is a finance chapter, unopened.
9. Does a match-first policy beat analysis on performance in sport? No causal sport study.
10. Does the 2026 triage gain hold for non-OpenAI models and for the safety-critical class? Only the ChatGPT family and 2 emergency cases.

## 11. Sources

[V] = opened and read (page, PDF text, or abstract page where noted in the evidence files); [M] = snippet or citation record only. Second-hand figures are marked in the text.

- [V] Bossard et al. (2022) Naturalistic decision-making in sport: advances in the RPD model (2022). https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.936140/full
- [V] Ashford, Abraham and Poolton (2021) Understanding a player's decision-making process in team sports: systematic review (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8156213/
- [V] Roca, Ford and Memmert (2018) Creative decision making and visual search behavior in skilled soccer players (2018). https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0199381
- [V] Le Menn, Bossard, Travassos, Duarte and Kermarrec (2019) Handball goalkeeper intuitive decision-making: a naturalistic case study (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6942481/
- [V] Collins, Collins and Carson (2016) If it feels right, do it: intuitive decision making in high-level sport coaches (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4830814/
- [V] Del Missier, Visentini and Mantyla (2015) Option generation in decision making: ideation beyond memory retrieval (cites Johnson and Raab 2003) (2015). https://pmc.ncbi.nlm.nih.gov/articles/PMC4302792/
- [V] Kalis, Kaiser and Mojzisch (2013) Why we should talk about option generation in decision-making research (2013). https://pmc.ncbi.nlm.nih.gov/articles/PMC3750205/
- [V] Editorial (2023) Naturalistic decision making (NDM): epistemic expertise in action, Frontiers Research Topic (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10667929/
- [M] Macquet (2009) Recognition within the decision-making process: a case study of expert volleyball players (2009). https://doi.org/10.1080/10413200802575759
- [M] Johnson and Raab (2003) Take The First: option-generation and resulting choices (2003). https://doi.org/10.1016/S0749-5978(03)00027-X
- [M] Kermarrec and Bossard (2014) Defensive soccer players decision making: a naturalistic study (2014). https://doi.org/10.1177/1555343414545019
- [M] Klatt and colleagues (2019) Creative and intuitive decision-making: Brazilian and German soccer coaches and players (2019). https://doi.org/10.1080/02701367.2019.1642994
- [M] Hepler and Feltz (2012) Take the first heuristic, self-efficacy, and decision-making in sport (J Exp Psychol Appl) (2012). https://doi.org/10.1037/a0026841
- [M] Raab and Laborde (2011) When to blink and when to think: preference for intuitive decisions (Res Q Exerc Sport) (2011). https://doi.org/10.1080/02701367.2011.10599744
- [M] Raab and Johnson (2007) Expertise-based differences in search and option-generation strategies (J Exp Psychol Appl) (2007). https://doi.org/10.1037/1076-898X.13.3.158
- [M] Musculus and colleagues (2019) A developmental perspective on option generation and selection (Developmental Psychology) (2019). https://doi.org/10.1037/dev0000738
- [M] Klatt and colleagues (2019) Creative and intuitive decision-making: Brazilian and German soccer coaches and players (2019). https://doi.org/10.1080/02701367.2019.1569116
- [V] Raab and Gigerenzer (2015) The power of simplicity: fast-and-frugal heuristics for performance science (Frontiers in Psychology) (2015). https://www.frontiersin.org/articles/10.3389/fpsyg.2015.01672/full
- [M] Secondary analysis of option generation task design and heuristics (2025) (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC13400725/
- [V] Hinz et al. (2022) Elite vs amateur handball decision making in a near-game test (Frontiers in Psychology) (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9038659/
- [V] Roca, Ford and Memmert (2018) Creative decision making and visual search in skilled soccer players (PLoS ONE) (2018). https://doi.org/10.1371/journal.pone.0199381
- [V] Powless et al. (2020) Video-based training to improve decision making in high school quarterbacks (Sports) (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7077253/
- [V] Decision-making in youth team-sports players: systematic review (2020) (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7312689/
- [V] Instructional design for accelerated macrocognitive expertise in the baseball workplace (Frontiers in Psychology 2016) (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4773639/
- [V] Effectiveness of a video-feedback and questioning programme to develop cognitive expertise in sport (PLoS ONE 2013) (2013). https://pmc.ncbi.nlm.nih.gov/articles/PMC3858278/
- [V] Kopka and Feufel (2026) Increasing LLM accuracy for care-seeking advice using prompts reflecting human reasoning strategies (JMIR Biomedical Engineering) (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13061108/
- [M] Scoping review of generative AI and LLMs in sports medicine (Frontiers in Public Health 2026) (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13461573/
- [M] NeuroPlayNet (2026) multimodal AI framework for basketball strategy (Scientific Reports) (2026). https://doi.org/10.1038/s41598-026-41140-y
- [V] Xia et al. (2024) SportQA: sports understanding benchmark for LLMs (2024). https://arxiv.org/abs/2402.15862
- [V] Xia et al. (2025) SPORTU: multimodal sports understanding benchmark (2025). https://arxiv.org/abs/2410.08474
- [V] Yang et al. (2024) Sports Intelligence: LLM and video-LM sports benchmark (2024). https://arxiv.org/abs/2406.14877
- [V] Hu et al. (2024) SportsMetrics: information fusion in LLMs (2024). https://arxiv.org/abs/2402.10979
- [V] Wang et al. (2024) TacticAI: an AI assistant for football tactics (DeepMind and Liverpool FC) (2024). https://arxiv.org/abs/2310.10553
- [V] Kurach et al. (2020) Google Research Football: an RL environment (2020). https://arxiv.org/abs/1907.11180
- [V] Ma et al. (2024) Large Language Models Play StarCraft II (TextStarCraft II, Chain of Summarization) (2024). https://arxiv.org/abs/2312.11865
- [V] Liu et al. (2025) Mind Your Step (by Step): CoT can reduce performance where thinking makes humans worse (ICML) (2025). https://arxiv.org/abs/2410.21333
- [V] Suri et al. (2023) Do LLMs show decision heuristics similar to humans? GPT-3.5 case study (2023). https://arxiv.org/abs/2305.04400
- [M] Fan, Sun, McNeese, Yen (2005) Extending the recognition-primed decision model to support human-agent collaboration (2005). https://doi.org/10.1145/1082473.1082616
- [M] Fan and Yen (2008) Team-RPD: a collaborative model of the recognition-primed decision process (2008). https://doi.org/10.1109/WIIAT.2008.44
- [M] Nowroozi, Shiri, Aslanian, Lucas (2012) A general computational recognition primed decision model with multi-agent rescue simulation benchmark (2012). https://doi.org/10.1016/j.ins.2011.09.039
- [M] Hu, Li, Zhang (2018) Predicting pilot behavior during midair encounters using recognition primed decision model (2018). https://doi.org/10.1016/j.ins.2017.09.035
- [M] Ivanova, Didenko, Grigoryan, Kraevskiy (2025) Simulating dynamics of the recognition-primed decision model on financial markets using LLM (2025). https://doi.org/10.4324/9781003606956-6
- [M] Susceptibility to misinformation: persuasion and prior orientation in recognition-primed decision pathways (J. Cognitive Engineering and Decision Making, 2026) (2026). https://doi.org/10.1177/15553434261472960
- [V] Del Missier et al. (2014) Option generation in decision making: ideation beyond memory retrieval (abstract via Europe PMC) (2014). https://europepmc.org/article/MED/25657628
- [V] Klatt et al. (2019) Creative and intuitive decision-making, Brazilian and German coaches and players (abstract via Europe PMC) (2019). https://europepmc.org/article/MED/31478798
- [V] Raab and Laborde (2011) When to blink and when to think (abstract via Europe PMC) (2011). https://europepmc.org/article/MED/21462689
- [V] Raab and Johnson (2007) Expertise-based differences in search and option-generation strategies (abstract via Europe PMC) (2007). https://europepmc.org/article/MED/17924801
- [V] Individual-sports visual-search meta-analysis (2026, abstract via Europe PMC) (2026). https://europepmc.org/article/MED/42222294
- [V] Rugby union decision mechanisms by time available (2021, abstract via Europe PMC) (2021). https://europepmc.org/article/MED/34054638
- [V] Solopova et al. (2026) LLMs as strategic actors in geopolitical simulations (arXiv 2603.02128) (2026). https://arxiv.org/html/2603.02128v1

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 5 established claims: 2 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E04.08-K01** (now single-source: the sources are not independent). All numbers confirmed (Bossard 2022 quoting Macquet 2020: 60-81/13-28/3-24; handball 46/20/34; soccer 60/16/23; rugby N=16 time effect from independent Ashford 2021), but the 60-81% range, the handball and the soccer figures all come from the Bossard/Kermarrec group (Bossard 2022, Le Menn 2019, Kermarrec and Bossard 2014), so the range has one real source.
- **E04.08-K02** (now single-source: the sources are not independent). Numbers are right (goalkeeper 46% below the 60% floor; wide ranges; retrospective speech), but both sources are from the same Bossard/Kermarrec group and neither says coding schemes, roles and sports are the cause of the spread; that explanation is the researcher's inference.
- **E04.08-K09** (number corrected). In SportQA Table 2 the human row (96.63/96.02/94.90/91.84) lines up under the four Level-3 columns (easy/hard single-hop, easy/hard multi-hop), not Levels 1-2; no human score is given for Levels 1-2, and human hard multi-hop is 91.84, not a single-hop figure. Only SportQA was read; the Sports Intelligence abstract was not opened. Corrected claim: On SportQA, GPT-4 (5-shot CoT) scores 85.63 on Level-1 and 78.82 on Level-2 (no human score reported for those levels); on Level-3 humans score 96.63 (easy single-hop), 96.02 (hard single-hop), 94.90 (easy multi-hop) and 91.84 (hard multi-hop) against GPT-4's 73.58, 64.08, 34.40 and 23.01.
