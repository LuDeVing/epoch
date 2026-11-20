# Social cognition in animals: deep document

*Subfield A18.06: corvid social cognition and what others know. Key works: Emery and Clayton (2001), Hare, Call and Tomasello (2000, 2001). Role for our agent: background only. The animal studies set the logic of controls. The usable results are the LLM studies in section 6. Evidence ids (a01 to d21) refer to evidence_a-d.jsonl in this folder; claim ids (K01 to K22) to claims.jsonl. Independence note: Kosinski, Ullman, Shapira, Sap and Kim each appear 2 to 3 times in the evidence files; each is one source.*

## 1. What it is

Social cognition in animals asks what an animal represents about other agents. Three levels are worth keeping apart.

1. **Behaviour reading.** The animal reacts to cues: gaze direction, head orientation, body position, who is near, what that individual did last time.
2. **Perception or knowledge tracking.** The animal behaves as if it knows what another individual has seen or can see ("what others know").
3. **Belief tracking.** The animal behaves as if it knows what another holds true even when it is false (false belief), or what another wants (desire).

The field's central problem is that level 1 can mimic levels 2 and 3 in almost every test. A bird that hides food away from a watching rival may have learned a rule ("a rival nearby means theft"), not a belief about the rival's knowledge. Most of the history is a fight over which controls separate the rule from the representation.

Two lines matter here.

- **Corvid caching studies.** Jays and ravens hide food and steal from others. A cacher can lose food to a watching thief, so it pays to track who saw what. Main sources: Emery and Clayton 2001 (scrub-jays), Dally, Emery and Clayton 2006, Bugnyar and Heinrich 2005, Bugnyar 2011, Bugnyar et al. 2016 (ravens), Amodio et al. 2021 (Eurasian jay null).
- **Primate competition and looking studies.** Hare, Call, Agnetta and Tomasello 2000 and Hare, Call and Tomasello 2001 (chimpanzees compete for food that a rival can or cannot see); Krupenye et al. 2016 (apes look where a deceived actor will search); Buttelmann et al. 2017 (apes help an actor who holds a false belief); Martin and Santos 2014 and Horschler et al. 2019 to 2021 (monkey looking times).

For our agent the link is indirect. A thinking scaffold is a single agent. It does not hide food. But a language model asked "what does Sally think?" faces the same inference problem, and the LLM literature has copied the animal-cognition toolkit: pass-fail tasks, control conditions, low-level alternative explanations. Section 6 covers it.

Overlap with earlier work in this series: this folder links to 05_prospection_and_mental_time_travel (scrub-jay planning, a25) and to the methods and alternative-explanation subfields (a26). The parallel subfield on simulation versus theory accounts is not covered here (a27).

## 2. History and theories in depth

**Premack and Woodruff (1978)** asked "does the chimpanzee have a theory of mind?" The question was whether an animal imputes mental states to others. Early answers used training tasks that could be solved by cue learning. (Background, not opened this session.)

**Hare, Call, Agnetta and Tomasello (2000)** moved to competition. A subordinate chimpanzee and a dominant compete for food. Food that only the subordinate can see is a "safe" target. In plain words: dominants took virtually all food both could see, and subordinates were often successful in three situations where they had better visual access (a07, abstract only, exact counts not read). Hare, Call and Tomasello (2001) added controls for the rival's past experience and the subordinate's own cues (a08, b12, not read). Reading: chimpanzees know what rivals can and cannot see. The competitive paradigm was seen as more natural than cooperative tasks.

**Emery and Clayton (2001)** made the corvid case. Western scrub-jays that had stolen from others' caches (and only those) re-cached in new places when they had been watched while caching, but not when they cached in private (a01 to a03). The authors argued for "experience projection": the bird uses its own history as a thief to predict what a watcher will do. Emery and Clayton (2004) generalised to "the mentality of crows", pointing at convergent evolution of cognition in corvids and apes (a22, not read).

**Dally, Emery and Clayton (2006, Science)** asked whether jays track which observer watched which caching event. Correction from the gap search: this is a "who watched when" study, not a deception study, and the evidence points to no cue-driven protection by observer behaviour (d14). Full text was not opened.

**Bugnyar and Heinrich (2005); Bugnyar (2011); Bugnyar, Reber and Buckner (2016)** are the raven line. Ravens changed pilfering and protecting by whether the rival had seen the caching (a04, a05, b06), and attributed visual access through a peephole from sound alone (a06, b07).

**The sceptical response.** Penn and Povinelli (2007) said that perceptual cues (face direction, body position) are enough to explain the data (b05, a21). Heyes (2015) argued that the field lacks agreed alternative explanations and tests that discriminate between them (a16). Call and Tomasello (2008), 30 years after Premack and Woodruff, argued chimpanzees understand perception and goals, probably not false belief (a23, not read). The state of play is a stalemate on belief and a weaker consensus on perception.

**Anticipatory looking (2016 on).** Krupenye et al. (2016) used eye tracking while apes watched videos. The sceptical reply was "submentalizing": the effect might come from low-level attention to objects and agents (a10). Kano et al. (2019) added an experience control. Apes who had watched through an opaque barrier anticipated; those with a see-through barrier did not (b08, d16).

**Replication-stress phase.** Infant versions of the same looking logic failed a 160-infant, two-site replication of Southgate 2007 (d17). Monkey knowledge looking times were small and depended on which change was used (a11 to a14). The Cambridge lab's own five-experiment retest of its jay perspective and desire effects mostly failed (Amodio et al. 2021, b01, b02, c17). Independent labs found pilferer-identity effects in other corvids but not desire-state ones (d15).

**Transfer to AI (2022 on).** Sap et al. (2022), Kosinski (2023), Ullman (2023), Shapira et al. (2023), Strachan et al. (2024) apply false-belief tasks to LLMs. The same pattern repeats: a high pass rate on classic items, collapse under small changes, and explicit use of the animal-cognition rule "check the low-level alternative" (Rane et al. 2025, c14; Hu, Sosa and Ullman 2025, c13).

