# Model-based diagnosis: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl, set before the stricter independence re-check. Treat each row as a candidate until that check is done. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Ids are global (C09.01-K05 and so on). Almost all LLM evidence here is from 2024-2026 papers, often read at abstract or table level, and many results are single-source (see section 7).

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 01 Consistency-based diagnosis and conflicts | [DEEP](subfields/01_consistency_based_diagnosis_and_conflicts/DEEP.md) | 36 | 11 (contested 2, single-source 23) |
| 06 Probing and measurement selection | [DEEP](subfields/06_probing_and_measurement_selection/DEEP.md) | 31 | 13 (contested 2, single-source 16) |
| **Total** | | **67** | **24** |

Each researched subfield has a UNKNOWNS.md with 14 test rows (28 in all).

Not yet researched (from SUBFIELDS.md): abductive diagnosis; hitting-set tree search and efficient algorithms (touched only inside 01); diagnosability and sensor placement; spectrum-based fault localisation (touched only inside 01); software, spreadsheet and knowledge-base debugging; the Hamscher, Console, de Kleer readings. The 06 DEEP also names parallel subfields: troubleshooting search strategies, hypothesis limits, adaptive stopping, verification design, anomaly handling and fixation, accuracy of monitoring, LLM debugging.

## 2. Established findings, merged

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | Diagnoses are exactly the minimal hitting sets of the conflict sets (Reiter). Code can compute them from conflicts alone. The model must not do this step. | C09.01-K01 | S5, S6, G5 | partly (G5 code selects; no hitting-set step or blame rule) |
| F2 | Published hitting-set algorithms had a real bug (non-minimal conflicts lost true diagnoses). Test any hitting-set code against brute force, including the counterexample set. | C09.01-K02 | G5 (engineering) | no |
| F3 | Full diagnosis does not scale. Cheap approximate rankers trade completeness for speed. Use a cheap ranker first, exact hitting set only on small step counts. Conflict-order heuristics have boundary conditions. | C09.01-K04, C09.01-K22 | G12 | partly (G12 spends by difficulty; no ranker rule) |
| F4 | Size caps are the main practical lever (c432: mean measurements 92.3 to 4.5). But after new evidence new diagnoses are supersets of old ones, so a fixed small cap loses the culprit. Recompute from all conflicts each attempt; raise the cap by one when no hitting set fits. | C09.01-K05, C09.01-K26 | S6 | no |
| F5 | With several faults the minimal diagnoses explode and precision falls. A ranking step (probability, size, spectrum score) is required. | C09.01-K06 | S6, G5 | no |
| F6 | Reiter's theory has no probabilities and no entropy rule. Priors, Bayes updates and entropy probe choice come from de Kleer and Williams 1987, which was not read. Cite as unverified. | C09.01-K25 | S6, S7 | no (and no numbers to be added) |
| F7 | LLMs are poor at naming the failing step in a multi-step trace (best step-level 14.2%, reasoning models under 10%, worse with longer context). Ban model-only blame. | C09.01-K14 | G2, G10 | partly (G2 says code locates; no explicit blame ban) |
| F8 | LLMs cannot reliably find their own errors but often fix them once the location is given. Unaided self-correction flips right answers to wrong more than the reverse. | C09.01-K15 | G2 | yes (G2, 4b self-reflection) |
| F9 | Repair loops flatten fast: 89% of repairs on the first try; gains flatten after about four rounds. | C09.01-K16 | S5 | yes (S5 at most 2 rounds; see X5) |
| F10 | Code, not the model, should score candidate probes. Expected information gain over a sampled hypothesis set beat prompt-only, CoT and model-picked questions (mean 70.7 vs 30.3 / 39.5 / 55.4 / 57.6). | C09.06-K01 | S7, G5 | partly (S7 has a discriminating test; no probe scoring) |
| F11 | Asking the model to reason about which question is best does not close the gap to computed scoring. Do not trust self-judged informativeness. | C09.06-K03 | G10, S7 | partly (G10 reasoning text is not evidence) |
| F12 | Keep an explicit hypothesis list in code and filter it by every observation. Raw in-context beliefs collapse (18 vs 88). | C09.06-K04 | S6, S7, memory | no |
| F13 | Probing works when answers cleanly eliminate hypotheses and a finite candidate list exists. Soft answers and open sets weaken it. Enumerate candidates first. | C09.06-K07 | S2, S6, S7 | no |
| F14 | The selection rule matters more than the proposer: a random proposer reranked by information gain matched an LLM proposer; more candidate probes help up to about 10. | C09.06-K18 | S7 | no |
| F15 | Un-scaffolded LLMs probe badly over several turns (early enumeration, repeated questions; GPT-4 wins 0.31 and 0.50 of 20-question games, humans 0.24 and 0.31). Log repeats and early guesses. | C09.06-K10 | G6, logging | no |
| F16 | Self-asking is poor and a separate gate changes it. Models notice ambiguity far more than they act (clarifying questions about 5% at best). Naive asking can hurt (MediQ -11.3% relative); a separate gate recovered 51.2% of the gap; in coding a separate checker raised resolve rate 61.2 to 69.4%. | C09.06-K19, C09.06-K24 | S7 gate, G1 | partly (G1 doubt only on a signal; 4b bars stated confidence as a stop signal) |
| F17 | Probing gains shrink as the base model gets stronger or the task softer (gap about 15 points for GPT-3.5, about 2 for GPT-4o-mini). Probe only above an uncertainty threshold. | C09.06-K06 | S7 gate, G7 | partly (G7, G12) |
| F18 | Reasoning models still leave probe-selection headroom: they pick the best of their own candidates in 19-36% of turns; QuestBench thinking models near 40-50% vs 99.8% for search. | C09.06-K23 | S7 | no |
| F19 | With one fault and independent checks, order by probability over cost; with equal values this is halving. The general policy is NP-complete. | C09.06-K12 | S7 | no |
| F20 | One-step greedy probe choice is theoretically sound (adaptive submodularity, log-factor competitive). Read as worst case, not as a percentage. | C09.06-K13 | S7 | no |
| F21 | Entropy selection can fail when the same wrong model chooses and interprets (fixation), and can collapse an LLM-proposed pool. Periodically choose a probe that could falsify the leader. | C09.06-K15 | S7, G1 | partly (S7 counterexample search) |

