# Deliberate practice: deep document

*Subfield E16.10. Evidence ids (a01-a25, b01-b25, c01-c26, d01-d16) refer to evidence_a-d.jsonl in this folder. Claim ids (K01-K34) refer to claims.jsonl. Weak spots are listed in critique.md. Why it matters for the agent: background only. No study tests deliberate practice as Ericsson defined it on a language model. The LLM evidence is about self-improvement, curricula and test-time compute, which is analogy, not a test.*

## 1. What it is

Deliberate practice (DP) is a theory of how experts get good. It says that differences in top performance are largely explained by how much of a special kind of practice a person has done. The special kind has these parts:

- It is designed (usually by a teacher) to improve one aspect of performance.
- It has a clear goal for each session.
- It gives immediate feedback.
- It is effortful and not much fun.
- It targets weaknesses, with repetition and correction.
- It is separate from play and from work performance.

Chess is the favourite test domain. Ratings (Elo) are objective, practice can be split into solitary study, coached study and tournament play, and the player population is large and well documented.

Three questions run through the field. They matter because they decide what "practice" could mean for an agent.

1. How much of the variance in skill does DP explain? A moderate share: 18% to about 34% in chess, depending on corrections (K01, K02).
2. What counts as DP? This is disputed. The answer moves the effect size from r=.38 to r=.56 (K25).
3. Does the kind of practice matter, over and above the amount? A large 2026 log study says yes: 3.61x learning efficiency for DP-aligned activity (K11, single source).

For our agent the construct is background. The agent cannot train weights. The useful translation is this: which parts of a practice loop (goal, feedback, weakness targeting, curriculum choice, fresh experience) can be reproduced inside a scaffold with a prompt and a memory, and do they pay at equal tokens (G7)?

## 2. History and theories in depth

**Before DP.** Chase and Simon (1973) argued that chess skill is stored patterns (chunks), built over about ten years of study. Ericsson's 1980 digit-span study showed that more than 200 hours of training lifted one college student's span (b23). That is the uncontroversial core: practice changes performance a great deal.

**Ericsson, Krampe and Tesch-Romer (1993), violin.** The founding claim (a01): "individual differences in ultimate performance can largely be accounted for by differential amounts of past and current levels of practice." Reported practice alone by age 18: best violinists M=7,410 h, good M=5,301 h, music-teacher group M=3,420 h (c01). Ericsson later gave the best group a 95% CI of 2,894 to 11,926 h (c01). The original was not opened this session; the numbers come through Macnamara and Maitra (2019), who opened it.

**Extension to chess.** Charness et al. (1996, 2005) found chess rating tracked accumulated serious solitary study (a10; read only through Hambrick 2020). Study 1 had N=239 and Study 2 N=169 in the 2005 paper; the 1996 chapter had N=136 (b22). Solitary study was the best predictor. Playing games added no reliable benefit once study was controlled. Ericsson rejected this paper for lacking teacher records in one place and cited it positively in another (a11). That is an inconsistency in how DP is defined, and it recurs.

**Challenge 1: Gobet and Campitelli (2007).** Chess club members: N=104 enrolled, about 90 analysed (the abstract says 104, Hambrick 2020 says 90). DP hours correlated with rating at r=.42, about 18% of variance (a05, b09, b21). Hours needed to reach master ranged from 3,016 to 23,608, almost an 8-fold spread. Starting age predicted skill beyond DP hours. Howard (2012) found the same (a04).

**Challenge 2: Macnamara, Hambrick and Oswald (2014).** Meta-analysis of 88 studies and 157 effect sizes. Overall r=.38 (CI .33-.42), 14.4% of variance (b03). By domain: games 26% (r=.51, 11 effect sizes), music 21% (r=.46), sports 18% (r=.42), education 4% (r=.21), professions under 1% (r=.05, p=.62) (a02, c03). The screen began from over 11,000 articles (a22). A 2018 corrigendum exists (b24, d01); its content was not retrieved.

**Reply 1: Platz et al. (2014).** Music meta-analysis, 13 studies, N=788, corrected r=.61 (CI .54-.67) (a08, b05). Hambrick et al. answer that Platz mixed in non-DP measures (a07).

**Reply 2: Ericsson and Harwell (2019).** A stricter DP definition on 8 effect sizes gives r=.56 (31.4%). They argue that range restriction and low reliability depress correlations (a09, a21). Chess rating reliability is alpha .95 for masters but .59 for typical players (Glickman and Jones 1999). Re-analysis by Hambrick et al. (2020): DP r=.56 (k=8), purposeful practice r=.51 (k=6), difference not significant, p=.64 (d02). So teacher guidance adds little beyond goal plus feedback in this data.

