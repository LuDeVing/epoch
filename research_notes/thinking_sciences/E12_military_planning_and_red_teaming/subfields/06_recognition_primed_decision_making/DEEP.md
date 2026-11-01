# Recognition-primed decision making: deep document

*Subfield E12.06. Written 2026-11-01 from evidence_a-d.jsonl, claims.jsonl (K01-K34) and critique.md in this folder. Evidence ids (a01 ... d18) and claim ids (K01 ... K34) point to those files. Status tags: [E] established (2+ independent sources), [S] single-source, [C] contested. Overlap with E04/01 (RPD and mental simulation) and E04/05 (conditions for valid intuition) is only linked, not repeated.*

## 1. What it is

Recognition-primed decision making (RPD) is Gary Klein's account of how experts decide under time pressure. The expert does not list options and score them. The expert reads the situation, sees it as a typical case, and recalls the action that fits. Then the expert checks that one action by mental simulation. If the simulation shows a flaw, the expert repairs it or moves to the next option. Options are handled one at a time (serial), not side by side (concurrent).

Three variants are usually listed (a30):

| Variant | Situation | What happens | Our reading |
|---|---|---|---|
| V1 simple match | Typical | Cues match a prototype, the known action follows ("if x then y") | Keep the first answer |
| V2 diagnose | Unfamiliar | The expert builds a picture first (feature matching or story building), then acts | Reopen the situation reading |
| V3 evaluate a course of action | Understood, but the action is untested | Simulate the action forward until it fits or breaks | Run a check on the first candidate |

Four parts of situation assessment come with a recognised pattern (a12): goals, relevant cues, expectancies, and a typical action. Expectancies matter most. A violated expectancy is the signal to leave the first option.

Why it matters for our agent: it is the human template for generate-test in keep-first mode. One candidate, one check, then next candidate only on failure. The skill sits in what gets generated first. A language model has no fire-ground experience, so it must get its first candidate from its own priors, and we must measure how good that candidate is.

Honest summary of the base: the human evidence is mostly interviews by one group on hand-picked hard cases (K01, K02). No controlled study shows the first option was the best one. The machine evidence (K16, K20, K32) supports a fast-first gate with a verifier. It does not test Klein's full loop. Direct LLM tests of RPD number one paper (Kopka and Feufel 2026, K14).

## 2. History and theories in depth

**Before RPD.** Classical decision theory said: list options, score them on attributes, pick the best (multi-attribute utility, decision analysis, elimination by aspects). The Klein team expected fire commanders to compare two options. This hypothesis was wrong (a15, b02).

**1985 founding study (a01-a07, a33).** Klein, Calderwood and Clinton-Cirocco, ARI Technical Report 796 (printed 2010 in J Cogn Eng Decis Mak).
- 26 fireground commanders (6 lieutenants, 4 captains, 16 chiefs), mean 23.2 years, range 12 to 37.
- 29 interviews of about 2 hours on 32 incidents (29 fires, 2 rescues, 1 gas leak), picked because they were command challenges or non-routine.
- 156 decision points, about 5 per incident (range 1 to 10).
- 127 of 156 (81%) fell in the prototype group. Only 28 had more than one option identified. Only 16 showed any relative evaluation. The abstract says under 12% had simultaneous comparison and over 80% were recognition.
- Table 4, as corrected in the cross-check: deliberated 18 (10 plus 8 at the pumping station), constructed 11, analog 3, prototype 124. The text's 127 equals prototype 124 plus analog 3. The groups are not additive to 156 as first listed.
- Time pressure (researcher-rated): 61% of points at level 3 or 4, 36% at level 2, 3% at level 1. Deliberated and constructed points had less time pressure.
- 3 of 156 points were mismatch events. Case 4: water on a house fire had no effect, it got hot and quiet, the commander pulled the crew out, and the floor collapsed a minute later (fire in the basement).
- Boundary case: the oil pumping-station fire (3 incidents, 22 points, almost a week). Local crews were not experts and decisions were deliberated in groups. The report says "roughly 59%" deliberated in the text, but its Table 4 gives 8 of 22 (36%). The report disagrees with itself.
- Method limits written by the authors: decision points were inferred by coders, coding took 3 to 7 hours per incident, no inter-coder statistic, interviewers probed for options a novice might consider.

**Serial option model.** The report's Fig. 1b: generate one option, implement or reject it, then the next. The authors say it fits better than the concurrent model (Fig. 1a). It was not tested against a rival model on the same data (a07).

**1990 expert versus novice (a08-a10).** Klein and Calderwood, ARI RN 90-59.
- 12 experts (mean 19.5 years) versus 12 novices (mean 10 years, under 2 as officer), six midwestern departments.
- 54% of decision points were situation assessment, 14% implementation or timing, 32% evaluating between options (14 points serial). Only 18% fit classical concurrent comparison.
- Experts constructed novel options more often, used imagery more, and were almost twice as likely to consider future contingencies. Both groups used recognition.
- Tank platoon trainees: limited deliberation and recognition-primed implementation about equally. Analogues helped about half the time. Trainees saw the same cues but misjudged their importance.
- Re-read of five studies, over 400 decision points, over 100 decision makers: 33 analogues detailed enough to analyse (about 8%). They served as flags more than templates.

**1990 military planning (a12-a14).** Klein, Thordsen and Calderwood. A 5-hour battalion planning session at Fort Hood had 27 decision points and 1 compared options. The authors warn where recognition fails: the commander lacks experience, cannot simulate the option to find pitfalls, or must optimise. Enemy course-of-action analysis needs worst-case thinking, where recognition can mislead. A planned controlled test with Army staff officers (Klein and Crandall 1990) hit practical barriers and was moved to MBA students. No controlled military test was done.

