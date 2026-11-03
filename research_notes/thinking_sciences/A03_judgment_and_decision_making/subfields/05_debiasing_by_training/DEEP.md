# Debiasing by training: deep document

*Subfield A03.05. Built from evidence_a-d.jsonl (a01-a26, b01-b30, c01-c25, d01-d19), claims.jsonl (K01-K27) and critique.md in this folder. Evidence ids are cited in brackets. "Opened" means the page or PDF text was read in this study; second-hand items are marked.*

## 1. What it is

Debiasing by training means teaching a decision maker, once, to avoid a known judgment error, and then checking that the error is lower later and in new settings. In people the training is a lecture, a video, a computer game, a workshop or a rule course. The error is a bias such as anchoring, confirmation bias, the fundamental attribution error (FAE), sunk cost or base-rate neglect.

The question for us is narrow. Our agent is a scaffold with no weight training (SCHEMA.md G7, section 4b). So we ask: what is the active ingredient in training that works in people, and can a prompt, a stored lesson or an in-run error log supply it?

The headline human result is Morewedge et al. (2015). One 60-minute game with personal feedback and practice cut six biases by 32-46% at once and 24-35% two to three months later [a01, a02, d05]. Warnings and awareness alone did not do that [a04, b04, b09]. This is the main support for the schema line "feedback plus practice, not warnings".

Three honest limits frame everything below.
- The human anchor is one research group (Morewedge, Sellier, Scopelliti). No independent replication was found [K26, d01, d03, d04].
- No LLM study copies the human design: repeated own-error feedback over rounds, then a delayed retest [K20, a23].
- Most LLM numbers come from 7B-70B models and 2023-2024 versions. Frontier models often have low baseline bias, so room to improve is small [critique].

## 2. History and theories in depth

**Fischhoff (1982), "Debiasing".** The founding review (book chapter; not opened, known only through Morewedge 2015 [a08, b26]). It sorted debiasing into four procedures, in rising strength:
1. Teach the person that the bias exists.
2. Teach its direction (does it push estimates up or down).
3. Give feedback on the person's own responses.
4. Extended feedback with coaching, intervention and mitigation strategies.

Warning alone gave little or no reduction. Morewedge et al. call the start of the field "rocky" [a05, a08].

**Rule training and everyday reasoning.**
- Nisbett, Fong, Lehman and Cheng (1987), Science 238:625-631. Brief formal training in statistical rules raised use of those rules on everyday-event problems. Graduate study in law, medicine and psychology raised it by field. Only the abstract was read; no N or effect sizes are on file [a07, b25]. Treat the numbers as unknown; the direction is stable in later work.
- Larrick, Morgan and Nisbett (1990). Brief cost-benefit training (sunk-cost and opportunity-cost rules) changed answers on new content. Study 2: trained people chose the normative answer 44% of the time against 28.6% untrained, t(87)=4.77, p<.01; trap answers 30.1% vs 38.6%, p<.05. A phone follow-up of 40 trained and 40 untrained showed some self-reported behaviour change [b08, opened].
- Sedlmeier and Gigerenzer (2001): teaching people to build natural-frequency representations beat teaching Bayes' rule on immediate learning and retention. Snippet only [b28].

**Consider-the-alternative.** Hirt and Markman (1995): explaining more than one possible outcome reduces bias. Abstract only; exact numbers unread; the paper is known for a plausibility moderator (the alternative must be plausible) [a09, critique]. Branchini et al. (2023): a short "think in opposites" training raised the share of people who found the 2-4-6 rule and sped discovery, mainly by getting them to test descending triples [d13].

**The backfire theory.** Sanna, Schwarz and Stocker (2002): listing 10 ways an event could have turned out otherwise increased hindsight bias; listing 2 did not. The felt difficulty of generating many alternatives was read as "few alternatives exist". Sanna and Schwarz (2003) replicated with brow contraction as a body difficulty cue [d11, d12]. So "more alternatives" is not monotone good.

**Skeptics.** Arkes (1991), Milkman, Chugh and Bazerman (2009) and Kahneman argue training teaches people to fix bias only when prompted, may be a Hawthorne effect, and can interfere with useful heuristics. Known second-hand through Sellier et al. [b27, K21]. Morewedge (2015) itself notes that expertise often fails to transfer: logic-trained philosophers show moral reversals, physicians show framing reversals, forecasters are calibrated in domain but overconfident outside [a06].

**The modern turn.**
- Morewedge et al. (2015): the IARPA-funded game vs video test [a01-a05, b01-b04].
- Mellers et al. (2014) and Chang et al. (2016): short probability training in forecasting tournaments [a11, b07].
- Sellier, Scopelliti and Morewedge (2019): field transfer to an unannounced business case [b05, b06, d01-d03].
- Heerma van Voss et al. (2025): national risk analysts [b12, d04].
- 2023-2026: LLM work. It splits into (a) prompt-level debiasing and self-rewrite loops (BiasBuster, SACD), (b) activation steering, (c) weight training that makes a bias cue non-predictive (EIT), and (d) human-intervention procedures turned into prompts (DIY). See section 6.

## 3. Core findings with exact numbers

