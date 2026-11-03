# Divergent thinking: deep document

*Subfield A09.08. Scope: convergent versus divergent thinking, Guilford's tests, Runco's argument that divergent thinking (DT) is not all of creativity, and every LLM study found that tests or uses DT tasks (2020-2026). Evidence ids (a01..d16) point to evidence_a-d.jsonl in this folder. Claim ids (K01..K21) point to claims.jsonl. Status marks: [E] established, [S] single-source, [C] contested.*

**Honest gap up front.** The founding sources (Guilford 1950 and 1967, Runco 2008, Mednick 1962, Acar et al. 2020) could not be opened. They are paywalled or books. Section 2 describes them from secondary text only and carries no founding numbers. Every exact number below comes from sources that were opened (marked [V] in section 11), except the two lines marked "snippet".

## 1. What it is

**Divergent thinking (DT)** is producing many different answers to an open prompt that has no single right answer. Example: "Name uses for a brick." **Convergent thinking** is narrowing to one best answer, such as a riddle or a Remote Associates Test item.

The tests in common use:

- **Alternative Uses Task (AUT).** Give uses for an everyday object (brick, rope, fork, tin can, tire). Scored on four things:
  - fluency: number of ideas;
  - flexibility: number of categories the ideas fall in;
  - originality: how rare or novel the ideas are;
  - elaboration: detail, often just word count.
- **Consequences task.** List what would follow from an odd event.
- **Divergent Association Task (DAT).** Name 10 words as unrelated to each other as possible. The score is the mean semantic distance between the words, scaled so humans average about 77 (a14, c01). It takes under 4 minutes and has a 100,000-person human norm (a19).
- **Forward Flow (FF), Forms of Fiction, Remote Associates Task (RAT).** FF measures how far a stream of thought drifts. RAT is convergent: find the word that links three cues.

**Scoring methods.** Four families:

1. Human rating on a 1-5 scale (the subjective top-2 method of Silvia et al. 2008, seen only via citation, a28).
2. Uniqueness counts (rare responses within a sample).
3. Semantic distance (SD): embedding distance between the object and the response, or between words. The SemDis tool uses five models and a multiplicative composition (a23).
4. LLM raters trained on human ratings.

**Why it matters for our agent.** The agent has an open mode (schema S3, O7). We need a metric for whether open mode works. DT tasks give cheap, scorable open-mode metrics. But Runco's argument is that DT is only one component of creativity, so a DT score alone cannot be the only open-mode metric (K10).

## 2. History and theories in depth

All of this section is secondary text unless stated. Treat it as background, not as verified founding numbers (a18, a26, a27, a28, d16).

**Guilford (1950, 1967).** Guilford separated divergent production from convergent production in his Structure of Intellect model. He proposed the AUT. Fluency, flexibility, originality and elaboration come from this line of work. The core claim is that DT is an ability separate from general intelligence. Later data support a weak form: DT and intelligence correlate only r = .25 (b01).

**Mednick (1962).** Creativity as a flatter associative hierarchy: creative people reach remote associates more easily. The Remote Associates Test (convergent) came from this. The same idea sits under semantic-distance scoring and the DAT. See the semantic-networks subfield (not covered here).

**Geneplore (Finke 1992).** Creative work alternates generation of preinventive structures with exploration of them (a18). This maps to our generate and select stages. See the dual-process creativity subfield.

**Runco (2008): "Divergent thinking is not synonymous with creativity."** The argument as cited by Stevenson et al. (a04, a26): DT tests measure one component of creative potential. They estimate potential, not creative achievement. Real creative work also needs problem finding, evaluation, knowledge, motivation and convergent steps. The text of Runco 2008 was not opened. The empirical backing is in section 5: DT scores do not consistently predict other creative outcomes (b14, a24). DT and evaluative skill are only weakly linked (b24, snippet only, r = .13).

**Runco and Jaeger (2012).** The standard definition: creative = novel plus useful (a18). This is why our agent must score originality and utility together (K05).

**Competing accounts of how ideas arise.** Persistence (deep search in few categories) versus flexibility (many category jumps) are two routes to similar scores in humans (a05, a25). The controlled-attention account says executive control (goal maintenance, inhibiting near concepts, switching) drives DT (a13). The associative account (Mednick) says memory structure drives it. Not resolved. See the executive-function and network-neuroscience subfields.

