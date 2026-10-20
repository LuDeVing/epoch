# Simplicity and logic in reasoning: evidence and a procedure

[V] = checked on the web this session. [M] = from memory, not rechecked. Details inside [M] entries (pages, exact titles) may be imperfect.

## 1. Simplicity

- Lombrozo, T. (2007). Simplicity and probability in causal explanation. Cognitive Psychology 55(3), 232-257. [V] Fewer causes are preferred, other things equal. Simplicity acts as a prior when probability information is missing. Clear probability information overrides it (Exp. 4). So simplicity is a default prior, not a trump card.
- Feldman, J. (2000). Minimization of Boolean complexity in human concept learning. Nature 407, 630-633. [V] Concept difficulty tracks the length of the shortest equivalent propositional formula. Vigo (2006, "A Note on the Complexity of Boolean Concepts") disputes some of the complexity values [V], so treat the effect as robust but the exact metric as contested.
- Tenenbaum, J. B. & Griffiths, T. L. (2001). Generalization, similarity, and Bayesian inference. Behavioral and Brain Sciences 24, 629-640. [V] The size principle: the likelihood of each example under a hypothesis h is 1/|h|, so tighter hypotheses gain when all the data fit. Its status as a law is debated [V].
- MacKay, D. J. C. (2003). Information Theory, Inference, and Learning Algorithms, ch. 28 (Occam's razor), Cambridge UP. [M] The Bayesian razor: a flexible model spreads probability over many data sets, so it assigns less to the observed one. No separate penalty is needed.
- Rissanen, J. (1978). Modeling by shortest data description. Automatica 14, 465-471. [M] Minimum description length: the best hypothesis minimizes L(H) + L(data | H).
- Solomonoff, R. J. (1964). A formal theory of inductive inference, Parts I and II. Information and Control 7. [M] Kolmogorov, A. N. (1965), Problems of Information Transmission 1. [M] Li & Vitanyi, An Introduction to Kolmogorov Complexity and Its Applications (Springer). [M] A universal prior weights each program by 2^-length. It is incomputable, so it works only as an ideal to approximate.
- Simon, H. A. (1956). Rational choice and the structure of the environment. Psychological Review 63, 129-138. [M] Satisficing: take the first option that meets an aspiration level, under bounded rationality.
- When simplicity misleads: Lombrozo's override [V]. Other known limits, all [M]: the no-free-lunch theorems (Wolpert) mean the razor is a bias that pays off only in some worlds; simplicity depends on the description language (Goodman's "grue"); true mechanisms are often complicated (biology, many-cause systems); and the data may be too sparse to favor any model.

## 2. Logic of discovery and inference

- Peirce, C. S. (c. 1903). Harvard lectures on pragmatism, in Collected Papers 5.171-5.189. [M] Abduction proposes a hypothesis, deduction derives its consequences, and induction tests them.
- Lipton, P. (2004). Inference to the Best Explanation, 2nd ed., Routledge. [M] Choose the "loveliest" (most explanatory) hypothesis among the "likely" ones. Explanatory virtues are heuristics for likelihood.
- Popper, K. (1959). The Logic of Scientific Discovery, Hutchinson (German original 1934). [M] Derive risky predictions. A refutation is decisive; a corroboration is not proof.
- Mayo, D. (2018). Statistical Inference as Severe Testing, Cambridge UP. [M] Evidence supports H only if the test would probably have exposed the error had H been false.
- Platt, J. R. (1964). Strong inference. Science 146(3642), 347-353, doi:10.1126/science.146.3642.347. [V] Devise alternative hypotheses, design a crucial experiment that can exclude some of them, run it cleanly, then repeat. Davis (2006) argues the paper's strength is rhetorical rather than empirical [V], so treat it as a discipline, not a proven method.
- Polya, G. (1945). How to Solve It, Princeton UP. [M] Four phases: understand, plan, carry out, look back. Heuristics: auxiliary problem, specialization, generalization, analogy, working backwards, "Can you solve a related problem?"
- Newell, A. & Simon, H. A. (1972). Human Problem Solving, Prentice-Hall; the earlier General Problem Solver (Newell, Shaw & Simon, 1959). [M] Means-ends analysis: measure the difference between the current and goal states, then pick an operator that reduces it. If the operator is blocked, set its precondition as a subgoal.

## 3. Errors in checking candidates