**1996 naval study (a17, b14).** Kaempf et al. in AEGIS combat information centers: recognition identified 95% of actions (74 actions), multiple options 4% (3 actions), novel 1%. 78% of recognition-generated actions were implemented without further evaluation. 87% of situation assessment was feature matching and 12% story building (via Reale 2023). Abstract and secondary report only.

**Extensions and formalisations.**
- Cohen, Freeman and Wolf 1996, metarecognition: add a critique layer that checks the situation model for incompleteness, conflict and unreliability, and decide whether more thought is worth it (a31, abstract only).
- Take-the-first heuristic (Johnson and Raab 2003; Raab and Gigerenzer 2015): search options in order of validity, stop after 2 to 3, choose the first. It predicts more options means worse choices (b17).
- Recognition Planning Model (Schmitt and Klein; Ross et al. 2004): one base course of action, wargame it, drop the compare-three-COAs step. A pre-mortem was added in practice (a19).
- Computational models: MoCog1 (Gevarter 1991), single-pass match-and-act only (a35); R-CAST agent with expectancy monitoring (Fan et al. 2005, b07-b08); Kunde and Darken 2006 simulation architecture for combat entities (a36); Patterson et al. 2009 system dynamics model (a34); Mueller and Thanasuan 2014 crossword model (a37). Danial et al. 2019 survey of RPD for artificial agents is in E04 (c18, not reopened).
- Rival formal model: the decision ladder of cognitive work analysis, whose shortcut paths mirror keep-first (a39, abstract level).

**2009 Kahneman and Klein, "A failure to disagree" (a15, a16, b01-b06).** The main author and the main critic agree on the conditions: trust a recognised option only where the environment is high-validity (stable cues) and the person has had enough practice with feedback. There is no subjective marker that separates a skilled intuition from a heuristic one. Expertise is fractionated: the same profession is good at some tasks and poor at others (Shanteau 1992). Statistical rules tie or beat clinicians in most reviewed studies (algorithms better in 63, tie in 65, clinicians better in 8; counts read from a garbled PDF).

