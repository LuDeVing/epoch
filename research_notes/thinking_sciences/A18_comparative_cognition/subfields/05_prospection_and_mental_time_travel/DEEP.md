# Prospection and mental time travel: deep document

*Subfield A18.05 of comparative cognition. Written 2026-11-20 from evidence_a-d.jsonl (a01-a25, b01-b29, c01-c25, d01-d21), claims.jsonl (K01-K32) and critique.md. Background subfield: the animal work cannot be run on our agent. The value is (a) a clean test design for "does it plan for a need it does not have now", (b) the human and LLM prospective-memory literature, which does carry over.*

## 1. What it is

**Prospection** is thinking about the future. **Mental time travel (MTT)** is the flexible version: building a specific imagined future (or past) scene, decoupled from what you sense now, and acting on it. Suddendorf and Corballis (2007, BBS, a01) set a ladder of how memory can serve the future:

1. Procedural prospection. Non-declarative systems. Stimulus-bound.
2. Semantic prospection. General knowledge of what usually happens next.
3. Episodic prospection (MTT). Flexible scene construction. Newest and most flexible system.

The central animal question: do any animals act now for a future need that differs from their present state? The test is the **Bischof-Kohler hypothesis (BKH)**: animals cannot act for a future need state that differs from the current drive (a02). Suddendorf and Busby proposed the nonverbal test. Control the current need (for example the animal is not thirsty), then offer a chance to secure a future need. The BKH is falsified only if one animal passes variants across several needs and contexts, and with non-species-typical behaviour (not caching, which may be innate).

Three families of tasks matter:

- **Caching for future need.** Scrub-jays (Raby 2007, Correia 2007), Eurasian jays (Cheke and Clayton 2012, Amodio 2021), Canada jays (Martin 2021).
- **Tool or item choice for a later problem ("spoon tests").** Apes (Mulcahy and Call 2006), ravens (Kabadayi and Osvath 2017), crows (Boeckle 2020), children (Redshaw and Suddendorf 2013).
- **Episodic-like memory (what-where-when).** Clayton and Dickinson 1998 and the 2025 revisit. This is the past-facing half of MTT.

For an LLM agent three different things are called "prospection" in the 2026 papers, and they must not be mixed:

1. **Prospective memory (PM).** Remembering to act on a stored intention when its trigger appears. Human PM work is Einstein and McDaniel. LLM benchmarks: TriggerBench, PM-Bench, Mittal 2026.
2. **Prospection-guided retrieval.** Imagine next steps and use them as probes (Chopra 2026).
3. **Episodic future thinking (EFT) cues.** A vivid imagined future outcome that changes a present choice. Human meta-analyses g = 0.44 and 0.52. LLM use is only as a generator of cues for humans.

Source note: no study tests an LLM on caching, future-need choice or a Bischof-Kohler design (K22, a23, c24, d19; about 22 searches, absence not proven). The agent link is analogical.

## 2. History and theories in depth

**1998. Clayton and Dickinson (a17).** Western scrub-jays cached perishable wax worms and non-perishable peanuts, then recovered after a short (4 h) or long (124 h) delay. After the short delay they searched for worms. After the long delay they searched for peanuts. Only birds that had experienced decayed worms showed the pattern. This was read as "episodic-like" memory: what, where, when. Critics: association or familiarity could explain it.

**2006. Mulcahy and Call (a12).** Bonobos and orangutans picked, carried and saved suitable tools for use 1 h later, 14 h later, and with the apparatus out of sight. Suddendorf and Corballis (a03) replied: average 7 of 16 trials correct, best orangutan 15/16, and the same tools were right on every trial, so a learned rule fits. Osvath and Osvath 2008 (a14) and the 2009 reply (a25, unopened) continued the dispute.

**2007. The founding review (a01, a02, a24).** Suddendorf and Corballis argue there is no convincing evidence of MTT in animals. They offer the BKH as the tractable falsifier. Raby, Alexis, Dickinson and Clayton answer in the same commentary round: MTT cannot be split cleanly into episodic versus semantic, since the difference may just be the feeling of pre-experiencing, so the BKH is the usable criterion. Schacter and Addis add the constructive episodic simulation view: the same constructive system builds past and future scenes (Addis 2007, Hassabis 2007, Szpunar 2007).

**2007. Raby et al. "Planning for the future by western scrub-jays" (a04, d01).** The headline result. Jays learned that in one compartment they would be hungry next morning and in another they would be fed. In the test evening they cached more food where they would be hungry (Exp 1). In Exp 2 they cached each of two foods where it would be missing next day. Second-hand: N = 8, six training mornings, one test evening (a03, a08). The primary counts were never read (paywalled; K05).

**2007. Correia et al. (a05, d02).** Specific satiety separates current from future desire. Jays fed one food cached the other, then were fed so that at recovery they would want a different food. After a few trials they cached what they would want at recovery. Second-hand: 3 h delay (Paxton and Hampton 2009). Criticism: the satiety difference may let association work (S&C 2008).

**2009. Paxton and Hampton (a10).** Rhesus monkeys (N = 6) did not give up a large food amount to avoid later thirst. Water drunk after a 120 min delay 51.17 mL vs 40.83 mL after 15 min, t(5) = -4.04, p = 0.01. The large amount was still chosen. Squirrel monkeys (Naqshbandi and Roberts 2006, a11) did reverse their preference. Rats appear to fail (b16).

**2012. Cheke and Clayton (a06).** Eurasian jays (N = 4) cached in two trays, each to be opened after a different pre-feeding. They came to cache in each tray what they would want there. Satiety check F(1,3) = 12.4, p = 0.039. Planning interaction F(2,2) = 24.95, p = 0.039. Effect gone in trial 3 (p = 0.23).

