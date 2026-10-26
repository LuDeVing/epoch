# Critique and cross-check: 06 Resource-rational analysis and strategy selection

## 1. Numbers re-opened (this session, from PDF text)

Confirmed unchanged unless noted.

1. Lieder and Griffiths 2017 (OSF PDF): 81.67% / 29.83% / 27.00% merge-sort choice, 83% adaptive, 70.5 +/- 3.2% model vs 59.0% best SCADS, BIC 60.70 vs 68.94, MSE 0.0018 vs 0.0043, casino engagement 37% to 19%, Exp 3 t(143)=2.87 d=0.26 with 57 excluded, Exp 4 76.2% and 70.4% to 80.4%, 73% on trial 1. All confirmed. NEW: the paper itself reports that people (83.0%) beat the model (70.5%), t(298)=2.34, p=0.01. a04 should be read as "model underpredicts adaptivity", not "model matches people".
2. NIPS 2014 (Lieder et al.): 99.78% vs 98.5%, 85.3% on random lists, 102.5 vs 27.96 s, 47.90 s restricted, 88.1 +/- 0.7% vs at most 30%. Confirmed.
3. CogSci 2015: 64.6% [62.5, 66.6], MSE 0.0050 vs 0.0048, model stays above 70%. Confirmed.
4. Callaway et al. 2022 PNAS: 94.4 vs 77.0 vs 73.5 (d=0.59, P=0.005); Exp 2 81.2 / 49.0 / 57.6; hotel-first 46.3 / 39.4 / 39.4 / 23.5; mediation 12.9. Confirmed. The PDF also gives an Exp 1 transfer result not in our lines (74.6 vs 57.0 vs 57.5, d=0.48 and 0.44).
5. De Sabbata et al. (arXiv 2410.05563): 35-42%, 23-32%, 50.3 / 34.4 / 19.0 / 0.5, 61.9 vs 63.5 and 215.1 vs 146.2 tokens, MMLU-CF rows. Confirmed. Caveat: the extracted MMLU-CF table rows are jumbled, so the model attached to the 27.0 to 29.5 and 40.2 to 36.4 rows rests on table layout (c10 says 3B and 8B; plausible, not proven). The abstract's "23 to 45%" is wider than the body ranges; use the body ranges.
6. ARES (arXiv 2603.07915): Retail 35.0 / 47.3 / 54.8 / 43.5 random; Airline High 38.0, Medium 42.0, SFT 36.0, RL 42.0; 52.7% reasoning-token cut; BrowseComp-Plus 41.3 vs 42.7; WebArena 46.5 vs 45.0; no-fine-tune router 41.7. Confirmed.
7. Zhang et al. (arXiv 2507.11423) Table 3: 47.2 / best single 49.0 / vote 54.9 / vote+prob 57.3 / verifier 46.9 / oracle 82.9; R1-Distill verifier 74.1, vote 68.4; min entropy 48.8, max prob 48.4. Confirmed.
8. RACER (arXiv 2605.10805) Table C.4: reasoning fractions 99.91 / 99.51 / 99.88 and cost ratios 19.07 / 6.25 / 6.36 confirmed. CORRECTION to c26: the accuracy columns in the extracted table are jumbled. The values 78.34 / 86.50 / 87.86 appear under "All-reasoning", and a row 78.35 / 86.50 / 87.86 appears beside them. Read them as "self-routing accuracy equals all-reasoning accuracy to within 0.01", not as a separate gain over all-instruct. The conclusion (self-routing is just always-reason) stands.
9. Hu et al. 2026: beta +1.0212 and -0.1466, AIC 2727.29, pseudo R2 0.160, judge accuracy 0.86 and kappa 0.76. Confirmed.
10. Callaway 2018 BMPS and Lieder 2018 anchoring numbers were not re-opened; they remain first-pass reads.

No number needed a large change. Two lines need re-wording (items 1 and 8).

## 2. Duplicates that inflate counts

- a03 and a16 are the same experiment (NIPS and journal). b01-b03 = c01-c04 (same 2015 paper). a18 = b07. a28-a29, b21, c07-c10 are one paper (RaM). b09-b13 are one paper. "Independent sources" in claims counts papers from distinct labs, not lines.
- a30 is the wrong paper (McGill, Nobandegani); do not cite it as Lieder.

## 3. Contradictions between sources

- Fit of metareasoning vs SSL: a tie in 2015 (MSE 0.0050 vs 0.0048) but SSL clearly better in 2017 (BIC 60.70 vs 68.94, MSE 0.0018 vs 0.0043) on the same Rieskamp and Otto data. The fitting differs (2 free parameters on block averages vs choice-level BIC).
- Anchoring with provided anchors: Lieder 2018 finds cost effects; Epley and Gilovich 2006 found none. Unresolved; the effect is 3 points.
- Learning rule in planning: SSL-style under 1% of people in He and Lieder 2024, yet SSL is the best fit to older choice data. Different tasks.
- RaM: tokens fall, but one 8B out-of-domain row lost 3.8 accuracy points; the abstract says "matching or increasing".
- Oracle gap (Zhang) vs router success (ARES): in agent tasks routers recover nearly all of high-effort success, in logic puzzles selection recovers little. Likely because ARES targets cost, not accuracy above the best fixed setting.

