# Cognitive biases in software work: deep document

*Subfield A20.08 of the psychology of programming. Built from evidence_a-d.jsonl, claims.jsonl (K01-K28) and critique.md in this folder. Evidence ids (a01, b07, d12 ...) point to the jsonl lines. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested.*

## 1. What it is

A cognitive bias here is a systematic, repeatable departure from sound judgment that a person (or a model) shows when working on software. The four the field names most are:

- **Anchoring.** An early number, code line or framing pulls later judgment toward it. Example: a high effort figure in a spec raises the estimate.
- **Optimism.** Expecting a better outcome than the base rate supports (estimates, plans, "it will pass").
- **Availability.** The easy-to-recall or most frequent option wins over the right one.
- **Confirmation bias.** Choosing tests or evidence that agree with the current hypothesis. In testing this is "positive test bias": write tests that should pass, not tests that could fail.

The systematic mapping (Mohanani, Salman, Turhan, Rodriguez, Ralph 2020; a01) found 65 articles (1990-2016) and 37 biases. Anchoring was studied most (26 articles), then confirmation (23) and overconfidence (16). 72% (47) of the articles were empirical, mostly lab experiments; 28% (18) were not.

Why this matters for our agent. Our schema guardrail G3 says a pass must be on something the answer was not fitted to. Confirmation bias is the human version of the failure G3 guards against. Anchoring is the human version of two other things we care about: a failed attempt left in context pulling the next attempt (S5/S6), and suggestive material in the task text pulling the answer (S1 input hygiene).

The subfield has two halves.

1. **Human software engineering studies** (1960 to 2026). Thin, mostly small, mostly students, little replication.
2. **LLM bias studies** (2022 to 2026). Many, mostly on short vignettes or rule games, mostly on old or small models, many 2026 preprints without independent replication.

The task framing said "logic training reduced confirmation bias". The research did not find that claim well supported (see 5 and K14). The useful material is elsewhere: how and when tests get chosen, how anchors enter the context, and which cheap fixes work on models.

## 2. History and theories in depth

**Wason 1960 (b24, [M]).** The 2-4-6 task. People are told 2-4-6 fits a rule, propose triples, and are told yes or no. Most propose triples that fit their own hypothesis (for example "ascending by 2") and so never learn the true rule ("any ascending numbers"). Numbers not read this session. This is the founding result for positive test bias. Klayman and Ha's later point (from memory, not opened): a positive test strategy is often a good heuristic when the true rule is narrower than the hypothesis. It fails when the true rule is broader. That is exactly the 2-4-6 design.

**Tversky and Kahneman era (1970s).** Anchoring and adjustment, availability, representativeness. In software, the first anchoring study cited here is Aranda and Easterbrook 2005 (b26, [M], not read): anchoring in software estimates.

**Positive test bias in testing, 1994.** Teasley, Leventhal, Mynatt and Rohlman 1994 (d11, [M]) and Leventhal, Teasley and Rohlman 1994 (d10, [M]) asked whether programmers test with cases that confirm the spec. Per Mohanani's summary (b02) and the abstracts: bias was present in every condition, reduced by expertise and by a more complete specification. Exact numbers were not obtained. Salman 2019 (d09) says the earlier studies labelled tests differently than he did.

**Confirmation bias in developers, 2010 onward.** Calikli, Arslan and Bener (PPIG 2010; a05-a10, b05, b06) built a questionnaire-based measure of confirmation bias (test severity, eliminative-to-enumerative index) and related it to experience, company size and, weakly, defects. This is the source of the "logic training reduced confirmation bias" line (Mohanani P4; a03, a04). The critique found the paper's title is "Confirmation Bias in Software Development and Testing: An Analysis of the Effects of Company Size, Experience and Reasoning Skills". The companion PROMISE 2010 paper (d14, [M]) was only seen as an abstract.

**The review era, 2016-2020.** Mohanani et al. (a01-a04, a26-a28) map the field. They note confusion between biases and heuristics, and no strong evidence for any debiasing technique. Only 6 of 37 biases had any proposed debiasing; all proposals for anchoring (planning poker, generating multiple designs, directed questions) were unevaluated (a26).

**Human anchoring experiments, 2018-2022.** Shepperd, Mair, Jorgensen 2018 (b07): anchor in developer estimates, tested with a debiasing workshop. Gren and Svensson 2021 (b08, b11): obsolete requirements still raise estimates. Wyrich et al. 2021, 2022 (b09, b10): framing code as easy or hard changes how comprehensible it is rated, not how well it is understood.

**LLM turn, 2022 onward.** Jones and Steinhardt 2022 (a17-a20, b12, c01-c03) used human biases as a source of code-model failure hypotheses (anchoring, availability, framing, attribute substitution). Suri et al. 2023 (c04, c05) and Malberg et al. 2025 (b13, c06-c08) measured many biases in chat models. Then came mitigation work (PROBE-SWE, SynAnchors, AnchorBench, CogBias) and falsification work (Failing to Falsify, FalsifyBench, WILT).

**Theory competition.** Three accounts compete for the LLM results.

