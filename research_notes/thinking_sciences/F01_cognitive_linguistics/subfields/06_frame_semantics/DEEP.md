# Frame semantics: deep document

*Subfield F01.06 of cognitive linguistics. Evidence ids (a01 to d17) point to evidence_a-d.jsonl; claim ids (F01.06-K01 to K22) point to claims.jsonl. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Date: 2026-11-20.*

## 1. What it is

Frame semantics is Charles Fillmore's theory that a word is understood against a background scene. The scene is a frame. A frame has named roles, called frame elements (FEs). A word evokes the frame, and the reader fills the roles from the text or from background knowledge.

Standard example: the Commercial Transaction frame has BUYER, SELLER, GOODS, MONEY. The words buy, sell, pay, charge, customer and clerk all evoke it. Each verb puts some roles in front and pushes others to the back. Buy focuses buyer and goods. Sell focuses seller and goods. Pay focuses buyer, money and seller (a01, d14).

Three ideas matter for an agent:

1. **Roles are local to a frame.** They are not global labels like "agent" or "patient". Each frame has its own set (a06).
2. **Frames are world knowledge, not only word knowledge.** Frames form a hierarchy; a sub-frame inherits roles from its parent (a02, a07).
3. **Readers fill blanks silently.** A sentence about opening presents and blowing out candles calls up a birthday party that is never mentioned (d14). The empty role is filled from the frame without notice.

The operational form is FrameNet: over 1,200 frames and about 13,000 lexical units in version 1.7 (a06, a23), plus parsers that label frames and roles in text.

**Why it matters for our agent.** Schema state S1/S2 says "restate the task, write it as a frame, look for empty roles". A task is a scene with roles (who, what, to whom, with what, when, under which limits). A role the text leaves blank is a gap. The agent can either ask or label an explicit assumption.

**Honest summary of the evidence.** The theory is well supported as a description of language and as an annotation scheme. It is almost untested as a reasoning scaffold. All LLM work in this folder is annotation, role labelling, fine-tuning, or the adjacent topic of underspecified tasks. No study tests "write the task as a frame and find blanks" on general reasoning (K22, d07, d16, d17).

## 2. History and theories in depth

**Case grammar to frames (1960s to 1976).** Fillmore began with case grammar: a verb takes a fixed set of deep cases. He moved to frames in the mid-1970s. In his early papers (1976, 1977) a *scene* is a cognitive entity and a *frame* is a linguistic one. Later he dropped "scene" and called a frame a cognitive structuring device indexed by words (a03, snippet only). His canonical statement is "Frame semantics" (1982, Seoul, pp. 111-137; a04, not opened). In 1985 he contrasted understanding-semantics (U-semantics, built on frames) with truth-conditional semantics (T-semantics) (a05, not opened). We have not opened any of these primary texts. What we know comes from Petruck's 1996 review (d14) and from the FrameNet papers.

**Fillmore ran no numbered human experiments (d14).** The theory was argued from linguistic examples, for instance land vs ground implying different background scenes. So there are no founding effect sizes for frame semantics itself. The nearest human data is script research (Bower, Black and Turner 1979): unstated script actions are confused with stated ones, and recognition ratings run stated > unstated script > novel false items. We have this only second hand (d15, PDF blocked). A later citation says recall of typical script actions was not reliably better than irrelevant information, so the script effect has bounds.

**Rival lineage: Minsky frames and slot-filling dialogue.** Minsky's frames and the GUS dialogue system (Bobrow et al. 1977) keep a frame of slots and keep asking until every slot is filled (c27, not opened). This is the engineering ancestor of modern slot filling. It is related to Fillmore's frames but is not the same theory.

**FrameNet (1997-98).** Lowe, Baker and Fillmore (1997) and Baker, Fillmore and Lowe (1998) started the Berkeley project (a01, a02, a06, a07). Plan: 5,000 lexical units, about 250,000 sentences, over 500,000 FE tokens. At project year 2 they had about 10,000 annotated sentences for just under 200 lemmas. Lowe et al. say they make no cognitive claim; "frame" is used formally (a01). Worked example of specialisation: TRANSPORTATION has MOVER, MEANS, PATH. DRIVING adds DRIVER and VEHICLE. RIDING_1 makes the RIDER the mover (a07). RealEstateTransaction inherits CommercialTransaction with BORROWER=BUYER and LOAN=PAYMENT and adds LENDER. Buying a candy bar vs a house evokes different sub-frames and changes where a "with" phrase attaches (a02). Frame choice changes interpretation.

**Statistical role labelling (2002-2019).**
- Gildea and Jurafsky (2002): first statistical FE labeller. 67 frames, 49,013 sentences, 99,232 FEs. Labelling given constituents: 80.4% (82.1% with 18 collapsed thematic roles); identify-and-label 65% precision, 61% recall; 13% of FEs have no matching parse constituent (a08, a09, c21).
- Das et al. (2014) SEMAFOR: frame ID plus argument ID with exact constraint decoding (a11-a13, c19).
- Swayamdipta et al. (2017) Open-SESAME: first syntax-free neural parser (a14, c20).
- Kabbach (2019) replication: reported baselines replicate but preprocessing choices move F1 as much as recent model gains (a15, c22).
- Hartmann et al. (2017) released YAGS, an out-of-domain test; parsers lose accuracy on it (a28, not opened).

