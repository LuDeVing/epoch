# Deployed CBR: deep document

*Subfield C08.03. Focus: the first successful deployed case-based reasoning (CBR) system (Lockheed CLAVIER, Bill Mark 1989) and what the deployed-CBR line taught, up to 2026 LLM case memories. Evidence ids (a01 to d18) are in evidence_a-d.jsonl; claim ids (K01 to K21) are in claims.jsonl; caveats are in critique.md. Why it matters for our agent: background plus a source of memory tests.*

## 1. What it is

Case-based reasoning solves a new problem by finding a similar solved problem (a case), reusing its solution, fixing the difference, and storing the result. The four steps are Retrieve, Reuse, Revise, Retain (the "4 Rs"; Aamodt and Plaza 1994, a09, b01).

"Deployed CBR" is the set of systems that did this in daily work, not in a lab. The first one is CLAVIER at Lockheed, Sunnyvale. It picks which composite part molds to cure together in an autoclave and where to place them. It matches the parts list against a library of past loads labelled valid or invalid (a01).

The point for us. CBR was chosen in the field when rules and physics models had failed. It worked because the humans already reasoned from remembered episodes. The 2025 LLM agents (Memento, ExpeL, ReasoningBank, Huawei Re4) rediscovered the same recipe: store whole episodes with outcomes, retrieve few, let a checker or a human revise, write back only verified cases.

Scope of the evidence. All 1990s numbers are builder self-reports with no control group (K02, K20). The 2023 to 2026 LLM numbers are real measurements but mostly single runs and often not matched on tokens. The primary Mark 1989 and Hennessy and Hinkle 1992 papers were never read (K15).

## 2. History and theories in depth

### 2.1 CLAVIER (Lockheed, 1987 to 1992)

- Autoclave cure takes 6 to 8 hours. Two autoclaves at Sunnyvale, 2 to 3 loads a day. A spoiled part costs up to $50,000. Hottest and coolest part must stay within spec (a delta of 30 F in the IAAI version) and ramp at least 1 degree per minute (a01, c02).
- Experts could not state rules for mold placement. They explained placement only by pointing to a specific past load. A mold moved 12 to 24 inches can leave the target thermal profile (c02). A thermodynamic model was infeasible because of mold-to-mold airflow. A machine-learning route was rejected: huge search space, only a few dozen past loads (a02; "few dozen" not re-verified, critique).
- Timeline: build began March 1989; first version fielded November 1989; v1.0 done September 1990; v2.0 by November 1991; extended to Lockheed Georgia in December 1992. About two person-years. In daily use since September 1990. Five operators and two support staff use it (a03, c07). Aamodt and Plaza date the start to 1987 and regular use to fall 1990 (a09).
- Seed cases came from the experts' own notebooks (a03, c04). The earlier process was already case-based by hand (a15).
- Retrieval ranks loads on three criteria: cover the needed parts, minimise extra parts, maximise compatibility (a05).
- Adaptation is done by the human, then CLAVIER validates the new load against similar valid and invalid loads. Three outcomes: configure; suggest a similar valid alternative; predict incompatible and split the load, trading efficiency for lower risk (a05, c26). An early version substituted parts automatically; engineers disliked this (a21, lecture slides only).
- Validity is context-dependent and non-monotonic. The same load can be valid in one autoclave and invalid in another. A load judged valid can be re-labelled invalid when a similar, less risky one turns up. Users edit and delete cases (a06).
- Payoff claim: discrepancy reports from incompatible loads "virtually eliminated". Each report costs about $1000 to inspect, about $2000 average if scrapped, $20,000 to $50,000 for some parts. Stated saving: "thousands of dollars each month". No counts, no N, no control period (a04).
- Lessons: users did not care about the AI technique. Interface and labour-saving features decided success. The most popular feature was printing load reports. The planner was built for several weeks ahead but trustworthy only to about one week, because input data was poor (a07, c06, c08).

### 2.2 Other early deployments

