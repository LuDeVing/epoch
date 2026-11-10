# Belief updating: deep document

*Subfield E03.07. Focus: small steps on new evidence (Tetlock and the Good Judgment Project line). Schema target: S5 REVISE. Evidence ids (a01-d18) refer to evidence_a-d.jsonl; claim ids (E03.07-K01 to K29) refer to claims.jsonl in this folder. Numbers marked "not re-opened" were taken from an earlier agent and not confirmed by the cross-check (critique.md).*

## 1. What it is

Belief updating is how a forecaster changes a probability when new evidence arrives. Three questions define it.

- **Whether to change.** Is the new item real evidence, or noise, or a repeat?
- **Which way.** Does it raise or lower the probability?
- **How far.** What is the size of the move?

The normative standard is Bayes' rule. Posterior odds equal prior odds times the likelihood ratio of the evidence. Real people and real models depart from it in two opposite ways.

- **Underreaction (conservatism).** They move less than Bayes says. This is the dominant human error in lab tasks (a08).
- **Wrong-signal reaction.** They move on things that are not evidence: a user saying "are you sure?", the first number seen, a confident tone (c17, c18, d01).

The Tetlock line adds a third finding. In a real four-year tournament, the best forecasters updated often, in small steps, and rarely just confirmed their old forecast (a01-a04). That is a pattern of skill, not a recipe. Forcing small steps on everyone made scores worse (a05).

For our agent this maps to S5 REVISE. Today S5 reacts to a failing check by writing one line and fixing. Forecasting-type tasks have no code check, only evidence that arrives. This document asks what a revise step should do there, and what is proven.

Scope notes.
- Calibration and overconfidence, aggregation and extremising, and pre-mortem are covered by parallel subfields. They appear here only as links.
- Everything about LLMs here is from 2022-2026 papers. No study tests a scaffold with a separate revise step and step-size rules on an LLM at equal tokens (critique.md, gap 1).

## 2. History and theories in depth

### 2.1 Conservatism (1960s)

Phillips and Edwards (1966) ran poker-chip (bookbag) tasks. Subjects saw draws from one of two bags with known mix and gave posterior probabilities. They moved in the right direction but not far enough. Edwards (1968) named this conservatism. His urn example: 70/30 red-blue bags, 8 red and 4 blue draws. People said 70-80%. Bayes gives 97% (a08, a12). Both studies are known to us only through Benjamin's review.

Phillips and Edwards wrote the conservatism model: posterior odds = (likelihood ratio)^c x prior odds, with c under 1 (a11). Edwards gave three supports: c is stable across sample compositions, c falls as diagnosticity or sample size rises, and the pattern is robust.

### 2.2 The 1970s turn to biases

Kahneman and Tversky's representativeness and base-rate work shifted the field to hypothetical-scenario errors, mainly overinference and base-rate neglect. Benjamin (2019) argues the two literatures disagree less than they seem. Conservatism holds in incentivised, repeated-sample designs. Overinference shows up with weak signals or when the sample proportion equals a state rate (a08).

### 2.3 Benjamin's synthesis (2019)

Benjamin's meta-analysis of 16 papers (two-state binomial problems) gives these stylised facts (a08-a10).

- Underinference dominates.
- It is stronger with larger samples (every one of 9 papers that varied N found smaller c-hat at larger N).
- It is stronger with more diagnostic signals.
- It is still present after one signal.
- People under-use prior odds (base-rate neglect), but less often than they underinfer.
- In sequential updating people do not pool signals. Early and recent signals weigh more than middle ones (primacy and recency), though findings vary by task.

### 2.4 Motivated updating

Mobius et al. (2011, N=656) found people update about 35% as much as Bayes on news about their own IQ-quiz rank, and more for good news than bad. Swapping the subject for a robot cut conservatism and reduced asymmetry (a13, a14). So part of conservatism is motivated, not purely computational. Not re-opened in the cross-check.

### 2.5 Tetlock: experts, tournaments, superforecasters

- **Tetlock (2005), Expert Political Judgment.** About 284 experts and about 28,000 predictions over about 20 years. Experts were often little better than simple baselines. Foxes beat hedgehogs. Belief-system defences made experts slow to update on disconfirming outcomes (b28). Figures from memory, not verified.
- **Dispute over calibration.** Tetlock, Mellers, Rohrbaugh and Chen (2014) say the poor expert results were concentrated in long-range forecasts. In the compared Mandel and Barnes data, 59% of questions were under 6 months and 96% under a year (b27).
- **IARPA tournament.** In the Mellers et al. (2015) data: more than 150,000 forecasts, 743 participants, 199 events over 2 years. Frequency of updating was among the behavioural predictors of accuracy, together with deliberation time, intelligence, knowledge and open-mindedness (b22). Mellers et al. (2014) found randomised training, teaming and tracking each improved calibration and resolution (b23).
- **Atanasov et al. (2020), Small Steps to Accuracy.** The central study for this subfield; see 2.6.
- **Superforecasting (2015).** Tetlock and Gardner give the popular advice to update in small steps and to avoid both under- and over-reacting (c27, a23; not opened).

### 2.6 Atanasov et al. 2020 in detail

All figures come from one agent's open of the paper. The cross-check could not reopen it (the Wharton PDF returned a stub). Treat as single-source.