Status key: E = established (two or more independent sources), S = single source or single group, C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| One-shot game cuts three biases (blind spot, confirmation, FAE) | Exp 1: bias -46.25% (game) vs -18.60% (video) at once; -34.76% vs -20.10% at 8 weeks. d pre-post 1.68 vs 0.69; pre-follow-up 1.11 vs 0.66. 243 lab, 196 follow-up | Morewedge 2015 [a01, b01] | S (one group) |
| Same for anchoring, projection, representativeness | Exp 2: -31.94% (game) vs -25.70% (video) at once; -23.57% vs -19.20% at 12 weeks. d 1.74/1.75 pre-post; 1.16/1.07 pre-follow-up. 238 lab, 192 follow-up | Morewedge 2015 [a02, b01] | S |
| Abstract ranges are minima across both experiments | games at least -31.94% at once, at least -23.57% later; videos at least -18.60%, -19.20% | critique item 2 | S |
| Game beats video only for some biases | Exp 1 d game/video: blind spot .98/.49; FAE 1.12/.38; confirmation 1.09/.38. Exp 2: anchoring .70/.80; representativeness 1.51/1.80 (video equal or better); projection 1.11/.49 | [b02, b03] | S |
| Confirmation effect decays most | pre-follow-up d .58 game vs .26 video (from 1.09/.38 at once); roughly halved over 8 weeks | [b02] | S |
| Knowing is not debiasing | Bias knowledge Exp 2: game 35.89 -> 63.16 -> 50.65; video 39.03 -> 74.11 -> 52.04. Video beat game on knowledge at once (F(1,235)=11.07) but not on bias; equal by follow-up | [a04, b04] | S |
| Transfer inside a bias | Untrained confirmation facets: d=.79 post, .65 follow-up; trained facets .78 and .24 | [a03, b04] | S |
| Components are confounded | Game variants (scores, hints, narrative, first round only) did not differ: Exp 1 F<=2.29, p>=.13; Exp 2 t<=1.77, p>=.08 | [d05] | S |
| Field transfer, MBA students | N=290 (182 trained, 108 not). Chose to race 58.8% vs 72.2%; b=-.60, exp(b)=.549, CI [.33,.92], p=.022; 19% relative drop (not 29%: corrected, see section 5) | Sellier 2019 [b05, d01] | S |
| Mechanism of field effect | Confirming arguments 1.45 vs 2.07, d=.39, p=.001; disconfirming 1.23 vs 1.08 n.s.; confidence lower, b=-.43, p=.017 | [b06] | S |
| No decay in field | 11-day lag (n=125) vs 43-52-day lag (n=57): 56.8% vs 63.2% chose race, p=.419 | [b06, d02] | S, low power |
| Analysts and students, pre-post | Analysts N=71, students N=118. General domain F(1,168)=104.58, partial eta2=.384; risk domain F=46.0, eta2p=.215; no group x training interaction. No untrained control | Heerma van Voss 2025 [b12, d04] | S |
| Forecasting training | Brier gain 10-11% (yr 1, n=119/113 vs 152), 12% (yr 2, t(395)=5.95), 6% (yr 3, p=.021), 7% (yr 4, p=.028). Indirect via practice -0.02 | Chang 2016 [b07] | E (with Mellers 2014) |
| Rule training generalises | Normative answers 44% vs 28.6%; trap 30.1% vs 38.6% | Larrick 1990 [b08] | E (with Nisbett 1987, abstract only) |
| Limit by bias type | N=154, 10 biases, 4 weeks; gains only on statistical-principle biases; awareness alone did not help others | Aczel 2015 [b09] | E |
| One-shot workshop on developer anchoring | d=1.19 without vs 0.72 with workshop; N=410 developers; spread fell about 3x | Shepperd 2018 [a12] | S, quasi-experiment |
| Cognitive forcing often fails | Doctors n=76: 2.8 vs 3.1 correct, CI -0.94 to 0.45; AI-advice studies n=281, 373: delay or slowing did not stop biased advice | [b10, b11] | E |
| Listing many alternatives backfires | 10 alternatives raised hindsight bias; 2 did not | Sanna 2002/2003 [d11, d12] | S (one lab, two papers) |
| LLM: SACD loop | FOMC Llama-3.1-8B bias 0.3805 -> 0.1570; GPT-4o 0.3650 -> 0.0300 (self-help 0.0625, few-shot debias 0.7350) | Lyu 2025 [a14, b17, d08] | S |
| LLM: generic prompts weak | CoT range 0.2470-0.6150; debate 0.5020 (Llama-8B), 0.5155 (GPT-3.5); Reflexion 0.5585 (Llama-70B PubMedQA) | [a15, c03, a22] | E |
| LLM: family-dependent | Prompt debias +40.5% position independence, -4.4% judgment accuracy, -1.1% info processing, +5.9% social | CogBias [a19, d15] | E (with Rethinking-prompt paper) |
| LLM: anchoring is shallow | Llama-3.1-8B 34.7% anchored; Anti-DP two-phase 24.7%; knowledge enhancement 50.5% (worse); self-improving 38.4% | Huang 2026 [a16, b16] | E for "CoT/ignore-anchor do not fix" (Lou and Sun too) |
| LLM: opposite-testing | Rule discovery 42% -> 56% over 11 LLMs; Think-in-Opposites better in all, Dual-Goal in 8 of 11; significant only for thinking models | Jhaveri 2026 [c15, d10] | S |
| LLM: weight training on cue | Qwen3-4B adversarial accuracy 70.1 -> 83.3; unseen distraction robustness 40.6% -> 79.7% (+39.1); position cue 38.6 -> 36.4 (no transfer) | Wang 2026 [b19, d14] | S |
| LLM: human procedures as prompts | Mean bias as low as 2% at 90% reasoning accuracy; up to 14.8 pp on unseen dimensions; REVISE gained +14.98 pp on one benchmark; SHOW alone -2.34 | Raj 2026 [a20, d16] | S |