- **General Dynamics Electric Boat valve selection.** A rule system (started 1986, 5 man-years) turned brittle and hard to maintain. A 1988 feasibility study moved to CBR; fielded 1990; used in 3 of 4 departments by fall 1991. The CBR system cost 5 man-years; both together $750,000. Dec 1990 to Sep 1991: 20,000 non-conformances handled. Cost cut about 10 percent, $240,000 saved in under a year (a10, b02, b03). The rule base was reused to structure and seed the first case base (b04).
- **Compaq SMART (1991 to 1992).** Help desk on Inference's CBR Express. End-user calls opened in March 1991 more than doubled support requests while staff had already grown 100 percent. Search takes 3 to 5 seconds; target under 2 minutes and about 5 questions; case base about 600 cases at first analysis; payback one year. A human-factors test in October 1991: under 50 percent of test cases resolved without SMART, 87 percent with it, N not stated (a12, a13). A 2006 review restates it as "over 95 percent of calls" resolved by untrained staff (a16). Use 87 percent (critique). Case base curation: knowledge engineer plus domain expert; new cases confirmed before activation; automated test tools produce random text and wrong answers to find badly defined cases (a14).
- **GE Plastics FormTool (1994 on).** CBR selects a past colour formula and adapts pigment loadings. Chosen because the exact physics (Kubelka-Munk) is only approximate and exhaustive colorant search needs a human to pre-pick 5 to 7 colorants (a17). Build cost: two developers, under 1 year, $300,000, one plastic family at one site (a19). Measured: test chips in the revise phase fell from 4.2 to 2.7 per match (-36 percent), about 4.5 hours saved per match, about 22,500 hours per year at over 5,000 matches; request-to-formula time cut by two thirds. A 1994 rematch of 100 colours found cheaper formulas for 64 (a18). Savings: $200,000 in 1994, $1.2M in 1995, $1.5M in 1996, then about $2.4M per year (estimate). Over 50,000 matched colours on file; 130 custom matches per week in 2004 (a17). Retention was automatic, with a redundancy filter. The case base moved from Access to Oracle as one global base (a20). Spreading to other sites was harder than expected because each site's process had to be standardised (a19).
- **Shells and spread.** Commercial CBR shells existed by 1991 to 1992 (ReMind, CBR Express/ART-IM, Esteem, CasePower, KATE-CBR, ReCall, S3-Case; a11, b06). Help desks were the fastest-growing type; cases were shown to people as information chunks (b05). By 1997 over 130 major companies fielded CBR (Watson 1997, via a15). Conversational CBR became the call-centre standard; NEC SQUAD served 150,000 employees (a16). Other fielded systems: Snecma Cassiopee (aim: halve diagnosis time, 25 percent less downtime) and the ICARUS locomotive diagnosis system, fielded 1997 (a15).

### 2.3 Why CBR was picked: the common pattern (a32, c24)

1. A human process already recalled past cases.
2. Rules or physics models had failed or were too brittle.
3. Outcomes were labelled (valid/invalid, resolved/not).
4. Humans did the adaptation or approval.
5. Case retention was gated (expert review, redundancy filter, confirmation workflow).
6. Small seed from real work, then growth by use. CLAVIER was live about 8 months after the start.

### 2.4 The LLM revival (2020 to 2026)

CBR returned as a framing for LLM agents and RAG. Systems in this document: CBR-KBQA (Das 2021), Atzeni 2022 (text games), Sourati 2023 (fallacies), ExpeL (2023/24), DS-Agent (2024), CBR-RAG (2024), Memento (2025), Re4 at Huawei (2025), ReasoningBank (2025), Dynamic Cheatsheet, Evo-Memory, ACE, Agent KB, plus 2026 work (CBR-to-SQL, TextBFGS, DomAgent, persistent memory for data science). Details in section 6. A boundary note: fine-tuned transformers doing arithmetic behave like similar-case lookup, not rule following (Hu et al. 2024, b28): random split 100 percent but held-out squares fail away from the training boundary. Rule-following fine-tuning gave Llama-2-7B 91.1 percent at 9-digit addition against under 40 percent for scratchpad.

## 3. Core findings with exact numbers