**LLM era (2024-2026).** Frame identification with prompts (Chundru 2025; Garat 2025), role extraction (Devasier 2025), frame-knowledge injection by fine-tuning (Rai 2025, 2026), FrameNet tags in commonsense prompts (Iwamoto and Ohara 2026), and the adjacent line on underspecified tasks (Ambig-SWE, Ask or Assume, Learning to Ask, OntoAgent). See section 6.

**Competing views.**
- Abstract thematic roles vs frame-specific roles: abstract ones scored slightly higher in the 2002 labeller (82.1 vs 80.4), so frame-specific roles are not obviously better for machines (a09).
- WordNet vs FrameNet: a WordNet sense-tag prompt matched the FrameNet prompt on commonsense choice (c15). The gain may be generic structure, not frame-specific.
- Pragmatic reading of numbers: much of the classic gain-loss framing effect may come from reading "saved 200" as "at least 200" (Mandel; b25, second hand). This is a rival to the idea that framing changes the scene.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Frame element labelling, given constituents (2002) | 80.4% frame-specific roles; 82.1% abstract roles; 40.9% baseline; 13% of FEs have no parse match | Gildea and Jurafsky 2002 (a08, a09, c21) | [E] |
| Supervised argument ID plateau, gold frames | about 75.6 to 77.1 F1 (FN 1.5/1.7); SEMAFOR 59.1 and Open-SESAME 62.9 to 65.3 on older splits | a14, a16, b01 | [E] |
| Cost of wrong predicted frames | about 22 F1 (18 partial credit) in SEMAFOR | Das 2014 (a12, c19) | [E] |
| Constraint "at most one overt argument per role" | holds for 96.5% of role instances; LP decoding tight 99.8% | Das 2014 (a13) | [S] |
| Out-of-domain loss for supervised parsers | about 20 F1 | Kabbach review of Johansson and Nugues (a16) | [E] |
| Preprocessing effects in replication | dependency parser change +1.3 to +2.6 F1; exemplar sentences +1.2 vs +2.8 originally; hierarchy feature +0.5 to +0.7 vs +1.3 | Kabbach 2019 (a15) | [S] |
| Frame ID, prompted Llama-3.1-8B, FN 1.7 | 80.0 zero-shot; 83.5 direct-QA few-shot; fine-tuned 91.9; supervised best 92.6 | Chundru 2025 (a23, b06, c08) | [E] |
| Frame ID, 6 LLMs on 6 violence frames | 90.5 to 94.3 F1 (DeepSeek Chat 94.3 at 100 shots); gain from shots 1.4 to 8.7 | Garat 2025 (a17, b04, b05, c05) | [E] |
| Frame names only vs with LU definitions (FN 1.7, simple format) | 59.9 / 79.1 vs 76.5 / 80.9 (zero / few shot) | Chundru (b07) | [S] |
| LLM-written frame definitions vs gold | 75.0 (Llama-8B), 79.3 (DeepSeek-V3.1), 80.0 (GPT-4o) vs gold 78.4 | Chundru (b08) | [S] |
| Frame ID out of domain | YAGS 65.4 zero-shot, 80.7 fine-tuned; Artifacts 25.6 to 49.6 | Chundru (b09, c10) | [E] |
| Shared errors with old parser | FIDO 519 errors, Llama 538, 320 shared; 296 of 320 the same wrong frame | Chundru (b10) | [S] |
| Role extraction, few-shot FN 1.7 | GPT-4o-mini 0.471; DeepSeek V3 0.548; GPT-4o 0.592 (supervised 0.755 to 0.813) | Devasier 2025 (a20, c01, d01) | [E] |
| Role extraction, fine-tuned | GPT-4o-mini 0.768; Phi-4 0.785; Qwen2.5-72B 0.794; vs Ai and Tu 0.755 (Table 4) | Devasier (b11, d01) | [E] |
| Prior best in Table 3 vs Table 4 | 0.771 (ICL table) vs 0.755 (fine-tune table), same paper, one arXiv version | d01, d02 | [S] |
| Output format for role extraction (GPT-4o-mini) | XML 0.342; JSON-all 0.440; Markdown 0.448; JSON-exist 0.471. JSON-all recall 0.577, precision 0.356 | Devasier (b12, c02) | [S] |
| Unseen roles vs unseen frames | Phi-4 0.785 overall; unseen frames 0.708 (-7.7); unseen FEs 0.515 (-27.0) | Devasier (b13, c03) | [E] |
| Data scaling | 1% 0.508; 5% 0.619; 10% 0.688; 25% 0.746; 100% 0.785 | Devasier (a21, c04) | [S] |
| Out-of-domain role extraction (YAGS) | GPT-4o 0.387; Phi-4 0.533; SEMAFOR 0.570 | Devasier (a21) | [E] |
| LLM-written instructions vs manual | GPT-4o-made 0.225 vs manual 0.471 | Devasier (a21) | [S] |
| Role F1 by FE info in the prompt (zero-shot, gold frame) | GPT-4o-mini 3.9 none / 36.4 def only / 39.3 all; DeepSeek Chat 28.0 / 42.4 / 44.6; Haiku 22.2 / 33.0 / 32.4; GPT-4o 25.6 / 32.1 / 39.5 | Garat (c07, b02) | [S] |
| Killing frame full parse | 0.0 F1 with no frame info; 34.1 to 48.4 zero-shot with info; best-shot 68.7 to 82.9 (Sonnet 3.5 82.9 at 250 shots, GPT-4o 80.2 at 400) | Garat (b02, a18, c06) | [S] |
| Per-role F1, Killing frame | Target 96-97; Victim 73-83; Killer 48-71; Cause 44-68; Means 0-50; Instrument 0-50 | Garat (b03) | [S] |
| FSRL gold frames vs detected frames | DeepSeek Reasoner 77.4 vs 74.9; Sonnet 76.3 vs 68.6; GPT-4o 73.9 vs 66.9; Haiku 68.9 vs 53.5; GPT-4o-mini 67.1 vs 53.2 | Garat (b01, b04, c06) | [S] |
| Frame injection by LoRA, CONFER | Llama-3.1-8B few-shot 0.39 to 0.75; zero-shot 0.52 to 0.55; GPT-OSS-20B 0.39; roles-only F1 0.14 to 0.60 | Rai 2025, 2026 (c11-c14, b16, b17) | [S] |
| FrameNet tags in prompts, SWAG | GPT-4o-mini 75.2 to 79.5-80.3; WordNet 80.3 | Iwamoto and Ohara 2026 (c15) | [C] |
| CoT listing FEs before defining a frame | FE-Eval 0.69 to 0.79-0.80; definition quality 3.40 vs 3.43-3.44 | Han 2024 (c16) | [S] |
| LLM-assisted annotation (Brazilian Portuguese) | 311 sentences; 14.96 vs 12.97 min per sentence; core-role coverage human 95.8%, machine 34.2%, hybrid 90.7%; annotation sets +24% | Belcavello 2025 (a25, b15) | [S] |
| Metaphor frames on crime reasoning (human) | Steen: N 253 / 259 / 252 / 1026, effects F<1 to 1.10 n.s.; Thibodeau and Boroditsky pooled N=876, w=.14 | b18, b19 | [C] |
| Loftus-Palmer verb effect | no overall effect, N=1204; moderator: description length b=-0.11 [-0.22,-0.004] | Holmes 2024 (b20, b21) | [C] |
| Asian disease framing (human) | Many Labs 1: about 53-67% of original size (snippet only) | b24 | [C] |
| LLM gain-loss framing | 2,550 decisions; championship +1.40 to +1.84; career -0.37 to -0.60 (sign flips) | Westover 2025 (b26) | [S] |
| LLM framing debiasing | DeFrame cuts BBQ framing disparity 92% on 8 models (3B-14B); CogBias framing 35.6 to 41.4% | b27, b28 | [C] |
| Reframing flips (7-8B models) | average flip 28.6%; value-tinted 36.3-47.2% vs paraphrase 18.0-21.5%; prompt fixes fail or amplify; hidden-state method 39.9 to 11.9% | FRAGILE (d08, d09) | [S] |
| Detecting underspecified tasks (Ambig-SWE) | Sonnet 4 acc/FPR/FNR strong prompt .89/.03/.18, neutral .74/.08/.44; Llama 3.1 70B FPR up to .95; Qwen 3 Coder never asks (FNR 1.00) | Vijayvargiya 2026 (c17, d03) | [E] |
| Value of asking | resolve rate up to +74% vs non-interactive; Sonnet 3.5 and Haiku 3.5 recover up to 80% of Full | Ambig-SWE (c17, d04) | [E] |
| Separate gate vs inline reminder | Sonnet 4.5: Full 70.8; Hidden 54.8; Interactive 70.4; UA-Single 61.2; UA-Multi 69.4 (vs Single p<0.001, vs Full p=0.458); queries 3.06 vs 1.84; about $3.50 vs $2.03 per task | Edwards and Schuster 2026 (c18, d05, d06) | [S] |
| Missing information in real tool queries | 56.0% of problematic queries; asking prompt raises correct asking: gpt-4o 0.52 to 0.90, o3-mini 0.00 to 0.78; final answer gpt-4o 0.34 to 0.36 | Wang 2025 (d12) | [E] |
| Slot ontology for elicitation | ReqElicitGym 101 scenarios: IRE 0.13 plain, 0.52 best prompt baseline, 0.41 ontology alone, 0.69 OntoAgent | Jin 2026 (d11) | [S] |
| FrameNet roles in requirements prompt | R01 44 vs 5-7 requirements; R02 26 vs 10-13; no accuracy measured | Kundi 2026 (d10) | [S] |