1. *Human-like bias learned from text.* Anchoring and framing replicate in GPT-3 and 3.5 (c04, c05).
2. *Prompt sensitivity or quiz recognition.* Tommasel and Schedl 2026 (b21) argue many "bias" scores do not warrant claims about bias, and low bias can mean the model failed the task (K19, [C]).
3. *Mechanism-level account.* Anchoring is an attention and context effect: causal tracing on Llama-3.1-8B puts the effect before the middle layers (c25). A failed attempt in context acts as an anchor on small code models (d01) and as a contamination cascade in agent pipelines (d04).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Size of the SE bias literature | 65 articles, 37 biases; anchoring 26, confirmation 23, overconfidence 16; 47 empirical | Mohanani 2020 (a01) | [E] descriptive |
| Debiasing evidence in SE | 6 of 37 biases have any proposal; 0 studies with strong effectiveness evidence | Mohanani 2020 (a02, b01) | [E] K16 |
| Positive test bias in testers | 86.5% of 371 test cases spec-consistent (321 vs 50); p=2.2e-8, r=0.598; N=42 grad students | Salman 2019 (d09) | [E] K01 |
| Time pressure and confirmatory testing | d=-0.357, n.s. (wrong direction); 30 vs 60 min groups of 21 | Salman 2019 (d09) | [S] K25 |
| Experience does not fix confirmation bias | no significant correlation of test experience (n=27) or development experience (n=50) with test severity or elimination index | Calikli 2010 (a06) | [S] |
| Company-size difference | large telecom C1 (n=34) vs small firms (n=26): elimination index z=-2.76, p<.01; severity z=-2.26, p<.05 | Calikli 2010 (a07) | [S] K14 |
| Students vs staff on abstract and software questions | chi2(1)=8.114, p<.005 and 7.085, p<.01; 27 of 28 students found the rule vs 29 of 34 at the large firm. Experience-matched (43 vs 13): only test duration differed (z=-1.39, reported p<.05 but z=-1.39 is p about .16) | Calikli 2010 (a08, b05) | [S] K14 |
| Confirmation bias and defects | 5 developers: defect ratios 0.86, 0.38, 0.20, 0.00, 0.11; 12 testers rho 0.8234 reported bugs vs production defects. No significance test | Calikli 2010 (a09, a10) | [S] K15 |
| Anchor effect in professional estimates | d=1.19, trimmed gap 60.5 (CI 51.6-69.4), about 350%; N=410 developers | Shepperd 2018 (b07) | [S] |
| Awareness workshop | workshop effect on estimates d=0.72 (26 LOC/h trimmed difference); variance down threefold; high-anchor median 100 to 30 LOC/h; non-randomised | Shepperd 2018 (b07) | [S] K09 |
| Obsolete requirements still anchor | effect sizes 0.54, 0.75, 0.54 across 3 experiment sets, N=461; industry means 4.62, 6.69, 8.33 for none/some/more obsolete | Gren and Svensson 2021 (b08) | [E] K08 |
| Framing changes rated comprehensibility, not understanding | path 0.165 (CI 0.071-0.265), N=256; rating d=-1.29 N=43; actual understanding d=-0.006 | Wyrich 2021, 2022 (b09, b10) | [E] K18 |
| Developer+LLM sessions are biased | 983 of 2,013 actions (48.8%) or 949 (47.14%) biased; LLM actions 456/808 (56.4%) or 434 (53.7%) | Zhou 2026 (a14-a16, b19) | [E] K17 |
| Fixation on LLM suggestion | 76 LLM actions, 43.4% reversed (highest category) | Zhou 2026 (c10) | [E] K17 |
| Bias-reversal link in LLM era | reversal 25% (505/2013) vs 52.9% (1104/2084) in 2020 study; biased actions reversed 27.08% (257/949); p=0.058 | Zhou 2026 vs Chattopadhyay 2020 (a16, a30) | [E] K17 (boundary, not clean failure) |
| Human debiasing, randomised | 2-4-6 with "think of the opposite": 78.33% vs 38.33% (properties only) vs 36.66% (control); N=180; chi2=27.986 | Branchini 2025 (d12) | [S] K02 human arm |
| Game training transfer | confirming option chosen 58.8% (n=182) vs 72.2% (n=108); N=290; odds 0.549; p=.022; quasi-experimental | Sellier 2019 (d13) | [S] K24 |
| Anchoring in code models | Codex copies anchor loop in 32-61% of solutions; framing line in 81% of outputs vs 4.5% baseline; accuracy lost 22.3 to 30.5 points; CodeGen 70.7% vs 0.0% | Jones and Steinhardt 2022 (a17, a18) | [E] K07 |
| Availability in code models | operation order flipped: accuracy 50% to 17%; 75% of the errors were the frequent-order solution | Jones and Steinhardt 2022 (a19, c03) | [S] |
| Attribute substitution | conflicting function name: accuracy 100% to 4.4% | Jones and Steinhardt 2022 (a19, c03) | [S] |
| Numeric anchoring in GPT-3.5 | low anchor mean 20.83, high 105.97; humans 22.50 and 80.50 | Suri 2023 (c04) | [E] K07 |
| Anchoring across 20 models | mean score 0.39, range -0.05 to 0.67; confirmation 0.15, range -0.18 to 0.72; availability 0.11; optimism 0.06; planning fallacy -0.02; escalation 0.07 | Malberg 2025 (b13, c07, c08, b22) | [E] K07, K13 |
| SynAnchors | 100 questions x 100 asks; anchored: Qwen3-235B thinking 22.0%, DeepSeek-R1 25.0%, Qwen2.5-0.5B 60.5% | SynAnchors 2025 (c25) | [C] K11 |
| Anchor entry pathway | external-anchor index 0.71 (Claude Haiku 4.5), history 0.00, ICL 0.00; Gemini 2.5 Flash 0.79, 0.23, 0.00 (table partly garbled) | AnchorBench 2026 (d15) | [S] K26 |
| SE-vignette bias sensitivity | median 12.9% control; anchoring weakest (5.9%), hindsight strongest (35.3%); confirmation +33.66 pp per complexity tier | PROBE-SWE 2025 (a11, a12) | [S] |
| Prompt fixes on SE vignettes | CoT 16.1% (worse), bias warning 10.3%, self-debias 10.2%, both 8.3% | PROBE-SWE 2026 (b17) | [E] K08 |
| Axiomatic cue (write the rules first) | 12.9% to 6.3-7.5%, about 51% cut; low tier 8.1% to 3.5%; high tier 17.0% to 12.2%; open-ended 40 items, CIs wide | PROBE-SWE 2026 (b18) | [E] K12 |
| Rule instruction on anchors | plausible-anchor index 0.33 to 0.06 with explicit rule vs 0.26 with vague judgment prompt | AnchorBench 2026 (d17) | [E] K12 |
| Generic prompt debiasing | judgment accuracy -4.4% (backfires); response-order +40.5% | CogBias 2026 (d18) | [E] K12 |
| Self-debias by rewriting prompt | GPT-4 framing 2.7%, group attribution 0% of biased elements left; Llama 2: 0-1.4% left but 40-52% decision changes on anchoring | Echterhoff 2024 (a21, b14) | [S] K22 |
| 2-4-6 falsification, LLM | thinking baseline success 0.21 (Qwen3-8B) to 0.73 (Gemini 2.5 Pro); infirming:confirming 0.15 to 0.66; humans who announced right 1.79 vs 0.24 | Failing to Falsify 2026 (c11) | [E] K01/K03 |
| Falsification prompts | average 42% to 56%; Think-in-Opposites up in 11 of 11 settings, Dual-Goal 8 of 11; I:C up in 18 of 22 | Failing to Falsify 2026 (c12) | [E] K02 |
| Transfer to math self-correction | Qwen3-8B AIME 2025 0.33 to 0.60 (p=0.039); Qwen3-32B 0.73 vs 0.80 (n.s.) | Failing to Falsify 2026 (d05) | [S] |
| Positive tests vs success | 12 models x 100 games; Spearman rho -0.779 (p=.003); GPT-5.2-Chat 75% with 27.3% positive tests; instruction-tuned 66-82% positive, 33-35% success | FalsifyBench 2026 (c14) | [E] K03 |
| WILT inductive games | best 14/50 (Claude 3.5 Sonnet 28%), GPT-4o 18%, Gemma 2 9B 0 | WILT 2024 (c15) | [S] |
| Misguided tests from buggy code | buggy code visible: misguided 137.69/model, effective 104.15; fixed code: 16.46 and 304.08; r=0.90 misguided vs effective count | Zhao 2026 (c16) | [E] K04 |
| Spec-first tests | docstring: effective 186.77; advanced docstring 230.23; 15-21% of docstrings kept the bug | Zhao 2026 (c17) | [E] K04 |
| Spec-grounded test writer | final correct 62% to 100% (+38 pp); false alarms 0% vs 33%; GPT-5.3-codex 72% to 100%; Gemini 3.5 Flash 72% to 92%; real library 90% vs 40% | Haeri 2026 (d06) | [E] K04 |
| Spec completeness | incomplete spec: detection 30/30 to 6/30; wrong endorsing rule: accuracy 82.8%, detection 30/30 | Haeri 2026 (d07) | [S] K25 |
| Weak test sets let wrong code pass | 80x tests: pass@1 down up to 19.3% (26 models); null input covered 34.8%, negative 23.8% | Liu 2023; BlindSpotEval (a23, c18) | [E] K05 |
| Self-correction without feedback | GPT-4 GSM8K 95.5 to 91.5 to 89.0; CommonSenseQA GPT-3.5 75.8 to 38.1; oracle labels help | Huang 2024 (c20) | [E] K06 |
| Self-repair vs resampling at matched compute | normalised pass rate 0.92-1.06 (no gain) | Olausson 2024 (c19) | [E] K06 |
| Failed attempt anchors small models | 1.5B: 0.749 resample vs 0.688 placebo; 3B 0.778 vs 0.709; 7B tie; near-identical retries 33-68% vs 2-14% | Verma 2026 (d01) | [C] K23 |
| Localised repair loses to blind resample | 3:40 (p=3e-9); span reproduced verbatim 48.9%; Mistral-24B 0.6% vs 11.9% | Jha 2026 (d03) | [C] K23 |
| Self-repair gains at scale | +4.9 to +17.1 pp (HumanEval), +16.0 to +30.0 (MBPP); Llama 3.3 70B 93.3 vs 90.9 resample | Arimbur 2026 (d02) | [C] K23 |
| Reasoning and bias | reasoning minus non-reasoning +0.031 (p=.157, dz=0.27); anchoring d=1.89; 79% of R1 calls over ceiling | Kraishan 2026 (b15) | [C] K10 |
| Chain-of-thought on anchors | lowers plausible-anchor influence in 11 of 15 cells (mean -0.06); above zero in 13; raises in 4 | AnchorBench 2026 (d16) | [C] K10 |
| Multi-estimate elicitation | 12 of 45 preregistered tests rejected; largest effect +10.68 pp more error; base-rate slopes near 1 | Jhang 2026 (d19) | [S] K28 |