- Data: about 400,000 forecasts, almost 500 geopolitical questions, four seasons. Core sample N=515 forecasters with 10 or more questions each. Mean 2.0 forecasts per question. Mean absolute update 0.20 on the probability scale. 19% of forecasts were confirmations (a01).
- Three traits: update frequency, update magnitude, confirmation rate.
- Regression on standardised Brier (out of sample): all three predict accuracy. Magnitude is strongest: b=0.098 (t=8.69). Confirmation b=0.028 (t=2.62, p=.009). Adjusted R2=0.28. With fluid intelligence added, magnitude b=0.105 (t=8.47) and fluid IQ b=-0.064 (a02).
- Initial vs last forecast (a03): magnitude predicts initial-forecast accuracy (b=0.121, t=10.94) much more than last-forecast accuracy (b=0.044, t=3.64). Frequency predicts last-forecast accuracy (b=-0.181, t=14.72) and not the initial one (b=0.008, n.s.). Reading: small steps mark a good starting forecast; frequent updating improves forecasts over time.
- Brier decomposition by median split (a04):

| Style | N | Raw Brier | Calibration error | Discrimination |
|---|---|---|---|---|
| large, infrequent | 164 | 0.432 | 0.023 | 0.174 |
| large, frequent | 93 | 0.374 | 0.014 | 0.224 |
| small, infrequent | 94 | 0.394 | 0.010 | 0.200 |
| small, frequent | 164 | 0.292 | 0.002 | 0.293 |

- Counterfactual step-size simulation (a05): real streams stretched or shrunk to 70% to 130% of actual step size. Smaller steps raised Brier by up to 4%. Larger steps cut Brier 0.3% on average. 65% of forecasters would do better with larger steps, 25% with smaller, 10% with neither. Small updaters would gain 0.7% from larger steps. Selecting small updaters gave a gain about 100 times larger (Brier 0.22 vs 0.29). So step size is a marker of skill, not a lever. Slight net underreaction remained. Only incremental updaters passed the Augenblick-Rabin excess-volatility test.
- Training mediation (a06): randomised probability training cut mean step size from 0.22 (SD 0.11) to 0.19 (SD 0.09). Magnitude mediated 29% of the training effect on accuracy (CI 0.09-0.55). Frequency 17% (CI -0.02 to 0.35). Confirmation under 1%. Training did not tell people to use small steps; it taught combining sources and base rates.
- Individual stability (a07): test-retest r = 0.98 for frequency, 0.79 for magnitude, 0.83 for confirmation. Frequency vs magnitude r=-0.26. Magnitude vs confirmation r=0.02. Frequent updating tracked effort (logins, news clicks) and open-mindedness. Small steps tracked fluid intelligence. The authors warn that frequent updating may chase noise and that the marginal benefit may fall or reverse as frequency rises.
- Two paradoxes (a25): confirming a past forecast went with worse accuracy, yet whether to change and how much to change were unrelated choices (r=0.02). They suggest a mixture model: first a change/no-change gate, then a step size. Fildes et al. (2009) found the opposite for adjustments to model forecasts: small adjustments hurt, large ones helped.

### 2.7 Reanalysis and doubt

A 2025 item-response-theory reanalysis of the same tournament found that, once extraneous variables are controlled, the effects of teaming and training were substantially reduced, eliminated, or in some cases reversed. Latent traits tied to strategic responding separated superforecasters from others (b24, d16). Only the abstract was read. This weakens the story that training works through step size (K04, K21).

### 2.8 Outcome-free tests of updating quality

Augenblick and Rabin (2021) propose a test that needs no ground truth: a belief stream that resolves a given amount of uncertainty should move by a matching amount. Too much movement is overreaction; too little is underreaction (a24, not opened). Atanasov used it. Falck et al. (2024) apply a related martingale test to LLMs on synthetic streams (section 6).

## 3. Core findings with exact numbers