## 4. Mechanisms and models

### 4.1 Frame lookup and role template (what a frame is as a data structure)

A frame record: `name`, `definition`, `core_roles[]`, `peripheral_roles[]` (means, instrument, time, place, cause, manner), `parent` (inheritance), `lexical_units[]`. A role record: `name`, `type`, `core|peripheral`, `excludes`, `requires`. FrameNet's constraint relations are the part an engineer can code: "excludes" (two roles cannot both appear) and "requires" (if one appears, so must another) (a11).

Scaffold implementation for S1/S2:
1. Model names the frame of the task ("this is a Booking / Debugging / Forecasting / Request-for-advice task").
2. Model lists roles as JSON: `{role, filler_text | null, source: "stated"|"inferred"|"absent"}`.
3. Code lists every role whose filler is null or inferred and passes them to an ask-or-assume step.
4. Code checks that the JSON parses and that each filler marked "stated" appears as a span in the task text.

Why JSON with absent roles: Devasier found JSON listing only existing roles beat XML by 12.9 F1 points. Listing all possible roles raised recall to 0.577 but cut precision to 0.356: the model invents fillers for absent roles (b12, c02). So the template must give "absent" as a legal value, and code must check "stated" fillers against the text.

### 4.2 Two-stage parsing, and why errors compound