Status key: Established = two or more independent sources agree; Single = one source; Contested = sources conflict; Self-report = builder claim, no control.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| CLAVIER fielded within months; daily use | build Mar 1989, fielded Nov 1989, v1.0 Sep 1990; about 2 person-years; 5 operators plus 2 support | a03, c07 | Established (two versions of same paper) |
| CLAVIER cut incompatible loads | "virtually eliminated"; no counts; $1000 inspect, $2000 average scrap, $20K to $50K some parts | a04, c03 | Self-report |
| Electric Boat valve CBR | $750K total build; about 10 percent cost cut = $240K in under 1 year; 20,000 non-conformances Dec 1990 to Sep 1991 | a10, b03 | Self-report |
| SMART resolution | under 50 percent without vs 87 percent with (lab test, N unstated); review says over 95 percent of calls | a13, a16 | Contested; use 87 |
| FormTool test chips | 4.2 to 2.7 per match (-36 percent); about 4.5 h saved per match; 22,500 h per year | a18 | Self-report, but a measured process metric |
| FormTool rematch | cheaper formula for 64 of 100 colours; $2.4M per year estimated | a18 | Self-report (only rematch test of the era) |
| FormTool build cost | 2 developers, under 1 year, $300,000 | a19 | Self-report |
| Failed cases useful in CLAVIER | invalid loads drive "likely incompatible" and split advice | a05, c26 | Single system |
| Context decides validity | same load valid in one autoclave, invalid in another | a06, c04 | Single source (K05) |
| Whole solved cases beat text insights (code tasks) | DS-Agent avg rank 2.08 full; 2.58 w/o ReviseRank; 3.41 w/o CBR (GPT-4, 12 dev tasks, 5 trials); deployment one-pass 85 percent (GPT-3.5), 99 percent (GPT-4) vs best baseline 56 and 60 | c13, c14 | Single source |
| DS-Agent cost | $0.06 (GPT-3.5) and $1.60 (GPT-4) per run in development, $0.0045 and $0.135 in deployment | c13 | Single source |
| Insights vs cases differ by task | ExpeL insights-only vs retrieval-only: HotpotQA 36 vs 31; ALFWorld 50 vs 55; WebShop 37 vs 38 | a31, b19 | Contested (K09) |
| ExpeL retrieval choice | ALFWorld SR: ReAct 40.0; random cases 42.5; reasoning-similarity 48.5; task-similarity 59.0 | b20 | Established that similarity beats random (K10) |
| ExpeL vs ReAct | HotpotQA 39.0 vs 28.0; ALFWorld 59.0 vs 40.0 | b19 | Single paper |
| ExpeL transfer | FEVER SR Act 58, ReAct 63, ExpeL transfer 70 | b22 | Single paper |
| Memento CBR gain (same pipeline) | F1/PM: HLE +4.5/+7.0 (22.2/17.4 to 26.7/24.4); SimpleQA +3.7/+5.3; DeepResearcher +6.7/+8.2 (59.9/72.2 to 66.6/80.4) | b10, d12 | Single source, no replication (K06, K19) |
| Memento OOD | +4.7 to +9.6 abs points with 4 cases; Musique F1 35.6 to 40.6, Bamboogle 77.5 to 86.2, PopQA 57.9 to 64.0 | b13 | Single source |
| Memento GAIA | val 87.88 Pass@3 (top-1 on 26 Jun 2025 board); test 79.40; Pass@1 val gpt-4.1+o3 70.91 | a29, b14 | Single source |
| Number of cases K | DeepResearcher F1/PM: K0 59.9/72.2, K1 63.6/77.9, K2 63.7/78.1, K4 64.5/78.5, K8 64.1/78.2, K32 63.9/78.1 | b11, d13 | Established: few cases enough (K07) |
| ReasoningBank k | success 46.0 (k=2), 45.5 (k=3), 44.4 (k=4) | d03 | Established with Memento, Sourati |
| Random or bad cases hurt | random 1-shot below zero-shot (driving); NOMAD RMSLE 0.0632 vs 0.0608 baseline (lower better); retrieved fallacy labels match truth only 27.7 percent | c18, c15, c19 | Established as a risk (K08) |
| Failures stored raw | WebArena-Shopping, Gemini-2.5-flash, success-only to with-failures: Synapse 40.6 to 41.7; AWM 44.4 to 42.2; ReasoningBank 46.5 to 49.7 | d02 | Contested (K04) |
| Unfiltered write-back | RegAgent SR fixed 67.53, add-all 55.48, coarse judge 63.18, tuned judge 67.35, strict 70.95; EHRAgent ACC 16.75 / 13.05 / 26.19 / 34.66 / 38.50 | d04 | Established (K16); strict = oracle |
| Experience-following | more similar a retrieved case, more the output copies it; wrong cases propagate; strict addition reaches error-free after about 2000 executions (AgentDriver) | d05 | Established (K18) |
| Gain scales with task similarity | ReMem gain vs within-dataset similarity: Pearson 0.717 (Gemini 2.5 Flash), 0.563 (Claude 3.7 Sonnet) | d09 | Established (K18) |
| Distilled memory beats raw (web agents) | WebArena SR: flash 40.5 none / 42.1 Synapse / 44.1 AWM / 48.8 ReasoningBank; pro 46.7/47.7/47.6/53.9; Claude-3.7-sonnet 41.7/42.6/40.8/46.3 | d01 | Contested overall (K09, K17) |
| ReasoningBank token cost | tokens per task: none 50,847; Synapse 58,515 (+15.1 percent); AWM 59,373 (+16.8); ReasoningBank 53,055 (+4.3); steps 9.7 to 8.3 | d03 | Single source (K21) |
| Non-agentic reasoning: curated vs raw | Claude 3.5 Sonnet AIME 2024 baseline 23.3 / raw retrieval 43.3 / DC-Cu 50.0 / DC-RS 46.7; AIME 2025 6.7/23.3/36.7/30.0; GPQA 59.6/63.6/61.1/68.7 | d06 | Contested (K17) |
| Raw retrieval can fall below baseline | GPT-4o Game of 24 baseline 10.0, raw 6.0, DC-Cu 93.0, DC-RS 99.0 (a stored Python solver); MMLU-Pro Eng 53.2 / 48.8 / 44.0 / 51.2 | d06 | Single source |
| Full-history append | AIME 2024 Sonnet FH 26.7 vs DC 50.0 (baseline 23.3); GPT-4o FH 6.7 vs 40.0 (baseline 20.0) | d07 | Single source |
| Evo-Memory | raw ExpRAG a strong baseline: 0.50 vs about 0.29 to 0.31 for several designs in one panel; ReMem 0.65 | d08 | Single source; table garbled |
| Brevity collapse | ACE: context 18,282 tokens (acc 66.7) collapsed to 122 tokens (acc 57.1), below 63.7 no-adapt baseline | d10 | Single source |
| Agent KB refine | GAIA val pass@1: none 55.15; full 61.21; raw workflow 58.18; w/o Refine 55.15; w/o Retrieve 57.58; pass@3 73.9 | d11 | Single source |
| Huawei Re4 offline | FF1 DCN: CBR 64.67, +SFT 67.87, +Re4 70.11; SP 55.83, 57.98, 61.92; clean test sets 689 and 366 | c10 | Single run per method |
| Huawei Re4 online | about 6,000 online samples; +2.75 percent (DCN), +10.08 percent (SP) FF1 over deployed CBR+SFT | c11, d14 | Single source |
| Naive fine-tuning below naive CBR | DCN FF1 49.46 vs 64.01; SP 38.71 vs 54.60 | c28 | Single source (K12) |
| Retain removal | large drop online; size unverified (do not cite -78.65 or -69.22; they are axis labels) | c11, d14, critique | Direction single-source; magnitude unknown |
| Re4 other | repetitive generation down 2.47 (DCN) and 2.41 (SP) points; retriever finetune removal cost about 1 percent FF1 | c12 | Single source |
| CBR-RAG legal QA | No-RAG 0.8967; hybrid AnglEBERT k=3 full 0.9141 (+1.94 percent); support-only k=1 0.9121; case base 2,084; test 32 synthetic Q/A | a24, b16 | Weak: one-tailed t-test at 95 percent; 90 percent vs hybrid BERT k=1 |
| CBR-KBQA | ComplexWebQuestions strict: T5-11B 52.4, T5+revise 55.6, CBR-KBQA 67.1; CFQ MCD1 72.9 to 87.8, MCD2 69.2 to 75.1, MCD3 62.0 to 71.5 | a26 | Single source |
| Text-game CBR | TextWorld Commonsense hard OOD: average drop 6 percent with CBR vs 35 percent without; Jericho better or comparable on 24 of 33 games | a27 | Single source |
| Fallacy CBR | +2.5 to 6 F1 in domain, up to +8 OOD; representation changes F1 by 6 to 8; best at k=1 with 10 percent of case base (4-point grid, no variance) | a28, c19, d15 | 10-percent claim weak |
| CBR-to-SQL | MIMICSQL AccEX 0.899 vs 0.894 fine-tuned MedTS; EHRSQL with under 10 percent data +11.9 AccEX over RAG-to-SQL | c16 | Single source |
| TextBFGS | HumanEval-Hard Plus 86.67 to 93.33; MBPP-Hard Plus 58.12 to 78.63; problem-based retrieval collapsed to 58.12 across domains (baseline 48.72), error-based +16.24 better | c17 | Single, industry, no replication |
| DomAgent | truck CAN task: GPT-4o 71.22 alone, 98.04 with retriever; Qwen2.5-7B 39.62 vanilla to 96.64 | c21 | Single source |
| Persistent CBR memory | Spaceship Titanic 0.8147 vs 0.8098 (SD 0.0024 vs 0.0042); NOMAD worse, p=0.20; 4 seeds | c15 | Single; underpowered (K14) |
| Argumentation with factors | gain only when new case has many factors (6 to 10; biggest jump 9 to 10); 50 pairs per set | c20 | Single; small |