**Where the theory is still weak.** Lipshitz, Klein, Orasanu and Salas 2001 name the scarcity of rigorous empirical work and the unconfirmed prescriptive value of NDM models as open problems (a32). Reale et al. 2023 found RPD phases are not strictly sequential in 11 studies (b15).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Fireground commanders mostly used recognition | 127 of 156 points (81%); 28 had >1 option; 16 had relative evaluation; <12% simultaneous comparison | Klein, Calderwood, Clinton-Cirocco 1985 (a01, a02, a33) | [S] (one data set; later "80 to 90%" is rounding up, a29) |
| Time pressure was high | 61% of points at level 3-4, 36% level 2, 3% level 1 (researcher-rated) | same (a03) | [S] |
| Mismatch triggers reassessment | 3 of 156 points were mismatch events | same (a04) | [S] |
| Pumping-station fire was mostly deliberated, in groups | 59% by text, 36% (8 of 22) by Table 4 | same (a05) | [S], report inconsistent |
| Experts and novices both recognise; experts build more novel options | 12 vs 12; 18% classical concurrent comparison; experts ~2x more contingency thinking | Klein and Calderwood 1990 (a08) | [E] (with K05 sources) |
| Analogues are rare and a coin flip | 33 of 400+ points (~8%); helped about half the time | Klein and Calderwood 1990 (a09, a10) | [S] |
| Naval officers: recognition dominates | 95% recognitional (74), 4% multiple options (3), 1% novel; 78% implemented without evaluation | Kaempf et al. 1996 via Reale 2023 (a17, a18, b14) | [E] across domains (K03); figure itself abstract/secondary |
| Systematic review of 32 high-risk studies | RPD found in all studies that looked at strategy; surgeons single option 6/12 and 11/24 | Reale et al. 2023 (a18, b13) | [E] |
| Sport: simple match share | 60 to 81% simple match, 13 to 28% diagnosis, 3 to 24% evaluate; ~80% first-option choice | Macquet 2020 via Bossard 2022 (a27, b24) | [S] second-hand, no primary N |
| Army RPM saves planning time | >=30% (participant estimate); ~20% faster tempo, bolder plans (Swedish division study) | Ross et al. 2004 (a19) | [S], developers, self-estimated |
| Grandmasters blunder more in blitz | 20 GMs, blunder proportion t(19)=6.54, d=1.39; size t(19)=4.23, d=0.96; worse for 18 of 20; Study 2: 11 title matches, 7 champions | Vidulich and Tsang 2026 (a21) | [C] against strong RPD reading |
| Classic chess intuition evidence is thin | 3 masters vs 3 class B, 24 games; blitz explains 64 to 81% of slow rank; first mentioned move kept 45% overall, 22/25% hard, 73/50% easy; final moves better than first | Calderwood 1988; Burns 2004; Moxley 2012 (a11, a22) | [C] |
| Take-the-first in sport: order effect holds, other claims did not | N=72; heuristic used on 70% of trials; earlier options better; no effect on consistency or confidence | Hepler and Feltz 2012 (b18); Johnson and Raab 2003 | [C] |
| Statistical rules tie or beat experts | algorithms better in 63, tie 65, clinicians better in 8 | Kahneman and Klein 2009 (b05) | [E] |
| RPD prompt raises LLM triage accuracy | 63.3 to 67.6% (OR 2.26, z=8.69); data-frame prompt 66.7% (OR 2.05); 10 ChatGPT models, 45 vignettes, 13,500 assessments | Kopka and Feufel 2026 (a23, b09) | [S] |
| ...gain is in self-care cases and absent for GPT-5.2 | self-care 13.4 to 29.8%; GPT-5.2 self-care 0 to 3.1% under all prompts; Instant 57.8 vs 56.4, Thinking 52.0 vs 53.1; accuracy up in 18 of 45 cases, down in 13; kappa 0.766 to 0.717; correct at least once 73.1 to 82.2% | same (a24, a25, b10-b12, d01, d02) | [S] |
| CoT hurts pattern tasks | GPT-4o implicit statistical learning 87.5 to 64.4 (-23.1, p<.0001); face recognition 64.0 to 51.2; 36.3-point gap is o1-preview 57.7 vs GPT-4o direct 94.0, two models | Liu et al. 2025 (c04) | [E] with Sprague, Ma |
| CoT helps mainly symbolic tasks | >100 papers; 20 datasets, 14 models; commonsense ~no gain | Sprague et al. 2025 (c06) | [E] |
| NoThinking beats Thinking at low budgets | AMC23 at 700 tokens 51.3 vs 28.9; below ~3000 tokens NoThinking better at every k; parallel best-of-N matches Thinking at up to 9x lower latency | Ma et al. 2025 (c07, c25) | [E] when a selector exists |
| Recognition-only chess network | 270M: puzzles 95.4%, blitz Elo 2895 vs humans, 2299 vs bots; 136M 94.5; 9M 88.9; 15.3B action values; AlphaZero policy 56.1 vs 95.6 with 400 MCTS; Leela 88.6 policy vs 99.6 with MCTS | Ruoss et al. 2024 (c01, c02) | [E] |
| Look-ahead inside a policy net | probe predicts best move 2 turns ahead at 92% | Jenner et al. 2024 (c03) | [S] |
| Learned gates save thinking | Thinkless -50 to -90% long chains; Dualformer maze: slow 97.6% optimal, fast 80% vs 30% solution-only, auto 96.6% with 59.9% fewer steps | c08, c09 | [E] (trained, not prompt-only) |
| Training-free draft-agreement gate | 13 of 14 pairs matched or beat always-think; thinking tokens -32 to -73%; Qwen3-8B MATH-500 88.2 vs 85.6; stage 1 answers 78 to 82% of queries | DART 2026 (d03) | [S] |
| Self-asked gates are weak | MC-Binary 85.8 (4% saved), HumanEval 10.4; MC-Conf 85.8 (24% saved), OlympiadBench 54.9 vs always-think 71.5 | DART Table 2; Guo 2026 (d04, d06) | [E] |
| Same-model check does not protect answers | GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-3.5 CommonSenseQA 75.8 to 38.1; self-critic passed 38 of 45 invalid plans; GPT-4 plans 40/100 alone, 55/100 with LLM verifier, 88/100 with external VAL | Huang 2024; Valmeekam 2023 (d07, d08) | [E] |
| First-attempt plan validity varies widely | Blocksworld, 600 zero-shot: GPT-4o-mini 8.8%, GPT-4 34.6, GPT-4o 35.5, Claude 3.5 Sonnet 54.8, Llama 3.1 405B 62.6, o1-mini 56.6, o1-preview 97.8 | Valmeekam 2024 (d09) | [E] (K25) |
| Simulating candidates beats re-ranking | WebDreamer VWA 23.6 vs reactive 17.6; ablation (read from chart) reactive 21.1, rerank 22.8, full 29.8 | Gu et al. 2025 (d10) | [S] |
| List position bias flips with option quality | GPT-4o-mini first-choice 98% (Ideal) vs 21% (Harsh); reorder of multiple-choice options moves accuracy 13 to 75% | Yin 2025; Pezeshkpour 2024 (d11, d12) | [E] |
| Early finish is competitive on verifiable tasks | shortest chain beats random by up to 18.8, longest by up to 34.5; short-1@k matches majority vote with up to 40% fewer thinking tokens | Hassid et al. 2025 (d13) | [E] with d16 |
| Adaptive stopping on agreement | sample budget cut up to 7.9x with <0.1% accuracy loss; 17 datasets, 3 LLMs | Aggarwal et al. 2023 (d16) | [S] |
| Complexity moderates first-solution value | >92% of correct responses had the correct answer in first round (conditional); o1-like used 1,953% more tokens on 2+3; Tower of Hanoi N<=4 accuracy falls along trace, N>=8 collapse | Chen 2025; Shojaee 2025 (d14, d15) | [E] |
| LLM wargames escalate | 5 models x 3 scenarios x 10 runs; GPT-3.5 10.15 to 26.02 (+256%, text claim, scenario label uncertain); 214 experts vs LLM teams: no significant difference on about half the actions; persona (pacifist vs aggressive) no effect | Rivera 2024; Lamparth 2024 (c13, c14) | [E] (K23) |
| Pharmacists switch to analysis when something does not fit | 12 pharmacists, 3 simulated prescriptions each | 2025 study (a38) | [S] |
| Code review maps to RPD | 10 developers, 34 reviews, 1159 segments | Heander et al. 2025 (a26, c17) | [S] qualitative |

## 4. Mechanisms and models

An engineer can read RPD as a control loop with five parts. Each part has a human version and an agent version.

**4.1 Situation assessment (what to build first).**
Human: match cues to a prototype. A prototype holds four items: goals, relevant cues, expectancies, typical action(s) in a queue (a04, a12).
Agent: represent a case as {goal, cues, expectancies, ordered action queue}. Fill it by retrieval from a verified case library (nearest cases) or from the model's own prior. Store expectancies as checkable statements ("after action X we should see Y").

**4.2 Typicality gate (V1 versus V2).**
Human: familiar cues give a simple match; mismatch or unfamiliarity sends the expert to diagnosis.
Agent options, from weakest to strongest evidence:
- Self-report ("is this typical?") is weak (d04, d06, K28). Do not use alone.
- Draft agreement: sample 2 cheap no-think drafts, keep if they agree, think otherwise (DART, d03). Training-free. 78 to 82% of queries answered at stage 1. Failure mode: drafts agree on a wrong answer (36 of 59 MATH-500 errors). Invalid on multiple choice.
- Candidate dispersion before generation (Guo 2026, d06).
- Retrieval similarity to stored solved cases (not yet tested for LLMs).
- Trained gates: Thinkless (RL, decoupled GRPO) and Dualformer (random trace dropping) (c08, c09). Need training.
- Entropy-triggered escalation (speculative try-then-verify) pays most on code at extra token cost (d05).
- No strategy wins at every model scale (HRBench, 527 runs): prompt-based leads at 9B and 1.1T, speculative at 20B and 671B, all equal at 2B (d05).