SEMAFOR runs frame ID first, then argument ID. A wrong frame costs about 22 F1 (a12). LLMs repeat the pattern: with gold frames role F1 is 67 to 77, with detected frames small models fall to 53 (b04). Mechanism: the frame sets the role inventory, so a wrong frame hands the second stage the wrong slots. For the scaffold this means one frame guess is a single point of failure. Cheap fix: let code check the roles against the frame's required roles, and re-pick the frame when too many required roles are impossible to fill. This is a design idea, not tested.

Devasier's role-first frame selection is a related mechanism. The model predicts roles, then the frame is chosen from the role set: 0.882 overall, 0.862 on ambiguous targets (b14).

### 4.3 Joint decoding with constraints

Das et al. found "at most one overt argument per role" holds for 96.5% of role instances, and exact decoding that enforces such constraints gave structurally clean output (a13). Gildea and Jurafsky found joint prediction of all roles beats labelling each alone: for "blame", {Evaluee, Judge, Reason} has prior 0.549, {Evaluee, Reason} 0.167, {Evaluee, Judge} 0.160, {Evaluee} 0.097 (a10). Engineering rule: ask for all roles in one JSON object, then run code constraints (no two roles with the same span; excluded pairs not both filled).

### 4.4 Missing-role detection and ask-or-assume gate

This is the part that matters most. Mechanisms tested in the nearby literature:
- **Separate gate agent.** Edwards and Schuster's Intent Agent only decides "ask or not". It beat a single agent told to check each turn (69.4 vs 61.2, p<0.001) and matched the forced-ask baseline (70.4, p=0.621) (d05). It asked in 344 of 500 tasks vs 369, with 3.06 vs 1.84 queries per task (d06). Both gates use generic "what is missing" prompts, not role lists (d07).
- **Strong detection prompt.** In Ambig-SWE only the strongest prompt on Sonnet 4 reached accuracy .89 with false positive .03 and false negative .18. Other models either never asked or asked on almost everything (Llama 3.1 70B FPR .93 to .95) (d03).
- **Ask-when-needed prompt.** Correct asking rose, but the final answer rose much less for some models (gpt-4o A3 0.34 to 0.36) (d12). Asking only helps if the answer changes the output.
- **Slot ontology chooses the question.** OntoAgent's code picks which slot to ask about; the model only writes the question. IRE 0.13 plain to 0.69 (d11). The ontology alone moved 0.13 to 0.41. Information-gain ranking of questions beat question-only reasoning (d13, abstract level).

### 4.5 Frame knowledge injected by training (upper bound, not a scaffold)

LoRA on FrameNet frames raised few-shot event inference on CONFER from 0.39 to 0.75 for Llama-3.1-8B and roles-only F1 from 0.14 to 0.60 (c11-c14). No matched non-FrameNet LoRA control exists, so the gain may be generic fine-tuning. We cannot use this.

## 5. What holds up

**Holds up well.**
- Frame identification is nearly solved with a candidate list: 80 to 94 F1 depending on setup, and a small fine-tuned model reaches 91.9 vs 92.6 for the best supervised system (K03).
- Role filling is the hard step. Few-shot LLM argument F1 sits at 47 to 59 on the full benchmark and 67 to 77 with gold frames on six frames. Supervised sits at 75 to 81 (K04).
- Rare, optional roles are missed most: Means and Instrument 0 to 50 F1, Cause 44-68, vs Victim 73-83. Unseen FEs cost 27.0 F1 vs 7.7 for unseen frames (K07).
- Out-of-domain failure: YAGS and Artifacts; GPT-4o 0.387 vs SEMAFOR 0.570; 296 of 320 shared errors are the same wrong frame (K09).
- Underspecification: models rarely notice, asking recovers much, detection is prompt- and model-sensitive (K17, K20).

**Replications and failures.**
- Kabbach's replication: baselines replicate, but the parser change moves F1 by +1.3 to +2.6, as large as claimed model gains; extra training data gains replicate smaller (+1.2 vs +2.8) (a15).
- Human wording effects are fragile. Steen et al. found no metaphor-frame difference across four experiments (N up to 1,026); power was about .95 for f=.25 but only .27 for f=.10. Thibodeau and Boroditsky re-coded the data with updated norms and found a small effect (pooled N=876, w=.14; Exp 2 only p=.039). Loftus-Palmer's smashed/hit effect did not replicate overall in N=1,204 (Holmes 2024), only inside a moderator (description length, b=-0.11, borderline p=.04). Earlier null replications: Read 1978, McAllister 1988, Raghunath 2021. A planned multi-lab replication of N about 2,000 had not run by late 2026 (b23).
- Asian disease framing replicates at about 53-67% of the original size (snippet only) and may shrink under a pragmatic reading of numbers (b24, b25).
- Script effects on recall are bounded (d15, second-hand).
- A WordNet control matched the FrameNet gain in a commonsense prompt (c15). That undercuts a frame-specific benefit.