**The LLM turn (2022 onward).** Stevenson et al. (2022) ran the first psychological AUT on GPT-3 (a01). GPT-4 then beat the average human (c01), but the best humans still match or beat it (a10, a19). The live problem is homogeneity (a21, c15). Section 6 covers this.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| DT and intelligence correlate weakly | r = .25, CI [.21,.30]; 112 studies, 849 correlations, N = 34,610; I2 = 92% | b01 Gerwig 2021 | [E] |
| Fluency-only scoring relates least to intelligence | fluency r = .20; composite r = .37 (not robust to sensitivity checks); contrast z = -3.75 | b02 | [E] |
| Instructions moderate the DT-intelligence link | game-like instructions: no significant correlation; best fit be-creative + originality scoring, r about .31-.37; QM(2) = 25.94 | b03 | [E] |
| No threshold effect in DT vs intelligence | N1 = 456, N2 = 438; r = .19 and .27; no slope change at any breakpoint | b05 Weiss 2020 | [E] (German samples) |
| Serial-order effect (later ideas more original) is real but tiny | N = 4,752 responses; d = 0.31 (subjective), 0.38 (frequency), 0.06 (semantic similarity); at most 3.5% variance; slope ICC < .31 | b06 Barbot 2026 | [E] |
| Semantic distance tracks human originality ratings | Study 1 N = 171 latent r = .91; Study 2 r = .75; Study 3 (brick) r = .45; Study 5 single models r = .76-.82 | a23, b08 Beaty and Johnson 2021 | [E] |
| Word count: negative with SD, positive with human ratings | r = -.25 vs .41; additive composition r = -.37 | a23 | [E] |
| SD vs subjective rating in an LLM-vs-human study | mean r = .55 [.46,.62]; max r = .52 [.43,.60] | a12 Koivisto 2023 | [E] |
| LLM scoring of originality agrees with experts | ICC > .80, r >= .70 in selected studies; weaker outside English | a16, b14 (review) | [E] at group level |
| Originality and utility trade off | r = -.56 (humans), -.61 (GPT-3) | a02 Stevenson 2022 | [E] |
| GPT-3 vs 42 humans, AUT | humans higher on originality (beta .17), surprise (.14), SD (.10); utility beta -.55 (GPT-3 higher); 144 GPT-3 runs | a01 | [E] (old model) |
| GPT-4 vs 151 humans, fluency matched post hoc | AUT originality F(1,600) = 622.10, eta2 = .51; fluency 6.94 vs 7.01; DAT 84.56 vs 76.95, t(300) = 13.65 | c01 Hubert 2024 | direction [E]; size [C] |
| GPT-4 answers are longer | AUT elaboration 15.45 vs 3.38 words, t(602) = 28.57 (the 38.69 vs 5.45 figure is the Consequences task) | c02, critique | [E] |
| GPT-4 repeats a small DAT word set | only 9.11% (n = 97) overlap with human words; elephant 55 and symphony 51 of 151 | c03 | [S] |
| 256 humans vs 3 chatbots, prospective fluency control | mean SD B = 0.049, t(274) = 4.949; max B = 0.027 (p = .003, not significant in post-hoc tests); subjective mean B = 0.453 | a10, b12 Koivisto 2023 | [E] |
| Best humans still match or beat the best AI | in 7% of trials the human max rating was < 2; AI never | a10 | [E] |
| Fluency confound | more responses lower mean originality and raise the max: B = -0.012 (mean SD), +0.011 (max SD) | a11 | [E] |
| 100 humans vs 5 chatbots (+GPT-4), AUT | mean originality B = -0.21, p = .218 (human raters); 32.8 humans beat the best of five chatbots per prompt; 9.4 humans beat GPT-4 (AI rater only, per-prompt counts 2, 29, 0, 3, 13) | a08, b10 Haase and Hanel 2023 | [E] |
| Effect size depends on fluency control | Hedges g: 2.61 [2.30,2.91] (post hoc matching); 0.70 [0.33,1.06] (prospective); 0.52 [0.39,0.64] (DAT vs 100,000); vs top 50% of humans g = -0.88 | a15, b13 (2026 review) | [E] on the dependence; not pooled |
| DAT: GPT-4 above the human mean, below top humans | GPT-4 at temperature 1.5 mean 85.6, above 72% of humans (n = 500 per condition); top human decile/quartile/half beat every model | a19, c04, c05 Bellemare-Pepin | [E] |
| 14 LLMs on AUT in 2025 | percentile means 65.66-77.85 (all p < .001 vs 50); only 0.28% of responses in the top 10% of humans | c07 Haase 2025 | [S] |
| Model-version drift on DAT | GPT-4o (Feb 2025) 77.34 vs GPT-4 84.56, d = 2.41; vs Cropley GPT-4 82.54, d = 2.04 | c08 | [C] (different studies) |
| Naming the DAT raises scores | aware 60.16 vs unaware 52.56 percentile, B = 11.89; per model d: Claude 3.5 1.82, Grok 2 1.08, o3-mini 0.60, R1-Distill-Qwen-7B -0.42 | c09 | [S] |
| Prompt strategy on DAT | etymology beat plain for GPT-3.5 and GPT-4; opposition hurt; thesaurus helped GPT-4 only | a20, c05 | [S] |
| LLM individual originality equals or beats humans; population variability far lower | AUT originality 0.711 vs 0.696 (d = 0.1); variability 0.459 vs 0.699 (d = 1.8); DAT 0.632 vs 0.791 (d = 1.1) | a21 (22 LLMs, 102 humans) | [S] |
| Same pattern, second study | AUT variability 0.459 vs 0.738; FF 0.534 vs 0.835; DAT 0.665 vs 0.819 | c13, b21 Wenger and Kenett | [E] with a21 |
| Creative system prompt barely helps | AUT individual originality 0.711 -> 0.754 (very creative); variability 0.459 -> 0.576, still far below humans 0.738 | b21, c14 | [E] |
| Within-model homogeneity | 79% of queries have mean pairwise similarity > 0.8 (random pairs 0.1-0.2); across models 0.71-0.82 | b19, c15 Jiang 2025 | [C] |
| Hivemind threshold is weak | same-prompt, different-idea pairs: median cosine 0.723 and 0.703; 20-32% exceed 0.8; Hivemind pairs exceed 0.8 about 2-3 times as often | d05 Schaeffer 2026 | [C] preprint |
| Min-p does not cure it | 81% of pairs above 0.7, 61.2% above 0.8 | c16 | [S] |
| Temperature is not a creativity dial | beta .308 to novelty, .240 to incoherence; AUT jumps unaffected | b16, a07 | [E] |
| NoveltyBench | 1,100 prompts, 20 models; frontier models < 3 distinct answers in 10 samples; closed-model cumulative utility < 4 of 10; classifier agrees with humans 79% | b17, c18 | [E] |
| In-context regeneration restores diversity | roughly human-writer level on 100 prompts, 8 generations, 3 models | b18, c19 | [E] with d03 |
| Verbalized Sampling | diversity x1.6-2.1; human-rated story diversity 2.74 direct vs 3.06 VS; quality +25.7%; recovers 66.8% of base diversity | c23, d03 | [S] (one team) |
| Typicality bias in preference data | beta .569 (SE .073) and .649; OR 1.42-1.47 | d04 | [S] correlational |
| Persona and anti-modal phrasing | effective rank 17.4 -> 28.9 (+66%) and 43.7 -> 120.2 (+175%); countable ideas 3.34 -> 3.99 | d06 | [C] preprint |
| Sample-then-ban consensus | diversity +85-167%, consensus phrases -43 to -95%; N = 16 users | d14 | [S] pilot |
| Persona + extreme temperature | pairwise cosine 0.85 -> 0.65 on open models < 20B | d15 | [S] |
| Short "wild, bold" cues beat long method prompts | +10% to +41% on novelty/rarity metrics; 81 briefs, 567 variants, 25 strategies | d11 IDEAFix | [E] with d06 |
| Goal-blind diverge then narrow | AUT originality 2.91 -> 3.77, elaboration 4.36 -> 4.97 (GPT-5.4, 3 runs); MUTATE paths 27/56 -> 38/56 | d01, d02 | [S] no equal-token control |
| LLM research ideas rated more novel than expert ideas | 4.84 vs 5.64 (5.81 reranked); 79 reviewers, 49 ideas per arm; ~200 of 4,000 seeds non-duplicate | b22, c20, c21 Si 2024 | [S] |
| LLM ranker accuracy on idea quality | 71.4% (Claude-3.5-Sonnet), 63.5% (Claude-3-Opus) | c22 | [S] |
| Strategy lists lower later human originality | test-phase H(2) = 9.14, p = .010; strategies vs no-LLM p = .009; N = 460 on AUT, 9,457 ideas | d10 Kumar 2025 | [S] |
| ChatGPT users' ideas more alike across users | distance from mean .24 vs .28, d = .47, p = .038; N = 36 | a22 Anderson 2024 | [C] |
| Random far analogies help humans; LLMs only when far and strong | 140 humans, 7 LLMs, 1,002 raters | d12 Liu 2026 | [S] |
| Capability confounds creativity tests | creative-achievement scores correlate with general capability up to 0.98; DAT validity on creative writing +0.51 to +0.71; no test significant on scientific ideation (n = 21) | d07 | [S] |
| DT diversity falls while writing rises over release dates | -0.47 z/year DT diversity; +1.22 creative writing; +1.00 science ideation (54 models) | d08 | [S] |
| Explicit-instruction meta-analysis | g about .24-.27 (snippet, unverified) | b23 | unverified |
| DT vs evaluative skill | r = .13 [.07,.20]; 20 studies, N = 3,019 (snippet, unverified) | b24 | unverified |