## 4. Mechanisms and models

An engineer can implement the mechanisms below. Each is stated with the evidence for what carries the effect.

**4.1 The four-step training ladder (Fischhoff, as used by Morewedge).** Four ingredients: name the bias; say which way it pushes; give feedback on the learner's own answer; extended feedback with coaching and mitigation tips. The game had all four plus adaptive practice (5 confirmation judgments with immediate feedback in Exp 1; up to 16 adaptive questions in Exp 2). The video had the first two plus tips, passively [a05, d05]. Nobody has ablated the four. The game also differs in length (60 vs 30 min), coaching and interactivity, so "feedback" is not isolated [K23].

Agent form (a design, not tested): a lesson store with, per bias, a short definition, the direction of effect, and one worked case in which an earlier wrong answer sits next to the corrected answer with a one-line reason. Fire it only when a cue is present (G1). See K01, K20.

**4.2 Why the field effect worked: fewer confirming arguments.** Trained students did not argue more for the other side. They argued less for their favoured option (1.45 vs 2.07) and were less confident [b06]. Mechanism: reduced one-sided search, not added disconfirmation. The intervention term fell to p=.509 once argument counts were in the model [d02], which fits full mediation. Agent form: when a decision is made, count the evidence items written for each option; flag lopsided counts in code. This is a code check, in line with "code counts, model fills slots" (SCHEMA section 1).

**4.3 Detect, analyse, rewrite (SACD).** The loop (Lyu et al. 2025):
1. Determine: does the prompt contain a bias? (yes/no)
2. Analyse: name the bias and where it sits in the text.
3. Rewrite the prompt without it.
4. Repeat until no bias is found, max 3 iterations.

Ablation on GPT-3.5, average bias, SACD / without determination / without analysis / without both (= one self-help rewrite): FOMC 0.1175 / 0.1890 / 0.2370 / 0.3490; PubMedQA 0.0560 / 0.3030 / 0.2660 / 0.2880; LegalBench 0.0965 / 0.2180 / 0.3020 / 0.4590 [d06]. Iteration curve on finance: vanilla 0.1648, iteration 1 0.2070 (worse), iteration 2 0.1460, iteration 3 0.1175 [d07]. Compute is not matched: SACD costs several calls. The same LLM judges the bias, and the bias score is the authors' own metric [b17].

**4.4 Self-help (one-pass rewrite).** One extra pass: "rewrite this prompt to remove bias cues". Best simple baseline in BiasBuster: GPT-4 framing gap -0.405 baseline vs -0.010 with self-help (a gap in admission rates, in points, not "percent more students"); awareness -0.470, contrastive -0.410, counterfactual -0.570 [b14, critique 5]. It needs a strong model: Llama-2 changed 40-52% of sequential decisions when asked to debias, i.e. it over-corrected [a25].

**4.5 Make the cue non-predictive (EIT).** Weight training only. Reward correct answers; make a bandwagon claim right half the time and wrong half the time, so the cue carries no signal. Include cases where the cue is right: wrong-only training taught a shortcut (bandwagon wrong-bias 63.6 -> 84.2 but correct-bias 90.4 -> 71.2) [d14]. Without the independence reward, wrong-bias robustness fell 80.0 -> 65. Scaffold analogue: S1 input hygiene should treat a cue as evidence of unknown validity, not as always wrong.

**4.6 Axiomatic cues (PROBE-SWE).** Elicit best-practice axioms for the decision domain first, then inject them. Median bias sensitivity: baseline 12.9%; CoT 16.1%; impersonated self-debiasing 10.2%; imperative 10.3%; both 8.3% (no per-bias test significant after FDR, q>=.07); axiom method about -51% on average (p<.001), up to -73% for some biases; hindsight was an exception [a18, d09]. This resembles human rule training (Larrick, Nisbett): give the rule, not a warning. Single group.

**4.7 Human procedures as templates (DIY).** Each of five prejudice-reduction practices is a three-step template, e.g. perspective-taking = adopt the person's view, simulate their thoughts, integrate into the answer. REVISE re-reads the first answer and applies one template [c25]. Revision at inference gave most of the reduction; training alone was smaller [d16]. Social-stereotype benchmarks only.

**4.8 Think in opposites / dual goal.** The prompt asks the model to test an instance it expects to fail as well as one it expects to pass. Measured by the ratio of incompatible to compatible tests, which rose in 18 of 22 cases [d10]. Cap the number of alternatives (section 5, backfire).

## 5. What holds up

**Held up (with limits).**
- Practice with feedback beats passive instruction in people, but only on some biases and with confounds [b02, b03, d05].
- Effects decay but persist: game about 24-35% at 2-3 months; for confirmation bias the effect roughly halves [b02].
- Rule teaching (statistics, cost-benefit, probability) transfers to new content [b08, b07]. It works for statistical-principle biases and mostly there [b09, K09].
- Forecast training: 6-12% Brier gain in each of four years [b07].
- In LLMs, three facts repeat across groups: debate and Reflexion do not help and can amplify bias [a15, a22, c03, d18]; few-shot "debiased examples" can make things worse [a21, d08]; CoT and "ignore the anchor" do not fix anchoring [a17, c09, d09].