## 4. Mechanisms and models

Each model below is written so an engineer can turn it into a check or a step.

**4.1 Positive test strategy (confirmation).** The agent holds hypothesis H. It picks tests t where H predicts "pass". Result: no test can separate H from rivals, so H survives. Quantity to log: share of tests that H predicts will pass versus tests where H predicts a failure. In people the ratio of infirming to confirming tests (I:C) separates winners (1.79) from losers (0.24) on 2-4-6 (c11). In LLMs, success tracks the positive-test share inversely (rho -0.779, c14). Implementation: for each candidate answer, code asks the model for a test whose expected result under H is "fail". Code runs it. A fail-detection score is the share of seeded wrong solutions the test set kills.

**4.2 Contaminated test writing.** A test writer who sees buggy code derives expected outputs from the code. Effect: 137.69 misguided tests per model versus 16.46 when code is fixed (c16). Mechanism: the code is an anchor on expected behaviour, not only on inputs. Implementation: write tests from the problem statement in a context that never holds the candidate code. Then run them. A rule list ("the rules a correct answer must satisfy") works as a checklist (Haeri, d06). Risk: the spec can itself inherit the bug (15-21% of generated docstrings, c17) or be incomplete (detection 30/30 to 6/30, d07). So derive the spec from the task text, not from the code.