**Competing accounts to hold in parallel.**

| Account | Claim | What would favour it |
|---|---|---|
| Behaviour reading (Penn and Povinelli) | Learned or innate rules on observable cues | Failure on cue-matched controls; no effect when cues absent |
| Experience projection (Emery and Clayton) | Own past as thief predicts others' behaviour | Effect only in birds with thieving history (a03) |
| Submentalizing (Heyes, Krupenye 2017 test) | Low-level attention effects mimic belief tracking | Same response when agents are replaced by shapes |
| Perception-goal reading (Call and Tomasello) | Tracks perception and goals, not belief | Passes on knowledge, fails on false belief |

## 3. Core findings with exact numbers

Status: **robust** (several independent sources), **single** (one lab or one source), **contested**, **failed** (did not replicate), **LLM** (language-model study).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Scrub-jays with thieving experience re-cache in new sites after being watched, not in private | Observer+pilferer n=7: 0.44 vs 0.06 re-cached (Z=2.20, P<0.05). Cambridge replication, same birds: 0.28 vs 0.08 | Emery and Clayton 2001 (a01) | single, same birds both sites |
| Jays track the social context of each caching event | Two trays, n=7: re-cached 0.45 observed vs 0.04 private (Z=2.37); recovered 0.73 vs 0.39; items cached equal (3.93 vs 3.57) | Emery and Clayton 2001 (a02) | single |
| Only jays with thieving experience show it | Observer-only group no selective re-caching (old sites Z=1.6, P>0.1); each pilfering group n=7, Z=2.20 to 2.37 | Emery and Clayton 2001 (a03) | single |
| Jay barrier test: out-of-view tray protected more | Friedman chi2(2)=2.57, n=8, p=0.03; Dunnett q=2.9; observer vs control re-caching sign test 6/6 p=0.03 vs 4/6 p=0.69; about 25% of items still moved | Clayton, Dally, Emery 2007 (b04) | single (review) |
| Desire-state cache protection in jays | Pilfering experiment n=16 (10 scrub, 6 Eurasian), p<0.001; caching n=16, p=0.006 seen and p=0.003 unseen; seen vs unseen p=0.255 | Ostojic et al. 2017 (b03) | contested (same lab null in 2021) |
| Eurasian jay perspective and desire cues failed to replicate | 14 birds, two colonies, 5 experiments; 4 of 7 directional tests wrong way; Exp 1 W=13 p=0.21; Exp 2 p=0.83; Exp 3 observed vs private median 0.71 vs 0.54 p=0.59; Exp 4 direct replication Z=0.15 p=0.56; Exp 5 p=0.18 | Amodio et al. 2021 (b01, b02, c17) | failed (same lab) |
| Pilferer identity drives re-caching in other corvids | 6 pinyon jays, 5 Clark's nutcrackers; conditions alone, objects, conspecifics, heterospecifics; re-caching fell over 3 blocks; females re-cached more | Vernouillet et al. 2025 (d15) | independent lab, partial, small n |
| Ravens use observer knowledge | Exp 1 (n=6) recovered more near former observers, T=0, p=0.032. Exp 2: time to pilfer about 10x longer with dominant non-observer; subordinate pilfer success 69% (non-observer) vs 12% (co-observer); distance 6 m vs 0.6 m | Bugnyar and Heinrich 2005 (a04, a05) | single lab |
| Knower-guesser differentiation in ravens | Informed vs uninformed, Wilcoxon n=8 p=0.023; partly informed 6/6 non-ties p=0.032; matching caches to competitors 7/7 p=0.016 (uninformed 4/7, p=1) | Bugnyar 2011 (b06) | single lab |
| Ravens guard caches on hearing rivals when peephole open | n=9, chi2(2)=14.889 p<0.001; peephole vs non-observed Z=-2.666 p=0.012; peephole vs observed p=0.08 and p=0.94; peephole geometry p=0.297; stay-treatment 3/5 p=1 | Bugnyar et al. 2016 (a06, b07, b25) | single lab; some tests null |
| Apes look first at the false-belief location | Exp 1 N=40: of 30 who looked, 20 first at target, P=0.098 alone. Exp 2 N=30: 17 of 22, P=0.016. Combined N=29: Z=3.25, P=0.001, r=0.42 | Krupenye et al. 2016 (a09) | contested |
| Submentalizing control weakens it | N=43: only 22 looked at a box (51.2%) vs 22 of 30 (73.3%) originally; first looks 14 of 22, p=0.28; viewing time F(1,37)=0.31 p=0.57 | Krupenye et al. 2017 (a10) | contested |
| Experience control in apes | n=47 (opaque 23, see-through 24), between subjects; opaque P=0.033 and P=0.019 follow-up; see-through P=0.42 | Kano et al. 2019 (b08) | single |
| Apes help the actor with a false belief | Study 1: 76.5% vs 53.1% (U=74.5, N=17 per group, p=.015, r=.42). Study 2: false belief 72.0% (p=.006); ignorance 49.9% (p=.877); difference U=55 p=.027 r=.41 | Buttelmann et al. 2017 (b09, b24) | single, has ignorance control |
| Chimps pick the bigger stick against a rival with a different view | M=60% (t(15)=2.60, p=.02); children 28%; with no preference, random choice | Karg et al. 2016 (b10) | contested (projection of own preference) |
| Monkeys look longer at incorrect search by a knowing agent | Exp 1: 4.34 s vs 3.04 s, t(60)=2.10, p=.04. Horschler 2019: 3.19 vs 2.32 s (n=36 each, p=.04, d=.48); Exp 2: 3.65 vs 2.36 s (n=50 each, p<.001, d=.79). False-belief version: no difference | Martin and Santos 2014; Horschler et al. 2019 (a11, a13) | marginal |
| Monkey effect depends on type of change | Longer after colour change, not size or shape; colour change was detectable | Horschler et al. 2021 (a14) | single |
| Anticipatory looking failed in infants | 160 infants (25 months), 2 sites; original had 20 infants. No evidence of action or belief anticipation; 49 correct first look vs 41 not | Kampis et al. 2021 (d17) | failed (infants) |
| GPT-4 passes 75% of 40 false-belief tasks | 640 prompts; GPT-3.5 and davinci-003 20%; older models 0%; ChatGPT-4 75% (each task needs 16 correct prompts) | Kosinski 2023/2024 (a17, b16, c01) | LLM, single source |
| False-belief pass is brittle | GPT-4 97% on originals, 0% on transparent-access and "inon" categories; P(chocolate) about 87 to 98% when protagonist can see the contents | Ullman 2023; Shapira et al. 2023 (a18, a19, c02, c03) | LLM, established |
| Brittleness persists in 2026 open models | Average accuracy 67.2 unperturbed vs 35.4 transparent container (vanilla); Llama 3 70B 100 to 25; about 8 items per cell | Nickel et al. 2026 (d04) | LLM, established (small cells) |
| Models state belief but do not act on it | SimpleToM: mental state 95.6, behaviour 49.5, judgment 15.3 (GPT-4o); GPT-5 98.5/64.4/40.0; o1 98.6/58.8/32.5; R1 97.3/73.8/65.8 | Gu et al. 2024/2026 (c10, d01) | LLM, established |
| Short reminder lifts behaviour | GPT-4o 49.5 to 82.8; Llama-405B 58.3 to 89.5; Claude-3.5-Sonnet 67.0 to 96.9. 8B model: 28.9 to 63.2 | Gu et al. 2026; Saxena et al. 2026 (d02, d03) | LLM, established |
| Conversation ToM is far harder | FANToM human 87.5; GPT-4 + CoT 26.6 (Jun) or 14.8 (Oct); ChatGPT 3.7; Llama-2 chat 0.4 | Kim et al. 2023 (c06) | LLM, established |
| Perspective filtering helps | SimToM, GPT-3.5 BigToM false belief 41.0 to 70.5 (CoT 56.25); GPT-4 ToMi false belief 25.5 to 87.75 (CoT 74.25) | Wilf et al. 2023 (c07) | LLM, established |
| Symbolic belief tracker helps | ToMi first order +62 points (Flan-T5-XL); second order +78 (GPT-3.5) | Sclar et al. 2023 (c08) | LLM, established |
| Longer thinking can hurt | o3 on HiToM 0.838 (lowest effort) to 0.693 (highest); Qwen3-8B reasoning capped at 1,500 tokens 0.706, above both modes | Gong et al. 2026 (d07) | LLM, single source |
| Option removal changes rankings | HiToM: R1 0.549 to 0.691 without options; Qwen3-8B non-reasoning 0.557 to 0.510 | Gong et al. 2026 (d08) | LLM, single source |