**Reply 3: Hambrick et al. (2014).** In the chess and music data, DP accounts for about one third of reliable variance: 34% chess, 29.9% music, assuming DP reliability .80 and chess rating reliability .91 (a06, b04). They note that r=.61 leaves room for two other predictors of r=.56 each.

**Other lines of evidence.**
- Sports: Macnamara, Moreau and Hambrick (2016) found 18% overall and 1% among elite performers (c04, b08). Ericsson disputes this on range restriction.
- Intelligence: Burgoyne et al. (2016, 2019) found ability matters. The ability effect is r=.32 in lower-skill and r=.14 in higher-skill players (d03, age-confounded). Practice-history variables explained over 50% of chess rating without correction (a13). Both Burgoyne 2016 and Macnamara 2014 have 2018 corrigenda (d01).
- Genetics: Mosing et al. (2024), 6,471 twins. About 50% genetic, 25% shared environment, 25% residual. More practice cut shared-environment and residual variance but not genetic variance (b07).
- Carlsen: Gobet and Ereku (2014) found Carlsen reached the top 18 years after starting, against a mean of 24.6 for ranks 2 to 11 (t(9)=2.83, p<.05). Rank vs years across the top ten was r=-0.21, p=.55 (b06).
- Violin replication: Macnamara and Maitra (2019), about 13 per group (N=39). "Best beat good" did not replicate (b01, c02). See section 3.

**Newest line: Southwick et al. (2026, Psychological Science).** N=44,213 Chess.com players, objective timestamped logs. Over 90% of time went to games. DP-aligned activities had 3.61x the learning efficiency of gameplay (ps<.001). Not all DP-aligned activities were equal (a14, b12, c06). Only the abstract was read. Authors include DP proponents. The design is observational.

**Where the theory stands.** Practice matters a lot. DP hours explain a real but moderate share. The strong form ("largely explained") is not supported in games, music or sports, and fails in professions and education. The weak form ("targeted practice beats unguided repetition") has support from one large observational study and several small human trials, not from randomised chess trials.

## 3. Core findings with exact numbers