**Moderators and boundary conditions.**
- Format: XML tags lose 12.9 F1 to JSON-exist (b12).
- Model: strong models (DeepSeek) already know frames; role definitions help weak ones (GPT-4o-mini 3.9 to 39.3) and add less for strong ones (Haiku 22.2 to 32.4; DeepSeek Chat 28.0 to 44.6) (c07).
- Shots help roles (+30 to +41 F1 on Killing) far more than frame ID (+1.4 to +8.7) (b05).
- Granularity: frame names alone work in multiple-choice format (80.1) but not in the simple format zero-shot (59.9). Differences of 1 to 3 points are inside the 3-run noise in places (c09).
- Benchmark correlation: MuSR-type reasoning correlates positively with argument ID; IFEval correlates negatively (a22, values not recorded).
- Prompts written by GPT-4o for role extraction scored 0.225 vs 0.471 manual (a21), but LLM-written frame definitions for frame ID matched gold (b08). So "self-written" works for definitions and fails for instructions.

**Interventions that worked.**
- Frame and role definitions in the prompt, plus examples (K05, K06) [S].
- A separate ask-or-assume gate over an inline reminder: +8.2 points, about 1.5 to 1.7x cost (d05, d06) [S].
- A fixed slot ontology to choose what to ask (d11) [S].
- Naming the roles first in a chain of thought for definitions (c16) [S].
- Human correction of a parser (hybrid): core-role coverage kept at 90.7% (b15).

**Interventions that did not work.**
- Text-level value-anchor and neutralising prompts against framing flips in 7-8B models: no help, sometimes worse (d08).
- Generic "be unbiased" debiasing: helps framing items but hurts others (hyperbolic discounting -13.4; mental accounting and disposition effect worsen) (b28).
- Machine-only annotation: 34.2% core-role coverage vs 95.8% for humans (b15).
- Time saved by pre-annotation: only 1.99 minutes per sentence (a25), echoing Rehbein 2009 (a26, second hand).
- FrameNet tags did not beat WordNet tags (c15).

## 6. Language models

**Frame naming.** Easy. Six LLMs at 90.5 to 94.3 F1 on six frames (b04); Llama-3.1-8B at 80.0 to 83.5 on all of FN 1.7 with a candidate list (b06). The frames were given as options, so this is choosing, not discovering (c08).

**Role filling.** Hard.
- Devasier (FN 1.7, full benchmark): GPT-4o-mini 0.471, DeepSeek V3 0.548, GPT-4o 0.592 few-shot. Fine-tuned open models reach 0.768 to 0.794 and pass the 0.755 Table 4 baseline by 3.0 to 3.9 points. In Table 3 the same prior system is 0.771 and KAF-SPA is 0.813, so "beat supervised" holds only against the Table 4 row. There is only one arXiv version, so the 0.755 vs 0.771 difference is a table difference, not a version change (d01, d02).
- Garat (six violence frames, 100 test examples): with gold frames 67.1 to 77.4; DeepSeek Reasoner 77.4 vs supervised 75.56 to 77.06. The authors say a direct comparison is not feasible. Do not mix the Killing-frame numbers (82.9, 80.2) with this headline; those are for one frame (critique item 3).
- What changed it: frame and role definitions (GPT-4o-mini 3.9 to 39.3 zero-shot), examples (+30 to +41), JSON-exist format (+12.9 over XML), fine-tuning (GPT-4o-mini 0.471 few-shot to 0.768 fine-tuned).
- Predicted vs gold frames: small models lose 14 to 15 points (Haiku 68.9 to 53.5; GPT-4o-mini 67.1 to 53.2); Reasoner loses 2.5 (77.4 to 74.9).

**Which model.** Reasoning-heavy models help: DeepSeek Reasoner was best at role labelling (77.4), and benchmark correlation says multi-step reasoning predicts argument ID (a22). Size is not decisive: Qwen2.5-3B 0.752 beat Llama-3.3-70B 0.743 in one table (b14).

**Frontier 2026 models.** No per-role F1 for GPT-5, Claude 4.x or Gemini 2.5+ was found (d16). The newest numbers are Sonnet 3.5 and GPT-4o era. The Garat findings on Means and Instrument may be out of date for the models we run.

**Frames in prompts for downstream tasks.**
- SWAG: GPT-4o-mini 75.2 +/- 0.3 to 79.5-80.3 with FrameNet tags; WordNet 80.3 +/- 0.6; GPT-5 mini 80.9 to 84.9 (row pairing partly inferred from garbled text); not peer reviewed (c15).
- Requirements: FrameNet roles forced into the prompt gave 44 vs 5-7 requirements with small Llama 3.2 models. No correctness rating, no equal-length control (d10).
- Natural language inference: frame-tuned Llama 0.39 to 0.75 few-shot; the base model dropped when given few-shot examples (0.52 to 0.39), which matches the CONFER original (c13, c14).

**Adjacent behaviour that matters most for us: missing information.**
- Models rarely notice and rarely ask. Qwen 3 Coder never asked (FNR 1.00). Reasoning models almost never asked without a prompt (A1 0.00 to 0.10) (d03, d12).
- Prompt and model decide the outcome: Sonnet 3.5 swings from FNR .81 (neutral) to .09 (moderate) while FPR rises .00 to .24 (d03).
- Asking recovers 80% (Sonnet 3.5, Haiku 3.5) to 89% (Sonnet 4) of lost performance in Ambig-SWE; interaction up to +74% (d04, c17).
- A separate gate costs more: Sonnet 4.5 asked 3.06 vs 1.84 questions per task and cost about $3.50 vs $2.03 (cost row mapping inferred from a garbled table) (d06). That is not an equal-token comparison.
- Where UA-Multi did not ask, it resolved 76.92% (Hidden 77.56%), so it skipped well. Where it asked it resolved 65.99% (UA-Single 55.81%, Hidden 44.48%) (d06).
- Kimi K2.6 asked in 435 of 500 tasks with 8.71 queries per task and was less well calibrated (d06). Poor calibration is a model-level risk.