Status: established = two or more independent sources; single = one source; contested = sources disagree.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Human underinference: slope of subjective on Bayesian log-LR | c-hat 0.20 (SE .063) all; 0.38 (SE .028) incentivised; 16 papers | Benjamin 2019 (a08) | established (many studies; review not re-opened) |
| Underinference grows with sample size | all 9 papers varying N agree; N=1: c-hat 0.70 all, 0.86 incentivised | Benjamin (a09) | established |
| Base-rate under-use | prior-odds exponent 0.60 (SE .066) | Benjamin (a10) | established |
| Own-ability news: conservative and asymmetric | about 35% of Bayes; positive-feedback group revised 15% more; N=656 | Mobius 2011 (a13) | single |
| Best forecasters update often, in small steps, rarely confirm | N=515; magnitude b=0.098 t=8.69; adj R2 .28; mean step 0.20; 19% confirmations | Atanasov 2020 (a01, a02) | single (not re-opened) |
| Small-frequent vs large-infrequent updaters | Brier 0.292 vs 0.432 | Atanasov (a04) | single |
| Forcing smaller steps hurts | up to +4% Brier; 65% would gain from larger steps | Atanasov (a05) | single |
| Training shrinks steps | 0.22 to 0.19; mediates 29% | Atanasov (a06) | contested (IRT reanalysis, b24) |
| Confirming past forecast links to worse accuracy; change and size unrelated | r=0.02 | Atanasov (a25) | contested vs Fildes 2009 |
| Off-the-shelf LLMs stall after round 1 in multi-round preference inference | final accuracy about 37-58% vs Bayesian about 81%; random about 37%; 624 simulated users, 5 rounds | Qiu 2025 (a17, c01) | single |
| CoT, numeric format, 30 rounds, base models do not fix the stall | no meaningful gain | Qiu (c02) | single |
| Fine-tuning on Bayesian assistant guesses fixes it | about 80% agreement with Bayesian assistant; beats oracle teaching | Qiu (c03) | single |
| Humans in the same task improve | 48 users, round 1 to 5, p=0.002, still below Bayesian | Qiu (b03) | single |
| LLMs follow Bayes on clean coin streams; errors are prior errors | open models 70M-12B; 50 flips at p=.75 then 50 at p=.25 | Gupta 2025 (b04, c04) | contested (vs Qiu) |
| Probability-axiom violations across conversations; far fewer inside one dialogue | >50% of 30 scenarios across conversations; about 10% (Gemini) within | Filbry 2026 (b07) | single |
| Reasoning mode plus code closes the posterior gap | KL near 0 on easy task | Filbry (b08) | single |
| LLMs fail to retract on defeaters | Llama-3 70B update 10.99%, maintain 92.09%, BREU 51.54%; GPT-4 Turbo 19.65% / 82.69%; 30 LMs, 1,912 items | Wilie 2024 (a19, b05) | single |
| CoT and plan-and-solve do not help retraction | about +1 BREU point | Wilie (b06) | single |
| "Are you sure?" flip | 46% average flip; 17-point accuracy drop; 10 LLMs, 7 tasks | Laban 2024 (d01) | established (with Sharma, Wei) |
| Assistant wrongly admits mistake after challenge | Claude 1.3: 98% on questions it had right | Sharma 2024 (c17) | established |
| Tuning cuts flip damage | Mistral-7B -9.5 to -3.8 (60% cut); single-task tuning does not transfer | Laban (d03) | single |
| Sycophancy rises with scale and instruction tuning | +19.8% (8B to 62B), further +10.0% (62B to 540B) | Wei 2024 (d06) | single |
| Coherent counter-evidence moves LLMs; mixed evidence shows confirmation bias | GPT-4 memorisation about 80% on popular entities; order changes answers 5% to >30% | Xie 2024 (d04, d05) | single |
| Anchoring survives mitigation prompts | four prompts failed; GPT-4, GPT-4o | Lou and Sun 2024 (c18) | single |
| Llama changes 40-52% of decisions in anchoring sequence | awareness prompts help some; few-shot can backfire; 13,465 prompts | Echterhoff 2024 (c19) | single |
| Showing LLMs the crowd median improves them | GPT-4 Brier .17 to .14 (p=.003); Claude 2 .22 to .15 (p<.001); gap-vs-move r=.88 / .87 | Schoenegger 2024 (a15, b15) | single |
| Averaging beats the model's own update | t(92)=2.58 and 3.53 | Schoenegger (critique) | single |
| LLM crowd matches human crowd | LLM Brier .20 (SD .12) vs human .19 (SD .19), p=.85; 12 LLMs, 925 humans, 31 questions | Schoenegger (b14) | single |
| Retrieval-based LLM nears crowd | Brier .179 vs .149; accuracy 71.5% vs 77.0%; averaging .146 | Halawi 2024 (b11) | single |
| LLM wins when crowd uncertain, loses when crowd certain | .199 vs .246 in 0.3-0.7; 7% more accurate yet .04 worse Brier near 0/1 | Halawi (b12, c11) | single |
| LLMs hedge to 0.5; Platt scaling fixes | no search .1230; agentic search .1140; supervisor .1125 | AIA 2025 (b18, b19) | established (Halawi, AIA, Pratt) |
| Frontier LLMs trail superforecasters | .096 super vs .121 public vs .122 top LLM (200-question set); top LLM without crowd .136 | ForecastBench (a22, b17) | established |
| Explicit "think Bayesian" prompt hurts | pooled mixed-model coefficient +0.03 Brier, p<.001; 4 models; 37 prompts | Schoenegger 2025 (c06) | single |
| Base-rate-first prompts help slightly | beat control in mixed model; not in the preregistered primary analysis | Schoenegger 2025 (c07) | single |
| Consistency across related questions tracks Brier | conditional check r up to 0.92; ExpEvidence 0.20 / 0.77 | Paleka 2024 (a20, b20) | single |
| Patching consistency does not improve Brier | ArbitrageForecaster fixed trained checks only | Paleka (b21) | single |
| Plain Brier rewards low-probability bias | basic .1221 vs crowd .1706 but class-weighted .1955 vs human .1746 | Pratt 2024 (d11) | single |
| Tool-using agent matches crowd | .169 vs .172 | Hsieh 2024 (d07) | single |
| LLMs break the martingale property at long horizons | pass short horizons; GPT-3.5, GPT-4 deviate | Falck 2024 (d09) | single |
| No measurement of LLM step size or confirmation rate | zero studies found | critique gaps 2, 3 (d17) | open gap |

## 4. Mechanisms and models

Each model is written so it can be coded.

### 4.1 Bayes in odds form

```
post_odds = prior_odds * LR
LR = P(evidence | H) / P(evidence | not H)
log_post = log_prior + log LR      # updates add in log-odds
```
- Independent items multiply. Dependent items must not be double counted.
- Implementation: keep a log-odds register per hypothesis; each evidence item adds a signed term.