## 4. Mechanisms and models

This section turns the findings into things an engineer could build or test.

### 4.1 The "who saw what" ledger (corvid model)

What the corvid data suggest the animal tracks (a01 to a06, b06):

- For each caching event: who was present, whether each had visual access, and whether each could hear.
- For each individual: past thieving record (identity effects in d15) and rank (dominance mattered in a05).
- A cost estimate: risk of theft times value of item, set against the cost of moving it. In a02 the number cached did not change (3.93 vs 3.57); only re-caching of exposed items did.

An implementable version for an agent:

```
ledger = {}  # item_id -> {"seen_by": set(), "heard_by": set(), "step": int}
on event(item, observers): ledger[item].seen_by |= observers
on decision about item:
    exposure = len(ledger[item].seen_by - trusted)
    if exposure > 0 and value(item) > cost(recheck): recheck_or_move(item)
```

Claim K01 gives the agent test. The evidence is single-source and the same-lab retest failed (section 5), so this stays a design hypothesis, not a rule.

### 4.2 Experience projection

Emery and Clayton: only birds that had stolen re-cached selectively (a03). Machine reading: the model of another agent is a copy of the self-model with the other's inputs swapped in. It matches simulation accounts in LLM work (SimToM below). It predicts failure when the other differs from the self, as when chimps projected their own preference (b10).

### 4.3 Perspective filtering (SimToM, Wilf et al. 2023, c07)

Two calls. Call 1: "State only what person X knows" (filter the story to events X observed). Call 2: answer the question about X using only the filtered story. It targets the failure where the model answers from the full story. Results in section 3. An oracle perspective did better than a model-chosen one (c07, partly read), so the filter step is where errors enter.

### 4.4 Symbolic belief tracking (SymbolicToM, Sclar et al. 2023, c08)

A graph per character holds that character's beliefs, including nested ones (what A believes B believes). A program updates each graph per sentence, from who was present. Only then is the question asked, with the relevant graph pasted in. Code does the bookkeeping; the model reads. It gave +62 and +78 points on ToMi and kept near-perfect scores on non-ToM questions. This follows guardrail G5 (code selects).

### 4.5 State to action: the reminder (Gu et al. 2026, d02)

Two steps: ask the mental-state question, then ask for the behaviour with the model's own state answer shown ("Remember, X does not know Y"). The reminder adds about 2 tokens; generic CoT adds 230 to 298 and helped less (GPT-4o behaviour 62.8 vs 82.8). Judgment questions ("was this reasonable?") gained less, and for Llama-405B stayed near 25 (d02, K14).

### 4.6 Opponent hypothesis loop (Hypothetical Minds, Cross et al. 2024, c16, d12)

A module keeps text hypotheses about the other agent's strategy. Each round: predict the other's next action from each hypothesis, score hypotheses against what happened, refine the best, plan against it. Ablating hypothesis evaluation hurt (c16). An independent team: beats vanilla in 3 games (+6.4, +12.8, +26.0 win-rate points) at about 543,649 tokens per Liar's Dice game, 93.5% of it history (d12). Head to head, the cheaper SAGE won 61.7% in Goofspiel, tied 50.0% in Liar's Dice, and lost 30.0% in Leduc (the SAGE authors re-implemented it and have a rival method).

### 4.7 Perishable memory (ScrubJay-MEM, Bhandari et al. 2026, c15, d13)