## 4. Weak spots

- Almost all human evidence comes from one lab (Lieder, Griffiths, Callaway, Jain, He). Outside-lab human data is Rieskamp 2008 (a reanalysis by the SSL author) plus Newell et al. and Broder and Schiffer, read second-hand. No independent replication of the four 2017 experiments was found.
- Human samples are online (MTurk, Prolific) with 15-28% exclusions; effects are often small (d 0.16 to 0.26 in Exp 3; 0.17 far transfer).
- Features and strategies are hand-set in every model. Selection from features says nothing about discovering features.
- LLM routing papers are mostly 2026 preprints; many use LLM-judged rewards, small test sets (Airline about 50 tasks), or routers trained per setting. None runs the pure Lieder-Griffiths form (per-strategy reward and time regressions with Thompson sampling) on an LLM.
- Routing between models (RouteLLM, FrugalGPT, R2-Router) is not the same as choosing a reasoning mode inside one model.
- Tooling note: the shared scratchpad was also used by a parallel agent, which overwrote a script file mid-run; the claims here were regenerated from a uniquely named script.

## 5. Seen only in snippets or abstracts

Rieskamp and Otto 2006 (a32, b26), Payne 1988, Russell and Wefald 1991, Shrager and Siegler 1998, Lieder and Griffiths 2020 BBS (a36, b08; PDF blocked), Scheibehenne 2013 (b25), Paglieri 2025 (c30), xRouter (c31), the Nature Human Behaviour version of Callaway 2022 (c32; conference version opened), and the search note c33. These are second-hand and are not used as support in claims.

## GAPS

1. Does a code-only class table (pass rate and token cost per problem class, Thompson-sampled) beat fixed modes and an LLM-chosen mode at equal tokens on our own tasks? No study runs this exact form on an LLM; our logs are the only test.
2. Which cheap features separate classes well enough to pay? Problem size predicts LLM strategy (Hu) but with pseudo R2 0.16; the sign of entropy flips across settings (Li). What minimal feature set survives a change of backbone?
3. How many logged runs per class are needed before the table beats a single global mode, and how fast does it go stale after a distribution shift (humans: slow and asymmetric)? Needs a change-detection rule.
4. Is lambda (token price) fixed or estimated? Human data say opportunity cost sets thinking amount; what lambda makes the gate match the best fixed budget?
5. Does process-level feedback (which step wasted tokens) improve a class table more than outcome-only logs? The only support is the Callaway PNAS tutor on humans, one lab, d=0.59 near and 0.17 far.
6. Where does the oracle gap between modes live (Zhang: 47.2 vs 82.9), and is any of it predictable before running, or is it sampling noise? Needs repeated runs per item.
7. When is the short mode better than the long mode on our classes (ARES Airline, RACER judge tasks, easy items)? Per-class pass rate at three token budgets is the missing table.
8. Do the 2017 strategy-selection results replicate outside the lab, and does the 83% vs 70.5% gap (people beat the model) reflect prior knowledge an LLM also has? No search for independent replications was done.
9. Can strategy discovery (adding a mode) be done safely online? Humans find a new strategy in under 30% of cases in 120 trials (He and Lieder); BMPS assumes a fixed set.

## Gap search results

Web search quota was exhausted at the start of this run, so I did not search for new papers. I opened four primary papers by known arXiv id (Garivier and Moulines, Russo et al., Snell et al., Brown et al., Chen et al.) and re-read three already-extracted papers (Zhang 2025, RACER, ARES). New lines are in `evidence_d.jsonl` (d01-d15; d12 is a record of the failed replication search, opened:false). Claims K10-K13 were extended and K19-K22 added.

- Gap 1 (table vs fixed vs LLM-chosen at equal tokens): open. Only our logs can test it.
- Gap 2 (cheap features): partly closed. Difficulty bins by pass rate predict the best strategy (Snell, K20), and item size shrinks the oracle gap (Zhang, d06). But Snell's bins cost 2048 samples per question and that cost is not counted. Backbone-stable feature set: still open.
- Gap 3 (runs needed, staleness): partly closed in form. Forgetting is needed (window, discount, or decayed Beta posterior; K19). No count of runs per class exists; measure by log replay.
- Gap 4 (lambda): partly closed in form. Treat lambda as a dual variable set by the token budget (RACER, K21). Match to the best fixed budget is untested.
- Gap 5 (process feedback): open, nothing new.
- Gap 6 (oracle gap): partly closed. The Zhang oracle is any-of-five prompts with no same-sample control; any-of-k rises log-linearly from sampling alone (Brown). The gap is smaller on hard items. How much is selectable stays open until a repeated-run control is run.
- Gap 7 (short vs long): partly closed. Easy-bin evidence that heavy modes lose (Snell d04, Chen d08, ARES Airline d11). Per-class pass rate at three budgets on our tasks is still missing.
- Gap 8 (replication outside the lab): open; search blocked (K22 on hold).
- Gap 9 (safe online strategy discovery): open, nothing new.

Caveat on sources: the Snell, Brown and Chen numbers are maths and code benchmarks; some Chen percentages were read from a figure. Airline numbers in d11 beyond Table 5 come from earlier lines.