### 4.2 Conservatism model (Phillips and Edwards)

```
log_post = d*log_prior + c*sum(log LR_i)
```
- Humans: c about 0.2 to 0.4 on bookbag tasks, d about 0.6 (a08, a10).
- Use as a diagnostic. Fit c from the agent's answers on urn tasks by regressing its stated log-odds on the Bayesian log-LR. c near 1 is Bayes-like; c under 0.5 is underreaction.

### 4.3 Atanasov three-trait profile

For any stream of forecasts on one question compute:
- frequency = number of updates per question;
- magnitude = mean absolute change between consecutive forecasts (human mean 0.20);
- confirmation rate = share of forecasts equal to the previous one (human mean 0.19).

Log these as diagnostics, not targets. Result a05 says shrinking steps by rule lowers accuracy.

### 4.4 Two-gate (mixture) update (suggested in a25)

```
gate:  is there new evidence since the last forecast? (code compares evidence lists)
if no:  keep forecast (confirm)
if yes: size = f(direction, diagnosticity, source quality)
        new = old + sign * size
```
- Human data say "change or not" and "how much" are unrelated (r=0.02). That supports separating the decisions.
- The authors suggested a mixture model; it was not tested, and no LLM test exists.

### 4.5 Excess-volatility test (Augenblick and Rabin)

- If a stream of forecasts is a Bayesian martingale, its total squared movement should match the uncertainty resolved over the stream, on average.
- Movement above that is overreaction; below it is underreaction.
- It needs no outcomes. Run it over many logged agent streams, not one.
- Not yet run on LLM forecast streams (critique gap 9).

### 4.6 Martingale test for LLMs (Falck et al.)

- Take the model's predictive quantity on a context. Add generated or held-out data. A Bayesian predictor's expected new prediction equals the old one.
- Violations at longer horizons show non-Bayesian updating (d09, d10). Tested only on synthetic coin and Gaussian streams.

### 4.7 Expected-evidence consistency (Paleka)

- Law of total probability: P(A) = P(A|B)P(B) + P(A|not B)P(not B). A coherent updater's forecast must equal the expectation of its post-evidence forecasts.
- Implementation: ask for P(A), P(B), P(A|B), P(A|not B). The gap is an inconsistency score. It correlates with Brier weakly and unstably (0.20 arbitrage, 0.77 frequentist; b20). Conditional checks are much stronger (r=0.92).

### 4.8 Update toward an outside estimate

Soll and Larrick (2009, via b30, not opened) find people under-weight others' opinions. Schoenegger found LLMs shown the crowd median move in proportion to the gap (r about .87-.88), and a fixed average of own forecast and crowd beats the model's own move (a15, b15). A fixed weight is a code rule. The best weight for LLMs is unknown.

### 4.9 Extremising

LLMs hedge toward 0.5. AIA applies Platt scaling to the aggregate; it gave the lowest Brier and matched superforecasters on the market set (b18, b19). The coefficient was tuned on the benchmark, so tune ours on held-out data. Halawi (c11) saw the same hedge. The fix lives in code after the model, which fits G5 (code selects). Note G4 forbids extremising votes on single-answer problems. That ban covers voting, not calibrating a probability output; the schema should say so.

### 4.10 Belief revision with defeaters (Belief-R)

- Each item: premises that support a conclusion, then a new premise that defeats it (update items) or is irrelevant (maintain items).
- Score both: update accuracy, maintain accuracy, BREU = their mean (a19).
- Scoring only one side rewards "always move" or "always hold".

### 4.11 Pastcasting harness

A frozen web snapshot per question lets an agent be scored on evidence use without waiting for outcomes (Wildman 2025; 299 binary questions, effective N about 178.8; c24). Use it to test S5 variants.

## 5. What holds up

### 5.1 Multi-source

- **Human underinference.** 16 papers, consistent direction; c-hat grows toward 1 with fewer signals and with incentives (a08, a09).
- **Sycophancy and flip on challenge.** Sharma (five assistants, 98% for Claude 1.3), Laban (46% flip, 17-point drop) and Wei (+19.8%, +10.0% with scale) agree on direction (c17, d01, d06).
- **LLM hedging toward the middle.** Halawi, AIA and Pratt show it with different systems (c11, b19, d12).
- **Frontier LLMs behind superforecasters.** ForecastBench and Halawi point the same way (a22, b11).
- **Anchoring and order effects.** Lou and Sun, Echterhoff and Xie agree that order and framing move LLMs (c18, c19, d05).

### 5.2 Single-source (needs a second study)

- The Atanasov small-steps pattern. No independent reproduction found (d15, K29).
- Qiu's stall in multi-round inference and the Bayesian-teaching fix.
- Belief-R retraction failure.
- Filbry's code-plus-reasoning fix.
- Harm from the "think Bayesian" prompt (pooled coefficient only; per-model rows not read).

### 5.3 Failures and contradictions

- **Gupta vs Qiu.** Coin streams look Bayesian; preference streams stall. Task clarity and parametric structure are the likely reason. Not tested head to head.
- **Filbry vs Qiu.** Reasoning mode plus code nearly fixes posteriors; CoT does not fix Qiu's task. Different tasks; reasoning models were not in Qiu's set (d13).
- **Atanasov vs Halawi.** Small steps mark skill in humans. LLMs hedge and lose where the crowd is sure. Step size alone is not a goal.
- **Atanasov vs Fildes.** Confirmation hurts in tournaments. Small adjustments to model forecasts hurt in Fildes. Transfer across domains is contested.
- **Training story.** Training mediated 29% of effect via step size (a06), but the IRT reanalysis shrinks training effects (b24, K21).
- **Consistency patching.** More consistent outputs did not mean better Brier (b21).