Status: established = two or more independent sources; otherwise single-source or contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Violin original: best > good > teachers | Practice alone to 18: 7,410 / 5,301 / 3,420 h | Ericsson 1993 via Macnamara and Maitra 2019 (c01) | As reported; original not opened |
| Violin replication: best vs good gap absent | Best M=8,224 h (CI 6,400-10,048); good M=9,844 h (CI 6,937-12,751); t(24)=-0.93, p=.364, d=-0.38; good vs less (M=4,558) t=3.26, d=1.33; eta2=.26 | Macnamara and Maitra 2019 (b01, c02) | Established (K04); small N, about 13 per group |
| Replication, teacher-designed practice | Best 6,251 h, good 6,821 h, less 2,799 h; eta2=.23 vs .26 for practice alone; r=.72 between the two measures | Macnamara and Maitra 2019 (b02) | Single replication |
| Replication, current weekly practice | Best 22.69 h vs good 30.65 h, p=.024, d=-1.03. Opposite direction to the original: good players practised more | Macnamara and Maitra 2019 (b02) | Single replication |
| Chess DP vs rating, club sample | r=.42 (about 18%); N=104 enrolled, about 90 analysed | Gobet and Campitelli 2007 (a05, b09) | Established (K01) |
| Games meta-analysis | r=.51, 26% of variance, 11 effect sizes (Games N not recovered) | Macnamara et al. 2014 (a02) | Established |
| Reliable variance, chess and music | Chess r=.49, music r=.43 before correction; 34% chess, 29.9% music reliable variance (reliability .80 DP, .91 rating) | Hambrick et al. 2014 (a06) | Established (K02) |
| Domain differences | Games 26%, music 21%, sports 18%, education 4%, professions under 1% | Macnamara et al. 2014 (a02, c03) | Established (K05) |
| Predictability moderator | 24% high (r=.49), 12% medium (r=.35), 4% low (r=.21) | Macnamara et al. 2014 (a03) | Established |
| Measurement moderator | Log 5% (r=.22), questionnaire 12% (r=.34), interview 20% (r=.45) | Macnamara et al. 2014 (a03) | Established (K03) |
| Performance-measure moderator | Group membership r=.51, lab task r=.37, expert rating r=.30, standardised objective measure r=.28 | Macnamara et al. 2014 (a24) | Single meta-analysis |
| Reliability correction | Macnamara r=.38 corrected to .63 / .54 / .48 / .42 (40.1% / 29.5% / 22.6% / 17.8% of variance) at four assumed reliability levels | Hambrick et al. 2020 (b25) | Established |
| DP definition effect | Ericsson and Harwell k=8 r=.56 (31.4%); Macnamara 2014 r=.38 (14.4%); Miller 2019 k=70 r=.40 (16.0%); Platz music k=14 r=.61 (37.2%); sports k=63 r=.45 (20.3%) | Hambrick et al. 2020 (b03, b20) | Contested (K25) |
| Teacher guidance adds little | DP r=.56 (k=8), purposeful r=.51 (k=6), combined r=.54 (k=14), p=.64 | Hambrick et al. 2020 reanalysis (d02) | Single-source (K32) |
| Elite performers | Sports 18% overall, 1% elite | Macnamara et al. 2016 (c04) | Contested (K06) |
| Ability by skill band | r=.32 lower skill vs .14 higher skill; age-confounded | Burgoyne 2016 via Hambrick 2020 (d03) | Single-source (K07) |
| Large individual spread | 3,016 to 23,608 h to reach master | Gobet and Campitelli 2007 (a05) | Established (K09) |
| Starting age beyond DP | Earlier start predicts higher rating after controlling DP | Gobet and Campitelli 2007; Howard 2012 (a04) | Established (K08) |
| Solitary study best predictor | Study 1 N=239, Study 2 N=169; games add nothing once study controlled | Charness 2005 via Hambrick 2020 (a10, b22) | Contested (K10) |
| Practice vs genes | 6,471 twins; about 50% genetic, 25% shared, 25% residual; practice reduced non-genetic variance only | Mosing et al. 2024 (b07) | Single-source (K12) |
| Dropouts | Developed slower, same gain per unit practice (abstract only) | de Bruin et al. 2008 (b10, c05) | Single-source (K13) |
| Carlsen | 18 years vs 24.6 (t(9)=2.83); rank vs years r=-0.21 | Gobet and Ereku 2014 (b06) | Single-source (K26) |
| Log study of practice type | N=44,213; over 90% of time on games; DP-aligned 3.61x efficiency (ps<.001) | Southwick et al. 2026 (a14, b12, c06) | Single-source (K11); abstract only, unadjusted |
| Diary validity | Weekly estimates vs diary r(34)=.6 to .8 | de Bruin 2008 via Ericsson and Harwell 2019 (a09) | Small sample |
| GM concept teaching | Four GMs, 36-48 puzzles, 13 concepts; GM1 0/12 to 5/12, GM2 4/12 to 7/12, GM3 3/12 to 5/12, GM4 6/16 to 7/15; 8 concepts up, 3 same, 2 worse; gain did not track rating | Schut et al. 2025 (a18, c22) | Single-source (K18); no unaided-practice control |
| Specialist chess transformer | 270M: puzzles 95.4%, tournament Elo 2299, Lichess blitz vs humans 2895; 136M 94.5%, Elo 2259; 9M 88.9%, Elo 2025; 1.33% of puzzle states in training | Ruoss et al. 2024 (a15, a25, c10) | Single-source (K14) |
| General LLM on chess | GPT-3.5-turbo-instruct 66.5% puzzles, about 1755 Elo vs bots | Ruoss et al. 2024 (c11) | Single-source (K15) |
| ChessLLM | Elo 1788; wins 61% / 56% / 30% at Stockfish skill 0 / 1 / 2; long-round data +350 Elo; over 20B tokens | Zhang et al. 2025 (a20, b16: same paper) | Single-source (K16) |
| Engines as human models | Stockfish/Leela match human moves 33-46%; Maia 50.8% (1100) to 52.9% (1900) | McIlroy-Young et al. 2020 (a16, c09) | Single-source (K19) |
| Self-play scale | Hex: about 500 Elo per 10x compute in the linear regime; AlphaZero beat Stockfish after about 4 h | Jones 2021; Silver et al. 2017 (c07, c08) | Background |
| Reflexion-style note memory | 130 of 134 ALFWorld tasks in 12 trials; HumanEval 91% vs 80%; ExpeL 59% ALFWorld; AWM +24.6% / +51.1% relative | d04, c17, d13, d14 | Established (K27) |
| Self-correction without oracle | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0 | Huang et al. 2024 (d05) | Established (K28) |
| Sound external verifier | Blocksworld 40/100 generator only, 55 with LLM verifier, 88 with sound VAL verifier | Valmeekam et al. 2023 (d06) | Established (K28) |
| Curriculum matters | Voyager random curriculum -93% items; PLR +76% test return; Skill-it 3B with 1B tokens beat uniform at 3B tokens | c18, c19, c20, d08 | Established (K21) |
| Adaptive curriculum gain shrinks with strength | SEC Countdown OOD 3B: 0.48 random to 0.54; 7B: 0.512 to 0.514; ordered curriculum 0.32 | Chen et al. 2025 (d09, d10) | Single-source (K30) |
| Adaptive test-time compute | Over 4x more efficient than best-of-N; smaller model beat 14x larger one at matched FLOPs where it had non-trivial success | Snell et al. 2024 (c21) | Single-source (K22) |