## 4. Mechanisms and models

An engineer can build each of these.

### 4.1 Case record (CLAVIER style, a01, a06, c04)

Fields: problem description; solution; outcome label (valid / invalid / resolved / failed); context tags (environment, which autoclave, which model version); source (expert seed or system-made); date; reviewer. Cases are editable and deletable. Labels may change when a better contrasting case appears (non-monotonic store).

### 4.2 Retrieve

- CLAVIER used a three-term score: coverage of needed items, penalty for extras, compatibility quality (a05). General form: score = coverage - extras + compatibility, ranked.
- Help desks: ask a few questions, rerank cases by answers (conversational CBR, a12, a16). Target about 5 questions.
- LLM era: embed problem text (bge-m3 in Re4, c10; hybrid AnglEBERT in CBR-RAG with weights [0.25, 0.40, 0.35] over question and support, a24). Task similarity beat reasoning-step similarity beat random in ExpeL (b20). TextBFGS retrieves by the error message, not the problem text, which survived a cross-domain test where problem-based retrieval collapsed (c17).
- Rule of thumb from data: retrieve 1 to 4 cases. Gains saturate at K=4 (Memento) and fall past about 2 (ReasoningBank) (b11, d03).
- Add a context filter before ranking (K05). Untested for LLMs (d18).

### 4.3 Reuse and Revise

- CLAVIER: human adapts, system validates by looking at nearest valid and nearest invalid cases (a05).
- Re4 and DS-Agent: the LLM adapts, a human (Huawei engineers) or code execution (DS-Agent) revises (c27).
- Agent KB: refine retrieved experiences before use; removing Refine cost the whole gain (55.15 = no KB) (d11).
- Rule: revision must be driven by real output (matches guardrail G2).

### 4.4 Retain with a gate (Re4, FormTool, Xiong; a20, c11, d04)

1. Solve problem. 2. Verify with an external check (tests, human, oracle). 3. If verified and not redundant (FormTool filter), write the case. 4. If the case later proves wrong or useless, delete it (Xiong: deletion with a strict judge helps, d05). Never add-all: 55.48 vs frozen 67.53 vs gated 70.95 on RegAgent (d04). Memory sizes differed (fixed 50 to 180, add-all up to 4100), so tokens were not matched.

### 4.5 Experience-following (the failure mechanism, d05)