## 4. Mechanisms and models

Written so an engineer can build each one.

**4.1 Scoring pipeline (what an open-mode metric needs).**

1. Collect ideas as separate strings. Strip style tells (numbering, "Use a X to ...") before any rating; this lifted human-rater ICC for originality from .57 to .78 (a02).
2. Embed each idea. Semantic distance = 1 - cosine between the object word and the idea. Use a multiplicative composition across several embedding models (SemDis), not an additive one, or long answers are punished (a23: additive r = -.37, multiplicative r = .91 in Study 1).
3. Control response length. Word count correlates -.25 with SD but .41 with human ratings (a23).
4. Add an LLM rater trained on human ratings as a second scorer. Require agreement between the two (K11).
5. Report **mean** and **max** originality separately, plus fluency. Mean falls and max rises as fluency rises (a11). A model with more ideas looks worse on mean and better on max.
6. Report utility next to originality. The trade-off is r = -.56 to -.61 (a02).
7. Report population diversity across samples, not only per-idea originality (4.2).

**4.2 Diversity measures (the homogeneity side).**

- Population variability: mean pairwise embedding distance between responses from different runs (a21, c13).
- Pairwise cosine similarity above a threshold (0.8 in Hivemind). Caveat: the threshold is weak. For genuinely different ideas on one prompt the median cosine is already 0.70-0.72 (d05). Use both an unrelated-prompt null and a same-prompt different-idea null.
- Effective rank / participation ratio of the embedding matrix (d06).
- Distinct-k, the NoveltyBench method: an equivalence classifier groups outputs; count classes among 10 samples. The classifier agreed with humans 79% (b17).
- Count of distinct ideas by LLM or human coding. Embedding spread moves more than the idea count (d06: ideas 3.34 -> 3.99 while effective rank rose 66-175%).
- Repeated words: share of tokens on the top-10 words (25.5% in small base models, c25), and share of runs containing one word (microscope 70%, elephant 60%, ocean > 90%; a20, c06).