## 4. Mechanisms and models

These are proposed models. The human DP data only motivate them.

**4.1 The four-part DP loop (operational form).**
1. Goal: a specific, narrow target ("rook-versus-pawn endgames", "class: mutation-test failures").
2. Task: an item set built for that target, a little above current level.
3. Feedback: an exact signal on each attempt (engine eval, unit test, answer key).
4. Repeat and correct: the same class again, with the correction applied.

The log study (K11) suggests the gain per hour comes from parts 1 to 3 together. The re-analysis (K32) suggests goal plus feedback gets most of it and a teacher adds little. For an agent: goal = class label from S0, feedback = code check, "teacher" = a coach model choosing classes.

**4.2 Weakness-targeted curriculum.** Keep per-class pass rate p_c in code (the schema already keeps a class record, SCHEMA section 5). Sample the next practice class with probability proportional to a learning-progress score, for example p_c(1-p_c) (highest at 50% success), or run a bandit on recent improvement. PLR (c19) does this with a regret proxy. Skill-it (c20) does it with a skill graph. SEC (d09) uses a bandit on advantage and beats random and easy-to-hard ordering. Fixed easy-to-hard can be worse than random (Countdown ID 0.551 vs 0.859 in d09). Rule: never hand-order; let a score decide.

**4.3 Prompt-only practice effect (no weights).** Episode loop: attempt, code check, write one lesson line, store it, retrieve it on later similar tasks. Reflexion (d04), ExpeL (d13) and AWM (d14) show gains this way. Implementation points the data support:
- It needs a reliable success signal. Without one, intrinsic self-correction lowers accuracy (d05).
- Retrieve by task similarity. Random retrieval loses to similar-task retrieval (d13).
- Experience must be new. Insights extracted only from the given few-shot examples gave no gain (d13).
- Expect a plateau. Reflexion's baseline plateaus at trials 6 to 7; the iterative self-improvement gap goes to 0 in a few rounds (d04, d12).

**4.4 External verifier as feedback.** A sound checker (rule engine, test suite, VAL) is the LLM analogue of the engine or teacher. Blocksworld goes 40 to 88 with a sound verifier vs 55 with an LLM verifier (d06). Gain is bounded by candidate quality: Blocks World 82%, Logistics 70%, obfuscated Mystery Blocks World about 10% (d07). A verifier loop on chess raised legal-move rate from 50.8% to 95.3% for RedPajama 3B but cut ChessGPT-Base puzzle accuracy from 38.6% to 18.7% (b19). Log verifier use and check accuracy.

**4.5 Concept-targeted examples (Schut-style).** Mine concepts from an engine, build puzzle sets per concept, teach with a few examples. For the agent: a small library of worked examples per class, offered after the first attempt (SCHEMA section 5), with a random-example control. The human result is uncontrolled (K18). ExpeL's random-retrieval loss (d13) is the nearest agent evidence.

**4.6 Compute allocation.** People ration DP because it is costly. Test-time compute should be rationed by difficulty (c21, schema G12). Jones (c07) gives the self-play analogue: about 500 Elo per 10x compute in the linear regime. Gains are near zero when baseline success is near zero.

**4.7 Amortisation (specialist models).** The chess transformers (a15, a20) compress search into weights by supervised training on engine labels. That is the weights-level counterpart of "years of practice". Our scaffold cannot do this. It can only approximate it with memory and selection.

**4.8 Variance model for DP.** Reliability-corrected variance explained = r^2 / (reliability_DP x reliability_performance). With rating reliability .91 and DP reliability .80, r=.49 gives .24/.73, about 33%, matching the 34% in a06. Use this formula when reporting any agent "practice" effect, and show corrected and uncorrected numbers (K03).

## 5. What holds up

**Holds up (replicated or multi-source).**
- Practice amount correlates with skill in games, music and sports. Chess: r about .42 to .51 uncorrected; 18% to 34% of variance (K01, K02).
- The effect is much smaller in professions and education and in unpredictable domains (K05).
- Measurement method moves the estimate: log 5%, interview 20% (K03).
- Hours needed to reach a given level vary about 8-fold between people (K09).
- Starting age predicts skill beyond accumulated DP in chess (K08).
- Self-improvement by note memory works when a reliable signal exists and saturates in a few rounds (K27).
- Sound external verifiers help; self-verification without a signal does not (K28).
- Curriculum choice matters, and adaptive beats random and fixed ordering (K21).