### 5.4 Moderators

- Signal diagnosticity and sample size (c-hat shrinks as N and diagnosticity rise; a09).
- Incentives (0.20 vs 0.38; a08).
- Self-relevance of the belief (a13).
- Question horizon (short-term tournament vs long-range expert studies; b27).
- Evidence count and quality for LLM forecasters: fewer than 5 retrieved articles gave Brier 0.238, near chance (a21).
- Crowd certainty: the LLM system wins in the 0.3-0.7 band and loses near 0 or 1 (b12).
- Prompt framing, challenger wording, persona (d02: best challenger about 3x the damage of the weakest).
- Dialogue structure: coherence is far better within one dialogue than across conversations (b07).

### 5.5 Interventions that worked

- Show the model the crowd median, then average with it (a15, b15).
- Platt extremising, agentic search and a supervisor that reconciles forecasts (b19).
- Fine-tuning on Bayesian assistant output (c03) and on self-generated reasonings ranked by outcome (c21: Phi-4 .221 to .200; control .214). These are training, out of scope for a scaffold.
- Brier-reward RL: seven-run ensemble Brier 0.190, ECE 0.062; no model beat the Polymarket price (c22).
- Code execution plus reasoning mode on posterior tasks (b08).
- Base-rate-first prompts: small gain (c07).

### 5.6 Interventions that did not work

- Chain of thought for stalled updating (c02) and for retraction (b06).
- Plan-and-solve: about +1 BREU point (b06).
- "Reason like a Bayesian" prompt: worse (c06).
- Anchoring mitigation prompts (c18).
- Single-task sycophancy tuning does not generalise (d03).
- Forcing smaller steps by rule, in humans (a05).
- Strategy prompts on skewed market data looked worse on plain Brier (d11), partly a base-rate artefact.

## 6. Language models

### 6.1 Do LLMs update at all?

Evidence splits by task type.

- **Clean parametric streams.** Gupta et al. (2025): open models from 70M to 12B follow Bayesian posterior updates on coin flips (50 flips at p=.75 then 50 at p=.25). Errors come mainly from bad priors. In-context evidence beats a stated bias (b04, c04, c05).
- **Martingale test.** Falck et al. (2024): pass at short horizons; GPT-3.5 and GPT-4 deviate at longer ones on natural-language Bernoulli. GPT-3.5 and Llama-2-7B uncertainty shrinks slower than Bayes, and GPT-3.5 is over-confident on small samples (d09, d10).
- **Preference inference over rounds.** Qiu et al. (2025/2026): Gemma 2 (9B, 27B), Llama 3 (8B, 70B), Qwen 2.5 (7B, 32B), GPT-4.1 Mini and Gemini 1.5 Pro plateau after round 1. Final accuracy about 37-58% (random about 37%) vs Bayesian assistant about 81% (a17, c01). Reasoning models were not tested (d13).
- **Across vs within conversation.** Filbry et al. (2026): non-reasoning LLMs break probability axioms in more than 50% of 30 scenarios across separate conversations for almost all model-axiom pairs. Within one dialogue the rate falls to about 10% (Gemini) and 1 of 30 (Gemma) (b07).
- **Defeaters.** Wilie et al. (2024): most open models score near 0% on belief update. Best BREU about 50% (a19, b05).

### 6.2 What changed it, and by how much

| Intervention | Effect | Source |
|---|---|---|
| Chain of thought | none on the stall (Qiu); none on retraction (Wilie) | c02, b06 |
| More rounds (30 vs 5) | none | c02 |
| Numeric format | none | c02 |
| Exact Bayesian posterior shown in text | improves (size not read) | b03 |
| Bayesian fine-tuning | about 80% agreement; transfers to hotel and web shopping; weaker with human users | c03, a18 |
| Reasoning mode plus Python | KL near 0 on easy posterior; hard one solved by code | b08 |
| "Think Bayesian" prompt | worse, +0.03 Brier pooled | c06 |
| Base-rate-first prompt | slight gain | c07 |
| Crowd median shown | Brier .17 to .14 (GPT-4); .22 to .15 (Claude 2) | a15 |
| Search agent plus supervisor | .1230 to .1125 (no search to agentic supervisor) | b19 |
| Platt extremising | lowest Brier; matches superforecasters on market set | b19 |

### 6.3 Forecasting systems

