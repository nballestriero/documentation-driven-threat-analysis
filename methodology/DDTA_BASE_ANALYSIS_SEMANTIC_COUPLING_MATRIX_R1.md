# DDTA Base Analysis — Semantic Coupling Matrix R1

## Status

`R40 COMPANION / NON-NORMATIVE / DERIVED FROM R4 CANDIDATE R3`

This matrix is a review/learning aid. It does not add operators to BA2 R3 and does not promote R25 candidates.

| Intuitive pattern | Governed meaning | Operator / composition | Boundary |
|---|---|---|---|
| Provider — Service — Consumer | consumer actually uses a capability/service | `consumeService`; `provider` optional when governed | provider identity does not automatically imply independent `provideService` semantics |
| Service Provider — Service | provider-service relation exists independently of a consumer | `provideService` **CANDIDATE / NOT_ADMITTED** | do not use as current operator before formal admission |
| Producer — Result | actor makes a result available | `produce` | no destination, consumer, transfer or new identity implied |
| Producer — Result — Consumer | A produces X; B actually uses X in an operation | `produce(A,X)` + X as `input` in B's proposition | no generic current `consumeData`; CC-01 was rejected redundant in tested scope |
| Sender — Content — Receiver | explicit source-to-destination conveyance | `transfer` | no service consumption, success or protocol implied |
| API / Endpoint — Client | client initiates/invokes a capability | `initiate` **CANDIDATE**; possibly `consumeService` for actual service use | separate initiation, service use, payload transfer, auth constraints |
| API — Request/Response — Client | governed request/response content crosses boundary | `transfer`; `correlate` for same-request binding | endpoint presence alone is not transfer |
| Client — Protected API | access/use constrained by governed credential/mechanism | `constrain` + the proposition describing the actual action | constraint is not the authentication execution itself |
| Initiator — Process/Operation | one party starts an operation/process | `initiate` **CANDIDATE / NOT_ADMITTED** | no success, completion, transfer or service consumption implied |
| Observer — Existing State/Data | explicit read/query/inspection | `observe` | selection membership is separate |
| Selector — Candidate Population — Selected Result | governed choice among candidates | local `selection` structure **NON-NORMATIVE** | ranking, bound, recency, selection are distinct |
| Classifier — Referent — Kind | category/kind assignment | `classify` | not selection, lifecycle transition or generic property assignment |
| Decision Actor — Inputs — Result | governed mapping conditions/input to result | `decisionRule` + condition language | allowed domain or conditional action alone is not enough |
| Responsible Party — Scope — Responsibility Kind | explicit responsibility/authority assignment | `assignResponsibility` | actor/provider/producer do not become responsible party by default |
| Abstract Capability — Concrete Realization | concrete element materializes abstract meaning | `realize` | not perform/execute and not responsibility assignment |
| Dependent — Prerequisite | prerequisite semantics | `dependOn` | temporal/pipeline order alone is insufficient |
| Referencer — Referenced Target | directional reference without stronger binding | `reference` | use `correlate` when same-case/request identity must be preserved |
| Item(s) — Same Context | same-request/case/evaluation binding | `correlate` | not generic association |
| Subject — From/To State | same identity changes governed state/lifecycle | `transition` | version selection, property update and rollback support are insufficient alone |
| Actor — New Item/Occurrence | new project-semantic identity/occurrence is established | `create` | not output production or persistence |
| Target — Restriction/Domain | governed reusable/queryable restriction | `constrain` | local condition, selection bound and decision mapping remain distinct |
| Stored Item — Store | independent at-rest association | `storedIn` **CANDIDATE / NOT_ADMITTED** | not current BA2 operator |
| Pipeline Stage A — Stage B | membership/order among stages | **OPEN local composition question** | `precedes != dependOn != transfer != initiate` |

## Three recurring coupling rules

### Producer and consumer

```text
A produces X
    -> produce(A, X)

B uses X to perform/decide/produce Y
    -> X is an input role in B's proposition

NOT AUTOMATICALLY
    consumeData(B, X)
```

### Service provider and consumer

```text
consumer uses service
    -> consumeService

provider is governed
    -> optional provider role may be present

provider-service relation must exist independently
    -> provideService candidate pressure
    -> NOT CURRENT until admitted
```

### API and client

```text
client invokes API/process
    -> initiate candidate, if initiation semantics are material

client consumes capability as service
    -> consumeService

request/response payload crosses boundary
    -> transfer

request must stay bound to response/case
    -> correlate

authentication requirement constrains use
    -> constrain
```

There is therefore no safe rule of the form `API + client = one operator`.