**Failed or weakened.**
- "Best violinists practised most": best (8,224 h) did not beat good (9,844 h) in the replication, and good players also practised more per week now (K04). N is small.
- "Practice largely explains performance": 18% to 34% in chess, 4% in education, under 1% in professions, 1% among elite athletes (K02, K05, K06).
- "Teacher-guided DP is special": r=.56 for DP vs .51 for purposeful practice, p=.64 (K32). Single re-analysis.
- Games in chess: Charness found games add nothing beyond solitary study. The log study found games took over 90% of time and were least efficient. Ericsson rejects the Charness study on his own grounds (K10, K11). Contested.
- Intrinsic LLM self-correction fails (K28). Self-Refine gave +0.2 on code optimisation at base 92.9 and 0 on math at 64.1 (d11).

**Moderators.**
- Predictability of the domain (24% vs 4%).
- Measurement method (interview > questionnaire > log).
- Performance measure (group membership .51 vs standardised objective measure .28).
- Skill level (ability effect r=.32 vs .14; practice effect smaller at the elite end, with range restriction contested).
- Rating reliability: .95 for masters vs .59 for typical players.
- Model strength in agents: SEC gain +13% at 3B vs near 0 at 7B on Countdown OOD (K30).

**Why the numbers conflict.** Ericsson and Harwell r=.56, Macnamara r=.38, Miller r=.40. In chess: 34% vs 26% vs 18% vs over 50%. The causes are the DP definition, the reliability correction, the measure, and which variables count. They are not a data dispute (critique.md).

**Interventions that worked.**
- Human: AlphaZero-concept teaching improved four GMs on novel puzzles (K18, no control). Residents' checklist scores rose MD 4.44 (CI 1.72-7.15; 10 RCTs, 277 residents) but OSATS global rating MD 1.34 (CI -2.82 to 5.51, n.s.) (b13). MedSimAI OSCE history 82.8 to 88.8 (d=0.75) at one site and no change at another (c23). CPX-MATE repeat score +1.67 (c24). HypoCompass +11.7%, n=19 (c25). All small, uncontrolled and human-facing (K23).
- Agent: Reflexion, ExpeL, AWM, adaptive curriculum, sound verifiers.

**Interventions that did not work.** Self-critique without an oracle; random curricula (Voyager -93%); fixed easy-to-hard order (SEC); ExpeL insights drawn only from its few-shot examples; verifier loops where base candidate quality is near zero (Mystery BW about 10%).

## 6. Language models

**Direct tests of DP: none.** No study gives a model a DP loop as defined and compares it with unguided practice at equal tokens (gap 1, closed negative). The Pelican-VL paper (c26) names "Deliberate Practice Policy Optimization", but it is an RL training method for vision-language models, not a test of the theory: +20.3% over base, +15.8% over RL alone, average +15.4% across nine reasoning dimensions. Only the name is borrowed.

**Chess models (weights trained).**
- Ruoss et al. 2024 (a15, a25, c10, c11): 270M model 95.4% puzzles, Elo 2299 tournament, 2895 Lichess blitz vs humans; 136M 94.5%, 2259; 9M 88.9%, 2025. The vs-bots Elo equals the tournament Elo only for the 270M model; the 9M and 136M vs-bots values are 2054 and 2156 (critique). GPT-3.5-turbo-instruct 66.5%, about 1755 vs bots. AlphaZero policy only 56.1%. Only 1.33% of puzzle states were in the training set. The paper says blitz Elo is not comparable to tournament Elo.
- ChessLLM (a20): Elo 1788, wins 61% / 56% / 30% at Stockfish skill 0 / 1 / 2; long-round supervision +350 Elo; 20B tokens.
- Brittleness (b18, b19): mate-in-N 71.9% and 74.5% for two models, 2.1% for a model trained on 54,681 self-play positions; ChessGPT-Base 16.1% normal and 38.6% at pass@10; the verifier loop cut it to 18.7%. Methods say n=600, tables n=300; unresolved.
- Piece tracking about 99% with large training sets (c12). AlphaZero concepts start rising near 32,000 steps; piece values converge after 128,000 steps (a17).
- These are amortised search from engine labels, not practice.

**Self-improvement with weights.** STaR on GSM8K: 36.6 few-shot, 60.0 direct fine-tune, 68.8 STaR, 72.5 with rationalisation; arithmetic 89.5 vs 76.3 after 16 iterations (c14). SPIN leaderboard 58.14 to 63.16 on a 50k subset (c15). LeMa GSM8K 83.5 vs 81.4 (c16). Our agent cannot do this.