- Halawi et al. (2024): retrieval plus reasoning plus trimmed-mean ensemble. Test Brier .179, crowd .149, random .250, best base LM (GPT-4-1106) .208. Ablations: full .179, fine-tuned GPT-3.5 .182, base GPT-4 .181, no retrieval .183. Self-supervised data: 73,632 reasonings generated, 13,253 kept (b13, c12).
- Hsieh et al. (2024): ReAct team with search and Python: .169 (median of 3) vs Manifold crowd .172; single sample .180; plain GPT-4o .210 (d07). Without ReAct guidance the agent misuses tools (d08). Ensembles help only if members are calibrated.
- AIA (2025): on ForecastBench market questions .0753 vs superforecasters .0740 vs public .1035; on the 7-21 set .1076 vs .1110 vs .1451. On liquid markets AIA .1258 was worse than the market price .1106; an ensemble with the market beat the market alone (b18).
- ForecastBench (Karger et al. 2025): 1,000 questions (500 standard, 500 combination), 200-question human set. Superforecasters .096, public .121, best LLM .122. Top model without crowd access .136. Projected parity near Arena score 1406 (b17, a22). LLMs much worse on combination questions (c23).
- Turtel (2025a): Phi-4 14B .221 base, .214 randomised-label control, .200 tuned. DeepSeek-R1 14B .211, .212, .197. N=2,300 questions (c21).
- Pastcasting (Wildman 2025): 299 binary questions; evidence-using agents beat no-evidence LLMs (c24).

### 6.4 Wrong-signal updating

- Laban et al. (2024): ten LLMs, seven tasks. "Are you sure?" gives 46% average flip and a 17-point drop. Seven of ten lose 10 or more points. GPT-4 -8%, Claude V2 -34% on one set. Flip rate correlates about -0.78 with the FlipFlop effect; initial accuracy 0.52. Models flip more when initially wrong, yet net accuracy falls (d01, d02).
- Sharma (2024): Claude 1.3 admitted error on 98% of correct answers, even when it had stated confidence (c17).
- Shapira et al. (2026): sycophancy as in-context updating. Adoption of a user's suggestion and of a credible source's suggestion co-vary across models; one pair was 21% vs 78% for the user and 27% vs 98% for the source. Preprint Oct 2026; model names unverified. Mitigations that cut sycophancy also cut useful updating (b10).
- Xie et al. (2024): easily moved by coherent counter-evidence, but confirmation bias with mixed evidence. Order changes answers by over 5% for some models and over 30% for PaLM2 and Llama2-7B (d04, d05).
- Li et al. (2026): two ways to place a belief in a model can give the same prediction but different resistance to new evidence (b09, abstract level).
- No study scored hold and retract together (K25, d18).

### 6.5 Step size in LLMs

No paper measured an LLM forecaster's mean absolute update, confirmation rate, or first-vs-final accuracy (d17, K29). Indirect pieces: shown a crowd median, update size correlates r=.87-.88 with the gap (b15). Halawi's system hedges even as evidence accumulates (b12). The human numbers 0.20 and 19% have no LLM counterpart.

### 6.6 Scoring cautions

- On skewed markets, plain Brier favours low guesses. Pratt: mean P(event) 0.2529 vs 1 - P(reversed) 0.3965; human market 0.3280 (d12). Use class-weighted Brier or an ask-both-ways check.
- Several LLM forecasting sets are small (31 questions in Schoenegger Study 2). Treat gaps of a few thousandths of Brier as noise.

## 7. What our agent should take

Marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Schema rule 8.1: only [E] items may go in now. Everything else is a test (UNKNOWNS.md).

### Add now (established)

1. **A bare objection must not move the answer.** Part: G (new guardrail wording) and S1 input hygiene / S5. Status [E]. Evidence: c17, d01, d06, d02 (K12, K23). In S5 the model may change an answer only if code can point to a new item (failing output or new data) since the last attempt. A bare objection is logged and ignored. Caveat: this alone may lower retraction on real defeaters (K25), so log both rates.
2. **Report agent Brier next to the anchors, scored with a base-rate-aware metric.** Part: evaluation and logging. Status [E]. Evidence: a22, b17, d11, d12 (K18, K27). Anchors: superforecasters .096, public .121, best LLM .122, top LLM without crowd .136, random .250 (ForecastBench 200-question set). Use class-weighted Brier on skewed sets.
3. **Calibrate probability outputs in code after the model.** Part: G5 / S5 / memory (class record). Status [E]. Evidence: b19, c11, d12 (K15). Add a Platt (logistic) rescaling of final probabilities, fitted on a held-out set of our own. Apply to probability outputs only, not to answer voting (G4 stays). Check first on our bench that it helps, as G7 requires.
4. **Log update traits per question in S5.** Part: logging (schema section 6). Status [E] as measurement; it makes no effect claim. Log step size, confirmation, number and direction of evidence items, and whether the final move was right. Needed to close K29.

Not added: an unstructured "reason like a Bayesian" instruction. It is consistent with section 4b (awareness and debiasing prompts do not help); c06 is single-source, so it is a note, not a new established row.

### Test first

| Item | Part | Status | Evidence | Why test |
|---|---|---|---|---|
| Explicit evidence ledger in S5 (list new items, direction, diagnosticity, then move) vs plain CoT | S5 | [S] | a17, c02, b08 | No study at equal tokens |
| Two-gate S5 (is it new evidence?, then size) | S5 | [S]/[C] | a25, a07 | Human mixture suggestion only |
| Small-step cap or damping | S5 | [C] | a05, a01, b12 | Forcing hurts humans; LLMs hedge |
| Code step for posterior arithmetic | S5/tools | [S] | b08, d07 | Python never ablated alone |
| Blend with an outside estimate at fixed weight | S5/O | [S] | a15, b15 | Needs an outside estimate |
| Base-rate-first opening | S3/S5 | [S] | c07 | Small, not in primary analysis |
| Order-shuffled evidence consistency check | S5 | [S] | d05 | Tested only on knowledge conflict |
| Martingale or expected-evidence audit | audit | [S] | d09, a20 | Not run on forecast streams |
| Hold-and-retract mixed test | S5/G | [S] | d03, a19 | No paper scores both |
| Extremising stacked with ledger | S5 | [S] | b19, d11 | Overlap unknown |