**4.3 Anchoring as context copying.** A string that appears in context raises the probability of near copies. Evidence: anchor lines copied in 32-61% of Codex solutions (a17); near-identical retries 33-68% after a failed attempt (d01). Pathway matters. In AnchorBench the anchor in an external prompt moved models strongly (0.71 to 0.79 index) while history and in-context-example pathways were near zero for Claude Haiku 4.5 (d15; table garbled). Implementation: make anchor entry points a list (task text, memory notes, retrieved items, earlier answers, failed attempts). For each, decide whether the model needs to see it. If not, code removes it.

**4.4 Ignore-instructions do not cancel anchors.** Telling a person or model to disregard an anchor leaves it in place: obsolete requirements raised estimates in 6 of 6 experiments (b08, per critique); warning prompts moved SE bias sensitivity only 12.9% to 10.3% (b17); a "think cautiously" prompt raised anchoring on Llama 8B and Qwen 7B (34.7% to 36.8%, 40.0% to 43.0%, c26). The reliable fix is removal from the context, not instruction.

**4.5 Axiomatic cue.** Before answering, write the rule set a correct answer must satisfy. Effect: bias sensitivity cut about 51% (b18); anchoring plausible index 0.33 to 0.06 with an explicit rule (d17), while a vague judgment prompt gave 0.26. Why it plausibly works: it replaces an attractor (the anchor) with a stated criterion that is checkable. Limits: works where a rule can be stated; hindsight not helped; wide intervals; small and cheap models; no code-task data.

**4.6 Failed attempt contamination.** After a failure, the model reads its own wrong program. For small models this raises the chance of a near copy and lowers pass@1 below a blind resample (d01). Yang's model (d04): per-attempt success after a failure p1=0.113 versus p0=0.761 fresh; cascade ratio 7.1; independent-attempt model predicts pass@3 98.6% vs observed 81.2%. This model is theory fit to two numbers, with a heterogeneity rival explanation. Counter-evidence at scale: self-repair with real error feedback matches or beats resampling for 30B+ models and uses fewer tokens (d02). Implementation choice: at S5, offer two retry formats (failed code shown plus failing output, or clean task plus only the failing test) and measure.

**4.7 Self-rated vs actual.** Framing changes self-rated comprehensibility (path 0.165) but not actual performance (d=-0.006) (b09, b10). Implementation: do not trust stated confidence after a framing cue. Use computed pass rates.

**4.8 Bias complexity growth.** Bias sensitivity rises with task complexity (confirmation +33.66 pp per tier, a12). Plan for hard items, not just easy ones.

## 5. What holds up

**Holds up (two or more sources).**

- Positive test bias exists in humans and models. Human: Salman 2019 (86.5%), 1994 studies (abstract only). LLM: Failing to Falsify, FalsifyBench, Zhao (K01).
- A falsification prompt helps on rule games. Human RCT (78.33% vs 36.66%) plus LLM average 42% to 56% (K02). Only on 2-4-6 style tasks.
- Spec-first tests beat code-visible tests (K04). Two sources, Java and Python, both 2026.
- Self-review without an external signal does not help (K06). Huang 2024, Olausson 2024.
- Warnings and "ignore this" do not remove anchoring (K08). Human and LLM sources.
- Writing the rule first cuts bias (K12). PROBE-SWE and AnchorBench, both small and cheap models, both 2026.
- Anchoring by in-context code or numbers is strong in LLMs (K07).

**Replications and failed replications.**