**Scaffold-only self-improvement.**
- Reflexion: HumanEval 91% vs 80%; ALFWorld 130/134 in 12 trials; +20% HotPotQA (c17, d04).
- ExpeL: HotpotQA 39.0%, ALFWorld 59.0%; insights-only vs retrieval-only 36%/31% HotpotQA and 50%/55% ALFWorld; WebShop 37%/38%; HotpotQA-to-FEVER transfer ReAct 58 vs 65 to 70 (d13).
- AWM: +24.6% Mind2Web, +51.1% WebArena relative; 8.9 to 14.0 points absolute as train-test gaps widen (d14).
- Voyager: 63 unique items in 160 iterations (3.3x); random curriculum -93%; no self-verification -73% (c18, d08).

**What lowered accuracy.**
- Self-correction without a signal (d05): GPT-3.5 GSM8K 75.9 to 74.7, CSQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0, HotpotQA 49.0 to 43.0.
- Chain of thought outside math and symbolic tasks gives little: up to 95% of the MMLU CoT gain is on symbolic questions (d15).
- Iterative self-improvement saturates and shows no gain on tasks beyond the model's own ability (d12).

**Ceiling effect in models.** SEC 3B vs 7B (d10); Self-Refine +0.2 where base is 92.9 (d11). This mirrors the human elite pattern, but no same-scaffold test across model strengths exists (K31, contested).

**Test-time compute.** Compute-optimal allocation is over 4x more efficient than best-of-N. A smaller model with test-time compute beat a 14x larger one on problems where it already had non-trivial success (c21). Matches G12.

**Medical practice platforms** (human learners with LLM feedback): see section 5.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = SCHEMA section 5. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Never trust self-verification without a code signal; log self-verifier false positives.** G2/G3 already say this. Evidence d05, d06, d07, d11. Part G2/G3. [E] (K28). Only the log field is new.
2. **Lessons come from real runs only and are retrieved by similarity, not at random.** Part memory (lessons). Evidence d13, d04, d14. [E] for the need of a signal and for similarity retrieval (K27); the "new experience only" rule is [S] (K33). Keep the existing "shown after first attempt" rule.
3. **Expect a plateau: cap practice rounds at about 3 to 6.** Part G7/G12. Evidence d04, d12. [E] (K27). Cap episodes in any practice loop and stop when per-round gain is below noise.
4. **Do not hand-order tasks easy to hard; if tasks are chosen, use a score.** Part S0 / memory (class record). Evidence d08, d09, c19, c20. [E] on "ordering matters and random can beat fixed" (K21). Applies only to batch runs with several items.
5. **Report corrected and uncorrected effects, using logged counts, not self-report.** Part section 6 (logs). Evidence a03, b25. [E] (K03).
6. **Ration spend by difficulty.** Already G12. Evidence c21. [S] here (K22), supported by other briefs.
7. **Use many seeds.** The 8-fold human spread in hours to master (K09, [E]) is a prior for run-to-run variance. Report intervals.

### Test first

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Weakness-targeted practice vs unguided practice at equal tokens | memory / O7 / S9 | [S] | a14, b12, c06, d09 (K11, K30) |
| Three-arm ablation: goal only, goal plus check, goal plus check plus coach model | S0 / S9 | [S] | d02 (K32) |
| Note memory as a practice effect, and its plateau | memory / S9 | [E] on other benches; [S] for ours | d04, d12, d13, d14 (K27) |
| Concept-targeted example sets vs random examples | O7 / memory | [S] | a18, c22, d13 (K18, K33) |
| Sound verifier step vs none, stratified by base solve rate | G2 / S4 / S8 | [E] direction; [S] on our bench | d06, d07, b19 (K28, K29, K17) |
| Scaffold gain vs base-model strength | G7 / G12 | [C] | d10, d11, d15, c04 (K31, K06) |
| Adaptive per-item budget vs fixed | G12 | [S] | c21 (K22) |
| Self-play-only vs targeted-study-only loop | memory | [C] | a10, a14 (K10) |

Not recommended: any prompt wording such as "practise deliberately". DP is a construct about human training history. It would fall under SCHEMA 4b ("be careful") and has no evidence.

## 8. Concrete tests on our bench

All arms at equal total tokens (setup, memory and retrieval cost counted). Several seeds per arm; report mean, interval and per-item flips.

1. **Practice-effect curve (memory).**
   - Items: batches of 20 to 40 same-class items with a code check (ARC-style grids, brain-teaser classes with answer keys, chess puzzles with an engine key).
   - Arms: plain model; scaffold with no cross-item memory; scaffold with one-line lessons stored in S9 and retrieved by similarity after the first attempt.
   - Metric: pass rate by item index and round; held-out items at the end.
   - Expected: a few points over the memory-free scaffold, plateau by round 3 to 6; zero where there is no reliable check.