**2014. Thom and Clayton (b05, b06).** No preference to cache where recovery would come sooner (delays from 7 min to 49 h). Exp 2 means: 5.24 (7 min), 4.97 (26 h), 5.45 (7-SR) of 20 worms; F(1.37, 15.07) = 0.123, p = .808. Authors lean to: birds tell present from future, not how far.

**2013. Redshaw and Suddendorf (b11).** Four-year-olds, instant condition 91.7% correct, delayed 50%, chance 16.7%. F(1,22) = 12.79, p = 0.002.

**2017. Kabadayi and Osvath (a13).** Ravens planned for tool use and bartering with delays up to 17 h. Redshaw, Taylor and Suddendorf (2017, b13) questioned leaner explanations.

**2020. Boeckle et al. spoon test (a15, b09, b10).** Built jointly by people on both sides. Pre-registered. New Caledonian crows saw a baited apparatus, 5 min later chose among 5 objects, 10 min later got the apparatus. 9 crows entered, 6 reached training, 4 reached criterion in 20-25 trials. Critical test: 9/10, 7/10, 7/10 correct (chance 20%, p < 0.001); one crow 3/10 (p = 0.429). All successful birds were female.

**2021. Esteve and Santariello (a16); Boeckle reply (d06).** The critique: first-order (associative) and higher-order (representation) explanations are not truly alternatives, and training could explain results. The reply argues past reward cannot explain it but gives no new data.

**2021. The null or reversed jay replications (a07, a09).** Amodio et al. in Eurasian jays and Martin et al. in Canada jays (section 5).

**2020. Farrar, Boeckle, Clayton (d05).** The original lab says direct replication is often impossible: it no longer houses California scrub-jays, and only one other lab publishes on their caching. Tiny N makes an original and a replication hard to tell apart.

**2024-2025. Episodic-like memory re-examined (a18, a19, b15, b16).** Davies and Clayton 2024 review: evidence mixed; recommend several paradigms. Davies et al. 2025 re-ran Clayton and Dickinson with finer measures (section 5). Eurasian jays show episodic-like memory in an incidental-encoding design (b15).

**Three competing accounts of the jay caching results (a08, b01).**

- *Future Planning (FPH).* Recall what-where-when of past events and predict future availability.
- *Mnemonic Association.* Long-delay learning at cache recovery strengthens the rewarded cache site.
- *Compensatory Caching (CCH).* Cache more where food has been scarce, a personal-history rule.

Each explains only some studies. Together the authors say they explain all published results.

**Human work (b19, b20, d16, d17).** Episodic future thinking lowers delay discounting. See section 3.

## 3. Core findings with exact numbers

