# Critique: C05.07 Automated planning (STRIPS, PDDL)

Cross-check done 2026-11-10. Sources re-opened by downloading the arXiv PDFs and running pdftotext (2409.13373, 2305.15771, 2206.10498, 2405.04776, 2404.11833, 2305.14909, 2304.11477, 2305.11014, 2310.08118, 2402.08115). PDFs were saved under D:/research_scratch/C05.07/.

## Numbers re-checked (10 groups)

1. o1-preview Blocksworld 587/600 (97.8%), o1-mini 340/600 (56.6%), Fast Downward 600/600 at 0.265 s, o1-preview 40.43 s: CONFIRMED (Table 2). 23.63% on 20-40 step plans: confirmed in text.
2. o1 Mystery Blocksworld: CORRECTED in detail. Table 2 shows 247/600 (41.6%) zero-shot Mystery, 317/600 (52.8%) one-shot Mystery, and 224/600 (37.3%) randomized. Evidence line a15 gave 52.8% with no shot count, which hides that zero-shot is 41.6%.
3. GPT-4 Blocksworld: 206/600 (34.3%) is ONE-shot natural language; zero-shot is 210/600 (34.6%); one-shot COT 214/600 (35.6%). Confirmed. Lines a11/b24/c27 give 206 without saying one-shot. Line b03 cites "210/600" for zero-shot, which is correct. The two are not in conflict.
4. GPT-4 Mystery BW: one-shot 26/600 (4.3%), zero-shot 1/600 (0.16%) confirmed. Table layout is jumbled, so c04's Logistics figures (28/200 one-shot, 15/200 zero-shot) sit on a row labelled "Mystery BW (Randomized)" in the extracted text. Those two numbers may belong to the randomized-mystery Logistics row rather than plain Logistics. Treat them as unreliable until the PDF table is read visually.
5. Back-prompting 82% (41/50) Blocksworld, 70% (35/50) Logistics, 3.68 and 3.31 rounds, Mystery 5/50 (10%) with 7.0 rounds: CONFIRMED. IMPORTANT CORRECTION OF MEANING: these were 50 instances per domain chosen from instances GPT-4 had ALREADY FAILED one-shot, not a random sample. So 82% is not the overall solve rate. Evidence line a17/b05 wording ("on 50 previously failed instances") is right, but a17 and c10 present it as if general. Logistics used only the 179 instances solvable under 550 search steps.
6. Human baseline 39/50 valid, 35 of 39 optimal (89.7%): confirmed.
7. Stechly CoT: zero-shot 3.83%, stacking prompt 59.3%, universal algorithm 51.3%, progression-proof 6.89% (GPT-4); GPT-4-Turbo 19.1 / 37.1 / 40.6: confirmed. Text says "over 261 instances".
8. Thought of Search: 502/502 Blocksworld, 0.56-9.7 s; 1362 Game of 24 at 100%, 1.92-6.83 s; ToT 75% on 100 medium problems; 2.8 and 1 iterations: CONFIRMED.
9. Guan et al.: Only-LLM 15% / 0%, Fast Downward with LLM model 95% / 100%: confirmed. The 48% and 33% cells (VAL-backprompted LLM) are in a garbled table; assignment of 48% to Household and 33% to Logistics is the likely reading, not certain. CORRECTION OF CONTEXT: the PDDL model was corrected with human or validator feedback before planning; the 95% is not a fully automatic result. The paper's own words: failures were "only due to goal translation errors".
10. LLM+P Blocksworld: LLM+P 90 vs LLM-as-planner 20: confirmed. Other domains in that table are garbled; the claim "85-95% on some other domains" in a18 could not be confirmed from extracted text. Only Blocksworld (90) and Storage/Barman (95 and 20 with parentheses) are readable; Floortile 0. Use 90% on Blocksworld only.
11. Self-verification: 2310.08118 gives 40 / 55 / 88 (no BP / LLM+LLM BP / LLM+VAL BP), verifier 61/100 correct, 54 true positives, 38 false positives (84.45% of invalid plans passed), 7 false negatives: confirmed. The later paper 2402.08115 gives 40 / 55 / 60 / 87 / 83 for Blocksworld (60 = binary VAL feedback, 87 = first error, 83 = all errors), so the 88% vs 87% difference is two different papers. Evidence a21 and c15 cite different arXiv ids for the same 55% / 40% baseline; they are not independent (same authors, same data).
12. Silver et al.: GPT-4 Delivery 0.90, Forest 1.00, Gripper 0.90, Ferry 0.80, Spanner 0.10, Miconic 0.01, Heavy 0.60 confirmed. A second table in the paper (lines ~598-603) shows other values (for example Miconic 0.07, Spanner 1.00 in a different condition); not examined further. The source column meaning should be checked before using ablation numbers.

## Contradictions between sources

- Verifier loops help (VAL 87-88%, LLM-Modulo on TravelPlanner) but self-correction hurts (Natural Plan: lowers accuracy for all models). Not a real contradiction: sound external verifier versus the model critiquing itself. Claims K05 and K06 keep these apart.
- Reasoning models: Shojaee et al. report collapse on large puzzles; Opus and Lawsen argue the collapse is token limits and impossible instances. Marked contested (K15). Valmeekam's o1 results show a length cliff (97.8% to 23.63%) that supports a real limit, but the o1 and Shojaee tasks differ.
- Graph colouring: b09 gives o1-mini 96% (vs 16% for GPT-4), c09 gives o1-preview 94% inside LRM-Modulo. Different models and settings; not checked.
- LLM-built PDDL: Guan reports 95-100% planner success with a human-corrected model; Oswald et al. show only 25% of generated domains are heuristically equivalent. These are consistent: the first has human repair.
- PDDL-Instruct (b20/c23) reports Mystery BW 64% for a trained Llama-3-8B, above o1-preview's 52.8%. It is training, with test domains close to PlanBench, so contamination is possible. Not a scaffold result.