- Wason, P. C. (1960). On the failure to eliminate hypotheses in a conceptual task. Quarterly Journal of Experimental Psychology 12, 129-140. [M] The 2-4-6 task: people test only triples that fit their rule.
- Klayman, J. & Ha, Y.-W. (1987). Confirmation, disconfirmation, and information in hypothesis testing. Psychological Review 94(2), 211-228. [V] The positive test strategy is a general heuristic, often good, but it fails when the true rule is narrower or broader than the guess, or when the confirming tests do not discriminate.
- Evans, J. St. B. T., Barston, J. L. & Pollard, P. (1983). On the conflict between logic and belief in syllogistic reasoning. Memory & Cognition 11, 295-306. [M] Belief bias: believable conclusions are accepted even when the argument is invalid.
- Lord, C. G., Lepper, M. R. & Preston, E. (1984). Considering the opposite: A corrective strategy for social judgment. J. Personality and Social Psychology 47(6), 1231-1243. [V] Asking people to consider the opposite reduced biased assimilation and biased hypothesis testing more than "be fair and unbiased" instructions did.

## 4. Problem finding and posing

- Getzels, J. W. & Csikszentmihalyi, M. (1976). The Creative Vision: A Longitudinal Study of Problem Finding in Art, Wiley. [M] (my search returned nothing for this book). Art students who explored more and left the problem open longer produced more original work, judged years later.
- Silver, E. A. (1994). On mathematical problem posing. For the Learning of Mathematics 14(1), 19-28. [V] Posing means generating new problems or reformulating given ones, before, during or after solving.
- Brown, S. I. & Walter, M. I. (1983/2005). The Art of Problem Posing, Erlbaum. [M] The "What-if-not?" method: list a problem's attributes, negate or vary each, and pose the new problems.
- Polya (1945) [M], above, for auxiliary problems. Auxiliary problems (a special case, a weaker goal, an analogue) help because they give a solved or solvable foothold.

## Ordered procedure

Each step cites its source. Keep every step as written text that a checker can inspect.

1. **Restate the problem.** List the unknowns, data and conditions. Check that the conditions are consistent and sufficient. (Polya, understand) Write the single criterion that would make an answer correct. Without it no test can be designed (Popper).
2. **Pose auxiliary problems before attacking the goal.** Choose at least three: a special case, a simpler analogue, the problem worked backwards from its goal, and one from "what if not?" (negate an attribute or relax a condition). (Polya; Brown & Walter; Silver) Solve the cheap ones first. Their solutions yield the examples used in steps 3 and 6. Keep a ledger of the problems posed. Do not close it early, since problem finders profit from keeping the problem open (Getzels & Csikszentmihalyi, [M]).
3. **Generate many candidate hypotheses (abduction).** Aim for at least 4, including a deliberately different one, not just variants of the first idea. (Peirce; Platt: "devise alternative hypotheses") Where candidates share a parent, store the difference, not a copy.
4. **Derive consequences (deduction).** For each hypothesis, list concrete predictions on the data in hand and on new inputs. Run the hypothesis, don't just reason about it. Where a prediction cannot be calculated, state that. (Peirce; Popper)
5. **Check candidates against all evidence, including the opposite.** Before accepting a candidate, write why it might be wrong, and look for cases where it predicts failure. (Lord, Lepper & Preston) Do not test only cases the hypothesis expects to succeed. Add tests where it should fail (Klayman & Ha; Wason). Judge arguments by form, not by whether the conclusion seems plausible (belief bias, Evans et al.).
6. **Design a discriminating test among survivors.** For each pair of rivals that still fit, find an input where their predictions differ. Prefer the input that splits the field most evenly (largest expected elimination, Platt's "crucial experiment"). It must be severe: if the favored hypothesis is false, the test should probably show it (Mayo). Run it. Remove or demote the loser. Repeat from step 3 with sharper variants of the winners (Platt's cycle). If no input separates two hypotheses, they are equivalent for this purpose; keep the simpler.
7. **Break ties by simplicity.** Among hypotheses that fit all evidence, score each by description length: the length of the hypothesis plus the length of its exceptions (MDL, Rissanen). Fewer free parameters and fewer ad hoc causes win (Lombrozo; MacKay; Feldman). Prefer the narrower hypothesis that still covers every observation (size principle). Treat this as a prior, not a verdict. Override it when the evidence or a known mechanism clearly favors the complex candidate (Lombrozo Exp. 4). Check that "simple" is judged in a fixed language, not one chosen to flatter a candidate (Goodman, [M]).
8. **Stop at good enough.** If a candidate passes every available test and a discriminating test has been run against its nearest rival, accept it. Do not keep searching for the optimum when the cost of more search exceeds the expected gain (Simon, satisficing). If a test is blocked, set the blocker as a subgoal (Newell & Simon, means-ends).
9. **Look back.** Re-derive the answer by a different route, test the result on a special case, and ask what the solution method could solve elsewhere. Record any problem you posed along the way that is worth solving later (Polya, look back; Silver).

## Caveats for implementation

- Items marked [M] were not rechecked this session. Verify before quoting them in anything external.
- Occam and MDL are priors. They can't replace tests, and the "best explanation" (Lipton) is only a guide to which hypotheses to test first.
- Strong inference and the positive test strategy both depend on the hypothesis space containing the truth. Step 2's auxiliary problems and "what-if-not?" exist to widen it.