- Zhou 2026 partly replicated Chattopadhyay 2020. Bias rate similar (47.14% vs 45.72%). Reversal link did not replicate (p=0.058; reversal 25% vs 52.9%). Settings and coding schemes differ, so this is a boundary condition, not a clean failure (a16).
- Salman 2019 replicates the positive-test tendency but not the logic link, and found no time-pressure effect (d09).
- No external replication of Calikli et al. 2010 was found. No randomised trial of logic or hypothesis-testing training in software testers was found (K14, K24).
- SynAnchors (reasoning models anchor less) and Kraishan (no difference) disagree (K10, K11). AnchorBench CoT sides closer to Kraishan.
- Anchoring is strong in Malberg (0.39) and weakest in PROBE-SWE (5.9%). Different measures: signed score on managerial scenarios versus decision flip rate on SE vignettes. PROBE-SWE 2025 and 2026 are the same group and benchmark, not independent.

**Moderators.**

- Spec completeness: more complete spec lowers positive test bias (Leventhal 1994, abstract only); incomplete spec cut LLM detection 30/30 to 6/30 (d07).
- Expertise: reduces bias in 1994 abstracts; Calikli found no experience correlation (a06). Calikli's students beat staff on abstract questions, but not when experience was matched (a08).
- Task type: the gap vanishes on well-specified algorithmic tasks (HumanEval+, Haeri) and on 8 logic tasks.
- Model strength: failed-attempt penalty shrinks with model strength (r=0.96 with baseline quality, d01); self-repair helps stronger models (d02).
- Complexity: confirmation grows with tier (+33.66 pp, a12).
- Anchor pathway and plausibility (d15): plausible anchors near the evidence move models most; far anchors weaken.
- Content: both humans and models do better when the rule content matches belief, poorly on abstract rules (a22). Humans did not beat chance on the abstract Wason task overall.
- Instruction tuning: instruction-tuned models test positives most (66-82%, c14); one abstract-level source says instruction tuning raises some biases (a24) (K20, [C]).

**Interventions that worked.**

- Think-in-Opposites / Dual-Goal on 2-4-6 (humans and LLMs).
- Spec grounding for test writers (+38 pp, Haeri).
- Axiomatic cues (about 51% cut).
- Awareness workshop partly (Shepperd).
- Activation steering cut bias scores 26-32% (d18). Needs model internals; not available to us.
- Selective prompt anchoring (c24) is a different meaning of "anchoring": it boosts spec tokens at decoding and gains up to +12.9 points. Needs logit access. Name overlap only.
- Removing the anchor is implied by K08 but was not tested as its own arm.

**Interventions that did not work.**

- "Be careful / think cautiously" prompts (c26: worse on two small models).
- Chain-of-thought as a debiaser (16.1% vs 12.9%).
- Bias warning alone: 10.3% vs 12.9%, modest.
- Instructions to ignore obsolete requirements (human, 6 of 6 experiments).
- Generic prompt debiasing on judgment biases (-4.4%).
- Asking for five weighted estimates (Jhang): 12 of 45 tests rejected, base-rate items at ceiling.
- Intrinsic self-correction (Huang).
- Feedback content on small models in the contamination test: feedback minus placebo +0.000/+0.026/+0.008, none significant (d01).

**Weak spots.**

- The core human claim rests on one 2010 study with N=88, Mann-Whitney on small groups, setting differences, and a reported p that does not match its z (a08).
- Defect link: 5 developers and 12 testers, no test.
- Zhou's own numbers conflict (949 vs 983 biased; chi-square 22.94 vs 30.72). Use ranges 47-49% and 54-56%.
- Zhao's misguided-test count correlates r=0.90 with effective tests, so it partly tracks volume.
- 2026 preprints (Failing to Falsify, FalsifyBench, Zhao, Haeri, Verma, Jha, AnchorBench, Jhang) are single-team and not independently replicated.

## 6. Language models

**Do models show the human biases?** Some do, depending on how it is measured.

- Anchoring on numbers: GPT-3.5 high-anchor mean 105.97 vs low 20.83 (c04). 20-model mean 0.39 (b13).
- Anchoring on code: Codex framing line in 81% of outputs (a18); wrong-anchor lines copied 32-61% (a17).
- Confirmation in test choice: strong. Instruction-tuned models test positives 66-82% (c14). Best models 24-39%. Success follows (rho -0.779).
- Confirmation in vignette judgment: weak and model-dependent (0.15 mean, -0.18 to 0.72, b13). Kraishan finds the opposite direction in all 7 models (K13). Treat as two separate constructs: choosing tests (strong) versus judging a vignette (weak).
- Optimism, planning fallacy, escalation: near zero (0.06, -0.02, 0.07; c08).
- Availability: Codex flipped operation order 50% to 17% (a19). Malberg mean 0.11.
- Developers using LLMs: 54-56% of LLM-involved actions are biased (b19).

**What changed bias, and by how much.**

| Lever | Change | Model scale | Source |
|---|---|---|---|
| Force falsifying tests (TiO, Dual-Goal) | success 42% to 56% average; Qwen3-32B 0.41 to 0.61 | 8B-32B plus Gemini 2.5 Pro | c12 |
| Distil from TiO traces | Qwen3-8B Wason 0.21 to 0.59 | 8B | c13 |
| Spec-grounded tests | +38 pp final correctness; false alarms 33% to 0% | Haiku/Sonnet/Opus 4.x, GPT-5.3-codex, Gemini 3.5 Flash | d06 |
| Spec instead of code to test writer | effective tests 104.15 to 186.77 (230.23 with advanced prompt) | 11 LLMs | c17 |
| Axiomatic cue | bias 12.9% to 6.3-7.5% | mini/8B/70B | b18 |
| Explicit rule on anchors | index 0.33 to 0.06 | open-weight panel | d17 |
| Self-debias rewrite | framing: 2.7% of biased elements left | GPT-4 only works well | a21 |
| Chain-of-thought | 12.9% to 16.1% (worse); AnchorBench mean -0.06 | mixed | b17, d16 |
| Warning | 12.9% to 10.3% | small | b17 |
| Activation steering | bias score -26 to -32% | 70B-72B | d18 |
| Reasoning on/off | code pass: Qwen3-32B 71.1% to 76.5% on HumanEval Pro; not a bias probe | 32B | d20 |