Idea from jays that stop re-fetching food that spoils: store each memory with a decay clock and a perishability tag; drop or down-weight stale entries. On the authors' temporal test (20 instances, 1,320 queries) GenGap +0.108 vs about -0.022 for flat retrieval; the decay ablation collapsed GenGap 5.7x. With a stronger backbone a plain retriever caught up (Contriever 78.68 F1 vs 72.82), and decay hurt on conflict resolution (d13). Not independent. Untested for us.

### 4.8 Control-condition design (the main transfer)

From the animal side: pair every "knows" condition with (a) an ignorance condition, (b) a cue-matched condition, (c) an experience control. Buttelmann 2017 is the clean example: false belief 72.0% vs ignorance 49.9% (b24). A rule "go where the actor last saw it" would predict chance on ignorance; the apes matched only the false-belief group. For LLM probes: original, reversed, transparent-access, informed-protagonist and random-label variants (Ullman, Rane c14). Caveat from Tauzin 2025: apes were rewarded in about one third of unpointed ignorance trials, a route to a learned rule (d18).

## 5. What holds up

### 5.1 Animal side

- **Replicated within a lab, mixed.** Emery and Clayton 2001 was repeated at a second site with the same seven birds (0.28 vs 0.08), so it is one dataset (a01).
- **Failed.** The same lab's 2021 test of perspective and desire cues in Eurasian jays: five experiments, 14 birds, 4 of 7 directional tests wrong way, direct replication Z=0.15 p=0.56 (b01, c17). Ostojic 2017 and Legg and Clayton 2014 are weakened (K02).
- **Independent partial support.** Pinyon jays and nutcrackers re-cache by pilferer identity (d15), not desire state. Dally 2006 itself found no evidence that protection is cued by observer behaviour (d14).
- **Ravens.** Bugnyar's lab is the only source. Informed matching 7/7 p=0.016 (2011) but peephole geometry p=0.297 and stay-treatment p=1 (2016). Effects for "who watched" are firmer than for "might be seen". No raven or crow replication outside Vienna was found (d21 is a 2026 corvid development review, abstract only).
- **Apes and looking.** The headline result (P=0.098 in Exp 1) needs the combined test. The submentalizing follow-up gave p=0.28 on first looks. The paradigm failed in 160 infants (d17). Experience-controlled looking (Kano 2019) and active helping with an ignorance control (Buttelmann 2017) are stronger single studies. No pre-registered large ape replication was found.
- **Monkeys.** Looking-time effects are small (d=.48 and .79) and depend on colour versus size changes (a13, a14). The false-belief version showed no difference (a11).
- **Meta-level.** Penn and Povinelli, Heyes and Tauzin (2025, d18) keep showing that learned rules explain the data.
- **Sample sizes.** Founding studies have n=6 to 17 with Wilcoxon and sign tests. Use them for direction, not effect size.

### 5.2 Moderators and boundary conditions

| Moderator | Effect |
|---|---|
| Own experience as thief | Needed in jays (a03) |
| Type of change in the display | Colour yes, size and shape no, in monkeys (a14) |
| Cue availability | Ravens: sound plus open peephole yes; geometry mixed (b07) |
| Rank | Dominant non-observer delayed pilfering about 10x (a05) |
| Sex | Females re-cached more in pinyon jays and nutcrackers (d15) |
| Habituation | Re-caching fell over blocks (d15) |
| Species | Pilferer-identity effects in other corvids, not desire state (d15) |

### 5.3 LLM side

- Established: perturbation drops (K11), state-action gap (K12), conversational difficulty (K13), control design (K18), benchmark inflation (K21).
- Interventions that worked: perspective filtering, symbolic belief graphs, the state reminder.
- Interventions that did not work or were mixed: generic CoT on ToMBench (about 0 gain, c11); extra reasoning effort on HiToM (hurt o3, d07); judgment questions after the reminder (25.8 to 42.2 for several models, c21; Claude 24.9 to 84.1 as an exception, d02).
- Format explains an apparent contradiction: Street 2024 (GPT-4 88.6% vs humans 90.4%, 6th order 93% vs 82%, c09) vs FANToM and SimpleToM. Short written statements versus interactive or applied tasks (K15 contested).

## 6. Language models

### 6.1 Classic false-belief battery

- Kosinski (2023/2024): 40 tasks, 11 models. Older models 0%; davinci-003 and ChatGPT-3.5-turbo 20%; ChatGPT-4 (June 2023) 75%, "matching six-year-olds". Readout is next-word probability (popcorn/chocolate; cat in box/basket) (a17, c01). Reversed version about 99.7%; prefix-only control: popcorn 0%, money 79.5%, gems 23.7% in separate completions (c23).
- Strachan et al. (2024, Nature Human Behaviour): 15 chats per model per test, about 50 humans per test, 1,907 humans overall. False belief at ceiling for humans and LLMs. GPT-4 at or above humans on 3 of 4 task types; faux pas was the exception (GPT-4 endorsed "didn't know" more for faux pas than neutral, chi2(2)=109) (a20, b21, b23). LLaMA2-70B scored above humans on faux pas, but a belief-likelihood analysis suggested bias, not understanding (a20, partly read).
- Sap et al. (2022), few-shot GPT-3: SocialIQa 55%, ToMi 60%, over 30 points below humans on SocialIQa (b20, c04).

### 6.2 Brittleness