**Did not hold or is weak.**
- Awareness and checklists. Morewedge 2015 and Aczel 2015 say knowledge is not debiasing. Cognitive forcing tool: 2.8 vs 3.1 correct in 76 doctors [b10]. Slowing or delaying did not reduce following of biased AI advice [b11]. In LLMs, awareness helps weaker models some (GPT-3.5 bandwagon: with-reason .524, AwaRe .260; the SoPro "answer as most people would" prompt was worse, .955 [b15]) and GPT-4 little (.214 baseline, .142 with AwaRe); in BiasBuster, GPT-4 awareness framing gap was -0.470 vs baseline -0.405, no gain [b14]. Verdict: contested, and small beside targeted procedures.
- Personas: conscientious and agreeable personas sometimes help debiasing; awareness sometimes raised bias; effects are model-specific [b20, c17].

**Corrections made during this study.**
- Sellier et al. (2019): 19% less likely, not 29%. The published abstract and PubMed say 19%. The accepted manuscript and the authors' Conversation piece said 29%. A Corrigendum exists (Psychol Sci 2020;31(6):762, PMID 32423341); its text was not read, so "29 to 19" is an inference [d01, d02, d03].
- Morewedge abstract numbers are minima over two experiments, not single numbers [critique 2].
- BiasBuster's -0.405 is a gap in admission rates in points [critique 5].
- CogBias steering is 26-32%, not "about a third" [critique 8].
- The 2025 analysts study was once labelled a replication. It is not independent (two authors are the original game team) and has no untrained control, so it is single-source [d04].

**Failed or doubtful replications.** No independent replication of Morewedge 2015 or Sellier 2019 was found. The field test was quasi-random (class schedule) and used one case; 22 untrained students (20.4%) never played the game; the long-lag group was only 57 people [d02]. In LLMs, a multi-model audit of eleven biases found 27 of 43 bias-model pairs significant, but only 1 pair survived a test requiring the effect across prompt rewordings [d18]. So some "LLM biases" are prompt artefacts.

**Moderators.**
- Bias type: statistical-rule biases respond to rule training and to the video; social and attributional biases respond more to practice with feedback [b02, b03, b09].
- Model capacity: self-help needs a strong model [a25]; thinking models benefit from opposite-testing, non-thinking ones do not [d10]; GPT-4's baseline bias is already low in some tests (4.7% in one) [b20].
- Bias family in LLMs: response-position biases yield to prompts (+40.5%), judgment biases do not (-4.4%) [a19].
- Content vs structure of the cue: weight-trained cue-ignoring transfers across content cues, not to answer position [d14]. Steering transfers across families, but random directions also lowered bias; learned directions were only 1.6% better than random [d15].
- Number of alternatives (people): 2 fine, 10 backfires [d11].
- Whether the cue is right: blindly ignoring cues costs accuracy when they are right [d14].

**Cost of overcorrection.**
- SACD: false flags on unbiased prompts 12 / 3 / 6 per 500 (finance / medical / legal); wrong bias type 49 / 108 / 73 per 500 [d07].
- Llama2-7B-Chat flagged over 90% of unbiased content as biased [c19, d17]. On BBQ, models hide behind "Unknown", so bias scores under 6% hide lost accuracy [d17].
- Prompt mitigation cut Qwen3-4B clean accuracy 66.2% -> 40.9%; SFT cut Qwen3-1.7B 84.3% -> 52.1% [d14].
- Qwen lost up to 19.0 pp on judgment benchmarks under steering [d15, b18].

**Contradictions left unresolved.**
- Awareness: small help for weaker LLMs and in some human workshops (Mair, Shepperd; not opened) vs no help in Morewedge/Aczel. Likely depends on bias, model and how much else is in the package.
- Self-reflection: Echterhoff (self-help works for strong models) and SACD (iterated loop works) vs Lou and Sun (reflection does nothing for GPT-4 anchoring). Likely bias type (anchoring is shallow) and one-pass vs iterative.
- Game vs video: strong in Exp 1; equal on two of three biases in Exp 2.

## 6. Language models

**Baseline: LLMs show human-like biases.** Instruction tuning and RLHF raised decoy, certainty and belief biases over base models; GPT-4 had the highest decoy scores [b21, c07]. A sweep of 30 biases across 20 models found all 30 in some models [c08]. Codex, GPT-3 and ChatGPT shift with framing and anchors [c12, c13, b23, c11]. GPT-4 admitted 40.5 points more students under one frame [c01]. Llama-2 7B rated 32.1% fewer females as good at math [c01]. Five LLMs were 20-60 points overconfident on algorithmic problems [c20]. Small vignette changes broke GPT-3 [c11]. Labelling an anchor as "a prior AI estimate" raised anchor slope 52% (0.272 to 0.413) in 51,000 calls to three recent commercial models; GPT-5-mini anchored far less than Claude Haiku 4.5 and Gemini 2.5 Flash [d19; SSRN, not peer reviewed]. A caution: in the audit that required effects to survive prompt rewording, only 1 of 43 bias-model pairs did [d18].

**What changed bias, by how much (lower bias = better).**