**Frontier coverage is thin.** PROBE-SWE 2026 says frontier models were not tested. Failing to Falsify tested Gemini 2.5 Pro (success 0.73, I:C 0.66), the only strong model with an intervention. Haeri used 2026 frontier models but on small pure functions. Kraishan used 7 models. AnchorBench found frontier API models above 95% control accuracy still shifted by plausible anchors (d15).

**Failed attempt in context (K23, [C]).** Small models (1.5B, 3B) do worse with their failed code in view than with a blind resample (-6.1 and -6.9 points). 30B+ models with real feedback do equal or better with self-repair. Nobody tested a frontier reasoning model. Accurate summary: the penalty shrinks with model strength, and it is unknown whether it reaches zero for the models we run.

**LLMs inside human workflows.** Fixation on the first suggestion has the highest reversal (43.4%) in Zhou's sample of 14 developers. Only one observational study exists.

**Cautions.** Do not count a low bias score as robustness. Low scores can mean the model failed the task (b21, b22). Pair each score with task accuracy (K19).

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| At S4, for each candidate, code requires at least one test the agent predicts will fail if the candidate is wrong. The "falsify" line is a slot with a count, not a mood. | G3, S4 | [E] on rule games; on code unproven (K02) | c11, c12, c14, d12 |
| Write tests from the task statement in a context that never contains candidate code. | G3, S4, S3 | [E] K04 | c16, c17, d06, d08 |
| Evaluate answers against extended and mutated inputs, not only the given examples. Report the drop. | G3, S4, S8 | [E] K05 | a23, c18 |
| Revise only on code-located failing output, never on self-critique alone. | G2, S5 | [E] K06 | c19, c20, a25 |
| Do not use "be careful", "ignore X" or a bias warning as a fix. Remove the cue from the context instead. | G3, S1 (input hygiene) | [E] K08 | b08, b17, c26, a13 |
| At S1 list the rules a correct answer must satisfy, before generating. Test against them in S4. | S1, G3 | [E] K12 (small and cheap models) | b18, d17, d18 |
| Log, per run, the share of falsifying tests and the final correctness. | G7 measurement | [E] K03 | c14, c11 |
| Treat all human-derived debiasing advice as hypotheses. | G7 | [E] K16, K24 | a02, d22 |
| Do not trust the agent's stated confidence after a framing cue. Use measured pass rates. | G6, G10 | [E] K18 | b09, b10 |

### Test first

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Forced falsification step (TiO / Dual-Goal) raises fix correctness on real code at equal tokens. | S4, S7 | [S] for code (no code test exists) | c12, d05, d12 |
| Retry from clean context (task plus only the failing test) versus retry with the failed code shown. | S5, S6, G3 | [C] K23 | d01, d02, d03, d04 |
| Spec derived from the task text, code hidden, versus code visible, on non-Java tasks. | S4 | [S] K04 gap | c16, d06 |
| Complete rule list versus partial rule list. | S1, S4 | [S] K25 | d07, d10 |
| Input hygiene: move suggestive cues (stated guess, number, authority claim) into a marked block, or remove them. | S1 | [S] | a17, d15, b08 |
| Check anchor entry pathways (memory notes, retrieved notes, earlier answers). | S1, S9, memory | [S] K26 | d15 |
| Neutral restatement step at S0/S1. | S0, S1 | [S] K22 | a21, b14 |
| Thinking budget as a bias lever. | G11 | [C] K10, K11 | b15, c25, d16 |
| Reference-class base rate prompt for the agent's stated success probability. | S0, S9 | [S] K28 | d19 |
| Cue wording ("this is easy") on stated confidence. | G10 | [S] K27 | b09, d21 |
| Base versus instruct model on the falsification probe. | none | [C] K20 | a24, c14 |

## 8. Concrete tests on our bench