**Framing in LLMs.**
- Gain-loss framing: sign flips by scenario, from +1.84 (championship, GPT-4o) to -0.60 (career) (b26).
- Fact-preserving reframing flips decisions 28.6% on average in 7-8B models; paraphrase alone flips 18.0 to 21.5%, which is the noise floor (d08). Closed small models show the same order (GPT-4o-mini value-tinted 30.5, Gemini-Flash-2.5-Lite 40.6) (d09).
- DeFrame (4 calls per question, 3B-14B) cuts BBQ framing disparity 92% (b27). It is a four-step prompt on small models, not tested on frontier ones.
- Frontier models and a neutral re-framing step: untested.

## 7. What our agent should take

Each item gives schema part, status and evidence. Nothing below becomes a schema element until its test passes (SCHEMA section 8).

### Add now (established)

1. **Flag missing information, then ask or label an assumption.** Schema: S1/S2 plus ask-or-assume. [E]. Evidence: c17, d03, d04, d12 (K17, K20). Models invent missing arguments and rarely ask unprompted. This item adds only "flag the gap", not a frame template.
2. **Peripheral roles are the weak point, so list them explicitly.** Schema: S1. [E]. Evidence: b03, a21, b13, c03 (K07). When writing the task as roles, include a fixed list of peripheral slots (means, instrument, time, place, cause, constraints, success criterion). Models find these least often.
3. **Do not trust a model-written role list without a check.** Schema: G2/G5 (code checks). [E]. Evidence: b15, a21 (K13 single-source for coverage figure, K07 for role misses). Code verifies that a "stated" filler appears in the text. Machine-only core-role coverage was 34.2% vs 95.8% human.
4. **Frame knowledge drops in unusual domains.** Schema: S0 gate, G7. [E]. Evidence: a24, b09, b10, a21 (K09). Lower trust in frame templates on unusual tasks; record the class pass rate (S9).

### Test first

5. **Write the task as a frame, list roles, flag blanks (S1/S2).** [S] on parts, untested as a whole (K01, K22). Evidence: b02, c07, b05 show definitions and shots help role labelling, but only on annotation.
6. **Separate missing-role gate vs inline reminder (S2/ask).** [S] (K17). Evidence: d05, d06. +8.2 points at about 1.5 to 1.7x cost.
7. **Role-list gate vs generic "what is missing" gate (S1/S2).** Untested directly. Evidence: d07, d11, d13 are indirect.
8. **Tag each filled role stated or inferred (G).** [S] (K21). Evidence: d14, d15, second-hand only. Humans silently fill and later cannot tell inferred from stated.
9. **Output format: JSON with "absent" allowed (S1).** [S] (K08). Evidence: b12, c02.
10. **Let the model write its own frame definition (S1).** [S] (K10). Evidence: b08 (frame ID only); a21 warns that model-written instructions can fail.
11. **Neutral re-framing step as a framing guard (G).** [C] (K16). Evidence: b27 (worked on 3B-14B), d08 (text fixes failed on 7-8B). Frontier untested. Compare with the paraphrase noise floor (18 to 21.5% flips).
12. **Frame-labelled roles vs generic bullet slots (S1).** [C] (K12). Evidence: c15 (WordNet matched FrameNet). The control is missing in the literature.
13. **Slot checklist picks what to ask (S2/memory).** [S] (K18). Evidence: d11. Task-specific slots, not FrameNet.
14. **Few-shot filled-frame exemplars vs more definitions (S1).** [S] (K06). Evidence: b05, c05.

**Memory.** One line per problem class: "roles that were blank on this class and mattered". This extends S9 lessons, shown after the first attempt (SCHEMA section 5). No direct evidence; status [D].

## 8. Concrete tests on our bench