2. **Targeted vs unguided practice (the 3.61x contrast).**
   - Items: a mixed-class pool; a practice phase, then a test phase on unseen items.
   - Arms: (A) practice on lowest-pass-rate classes; (B) practice on random classes; (C) no practice phase, tokens spent on extra test-time samples.
   - Metric: test-phase pass rate; tokens per point gained.
   - Expected: A > B by a small margin; A vs C unclear. If A does not beat C at equal tokens, practice phases do not pay (G7).
3. **Three-component ablation.**
   - Arms: goal only; goal plus code check; goal plus code check plus coach-model class selection.
   - Metric: test pass rate.
   - Expected (from d02): arm 2 captures most of the gain; arm 3 adds little.
4. **Random vs similar vs concept examples.**
   - Arms: no examples; random past examples; similar-task past examples; concept-labelled examples.
   - Metric: pass rate on new items; right-to-wrong flips.
   - Expected (from d13): similar beats random; random may equal no examples.
5. **Verifier step.**
   - Arms: no verifier; self-verifier; code verifier (legal-move check, unit tests, VAL-like checker). Items stratified into low, mid and high base pass rate.
   - Metric: accuracy by stratum; verifier false-positive rate.
   - Expected: code verifier helps in the mid stratum and does little near 0%; self-verifier null or harmful (d05, d07, b19). Watch for the ChessGPT-style drop.
6. **Strength sweep (ceiling).**
   - Arms: same scaffold on three base models of increasing strength.
   - Metric: scaffold gain vs base pass rate.
   - Expected: gain shrinks as base rate rises above about 90% (d10, d11).
7. **Adaptive budget.**
   - Arms: fixed samples per item vs budget scaled by class pass rate.
   - Metric: accuracy at equal tokens.
   - Expected: adaptive better, as in c21. If flat, G12 is not bound by this signal.
8. **Chess puzzle anchor (optional).**
   - Items: Lichess puzzles with a unique best move (Ruoss-style).
   - Arms: plain general LLM; scaffold with legal-move check; scaffold with engine-key verifier.
   - Metric: accuracy. Reference: GPT-3.5-turbo-instruct 66.5%, specialist 95.4% (c11).
   - Expected: a sound legal-move check lifts a weak model; the result stays far below the specialist.

## 9. What does not transfer, and why

- **Years of effortful practice, motivation, boredom, rest.** The agent has no fatigue, motivation limit or hours. The human 8-fold variance in hours reflects stamina and access.
- **Teacher.** The human DP definition needs a teacher. The data say teacher guidance adds little (K32), and our coach would be another model whose errors correlate with the agent's (G4).
- **Weight change.** STaR, SPIN, LeMa, AlphaZero self-play, ChessLLM and the 270M transformer all change weights. The scaffold cannot. Their gains are about amortising search, not practice habits.
- **Retrospective self-report.** Nearly all human DP numbers are interviews or questionnaires. Agent practice is logged exactly, so human r and variance figures are only rough priors.
- **Genes, starting age, ability.** Twin and starting-age findings (K08, K12) have no agent counterpart, except possibly the base-model choice.
- **Elite range restriction.** The human elite effect comes from a population selected on the outcome. The agent's "elite" is just a stronger base model, and the test is a sweep (section 8, test 6).
- **Human learning platforms.** MedSimAI, CPX-MATE, HypoCompass and the music SEM study are about human learners using AI feedback (K23, K24). They say nothing about an agent.
- **Debate-style coaching.** Excluded by G9.
- **Telling the model to be "deliberate".** Same family as "be careful"; SCHEMA 4b rejects it.

## 10. Open questions

1. Does targeted weakness practice beat unguided self-play on a model at equal tokens? No study (gap 1).
2. Does a note memory show a practice effect on our benches, and where does it plateau? Reflexion and ExpeL say yes on ALFWorld-type tasks (d04, d13). Untested for us.
3. What are the skill-band effect sizes in Burgoyne 2016, and what do the 2018 corrigenda of Macnamara 2014 and Burgoyne 2016 change? Content and the Games k and N were not retrieved.
4. Does the Southwick 3.61x survive controls for motivation and prior rating? Full text and supplement not reachable (d16).
5. Does an engine-derived concept-example set help an LLM agent over random examples at equal tokens? No Schut-style study found.
6. Does an external verifier help on reasoning tasks beyond legal-move checks? Legal-move yes; puzzle accuracy can fall (b19).
7. Is there a clean prompt-only ordered-vs-random curriculum test? Voyager's curriculum is state-adaptive.
8. Is the ceiling effect mirrored in agents across model strengths with one fixed scaffold?
9. Which operational definition of "deliberate" for an agent predicts gain best: goal, feedback or weakness targeting?
10. Unresolved data issues: b18 n (300 vs 600); ChessQA (b17) and ChessGPT (c13) scores were not extracted.