**4.3 Why LLM output is homogeneous (proposed).** Preference data rewards text that a base model finds likely (beta .57-.65, d04). RLHF sharpens the policy toward the mode. The result is mode collapse on open prompts. The evidence is correlational and from one team. Sampling temperature adds noise but does not move the mode (b16, a07, c16).

**4.4 Interventions as algorithms.**

- **List-then-dedupe.** Ask for K ideas; embed; drop any within cosine 0.8 of an earlier idea. In Si et al. the non-duplicate share fell as the pool grew (c21).
- **In-context regeneration.** Call 1 gives an answer. Call 2 shows all earlier answers and asks for a different one. Repeat to 8. Matched human-writer diversity on NoveltyBench (b18). It is sequential and the context grows.
- **Verbalized sampling.** One prompt: give N answers with probabilities that reflect their likelihood; sample or pick from the low-probability tail. Beat direct, CoT, sequence and multi-turn at the same N responses on creative writing (d03). Not tested on AUT or DAT.
- **Sample-then-ban.** Sample K = 12; find the centroid and repeated phrases; regenerate with those as negative concepts (d14).
- **Persona anchoring.** The model first picks an idiosyncratic persona, then answers as it (d06, d15). Persona and extreme temperature changed together in d15, so the active ingredient is unknown.
- **Anti-modal cue.** "Consider what most models would write and choose something different" (d06).
- **Goal-blind diverge, then narrow (ReDNA).** Call 1 sees only the scene or object, not the goal or criteria. Call 2 gets the goal, failures and earlier ideas and selects (d01, d02).
- **Remote-source analogy.** Give a random far-domain source. Humans gain at almost any distance. LLMs gain only when the source is far and the model is strong (d12).
- **Weight steering (CreativityNeuro).** Contrastive weight steering with no behavioural data raised DAT percentile and AUT originality on 3B-14B open models (c24, d09). Needs weights, so unusable for a prompt-only agent.

**4.5 Process models.** Jump count: cosine similarity between successive ideas below a threshold counts as a switch. Human clusters: persistent (7-12 jumps), flexible (15-18), mixed (12-16) (a05). LLM jump counts match humans on AUT, but test-retest reliability is r = .22 against .42 for humans (a06). A process metric from one run is noisy.

## 5. What holds up

**Replicated or consistent across independent sources.**

- LLMs equal or beat the average human on semantic-distance originality in AUT and DAT (a08, a10, a14, a19, b15, c07). The direction is stable. The size is not (Hedges g 0.52 to 2.61 depending on fluency control; a15, b13).
- Best humans still match or beat LLMs (a10, a19, a08). Against the top 50% of humans on DAT, g = -0.88 (a15).
- Individual originality is not the issue. Population diversity is: a large effect (d = 1.1 to 1.8) in two studies (a21, c13), echoed by Hivemind and NoveltyBench (b19, b17).
- Temperature is not a creativity control (b16, a07, c16). Min-p does not fix it (c16). Min-p's own human evaluations show no diversity advantage (d06), so the Hivemind null for min-p says little.
- Originality and utility trade off (a02; AUT utility also fell in CreativityNeuro, c24).
- Instruction wording matters for LLMs on DAT (aware vs unaware +11.9 points, c09; etymology up, opposition down, a20). Short "wild, bold" cues beat long method prompts (d11).
- Regeneration with earlier answers shown, verbalized sampling, persona and anti-modal cues all raise diversity more than temperature (b18, d03, d06, d14, d15).

**Failed or weak.**

- Threshold hypothesis: no threshold in two large samples (b05).
- DT as an intelligence proxy: only r = .25 (b01). Fluency alone r = .20.
- DT predicts real creativity: inconsistently. AUT does not consistently predict TTCT, story writing or real-world problem solving (b14). Contested (K10).
- Creativity training as prompts: shrinks to d = 0.29-0.32 after publication-bias correction (SCHEMA 4b).
- Hivemind headline size: the 0.8 threshold is weak and much of the similarity is prompt geometry (d05). A residual 2-3x effect remains. Preprint, not peer reviewed.
- LLM process measures are unreliable across runs (a06).
- Model-version progress: none on DAT. GPT-4o scored well below GPT-4 (c08, d = 2.41), but the comparison mixes studies, raters and dates. GPT-4-turbo was below GPT-4 (a19, c06). Across 54 models, DT diversity scores fall 0.47 z per year while creative writing rises (d08).
- Activation steering did not transfer to AUT or Task Task, though weight steering did (d09).