All arms at equal tokens. If an arm uses extra calls, the other arms get matched padding or extra independent attempts with a vote (G7, G11). Each item carries a hidden gold list of the planted missing roles.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 60 tasks with 1 to 3 planted missing roles (underspecified requests, multi-constraint puzzles) | (a) plain restatement; (b) frame step with core and peripheral roles, flags blanks; (c) generic bullet slots; (d) generic "what is missing" prompt | Recall and precision of planted gaps; downstream accuracy of the final answer | (b) beats (d) on recall by 5+ points; small or zero gain over (c) is likely (WordNet precedent). |
| T2 | Same items | Inline reminder vs separate gate call, plus a baseline that spends the same tokens on 2 extra attempts | Final accuracy; false positive rate on fully specified controls; tokens | Gate +5 to +8 points over inline (d05); the extra-attempts arm shows how much is just sampling. |
| T3 | Items with a clear answer once the missing role is supplied (simulated user) | Ask vs label assumption vs guess | Accuracy of the final answer, not asking rate | Asking rises sharply; final accuracy rises less (gpt-4o 0.34 to 0.36 pattern). |
| T4 | 30 tasks with a planted peripheral role (means, instrument, time) | Core-only template vs core plus peripheral template | Recall of the planted peripheral role; precision | Higher recall with peripheral slots; precision check catches invented fillers (JSON-all precision 0.356). |
| T5 | 40 tasks with a two-frame ambiguity (candy bar vs mortgage style) | Free frame choice vs "most specific frame, inherit parent roles" | Correct disambiguation | Small effect; mostly a sanity check on frame-choice errors. |
| T6 | Same task in gain, loss and neutral wording, 30 pairs | No guard; neutral re-statement step; DeFrame-style 4-step prompt | Flip rate vs paraphrase noise floor (18 to 21.5% on small models) | Frontier models flip less; a guard is worth it only if the drop is above noise. |
| T7 | 40 tasks where the model must fill roles | Stated-vs-inferred tag required vs not | Rate of wrong inferred fills used unchecked; final accuracy | Fewer silent wrong assumptions; raw accuracy may not move. |
| T8 | Role extraction on 40 tasks | "absent" allowed vs all slots must be filled | Precision of filled roles; invented fillers | Precision +5 to +10 with "absent" allowed (b12). |
| T9 | Role recall on 30 tasks | Self-written vs retrieved frame definition | Role recall; tokens | Similar recall; self-written costs fewer tokens. |

For every test, log the fields in SCHEMA section 6. Count setup tokens in cost.

## 9. What does not transfer, and why

- **FrameNet role F1 numbers.** They score exact spans on annotated sentences. Our tasks are open problems, not labelled spans.
- **Fine-tuning results.** CONFER 0.39 to 0.75 and roles-only 0.14 to 0.60 come from training on FrameNet (c11-c14); one group wrote both papers. Our agent works through a scaffold, not training.
- **FrameNet's inventory.** About 1,200 frames of verbs and nouns. There is no frame for "ARC grid puzzle" or "forecasting a rate". The agent must write its own frame, so frame quality depends on the model, not on the lexicon. Off-domain, frame knowledge falls (Artifacts 25.6 to 49.6, YAGS) (K09).
- **Theory claims.** Fillmore ran no human experiments (d14). FrameNet's authors say they make no cognitive claim (a01). Reader-completion data (Bower et al. 1979) is second-hand and for stories, not task text.
- **Human framing effects.** Metaphor, verb choice and Asian disease effects are small, contested or reduced by a pragmatic reading (K14, K15). They give no size to expect for an LLM wording effect. LLM flips (28.6%) must be measured on our own agent.
- **Hidden-state framing fixes.** VALIGN (39.9% to 11.9%) needs open weights, not available for an API agent (d08).
- **Requirements output counts.** 44 vs 7 requirements measures verbosity, not correctness (d10).
- **Ask-or-assume numbers.** All from SWE-bench issues with synthetic gaps and a simulated user, on Sonnet 4 / 4.5, Kimi K2.6 and 2024-25 models (d03, d05). Cost ratios are not equal-token.
- **Frame identification as a step.** It is a solved choice among listed lexical units. Our agent has no such list.
- **Fixation risk.** SCHEMA S3 isolates attempts because early output constrains later output. A frame written at S1 may anchor S3 attempts. The frame literature does not study this.

## 10. Open questions

1. Does a "write as frame, list roles, flag blanks" step improve accuracy on underspecified or multi-constraint tasks at equal tokens? No direct study (K22).
2. Does a role-based gap check beat a generic "what is missing" prompt? (d07)
3. How well do 2026 frontier models list peripheral roles (means, instrument, cause) that 2025 models missed at 0 to 50 F1? (d16)
4. Is the FrameNet prompt gain frame-specific or generic structure? A plain role-list control is missing (d17, K12).
5. Does a neutral re-framing step reduce flips in frontier models? FRAGILE says text-level fixes fail at 7-8B; DeFrame says four steps work at 3B-14B (K16).
6. What do Fillmore's primary 1976-1985 papers say about scene completion? Never read (a03-a05, d14).
7. What are the exact numbers in Bower, Black and Turner 1979 (script inference)? PDF blocked (d15).
8. Does frame decomposition help on agent planning benchmarks? OntoAgent uses its own ontology; FrameLLM measured counts only (d10, d11).
9. Does a stated-vs-inferred tag cut silent wrong assumptions?
10. Does the EMNLP camera-ready of Devasier differ from arXiv? Not opened (d02).
11. Does a frame written at S1 anchor later attempts at S3?

## 11. Sources

[V] = opened and read in the research pass; [M] = snippet or second hand only.