**4.3 Generate one candidate (serial).**
Human: first option is usually workable for experts (Johnson and Raab: later options worse; Moxley: easy positions kept first move 73 and 50%). Agent: first-attempt validity is model- and task-specific (8.8% to 97.8% on Blocksworld, d09). The rate must be measured before keep-first is enabled.

**4.4 Mental simulation (V3 check).**
Human: run the option forward in imagination, up to about three variables (Klein 1999 via a36), look for pitfalls. Often skipped in practice (a18).
Agent: three kinds of check, ordered by evidence.
- Same-model re-read or "simulate it" in prose: does not help and often hurts, and approves 38 of 45 bad plans (d07, d08, K26).
- External check: code execution, a rule validator, a symbolic solver, held-out test. GPT-4 plans rose from 40% to 88% with an external verifier (d08). Tools beat CoT on symbolic execution (c24).
- Learned or LLM world-model simulation of each candidate: beat re-ranking in WebDreamer (d10), and Kunde and Darken show small predictors plus a coded decision rule (a36).
The check must carry outside information. This is the main way the agent differs from the human expert, whose simulation draws on real world knowledge.

**4.5 Expectancy monitor and drop trigger.**
Human: a violated expectancy sends the expert back to diagnosis. Only 3 of 156 points were mismatch events, so the trigger is rare. System dynamics model (a34): diagnosis took about 8 s from a cold start but about 16 s when the situation first looked typical and expectations were then violated, so the first match primes and slows the switch (anchoring).
Agent: write expectancies when choosing the action. After acting, code compares output to expectancies. Violation routes to V2 (re-diagnose from the actual surprise). R-CAST did this (b07-b08). For sampled answers, adaptive-consistency stops sampling when the leader is clearly ahead (up to 7.9x saving, <0.1% loss, d16). Plan-level triggers are untested.

**4.6 Fallback modes.**
About 19% of fireground points (28 deliberated or constructed plus mismatches) needed another mode (a02). Surgery shows about half single-option (a18). The agent needs a compare-N path and a construct path.

**4.7 Pseudocode.**
```
case = assess(task)                      # goal, cues, expectancies, action queue
if not typical(case):                    # agreement / retrieval / measured first-option rate
    return diagnose_then_compare(case)   # V2, compare-N path
for action in case.queue:                # serial
    result = external_check(action)      # code/tool/test, not same-model prose
    if result.passes and not violates(result, case.expectancies):
        return action                    # V1/V3 exit
    case = reassess(case, result)        # revise only from real output
return best_so_far                       # never abstain
```

## 5. What holds up

**Replications.**
- Recognition as the commonest reported strategy: [E]. Naval (95%), surgery (~half), a 32-study review (every study that looked), sport reviews (60 to 81%), pharmacists, code review, military planning (K03, a18, a38, a26). Caveat: all use the same retrospective, coder-inferred style, and the original share depends on how a "decision point" is coded. Klein and Calderwood 1990 found only 18% classical concurrent comparison but 32% involved evaluating options, so "no comparison" depends on coding (critique).
- Option-order effect (earlier options better): replicated by Hepler and Feltz (N=72, 70% heuristic use) [partial]. Consistency and confidence predictions failed (b18).
- Eleven studies found phases not strictly sequential (b15).

**Failures and contested results.**
- Calderwood 1988 chess (3 vs 3) is too small to carry the claim (a11, a22).
- Grandmasters made more and bigger blunders under blitz (d=1.39, 18 of 20 worse), and Chabris and Hearst 2003 and Moxley 2012 agree that deliberation helps on hard positions (a21, a22). This does not refute RPD, because blitz restricts search as well as recognition. It refutes the strong "fast expert intuition is as good" reading.
- Sport: the intuitive-to-analytical continuum evidence is inconsistent (b24).
- Kopka RPD prompt: +4.3 points, but the data-frame prompt gave +3.4 and the two did not differ significantly; no length-matched control; no gain for GPT-5.2 (floor effect in self-care, 0 to 3.1%); gain concentrated in one answer class where the models were over-cautious; 13 of 45 cases got worse (K14, K15, d01, d02).
- Army RPM time savings are participant estimates by the model's developers (a19).

**Moderators that hold.**
- Validity of the environment and practice with feedback (Kahneman and Klein 2009) [E].
- Time available: more time gives more options and more analysis (sport reviews b16, a27; fireground deliberated points had less time pressure, a03). Two reviewed studies found self-reported time pressure had no significant effect on strategy (a18).
- Typicality and task complexity: easy items keep the first answer (Moxley; Chen >92%; Shojaee low regime); hard items fixate on early wrong attempts (d14, K30).
- Group and expertise: the pumping-station fire, novices, and group decisions deliberate more (a05, a08).
- Stress pushes people toward intuition whether or not it fits (b22).

**What worked as interventions.**
- Pre-mortem added to single-COA planning (a19, anecdotal).
- External verifier on plans (40% to 88%, d08).
- Agreement-based routing and stopping (d03, d16).
- Selector on top of many fast tries (Ma, c25).
- Structured NDM prompt on ambiguous triage (+3.4 to +4.3, K14).

**What did not work.**
- Generic analytic-process training in the military (decision analysis, Bayes) "was not very successful" (a13), though no RPD training replaced it in a test.
- Same-model self-correction and self-critique without outside feedback (d07, d08).
- Asking the model whether it needs to think (d04, d06).
- Persona prompts to steer wargame behaviour (c13).
- Chain-of-thought on pattern tasks (c04, c05).

## 6. Language models