| Method | Result | Verdict |
|---|---|---|
| SACD loop (detect, analyse, rewrite) | Llama-8B FOMC 0.3805 -> 0.1570; Llama-70B 0.1648 -> 0.1080; GPT-3.5 0.4765 -> 0.1175; GPT-4o 0.3650 -> 0.0300; GPT-3.5 multi-bias 0.9540 -> 0.1220. Errors out of 500, self-help vs SACD: 257/209/409 vs 61/111/79 [b17, c03] | Best in this set. One group; costs several calls |
| Self-help rewrite | GPT-4o 0.0625; GPT-4 framing gap -0.405 -> -0.010; Llama-8B 0.2100 [b14, d08] | Strong baseline for strong models; harms weak ones |
| Zero-shot debias instruction | FOMC Llama-8B 0.2965; GPT-4o 0.2650 [a14, d08] | Small |
| Few-shot debias examples | Llama-8B 0.2970; GPT-4o 0.7350 vs vanilla 0.3650 (worse); Llama-2-7B collapsed to admit/reject-all (0.996/1.000) [a21, d08] | Unsafe |
| CoT | 0.3425 vs 0.3805 (Llama-8B); GPT-4o 0.3650 (no change); worse than no prompt in PROBE-SWE (16.1% vs 12.9%) [a14, d08, d09] | Weak. A GPT-3 class model went 5% -> 28% correct on CRT with CoT but atypical answers rose 15% -> 43% [c10] |
| Reflexion | GPT-4o 0.2450 (helped); Llama-70B PubMedQA 0.5585 (worse); multi-bias worse [d08, a15] | Model-dependent; can amplify |
| Multi-agent debate | Llama-8B 0.5020 (worse than vanilla .3805); GPT-3.5 0.5155; GPT-4o 0.3700 [a14, c03, d08] | Do not use (matches G9) |
| Awareness reminder | GPT-3.5 bandwagon .524 -> .260; GPT-4 .214 -> .142; GPT-4 BiasBuster framing -0.470 [b15, b14] | Mixed, small |
| Axiomatic cues (PROBE-SWE) | about -51% average sensitivity, up to -73%; hindsight exception [d09] | Promising; single group |
| Anchoring: Anti-DP two-phase (set a standard first, then rethink) | Llama-8B 34.7% -> 24.7%; Qwen2.5-7B 40.0% -> 40.8% (no gain) [a16, b16] | About 10 points on one model only |
| Anchoring: Both-Anchor (low and high hints) | GPT-4 near bias-free value only where the two hints straddled it [a17] | Narrow |
| Opposite-testing prompts | 42% -> 56% across 11 LLMs; significant for thinking models only [d10] | Conditional on model type |
| Human procedures (DIY REVISE) | mean bias 2% at 90% reasoning accuracy; up to 14.8 pp on unseen dimension [a20, d16] | Social bias only |
| Prompt debias on CogBias | +40.5% response, -4.4% judgment [a19] | Family-dependent |
| Activation steering | 26-32% bias reduction; Qwen -19.0 pp capability on judgment [b18, d15] | Open weights only |
| Weight training with non-predictive cue | 70.1 -> 83.3 adversarial; +39.1 on unseen distraction [b19, d14] | Out of scope; analogue only |
| Bayesian teaching (fine-tune) | about 80% agreement with Bayesian assistant; prompt variants incl. CoT gave no meaningful gain [c14] | Out of scope |
| Choice-supportive bias fine-tune | 81.5% (memory) and 94.3% (evaluation) improvement [c21] | Out of scope; single |

**Pattern.** Prompting methods that give the model something new to check (the actual bias in the actual prompt, a domain axiom, an opposite test) work. Methods that add more of the same reasoning (CoT, debate, more examples) do not. This agrees with the human finding that rules and feedback beat warnings.

**Gaps.** (1) No LLM study runs repeated own-error feedback inside a run [K20]. (2) No test of how effects decay over steps [K27]. (3) No equal-token SACD vs one-pass test. (4) Frontier reasoning models are almost absent from the debiasing tests: GPT-4o was the top model in SACD; DeepSeek-R1 appears only in PROBE-SWE, where CoT raised sensitivity 16.3% -> 18.5% [d09].

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **G: Do not use warnings, "be careful" or generic checklists as the debiasing method.** [E] Evidence a04, b04, b09, b10, b11, b15, b14. Already in SCHEMA 4b; this adds the training literature and the cognitive-forcing nulls to its citation list.
2. **G: No debate and no unstructured reflection as a debiaser.** [E] Evidence a15, a22, c03, d08, d18. Matches G9 and 4b. New numbers: debate 0.5020 vs vanilla 0.3805.
3. **G: No static few-shot "debiased answer" blocks as a default.** [E] Evidence a21, a22, d08: GPT-4o 0.7350 vs vanilla 0.3650; Llama-2-7B collapsed to accept-all. Applies to examples that show the debiased answer; cue-triggered worked cases are in "Test first".
4. **G: Every debiasing step is scored on unbiased twins (false-alarm and accuracy check).** [E] Evidence d07, d14, d17, c19, a19 (K24). Log accuracy, refusal or "unknown" rate and false-flag rate with each step. Fits G7 and section 6 logging.
5. **G: Debiasing is per bias type; do not claim general debiasing.** [E] Evidence b09, a19, d14, d15. Prompt-level fixes work for response-position and some social biases and can hurt judgment biases (-4.4%).
6. **S1 input hygiene: put cues in a marked block, but do not treat them as always wrong.** Harm of suggestive cues [E] (SCHEMA S1); the refinement "the cue may be right" is [S]. Evidence d14, b19.
7. **O: rule card for statistical and economic rules where a check exists** (sunk cost, base rate, sample size, regression to the mean). [E] Evidence b08, a07, b09, b07. Supply the rule at the moment of use, not as a general reminder. Statistical-principle biases only.

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | In-run error log with immediate corrective feedback on repeated item sets vs one-shot warning | M (lesson store), S9 | [S] human; none for LLMs | a01, a02, d05, K20 |
| T2 | Detect-analyse-rewrite (SACD) at S1 vs one-pass self-help at equal tokens | S1, O reframe | [S] | b17, d06, d07 |
| T3 | Axiom-first prompt (elicit domain best-practice rules, then inject) | S1 or S2 | [S] | a18, d09 |
| T4 | Opposite-test operator at S7 for rule discovery (thinking models only) | S7 / O | [S] | c15, d10, d13 |
| T5 | Cap on the number of alternatives (1, 2, 3, 5, 10) | O | [S] human; none for LLMs | d11, d12, K22 |
| T6 | Anchor-controlled estimate (set own standard first, then read the anchor) | S1 / O | [E] that CoT fails; [S] for the fix | a16, a17, c09 |
| T7 | Argument-count code check: flag lopsided evidence counts for the chosen option | S7 / S8 | [S] human mechanism | b06, d02 |
| T8 | Perspective-taking REVISE template for social-judgment items | O | [S] | a20, d16, c25 |
| T9 | Re-injection schedule of the debiasing block (step 1 vs every k steps vs on cue) | M | [S]; none direct | d02, d19, K27 |
| T10 | Cross-family transfer of in-context practice | M | [S]; weights only | d14, d15, d16 |
| T11 | Ablation of the Fischhoff four ingredients as prompt blocks | M | [S] | a05, d05, K23 |
| T12 | Awareness prompt by model size | G | [C] | b15, b14, b20, K13 |

