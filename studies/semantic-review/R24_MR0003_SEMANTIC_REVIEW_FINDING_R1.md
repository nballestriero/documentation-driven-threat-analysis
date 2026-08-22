# R24 MR-0003 semantic-review finding — R1

**Status:** WORKING RESEARCH EVIDENCE / NOT PROJECT AUTHORITY
**Reviewed repository baseline:** `fa8f5affe29143764230e43ec52514bf7f3ee8df`
**Affected authority baseline:** `FACIAL-ACCESS-GOV-R1`
**Primary purpose:** preserve what was found in the superseded MR-0003, how it was found, and which methodological hypotheses are justified for later thesis writing.

## 1. Scope

This record concerns one material semantic ambiguity in the former current-governed MR-0003 and the review procedure that exposed it.

It does not introduce confidence scores, thresholds, biometric-quality semantics, a new BA operator, a new BAE family, or a general problem-pattern classifier.

## 2. Former wording under review

The superseded MR-0003 stated:

> Consentire al processo di accesso di stabilire se la persona presente al punto di accesso corrisponde a un'identità governata [...]

The R24 working documentation later used the stronger wording:

> stabilire a quale `GovernedIdentity` corrisponde `PersonAtAccessPoint`

That wording reduced the ambiguity but still relied on a subtle linguistic distinction and did not state the entry-state fact explicitly.

## 3. Material ambiguity found

The former documentation did not explicitly govern whether a specific governed identity was already determined when the responsibility began.

Two materially different readings remained possible:

```text
A — identity not yet determined

person present
    ->
responsibility
    ->
determine which governed identity corresponds
```

```text
B — identity already selected

person present + specific governed identity
    ->
responsibility
    ->
determine whether they correspond
```

The difference is material because it changes the semantic entry state and the role played by the specific governed identity.

## 4. Smallest critical proposition

The smallest proposition separating the two readings was:

> A specific `GovernedIdentity` is already available/selected as the reference before the responsibility begins.

Evidence review against the then-current governed corpus produced:

```text
AFFIRMED       no
DENIED         no
CONFLICTING    no
NOT SPECIFIED  yes
```

The project clarification then established the intended meaning:

```text
specific GovernedIdentity already selected at entry  -> DENIED
responsibility determines which GovernedIdentity     -> AFFIRMED
```

This clarification is project meaning supplied through governance discussion, not a conclusion imported from the labels `identification` or `verification`.

## 5. How the ambiguity was found

The review path was:

```text
1. label/pattern suspicion
   "verification" might anchor the reviewer

2. neutral-label review
   temporarily remove semantic authority from suggestive names

3. competing readings
   construct the smallest materially different interpretations

4. materiality test
   ask whether the readings change responsibility/state/relations

5. critical-difference extraction
   isolate the smallest proposition on which the readings differ

6. governed-evidence check
   classify evidence as AFFIRMED / DENIED / NOT SPECIFIED / CONFLICTING

7. project clarification
   govern the missing project fact instead of inferring it

8. post-BA structural hypothesis
   ask whether BA can preserve and expose the same distinction
```

## 6. Controlled BA-topology pressure test

A controlled test was performed before deriving a real accepted BA.

If graph comparison keeps only untyped connectivity, both readings can collapse to the same apparent topology.

If BA semantics preserve proposition operator and participation roles, the distinction can remain visible.

Illustrative controlled shapes:

```text
A
produce
  input  -> PERSON
  result -> IDENTITY
  result -> EVIDENCE
```

```text
B
produce
  input  -> PERSON
  input  -> IDENTITY
  result -> EVIDENCE
```

Therefore:

```text
plain graph connectivity           -> insufficient in this controlled case
role-aware BA semantic topology    -> distinguishes the controlled readings
```

This is not yet a general theorem and does not establish that `produce` is the final accepted proposition for the corrected MR. It is a falsification-oriented structural experiment.

## 7. Diagnostic consequence

A future post-BA regression may compare a role-aware BA semantic graph projection with the stable responsibility established by governed documentation.

A mismatch is a review trigger, not project authority.

Possible diagnoses include:

```text
documentation ambiguity
BA derivation error
missing governed fact
BA expressiveness problem
```

A BA expressiveness problem must not be reported automatically as a documentation defect.

## 8. What was not found

This review did not show that identity determination, authorization, and access decision were all fused into one responsibility.

The defect found is narrower:

> MR-0003 did not stabilize sufficiently that the specific governed identity is not yet determined at the beginning of the responsibility.

The existing decomposition already intended authorization and access decision to remain separate concerns.

## 9. Minimality boundary

The review intentionally does not introduce:

```text
confidence
score
threshold
1:N terminology
new BAReferent
new BA operator
new Decision
new FunctionalRequirement
```

The purpose of semantic sufficiency review is to add the smallest governed fact needed to stabilize meaning, not to make the documentation semantically exhaustive.

## 10. Thesis carry-forward notes

### 10.1 Authoring markers versus final prose

Temporary markers such as `*<...>`, `#<...>`, and `@<...>` are authoring/review bindings, not intended final-document syntax.

The final project documentation should remain fluent human-readable prose.

### 10.2 Controlled lexical realization

A recurring semantic identity should have a stable governed human term across the documentation while still allowing grammatical variation.

Example:

```text
stable semantic identity: GovernedIdentity
preferred human term:     identità governata

allowed grammatical variation:
  l'identità governata
  dell'identità governata
  alle identità governate

uncontrolled synonym drift to avoid:
  identità registrata
  profilo identitario
  soggetto censito
```

The same principle applies to BA semantic operators. `produce` is a BA2 operator; grammatical realization may vary (`produrre`, `produce`, `viene prodotto`) without silently replacing it with a different BA operator such as `create`.

This discipline primarily protects human semantic stability. A secondary future benefit is easier automated/LLM interpretation because less synonym/coreference reconciliation is required.

### 10.3 Candidate future evaluation

A possible secondary evaluation is terminological round-trip stability:

```text
known authoring bindings
    ->
marker-free controlled prose
    ->
human / LLM reconstruction
    ->
same semantic identities/operators recovered?
```

This is a future-tooling implication, not a current DDTA authority rule.

### 10.4 Role-aware BA semantic topology

Candidate thesis impact:

> Role-aware BA semantic topology may support post-BA diagnostic comparison of recurring problem motifs.

Current status:

```text
PROMISING / ONE CONTROLLED CASE
NOT YET GENERALIZED
NOT PROJECT CLASSIFICATION AUTHORITY
```

## 11. Immediate next review target

Before any R2 promotion or accepted BA derivation:

1. review `D-3.1` and `D-3.2` against the corrected MR meaning;
2. review `FR-3.2.1` against the corrected MR meaning;
3. check whether any downstream artifact silently assumes a preselected `GovernedIdentity`;
4. only then decide whether a coherent new governed facial-access baseline can be promoted.