**Direct tests of RPD.** One: Kopka and Feufel 2026 (a23-a25, b09-b12, d01-d02). The prompt: recall a typical case, state the usual decision, simulate it, modify if it fails, otherwise reassess until familiar. Result: 63.3 to 67.6% (OR 2.26), with the data-frame prompt at 66.7%. Larger gain for reasoning models (OR 2.15). Self-care accuracy 13.4 to 29.8%; GPT-4.1 self-care 0 to 43.8%. No gain for GPT-5.2. Correct-at-least-once 73.1 to 82.2%, but modal-answer share fell 76.9 to 66.9% (not significant). A preprint reported 70.2 vs 64.7%, so numbers moved between versions. Read: a structured think-first prompt corrects an over-caution bias on an uncertain task. It is not proof of RPD.

**Nothing found** that tests an LLM on Klein's fireground paradigm, scores first options against expert commanders, or measures how often a model's first option is workable on RPD-type cases (K24). Closest: first-attempt plan validity on Blocksworld, 8.8% to 97.8% (K25).

**Fast-first versus slow, by task type.**
- Pattern-like tasks: CoT hurts. GPT-4o 87.5 to 64.4 on implicit statistical learning; 8 other models also dropped; face recognition all 6 VLMs worse (GPT-4o 64.0 to 51.2); exception learning needed over 4x the passes, up to 331% more (c04, c05). Three of six task types did not show drops.
- Commonsense and language understanding: CoT about equal to direct (Sprague, c06).
- Symbolic and math: CoT helps, tools help more.
- Low token budgets: NoThinking 51.3 vs Thinking 28.9 at 700 tokens; at about 3500 tokens Thinking is better at pass@1 but NoThinking passes it from k=2 (c07). Needs a selector.
- Easy items: more than 92% of correct responses already had the right answer in the first round (conditional figure); o1-like models used 1,953% more tokens on 2+3 (d15).
- Hard items: models fixate on early wrong attempts and effort drops (d14).

**Gates.** Trained: Thinkless cut long-chain use 50 to 90%; Dualformer auto mode 96.6% optimal with 59.9% fewer steps. Training-free: draft agreement matches or beats always-think with 32 to 73% fewer thinking tokens. Self-asked gates fail. No head-to-head of DART against Thinkless exists. Best gate depends on model scale (d05).

**Checks.** Same-model checks hurt or do nothing (GPT-4 GSM8K 95.5 to 89.0; CommonSenseQA GPT-3.5 75.8 to 38.1; self-critic false-positive rate 84.45%). External verifiers help most (40 to 88). These models are 2023 vintage. Reasoning models trained with RL were not tested in these papers.

**Early finish.** Shortest chain beat random by up to 18.8 points and longest by up to 34.5; stopping at the first finishers matched majority vote at up to 40% fewer thinking tokens (d13). On verifiable math and code only.

**Position effects.** First-listed option favoured when options are good, last when poor (GPT-4o-mini 98 vs 21%; Claude 4 Sonnet 91 vs 2). Multiple-choice reordering shifts accuracy 13 to 75%. At T=0 the bias hides. No study measures option quality by generation order, and no reasoning model was tested (d11, d12).

**Wargames and roles.** All five LLMs escalated (GPT-3.5 10.15 to 26.02); LLM teams differ from 214 experts on about half the actions; persona prompts did nothing (c13, c14). A model playing a commander is not a model of an expert commander. Early GPT-3 gave the intuitive wrong answer on all 3 CRT items (c12).

**Architectures.** DPT-Agent (fast rule layer plus slow LLM layer) scored highest on both maps in a human test with 68 valid trials (c11). Talker-Reasoner reports no numbers (c10). Both have latency as the point. R-CAST (non-LLM) held up under time pressure with expectancy monitoring (6 teams vs 6; p<0.001 for enemy destroyed; supply delivery p=0.211) (b07).

**Machine recognition at scale.** A 270M searchless chess transformer reached puzzles 95.4% and Elo 2895 vs humans (2299 vs bots) but needed 15.3B action values; search still adds margin in other systems (AlphaZero 56.1 policy vs 95.6 with 400 MCTS; Leela 88.6 vs 99.6). Policy networks hold implicit look-ahead (92% probe accuracy 2 plies ahead) (c01-c03, d17).

## 7. What our agent should take

Schema parts: G guardrails (G1-G12), S states (S0 gate, S1 understand, S3 generate, S4 test, S7 select, S8 verify), O operators (O1-O8), memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Do not use stated confidence to skip checking. Trust in the first option depends on environment validity and practice, not on feeling. Gate on task type and measured hit rate. | G1, S0 | [E] | K06; a16, b01, b03, b04 |
| 2 | Keep-first mode is on only where a cheap external test exists or the task is pattern-like. Otherwise take the slow path. | S0 gate, G12 | [E] | K16, K17; c04, c06, c07, c21, c25 |
| 3 | The check on the first option must carry outside information (code, tool, validator, held-out case). A same-model re-read or "simulate it" in prose is not a check. | S4, G2, G3, G10 | [E] | K26; d07, d08, c24 |
| 4 | Do not use self-report ("does this need thinking?") as the gate. Use observed signals: agreement of cheap drafts, retrieval similarity, measured first-option rate. | S0 | [E] for the negative | K28; d04, d06 |
| 5 | Revise or drop the first option only on a signal: a failed external check or a violated written expectancy. Revision must cite the failing output. | G1, G2, O (expectancy monitor) | [E] | K09; a04, b07, b08, a38 |
| 6 | Measure the first-option workable rate per model and per task family before enabling keep-first. It ranged 8.8% to 97.8% on one domain. | S0 input, G7 | [E] | K25; d09, d08 |
| 7 | Keep a fallback path. About 1 in 5 fireground points, and about half of surgical decisions, needed a different mode. Unfamiliar, group or slow problems go to diagnose and compare. | S0 router, S3 | [E] | K03, K04; a02, a05, a18 |
| 8 | Do not trust list position. Shuffle options when selecting among them; code selects. | G5 | [E] | K31; d11, d12 |
| 9 | Spend by difficulty. Easy items keep the first answer; hard items need budget and fixate on early wrong attempts. Cap reasoning on easy items. | G11, G12 | [E] | K30; d14, d15 |
| 10 | Put checking effort on the situation reading (what kind of case is this), not on a list of rival answers. Experts differ in what they think about, not whether they think. | S1, S2 | [E] | K05; a08, b14 |
| 11 | Prefer an explicit rule or scorer to recognition in low-validity tasks. | G, S4 | [E] | K07; b05, b06, a16 |
| 12 | On military-style tasks, first plans may be biased (escalatory). Add a red-team check on the first plan, and do not rely on persona prompts. | G (red-team check) | [E] | K23; c13, c14 |
| 13 | Samples that stop early on agreement save tokens at near-zero loss on verifiable tasks. Agreement is a hint, not proof. | G4, S3 | [E]/[S] (first-finish d13; agreement stopping d16 single-source) | K32; d13, d16 |
| 14 | Seed any case library only with verified cases. Wrong patterns are sticky. Retrieved analogues help about half the time, so each needs a check. | memory | [S] | a09, a10, b23 |