Rule for all: both arms get the same total token budget, set by the plain arm's mean; setup cost counts (G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Forced falsification at S4 | ARC-like fit-the-examples items and code-fix items with seeded wrong candidates that pass the given examples | plain; plain + one "name a test that would fail if wrong" slot run by code | share of wrong candidates killed; final accuracy | fail-detection up; accuracy up on items where a wrong rule fits all examples. Rule games gave 42% to 56%. Code items unknown. |
| T2 Clean-context retry | items where the first attempt fails: ARC and code | (a) failed code plus output shown; (b) original task plus only the failing test; (c) blind resample | pass@retry; similarity of attempts; tokens | (b) or (c) at or above (a) on small models; near equal on frontier (d01, d02) |
| T3 Spec-first tests | code tasks with missing-validation bugs | tests written with candidate visible; tests from the task text only; tests from an explicit rule list | bugs caught; false alarm rate; final correctness | rule list best; code-hidden above code-visible (Haeri +38 pp; Zhao 104 to 187) |
| T4 Rule-first at S1 | brain-teaser and ARC items with a tempting wrong answer | plain; plain + "list rules a correct answer must satisfy" then test | accuracy; flip rate on paired cued/uncued prompts | bias sensitivity down, as in b18 (about 51%), smaller on frontier |
| T5 Input hygiene | each item paired with a version with a planted guess or number | cue in prompt; cue removed by code; cue in marked block; "ignore the cue" instruction | accuracy gap between paired versions | removal closes the gap; ignore instruction does not (K08) |
| T6 Anchor pathway | multi-step runs with memory notes | wrong note in prompt; in history; retrieved | answer shift toward the note | pathway-dependent (d15) |
| T7 Thinking budget | same base model, thinking on or off | same schema; two budgets | anchoring and falsification scores paired with accuracy | unknown; resolves K10/K11 |
| T8 Confidence framing | same task with "easy" or "hard" cue | stated confidence versus measured pass | confidence gap, accuracy gap | confidence moves, accuracy does not (b09, b10) |
| T9 Base-rate prompt | tasks with known class pass rate | agent states success probability without and with class base rate | Brier score of stated probability | small at best (Jhang: ceiling) |

## 9. What does not transfer, and why

- **Planning poker, multiple designs, directed questions** (a26). Human-team estimation tools. Unevaluated even for humans, and our agent does not estimate effort with a team.
- **Awareness workshops.** An LLM cannot be trained in a session. A system prompt warning is the nearest thing, and it moved bias only 12.9% to 10.3% (b17).
- **Logic training reducing confirmation bias.** One correlational study, no randomised trial, no replication (K14). A prompted falsification step is the only transferable form, and its evidence is on rule games.
- **Optimism and planning fallacy.** Near zero on models (c08). Do not spend schema space on them.
- **Time pressure effect.** Not found even in humans (d09, d=-0.357).
- **Activation steering and selective prompt anchoring.** Need model internals or logit access (d18, c24).
- **Expertise as moderator.** Our agent has no career. The nearest analogue is model strength, which does moderate (d01, d02).
- **Defect-bias link.** 5 developers and 12 testers (a09, a10). Nothing to transfer.
- **Human-LLM workflow biases (Zhou).** They describe developers, not an autonomous agent. Only the fixation finding hints at a process lesson (force a second independent candidate; K17).
- **Student and company-size differences.** Setting confounded (a08).
- **Vignette bias scores.** Hypothetical choices on short text. They say little about behaviour inside a code loop. Test choice is the bias that matters.

## 10. Open questions

1. Does a forced falsification step raise fix correctness on real code, at equal tokens, on a frontier model? (No code test exists.)
2. Does leaving a failed attempt in context hurt a frontier reasoning model? Only 1.5B-7B (hurt), 24-32B (hurt for localized edits), and 8B-70B+ (self-repair equals or beats resampling) were tested.
3. Do reasoning models anchor and confirm less? SynAnchors says yes; Kraishan and AnchorBench say little. No common probe.
4. Code-visible versus code-hidden test writing, everything else fixed, on non-Java code.
5. What share of generated specs inherit the bug as a rate, not an injected case?
6. Any randomised trial of logic or hypothesis-testing training in human testers? Any replication of Calikli 2010? The PROMISE 2010 and 2015 papers were not opened.
7. Leventhal 1994 numbers (spec completeness, domain knowledge) were not read.
8. Does a reference-class base rate reduce an agent's optimism about its own success? Nobody has tested it.
9. Do "this is easy" cue words move an agent's stated confidence while accuracy stays flat?
10. What is the cost-benefit of axiomatic cues on frontier models and on code tasks?
11. Base versus instruct models on the same falsification probe.
12. Does training on falsification traces generalise to debugging? Failing to Falsify showed an AIME effect for 8B only and says debugging was untested.

Links to subfields researched in parallel (not covered here): Debiasing and cognitive forcing; Cognitive bias and premature closure; Conformity; Calibration and overconfidence; Belief updating; Software, spreadsheet, KB debugging.

## 11. Sources

[V] = opened this session or by the cross-check. [M] = snippet or abstract only.