**Moderators.**

- Fluency control (post hoc vs prospective vs none) drives effect size (a11, a15).
- Scorer: SD rewards odd words and punishes elaboration; human ratings reward elaboration (a23). AI vs human raters differ for GPT-4 (b10).
- Task: AUT means are tight across 14 models (65.66-77.85); DAT spread is wide (c10). The authors suggest a fixed count of distant words conflicts with local coherence. Untested interpretation.
- Prompt wording and whether the model is told the test (c09).
- Human sample: small student or Prolific samples with minimal instruction versus tuned LLM prompts (a01). Human instruction matters: game-like instructions gave no DT-intelligence correlation (b03).
- Contamination: classic AUT and DAT items are probably in training data (a01, b13, b15, d11). Not tested with unseen objects.

**Interventions on humans.**

- Explicit "be creative / quality" instructions improved DT in a meta-analysis (g .24-.27, snippet only, b23, unverified). NoveltyBench shows the same kind of instruction is weak for LLMs (b18).
- LLM help to humans: strategy lists lowered later solo originality and raised similarity (d10, N = 460 on AUT). Idea lists did not. ChatGPT users' ideas were more alike across users, with a wider category spread (a22, N = 36). So homogenisation by LLM aid is contested (K12) and depends on the form of help.

## 6. Language models

**Timeline of measured results.**

1. **GPT-3 (2022).** Humans were more original and surprising; GPT-3 was more useful (a01, 42 humans, 144 runs). Temperature had no link to flexibility (r = .04).
2. **GPT-4 and chatbots (2023).** Chatbots matched or beat the average (a08, a10). Koivisto: B = 0.049 for mean SD, but the top scores were equal. Haase and Hanel: 32.8 humans beat the best of five chatbots per prompt; 9.4 beat GPT-4. Hubert: eta2 = .51 with post hoc fluency matching.
3. **DAT (2024).** GPT-4 above the human mean, below the top deciles (a19). Output is repetitive: microscope 70%, elephant 60% (a20).
4. **2025 sweeps.** 14 LLMs, AUT percentile 65.66-77.85; 0.28% of responses in the top 10% of humans (c07). DAT is unstable: GPT-4.5 had 6 of 100 runs below the 50th percentile; DeepSeek-R1-Distill-Qwen-7B did worse when told the test (d = -0.42) (c09).
5. **Homogeneity (2025-2026).** Individual originality equal or higher; variability far lower (a21, c13, b21). Hivemind: 79% of queries with mean similarity > 0.8; across models 0.71-0.82 (b19). A re-analysis shrinks the headline but keeps a residual 2-3x effect (d05).
6. **Research ideation.** LLM ideas rated 5.64 vs 4.84 for experts, with lower feasibility (b22). Duplicates dominate: ~200 of 4,000 seeds unique (c21). LLM rankers reach only 63.5-71.4% accuracy (c22). Supports schema G8.
7. **Reasoning-trained models.** A reasoning-trained Llama variant showed negative alignment with high-creativity human fMRI responses, while a creativity-optimized one kept it (d13, abstract and intro only). One reasoning model started above 0.88 similarity (d15). So reasoning training may hurt divergence. [S].

**What changed results, by how much.**

| Lever | Change | Status |
|---|---|---|
| Naming the DAT in the prompt | +11.9 percentile points on average; per model d from -0.42 to 1.82 | [S] c09 |
| Etymology prompt | beat plain on GPT-3.5 and GPT-4; no size recorded | [S] a20 |
| Higher temperature on DAT | GPT-4 rises with temperature 0.5 -> 1.5, mean 85.6 at 1.5 | [S] c05 |
| Higher temperature on AUT or stories | no jump change (a07); beta .308 novelty with more incoherence (b16) | [E] small |
| "Very creative" system prompt | individual originality +0.043, variability +0.117, still below humans 0.738 | [E] b21 |
| In-context regeneration | to roughly human-writer diversity | [E] b18, d03 |
| Verbalized sampling | diversity x1.6-2.1; +25.7% rated quality | [S] d03 |
| Persona / anti-modal phrasing | effective rank +66% to +175%; ideas 3.34 -> 3.99 | [C] d06 |
| Sample-then-ban | diversity +85% to +167% | [S] d14 |
| Goal-blind diverge then narrow | AUT originality 2.91 -> 3.77 | [S] d02 |
| Short "wild" cue vs SCAMPER/TRIZ | short cue wins; +10% to +41% | [E] d11 |
| Weight steering | DAT +14 points; AUT originality d = +0.36; utility falls | [S] c24, d09 |
| Random far analogy | LLMs gain only if far and strong model | [S] d12 |
| Multi-agent debate | 26.0% -> 37.0% on Counter-Intuitive AR; "divergent" means argument diversity, not idea fluency | other construct; see G9 |

**Caveats on the whole LLM literature.**