Output copies the retrieved case in proportion to similarity. So a wrong but similar case is copied. This is why raw failures and unverified successes hurt, and why random cases drag results below zero-shot (c18). Defence: verified labels, contrast pairs, a random-case control in every test.

### 4.6 Distilling cases (ReasoningBank, ACE, DC; d01, d06, d10)

Store lessons derived from both successes and failures; consolidate in code. Risks: brevity bias (ACE 18,282 to 122 tokens, accuracy 66.7 to 57.1); a total rewrite can collapse the memory. Use incremental edits (ACE) and keep raw cases behind the lesson.

### 4.7 Memento loop (a29, b09)

Planner (GPT-4.1) retrieves K cases of (state, action, reward) from a case bank, plans, an executor (o3 or o4-mini) runs tools, the trajectory and reward are written back. The optional learned retriever (parametric) beat similarity retrieval by under 1 point PM (80.46 vs 79.84 at iteration 1; 85.44 vs 84.85 at iteration 5; b12). No gradient update to the LLM.

## 5. What holds up

### 5.1 Replications and independent agreement

- Few retrieved cases are enough: Memento (K=1 gets most of the gain), ReasoningBank (best near 1 to 2), Sourati (k=1). Three independent sources (K07). Established.
- Retrieved cases can hurt: driving (random 1-shot below zero-shot), NOMAD, fallacy labels 27.7 percent correct, Dynamic Cheatsheet raw retrieval below baseline on GPT-4o Game of 24 and MMLU-Pro Engineering. Four-plus sources (K08). Established.
- Similarity beats random: ExpeL (59.0 vs 42.5), driving, CBR-RAG (weak). Established (K10).
- Unfiltered write-back harms; verified write-back helps: Xiong (four agents), Huawei Re4 (direction), Evo-Memory (unfiltered failures hurt). Established (K16).
- Benefit tracks task recurrence and feedback quality: Evo-Memory (r 0.717, 0.563), ACE, DC, Xiong. Established (K18).
- 1990s pattern (rules failed, seed from experts, retain with review, humans adapt): CLAVIER, Electric Boat, SMART, FormTool. Four systems but all builder-reported (K01).

### 5.2 Failures, contradictions, weak spots