- Ullman (2023): content prompt P(popcorn)=100%, first belief prompt P(chocolate)=99% on the original. With a transparent bag the model still says she believes chocolate (about 95 to 98%). Transparent chest: still looks in the old place (90 to 94%). A double-space change shifted chocolate 53% vs 39% (a18, b17, c02). These are different variants; do not average them.
- Shapira et al. (2023): GPT-4 97% on originals, 0% on transparent-access and "inon" adversarial sets; davinci-002 66.7% on transparent access; FauxPas-EAI best model 27%, below a most-frequent-class baseline; probing method matters (a19, c03).
- Nickel et al. (2026): six open 2023-24 models, 1,088 questions, 10 perturbation classes. Average accuracy unperturbed 67.2 (vanilla) and 89.6 (CoT); transparent container 35.4 and 27.1. Llama 3 70B 100 to 25. Cells are about 8 items (d04).
- de Haan et al. (2026a): 14 hand-scored items, 0, 0.5 or 1 each. Claude thinking, Grok-3-mini and R1 all 0.0 on transparent-access and relationship-change variants; GPT-5-high 0.5 on one transparent-access variant, 0 on the other. Non-reasoning Claude lost points on 1A, 1B, 1D, 2C (d05). Reasoning shrinks failures but does not remove them.
- No study runs one current model on Kosinski items and perturbed items with the same scoring (K20).

### 6.3 State versus action

SimpleToM (1,147 stories, 3,441 questions, 21 LLMs, 95% CI about +-2.7; d01). Models tested run from mid-2024 to Aug 2025.

| Model | Mental state | Behaviour | Judgment |
|---|---|---|---|
| GPT-4o | 95.6 | 49.5 | 15.3 |
| Claude-3.5-Sonnet | 97.9 | 67.0 | 24.9 |
| GPT-4.5-preview | 97.0 | 67.8 | 26.7 |
| o1 | 98.6 | 58.8 | 32.5 |
| o3-mini | 85.4 | 66.8 | 41.3 |
| GPT-5 | 98.5 | 64.4 | 40.0 |
| DeepSeek-R1 | 97.3 | 73.8 | 65.8 |
| o1-preview | 95.6 | 84.1 | 59.5 |

With the reminder: behaviour GPT-4o 49.5 to 82.8; Llama-405B 58.3 to 89.5; Claude-3.5-Sonnet 67.0 to 96.9. Judgment: GPT-4o 15.3 to 42.2; Claude 24.9 to 84.1; Llama-405B stays near 25 (d02). An independent lab on small models: Llama-3.1-8B overall 51.5, recognition 99.4, behaviour 28.9; reminder 63.2; reminder plus their training method (BSTTT) 69.7 (+40.8); GPT-oss-20B judgment 3.1 to 18.7 or 26.8. On OpenToM, Llama ICL 56.4% beat BSTTT 43.1% (d03). Hagendorff: first-order deception 97 to 99%, second-order only 11.67% (false recommendation) and 62.08% (false label) (c12). No 2026 frontier model has been tested on SimpleToM.

### 6.4 Interactive and higher-order tasks

- FANToM: human ALL 87.5; GPT-4 0613 + CoT 26.6 (June) or 14.8 (October); ChatGPT 3.7; Llama-2 chat 0.4 (c06). Humans were 11 students; models trail by over 70 points on average (b19).
- BigToM (Gandhi et al. 2023): GPT-4 forward belief .97 to .99; backward false belief .53 (true belief .86); humans 82% and 72%; one-shot CoT lifts backward false belief (c05).
- ToMBench (Chen et al. 2024): human 85.4 vs GPT-4-1106 75.3 (gap 10.1); CoT adds about nothing (72.8 vs 73.5) (c11).
- Street et al. (2024): humans 90.4% on ToM statements; GPT-4 88.6; Flan-PaLM 84.3; GPT-3.5 52.5; PaLM 59.3; LaMDA 50; 6th order GPT-4 93% vs humans 82% (c09).

### 6.5 What changed performance, by how much

| Change | Size | Where |
|---|---|---|
| Perspective filter (SimToM) | +29.5 (GPT-3.5, BigToM), +62.2 (GPT-4, ToMi) over 0-shot; +14.2 and +13.5 over CoT | c07 |
| Symbolic belief graph | +62 (first order), +78 (second order) | c08 |
| State reminder (about 2 tokens) | Behaviour +33 (GPT-4o), +31 (Llama-405B), +30 (Claude) | d02 |
| Generic CoT (230 to 298 tokens) | GPT-4o behaviour 62.8, below reminder 82.8 | d02 |
| CoT on ToMBench | about 0 | c11 |
| More reasoning effort (HiToM, o3) | -14.5 points (0.838 to 0.693) | d07 |
| Token cap 1,500 (Qwen3-8B reasoning) | 0.706, above both modes | d07 |
| Adaptive stop (R1-Distill-Qwen-32B) | 0.571 to 0.701 on HiToM; negligible on ToMBench | d07 |
| Remove answer options (HiToM) | R1 +14.2; Qwen3-8B reasoning +14.8 (0.481 to 0.629); Qwen3-8B non-reasoning -4.7 | d08 |
| Opponent hypotheses (Hypothetical Minds) | +6.4 to +26.0 win-rate points over vanilla in 3 games | d12 |
| EnigmaToM on ToMi (Gemma2-27B) | vanilla 0.767, SimToM 0.749, EnigmaToM about 0.79 to 0.87; tokens not reported | d10 |

### 6.6 Evaluation lessons

- Rane et al. (2025, ICML position): GPT-4o on ranked-animal prompts 0.97, reverse ranked 0.78 (SD .20), random string 0.92 (SD .09), trial-based n-term 0.40 (about chance). Control conditions shift scores by more than many reported model gaps (c14).
- ToM-RL (Lu et al. 2025): high accuracy in small RL-trained models with collapsed one-line reasoning; scale-dependent (7B good traces, 3B collapse) (d09).
- OmniToM (Bawatneh et al. 2026): 895 stories, 22,343 labelled belief propositions, seven label dimensions. Model scores not extracted (d11).
- Hu, Sosa and Ullman (2025) argue for re-evaluating ToM tests; no new accuracy numbers (c13).

### 6.7 Corvid-inspired AI