Do not quote 81% or "80 to 90%" as a prior for the agent (K02). Mark RPD numbers [S] in the schema.

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Keep-first-then-check versus generate-N-and-compare at equal tokens, on tasks with a cheap external check. | S3/S4/S7 | [S] | K24, K32; d13, c07, K25 |
| T2 | Prompt-only typicality gate by draft agreement for free-text planning and diagnosis tasks. | S0 | [S] | K27; d03, d04 |
| T3 | Written expectancies plus a violation check, against plain generate-test. | O expectancy monitor | [S] (humans [E], LLM untested) | K09; a04, b07 |
| T4 | RPD-style prompt (typical case, usual action, simulate, modify) versus a different structured prompt versus a length-matched neutral prompt. | S1/S3 | [S] | K14, K15; d02 |
| T5 | Single-COA plus pre-mortem versus three-COA comparison on planning cases, blind-scored. | S planning | [S] | K13; a19 |
| T6 | Option quality by generation order, reasoning and non-reasoning models. | O option budget | [C] (humans mixed, LLM untested) | K12, K31 |
| T7 | Token cap and blunder rate. | G11/G12 | [C] | K10, K11; a21 |
| T8 | Case memory size versus keep-first accuracy. | memory | [S] | K33; d17 |
| T9 | Red-team best-reply search with and without keep-first. | G, S3 | untested | K34; a13 |

## 8. Concrete tests on our bench

All arms use equal total tokens, counting setup, retrieval and checks (G7). Report mean with a paired interval over items, and run 3 seeds. Expected effects are guesses from the cited evidence, not findings.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 keep-first vs compare-N | Planning or diagnosis items with an automatic validator (Blocksworld-like, code-with-tests, 100 cases per model) | A: one candidate, external check, next candidate on fail (budget cap). B: N candidates at the same token total, external selector. C: one long chain | Accuracy at fixed tokens; mean tokens to first valid | A >= B on easy and typical items; B wins on hard items. Crossover found by the gate (K05, K30) |
| T1b first-option rate | Same set, first sample only | Per model | % first option valid | Reproduces the 9% to 98% spread; sets the gate threshold (K25) |
| T2 gate | Mixed easy/hard free-text items (100 to 200) | A: always think. B: draft-agreement gate. C: self-report gate. D: retrieval-similarity gate | Accuracy vs tokens (Pareto) | B >= A at 30 to 70% fewer thinking tokens; C no better than A (K27, K28). Watch false-accept rate |
| T3 expectancy monitor | Multi-step tasks where a step can silently fail (tool tasks, ARC-style) | A: plain generate-test. B: model writes expectancies, code checks them, violations trigger re-diagnose | Steps to detect failure; final accuracy | B detects earlier, small accuracy gain (K09) |
| T4 prompt ablation | Ambiguous triage or classification items (45+ vignettes plus a second task) | Default; RPD prompt; data-frame prompt; length-matched "think step by step" neutral prompt. Two model families | Accuracy; at-least-once; answer-class shift | RPD ~ data-frame ~ neutral on new models; gain only where there is an answer bias (K15, d01) |
| T5 single-COA | Military-style planning items with a blind rater and a simulator or red-team scorer | A: one COA + pre-mortem. B: 3 COAs + compare, same tokens | Blind-rated plan quality; failures found by an adversary | A equal to B in typical scenarios; B better in novel ones (K13) |
| T6 order | Open-ended option generation (5 options in one pass), validator per option | Reasoning vs non-reasoning model | Score against generation index (slope) | Weak negative slope for non-reasoning; flatter for reasoning (K12, K31) |
| T7 token cap | Chess puzzles or planning items with an exact oracle | Cap 1x, 2x, 4x, uncapped | Blunder rate and size | Blunder rate rises as cap falls on hard items, not on easy ones (K10) |
| T8 case memory | Task family with solved cases, retrieved as first option | 0, 10, 100, 1000 cases | Keep-first accuracy; retrieval hit rate | Rising, then flat; locate the elbow (K33) |
| T9 red-team | Seeded scenarios with a known adversary best reply (atypical by design) | A: keep-first. B: forced generation of adversary replies (compare-N) | % best replies found | B > A (K34, a13) |
| T10 same-model vs external check | Items with tool-checkable answers | Keep-first alone; + same-model check; + tool check | Accuracy at equal tokens | Same-model check <= alone; tool check > both (K26). Retest on current reasoning models |

## 9. What does not transfer, and why