All T-items follow G1: fire on a signal (a bias cue found by code, an impasse, a check failure), never on a schedule. Each also needs the false-alarm check from Add-now item 4.

## 8. Concrete tests on our bench

All arms get equal total tokens including setup (G7). Report accuracy, bias score, refusal/"unknown" rate and false-flag rate on clean twins. Use at least 100 items per cell and a paired bootstrap.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Error log vs warning | 40 anchoring and confirmation items, three rounds of 10 per bias; in the log arm, after each item show the model's own earlier error, the correct handling and a one-line reason; held-out items at round 4 and again 20 steps later | (a) plain; (b) warning naming the bias; (c) warning plus worked example; (d) practice without feedback; (e) practice with feedback | bias score on held-out items, immediate and delayed | Human prior 24-46%. Expect (e) > (c) > (b) ~ (a). Add if (e) beats (b) by at least 25% relative reduction at equal tokens |
| B2 SACD vs self-help | FOMC/PubMedQA/LegalBench-style prompts with anchoring, bandwagon, loss-aversion cues, 500 each, plus 100 clean twins | plain; self-help x1; self-help given the same token total as 2-3 passes; SACD (max 3) | bias score, false-flag rate, wrong-type rate | Lyu: SACD 0.03-0.157 vs self-help 0.0625-0.349. Expect the gap to shrink at equal tokens and on strong models |
| B3 Axioms first | 8 software-dilemma bias types (PROBE-SWE style) | plain; CoT; self-debias; axiom-first | flip rate between biased and unbiased dilemma | about -51% sensitivity if the finding holds; hindsight an exception |
| B4 Opposite test | 2-4-6 rule discovery and 3 other rule-discovery tasks, thinking mode on and off | plain; Think-in-Opposites; Dual-Goal | success rate; ratio of disconfirming tests | 42% -> 56% overall; gain only with thinking on |
| B5 List length | hindsight and confirmation items | 0, 1, 2, 3, 5, 10 alternatives | bias score vs list length | If the human backfire transfers, bias rises above about 5; else flat |
| B6 Anchor estimates | 62-question numeric items with fact, expert and irrelevant hints (Lou and Sun style) | plain; CoT; ignore-anchor; set-standard-first; both-anchor | anchoring index | set-standard-first about -10 points on one model; others ~0 |
| B7 Cue sometimes right | MMLU-style items where a bandwagon claim is right half the time | plain; "ignore cues" instruction; cue-as-unknown-validity block | accuracy on cue-right and cue-wrong halves | "Ignore cues" lowers cue-right accuracy (the wrong-only shortcut) |
| B8 Argument-count check | 60 decision cases with a favoured option | plain; code flag on lopsided counts, then rewrite | share choosing the confirming option | Human: 19% relative drop; expect smaller |
| B9 Re-injection | 60-step runs with probes at steps 5, 20, 50 | block at step 1 only; every 10 steps; on cue only | bias score at each probe | Decay if step-1 only; on-cue should match every-k at fewer tokens |
| B10 Transfer | train 3 biases in-context, test 3 other families | as B1 | held-out bias | Expect no transfer across families (position cues did not transfer) |
| B11 Awareness by model size | small, mid, frontier | plain; AwaRe | bias score | Help for small, none for frontier |

## 9. What does not transfer, and why