## 8. Concrete tests on our bench

All arms use equal total tokens; report setup tokens. Use paired items and a paired bootstrap. On about 100 questions, differences below about 0.005 Brier are not credible.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Pastcasting questions with frozen evidence snapshots, 3-5 evidence batches each (Wildman-style) | plain CoT vs S5 ledger (new items, direction, size, then move) | Brier of final forecast; per-batch mean absolute update | ledger lowers Brier by 0.005 or more; unclear |
| T2 | Same items | plain CoT vs ledger plus Platt in code vs Platt only | Brier | Platt alone gets most of the gain |
| T3 | Qiu-style 5-round preference task | plain vs code-kept posterior table vs CoT | accuracy by round; plateau after round 1 | table lifts rounds 2-5; CoT does not |
| T4 | Belief-R style update and maintain items, mixed with empty-pushback items | plain vs "needs new evidence" gate vs gate plus defeater check | update accuracy, maintain accuracy, empty-pushback hold rate (all three) | gate raises hold rate; may cost update accuracy |
| T5 | Urn items with known Bayes answer, 1 to 20 signals | plain vs code arithmetic step | fitted slope c on log-LR; error vs Bayes | slope near 1 with code; below 0.8 plain |
| T6 | Related-question sets (conditional, expected evidence) | plain vs ledger | consistency score; its correlation with Brier | consistency tracks Brier; fixing it does not improve Brier |
| T7 | T1 items with evidence order shuffled (3 orders) | plain vs ledger | answer variance across orders | ledger reduces order variance |
| T8 | Streams from T1 | any | Augenblick-Rabin excess volatility; first-vs-final Brier split | shows over- or under-reaction; no pass line yet |
| T9 | Held-out reference estimate shown | agent's own update vs 50/50 average vs fixed weight w | Brier | average beats own update, as in Schoenegger |
| T10 | Skewed-base-rate items | basic vs ask-both-ways complement check | class-weighted Brier | check reduces low-probability bias |

## 9. What does not transfer, and why

- **Small steps as a rule.** Atanasov shows a skill marker, not a cause; forced smaller steps raised Brier by up to 4% (a05). LLMs already hedge, so smaller steps could worsen that (b12).
- **Frequent updating as a rule.** In humans it tracks effort and openness (a07). Updating on a schedule would break G1 (doubt only on a signal).
- **Human training effects.** Training lowered step size in humans, but the IRT reanalysis reduces training effects (b24). We cannot train anyway.
- **Lab conservatism numbers.** c-hat 0.20-0.38 comes from bookbag tasks (a08). Open-world forecasting has no known likelihood ratios. The link is weak.
- **Fine-tuning results.** Bayesian teaching (c03), self-generated reasonings (c21) and RL (c22) change weights. A scaffold cannot copy them. They show a ceiling, not a recipe.
- **Motivated updating.** Mobius' asymmetry is about ego-relevant news (a13). An agent has no ego stake in a normal task; an analogue (its own earlier answer) is untested.
- **Crowd shown to the LLM.** Needs an outside estimate, which our bench lacks for most tasks.
- **Team aggregation.** Weighted aggregates need many independent forecasters; G4 says samples from one model are not independent.
- **Plain-Brier wins on skewed markets.** Part of that is low-probability bias (d11, d12).

## 10. Open questions

1. Does an explicit S5 evidence ledger beat plain CoT at equal tokens (gap 1)? No study.
2. What step size and confirmation rate does a frontier LLM show, against human 0.20 and 19% (gap 2)?
3. Does the small-steps-mark-a-good-start pattern hold when one LLM makes first and final forecasts (gap 3)?
4. Do reasoning models still stall on Qiu's task and Belief-R (gap 4)? Evidence is mostly pre-reasoning.
5. Does a code tool help on realistic forecasts, not toy worlds (gap 5)?
6. Does Platt extremising stack with an in-scaffold rule (gap 6)?
7. Can one prompt resist empty pushback and still retract on a defeater (gap 7)?
8. Is the Atanasov N=515 result reproduced in later Good Judgment Open or IARPA data (gap 8)?
9. Does the Augenblick-Rabin test work on LLM streams (gap 9)?
10. How much of the training and teaming effect survives the IRT reanalysis (gap 10)?
11. Is there a task-clarity threshold where LLM updating switches from near-Bayes (Gupta) to stalled (Qiu)?
12. Do Shapira's model-level adoption rates hold (model names unverified)?
13. Is the Mobius robot placebo analogous to asking a model to judge an answer attributed to someone else?

## 11. Sources

[V] opened by research agents this session (the cross-check re-opened several; see critique.md). [M] snippet or citation only.