## 3. Contradictions between subfields

| # | Tension | Claims | Reading |
|---|---|---|---|
| X1 | More information or effort helps in one place and hurts in another. Located conflicts help repair (F8); test traces lowered F1 .85 to .78 and effort collapsed one model (.49 to .15). | C09.01-K15 vs C09.01-K10, C09.01-K35 (contested) | Cause not isolated (context limit, parse errors). Per-model, not general. See T13. |
| X2 | Computed probe scoring wins widely (F10), but with reasoning models the gain is modest or negative and costs 61x a trained policy. | C09.06-K01 vs C09.06-K17 (contested), C09.06-K23 | Wins shown on non-reasoning models. Open until the equal-token test (T6). |
| X3 | Asking helps (F10) and asking hurts (F16: naive asking -11.3%). | C09.06-K01 vs C09.06-K19 | Not a true conflict: the difference is the gate. Probe only on a computed signal. |
| X4 | Prune hard with a small cap (F4) vs a fixed small cap loses the culprit after new evidence. | C09.01-K05 vs C09.01-K26 | Resolved by the auto-raise rule. |
| X5 | SCHEMA S5 caps revision at 2 rounds; gains keep rising to about 4 on weaker models (Llama 405b 29.0 to 44.9%), while 89% fix on the first try. | C09.01-K16 vs SCHEMA S5 | Cap 2 fits the 89% but may leave gains on weak models. Plot pass rate by round (planned in the C09.01-K16 test). |
| X6 | Greedy probing is near-optimal in theory (F20) yet fails under a wrong model (F21). Theory assumes the model is right. | C09.06-K13 vs C09.06-K15 | Keep greedy, add a falsifying probe on stall (T10). |
| X7 | Order by prior over cost (F19) needs priors, but the only LLM test of priors is synthetic and the GDE source is unread. | C09.06-K12 vs C09.01-K25 | Theory only until T11. |
| X8 | With A01: A01 F10 says refinement plateaus after about 2 rounds; here the plateau is about 4. | A01.06-K17 vs C09.01-K16 | Different tasks; unresolved. |
| X9 | With A01: A01 F21 says "slow down" cues fail; here a forced gate works where self-initiated asking fails. | A01.05-K06 vs C09.06-K24 | Agrees: code-triggered beats instructed. |
| X10 | With A01: A01 F12 says LLMs rarely find falsifying cases alone; probe choice shows the same. | A01.07-K12 vs C09.06-K10 | Agrees. |