- Most studies use semantic-distance scoring (rewards odd words, penalises elaboration).
- Contamination of AUT and DAT items is unaddressed.
- Human samples are small and given minimal instructions; LLM prompts are tuned.
- No study compares a multi-step scaffold with best-of-N at equal tokens on AUT or DAT. This is the main hole.
- Hubert's reported F values for AUT and Consequences are identical in the text (possible copy error; a14, b11).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Report originality and utility together in open mode, with a utility floor.** Part: G (quality gate), S7. [E]. Ids: a02, c11, c24, b16. Claim K05.
2. **Never rely on temperature or min-p for diversity.** Part: G (extends G4: sampling noise is not diversification). [E]. Ids: b16, a07, c16, a03, d06. Claim K04.
3. **Diversify by structure, not sampling noise: show earlier ideas and ask for a different one (regeneration), or list-then-dedupe in code.** Part: O in S3 open mode (code keeps the history of directions and assigns untried ones). [E]. Ids: b18, c19, d03, c21, d06. Claim K07. Matches S3 already; the equal-token check is pending (section 8).
4. **Keep the diverge prompt short and explicit ("wild, bold, unconventional").** Do not use SCAMPER/TRIZ multi-step prompts. Part: O diverge prompt. [E]. Ids: d11, d06, d09, c14. Claim K17.
5. **Score open mode with two scorers (embedding distance and an LLM rater), strip style tells, length-normalise, report mean, max, fluency and utility.** Part: S open-mode measurement; ties to G5. [E]. Ids: a23, a24, a12, b08, a02, a11. Claim K11.
6. **Do not use a DT or AUT score alone as the open-mode metric.** Add a task-grounded metric. Do not treat a reasoning score as a creativity proxy (r = .25). Part: S0 / metrics. [E] for the weak links, [C] for prediction. Ids: b14, a24, d07, b01, b05, b24. Claims K09, K10, K19.
7. **Do not run open generation to a fixed large count.** The serial-order gain per extra idea is tiny (at most 3.5% variance). Stop on a code rule (new non-duplicate share low). Part: O stop rule, M seen-idea memory. [E] for the tiny effect (b06); [S] for the dedupe-plateau stop (c21). Claims K15, K08.
8. **Fix prompt, snapshot and rater before comparing arms; repeat runs.** Single runs vary widely (c09, c07, a06). Part: G7 harness. [E]. Claims K02, K13.

### Test first

| Item | Part | Status | Ids | Why test |
|---|---|---|---|---|
| Goal-blind diverge call, then a narrowing call, as separate calls | O diverge / converge, S3 | [S] | d01, d02 (K16) | no equal-token control; extra calls may explain the gain |
| Verbalized sampling in the diverge step | O diverge | [S] | d03, d04 (K18) | shown on creative writing, not AUT or DAT |
| Sample-then-ban of the model's own frequent words | O diverge | [S] | d14, c25, a20 (K14, K20) | pilot N = 16; never tested head to head with regeneration |
| Persona anchoring and anti-modal cue | O diverge | [C] | d06, d15 | gain in embedding spread more than in distinct ideas |
| Seen-idea memory with dedupe stop | M | [S] | c21 (K08) | one study, 0.8 threshold is weak |
| Far-analogue seeds in open mode only, scaled by model strength | O7 | [S] | d12 (K21) | LLMs gain only if far and strong |
| Naming the task type in the prompt | S0/S1 | [S] | c09 (K06) | per-model sign differs |
| Agent shows idea lists, not strategy lists, to human users | multiplayer note | [C] | d10, a22 (K12) | strategy lists lowered later human originality |
| Long reasoning hurts divergence? | G11 | [S] | d13, d15 | may conflict with a long-reasoning default |

## 8. Concrete tests on our bench

All arms get the same total tokens, counted including setup (G7). Use at least 3 runs per item per arm and at least 20 items, including new objects (to avoid contamination). Score with two scorers.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | AUT, 20 objects including 10 invented or rare objects | (A) plain single call asking for N ideas; (B) best-of-K independent calls then dedupe; (C) goal-blind diverge call then narrowing call; (D) regeneration with earlier ideas shown | mean and max SD originality at matched fluency, LLM-rated utility, distinct-ideas count, population variability over 10 runs | C and D above A and B on variability; the d02 originality gain (+0.86 on a 5-point scale) is expected to shrink at equal tokens |
| T2 | DAT, 50 runs per arm | plain; DAT-aware prompt; verbalized-sampling list; sample-then-ban on top-10 words | DAT score, top-10 word share, overlap with a human word list | ban list lowers top-10 share (25.5% baseline in small models); DAT gain of a few points |
| T3 | NoveltyBench subset (100 prompts, 8 generations) | plain; temperature 1.5; regeneration; verbalized sampling; persona | distinct-k, cumulative utility | regeneration and VS near human level; temperature near zero gain |
| T4 | Open-ended idea task with a checkable outcome (our open-mode item set) | plain; best-of-N; diverge-then-select; diverge-then-select plus seen-idea memory | share of tasks where a checked idea works; distinct working ideas | tests Runco: whether AUT-style gains carry to outcomes (K10) |
| T5 | Stop rule | generate to 40 ideas, log by index | originality vs index; non-duplicate share vs index | flat slope; stop where new non-duplicate share < 25% |
| T6 | Drift check | same 50 DAT items, same prompt, 3 snapshots or dates | score variance across snapshots | measures the noise floor before any arm comparison |
| T7 | Reasoning budget | open items with short vs long reasoning at equal tokens | originality, distinct ideas | long reasoning not better (G11); maybe worse |
| T8 | Scorer validity | 100 ideas rated by humans | agreement of SD, LLM rater and human; link to utility | SD-human r about .5; require both scorers to agree |
| T9 | Utility floor | T1 outputs | originality with and without a utility floor | floor removes the odd-but-useless gain (r about -.6) |