Status key: **established** (two or more independent sources), **single-source**, **contested**, **replicated-preprint** (several preprints, authors' own methods).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Scrub-jays cache where they will be hungry (Raby) | N = 8, 6 training mornings, 1 test evening (second-hand; counts unread) | Raby 2007 (a04, d01) | contested |
| Scrub-jays cache the food they will want at recovery (specific satiety) | 3 h delay; by trial 3 "different" group shifted (second-hand) | Correia 2007 (a05) | single-source |
| Eurasian jays: caching independent of compartment | Exp 1: 6 tested of 9 started; posterior 0.997 compartment-independent, FPH 0.0014, CCH 0.00001. Exp 2 (pre-registered): 7 entered, 6 received the test trial; 0.72, CCH 0.16, FPH 0.002 | Amodio 2021 (a07, b02, b03) | single-source (pre-registered) |
| Same, without bird Lisbon in Exp 1 | FPH 0.00008, CCH 0.0002 | Amodio 2021 | single-source |
| Canada jays cache the opposite way | N = 6; F(1,15) = 12.18, p < 0.001; interaction F(1,15) = 3.23, p = 0.09; 3 of 6 did not cache in the breakfast choice | Martin 2021 (a09, d04) | single-source |
| Eurasian jays, two future desires | N = 4; satiety F(1,3) = 12.4 p = 0.039; planning F(2,2) = 24.95 p = 0.039; lost by trial 3 (p = 0.23) | Cheke and Clayton 2012 (a06) | contested |
| No temporal preference in caching | 5.24 / 4.97 / 5.45 of 20; F(1.37,15.07) = 0.123, p = .808 | Thom and Clayton 2014 (b05) | single-source |
| Apes save tools | average 7/16, best orangutan 15/16 (second-hand) | Mulcahy and Call 2006 (a12, a03) | single-source (disputed) |
| Ravens plan with delays up to 17 h | N not read | Kabadayi and Osvath 2017 (a13) | single-source |
| Rhesus do not give up food to avoid later thirst | N = 6; 51.17 vs 40.83 mL; t(5) = -4.04, p = 0.01 | Paxton and Hampton 2009 (a10) | single-source |
| Crow spoon test | 4 of 6 trained crows passed; 9/10, 7/10, 7/10; one 3/10 (p = 0.429); chance 20% | Boeckle 2020 (a15, b09) | contested |
| Four-year-olds fail the delayed version | instant 91.7%, delayed 50%, chance 16.7%; F(1,22) = 12.79, p = 0.002; 25% mentioned future use and all were correct | Redshaw and Suddendorf 2013 (b11) | single-source |
| Episodic-like memory replication is weak | 4 birds both delays; short delay all 4 to worms (p < 0.001); long delay 1/4 to pine nuts; cached-vs-control W = 4, p = 0.068 (lowest possible p with that N) | Davies 2025 (a18) | contested |
| Eurasian jays: incidental encoding | N = 7; main test p < 0.001; spatial p < 0.001, visual p = 0.151 | b15 | single-source |
| Delayed gratification depends on social context | 6 crows chose delayed in all 3 conditions; no jay (N = 5) did with anyone present; chi2(2) = 60.36 | b17 | single-source |
| Flying squirrels follow past food, not future | 733 litters; past alder 1.5 (CI 1.1-2.1); future -0.30; delta AIC 26 and 29 | b18 | single-source |
| EFT lowers delay discounting (human) | g = 0.44 [0.33, 0.55], 174 effects, 48 articles; g = 0.52, 47 studies, 63 contrasts; positive 0.64, valence unstated 0.28, neutral or negative -0.03 | b19, b20, d16, d17 | established (abstract level) |
| AI future-self avatars (human) | N = 192; switch rate 34.2% vs 10.8% (p = 0.015); novel option 20.0% vs 2.7% (p = 0.019) | Poonsiriwong 2025 (b21) | single-source |
| Future You chat (human) | N = 344; anxiety -0.68 vs +0.21 (p = 0.002); self-continuity +0.42 vs 0.00; 2025 follow-up N = 92, no format differences | c19, c20 | single-source |
| LLM formatting-constraint compliance falls under task load | drops 2-21%; mean drop o4-mini 8.9, DeepSeek-V3.1 10.2, Llama-3.3-70B 6.0; terminal constraints up to 50% | Mittal 2026 (c04, c05) | single-source |
| Salience prompt restores compliance | 5xGSM8K DeepSeek 72.2 to 100, Llama 70.4 to 98.1; mean gains 17.7, 16.9, 12.7 | Mittal 2026 (c06) | single-source |
| The reminder costs task accuracy | o4-mini GSM8K x3 93.3 to 26.7; DeepSeek 76.7; Llama 64.4; x5 o4-mini 53.7; MMLU 82.2 to 76.5 (2048 max tokens) | Mittal (d14) | single-source |
| LLM PM collapses with context while retrospective memory holds | GPT-4o retrospective about 98% to 100K; PM from over 90% to under 40%; Qwen3-235B-Think about 90% | TriggerBench (b23, c09) | established |
| Dual-task interference | drops up to 73 points (GPT-4o), 71 (Qwen3-32B) | TriggerBench (b24) | single-source |
| PM tracks spare reasoning capacity | 30-50K tokens: AIME correct (n = 272) 47.1% vs wrong (n = 143) 37.8% | TriggerBench (c10) | single-source |
| Reasoning raises recall but also false alarms | Qwen3-235B-Think 74.86% (92.83% Pos-Clean); GPT-5.2 +13.91 points none to high; GPT-5.2 high 43.94% on negatives; at 40K, GPT-5.2 high 75.02 and negative-clean 39.80 | TriggerBench (c08, d15) | single-source |
| LLM agents on PM-Bench | best GPT-5.4 + heartbeat 65.1% macro Set-F1; todo ledger 62.8%; cross-day hit 50.0%; update 44.4%; hidden-channel monitoring 15.8% | Liu and Gabriel 2026 (b26) | single-source |
| Typed intention stores | DeepSeek-Chat 82.9%; Gemma-E2B 4.2 to 66.2; naive RAG 46.5, Mem0 48.7, A-Mem 54.1 | Zhao and Wu 2026 (b27, c13) | replicated-preprint |
| Pro-Memory (independent group) | PM-Bench Set-F1 Sonnet 4.5 0.5224 to 0.7600, Haiku 4.5 0.4561 to 0.7324; GLM-4.7 baseline RWM 0.7218 beat Pro-Memory 0.7068 | Bei 2026 (d09) | replicated-preprint |
| Retrospective memory can hurt proactive behaviour | Haiku 4.5 ProactiveBench F1: none 0.5103, RAG 0.3636, A-Mem 0.3276, T-Mem 0.3248, Pro-Memory 0.6634; removing evidence links -8.45 Set-F1 and over 2x false alarms | Bei 2026 (d10) | single-source |
| Ledger on synthetic set | hard stratum recall@5 0.000 to 0.955; zero false boosts over 53 tasks; only 17-29% of phrased pairs defeat embedding similarity | Groff 2026 (d13) | single-source |
| Prospection-guided retrieval | MemoryQuest recall 0.723 vs Mem0 0.256, GraphRAG 0.160, query-only 0.58; TOT 0.723 vs COT 0.718; second generator 0.748 | Chopra 2026 (c01-c03) | single-source |
| Proactive agents fail at root cause | best end-to-end 40% (GPT-5, Claude Opus 4.1); wrong root cause 73.8% of identification failures | Pasternak 2025 (b28) | single-source |
| CheeseBench: frontier LLMs vs rodents | rodent 78.9%; v2 best open-weight 68.0% vs random 38.0%; Opus 4.7 86.7%; radial-arm maze Opus 4.7 100%, Opus 4.6 90%, GPT-4.1 0% | Bugaud 2026 (c14, c15, d08) | single-source |
| Episodic benchmark for LLMs | single-match F1 gpt-4o 0.81, claude-3.5-sonnet 0.35, o1-mini 0.05; 6+ matches gpt-4o 0.53 | Huet 2025 (a20) | single-source |

## 4. Mechanisms and models

The jay literature gives three mechanism models that predict different caching patterns. An engineer can implement them as three small policies and fit them to any agent's choices. Amodio 2021 did exactly this with Bayesian model comparison.

**4.1 Three caching policies (a07, a08).**

State: C compartments (or locations), F foods, a history of days. Each day each compartment has a condition (food available early, or not; or a food type).

- *Future Planning (FPH).* Keep a table of what-where-when. Predict, for tomorrow, which compartment will lack food. Allocate caches to the compartments predicted to lack food, per food type. Output: cache share by compartment is a function of predicted scarcity tomorrow.
- *Mnemonic Association.* Keep a value per (compartment, food) that rises when a cache there was later recovered and rewarded after a long delay. Allocate by value. No explicit prediction.
- *Compensatory Caching (CCH).* Keep a count of recent scarcity per compartment (past, not future). Allocate more to compartments recently lacking food. In Amodio the CCH and FPH predict opposite patterns when the compartment cycle runs on 3 days against a 2-day food cycle.
- *Null (uniform).* Cache equally, with bird and food-type baselines.

Comparison method: fit all four to per-bird caching counts and compare posterior model probabilities. In Amodio Exp 1 the null (bird and food type, no compartment) won with 0.997. This is the model set to apply to an agent's choices (K02 test). The exact model parametrisation is in the paper and should be copied from it, not from this summary.

**4.2 The BKH test as an agent protocol (a02).**

1. Put the agent in state A (for example "no resource needed now").
2. Tell it, or let it learn by experience, that state B comes later with a distinct need.
3. Offer an action now that only pays off in state B, with a cost now.
4. Vary need and context so a single learned rule cannot pass. Score choice against chance (5 options, chance 20%, as in the spoon test).
5. Add decoy options that were right in a previous condition (the spoon test uses tools that were right for another apparatus). That separates "plans for this future" from "likes this option".

**4.3 Spoon-test logic (a15, d06).** Three phases: see problem, delay without the problem in view, choose among options, then problem returns. Pass means choosing the one object that solves the problem that was seen, against both high-value objects and objects tied to past reward. For an LLM the "delay without sight" is trivially met (it lacks the apparatus). What a test must control is whether the right choice can be made from a fixed rule learned in the prompt or few-shot examples.

**4.4 Prospective memory pipeline (PM-Bench, Pro-Memory, PIS; b26, b27, d09, d12).** The working design is a typed store of pending intentions with a lifecycle run in code:

1. *Form.* On each input, detect a deferred intention (what to do, activation condition, deadline or trigger). Write it as a typed record.
2. *Revise.* On updates ("actually, cancel that"), edit the record.
3. *Filter.* At each step, code selects the records whose trigger could match the current input.
4. *Decide.* A scoped model call decides whether the trigger really fires, given the record and the evidence link.

Key part: the evidence link between intention and the observation that supports it. Removing it on Haiku 4.5 cost 8.45 Set-F1 points and more than doubled false alarms (d10). The lifecycle is in code, not in the model (PIS: Gemma-E2B 4.2 to 66.2).

A simpler variant, the commitment ledger (Groff 2026, d13), boosts the retrieval of items linked to a dated or trigger-conditioned commitment. Zero inference at lookup. It matters because only 17-29% of naturally phrased commitment-trigger pairs defeat embedding similarity.

**4.5 Prospection-guided retrieval (Chopra 2026, c01, c02).** Three steps: Simulate (write plausible next steps), Retrieve (use each imagined step as a query), Refine (second round grounded by retrieved facts). Iterating helps (TOT 0.677 to 0.723, COT 0.645 to 0.718). The linear chain gets nearly all the gain (0.718 vs 0.723), so branching is not needed.

**4.6 Salience reminder (Mittal 2026, c06).** A trailing, explicit restatement of the constraint, placed where the action happens (at the end). Human PM account: delayed intentions need a cue at the right time. Terminal constraints fail most; avoidance constraints are nearly immune (c05).

**4.7 EFT cue (human meta-analyses, b19, b20).** Components that moderate the effect: positive valence, vividness, concreteness, link to the delayed choice. A neutral or negative future gives g = -0.03. For an LLM, the nearest implementable form is a short, concrete, positive description of the delayed outcome placed before the choice. No test exists (K32).

**4.8 Reasoning budget and PM (c08, c10).** More thinking helps recall but pushes to an always-remind rule. Treat the trigger decision as a detector with a false-alarm rate, not as a recall number.

## 5. What holds up

**Animal planning: contested, not refuted.**

- The only direct re-runs of Raby 2007 went the other way or did not fit. Martin 2021 (Canada jays, N = 6) found more caching in the feeding compartment (F(1,15) = 12.18). Amodio 2021 (Eurasian jays, pre-registered) found no compartment effect (0.997). Neither used the original species, so neither is a clean failed replication (K01, K27). Nobody has re-run it in western scrub-jays: the original lab no longer houses them (d05).
- Design differences that could explain the split (d03, b04): housing (pairs in 2 x 1 x 1 m cages vs a group in a 20 x 10 x 3 m aviary), trial length (2 h vs 15 min), a fixed vs a rotating compartment-condition link, 6 vs 9 experience days. Neither paper can show which matters. The "load" excuse is not testable as framed, since neither hypothesis states a load limit.
- Martin: prior caching experience of wild-caught birds in captivity 8-18 months, 1 h light-time shift, 3 of 6 did not cache in the breakfast choice.
- Primary counts for Raby and Correia are unread; all jay effect sizes are second-hand (K05).
- Tiny N throughout (4 to 8 birds). Farrar 2020 argues tiny N makes an original and a replication hard to tell apart.

**Spoon test: contested.** Passed by 3 of 4 trained crows, but only 4 of 9 reached criterion and all were female. Training may explain it (Esteve and Santariello 2021). No second lab, no new birds (d06, K07).

**Episodic-like memory: weak replication.** Davies 2025: W = 4, p = 0.068, the lowest p reachable with N = 4. Only birds that had experienced decay show the pattern. The lab's account of "replicates" is generous (a18).

**Apes and monkeys.** Rhesus fail the choose-for-future-thirst design (a10). Squirrel monkeys pass an analogous task (a11, abstract only). S&C argue apes could have learned a fixed rule (a03).

**Field.** Flying squirrels do not anticipate future abundance (b18). Observational, reproduction not cognition.

**Children.** Under-fives are at chance in a two-option version of a similar task (b10). Foresight beyond the very next event gives 50% delayed vs 91.7% instant (b11).

**Humans: EFT works, with moderators.** Two meta-analyses at abstract level (g = 0.44, 0.52). Not independent confirmations (different samples, d17). Valence and vividness matter. Outcomes are mostly self-reported or discounting choices, not planning quality. The full texts were not read.

**LLM prospective memory.**

- Held across studies: PM fails while retrospective memory holds (TriggerBench: 98% vs under 40% for GPT-4o at 100K; b23, c09). Terminal constraints fail most (Mittal). Two papers on different tasks agree on the direction.
- Reminders restore compliance (Mittal) but cost main-task accuracy (d14). Never read as a free gain.
- Reasoning helps (+13.91 points GPT-5.2) and also raises false alarms (negatives 43.94%).
- Typed intention stores beat retrospective memory systems across four preprints (K18). Boundaries: all are preprints with the authors' own methods; GLM-4.7's baseline RWM beat Pro-Memory on PM-Bench (0.7218 vs 0.7068); the ProMemAgent reasoner was a fine-tuned Qwen3-8B; the ledger test was on an author-built synthetic set.
- Retrospective RAG-style memory can hurt: Haiku 4.5 ProactiveBench F1 dropped from 0.5103 to 0.3636 (RAG).

**Interventions that worked:** salience reminder (compliance), typed intention store, evidence links, prospection-guided probes (recall).
**Did not work or no evidence:** tree vs chain branching (0.723 vs 0.718, no real gain), format differences in AI future selves (N = 92), chain-of-thought on CheeseBench Qwen2.5-VL-7B (46.7 to 31.9), retrospective memory tools for PM (RAG, A-Mem, Mem0, Letta all below no memory in several cells).

**Corrections kept from the critique:** CheeseBench v1 (12 Apr 2026) 52.6% vs 32.1% random; v2 (15 May 2026) 68.0% vs 38.0%; the arXiv abstract page labelled v2 still shows v1 numbers. Amodio Exp 2: 7 entered the test phase, 6 received the test trial (one stopped on welfare grounds). The Raby birds are western (California) scrub-jays.

## 6. Language models

No LLM study runs a caching, future-need or Bischof-Kohler test (K22). What exists:

**6.1 Prospective memory (the best-measured area).**

| Study | Setup | Result |
|---|---|---|
| Mittal 2026 (c04-c06, d14, c25) | 3 models (o4-mini, DeepSeek-V3.1, Llama-3.3-70B), over 8,000 prompts, formatting constraint + concurrent task; 3 runs, greedy, 2048 max tokens | compliance drops 2-21%; terminal constraints up to 50%; salience prompt restores to 90-100% in many cells; reminder costs main task: o4-mini GSM8K x3 93.3 to 26.7 |
| TriggerBench (b23-b25, c07-c11, d15) | latent constraints without prompt; Qwen3, Gemma3, GPT-4o, GPT-4.1, GPT-5.2; RAG, A-MEM, Mem0, Letta-sim; LLM judge | PM over 90 to under 40 (GPT-4o, 100K); Qwen3-235B-Think 74.86; GPT-5.2 +13.91 with thinking; negatives 43.94 or 39.80 |
| PM-Bench (b26) | simulated week | best 65.1% Set-F1; ledger 62.8% |
| PIS (b27, c13) | typed store | DeepSeek-Chat 82.9; Gemma-E2B 4.2 to 66.2; retrospective methods at most 54.4 |
| Pro-Memory (d09, d10) | Claude Sonnet 4.5 and Haiku 4.5, Kimi-K2.5, GLM-4.7 | Sonnet 0.5224 to 0.7600; Haiku 0.4561 to 0.7324; RAG hurt on ProactiveBench |
| ProMemAgent (d11) | CPMBench 1,000 instances | Set-F1 75.2; without cross-event linking 65.9; fine-tuned Qwen3-8B reasoner |
| Groff (d13) | commitment ledger | recall@5 0.000 to 0.955 |
| ProactiveBench (Pasternak, b28) | long-horizon proactive | best 40% (GPT-5, Claude Opus 4.1); 73.8% of identification failures are wrong root cause |

What changed performance: context length (large drop), a competing request (up to 73 points), spare reasoning budget (47.1 vs 37.8), a trailing reminder (+12.7 to +17.7 points), a typed store (up to +62 points for a 2B model), reasoning effort (+13.91). What did not: generic retrospective memory (often lower), tree over chain.

**6.2 Prospection as a retrieval probe.** Chopra 2026: recall 0.723 vs 0.58 query-only vs 0.256 Mem0. Caveat: the benchmark was built with a low query-reference similarity filter (cosine <= 0.3), which favours the method; generator GPT-4o, second generator DeepSeek-V3.2 0.748; pairwise LLM-judge win rates 89-98%, humans 60-95% on held-out subsets.

**6.3 Animal-paradigm benchmarks.** CheeseBench (c14-c16, d07, d08): nine rodent paradigms as ASCII gridworlds, 13 LLMs, zero-shot. Frontier models reach or pass the rodent reference (Opus 4.7 86.7 vs 78.9). Working memory across choices (radial arm maze) is solved by Opus 4.7 (100%) and Opus 4.6 (90%), not by GPT-4.1 (0%, action bias). Only 10 trials per cell for frontier models; best of three view modes; one author; no caching or future-planning paradigm. Scaffold effect on one 7B model: default 46.7, CoT 31.9, minimal 35.6, few-shot 29.6.

**6.4 Episodic memory and delay.** Huet 2025 (a20): cue overload hurts (F1 drops when a cue matches 2 or more events); confabulation when no event matches. In-context single-match F1: gpt-4o 0.81, claude-3.5-sonnet 0.35 (affected by a verbosity bug), o1-mini 0.05. Position papers (Pink 2025, TiCS 2025; a21, a22, b29, c17): episodic memory is missing from LLM agents; no experiments.

**6.5 Delay of gratification.** Manakina 2026 (c22, d18): 19,200 trajectories, 75.9% persist; removing hedonic drive and persona age pushes completion toward 1.0. Persona prompts supply the drive, so it is role play, not a state the agent has.

**6.6 Planning scaffolds.** Generative Agents (c18): observation, planning and reflection each contribute (abstract only). Self-regulated simulative planning (c23): RL raises average planning horizon 22.8%, frequency only 2.0%; 25.8-95.3% fewer reasoning tokens (RL-trained model; not a prompt-only effect). Situation-conditioned thinking policies (d21): synthetic, easy (perfect scores).

**6.7 Human-facing LLM use.** AI-generated future selves (b21, b22, c19, c20, c21, d20). Not about the agent's own prospection.

## 7. What our agent should take

Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Almost nothing here is established for an agent. The animal work is background (the brief says so). The transferable part is prospective memory.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Never trust recall-only metrics for triggers. Report hit rate and false-alarm rate together in every bench that adds reminders or ledgers. | G7 (test hygiene) | [E] for the trade-off; two benchmarks | K17, K30, c08, d15 |
| Do not rely on a constraint stated early in a long context. Critical constraints and pending actions get restated near where the action happens (end of the prompt, before the final answer). A placement rule only, not a new state. | G, S8 (verify uses the original task text) | [E] for the failure (PM collapses with context, retrospective memory intact); the remedy [S] | K16, b23, c09, K14 |
| Do not add a generic retrospective memory (RAG, A-Mem, Mem0) as a fix for deferred intentions. It did not help and sometimes lowered scores. Record as a "do not add" note. | memory | [S], consistent in 3 papers | K18, K28, b27, d10 |
| Keep the human EFT finding out of the schema as a rule: it is a human finding with no LLM test. Record it as a candidate only. | none | [E] human only | K11, K32 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Typed intention ledger (form, revise, filter, decide in code; each record carries its evidence link). SCHEMA section 5 (memory) has no store for deferred actions. | memory | [S] (replicated-preprint) | K18, K28, b26, b27, d09, d10, d13 |
| Final constraint check at S8/S9: re-read the original constraints and compare, with the check done by code where possible. Measure main-task accuracy and compliance together. | G, S8, S9 | [S] | K15, K29, c06, d14 |
| Prospection-guided probes at retrieval: write 3 imagined next steps, use each as a query. | S2/S3 retrieval, memory | [S] | K19, c01, c02 |
| Prospective check at S1: list what later steps will need from the task (hidden constraints, later-stage requirements) and record them as pending intentions. | S1, S2 | [S] analogy only | K20, b28 |
| Vivid concrete outcome cue before a patient-vs-impulsive choice (agent EFT). | O2/S3 | [S] (human [E], LLM none) | K11, K32 |
| Evidence-link requirement: a pending intention may fire only if code can point to the observation that matches the trigger. | G2, G10 | [S] | K28, d10 |
| BKH-style caching analogue to see whether the agent plans for a different future state or only hedges. | none (diagnostic) | untested | K02, K22 |

## 8. Concrete tests on our bench

All arms at equal total tokens (setup counted, per G7). Bench items are our normal problem types plus synthetic PM items.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Multi-step tasks with a latent constraint set early and a trigger 20K or 100K tokens later (TriggerBench-style, plus negative controls matched 1:1) | (a) plain notes buffer; (b) typed intention ledger with evidence links; (c) ledger without evidence links | hit rate, false-alarm rate, Set-F1 | (b) over (a) by 10+ points Set-F1; (c) doubles false alarms, per d10 |
| T2 | Normal bench items with 2-3 output-format constraints, plus a concurrent main task | (a) constraints stated once up front; (b) plus trailing constraint reminder; (c) final code-checked constraint comparison | constraint compliance and main-task accuracy, reported together | (b) +12 to +17 points compliance (Mittal), possible loss of main accuracy; (c) should avoid the loss |
| T3 | Retrieval over a long profile or notes store with queries far from the answer in embedding space | (a) query-only; (b) 3 imagined next steps as queries (linear); (c) tree-style branching | recall, exact recall, retrieval tokens | (b) over (a) by 0.10+ recall; (c) about equal to (b) |
| T4 | Hidden-cause scenarios | (a) plain; (b) S1 "what will later steps need" list | root-cause accuracy | small gain; failures dominated by wrong root cause (73.8%) |
| T5 | Patient-vs-impulsive choices (smaller sooner vs larger later), several framings | (a) plain; (b) neutral future description; (c) vivid positive concrete outcome; (d) vivid negative outcome | rate of delayed choice | (c) above (a), effect size up to about 0.4 if it transfers; (b) and (d) about 0 (human valence pattern) |
| T6 | Caching analogue: agent hides items among locations under different "hunger" states, then states switch | (a) plain; (b) scratch notes; (c) imagined-needs step | share of items placed where they will be needed vs uniform spread; fit FPH, CCH and null models as in Amodio | diagnostic; expect many agents to spread evenly (the null won in jays) |
| T7 | Spoon-style choice: show a problem, remove it, offer 5 options after a delay, decoys that were right in a previous condition | (a) plain; (b) with notes; (c) with imagined-need step | accuracy vs chance 20% | strong models near ceiling; value is as a control for rule learning |
| T8 | Episodic recall at short vs long delay with one item type decaying (Clayton and Dickinson analogue) | memory store with and without timestamps | what-where-when accuracy | sanity check for the memory part; not a schema gain |
| T9 | Reasoning effort sweep on T1 | low vs high effort at equal tokens | hit rate vs false-alarm rate curve | gain in hits and loss on negatives (TriggerBench) |

Run at least 3 seeds per arm. The literature's effects rest on 90-item cells (Mittal) and 10-trial cells (CheeseBench), so confidence intervals must be reported.

## 9. What does not transfer, and why

- **Caching itself.** It is an innate behaviour of corvids. The BKH literature asks for non-species-typical behaviour for this reason. An LLM has no cache hoard, no hunger state, no body. Persona prompts supply drives (d18), so any "hunger" is role play.
- **Raby's one-evening design and 4-8 bird samples.** Weak statistics, and the replications went the other way. Nothing from the jay data gives an effect size worth importing.
- **Species-level claims about foresight.** Whether jays, crows, ravens or apes have MTT is contested and does not change how our agent should think.
- **"Imagined scene" phenomenology.** MTT is defined partly by the feeling of pre-experiencing (a24). An LLM cannot show that; only behavioural dissociations are usable.
- **Human EFT numbers.** The meta-analyses measure delay discounting in humans (mostly hypothetical choices). They do not measure planning quality, and an LLM's "patience" is a prompt-framing effect, not a self-control state.
- **Human future-self avatars (b21, c19, c20).** The output is a change in human feelings or intentions, not agent reasoning.
- **Neural claims.** The simulation account (Schacter and Addis) offers no implementation constraint for a scaffold.
- **Delay-without-sight in LLMs.** The spoon test's delay is trivial for a stateless model, so passing says less than it does for a crow.
- **Self-regulated simulative planning savings (25.8-95.3% fewer tokens).** These come from an RL-trained model, not a prompt (c23).
- **Anything that conflicts with SCHEMA 4b.** Do not add "slow down and think ahead" or unstructured reflection: those are established nulls. A prospection step must produce a typed artefact that code checks (a pending-intention record, a query list), not free thinking.

## 10. Open questions

1. Exact cache counts and statistics in Raby 2007 and Correia 2007 (primary text). Still unread (K05).
2. A pre-registered, larger-N western scrub-jay replication of Raby. Not currently possible (K27).
3. Does a prospection step ("imagine future needs, then plan") beat a plain scratch-note baseline on an agent task at equal tokens? No test found.
4. Do typed intention ledgers hold up on benchmarks and by authors other than those who built them? Four preprints, all authors' own methods, one counter-case (GLM-4.7).
5. What is the token cost of a trailing reminder itself, and does it help recent frontier models? Not measured (K29, K30).
6. Do the EFT meta-analyses survive an independent full-text read, and which moderators carry to an LLM prompt? (K32).
7. Do other frontier models match Claude Opus on the CheeseBench radial-arm maze with more than 10 trials per cell? (K21).
8. Is the spoon-test result robust to training history, and has it been tried in more crows or in a second lab? (K07).
9. Does an LLM agent track future need or only hedge when given states and locations (Amodio pattern)? No study (K22).
10. Is TriggerBench scored correctly? PM Acc uses a GPT-4o judge at T = 0 and LLM-generated scenarios (c07).
11. Do the PM benchmarks measure the same construct, given three definitions (formatting constraints, latent triggers, intention ledgers)?
12. Do reasoning models' false alarms fall when a ledger demands an evidence link? Untested.

## 11. Sources

[V] = opened and read this series (page or PDF text). [M] = abstract, snippet or citation only.

**Animal and developmental**

- [V] Suddendorf and Corballis (2007) The evolution of foresight. BBS 30:299-351. http://alicekim.ca/BBS.pdf (a01, a02, a03, a24)
- [M] Raby, Alexis, Dickinson, Clayton (2007) Planning for the future by western scrub-jays. Nature. https://www.nature.com/articles/nature05575 (a04, d01; abstract and figure captions only, full text paywalled, so counts are unread)
- [M] Correia, Dickinson, Clayton (2007) Western scrub-jays anticipate future needs independently of their current motivational state. Curr Biol. https://doi.org/10.1016/j.cub.2007.03.063 (a05, d02; abstract only)
- [V] Cheke and Clayton (2012) Eurasian jays overcome their current desires to anticipate two distinct future needs. https://pmc.ncbi.nlm.nih.gov/articles/PMC3297405/ (a06; b08 was an abstract-only copy)
- [V] Amodio, Brea, Farrar, Ostojic, Clayton (2021) Testing two competing hypotheses for Eurasian jay caching. https://pmc.ncbi.nlm.nih.gov/articles/PMC7804264/ (a07, a08, b01-b04, d03)
- [V] Martin, Martin, Roberts, Sherry (2021) No evidence for future planning in Canada jays. https://pmc.ncbi.nlm.nih.gov/articles/PMC8651407/ (a09, d04; b07 was a snippet-only copy)
- [V] Paxton and Hampton (2009) Tests of planning and the Bischof-Kohler hypothesis in rhesus monkeys. https://pmc.ncbi.nlm.nih.gov/articles/PMC2739929/ (a10)
- [M] Naqshbandi and Roberts (2006) Anticipation of future events in squirrel monkeys and rats. J Comp Psychol. https://doi.org/10.1037/0735-7036.120.4.34 (a11)
- [M] Mulcahy and Call (2006) Apes save tools for future use. Science. https://doi.org/10.1126/science.1125456 (a12)
- [M] Kabadayi and Osvath (2017) Ravens parallel great apes in flexible planning. Science. https://doi.org/10.1126/science.aam8138 (a13)
- [M] Osvath and Osvath (2008) Chimpanzee and orangutan forethought. https://doi.org/10.1007/s10071-008-0157-0 (a14)
- [V] Boeckle et al. (2020) New Caledonian crows plan for specific future tool use. https://pmc.ncbi.nlm.nih.gov/articles/PMC7735258/ (a15, b09, b10)
- [V] Esteve and Santariello (2021) New test, old problems. https://pmc.ncbi.nlm.nih.gov/articles/PMC8437223/ (a16)
- [V] Boeckle et al. (2021) New Caledonian crows' planning behaviour: a reply. https://pmc.ncbi.nlm.nih.gov/articles/PMC8437238/ (d06)
- [M] Clayton and Dickinson (1998) Episodic-like memory during cache recovery by scrub jays. Nature. https://doi.org/10.1038/26216 (a17; abstract plus design details from the 2025 revisit)
- [V] Davies, Clayton et al. (2025) Revisiting episodic-like memory in scrub-jays. https://pmc.ncbi.nlm.nih.gov/articles/PMC11880068/ (a18)
- [V] Davies and Clayton (2024) Is episodic-like memory like episodic memory? https://pmc.ncbi.nlm.nih.gov/articles/PMC11449162/ (a19, b16)
- [M] Suddendorf, Corballis, Collier-Baker (2009) How great is great ape foresight? https://doi.org/10.1007/s10071-009-0253-9 (a25; citation only)
- [V] Thom and Clayton (2014) No evidence of temporal preferences in caching by Western scrub-jays. https://pmc.ncbi.nlm.nih.gov/articles/PMC4004823/ (b05, b06)
- [V] Eurasian jays show episodic-like memory through incidental encoding. https://pmc.ncbi.nlm.nih.gov/articles/PMC11095760/ (b15)
- [V] Social influences on delayed gratification in New Caledonian crows and jays. https://pmc.ncbi.nlm.nih.gov/articles/PMC10699590/ (b17)
- [V] Siberian flying squirrels do not anticipate future resource abundance. https://pmc.ncbi.nlm.nih.gov/articles/PMC5109687/ (b18)
- [V] Redshaw and Suddendorf (2013) Foresight beyond the very next event. https://pmc.ncbi.nlm.nih.gov/articles/PMC3705196/ (b11, b12)
- [M] Redshaw, Taylor, Suddendorf (2017) Flexible planning in ravens? Trends Cogn Sci. https://doi.org/10.1016/j.tics.2017.09.001 (b13)
- [M] Suddendorf and Corballis (2010) Behavioural evidence for mental time travel in nonhuman animals. Behav Brain Res. https://doi.org/10.1016/j.bbr.2009.11.044 (b14)
- [V] Farrar, Boeckle, Clayton (2020) Replications in comparative cognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC7334049/ (d05)

**Human EFT**

- [M] Meta-analysis, Promoting farsighted decisions via episodic future thinking. J Exp Psychol Gen 2022. https://doi.org/10.1037/xge0001148 (b19, d16; abstract via Europe PMC)
- [M] Meta-analysis of episodic future thinking and delay discounting. QJEP 2022. https://doi.org/10.1177/17470218211066282 (b20, d17; abstract via Europe PMC)
- [V] Poonsiriwong et al. (2025) Simulating Life Paths with Digital Twins. https://arxiv.org/abs/2512.05397 (b21, b22)
- [V] Pataranutaporn et al. (2024) Future You. https://arxiv.org/abs/2405.12514 (c19)
- [M] Future You: multimodal AI-generated digital twins (2025). https://arxiv.org/abs/2512.06106 (c20; abstract only)
- [M] Ahmadi et al. (2025) AI-facilitated EFT for adults with obesity. https://arxiv.org/abs/2503.16484 (c21, d20; abstract only)

**LLM and AI**

- [V] Huet, Ben Houidi, Rossi (2025) Episodic memories generation and evaluation benchmark. https://arxiv.org/html/2501.13121v1 (a20, a23)
- [M] Pink et al. (2025) Position: Episodic memory is the missing piece. https://arxiv.org/abs/2502.06975 (a21, b29, c17; no results)
- [M] Towards LLMs with human-like episodic memory. Trends Cogn Sci 2025. https://doi.org/10.1016/j.tics.2025.06.016 (a22; abstract only)
- [V] Zhang et al. (2026) TriggerBench. https://arxiv.org/abs/2606.23459 (b23-b25, c07-c11, d15)
- [V] Liu and Gabriel (2026) PM-Bench. https://arxiv.org/abs/2607.12385 (b26)
- [V] Zhao and Wu (2026) Making prospective memory SLM-shaped (PIS). https://arxiv.org/abs/2609.01272 (b27, c13, d12; abstract page only for d12)
- [V] Pasternak et al. (2025, v4 2026) Beyond Reactivity: measuring proactive problem solving. https://arxiv.org/abs/2510.19771 (b28)
- [V] Chopra et al. (2026) Thinking Ahead: prospection-guided retrieval. https://arxiv.org/abs/2605.14177 (c01-c03)
- [V] Mittal (2026) Did you forget what I asked? https://arxiv.org/abs/2603.23530 (c04-c06, c25, d14)
- [M] Xu et al. (2026) ProMemAgent and CPMBench. https://arxiv.org/abs/2610.27400 (c12, d11; abstract level, ablation labels lost)
- [V] Bugaud (2026) CheeseBench v1 and v2. https://arxiv.org/abs/2604.10825 (c14-c16, d07, d08)
- [V] Bei et al. (2026) Pro-Memory. https://arxiv.org/abs/2611.05731 (d09, d10)
- [M] Groff (2026) Memory that looks forward. https://arxiv.org/abs/2609.22091 (d13)
- [M] Manakina et al. (2026) Delay-of-gratification micro-benchmark. https://arxiv.org/abs/2609.29509 (c22, d18; abstract only)
- [M] Efficient agentic reasoning through self-regulated simulative planning. https://arxiv.org/abs/2605.22138 (c23; abstract only)
- [M] Park et al. (2023) Generative Agents. https://arxiv.org/abs/2304.03442 (c18; abstract only)
- [M] Su (2026) Learning situation-conditioned thinking policies. https://arxiv.org/abs/2610.09590 (d21; abstract only)
- [M] Search records: arXiv listing queries on caching, future needs, Bischof-Kohler (c24, d19)