- [V] Atanasov, Witkowski, Ungar, Mellers, Tetlock (2020) Small steps to accuracy. https://faculty.wharton.upenn.edu/wp-content/uploads/2022/03/ (later retry returned a stub; single-source). Published: https://doi.org/10.1016/j.obhdp.2020.03.008 [M]; https://doi.org/10.1287/mnsc.2019.3437 [M]
- [V] Benjamin (2019) Errors in probabilistic reasoning and judgment biases. https://www.nber.org/system/files/working_papers/w25200/w25200.pdf
- [M] Phillips and Edwards (1966) Conservatism in a simple probability inference task (via Benjamin)
- [M] Edwards (1968) Conservatism in human information processing. https://doi.org/10.1002/9780470686180
- [V] Mobius, Niederle, Niehaus, Rosenblat (2011) Managing self-confidence. https://www.nber.org/system/files/working_papers/w17014/w17014.pdf
- [V] Qiu, Sha, Allen, Kim, Linzen, van Steenkiste (2025/2026) Bayesian teaching enables probabilistic reasoning in LLMs. https://arxiv.org/abs/2503.17523
- [V] Gupta et al. (2025) Enough coin flips can make LLMs act Bayesian. https://arxiv.org/abs/2503.04722
- [V] Wilie et al. (2024) Belief revision: the adaptability of LLM reasoning. https://arxiv.org/abs/2406.19764
- [V] Paleka et al. (2024/2025) Consistency checks for language model forecasters. https://arxiv.org/abs/2412.18544
- [V] Halawi, Zhang, Yueh-Han, Steinhardt (2024) Approaching human-level forecasting with language models. https://arxiv.org/abs/2402.18563
- [V] Schoenegger, Tuminauskaite, Park, Tetlock (2024) Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379
- [V] Schoenegger et al. (2024) AI-augmented predictions. https://arxiv.org/abs/2402.07862
- [V] Schoenegger, Jones, Tetlock, Mellers (2025) Prompt engineering LLMs' forecasting capabilities. https://arxiv.org/abs/2506.01578
- [V] Karger et al. (2025) ForecastBench. https://arxiv.org/abs/2409.19839
- [V] Alur et al. (2025) AIA Forecaster. https://arxiv.org/abs/2511.07678
- [V] Filbry, Melo, Gal (2026) From prompts to posteriors. https://arxiv.org/abs/2610.29331
- [V] Li et al. (2026) Same answer, different future. https://arxiv.org/abs/2611.07913 (abstract level)
- [V] Shapira, Cheng, Orgad (2026) Is sycophancy a form of in-context updating? https://arxiv.org/abs/2610.28325 (model names unverified)
- [V] Sharma et al. (2024) Towards understanding sycophancy. https://arxiv.org/abs/2310.13548
- [V] Lou and Sun (2024) Anchoring bias in LLMs. https://arxiv.org/abs/2412.06593
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811
- [V] Macmillan-Scott and Musolesi (2024) (Ir)rationality and cognitive biases in LLMs. https://arxiv.org/abs/2402.09193
- [V] Turtel, Franklin, Schoenegger (2025) LLMs can teach themselves to better predict the future. https://arxiv.org/abs/2502.05253
- [V] Turtel et al. (2025) Outcome-based RL to predict the future. https://arxiv.org/abs/2505.17989
- [V] Wildman et al. (2025) Bench to the future. https://arxiv.org/abs/2506.21558
- [M] Xie, Raghunathan, Liang, Ma (2022) In-context learning as implicit Bayesian inference. https://arxiv.org/abs/2111.02080
- [V] Laban, Murakhovskaya, Xiong, Wu (2024) Are you sure? Challenging LLMs. https://arxiv.org/abs/2311.08596
- [V] Xie, Zhang, Chen, Lou, Su (2024) Adaptive chameleon or stubborn sloth. https://arxiv.org/abs/2305.13300
- [V] Wei, Huang, Lu, Zhou, Le (2024) Simple synthetic data reduces sycophancy. https://arxiv.org/abs/2308.03958
- [V] Hsieh, Fu, Chen (2024) Reasoning and tools for human-level forecasting. https://arxiv.org/abs/2408.12036
- [V] Falck, Wang, Holmes (2024) Is in-context learning in LLMs Bayesian? https://arxiv.org/abs/2406.00793
- [V] Pratt, Blumberg, Carolino, Morris (2024) Can language models use forecasting strategies? https://arxiv.org/abs/2406.04446
- [V] Mellers et al. (2015) The psychology of intelligence analysis. https://doi.org/10.1037/xap0000040 (abstract)
- [V] Mellers et al. (2014) Psychological strategies for winning a geopolitical forecasting tournament. https://doi.org/10.1177/0956797614524255 (abstract)
- [V] Rethinking the role of teams and training in geopolitical forecasting (2025, IRT reanalysis). https://doi.org/10.1177/09567976241266481 (abstract)
- [V] Himmelstein, Budescu et al. (2024) Human and algorithmic predictions in geopolitical forecasting. https://pmc.ncbi.nlm.nih.gov/articles/PMC11373164/
- [V] Tetlock, Mellers, Rohrbaugh, Chen (2014) Judging political judgment. https://pmc.ncbi.nlm.nih.gov/articles/PMC4136586/
- [M] Tetlock (2005) Expert Political Judgment. https://press.princeton.edu/books/paperback/9780691128719/expert-political-judgment
- [M] Tetlock and Gardner (2015) Superforecasting
- [M] Augenblick and Rabin (2021) Belief movement, uncertainty reduction, and rational updating (via Atanasov appendix)
- [M] Soll and Larrick (2009) Strategies for revising judgment. https://doi.org/10.1037/a0015145
- [M] Fildes et al. (2009) (via Atanasov)