- **Expertise and 10 to 20 years of feedback.** The fireground effect rests on experienced commanders. A prompt-only agent has no such practice. Gains from training (Thinkless, Dualformer, 15.3B chess labels) do not follow from a prompt (K18, K33).
- **Real-world mental models.** The human simulation uses knowledge of fire and buildings. The same-model LLM check has no new information and fails (d07, d08).
- **The 81% figure.** It is one interview data set, retrospective and coder-inferred, hand-picked hard cases. It says what experts reported, not that the first option was best (K02).
- **Stress and time pressure.** The human setting involves threatened life. LLM budget pressure is different. The stress literature says stress pushes people into intuition whether or not it fits (b22), so budget pressure must not silently turn off checking.
- **Interview-era "decision points".** Text agents have explicit steps. The coding rules do not carry over, and the choice of unit changes the share.
- **Machine fast-versus-slow results.** They are about modes (Sprague, Liu, Ma, Dualformer, Thinkless), not Klein's serial generate-and-simulate loop. They support a gate, not the full procedure (critique).
- **Chess results.** An exact oracle and closed rules. Open military problems have neither (c01, a21).
- **Wargame LLM papers.** They test escalation, not recognition. Role and persona prompts did not make models behave like expert commanders (c13, c14).
- **Take-the-first from sport.** Video tasks with students and athletes. The order effect for an LLM's own generation is untested; presentation order effects flip with quality (d11).
- **Army RPM numbers.** Self-estimated time savings from developers (a19).
- **Red teaming.** An adversary's best reply is atypical by design. Recognition is weakest there, and the founders say worst-case analysis is where recognition can mislead (a13). Keep-first should be off for adversary-search steps.

## 10. Open questions

1. At equal tokens, does keep-first-then-simulate beat generate-N-and-compare on tasks with expert-labelled workable options? No study measures a model's first-option workable rate against experts (K24).
2. Which cue says "typical enough to keep the first option"? Draft agreement is training-free and works on math and code. Does it work for free-text plans, and how does it compare with Thinkless and Dualformer?
3. Is the simulate step what protects RPD? No ablation exists in humans or in a keep-first LLM agent.
4. Does the Kopka gain hold on a second task, a non-OpenAI model, and against a length-matched neutral prompt?
5. Does option quality fall with generation order in LLMs, and does it differ for reasoning models?
6. What drop trigger works at plan level, and how fast? Only 3 of 156 mismatch events occurred in the founding data; a rare-event trigger differs from a vote.
7. Does the grandmaster blitz result transfer: is the harm from less search or less verification?
8. Does the Army single-COA plus pre-mortem method beat three-COA comparison on a blind-scored outcome?
9. Does keep-first weaken adversary best-reply search in red teaming?
10. How many cases must memory hold before retrieval replaces search?
11. Does the 2023 finding that self-checks fail hold for current RL-trained reasoning models?
12. Is the draft-agreement false-accept problem (36 of 59 errors) worse on atypical cases that look typical, which is the RPD failure itself?

Items 7, 8 and 9 were left open by a blocked search (quota and 429 errors). They are limits of the search, not evidence that no study exists.

## 11. Sources

[V] = opened and read this session. [M] = abstract, snippet or second-hand only.

Human and founding studies
- [V] Klein, Calderwood, Clinton-Cirocco 1985, Rapid Decision Making on the Fire Ground, ARI TR 796. https://archive.org/details/DTIC_ADA199492 (a01-a07)
- [M] Klein et al. 2010 print version, J Cogn Eng Decis Mak. https://doi.org/10.1518/155534310X12844000801203 (a33)
- [V] Klein and Calderwood 1990, Investigations of NDM and the RPD model, ARI RN 90-59. https://archive.org/details/DTIC_ADA226006 (a08-a11)
- [V] Klein, Thordsen, Calderwood 1990, Descriptive Models of Military Decision Making. https://archive.org/details/DTIC_ADA226884 (a12, a13)
- [V] Klein and Crandall 1990, RPD Strategies: First-Year Interim Report. https://archive.org/details/DTIC_ADA226887 (a14)
- [V] Kahneman and Klein 2009, Conditions for Intuitive Expertise. https://www.gwern.net/doc/psychology/cognitive-bias/2009-kahneman.pdf ; https://doi.org/10.1037/a0016755 (a15, a16, b01-b06)
- [M] Kaempf, Klein, Thordsen, Wolf 1996, Human Factors. https://doi.org/10.1177/001872089606380204 (a17)
- [V] Reale et al. 2023, Decision-Making During High-Risk Events (systematic review). https://pmc.ncbi.nlm.nih.gov/articles/PMC10564111/ (a18, b13-b15)
- [V] Ross, Klein, Thunholm, Schmitt, Baxter 2004, Military Review. https://archive.org/details/DTIC_ADA521492 (a19, a20)
- [V] Vidulich and Tsang 2026, Cognitive Research 11:35. https://pmc.ncbi.nlm.nih.gov/articles/PMC13100097/ (a21, a22)
- [V] Bossard et al. 2022, NDM in sport. https://pmc.ncbi.nlm.nih.gov/articles/PMC9252097/ (a27, b24)
- [V] Ashford, Abraham, Poolton 2021, Sports 9(5):65. https://pmc.ncbi.nlm.nih.gov/articles/PMC8156213/ (a28, b16)
- [V] Macrocognition: From Theory to Toolbox 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC4731510/ (a29)
- [V] Wikipedia, Recognition primed decision, and clinical reasoning review PMC6900348. https://en.wikipedia.org/wiki/Recognition_primed_decision (a30, b26)
- [M] Cohen, Freeman, Wolf 1996. https://doi.org/10.1177/001872089606380203 (a31)
- [M] Lipshitz, Klein, Orasanu, Salas 2001. https://doi.org/10.1002/bdm.381 (a32)
- [V] Patterson et al. 2009, System dynamics of RPD. https://archive.org/details/DTIC_ADA518391 (a34)
- [V] Gevarter 1991, MoCog1, NASA TM-103868. https://archive.org/details/NASA_NTRS_Archive_19930020197 (a35)
- [V] Kunde and Darken 2006. https://archive.org/details/DTIC_ADA575044 (a36)
- [V] Mueller and Thanasuan 2014, crossword expertise. https://pmc.ncbi.nlm.nih.gov/articles/PMC4161049/ (a37)
- [V] Community pharmacists' decision-making, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC11833647/ (a38)
- [V] Naikar 2010, decision ladder vs RPD (abstract and summary). https://archive.org/details/DTIC_ADA523330 (a39)
- [V] Raab and Gigerenzer 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4625029/ (b17)
- [M] Hepler and Feltz 2012 (abstract only). https://doi.org/10.1037/a0027807 (b18)
- [M] Raab and Johnson 2007 (abstract only). https://doi.org/10.1037/1076-898x.13.3.158 (b19)
- [M] Raab and Laborde 2011 (abstract only). https://doi.org/10.1080/02701367.2011.10599725 (b20)
- [M] Flin et al. 2007 (abstract only). https://doi.org/10.1136/qshc.2006.020743 (b21)
- [V] Yu 2016, SIDI stress model. https://pmc.ncbi.nlm.nih.gov/articles/PMC5146206/ (b22)
- [V] Police training review 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6692711/ (b23)
- [M] Fire Engineering trade article. https://www.fireengineering.com/firefighting/fireground-command-decisions/ (b25)
- [M] Klein, Wolf, Militello, Zsambok 1995. https://doi.org/10.1006/obhd.1995.1056 (b28)
- [M] Johnson and Raab 2003. https://doi.org/10.1016/S0749-5978(03)00027-X (b29)
- [V] Fan, Sun, McNeese, Yen 2005, R-CAST. https://cs.huji.ac.il/course/2005/aisemin/articles2006/docs/pa7e4_945.pdf (b07, b08)