- [V] Mohanani, Salman, Turhan, Rodriguez, Ralph (2020) Cognitive Biases in Software Engineering. https://arxiv.org/abs/1707.03869 (PDF https://arxiv.org/pdf/1707.03869)
- [V] Calikli, Arslan, Bener (2010) Confirmation Bias in Software Development and Testing (PPIG). https://ppig.org/files/2010-PPIG-22nd-Calikli.pdf
- [M] Calikli and Bener (2010) PROMISE companion. https://oro.open.ac.uk/45352
- [V] Salman, Turhan, Vegas (2019) Time pressure and confirmation bias in software testing. https://link.springer.com/article/10.1007/s10664-018-9668-8
- [M] Leventhal, Teasley, Rohlman (1994) positive test bias in software testing. https://doi.org/10.1006/ijhc.1994.1079
- [M] Teasley, Leventhal, Mynatt, Rohlman (1994) Why software testing is sometimes ineffective. https://doi.org/10.1037/0021-9010.79.1.142
- [M] Wason (1960) On the failure to eliminate hypotheses. https://doi.org/10.1080/17470216008416717
- [M] Aranda and Easterbrook (2005) Anchoring and adjustment in software estimation. https://doi.org/10.1145/1081706.1081736
- [M] Fischhoff (1982) Debiasing, via Mohanani. https://arxiv.org/pdf/1707.03869
- [V] Shepperd, Mair, Jorgensen (2018) An experimental evaluation of a de-biasing intervention. https://arxiv.org/abs/1804.03919
- [V] Gren and Svensson (2021) Is it possible to disregard obsolete requirements? https://arxiv.org/abs/2103.13265
- [V] Wyrich, Merz, Graziotin (2022) Anchoring code understandability evaluations. https://arxiv.org/abs/2203.13705
- [V] Wyrich, Preikschat, Graziotin, Wagner (2021) The mind is a powerful place. https://arxiv.org/abs/2012.09590
- [M] Chattopadhyay et al. (2020) A tale from the trenches (ICSE), numbers via Zhou. https://doi.org/10.1145/3377811.3380330
- [V] Zhou, Saghi, Sabouri, Pandita, McGuire, Chattopadhyay (2026) Cognitive biases in LLM-assisted software development. https://arxiv.org/abs/2601.08045 (HTML https://arxiv.org/html/2601.08045v1)
- [V] Jones and Steinhardt (2022) Capturing failures of large language models via human cognitive biases. https://arxiv.org/abs/2202.12299
- [V] Suri et al. (2023) Do LLMs show decision heuristics similar to humans? https://arxiv.org/abs/2305.04400
- [V] Malberg, Poletukhin, Schuster, Groh (2025) A comprehensive evaluation of cognitive biases in LLMs. https://arxiv.org/abs/2410.15413
- [V] Sovrano, Dominici, Sevastjanova, Stramiglio, Bacchelli (2025) Is general-purpose AI reasoning sensitive to data-induced cognitive biases? https://arxiv.org/abs/2508.11278
- [V] Sovrano, Dominici, Bacchelli (2026) Mitigating prompt-induced cognitive biases (PROBE-SWE). https://arxiv.org/abs/2604.16756
- [V] Kraishan (2026) The long road to the same answer. https://arxiv.org/abs/2610.10049
- [V] Echterhoff, Liu, Alessa, McAuley, He (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811
- [V] SynAnchors (2025) Empirical study of the anchoring effect in LLMs. https://arxiv.org/html/2505.15392
- [V] Borjigin, Hermann, Cyron, Aydin (2026) AnchorBench. https://arxiv.org/abs/2608.14320
- [V] Huang, Zhang, Kwak, An (2026) CogBias. https://arxiv.org/abs/2604.01366
- [V] Jhang (2026) Multi-estimate elicitation does not uniformly debias. https://arxiv.org/abs/2611.00597
- [V] Tommasel and Schedl (2026) Measuring human-like bias in LLMs. https://arxiv.org/abs/2610.00070
- [M] Itzhak, Stanovsky, Rosenfeld, Belinkov (2024) Instructed to bias. https://arxiv.org/abs/2308.00225
- [V] Jhaveri et al. (2026) Failing to Falsify. https://arxiv.org/abs/2604.02485 (HTML https://arxiv.org/html/2604.02485)
- [V] FalsifyBench (2026). https://arxiv.org/html/2606.04751
- [V] WILT (2024). https://ar5iv.labs.arxiv.org/html/2410.10998
- [V] Branchini et al. (2025) Thinking in opposites. https://doi.org/10.3758/s13421-025-01691-3
- [V] Sellier, Scopelliti, Morewedge (2019) Debiasing training improves decision making in the field. https://doi.org/10.1177/0956797619861429
- [V] Lampinen, Dasgupta et al. (2024) Language models show human-like content effects on reasoning. https://arxiv.org/abs/2207.07051
- [V] Zhao, Zhou, Cohen (2026) Misguidance effect of buggy code on LLM test generation. https://arxiv.org/html/2607.22883v1
- [V] Haeri and Ghelichi (2026) Specification grounding drives test effectiveness. https://arxiv.org/abs/2607.06636
- [V] Ma and Eisty (2026) From business requirements to test assertions. https://arxiv.org/abs/2607.10277
- [V] Liu, Xia, Wang, Zhang (2023) Is your code generated by ChatGPT really correct? https://arxiv.org/abs/2305.01210
- [M] BlindSpotEval / ObligBench (2026). https://arxiv.org/abs/2610.32548
- [V] Tian and Zhang (2024) Selective prompt anchoring for code generation. https://arxiv.org/html/2408.09121v5
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Olausson et al. (2024) Is self-repair a silver bullet? https://arxiv.org/abs/2306.09896
- [M] Sharma et al. (2023) Sycophancy. https://arxiv.org/abs/2310.13548
- [M] Justice or Prejudice? LLM-as-a-judge biases (2024). https://arxiv.org/abs/2410.02736
- [V] Verma (2026) Try again, don't look back. https://arxiv.org/abs/2607.26117
- [V] Arimbur (2026) How many tries does it take? https://arxiv.org/abs/2604.10508
- [V] Jha (2026) Does fault localization beat a fresh attempt? https://arxiv.org/abs/2609.00854
- [V] Yang (2026) Why retrying fails: context contamination. https://arxiv.org/abs/2605.08563
- [V] Huang, Pang, Zhang, Cheng, Ma (2026) Does more thinking pay off? https://arxiv.org/abs/2610.36952
- [M] Impact of request formats on effort estimation (2025). https://doi.org/10.1145/3715771
- [V] Gap-search results 2026-11-10 (OpenAlex queries, partial coverage). https://api.openalex.org/works
