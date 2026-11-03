# Critique: C12.07 MDPs and POMDPs (cross-check)

## Corrections made (sources re-opened this session)
1. Qiu et al. Bayesian Teaching (arXiv 2503.17523v3): Bayesian Assistant final-round accuracy is 81% (Fig 2), random 37%; off-the-shelf LLMs 36-58%, humans about 58%. Line c09 said "about 68%": wrong. b10 (81%) is right.
2. Krishnamurthy et al.: the ">60% suffix failure" headline is T=500, N=20; the 32-prompt scan is T=100. Line b09 mixes these. Fig 4 says three GPT-4 configs show no suffix failure, but two of those fail by uniform-like choice; only BSSC0 truly works. "1 of 32" holds.
3. EVOLvE (2410.06238): 50.2 vs 27.5 is Gemini 1.5 Flash, multi-armed bandit, few-shot, summary vs raw history. For fine-tuning the order reverses (raw 65.6 above summary). Line c22 said the summary is the "largest single lever" without that caveat; corrected in claim K10.
4. BSE Tiger (2609.10036): 38/40 vs 32/40 confirmed, but return CIs overlap ([-4.41, 8.24] vs [-25.75, 1.75]). The paper itself says the attack-graph ordering is not significant. Do not treat 95% vs 80% as proven.
5. Valmeekam 2023 confirmed: 40 / 55 / 88 of 100; verifier right on 61 of 100.
6. LLM-MCTS VirtualHome numbers confirmed (91.4, 71.2, 83.4, 47.0, fine-tuned GPT2 81.3 / 59.0). Tru-POMDP setup (300 tasks, step limits 25/30/35, baselines under 20% and about 40%) confirmed. UoT 38.1 / 46.6 / 33.8 / 29.9 / 28.3 / 12.4 confirmed; the paper does not say whether these are absolute points or relative.
7. Ni et al. "18 out of 21 environments" found in the text; the 6-of-8 occlusion claim was not re-checked.

## Contradictions between sources
- Qiu 81% (b10) vs 68% (c09): resolved above.
- Summary vs raw history: helps prompting, hurts fine-tuning (EVOLvE).
- Hausknecht and Stone: recurrence gives mixed results; Ni 2022 says it is strong once tuned. The difference is tuning, not nature.
- BSE: belief helps on Tiger (weakly), no effect on the larger task.

## Weak spots
- Only one source (BSE, single preprint, N=40) tests a chat LLM on a true POMDP. The rest is bandits, planning domains or games.
- PBVI time on Tag is garbled in the PDF table (180,880 s vs 59,772 s quoted by Perseus); use ratios only.
- RAP, UoT and Tru-POMDP use different budgets and baselines; no equal-token comparison exists anywhere.

## Only seen in snippets or not opened
a09, a10, a31, b23-b26 (Papadimitriou-Tsitsiklis, Madani et al., Puterman, DESPOT in b-file), c03, c17-c21. The complexity claim in K02 rests on citations. Puterman was never opened.

## GAPS
1. Does an LLM handed an exact code-computed posterior (BSE-style) beat free-text belief tracking at equal tokens on Tiger and RockSample-small with N of 200 or more?
2. What is the right commit threshold for an LLM agent, and does a stated stop rule (net evidence 2) change behaviour versus no rule?
3. At equal tokens, does particle-style search over K sampled hypotheses (POMCP or Tru-POMDP style) beat one long chain of thought, and what K is best?
4. Where does summary-over-raw-history stop helping (prompt vs fine-tune split) for non-bandit tasks such as diagnosis or code debugging?
5. Is UoT's 38.1% gain absolute or relative, and does it survive an equal-token comparison against self-consistency?
6. Can a sound verifier be built for open-ended tasks that lack a VAL-like checker, and how much is lost with a weak verifier?
7. Does belief-state compression (PABU-style pruning) help zero-shot agents, or only trained ones?
8. Do stated beliefs and actions agree (Qiu: under 50% agreement in some models), and does forcing the action from the stated belief fix it?
9. How large is implementation variance (the POMCP reproduction failure) when comparing LLM planners?
10. Puterman and the complexity papers were never opened: confirm the exact classes (PSPACE-complete, P-complete) from the sources.

## Gap search results (evidence_d.jsonl, d01-d20)
Search budget: WebSearch was cut off after the first calls; arXiv/OpenAlex/Semantic Scholar APIs were rate-limited, so work used direct PDF fetches and the local text copies.

CLOSED
- Gap 5 (UoT 38.1%): relative gain. Rebuilt exactly for Llama3-70B (46.6 = mean of relative gains over closed and open set; absolute gain only +8.7 to +11.5 points). Equal-token check exists in the paper (Table 2): at about 4.6k tokens, CoT-SC k=33 scores 32.6/37.6/42.5 vs Pruned UoT 48.1/88.4/63.2. Caveats: n=3 runs, authors' own baselines. (d01-d03)
- Gap 10 (complexity classes): finite-horizon POMDP PSPACE-complete and MDP P-complete confirmed in an opened restatement (Bernstein et al. 2002); infinite-horizon undecidability confirmed from the Madani et al. abstract and a 2026 restatement. The 1987 paper and Puterman were still not opened directly. (d18-d20)
- Gap 8 (stated belief vs action): untuned LLMs agree under 50% between stated belief and direct action; an external rule on the stated belief was more accurate than the direct choice (Qiu appendix). Only one task; Qwen 2.5 is an exception. Closed for this task, untested elsewhere. (d07)
- Gap 6 (weak verifier loss): measured. GPT-4 verifier FNR 97% on Mystery Blocksworld, Game of 24 standard 5% vs LLM+LLM 3% vs sound 36%; CoT verifier at 99% accuracy still leaves a 6 point gap at 17x tokens. How to BUILD a sound verifier for open-ended tasks stays open. (d08-d10)

PARTLY CLOSED
- Gap 4 (summary vs raw history, non-bandit): on SWE-bench Verified (500 instances, 5 setups) LLM summary did not beat masking (53.8 vs 54.8 for Qwen3-Coder 480B; 35.6 vs 36.0 Gemini 2.5 Flash), both about -50% cost; summaries lengthened runs 13-15%. Diagnosis tasks not found. Differences are within the +-3-4 point intervals. (d11, d12)
- Gap 7 (belief compression zero-shot vs trained): PABU gains come from fine-tuning, no prompt-only arm seen; zero-shot compaction saves cost without raising solve rate. Open for belief-style compaction specifically. (d11, d13)
- Gap 9 (implementation variance): existence confirmed (DESPOT could not reproduce POMCP; TRPO seeds t=-9.09), no quantitative LLM-planner variance measure exists. (d16, d17)
- Gap 2 (commit threshold): the only data point is BSE, where the posterior with no stated threshold gave 1.45 listens (optimal rule needs about 2 net hearings) and 95% vs 80% success, CIs overlapping, N=40. No stated-rule vs no-rule arm anywhere. Stays mostly open. (d04)

STILL OPEN
- Gap 1: no study compares a code posterior with a free-text belief at equal tokens, N>=200. BSE skipped the free-text ablation (AB6) and RockSample; its NL-Tracker behaved identically to the no-belief baseline; BSE used 2.45x LLM calls. (d04-d06)
- Gap 3: no K sweep and no equal-token comparison against one long chain. Tru-POMDP only shows that structured 3x3 hypotheses beat a flat one-shot set. (d14, d15)

New claims added: K24-K27. Statuses changed: none downgraded; K17 stays contested; K02 now cites three sources and notes what is still unopened.