ScrubJay-MEM (4.7) and the Hypothetical Minds scaffold (4.6) are the corvid-style and opponent-model systems found. Both have author-reported gains; Hypothetical Minds has one independent re-run (partial, rival author); ScrubJay-MEM's gain shrinks with a stronger backbone.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | **Adversarial variants before trusting a social or belief answer.** For any "what does X know" item in checked mode, build one variant where access is changed (transparent, informed) and require the answer to change correctly. | G (extends G3) | [E] | a18, a19, c02, c03, d04, d05, K11 |
| 2 | **Apply the state to the action.** After the agent writes what a party knows, the next step must use that written state to answer the action question. Use a short reminder, not a long CoT. | S (apply step) / O | [E] | c10, d01 to d03, K12 |
| 3 | **Perspective filter operator.** Before answering about party X, restrict the context to what X observed. Do it in code where possible. | O | [E] | c07, c08, d02, K14 |
| 4 | **Do not trust a single question type.** Ask the same fact in several forms (state, action, judgment) and accept only consistent sets. | G | [E] | c06, c05, c11, K13 |
| 5 | **Controls in every probe.** Original, reversed, random or cue-matched variants; write the low-level alternative explanation beside each social inference. | G | [E] | c14, d07 to d09, a16, K09, K18, K21 |
| 6 | **Inspect traces and drop options when scoring belief tasks.** Score the written belief state against a gold list; run once without answer options. | G (extends G10) | [E] | d08, d09, d11, K21 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 7 | Per-party belief ledger kept in code vs SimToM filter, at equal tokens | O / memory | [S] | c08, c07, d10 (no equal-token study) |
| 8 | Token cap on the social-reasoning step (about 1,500) vs default | G11, S | [S] | d07, K19 |
| 9 | Opponent-hypothesis loop in multi-party tasks | O | [C] | c16, d12, K16 |
| 10 | "Exposed item" flag: re-verify items whose content was shared | memory / G | [S] | a01 to a03, K01 |
| 11 | Perishability tag on lessons | memory | [S] | c15, d13, K17 |
| 12 | Ignorance-versus-false-belief contrast items | G | [S] | b09, b24, K06 |

What not to take: any rule that rests on a single animal result (K02, K05, K07). Corvid findings are hypotheses until replicated by an independent lab.

## 8. Concrete tests on our bench