## 9. What does not transfer, and why

- **Human serial-order and fluency effects.** The human effect is tiny (b06). An agent that samples in parallel has no warm-up in the same sense. Any order effect within one context may be an in-context diversity effect; untested.
- **Human instruction research (be-creative vs be-fluent).** For LLMs a creative system prompt does little (b18, b21), so the human meta-analyses (b03, b23) are weak guides.
- **DT-intelligence correlation.** A human individual-difference result. It says nothing about arms of our agent, except that a reasoning score is not a creativity score (K09).
- **Threshold hypothesis.** Human-only, and it failed anyway (b05).
- **Persistence vs flexibility paths.** Based on human memory search. LLM jump behaviour is unreliable across runs (a06).
- **Weight steering (CreativityNeuro).** Needs open weights (c24, d09). Not usable in a prompt-only scaffold.
- **Multi-agent debate "divergent thinking".** The term means argument diversity (c26). A different construct, and against G9.
- **Strong DAT/AUT numbers.** Possibly inflated by contamination and fluency matching. They do not show the agent invents better ideas (a14, d11).
- **Executive-control explanation for the human lag.** Cited (a13), untested, and an LLM has no inhibition mechanism in that sense.
- **Human-group homogenisation results.** Small samples and a human-with-tool setup (a22 N = 36); relevant only to the multiplayer extension.

## 10. Open questions

1. Does a multi-step scaffold raise AUT/DAT originality and population diversity at equal tokens versus best-of-N and verbalized sampling?
2. What do Guilford 1950/1967 and Runco 2008 actually report? Not opened, paywalled.
3. How much of the LLM edge survives on new unseen objects with fluency and length controlled?
4. How stable is DAT/AUT across snapshots? What are the 2026 frontier numbers?
5. Do semantic-distance scores predict human-rated usefulness and task outcomes for LLM ideas?
6. Is the Hivemind effect as large as claimed under a stricter null, and what breaks it best: banned frequent words, persona or retrieval of seen ideas?
7. What are the verified effect sizes of explicit instructions (Acar 2020) and of DT vs evaluative skill (b23, b24)?
8. Is there a serial-order effect in LLM idea chains, and where should the stop rule sit?
9. Does using an agent reduce diversity of a human group's ideas? Replication beyond N = 36 and the Kumar study (K12).
10. Does reasoning training reduce divergence (d13, d15)?
11. Is the gap to top humans closing for 2026 frontier models? No data found.

## 11. Sources

[V] opened, [M] snippet or citation only.