## 11. Sources

[V] = opened this session (full text or page). [M] = snippet or abstract only, or numbers second-hand.

- [M] Ericsson, Krampe, Tesch-Romer (1993). https://doi.org/10.1037/0033-295X.100.3.363 (numbers via Macnamara and Maitra 2019)
- [V] Macnamara, Hambrick, Oswald (2014) meta-analysis. https://pubmed.ncbi.nlm.nih.gov/24986855/ ; https://doi.org/10.1177/0956797614535810
- [V] Macnamara and Maitra (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6731745/
- [V] Hambrick, Macnamara, Oswald (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7461852/
- [V] Hambrick, Altmann, Oswald, Meinz, Gobet (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC4101876/
- [V] Ericsson and Harwell (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6824411/
- [V] Platz, Kopiez, Lehmann, Wolf (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC4073287/
- [V] Gobet and Ereku (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC4132259/
- [V] Mosing et al. (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11433073/
- [V] Macnamara, Moreau, Hambrick (2016). https://pubmed.ncbi.nlm.nih.gov/27217246/
- [M] Gobet and Campitelli (2007), via Hambrick 2020 and a Europe PMC abstract. https://europepmc.org/
- [M] Charness et al. (2005), via Hambrick 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7461852/
- [M] Burgoyne et al. (2016, 2019), via Hambrick 2020 and Ericsson and Harwell 2019.
- [V] de Bruin et al. (2008) abstract. https://pubmed.ncbi.nlm.nih.gov/18433518/
- [M] Vaci et al. (2019); Clark et al. (2022); Li et al. (2023), abstracts via Europe PMC. https://europepmc.org/
- [M] Southwick et al. (2026). https://doi.org/10.1177/09567976261452568 ; https://pubmed.ncbi.nlm.nih.gov/42335356/ (abstract only)
- [V] Song (2026) AI-assisted music practice. https://pmc.ncbi.nlm.nih.gov/articles/PMC13619875/
- [V] Ruoss et al. (2024). https://arxiv.org/abs/2402.04494
- [V] Zhang et al. (2025) ChessLLM. https://arxiv.org/abs/2501.17186
- [V] McIlroy-Young et al. (2020) Maia. https://arxiv.org/abs/2006.01855
- [V] McGrath et al. (2022). https://arxiv.org/abs/2111.09259
- [V] Schut et al. (2023/2025). https://arxiv.org/abs/2310.16410 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12002201/
- [V] Tang (2026) brittleness. https://arxiv.org/html/2605.17565
- [M] Wen, Tang, Anderson (2025) ChessQA (no scores). https://arxiv.org/abs/2510.23948
- [M] ChessGPT (2023) (no scores). https://arxiv.org/abs/2306.09200
- [V] Toshniwal et al. (2022). https://arxiv.org/abs/2102.13249
- [V] Jones (2021). https://arxiv.org/abs/2104.03113
- [V] Silver et al. (2017). https://arxiv.org/abs/1712.01815
- [V] Zelikman et al. (2022) STaR. https://arxiv.org/abs/2203.14465
- [V] Chen et al. (2024) SPIN. https://arxiv.org/abs/2401.01335
- [V] An et al. (2023) LeMa. https://arxiv.org/abs/2310.20689
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291
- [V] Jiang et al. (2021) PLR. https://arxiv.org/abs/2010.03934
- [V] Chen et al. (2023) Skill-it. https://arxiv.org/abs/2307.14430
- [V] Snell et al. (2024). https://arxiv.org/abs/2408.03314
- [V] Chen et al. (2025) SEC. https://arxiv.org/abs/2505.14970
- [V] Huang et al. (2024). https://arxiv.org/abs/2310.01798
- [V] Valmeekam et al. (2023). https://arxiv.org/abs/2310.08118
- [V] Kambhampati et al. (2024). https://arxiv.org/abs/2402.01817
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651
- [V] Song et al. (2025) Mind the gap. https://arxiv.org/abs/2412.02674
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Wang et al. (2024) AWM. https://arxiv.org/abs/2409.07429
- [V] Sprague et al. (2024). https://arxiv.org/abs/2409.12183
- [V] Hicke et al. (2026) MedSimAI. https://arxiv.org/abs/2503.05793
- [V] Song et al. (2026) CPX-MATE. https://pmc.ncbi.nlm.nih.gov/articles/PMC13740229/
- [V] Ma et al. (2023) HypoCompass. https://arxiv.org/abs/2310.05292
- [V] Zhang et al. (2025) Pelican-VL, DPPO. https://arxiv.org/abs/2511.16602