LLM and AI studies
- [V] Kopka and Feufel 2026, JMIR Biomed Eng 11:e88053. https://pmc.ncbi.nlm.nih.gov/articles/PMC13061108/ ; https://biomedeng.jmir.org/2026/1/e88053 (a23-a25, b09-b12, d01, d02)
- [V] Heander, Soderberg, Rydenfalt 2025, Code Review as Decision-Making. https://arxiv.org/abs/2507.09637 (a26, c17)
- [V] Ruoss et al. 2024, Amortized Planning with Large-Scale Transformers. https://arxiv.org/abs/2402.04494 (c01, c02, d17)
- [V] Jenner et al. 2024, learned look-ahead in chess. https://arxiv.org/abs/2406.00877 (c03)
- [V] Liu et al. 2025, Mind Your Step (by Step). https://arxiv.org/abs/2410.21333 (c04, c05)
- [V] Sprague et al. 2025, To CoT or not to CoT. https://arxiv.org/abs/2409.12183 (c06, c24)
- [V] Ma et al. 2025, Reasoning Models Can Be Effective Without Thinking. https://arxiv.org/abs/2504.09858 (c07, c25)
- [V] Fang, Ma, Wang 2025, Thinkless. https://arxiv.org/abs/2505.13379 (c08)
- [V] Su et al. 2025, Dualformer. https://arxiv.org/abs/2410.09918 (c09)
- [V] Christakopoulou et al. 2024, Talker-Reasoner. https://arxiv.org/abs/2410.08328 (c10)
- [V] Zhang et al. 2025, DPT-Agent. https://arxiv.org/abs/2502.11882 (c11)
- [V] Binz and Schulz 2023, GPT-3 cognitive psychology. https://arxiv.org/abs/2206.14576 (c12)
- [V] Lamparth et al. 2024, Human vs. Machine wargames. https://arxiv.org/abs/2403.03407 (c13)
- [V] Rivera et al. 2024, Escalation Risks. https://arxiv.org/abs/2401.03408 (c14)
- [V] Hogan and Brennen 2024, Open-Ended Wargames with LLMs. https://arxiv.org/abs/2404.11446 (c15)
- [V] Mainali et al. 2025, Classical AI vs LLMs for decision-maker alignment. https://arxiv.org/abs/2510.06093 (c16)
- [M] Danial et al. 2019, RPD for artificial agents. https://doi.org/10.1186/s13673-019-0197-2 (c18)
- [V] Lee et al. 2026, DART. https://arxiv.org/abs/2606.23181 (d03, d04)
- [V] Ning et al. 2026, HRBench. https://arxiv.org/abs/2605.28398 (d05)
- [V] Guo et al. 2026, Think When Needed. https://arxiv.org/abs/2601.18146 (d06)
- [V] Huang et al. 2024, LLMs Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (d07)
- [V] Valmeekam, Marquez, Kambhampati 2023, self-critiquing plans. https://arxiv.org/abs/2310.08118 (d08)
- [V] Valmeekam et al. 2024, Planning in Strawberry Fields. https://arxiv.org/abs/2409.13373 (d09)
- [V] Gu et al. 2025, WebDreamer. https://arxiv.org/abs/2411.06559 (d10)
- [V] Yin, Vardi, Choudhary 2025, Fragile Preferences. https://arxiv.org/abs/2506.14092 (d11)
- [V] Pezeshkpour and Hruschka 2024, option order. https://arxiv.org/abs/2308.11483 (d12)
- [V] Hassid et al. 2025, Don't Overthink it. https://arxiv.org/abs/2505.17813 (d13)
- [V] Shojaee et al. 2025, The Illusion of Thinking. https://arxiv.org/abs/2506.06941 (d14)
- [V] Chen et al. 2025, Do NOT Think That Much for 2+3=?. https://arxiv.org/abs/2412.21187 (d15)
- [V] Aggarwal et al. 2023, Adaptive-Consistency. https://arxiv.org/abs/2305.11860 (d16)
- Cross-reference (file, not re-read): E04/01 evidence_c, E04/05 files (c20).