- [V] Stevenson et al. (2022) Putting GPT-3's Creativity to the Alternative Uses Test. https://arxiv.org/abs/2206.08932 (a01-a04, c11, c12)
- [V] Nath, Dayan, Stevenson (2024) Characterising the creative process in humans and LLMs. https://arxiv.org/abs/2405.00899 (a05-a07)
- [V] Haase and Hanel (2023) Artificial muses. https://arxiv.org/abs/2303.12003 (a08, a09, b10)
- [V] Koivisto and Grassini (2023) Best humans still outperform AI. https://www.nature.com/articles/s41598-023-40858-3 (a10-a13, b12)
- [V] Hubert, Awa, Zabelina (2024) Current state of AI generative language models. https://www.nature.com/articles/s41598-024-53303-w (a14, b11, c01-c03)
- [V] 2026 review, Evaluation of LLMs as tools, models and partners in creative thinking research. https://pmc.ncbi.nlm.nih.gov/articles/PMC13608707/ (a15-a18, b13, b14)
- [V] Bellemare-Pepin et al. (2024/26) Divergent creativity in humans and LLMs. https://arxiv.org/abs/2405.13012 (a19, a20, c04-c06)
- [V] Homogeneity study (2026) LLMs are homogeneously creative. https://pmc.ncbi.nlm.nih.gov/articles/PMC13010328/ (a21)
- [V] Anderson, Shah, Kreminski (2024) Homogenization effects of LLMs on human creative ideation. https://arxiv.org/abs/2402.01536 (a22)
- [V] Beaty and Johnson (2021) Automating creativity assessment with SemDis. https://doi.org/10.3758/s13428-020-01453-w (a23, a24, b08, b09)
- [V] Gerwig et al. (2021) Intelligence and DT meta-analysis. https://mdpi-res.com/d_attachment/jintelligence/jintelligence-09-00023/article_deploy/jintelligence-09-00023.pdf (b01-b04)
- [V] Weiss et al. (2020) Threshold hypothesis reappraisal. https://pmc.ncbi.nlm.nih.gov/articles/PMC7709632/ (b05)
- [V] Barbot, Van den Noortgate, Said-Metwaly (2026) Robust but tiny. https://pmc.ncbi.nlm.nih.gov/articles/PMC13300940/ (b06; b07 via it)
- [V] Arora et al. (2025) Generative AI outperforms students on DT. https://pmc.ncbi.nlm.nih.gov/articles/PMC12546817/ (b15)
- [V] Peeperkorn et al. (2024) Is temperature the creativity parameter of LLMs? https://arxiv.org/pdf/2405.00492 (b16)
- [V] Zhang et al. (2025) NoveltyBench. https://arxiv.org/abs/2504.05228 (b17, b18, c18, c19)
- [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954 (b19, b20, c15-c17)
- [V] Wenger and Kenett (2025) We're different, we're the same. https://arxiv.org/abs/2501.19361 (b21, c13, c14)
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109 (b22, c20-c22)
- [V] Haase, Hanel, Pokutta (2025) Has the creativity of LLMs peaked? https://arxiv.org/abs/2504.12320 (c07-c10)
- [V] Zhang et al. (2025/26) Verbalized Sampling. https://arxiv.org/abs/2510.01171 (c23, d03, d04)
- [V] Schapiro et al. (2026) CreativityNeuro. https://arxiv.org/abs/2607.01433 (c24, c25, d09)
- [V] Liang et al. (2023) Multi-agent debate. https://arxiv.org/abs/2305.19118 (c26)
- [V] Park et al. (2026) Beyond One Path / MUTATE / ReDNA. https://arxiv.org/abs/2605.28465 (d01, d02)
- [V] Schaeffer et al. (2026) Reevaluating the Artificial Hivemind. https://arxiv.org/abs/2609.33936 (d05, d06)
- [V] Schapiro et al. (2026) Assessing the creativity of LLMs. https://arxiv.org/abs/2605.13450 (d07, d08)
- [V] Kumar et al. (2025) Human creativity in the age of LLMs. https://arxiv.org/abs/2410.03703 (d10)
- [V] Carichon et al. (2026) IDEAFix. https://arxiv.org/abs/2606.00875 (d11)
- [V] Liu et al. (2026) Cross-domain analogy. https://arxiv.org/abs/2603.19087 (d12)
- [V] Ismayilzada et al. (2026) fMRI and LLM representations on the AUT (abstract and intro only). https://arxiv.org/abs/2604.03480 (d13)
- [V] Khan and Wester (2026) Seeing the Hivemind. https://arxiv.org/abs/2606.09587 (d14)
- [V] Beyond the Hivemind (2026) meta-persona anchoring. https://arxiv.org/abs/2608.02618 (d15)
- [M] Runco (2008) Divergent thinking is not synonymous with creativity. https://doi.org/10.1037/1931-3896.2.2.93 (a26, d16)
- [M] Guilford (1950, 1967), books, no URL (a27)
- [M] Silvia et al. (2008); Mednick (1962) (a28)
- [M] Hass 2017, Baas 2013, Nijstad 2010, via Nath 2024 (a25)
- [M] Summers-Stay et al. 2023, via Bellemare-Pepin (c27)
- [M] Gonthier and Besancon 2024; Miroshnik and Shcherbakova, via Barbot 2026 (b07)
- [M] Acar, Runco, Park (2020) explicit instructions meta-analysis. https://eprints.whiterose.ac.uk/209749/2/Supplemental_Material_accepted_pre_format_version.pdf (b23, d16)
- [M] DT and evaluative skill meta-analysis (2022). https://eld.bl.uk/catalog/100167803796_0x000001 (b24)

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 8 established claims: 6 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A09.08-K01** (reworded: the sources support less). Haase and Hanel (listed as support) found no mean originality difference between chatbots and humans, and in Bellemare-Pepin only some LLMs (GPT-4, 'several leading LLMs') beat the human DAT mean while Gemini Pro did not; fluency was matched only in the Hubert AUT; evidence is from 2023-24 chatbots and mostly GPT-4. Corrected claim: In 2023-24 studies, some chatbots (mainly GPT-4, also ChatGPT-3 and Copy.ai in Koivisto and Grassini) scored higher than the average human on semantic-distance originality in the AUT (fluency controlled or matched) and in the DAT (GPT-4 over humans; other models such as Gemini Pro were indistinguishable from humans, and Haase and Hanel found no mean AUT difference); in one-shot tasks the best humans still matched or beat the best AI (Koivisto and Grassini; top human decile/quartile beat every DAT model in Bellemare-Pepin).
- **A09.08-K05** (reworded: the sources support less). r = -.56 (humans) and -.61 (GPT-3) is confirmed in Stevenson, but neither source shows originality rising with temperature or prompts while usefulness falls; Peeperkorn measures novelty vs coherence/typicality, not usefulness. Corrected claim: Originality and utility were negatively correlated within responses (r = -.56 for humans, r = -.61 for GPT-3, Stevenson et al 2022); higher temperature gave slightly more novel but more incoherent stories (Peeperkorn et al 2024), so open-mode metrics should score both novelty and usefulness or coherence.
- **A09.08-K15** (now single-source: only one opened source, code check).