Both arms get the same token budget, including setup cost (G7). If our bench has no social items, build them from SimpleToM, ToMi and FANToM style stories.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | SimpleToM-style two-sentence stories (behaviour question) | Plain vs "state then reminder" vs plain with generic CoT padded to the same tokens | Behaviour accuracy; state-to-action gap | Reminder +20 to +30 points over plain; beats CoT by about 10 or more (d02) |
| T2 | ToMi and BigToM false-belief items | Plain vs SimToM filter vs code-kept belief ledger in the prompt | Accuracy per arm, tokens logged | Filter and ledger both beat plain; ledger at least equal to filter (K14 gap) |
| T3 | Kosinski items plus Ullman variants (transparent access, informed protagonist, reversed) | Plain vs plain plus perturbation check | Original accuracy, perturbed accuracy, drop | Plain drops over 20 points on perturbed; check arm flags the failures |
| T4 | HiToM-style higher-order items | Default effort vs 1,500-token cap vs adaptive stop | Accuracy at equal tokens | Cap arm not worse, better per token (d07) |
| T5 | Same items with and without answer options | Options vs free-form scored by gold belief list | Accuracy delta; ranking change | Delta of 5 to 15 points that flips a ranking in some pairs (d08) |
| T6 | Multi-party tracking: three parties, items shared or private | Plain vs exposure flag plus re-verify | Errors on exposed vs private items; tokens | Fewer errors on exposed items with no token rise (K01) |
| T7 | Two-player repeated game (Liar's Dice or Goofspiel style) | Plain vs hypothesis loop vs cheap structured agent | Win rate per 1,000 tokens | Loop beats plain on win rate; loses per token to the cheap agent (d12) |
| T8 | Ignorance vs false-belief contrast items | Plain vs rule prompt "go where last seen" | Accuracy in both conditions | Plain passes both; rule prompt passes false belief, fails ignorance (b24) |
| T9 | Lesson store with perishability tag | Flat lessons vs lessons with decay | Held-out accuracy, conflict items | Gain on temporal items; none or negative on conflict items (d13) |

## 9. What does not transfer, and why

- **Cache protection as a policy.** Our agent has no thieves. Only the abstract "exposed information" idea carries over, and it rests on a same-lab single result (K01).
- **Desire-state and perspective effects in jays.** They failed to replicate in the original lab (K02).
- **Looking-time and eye-tracking results.** An LLM has no gaze. The paradigm failed an infant replication (d17).
- **Statistical effect sizes from animals.** n=6 to 17. They give direction only.
- **Evolutionary claims** (convergent evolution, Machiavellian intelligence). No bearing on a scaffold.
- **"Passes as well as a six-year-old."** Different format, no developmental trajectory in a model (a17).
- **Human-like belief states in LLMs.** Passing a stated test does not show the state is used (K12, K21).
- **Hypothetical Minds as a free gain.** At about 543,649 tokens per game it fails G7 unless it wins per token (d12).
- **ScrubJay-MEM gain.** Not independent, and it shrinks with strong backbones (d13).

## 10. Open questions

1. Do 2026 frontier models still show the state-versus-behaviour gap, and does a short reminder close it at equal tokens? (d01 covers models to Aug 2025.)
2. Does a code-kept belief ledger beat a SimToM filter at equal tokens?
3. How large is the perturbation drop for current reasoning models on the same items as Kosinski?
4. Any independent replication of Ostojic 2017 desire-state protection? Did Dally 2006 stand? (Full texts not opened.)
5. Do Bugnyar's raven results replicate outside Vienna?
6. What does a pre-registered large ape replication of Krupenye 2016 show, with the submentalizing control?
7. Does Hypothetical Minds hold its gain with independent evaluators on Melting Pot style tasks?
8. Does perishable memory help on an independent benchmark against a recency baseline?
9. Do control conditions change which social-reasoning claims survive across model versions?
10. Does reasoning effort raise or lower social accuracy by task order? o3 on HiToM fell with effort; first-order ToMBench showed no gain (d07).

## 11. Sources

[V] opened by an agent. [M] snippet or title only.

Animal studies and reviews
- [V] Emery and Clayton (2001) Effects of experience and social context on prospective caching strategies by scrub jays. https://gwern.net/doc/psychology/animal/bird/2001-emery.pdf
- [V] Clayton, Dally and Emery (2007) Social cognition by food-caching corvids. https://pmc.ncbi.nlm.nih.gov/articles/PMC2346514/
- [V] Dally, Emery and Clayton (2006) Food-caching western scrub-jays keep track of who was watching when (abstract only). https://doi.org/10.1126/science.1126539
- [M] Emery and Clayton (2004) The mentality of crows. https://doi.org/10.1126/science.1098410
- [V] Ostojic et al. (2017) Current desires of conspecific observers affect cache-protection strategies in California scrub-jays and Eurasian jays. https://pmc.ncbi.nlm.nih.gov/articles/PMC5266788/
- [V] Amodio et al. (2021, eLife) Little evidence that Eurasian jays protect their caches by responding to cues about a conspecific's perspective and desire. https://pmc.ncbi.nlm.nih.gov/articles/PMC8536255/
- [V] Vernouillet, Huang and Kelly (2025) Pinyon jays and Clark's nutcrackers re-cache by pilferer identity. https://pmc.ncbi.nlm.nih.gov/articles/PMC11870924/
- [V] Bugnyar and Heinrich (2005) Ravens differentiate between knowledgeable and ignorant competitors. https://pmc.ncbi.nlm.nih.gov/articles/PMC1559847/
- [V] Bugnyar (2011) Knower-guesser differentiation in ravens. https://pmc.ncbi.nlm.nih.gov/articles/PMC3025684/
- [V] Bugnyar, Reber and Buckner (2016) Ravens attribute visual access to unseen competitors. https://www.nature.com/articles/ncomms10506 and https://pmc.ncbi.nlm.nih.gov/articles/PMC4740864/
- [M] Hare, Call, Agnetta and Tomasello (2000) Chimpanzees know what conspecifics do and do not see. https://doi.org/10.1006/anbe.1999.1377
- [M] Hare, Call and Tomasello (2001) Do chimpanzees know what conspecifics know? https://doi.org/10.1006/anbe.2000.1518 and https://www.eva.mpg.de/documents/Elsevier/Hare_Chimpanzees_AnimalBeh_2001_1556063.pdf
- [M] Hare et al. (2002) capuchin monkeys. https://evolutionaryanthropology.duke.edu/sites/evolutionaryanthropology.duke.edu/files/site-images/Hare%20et%20al_%202002_%20Do%20capuchin%20monkeys%20know%20what%20conspecifics%20do%20and%20do%20not%20see.pdf
- [M] Krachun et al. (2009) chimpanzee visual perspective. https://pure.mpg.de/pubman/item/item_1552968_3/component/file_2225457/Krachun_Chimpanzees_AnimCog_2009.pdf
- [M] Call and Tomasello (2008) Does the chimpanzee have a theory of mind? 30 years later. https://doi.org/10.1016/j.tics.2008.02.010
- [V] Penn and Povinelli (2007) On the lack of evidence that non-human animals possess anything remotely resembling a theory of mind. https://pmc.ncbi.nlm.nih.gov/articles/PMC2346530/ (also listed as [M] via a21, https://doi.org/10.1098/rstb.2006.2004)
- [V] Heyes (2015) Animal mindreading: what's the problem? https://users.ox.ac.uk/~ascch/Celia's%20pdfs/2%20Heyes%202015%20AMR.pdf
- [V] Krupenye, Kano, Hirata, Call and Tomasello (2016) Great apes anticipate that other individuals will act according to false beliefs. https://sites.duke.edu/tomasellolabduke/files/2016/09/KrupenyeKanoHirataCallTomasello_2016_Science.pdf (also https://doi.org/10.1126/science.aaf8110, [M])
- [V] Krupenye et al. (2017) A test of the submentalizing hypothesis in apes. https://pmc.ncbi.nlm.nih.gov/articles/PMC5595417/
- [V] Kano et al. (2017) Eye tracking uncovered great apes' ability to anticipate that other individuals will act according to false beliefs. https://pmc.ncbi.nlm.nih.gov/articles/PMC5398232/
- [V] Kano, Krupenye, Hirata, Tomonaga and Call (2019) Great apes use self-experience to anticipate an agent's action. https://pmc.ncbi.nlm.nih.gov/articles/PMC6800361/ and https://doi.org/10.1073/pnas.1910095116
- [V] Krupenye and Call (2019) Theory of mind in animals: current and future directions. https://doi.org/10.1002/wcs.1503
- [V] Buttelmann, Buttelmann, Carpenter, Call and Tomasello (2017) Great apes distinguish true from false beliefs in an interactive helping task. https://pmc.ncbi.nlm.nih.gov/articles/PMC5381863/
- [V] Karg, Schmelz, Call and Tomasello (2016) Differing views. https://pmc.ncbi.nlm.nih.gov/articles/PMC4824821/
- [V] Chimpanzees gesture to humans in mirrors. https://pmc.ncbi.nlm.nih.gov/articles/PMC5877477/
- [V] Martin and Santos (2014) Monkeys represent others' knowledge but not their beliefs. https://pmc.ncbi.nlm.nih.gov/articles/PMC3970702/
- [V] Horschler, MacLean and Santos (2019) Do non-human primates really represent others' beliefs? https://pmc.ncbi.nlm.nih.gov/articles/PMC6570545/
- [M] Horschler, MacLean and Santos (2020) summary. https://experts.arizona.edu/en/publications/do-non-human-primates-really-represent-others-beliefs/
- [V] Horschler et al. (2021) How do non-human primates represent others' beliefs (abstract level). https://pmc.ncbi.nlm.nih.gov/articles/PMC8154671/
- [V] Kampis et al. (2021) A two-lab direct replication attempt of Southgate et al. (2007). https://pmc.ncbi.nlm.nih.gov/articles/PMC8386515/
- [M] Kulke, Reiss, Krist and Rakoczy (2018) Implicit false belief. https://doi.org/10.1016/j.cogdev.2017.08.006
- [V] Tauzin (2025) Communicative mentalization is limited in nonhuman primates. https://pmc.ncbi.nlm.nih.gov/articles/PMC12130812/
- [M] Development of cognition in corvids (2026, Anim Cogn), 47 studies, 16 species. https://pmc.ncbi.nlm.nih.gov/articles/PMC13722769/
- [M] Pang et al. (2025) commentary on animal-cognition methods for AI. https://pmc.ncbi.nlm.nih.gov/articles/PMC12280963/

LLM and AI studies
- [V] Kosinski (2023/2024) Evaluating large language models in theory of mind tasks. https://arxiv.org/abs/2302.02083
- [V] Ullman (2023) Large language models fail on trivial alterations to theory-of-mind tasks. https://arxiv.org/abs/2302.08399
- [V] Shapira et al. (2023) Clever Hans or Neural Theory of Mind? https://arxiv.org/abs/2305.14763
- [V] Sap, Le Bras, Fried and Choi (2022) Neural Theory-of-Mind? https://arxiv.org/abs/2210.13312
- [V] Strachan et al. (2024) Testing theory of mind in large language models and humans. https://www.nature.com/articles/s41562-024-01882-z and https://pmc.ncbi.nlm.nih.gov/articles/PMC11272575/
- [V] Gandhi, Franken, Gerstenberg and Goodman (2023) Understanding social reasoning in language models with language models (BigToM). https://arxiv.org/abs/2306.15448
- [V] Kim et al. (2023) FANToM. https://arxiv.org/abs/2310.15421
- [V] Wilf et al. (2023) Think Twice: perspective-taking improves LLM theory of mind (SimToM). https://arxiv.org/abs/2311.10227
- [V] Sclar et al. (2023) Minding language models' (lack of) theory of mind (SymbolicToM). https://arxiv.org/abs/2306.00924
- [V] Street et al. (2024) LLMs achieve adult human performance on higher-order theory of mind tasks. https://arxiv.org/abs/2405.18870
- [V] Gu et al. (2024; ICLR 2026) SimpleToM. https://arxiv.org/abs/2410.13648
- [V] Chen et al. (2024) ToMBench. https://arxiv.org/abs/2402.15052
- [V] Hagendorff (2023/2024) Deception abilities emerged in large language models. https://arxiv.org/abs/2307.16513
- [V] Hu, Sosa and Ullman (2025) Re-evaluating theory of mind evaluation in large language models. https://arxiv.org/abs/2502.21098
- [V] Rane et al. (2025) Principles of animal cognition for LLM evaluations. https://amandaroyka.github.io/icml2025.pdf
- [M] Ma et al. (2023/2024) Towards a holistic landscape of situated theory of mind. https://arxiv.org/abs/2310.19619
- [V] Bhandari et al. (2026) Caching for the Future: Scrub Jay episodic memory (ScrubJay-MEM). https://arxiv.org/abs/2608.04746
- [V] Cross et al. (2024; ICLR 2025) Hypothetical Minds. https://arxiv.org/abs/2407.07086
- [V] Saxena, Janzen and Maass (2026) Diagnosing the explicit-to-applied gap. https://arxiv.org/abs/2610.31060
- [V] Nickel, Schrewe, Mai and Flek (2026) Understanding artificial theory of mind. https://arxiv.org/abs/2602.22072
- [V] de Haan, van der Putten and van Duijn (2026a) Reasoning promotes robustness in ToM. https://arxiv.org/abs/2601.16853
- [V] de Haan et al. (2026b) Evaluating theory of mind in reasoning models (abstract and introduction). https://arxiv.org/abs/2608.04646
- [V] Gong et al. (2026) To think or not to think. https://arxiv.org/abs/2602.10625
- [V] Lu, Zhang, Song, Fan and Wang (2025) Do theory of mind benchmarks need explicit human-like reasoning? (abstract) https://arxiv.org/abs/2504.01698
- [V] EnigmaToM (2025) Improve LLMs' theory-of-mind reasoning capabilities. https://arxiv.org/abs/2503.03340
- [V] Bawatneh et al. (2026) OmniToM. https://arxiv.org/abs/2605.26322
- [V] Chen et al. (2026) SAGE. https://arxiv.org/abs/2609.34342

Provenance caution: several arXiv ids above (26xx.xxxxx) are as recorded by the research agents; confirm before citing outside this folder.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 8 established claims: 6 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A18.06-K08** (unverifiable). PMC pages blocked by captcha; only the Horschler 2021 abstract (colour change yes, size/shape no) was reachable; the 4.34 vs 3.04 and 3.65 vs 2.36 numbers could not be checked, and PMC3970702 appears to be Marticorena et al. 2011 (Dev Sci), not Martin and Santos 2014 as labelled.
- **A18.06-K12** (reworded: the sources support less). Hagendorff reports GPT-4 second-order deception of 11.67% for false recommendation but 62.08% for false label (and 70% with step-by-step prompting), so 'second-order only 11.67%' picks the lowest of the reported results; SimpleToM and Saxena numbers check out. Corrected claim: LLMs state awareness but do not apply it: SimpleToM mental-state question over 95% for GPT-4o, Llama-3.1-405B, Claude-3.5-Sonnet; behaviour prediction at least 30 points lower; judgment 10-25%. Hagendorff: GPT-4 first-order deception 97-99% but second-order only 11.67% (false recommendation) and 62.08% (false label). SimpleToM v2 (ICLR 2026) shows the gap in GPT-5 (state 98.5, behaviour 64.4, judgment 40.0), o1 (98.6/58.8/32.5), o3-mini (85.4/66.8/41.3); R1 (97.3/73.8/65.8) and o1-preview (95.6/84.1/59.5) are best. The reminder lifts behaviour to 82.8-96.9 for three non-reasoning models; an independent lab sees the same on 8B models (28.9 to 63.2).
- **A18.06-K03** (now single-source: only one opened source, code check).