- [V] Lowe, Baker, Fillmore (1997), A Frame-Semantic Approach to Semantic Annotation. https://aclanthology.org/W97-0204.pdf (a01, a02)
- [V] Baker, Fillmore, Lowe (1998), The Berkeley FrameNet Project. https://aclanthology.org/P98-1013.pdf (a06, a07)
- [V] Gildea and Jurafsky (2002), Automatic Labeling of Semantic Roles. https://aclanthology.org/J02-3001.pdf (a08-a10, c21)
- [V] Das et al. (2014), Frame-Semantic Parsing. https://aclanthology.org/J14-1002.pdf (a11-a13, c19)
- [V] Swayamdipta et al. (2017), Open-SESAME. https://arxiv.org/abs/1706.09528 (a14, c20)
- [V] Kabbach (2019), Debugging Frame Semantic Role Labeling. https://arxiv.org/abs/1901.07475 (a15, a16, c22)
- [V] Garat, Moncecchi, Wonsever (2025), Exploring In-Context Learning for Frame-Semantic Parsing. https://arxiv.org/abs/2507.23082 (a17-a19, b01-b05, c05-c07)
- [V] Devasier, Mediratta, Li (2025), Can LLMs Extract Frame-Semantic Arguments? https://arxiv.org/abs/2502.12516 (a20-a22, b11-b14, c01-c04, d01, d02)
- [V] Chundru, Poddar, Cao, Jiang (2025), Do LLMs Encode Frame Semantics? https://arxiv.org/abs/2509.19540 (a23, a24, b06-b10, c08-c10)
- [V] Belcavello et al. (2025), LLM-assisted annotation in a perspectivized setting. https://arxiv.org/abs/2510.25904 (a25, b15)
- [V] Rai, Croce, Basili (2025), Injecting Frame Semantics into LLMs. https://aclanthology.org/2025.starsem-1.3 (c11, c12)
- [V] Rai, Croce, Basili (2026), Frame-Semantic Knowledge Injection for Event-Level Inference. https://aclanthology.org/2026.acl-short.55/ (b16, b17, c13, c14)
- [V] Iwamoto and Ohara (2026), FrameNet annotations in LLM prompts. https://www.anlp.jp/proceedings/annual_meeting/2026/pdf_dir/P8-3.pdf (c15; Japanese text garbled)
- [V] Han, Sasano, Takeda (2024), Definition Generation for Automatically Induced Semantic Frames. https://aclanthology.org/2024.findings-acl.661/ (c16)
- [V] Steen, Reijnierse, Burgers (2014), When do natural language metaphors influence reasoning? https://pmc.ncbi.nlm.nih.gov/articles/PMC4260786 (b18)
- [V] Thibodeau and Boroditsky (2015), Measuring effects of metaphor in a dynamic opinion landscape. https://pmc.ncbi.nlm.nih.gov/articles/PMC4517745 (b19)
- [V] Holmes, Kassin, Flusberg (2024), Loftus and Palmer replication. https://escholarship.org/uc/item/0wk430xs (b20-b22)
- [V] Zwaan (2026), Memory, misinformation, and the need to replicate. https://rolfzwaan.substack.com/p/memory-misinformation-and-the-need (b23)
- [V] Westover (2025), An analysis of AI decision under risk. https://arxiv.org/html/2508.00902v1 (b25, b26; Mandel cited second hand)
- [V] Lim, Kim, Whang (2026), DeFrame. https://arxiv.org/html/2602.04306 (b27)
- [V] Huang et al. (2026), CogBias. https://arxiv.org/pdf/2604.01366 (b28)
- [V] Vijayvargiya et al. (2026), Ambig-SWE. https://arxiv.org/pdf/2502.13069 (c17, d03, d04)
- [V] Edwards and Schuster (2026), Ask or Assume? https://arxiv.org/pdf/2603.26233 (c18, d05-d07)
- [V] Hwang et al. (2026), Framing Matters / FRAGILE. https://arxiv.org/pdf/2605.28188 (d08, d09)
- [V] Kundi, Ahmad, Monahan (2026), FrameLLM for Requirements Generation. https://ojs.aaai.org/index.php/AAAI-SS/article/download/42907/50467/47012 (c25, d10)
- [V] Jin et al. (2026), OntoAgent. https://arxiv.org/pdf/2605.05828 (d11)
- [V] Wang et al. (2025), Learning to Ask. https://aclanthology.org/anthology-files/pdf/emnlp/2025.emnlp-main.1104.pdf (c26, d12)
- [V] Kobalczyk et al. (2025), Active Task Disambiguation, abstract level only. https://arxiv.org/pdf/2502.04485 (d13)
- [V] Petruck (1996), Frame Semantics. https://open.istu.edu/mod/resource/view.php?id=6247 (d14)
- [M] Fillmore (1976, 1977), Frame semantics and the nature of language; Scenes-and-frames semantics. https://en.wikipedia.org/wiki/Frame_semantics_(linguistics) (a03)
- [M] Fillmore (1982), Frame semantics. https://en.wikipedia.org/wiki/Frame_semantics_(linguistics) (a04)
- [M] Fillmore (1985), Frames and the semantics of understanding. https://bibbase.org/network/publication/fillmore-framesandthesemanticsofunderstanding-1985 (a05)
- [M] Rehbein et al. (2009), reported in Belcavello (a26)
- [M] Su et al. (2024) and a PropBank GPT-4 study. https://aclanthology.org/2024.dmr-1.12.pdf (a27, c23)
- [M] Hartmann et al. (2017), YAGS, via Chundru (a28)
- [M] Klein et al. (2014), Many Labs 1. https://www.doi.org/10.1027/1864-9335/A000178 (b24)
- [M] Cheng et al. (2024), ChatGPT SRL on PropBank, via Rai (c24)
- [M] Bobrow et al. (1977), GUS. https://doi.org/10.1016/0004-3702(77)90018-2 (c27)
- [M] Bower, Black, Turner (1979), Scripts in memory for text. https://stanford.edu/class/psych205/papers/Bower-etal-1979.pdf (d15; PDF 403)
- [M] Mandel (2014, 2015), numeric quantifiers in framing problems, via Westover (b25)