- **The 60-minute game itself.** Human learners are slow, forget, and need motivation. Our agent re-reads text perfectly but has no persistent memory unless we build it. Game variants with scores, hints or story did not differ in people [d05], so the motivational layer is not the part to copy.
- **Retention numbers (2-3 months, d about 1.1).** Human forgetting curves do not map to context length. Our decay is context dilution over steps [K27].
- **Awareness as a human lever.** In people, awareness shifts attention to one's own thinking. For a model, naming the bias partly acts as a prompt cue and can raise or lower the behaviour, depending on the model [b15, b20].
- **The Hawthorne and demand-effect worry.** The skeptics' point does not apply to an agent in the same way. It does warn that a prompt that only looks like debiasing can lower the bias score by avoidance [d17].
- **Weight training (EIT, Bayesian teaching, fine-tunes, steering).** Out of scope: the schema changes no weights (G7, 4b). These results show what feedback and practice can do in principle, and show cue-type transfer limits [K17, K25].
- **Social stereotype results (DIY, BBQ).** They concern prejudice benchmarks. Judgment biases (anchoring, sunk cost) are a different family and responded differently (-4.4%) [a19].
- **Calibration training.** Forecast calibration in people does not tell us about LLM confidence, which is 20-60 points overconfident [c20] and which the schema already treats as unreliable (4b).
- **Individual differences.** Need for cognition helped humans resist biased AI advice [b11]; there is no counterpart in a single agent.
- **Rule training for statistics in people.** A model already knows the rules. The issue is applying them at the right moment, so the reminder must be cue-triggered, not taught [b09].

## 10. Open questions

1. Does feedback on the agent's own earlier errors inside a run lower bias at equal tokens? (K20.)
2. Which of the four Fischhoff ingredients carries the effect: naming, direction, practice, feedback? No ablation in people or LLMs (K23).
3. Does SACD beat one-pass self-help at equal tokens, and on frontier reasoning models?
4. Does in-context practice on one bias family transfer to another? Weights: content yes, structure no (K25). In-context: unknown.
5. What is the best number of alternatives for an LLM, and is there a backfire? (K22.)
6. How fast does the effect decay over steps? (K27.)
7. What did the Sellier corrigendum change (text not read)? Is there any independent replication of Morewedge 2015?
8. Why did Exp 2 show video = game on anchoring and representativeness? Rule-like biases may need only the rule.
9. Why does self-reflection help in some tests (Echterhoff, SACD) and not others (Lou and Sun)? Bias type and iteration are the leading guesses, untested.
10. How much of the SACD gain is real vs a metric artefact, given the same LLM detects the bias and the score is the authors' own? Wrong-type errors reached 108 of 500 [d07].
11. Does debiasing change accuracy on clean items for frontier models? Only older or small models were measured.
12. Do consider-the-alternative prompts help non-thinking models at all? (Dual-Goal slightly lowered accuracy [d10].)

## 11. Sources

[V] opened and read in this study; [M] snippet, title or abstract only, or second-hand.