- No controlled before/after study with N and a baseline exists for any 1990s system (d17). SMART's 87 percent has no N and drifts to over 95 percent in a review.
- Raw vs distilled is unresolved. For distilled: ReasoningBank, Agent KB refine, Dynamic Cheatsheet. For raw: Evo-Memory ExpRAG, ExpeL ALFWorld (55 vs 50), DS-Agent (executable cases beat text insights). It is not predictable from task type yet (K09, K17).
- Failed cases: CLAVIER used invalid loads on purpose; in LLMs raw failures hurt (AWM 44.4 to 42.2) while distilled failures help (46.5 to 49.7). Memento stores failures but has no success-only arm (d13). Contested (K04).
- Memento: the offline-to-online executor gap is -18.0 F1 (48.8 to 30.8) and the authors suspect contamination. The CBR gain is a same-pipeline contrast, so contamination of the executor does not explain it. A leak through the case bank is not excluded. No replication (K19). Ablations mix CBR with planner changes (planning gain on DeepResearcher +29.1 F1 / +11.5 PM, larger than CBR's).
- Re4 Retain-removal size unverified (critique c11). Do not quote it.
- Persistent memory over loops: four seeds; NOMAD worse; the memory can reduce exploration (c15, c25).
- Sourati "10 percent best" is a four-ratio grid with no variance, and the abstract says case-base size has negligible effect while the body says 10 percent is best (d15). Weak.
- CBR-RAG's gain is 1.94 percent on 32 synthetic questions with a one-tailed test (b17). Weak.
- ExpeL ALFWorld 59.0 only partly re-found in a binary text (critique).
- Moderators found: task recurrence (similarity), feedback quality, model strength (Claude 3.7 gain smaller than Gemini in d01), tool-reuse effects (Game of 24 jump is a stored solver), number of factors (c20).

### 5.3 Interventions that worked

Verified-only write-back (+15.5 SR over add-all, RegAgent); distilled lessons including failures (+3.2 SR from failures, d02); refine-before-use (+6.06 points GAIA, d11); error-message retrieval across domains (c17); human-revised cases retained (Re4).

### 5.4 Interventions that did not work

Add-all memory; raw failure storage; full-history append (AIME 2024 Sonnet 26.7 vs 50.0); reflection text added to insights (HotpotQA 29.0 vs ReAct 28.0, b21); large case bases (fallacy); fine-tuning in place of CBR on Huawei units; automatic part substitution in CLAVIER (engineers disliked it, a21).

## 6. Language models

How they behave on case-memory tasks, and what changed it.

- **Cases help most when tasks recur and feedback is reliable.** Evo-Memory gain correlates with within-dataset task similarity (0.717, 0.563). PDDL and ALFWorld (tight clusters) gain most (d09).
- **Out of distribution.** Memento +4.7 to +9.6 points (b13); Atzeni 6 percent drop with CBR vs 35 percent without (a27); CBR-KBQA CFQ MCD1 72.9 to 87.8 (a26). All used cases from related tasks.
- **Retrieval quality is the swing factor.** ExpeL 59.0 vs 42.5 random vs 40.0 ReAct. Random 1-shot below zero-shot in driving, where the best model, Llama 3.3 70B, was already at 0.937 to 0.941 without cases (c18), so there was little room. Fallacy retrieved labels matched truth 27.7 percent (a28).
- **Number of cases.** 1 to 4 (section 3).
- **Raw vs curated memory on non-agentic reasoning** (Dynamic Cheatsheet, Claude 3.5 Sonnet): AIME 2024 23.3 baseline, 43.3 raw retrieval, 50.0 curated (30 questions, 1 question = 3.3 points). GPQA 59.6/63.6/61.1/68.7. GPT-4o Game of 24 10.0 baseline, 6.0 raw, 93.0 to 99.0 curated, but this is a stored Python solver, so tool reuse (d06). Sonnet moved only 12 to 14 there. Tokens not matched; DC adds a curator call.
- **Write-back policy.** Add-all is worse than a frozen 50 to 180 case store on four agents (d04).
- **Cost.** ReasoningBank +4.3 percent tokens against +15.1 and +16.8 for Synapse and AWM, with the bigger gain (d03). DS-Agent deployment is about 12 times cheaper than development per run ($1.60 to $0.135 for GPT-4, c13). TextBFGS claims -50.6 percent tokens on HumanEval vs TextGrad (c17, industry author).
- **Deployment.** Huawei Re4: about 6,000 online samples, +2.75 and +10.08 percent FF1 over deployed CBR+SFT. Offline FF1 +3.30 and +6.80 percent. Single run per method (c10, c11).
- **Small models.** DomAgent Qwen2.5-7B from 39.62 to 96.64 on a truck-signal task with retrieval; GPT-4o 71.22 to 98.04 (c21). CBR-to-SQL with 10 percent of the data beat RAG-to-SQL at full data on nearly all metrics (c16). CBR memory lifts small models most where knowledge is missing. Less relevant if we use one strong model.
- **Collapse risks.** ACE brevity collapse (d10); memory reduces exploration in loops (c25, c15); copying wrong neighbours (d05).
- **Planning vs memory.** In Memento, planning (+29.1 F1) moved more than CBR (+6.7 F1). Concise planning beat deliberate planning: Qwen3-32B Fast 53.94 vs Slow 40.61; gpt-4.1+o3 70.91 vs o3+o3 63.03 (b14). This agrees with guardrail G11.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Gate every write to memory on an external verified outcome. Never add-all. | memory, G2, G3 | [E] | d04, d05, c11, d14 (K16) |
| 2 | Retrieve few: default 1 to 4 items, never dump a large store. | memory, S3 | [E] | b11, d03, a28 (K07) |
| 3 | Every memory test carries a random-item arm and a no-memory arm; do not ship a memory that fails to beat random items. | G7, memory | [E] | c18, c15, d06, a28 (K08) |
| 4 | Rank by task similarity, not by surface or reasoning-step similarity. | memory | [E] | b20, c18 (K10) |
| 5 | Record the problem class and use within-class similarity as a gate: use memory only when the new item is close to stored ones. | S0, memory | [E] | d09, d05 (K18) |
| 6 | Do not cite 1990s deployment numbers as effect sizes. | none | [E] | K02, K20 |
| 7 | Keep SCHEMA's rule "lessons shown after the first attempt, trusted after helping on two problems". Deployed CBR does not contradict it. Executable or checked cases are the strongest type. | memory | [E] consistent | b19, c14 |

### Test first (single-source or contested; none goes into SCHEMA.md until the test passes)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Raw verified cases vs distilled one-line lessons vs random items vs no memory, at equal tokens, per task type. | memory | [C] | d01, d06, d08, a31, c14 (K09, K17) |
| T2 | Store failures as distilled lessons or contrast pairs (CLAVIER style); compare with successes only. | memory, S7 | [C] | a05, d02, d09, d13 (K04) |
| T3 | Context tags and a context filter before retrieval. | memory, S0 | [S] | a06, d18 (K05) |
| T4 | A Retain step on our bench (frozen vs gated add) and its true effect size. | memory | [S] | c11, d04 (K11) |
| T5 | Retrieve by error message or failing output, not by problem text, at S7 repair. | S7, memory | [S] | c17 |
| T6 | Refine/adapt a retrieved case with execution feedback before use (Revise as a code-checked step). | O7, S5 | [S] | c14, d11, c27 (K13) |
| T7 | Case memory only at an impasse vs always (ties to G12 and G1). | G1, G12, S6 | [S] | c15, c25 |
| T8 | Executable cases (code, programs) beat text lessons for code-like items. | memory | [S] | c14, b26 |
| T9 | Case memory plus short planning vs planning alone (planning moved more than CBR in Memento). | G11 | [S] | b10, b14 |

## 8. Concrete tests on our bench

All arms at equal tokens (count the retrieved text, the curator call and setup, per G7). Use at least 3 seeds, report per item type. Hold the case bank out from the test items (disjoint tasks, K19).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 case memory vs controls | ARC-style and BrainTeaser-style items with a recurrent class structure | no memory; random 2 solved items; top-2 task-similar verified items; one-line lessons | solve rate at equal tokens; tokens per solved item | similar > random by 5 to 15 points on recurrent classes; random about equal or below no memory; lessons cheaper than raw cases |
| B2 failures | same | successes only; successes + raw failures; successes + distilled failure lessons | solve rate; repeat-error rate | distilled failures +2 to 4 points; raw failures flat or negative (as in d02) |
| B3 write-back gating | repeated-class stream of 300+ items | frozen seed store; add-all; add only on verified pass | accuracy over the stream; store size; tokens | gated > frozen > add-all (RegAgent gap 70.95 / 67.53 / 55.48) |
| B4 K sweep | any | K = 0, 1, 2, 4, 8 | solve rate; tokens | saturation at K = 1 to 4 |
| B5 context filter | items tagged with a setting where the same pattern has different answers | retrieve by similarity; retrieve with a same-context filter | accuracy on the changed-context items | filter helps where context flips the answer; no effect otherwise |
| B6 error-keyed retrieval | code or program repair items | retrieve by problem text vs by failing output | pass@1 after one repair | error-keyed wins cross-domain (TextBFGS +16.24) |
| B7 refine step | items with an executable check | reuse as is; refine with execution feedback | pass rate | refine +3 to 6 points (Agent KB +6.06) |
| B8 gate by similarity | mixed novel and recurrent items | always use memory; use only above a similarity threshold | accuracy on novel items | gate removes the harm on novel items |

## 9. What does not transfer, and why

- **Deployment numbers (dollars, scrap, hours).** Self-reports in manufacturing and call centres. No control group. They say CBR is practical, not that it improves accuracy.
- **CLAVIER's human adaptation.** Our loop has no human at revise. Code checks must stand in (G2, G3).
- **Large, slowly curated case bases.** FormTool had 50,000 colours and a global DB. Our bench has few items; the LLM evidence says small stores and K = 1 to 4 are best.
- **Agent benchmarks (WebArena, ALFWorld, GAIA).** Highly recurrent tasks. Our reasoning-puzzle items may recur less, so gains from similar cases may shrink (the r of 0.563 to 0.717 is within datasets).
- **Fine-tuning comparisons (Huawei).** The naive SFT loss applies where the model lacks function knowledge. A frozen strong model on puzzles is a different case.
- **Small-model lifts (DomAgent 39.62 to 96.64).** Largely missing-knowledge effects.
- **Tool-reuse wins (Game of 24 93 to 99).** The memory stored a solver. That is a subgoal library (SCHEMA section 7), not case reasoning.
- **Benchmark leaderboard results (Memento GAIA 87.88).** Mixed planner, tools, executor; contamination suspected on the offline-online step; no replication.
- **Rule-vs-case in transformer weights (Hu et al.).** It concerns what fine-tuned models learn, not prompting.

## 10. Open questions

1. Does case memory beat plain summaries and random cases at equal tokens on a non-agentic reasoning task? (Partly closed: DC and Evo-Memory give direction, no token-matched or random arm.)
2. Do failed cases, stored CLAVIER style, beat successes-only for an LLM at equal tokens?
3. What is the true size of the Retain effect in Re4? Direction certain, magnitude unknown.
4. What retrieval-quality threshold makes cases net positive? No numeric threshold exists in any source.
5. Raw vs distilled: which wins per task type, and is it predictable?
6. Is there any controlled before/after study of a 1990s deployed CBR system? None found.
7. What do Mark 1989 and Hennessy and Hinkle 1992 say about case count and accuracy? Unread.
8. Does Memento survive a clean, disjoint case bank? Unreplicated.
9. Does a context filter help LLM retrieval? No study.
10. Is "10 percent of case base best" general? Weak: four ratios, no variance.
11. Does persistent memory reduce exploration in open mode (NOMAD)? Four seeds only.

## 11. Sources

[V] opened and read; [M] snippet only or not found.

- [V] Hinkle and Toomey (1995) Applying CBR to Manufacturing, AI Magazine 16(1). https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1124
- [V] Hinkle and Toomey (1994) CLAVIER, IAAI-94. https://cdn.aaai.org/IAAI/1994/IAAI94-007.pdf
- [V] Aamodt and Plaza (1994) Case-Based Reasoning: Foundational Issues. https://www.iiia.csic.es/~enric/papers/AICom.pdf
- [V] Acorn and Walden (1992) SMART, IAAI-92. https://cdn.aaai.org/IAAI/1992/IAAI92-003.pdf
- [V] Cheetham and Watson (2006) Fielded applications of CBR. https://www.maxapress.com/data/article/ker/preview/pdf/S0269888906000580.pdf
- [V] Cheetham (2005) Tenth anniversary of the Plastics Color Formulation Tool, AI Magazine. https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1825
- [V] Watson lecture slides CS760, Univ. of Auckland (slides only; weak). https://www.cs.auckland.ac.nz/~ian/CBR/cbr05.pdf
- [V] Wikipedia, Case-based reasoning (pointer to Mark 1989). https://en.wikipedia.org/wiki/Case-based_reasoning
- [M] Mark (1989) CLAVIER, CBR Workshop proceedings. Not found.
- [M] Hennessy and Hinkle (1992) IEEE Expert 7(5). https://ieeexplore.ieee.org/document/163669
- [V] Wiratunga et al. (2024) CBR-RAG. https://arxiv.org/abs/2404.04302
- [V] Das et al. (2021) CBR for natural language queries over KBs. https://arxiv.org/abs/2104.08762
- [V] Atzeni et al. (2022) CBR for generalization in text games. https://arxiv.org/abs/2110.08470
- [V] Sourati et al. (2023) CBR with LMs for logical fallacies. https://arxiv.org/abs/2301.11879
- [V] Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291
- [V] Majumder et al. (2023) CLIN. https://arxiv.org/abs/2310.10134
- [V] Hu et al. (2024) Case-based or rule-based: transformers on arithmetic. https://arxiv.org/abs/2402.17709
- [V] Guo et al. (2025) Re4 test generation at Huawei. https://arxiv.org/abs/2503.20576
- [V] Guo et al. (2024) DS-Agent. https://arxiv.org/abs/2402.17453
- [V] Stocker (2026) Persistent case-based memory for data science. https://arxiv.org/abs/2606.05250
- [V] Nguyen, Moen, Marttinen (2026) CBR-to-SQL. https://arxiv.org/abs/2603.05569
- [V] Zhang et al. (2026) TextBFGS. https://arxiv.org/abs/2602.00059
- [V] Gan, Dao, Zettsu (2025) CBR-LLM for driving decisions. https://arxiv.org/abs/2506.20531
- [V] Fungwacharakorn et al. (2025) Argumentative reasoning with LMs. https://arxiv.org/abs/2512.12656
- [V] Wang et al. (2026) DomAgent. https://arxiv.org/abs/2603.21430
- [V] CBR for FinQA (2024). https://arxiv.org/abs/2405.13044
- [M] Review of CBR for LLM Agents (2025), abstract only. https://arxiv.org/abs/2504.06943
- [V] Ouyang et al. (2025) ReasoningBank. https://arxiv.org/abs/2509.25140
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952
- [V] Wei et al. (2025) Evo-Memory. https://arxiv.org/abs/2511.20857
- [V] Zhang et al. (2025) Agentic Context Engineering (ACE). https://arxiv.org/abs/2510.04618
- [V] Agent KB (2025). https://arxiv.org/abs/2507.06229
- Internal: C08.03 critique.md; claims.jsonl K01 to K21; SCHEMA.md at C:/Users/User/Desktop/AGI/research_notes/single_agent/SCHEMA.md.

Links to parallel subfields (not covered here): Retrieval and ensembles for LLM forecasts; Analogy and precedent in legal theory; Expert-novice differences; Efficient diagnosis algorithms; Industrial fault detection; Naturalistic decision making; RL on verifiable rewards.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 7 established claims: 4 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C08.03-K01** (number corrected). FormTool has been in use since 1994 (Cheetham abstract), not 1989-1992; Electric Boat (rule base seeded cases, fielded 1990) and SMART (doubled calls Mar 1991, payback one year, 600 cases) check out; Hinkle/AAAI pages bot-blocked so CLAVIER details only partly checked (Aamodt gives CLAVIER start 1987 vs Hinkle 1989). Corrected claim: Deployed CBR systems of 1989-1994 (CLAVIER, SMART, Electric Boat valves, GE FormTool) were built around retrieving whole past cases with outcome labels, seeded from expert notebooks or an existing rule base, rather than from a model of the domain.
- **C08.03-K08** (reworded: the sources support less). NOMAD gap (0.0632 vs 0.0608) is 4 seeds, d=-0.75, p=0.20, not significant; 27.7% label overlap is the highest of the Table 5 in-domain values (explanations; others 6-25%) and the paper says best CBR variants do not reuse retrieved labels, so it is not evidence of harm; random 1-shot below zero-shot is only a general trend in the driving paper, and larger case bases lowering F1 is confirmed. Corrected claim: Retrieved cases can hurt: in a driving study a single randomly chosen example (1-shot) often scored below zero-shot; in a small 4-seed data-science-agent test CBR memory had a worse NOMAD RMSLE than the baseline (0.0632 vs 0.0608, not significant, p=0.20); and in fallacy classification larger case bases lowered F1, with the best setting using 10 percent of the case base.
- **C08.03-K18** (reworded: the sources support less). Pearson 0.717/0.563 (Evo-Memory), ACE/DC 'may degrade' without reliable feedback, and Xiong experience-following are all verified, but no source measures task recurrence (similarity within a dataset is the proxy; correlations are over few datasets) and ACE says 'may degrade'. Corrected claim: Case benefit tracks task similarity within a dataset and the quality of feedback: ReMem's gain correlates with within-dataset task similarity (Pearson 0.717 on Gemini 2.5 Flash, 0.563 on Claude 3.7 Sonnet); ACE and Dynamic Cheatsheet may degrade without reliable feedback signals; and agents copy outputs of similar retrieved records, so wrong similar cases propagate (experience-following).