## 4. Recurring mechanisms

| Mechanism | Where it shows | Consequence |
|---|---|---|
| M1 Code computes; the model only fills a slot. | Hitting sets (K01), probe scoring (C09.06-K01), posterior, gates. | Same rule as G5. Strongest cross-subfield pattern. |
| M2 The model cannot localise or choose, but can act once told. | Blame (K14), self-correction (K15), probe choice (C09.06-K03, K10, K23). | Locate or score by code, then hand the model one located item. |
| M3 Extra context or compute helps only above a model-strength and task-softness line. | C09.01-K10, K35; C09.06-K06, K17. | Per-model caps and gates; measure at equal tokens (G7). |
| M4 A gate must be computed, not self-reported. | C09.06-K19, K24; C09.01-K26 (cap raise on empty). | Triggers from counts: empty conflict, hypothesis share, disagreement. |
| M5 The candidate space must be finite and clean. | C09.06-K07, K15; C09.01-K06. | Enumerate and filter first; open spaces stall or explode. |
| M6 Pruning buys speed and costs recall. | Size caps (C09.01-K05, K26), pruned diagnoses (C09.06-K15). | Always keep a raise rule. |
| M7 Who proposes matters less than who selects. | C09.06-K18; best-of-N with a checker as a fair baseline (DEEP 01 A10). | Baselines get the same checker. |

## 5. Merged tests

| Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|
| T1 Hitting-set brute-force check | none (C09.01 DEEP E11; K02) | Property-test the hitting-set function on random conflict collections incl. {{a,b},{b,c},{a,c},{b,d},{b}}. Cheap; do first. | High |
| T2 Conflict statistics on real traces | C09.01-U1, C09.01-U8 | Label 100 traces; report empty rate, size-1 rate, mean size, per unit of blame (step, claim, check). | High |
| T3 Blame head-to-head | C09.01-U2, C09.01-U5, C09.01-U6, C09.01-U7 | Hitting set vs model blame vs last step of smallest failed check vs best-of-N with the same checker (plus Ochiai, toggle, prior ranking, accumulate-vs-latest arms) at equal tokens. | High |
| T4 Cap recall and raise rule | C09.01-U4 | Reuse T2 traces; recall of the true set at caps 1, 2, 3 and candidate count. | High |
| T5 Feedback format | C09.01-U3, C09.01-U9, C09.01-U11, C09.01-U14 | Minimal core vs raw error text vs correction subset vs QXR claim-set localisation; vary suspects shown (1, 3, all). | High (U3), Med (rest) |
| T6 Equal-token probe head-to-head | C09.06-U1, C09.06-U2, C09.06-U11, C09.06-U14 | Thinking model vs code-scored probes (split vs EIG; N, K sweep; K=2 on enabling items) at equal tokens. | High |
| T7 Form rules baseline | C09.06-U3, C09.06-U13 | Plain vs plain plus no-repeat / no-early-guess / open question vs scored. Zero token cost. | High |
| T8 Noisy answers | C09.06-U4 | Flip 0, 10, 20% of probe answers; scored vs unscored vs scored with re-ask. | High |
| T9 Computed probe gate | C09.06-U5, C09.06-U8 | Hypothesis-share gate vs ask-always, no-ask, self-initiated, separate check; then token-priced VoI. | High (U5), Med (U8) |
| T10 Falsifying probe on stall | C09.06-U6, C09.06-U12 | Max-entropy vs leader-falsifying vs positive-test vs switch rule on fixation-prone items. | High |
| T11 Priors and cost | C09.06-U7 | Uniform vs prior vs prior/cost suspect order; priors from held-out history. | Med |
| T12 Code-held posterior | C09.06-U10 | LLM tracks vs code tracks posterior with a likelihood table. | Med |
| T13 Effort and trace ladder per model | C09.01-U10 | Effort x traces; log overflow, parse failure and wrong answer separately; set G11 caps. | Med |
| T14 Probe roles | C09.06-U9 | Ablate challenger, steward, differential, ensemble; keep only roles that pass. | Med |
| T15 Strategy union | C09.01-U12 | 4 different strategies vs 4 samples of the best at equal tokens. | Low |
| T16 Next check by split | C09.01-U13 | Split of top diagnoses vs random vs cheapest. Shares design with T6; run after T3. | Low |

Run order: T1, then T2 with T4, then T3, then T7, T6, T8.

## 6. Not to add

| Idea | Why not | Claim ids |
|---|---|---|
| Probability ranking, Bayes updating or entropy probe numbers from GDE | Source unread; second-hand. | C09.01-K25 |
| "Assume normal" for text steps | No model of normal behaviour for prose; we may only be doing hitting sets over check supports. | DEEP 01 sec 9 |
| Model-only blame of a failing step | 14.2% best, under 10% for reasoning models. | C09.01-K14 |
| Same model as the consistency oracle or revision judge | Self-correction flips right to wrong. | C09.01-K15 |
| Model self-judged "which question is best" | CoT does not close the gap to computed scoring. | C09.06-K03 |
| Self-initiated probing from the model's feeling | Models notice but do not act. | C09.06-K24, K19 |
| Fine-tuning for informative questions | Outside our constraint; upper bound only. | C09.06-K20 |
| Adding test traces or maximum effort by default | Contested; can collapse some models. | C09.01-K10, K35 |
| Exact lookahead beyond one step | Greedy is the default; two-step only for enabling-test items (untested). | C09.06-K13 |

## 7. Gaps

- Only 2 of about 10 subfields researched. Abductive diagnosis, diagnosability, spectrum-based localisation and software/KB debugging are open.
- No LLM study runs conflict plus hitting set over several failed attempts end to end (C09.01-K23, single-source). T3 would be the first.
- Every cap, empty-rate and ranking number comes from a toy simulation, not real traces (C09.01-U1, U4).
- de Kleer and Williams 1987 and related papers are unread; all prior, Bayes and entropy statements are second-hand.
- All LLM probing results use a simulated answerer and closed lists. No real noisy executable probes (C09.06-U4).
- Reasoning-model evidence is thin and partly self-reimplemented (C09.06-K17, K23).
- 2026 LLM-plus-conflict results (Sarkar n=14, He three models, SemLoc 250 programs) are unreplicated.
- Only the A01 synthesis exists to cross-check; section 3 compares against A01 alone.
- No probe cost model (tokens, wall-clock, irreversibility).
- 43 of 67 claims are single-source or contested; the stricter independence re-check is still pending.

**Audit (code check, 2026-10-26):** C09.01-K26, C09.06-K12 had only one opened source and are now single-source, not established. Treat their rows above as unconfirmed.