- [V] Morewedge, Yoon, Scopelliti, Symborski, Korris, Kassam (2015) Debiasing decisions, Policy Insights from the Behavioral and Brain Sciences. https://openaccess.city.ac.uk/id/eprint/12324/ (a01-a06, b01-b04, d05)
- [V] Sellier, Scopelliti, Morewedge (2019) Debiasing training improves decision making in the field, Psychological Science. https://openaccess.city.ac.uk/id/eprint/22233/ ; abstract https://pubmed.ncbi.nlm.nih.gov/31347444/ ; summary https://theconversation.com/training-to-reduce-cognitive-bias-may-improve-decision-making-after-all-126402 (b05, b06, d01-d03). Corrigendum PMID 32423341 [M, text not read].
- [V] Heerma van Voss, Yoon, Scopelliti, Zweet, Helsloot, Morewedge (2025) Debiasing training reduces confirmation bias in national risk analysts. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12660316/ (b12, d04)
- [V] Chang, Chen, Mellers, Tetlock (2016) Developing expert political judgment, Judgment and Decision Making. https://jbaron.org/journal/16/16511/jdm16511.pdf (b07)
- [M] Mellers et al. (2014) Psychological strategies for winning a geopolitical forecasting tournament. https://escholarship.org/uc/item/4rg4n9vr (a11)
- [V] Larrick, Morgan, Nisbett (1990) Teaching the use of cost-benefit reasoning in everyday life. https://gwern.net/doc/psychology/cognitive-bias/sunk-cost/19 (b08)
- [M] Nisbett, Fong, Lehman, Cheng (1987) Teaching reasoning, Science 238:625-631. https://www.science.org/doi/10.1126/science.3672116 (a07, b25)
- [M] Fischhoff (1982) Debiasing, in Kahneman, Slovic, Tversky. https://doi.org/10.1017/CBO9780511809477.032 (a08, b26)
- [M] Hirt and Markman (1995) Multiple explanation, JPSP 69:1069. https://doi.org/10.1037/0022-3514.69.6.1069 (a09)
- [V] Aczel, Bago, Szollosi, Foldes, Lukacs (2015) Is it time for studying real-life debiasing? Frontiers in Psychology. https://www.frontiersin.org/articles/10.3389/fpsyg.2015.01120/full (b09)
- [V] Shepperd, Mair, Jorgensen (2018) An experimental evaluation of a de-biasing intervention for professional software developers. https://arxiv.org/abs/1804.03919 (a12)
- [M] Mair, Shepperd, Jorgensen (2014) Debiasing through raising awareness reduces the anchoring effect (c23; not opened)
- [V] O'Sullivan, Schofield (2019) A cognitive forcing tool to mitigate cognitive bias. https://pmc.ncbi.nlm.nih.gov/articles/PMC6325867/ (b10)
- [V] Cognitive forcing and need for cognition in AI-assisted decision making, Scientific Reports. https://pmc.ncbi.nlm.nih.gov/articles/PMC12779943/ (b11)
- [M] Ludolph, Schulz (2018) Debiasing health-related judgments and decision making. https://econpapers.repec.org/RePEc:sae:medema:v:38:y:2018:i:1:p:3-13 (b13)
- [M] Sedlmeier, Gigerenzer (2001) Teaching Bayesian reasoning in less than two hours. https://www.causeweb.org/cause/node/6925 (b28)
- [M] Anesthesiology trainees consider-the-opposite trial (2025, title only). https://europepmc.org/search?query=%22Consider-the-Opposite%22 (b29)
- [V] Sanna, Schwarz, Stocker (2002) When debiasing backfires. https://pubmed.ncbi.nlm.nih.gov/12018501/ (d11)
- [V] Sanna, Schwarz (2003) Accessibility experiences and the hindsight bias. https://pubmed.ncbi.nlm.nih.gov/12661859/ (d12)
- [V] Branchini, Burro, Bianchi (2023) Training people to think in opposites facilitates falsification. https://pubmed.ncbi.nlm.nih.gov/37233340/ (d13)
- [M] Arkes (1991); Milkman, Chugh, Bazerman (2009); Kahneman and Egan (2011): skeptics, second-hand via Sellier (b27)
- [M] Devine et al. (2012) prejudice habit-breaking intervention (c22, a24; second-hand via Raj)
- [V] Echterhoff, Liu, Alessa, McAuley, He (2024) Cognitive bias in decision-making with LLMs (BiasBuster). https://arxiv.org/abs/2403.00811 (a13, a21, a25, b14, c01, c24)
- [V] Lyu, Ren, Feng, Wang, Chen, Ren, de Rijke (2025) Self-adaptive cognitive debiasing (SACD). https://arxiv.org/abs/2504.04141 (a14, a15, a22, b17, c02, c03, d06-d08)
- [V] Huang, Bie, Na, Ruan, Lei, Yue, He (2026) Understanding the anchoring effect of LLMs with synthetic data. https://arxiv.org/abs/2505.15392 (a16, b16)
- [V] Lou and Sun (2024) Anchoring bias in large language models. https://arxiv.org/abs/2412.06593 (a17, a26, c09)
- [V] Sovrano, Dominici, Bacchelli (2026) Mitigating prompt-induced cognitive biases in general-purpose AI for software engineering (PROBE-SWE). https://arxiv.org/abs/2604.16756 (a18, d09)
- [V] Huang, Zhang, Kwak, An (2026) CogBias. https://arxiv.org/abs/2604.01366 (a19, b18, c04, d15)
- [V] Raj, Mansouri, Caliskan, Anastasopoulos, Zhu (2026) Debias It Yourself. https://arxiv.org/abs/2609.40124 (a20, a24, b24, c05, c25, d16)
- [V] Wang et al. (2026) Making bias non-predictive: Epistemic Independence Training. https://arxiv.org/abs/2602.01528 (b19, c06, d14)
- [V] Sumita, Takeuchi, Kashima (2024/2025) Cognitive biases in LLMs: a survey and mitigation experiments. https://arxiv.org/abs/2412.00323 (b15, c16)
- [V] He and Liu (2025) Impact of LLM personality on cognitive bias. https://arxiv.org/abs/2502.14219 (b20, c17)
- [V] Itzhak, Stanovsky, Rosenfeld, Belinkov (2024) Instructed to bias. https://arxiv.org/abs/2308.00225 (b21, c07)
- [V] Liu and He (2024) The decoy dilemma in online medical information evaluation. https://arxiv.org/abs/2411.15396 (b22); c18 same paper, abstract only [M]
- [V] Binz and Schulz (2022/2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (b23, c11)
- [V] Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs. https://arxiv.org/abs/2410.15413 (c08)
- [V] Suri et al. (2024) Do LLMs show decision heuristics similar to humans? https://arxiv.org/abs/2305.04400 (c12)
- [V] Jones and Steinhardt (2022) Capturing failures of LLMs via human cognitive biases. https://arxiv.org/abs/2202.12299 (c13)
- [V] Hagendorff, Fabi, Kosinski (2023) Thinking fast and slow in LLMs. https://arxiv.org/abs/2212.05206 (c10)
- [V] Qiu et al. (2026) Bayesian teaching enables probabilistic reasoning in LLMs. https://arxiv.org/abs/2503.17523 (c14)
- [V] Jhaveri, GX-Chen, Sucholutsky, Choi (2026) Failing to falsify. https://arxiv.org/abs/2604.02485 (c15, d10)
- [V] Rethinking prompt-based debiasing in LLMs (2025). https://arxiv.org/abs/2503.09219 (c19, d17)
- [V] Overconfidence in LLMs (2025). https://arxiv.org/abs/2505.02151 (c20)
- [V] Alleviating choice-supportive bias in LLM with reasoning dependency generation (2025). https://arxiv.org/abs/2512.03082 (c21)
- [V] Cognitive biases in LLMs: a systematic quantitative assessment and debiasing, Electronics 2026. https://doi.org/10.3390/electronics15112428 (d18)
- [V] Algorithmic anchoring (SSRN 6366838). https://doi.org/10.2139/ssrn.6366838 (d19)
