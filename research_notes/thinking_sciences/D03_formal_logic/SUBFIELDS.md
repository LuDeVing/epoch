# Formal logic: subfields

Formal logic studies valid inference in precise languages. It is divided by what it covers: proof theory (derivations), model theory (meaning and truth in structures), computability (what can be decided), and families of logics that change the rules (non-monotonic, modal, paraconsistent, intuitionistic, and others). Much of it is runnable: consistency and validity can be checked by programs. Its limit for us is that tasks arrive in natural language and must first be translated into a formal language.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Classical propositional and first-order logic | Syntax, deduction, semantics, soundness and completeness | Frege; Godel (1930); SEP "Classical Logic" | High | Test (S4) and verify (S8): check that stated rules do not contradict |
| Satisfiability and SMT solving | Is a set of constraints consistent; find a model | SAT/SMT solver literature | High | Test and select (S4, S7): code checks consistency, finds a counterexample model |
| Automated theorem proving | Searching for proofs by machine | Resolution (Robinson); proof assistants | Med | Verify (S8) for exact tasks; subgoal library |
| Non-monotonic and default logic | Conclusions that later evidence can withdraw | Reiter; McCarthy; Makinson | High | Revise (S5): default rules with exceptions fit "doubt only on a signal" |
| Modal and epistemic logic | Necessity, knowledge, belief | Kripke; Hintikka | Low | Background only |
| Paraconsistent logic | Reasoning from inconsistent information without explosion | Priest; da Costa | Med | Impasse (S6): keep working with a contradictory set without collapse |
| Intuitionistic and constructive logic | Proof means construction | Brouwer; Dummett | Low | Background only (construction as a witness idea) |
| Logic programming and knowledge representation | Rules and facts run as programs; description logics | Kowalski; Prolog | Med | Represent (S2): rules in a checkable form |
| Inductive logic and ILP | Learning rules from examples | Muggleton | Med | Represent and generate rule candidates (S2, S3) |
| Computability and complexity | What is decidable, how costly | Turing; Church | Low | Background (budget awareness) |

## Dig into next

**1. SAT/SMT consistency and counterexample search.** Questions: (a) Can the rule candidates from S2 be encoded so a solver finds an input where two candidates disagree (the discriminating test in S7)? (b) What share of our task classes can be encoded at acceptable cost? (c) Does the solver check beat sampled tests? Evidence: encodability counts and agreement with ground truth.

**2. Non-monotonic reasoning.** Questions: (a) How do default rules with exceptions map to lessons in memory? (b) Which formalism (default logic, circumscription) gives a simple retract-on-conflict rule code can apply? Evidence: toy tasks with exceptions, retraction logs.

**3. Paraconsistent reasoning.** Question: does holding two conflicting candidates active, without discarding either, help at an impasse versus forcing one? Evidence: runs where early candidates conflict.

## Purely conceptual

Debates over the one right logic, the philosophy of logical consequence, and metatheory (compactness, Lowenheim-Skolem) give no step for our agent. Modal logic of knowledge is mostly descriptive.

## Sources

1. https://plato.stanford.edu/entries/logic-classical/ [V]
2. Reiter (1980), "A logic for default reasoning" [M]
3. Priest, *In Contradiction* (1987) [M]
4. Muggleton (1991), "Inductive logic programming" [M]
5. de Moura and Bjorner (2008), "Z3: an efficient SMT solver" [M]
