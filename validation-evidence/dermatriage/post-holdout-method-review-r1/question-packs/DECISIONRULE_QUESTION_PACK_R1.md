# OP-14 `decisionRule` Question Pack R1

Use this pack for source-grounded review of `decisionRule`. The questions do not create project truth.

| Q | Question | DermaTriage review result |
|---|---|---|
| Q1 | Is a governed actor identifiable without invention? | PASS |
| Q2 | Are one or more governed inputs identifiable? | STRONG PASS |
| Q3 | Is one governed result identifiable independently of the rule syntax? | STRONG PASS |
| Q4 | Does the source actually map conditions/inputs to that result? | STRONG PASS |
| Q5 | Is every actor/input/result/condition source-grounded or necessarily derivable? | STRONG PASS |
| Q6 | Would the meaning be better represented as a reusable `constrain` restriction? | DISTINCT |
| Q7 | Is the consequent a result assignment rather than merely an action/behavior? | STRONG BOUNDARY |
| Q8 | Is a threshold acting as a trigger rather than selecting a result value? | TRIGGER DISTINCT |
| Q9 | Can the rule be represented with equality/not-equality only? | SOMETIMES |
| Q10 | Does it require ordered/scalar comparison? | YES; PRESSURE CONFIRMED |
| Q11 | Does the source require conjunction of conditions? | YES; STRONG EVIDENCE |
| Q12 | Does the source name a condition without governing its internal property model? | RELEVANT; CL-02 REVIEW PENDING |
| Q13 | Does the source govern an ELSE/otherwise branch? | YES in P-scale mapping |
| Q14 | Is a negative statement really local negation, or only non-sufficiency/non-implication? | DISTINCT |
| Q15 | Is applicability/path/phase/reference scope preserved? | PRESSURE CONFIRMED |
| Q16 | Does the mapping require ranking/argmax/bounded selection beyond simple comparison? | PRESSURE PRESENT |
| Q17 | Are multiple possible values values of one result rather than multiple result roles? | YES; KEEP result [1] |
| Q18 | If OP-14 is deleted, can other constructs reconstruct the governed result mapping? | NO; REDUNDANCY FALSIFIED |
| Q19 | Does OP-14 enable useful deterministic decision/rule projections? | STRONG PASS |
| Q20 | Does final admission avoid invented actor, input, result, condition or automaticity? | PASS WITH GATE |

## Stopping rule

Do not complete a `decisionRule` proposition by inventing a result just because the documentation contains a conditional action.
Do not translate capability/support requirements into automatic result/action rules.
Do not translate `A MUST NOT imply B` into `IF A THEN NOT B` unless the source actually governs that logic.

## Minimality test

Before proposing a new primitive, test whether the observed meaning is representable as:

1. an OP-14 instance;
2. an extension of controlled local condition vocabulary;
3. a kind/value within an existing construct;
4. a composition of propositions;
5. a deterministic projection.

Escalate only if material governed meaning would otherwise be lost.