## Weak spots

- Independence is thin. Most LLM numbers come from one lab (Valmeekam, Stechly, Kambhampati and co-authors, who also argue for LLM-Modulo). Independent groups: Liu (LLM+P), Silver, Katz/Oswald/Kokel (IBM), Xie, Zheng (Natural Plan), Shojaee (Apple), Goebel and Zips, Huang. In K01 to K06 I counted independent sources honestly, not by paper count.
- The foundational and classical items (STRIPS, Bylander, Graphplan, HSP, FF, Fast Downward, PDDL, Ghallab book) are all from memory or Wikipedia and unopened (a01-a06, a10, a27, a28, c01, c02). There are no measured numbers for them. Nothing in the claims relies on them except K19.
- No direct test of backward (regression) search versus forward search in LLMs was found. O5 "work backwards" has only indirect support. This is the largest gap for our schema.
- Most results are on Blocksworld/Logistics, domains likely in training data. Benchmarks are 2022-2025 models; no results for the newest models were checked.
- Table cells from extracted PDF text (LLM+P table, Guan Table 2, GPT-4 Logistics rows) are garbled; the readings above are the likeliest, not certain.
- No token-matched comparison between a scaffold and plain reasoning exists in the evidence; cost data (b09) shows hidden tokens matter.

## Only seen in snippets or not opened

a01-a06, a10, a26-a28, c01, c02, c24-c26 (Pallagani, Dagan, SayCan) opened:false. a07 (IPC-3 summary) and a08 TLPlan table columns not fully readable. b18, b19, c16-c19, c21, c22 were marked opened by the earlier agents and not re-opened by me.

## GAPS

1. Does regression (planning backward from the goal) beat forward state simulation for an LLM at equal tokens on Blocksworld and Logistics? No study found.
2. How much of a scaffold gain comes from a code-held state and applicability check, versus the model reasoning longer, at equal total tokens including hidden reasoning tokens?
3. Does the 97.8%-to-23.63% length cliff of o1-preview hold for current (2026) models, and does a verifier loop shift the cliff?
4. How often does a sound-verifier loop cost more tokens than it saves? Marginal gain per backprompt round, and a stopping rule.
5. Can an LLM-written state-transition program (Thought of Search style) be trusted without a human, and how often is it wrong in ways its own tests miss (the 25% equivalence figure suggests often)?
6. Does the Mystery/obfuscation drop come from memorization or from lost commonsense cues, and does a scaffold close it?
7. What is the false-pass rate of an LLM critic that sees a precondition trace, compared with one that sees only the plan (the 84.45% figure was for plain plans)?
8. How well do agents detect unsolvable instances (o1: 27% flagged), and does an explicit "prove a plan exists" step fix it?
9. Do planning gains transfer to non-PDDL tasks (TravelPlanner, Natural Plan style) with hand-written critics, and how much critic engineering is needed?
10. Is the human baseline (78% valid) beaten by a scaffolded model on the same instances, and at what token cost?

## Gap search results

Done 2026-11-10. WebSearch budget was exhausted by other agents and the Semantic Scholar, OpenAlex and arXiv search APIs returned 429, so I worked from known arXiv ids opened as PDFs (2212.13894, 2411.19865, 2506.06941, 2506.09250, 2402.01817, 2406.04520, plus the earlier local PDFs). Evidence is in evidence_d.jsonl (d01-d16). No newer (2026) papers could be searched for.

- Gap 1 (regression vs forward, equal tokens): STILL OPEN. Only indirect evidence: LAMBADA (d01, d02, d16) shows backward chaining with a modular sub-goal loop wins on logic proofs (44% relative over CoT, 11.8x fewer calls at Depth-5) while plain backward CoT does not. No STRIPS test. Claim K18 updated, K19 added.
- Gap 2 (code-held state vs longer reasoning at equal tokens): PARTLY. d04/d06: sound verification plus blind resampling gives most of the gain on Blocksworld (68-72% vs 87% with first-error feedback, 40% base). No token-matched comparison against a long-reasoning model exists.
- Gap 3 (length cliff for 2026 models, verifier shift): STILL OPEN. d08/d09 show the cliff location depends on sampling (N=4 vs N=30), output form and impossible instances (K22, contested). No verifier-shifted cliff measured; no 2026 models found.
- Gap 4 (cost of verifier loops, stopping rule): PARTLY. d06: LLM verifier loops degrade each round, sound verifier loops rise to an asymptote, resampling prompts are cheaper. Marginal gain per round is only in a figure; no stopping rule study.
- Gap 5 (trust in LLM-written transition code): STILL OPEN. d10: 1.2-2.4 interactions with human error messages; no silent-error rate measured. K23 added.
- Gap 6 (memorisation vs lost cues): PARTLY. d11: randomized names slightly worse than deceptive names (2% vs 4.3%); d12: verifier loop does not close the gap. Still no control that keeps names and changes dynamics.
- Gap 7 (critic with precondition trace): STILL OPEN. d05 gives only plan-only critic rates (Blocksworld FP 6.5%, FN 15.48%; Mystery FP 18.55%, FN 97.09%).
- Gap 8 (unsolvable detection): PARTLY. d07 confirms the 27% figure and adds a 16% / 79% Mystery result and 11.5% false alarms. No existence-proof step was tested anywhere. K21 added.
- Gap 9 (transfer to non-PDDL, critic engineering): STILL OPEN. d13-d15 show self-correction hurts and critics are hand-written, with no cost accounting.
- Gap 10 (human baseline vs scaffolded model): STILL OPEN. No new source found.

Closed outright: none. Narrowed: 2, 4, 6, 8.
